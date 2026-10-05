"""
Runs evaluation/routing_cases.json through the real classify_route() function
(app/services/tutor_graph.py) — the same routing logic production uses, called
directly rather than through the full graph, since these cases only test
routing and don't need retrieval/generation to run.

"ambiguous" cases are scored separately and excluded from the accuracy number,
by design (see routing_cases.json's schema notes) — forcing a single answer
on a genuinely dual-valid case would corrupt the metric, not strengthen it.

Usage:
    uv run python evaluation/run_routing_eval.py
"""

import asyncio
import json
import os
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dotenv import load_dotenv
from openai import AsyncOpenAI

from app.database import async_session_maker
from app.services.tutor_graph import classify_route
from evaluation.common import resolve_chunk_ref, resolve_document_id

load_dotenv()

CASES_PATH = Path(__file__).parent / "routing_cases.json"
RESULTS_DIR = Path(__file__).parent / "results"


def git_commit() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True
        ).strip()
    except Exception:
        return None


async def run_case(session, client: AsyncOpenAI, case: dict, doc_id_cache: dict) -> dict:
    title = case["document_title"]
    if title not in doc_id_cache:
        resolved_id = await resolve_document_id(session, title)
        if resolved_id is None:
            raise RuntimeError(f"document_title {title!r} not found — ingest it first.")
        doc_id_cache[title] = resolved_id
    document_id = doc_id_cache[title]

    disp = case["displayed"]
    ref = await resolve_chunk_ref(session, document_id, disp["chunk_type"], disp.get("number"))
    if ref.content is None:
        return {**case, "error": f"displayed chunk not found: {disp}"}

    decision = await classify_route(client, ref.content, case["query"])
    predicted = decision["route"]
    expected = case["expected_route"]
    correct = (predicted == expected) if expected != "ambiguous" else None

    return {
        "id": case["id"],
        "category": case["category"],
        "query": case["query"],
        "expected_route": expected,
        "predicted_route": predicted,
        "correct": correct,
        "prompt_tokens": decision["prompt_tokens"],
        "completion_tokens": decision["completion_tokens"],
        "notes": case.get("notes"),
    }


async def main() -> None:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))["cases"]
    client = AsyncOpenAI(api_key=os.getenv("OPEN_AI_KEY"))
    doc_id_cache: dict[str, str] = {}

    results = []
    async with async_session_maker() as session:
        for case in cases:
            r = await run_case(session, client, case, doc_id_cache)
            results.append(r)
            tag = "ambiguous" if r.get("correct") is None else ("PASS" if r["correct"] else "FAIL")
            print(f"  [{tag:9}] {r['id']} ({r['category']}): expected={r['expected_route']} got={r['predicted_route']}")

    scored = [r for r in results if r.get("correct") is not None]
    n_correct = sum(1 for r in scored if r["correct"])
    accuracy = n_correct / len(scored) if scored else 0.0

    confusion = defaultdict(int)
    for r in scored:
        confusion[(r["expected_route"], r["predicted_route"])] += 1

    by_category = defaultdict(lambda: {"correct": 0, "total": 0})
    for r in scored:
        by_category[r["category"]]["total"] += 1
        by_category[r["category"]]["correct"] += int(r["correct"])

    followup_case = next((r for r in results if r["category"] == "followup_needs_history"), None)

    summary = {
        "manifest": {
            "git_commit": git_commit(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "cases_path": str(CASES_PATH),
            "num_cases": len(cases),
            "num_scored": len(scored),
            "num_ambiguous_excluded": len(results) - len(scored),
        },
        "accuracy": accuracy,
        "n_correct": n_correct,
        "n_scored": len(scored),
        "confusion_matrix": {f"expected={e},predicted={p}": c for (e, p), c in confusion.items()},
        "by_category": dict(by_category),
        "results": results,
    }

    RESULTS_DIR.mkdir(exist_ok=True)
    out_path = RESULTS_DIR / "routing_eval.json"
    out_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n=== Routing eval: {n_correct}/{len(scored)} correct ({accuracy:.1%}) ===")
    print(f"Excluded as ambiguous: {len(results) - len(scored)}")
    print("\nConfusion matrix (expected -> predicted):")
    for (e, p), c in confusion.items():
        print(f"  {e:8} -> {p:8} : {c}")
    print("\nBy category:")
    for cat, stats in by_category.items():
        print(f"  {cat:35} {stats['correct']}/{stats['total']}")
    if followup_case:
        tag = "matched expected label anyway" if followup_case["correct"] else "did NOT match expected label"
        print(f"\nNote — followup_needs_history ({followup_case['id']}): {tag}.")
        print("This case's result isn't a real pass/fail on routing quality — classify_route")
        print("never receives conversation history, so it can't actually know what the")
        print("question's pronoun refers to. See routing_cases.json's notes for this case.")
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    asyncio.run(main())
