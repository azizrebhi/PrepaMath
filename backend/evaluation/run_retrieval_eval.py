"""
Runs the curated dataset through the shared retrieval pipeline
(app/services/retrieval_pipeline.py) under three configs — dense-only,
hybrid (lexical+dense, no rerank), and full (hybrid+rerank) — and dumps a
full per-candidate trace for each query to evaluation/results/<config>.json.

This does NOT compute recall/MRR — see metrics.py for that. This script's
only job is to capture exactly what each pipeline stage produced, honestly,
so failures can be attributed to a specific stage after the fact.

Usage:
    uv run python evaluation/run_retrieval_eval.py [--limit 10]
"""

import argparse
import asyncio
import json
import os
import subprocess
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from dotenv import load_dotenv
from openai import AsyncOpenAI

from app.database import async_session_maker
from app.services.retrieval_pipeline import run_pipeline
from evaluation.common import resolve_chunk_ref, resolve_document_id

load_dotenv()

DATASET_PATH = Path(__file__).parent / "dataset.json"
RESULTS_DIR = Path(__file__).parent / "results"

CONFIGS = {
    "dense": {"use_lexical": False, "use_semantic": True, "use_rerank": False},
    "hybrid": {"use_lexical": True, "use_semantic": True, "use_rerank": False},
    "reranked": {"use_lexical": True, "use_semantic": True, "use_rerank": True},
}


def git_commit() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True
        ).strip()
    except Exception:
        return None


async def resolve_ground_truth(session, document_id: str, question: dict) -> tuple[list[int], list[dict]]:
    """Returns (resolved_parent_indices, unresolved_refs)."""
    resolved, unresolved = [], []
    snippet = question.get("content_snippet")
    for ref in question["relevant_chunks"]:
        r = await resolve_chunk_ref(
            session, document_id, ref["chunk_type"], ref.get("number"),
            content_snippet=snippet,
        )
        if r.parent_index is None:
            unresolved.append(ref)
        else:
            resolved.append(r.parent_index)
    return resolved, unresolved


async def run_config(config_name: str, flags: dict, limit: int, client: AsyncOpenAI, dataset: dict) -> dict:
    query_results = []
    doc_id_cache: dict[str, str] = {}

    async with async_session_maker() as session:
        for q in dataset["questions"]:
            title = q["document_title"]
            if title not in doc_id_cache:
                resolved_id = await resolve_document_id(session, title)
                if resolved_id is None:
                    raise RuntimeError(f"document_title {title!r} not found — ingest it first.")
                doc_id_cache[title] = resolved_id
            document_id = doc_id_cache[title]

            ground_truth, unresolved_gt = await resolve_ground_truth(session, document_id, q)

            result = await run_pipeline(
                query=q["query"],
                session=session,
                limit=limit,
                client=client,
                trace=True,
                **flags,
            )

            # Drop verbatim chunk text before it ever reaches disk — these
            # trace files get published alongside the benchmark writeup, and
            # `content` is copyrighted source-textbook text (sometimes a
            # full exercise/example, not just a snippet). Rank/score data is
            # all metrics.py or a reader needs to verify the numbers.
            candidates = [
                {k: v for k, v in asdict(c).items() if k != "content"}
                for c in result.candidates.values()
            ]
            # Rank-ordered (not deduped-into-a-set) — result.results already
            # reflects the final, one-per-parent, ranked output.
            final_parent_indices_ordered = [r.chunk_index for r in result.results]

            query_results.append({
                "id": q["id"],
                "document_title": title,
                "category": q.get("category"),
                "query": q["query"],
                "expected_ingestion_gap": q.get("expected_ingestion_gap", False),
                "ground_truth_parent_indices": ground_truth,
                "unresolved_ground_truth": unresolved_gt,
                "final_parent_indices_ordered": final_parent_indices_ordered,
                "candidates": candidates,
            })

    return {
        "manifest": {
            "config": config_name,
            **flags,
            "limit": limit,
            "git_commit": git_commit(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "dataset_path": str(DATASET_PATH),
            "num_questions": len(dataset["questions"]),
        },
        "queries": query_results,
    }


async def main(limit: int) -> None:
    dataset = json.loads(DATASET_PATH.read_text(encoding="utf-8"))
    client = AsyncOpenAI(api_key=os.getenv("OPEN_AI_KEY"))

    RESULTS_DIR.mkdir(exist_ok=True)
    experiments_path = RESULTS_DIR / "experiments.json"
    experiments = json.loads(experiments_path.read_text(encoding="utf-8")) if experiments_path.exists() else []

    for config_name, flags in CONFIGS.items():
        print(f"Running config: {config_name} ({flags})")
        output = await run_config(config_name, flags, limit, client, dataset)

        out_path = RESULTS_DIR / f"{config_name}.json"
        out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  -> wrote {out_path}")

        experiments.append(output["manifest"])

    experiments_path.write_text(json.dumps(experiments, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nUpdated {experiments_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    asyncio.run(main(args.limit))
