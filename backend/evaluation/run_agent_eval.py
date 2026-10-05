"""
Runs evaluation/dataset.json end-to-end through the real tutor graph
(build_tutor_graph in app/services/tutor_graph.py) — same code path as
production's /ask — recording two independent things per question:

  1. Routing: does the real route match expected_route (added to dataset.json
     under the canonical assumption that the student is viewing the chunk(s)
     that answer the question)?
  2. Answer quality: a RAGAS-style judge (gpt-4o — deliberately a different,
     stronger model than the gpt-4o-mini that generates, to avoid self-grading
     bias) scores faithfulness and answer relevancy against the context the
     graph actually retrieved.

These two are kept as separate fields per question, never blended into one
score — a wrong route doesn't necessarily mean a bad answer (corpus search is
still real search over the real document), and a right route can still
produce a bad answer. Collapsing them would erase that distinction.

A cheap deterministic check (not LLM-judged) also verifies the LaTeX-syntax
rule from the system prompt: never \\( \\) or \\[ \\].

Usage:
    uv run python evaluation/run_agent_eval.py [--limit N]
"""

import argparse
import asyncio
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dotenv import load_dotenv
from openai import AsyncOpenAI

from app.database import async_session_maker
from app.services.tutor_graph import build_tutor_graph
from evaluation.common import resolve_chunk_ref, resolve_document_id

load_dotenv()

DATASET_PATH = Path(__file__).parent / "dataset.json"
RESULTS_DIR = Path(__file__).parent / "results"
JUDGE_MODEL = "gpt-4o"

FORBIDDEN_LATEX = re.compile(r"\\\(|\\\)|\\\[|\\\]")


def git_commit() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True
        ).strip()
    except Exception:
        return None


async def judge_answer(client: AsyncOpenAI, question: str, context: str, answer: str) -> dict:
    prompt = (
        "Tu es un correcteur expert de mathématiques de classe préparatoire. "
        "Évalue la réponse d'un tuteur IA selon deux critères indépendants, "
        "en te basant UNIQUEMENT sur le contexte fourni — pas sur tes propres "
        "connaissances en mathématiques.\n\n"
        "1. faithfulness (1-5) : chaque affirmation de la réponse est-elle "
        "réellement soutenue par le contexte ? 5 = tout est soutenu par le "
        "contexte. 1 = la réponse invente ou contredit le contexte.\n"
        "2. answer_relevancy (1-5) : la réponse traite-t-elle réellement la "
        "question posée (ni hors-sujet, ni évasive) ? 5 = répond précisément "
        "à la question. 1 = ne répond pas à la question posée.\n\n"
        f"Contexte fourni au tuteur :\n{context}\n\n"
        f"Question de l'étudiant :\n{question}\n\n"
        f"Réponse du tuteur à évaluer :\n{answer}\n\n"
        "Donne une justification brève (une phrase) pour chaque score."
    )
    completion = await client.chat.completions.create(
        model=JUDGE_MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "judgment",
                "schema": {
                    "type": "object",
                    "properties": {
                        "faithfulness": {"type": "integer", "minimum": 1, "maximum": 5},
                        "faithfulness_reason": {"type": "string"},
                        "answer_relevancy": {"type": "integer", "minimum": 1, "maximum": 5},
                        "answer_relevancy_reason": {"type": "string"},
                    },
                    "required": [
                        "faithfulness", "faithfulness_reason",
                        "answer_relevancy", "answer_relevancy_reason",
                    ],
                    "additionalProperties": False,
                },
                "strict": True,
            },
        },
    )
    return json.loads(completion.choices[0].message.content)


async def run_question(session, client: AsyncOpenAI, q: dict, doc_id_cache: dict) -> dict:
    title = q["document_title"]
    if title not in doc_id_cache:
        resolved_id = await resolve_document_id(session, title)
        if resolved_id is None:
            raise RuntimeError(f"document_title {title!r} not found — ingest it first.")
        doc_id_cache[title] = resolved_id
    document_id = doc_id_cache[title]

    # Canonical assumption (see dataset.json's schema notes): the student is
    # viewing the first listed relevant chunk when asking. For multi_context
    # questions this is deliberately only ONE of the two needed chunks — the
    # whole point of those cases is that the displayed lesson alone is
    # incomplete.
    primary_ref = q["relevant_chunks"][0]
    ref = await resolve_chunk_ref(
        session, document_id, primary_ref["chunk_type"], primary_ref.get("number"),
        content_snippet=q.get("content_snippet"),
    )
    if ref.parent_id is None:
        return {**q, "error": f"could not resolve displayed chunk: {primary_ref}"}

    graph = build_tutor_graph(session, client)
    result = await graph.ainvoke({
        "question": q["query"],
        "document_id": document_id,
        "part_id": ref.part_id,
        "lesson_chunk_ids": [ref.parent_id],
        "lesson_content": "",
        "rest_of_section_content": "",
        "route": "",
        "context": "",
        "answer": "",
        "history": [],
        "prompt_tokens": 0,
        "completion_tokens": 0,
    })

    full_context = "\n\n---\n\n".join(
        part for part in [result["lesson_content"], result["rest_of_section_content"], result["context"]] if part
    )
    judgment = await judge_answer(client, q["query"], full_context, result["answer"])
    latex_violation = bool(FORBIDDEN_LATEX.search(result["answer"]))

    expected_route = q.get("expected_route")
    route_correct = (result["route"] == expected_route) if expected_route else None

    return {
        "id": q["id"],
        "category": q.get("category"),
        "query": q["query"],
        "expected_route": expected_route,
        "actual_route": result["route"],
        "route_correct": route_correct,
        "faithfulness": judgment["faithfulness"],
        "faithfulness_reason": judgment["faithfulness_reason"],
        "answer_relevancy": judgment["answer_relevancy"],
        "answer_relevancy_reason": judgment["answer_relevancy_reason"],
        "latex_violation": latex_violation,
        "prompt_tokens": result["prompt_tokens"],
        "completion_tokens": result["completion_tokens"],
        "answer": result["answer"],
    }


async def main(limit: int | None) -> None:
    dataset = json.loads(DATASET_PATH.read_text(encoding="utf-8"))
    questions = dataset["questions"][:limit] if limit else dataset["questions"]
    client = AsyncOpenAI(api_key=os.getenv("OPEN_AI_KEY"))
    doc_id_cache: dict[str, str] = {}

    results = []
    async with async_session_maker() as session:
        for q in questions:
            r = await run_question(session, client, q, doc_id_cache)
            results.append(r)
            if "error" in r:
                print(f"  [ERROR] {r['id']}: {r['error']}")
            else:
                route_tag = "?" if r["route_correct"] is None else ("OK" if r["route_correct"] else "MISS")
                print(
                    f"  {r['id']} route={r['actual_route']:7} ({route_tag:4}) "
                    f"faithfulness={r['faithfulness']} relevancy={r['answer_relevancy']} "
                    f"latex_ok={not r['latex_violation']}"
                )

    valid = [r for r in results if "error" not in r]
    routed = [r for r in valid if r["route_correct"] is not None]
    route_accuracy = sum(1 for r in routed if r["route_correct"]) / len(routed) if routed else None
    avg_faithfulness = sum(r["faithfulness"] for r in valid) / len(valid) if valid else 0
    avg_relevancy = sum(r["answer_relevancy"] for r in valid) / len(valid) if valid else 0
    latex_violations = sum(1 for r in valid if r["latex_violation"])

    summary = {
        "manifest": {
            "git_commit": git_commit(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "judge_model": JUDGE_MODEL,
            "dataset_path": str(DATASET_PATH),
            "num_questions": len(questions),
            "num_errors": len(results) - len(valid),
        },
        "route_accuracy": route_accuracy,
        "avg_faithfulness": avg_faithfulness,
        "avg_answer_relevancy": avg_relevancy,
        "latex_violations": latex_violations,
        "results": results,
    }

    RESULTS_DIR.mkdir(exist_ok=True)
    out_path = RESULTS_DIR / "agent_eval.json"
    out_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n=== Agent eval over {len(valid)} questions ===")
    if route_accuracy is not None:
        print(f"Route accuracy: {sum(1 for r in routed if r['route_correct'])}/{len(routed)} ({route_accuracy:.1%})")
    print(f"Avg faithfulness: {avg_faithfulness:.2f}/5")
    print(f"Avg answer relevancy: {avg_relevancy:.2f}/5")
    print(f"LaTeX-syntax violations: {latex_violations}/{len(valid)}")
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()
    asyncio.run(main(args.limit))
