"""
Computes per-stage recall@k / MRR and a per-query failure attribution from
the raw traces written by run_retrieval_eval.py.

Usage:
    uv run python evaluation/metrics.py results/hybrid.json
    uv run python evaluation/metrics.py results/dense.json results/hybrid.json results/reranked.json
"""

import json
import sys
from pathlib import Path

K_VALUES = (1, 3, 5, 10)
RANK_STAGES = ["lexical", "dense", "rrf", "rerank"]


def best_rank(candidates: list[dict], gt: set[int], rank_field: str) -> int | None:
    ranks = [
        c[rank_field]
        for c in candidates
        if c["parent_index"] in gt and c[rank_field] is not None
    ]
    return min(ranks) if ranks else None


def final_rank(final_parent_indices_ordered: list[int], gt: set[int]) -> int | None:
    for i, pid in enumerate(final_parent_indices_ordered, start=1):
        if pid in gt:
            return i
    return None


def attribute_failure(query: dict, stages_present: dict[str, bool], limit: int) -> str:
    gt = set(query["ground_truth_parent_indices"])
    if not gt:
        return "ingestion_gap" if query["unresolved_ground_truth"] else "no_ground_truth"

    ranks = {
        stage: best_rank(query["candidates"], gt, f"{stage}_rank")
        for stage in RANK_STAGES
        if stages_present.get(stage)
    }
    fr = final_rank(query["final_parent_indices_ordered"], gt)

    if fr is not None:
        label = "found" if fr <= limit else "found_beyond_limit"  # shouldn't happen, defensive
    elif not any(ranks.get(s) is not None for s in ("dense", "lexical")):
        label = "missed_by_retrieval"
    elif stages_present.get("rrf") and ranks.get("rrf") is None:
        label = "lost_in_rrf_fusion"
    elif stages_present.get("rerank") and ranks.get("rerank") is None:
        label = "lost_in_rerank"  # structurally shouldn't occur; flagged if it does
    else:
        last_rank = ranks.get("rerank") or ranks.get("rrf")
        label = "cut_by_limit" if last_rank and last_rank > limit else "lost_in_parent_dedup"

    if query["unresolved_ground_truth"]:
        label += "+partial_ingestion_gap"
    return label


def compute_stage_metrics(queries: list[dict], stages_present: dict[str, bool]) -> dict:
    evaluable = [q for q in queries if q["ground_truth_parent_indices"]]
    n = len(evaluable)
    metrics = {"n_evaluable": n, "n_total": len(queries)}

    stages = [s for s in RANK_STAGES if stages_present.get(s)] + ["final"]
    for stage in stages:
        rrs = []
        hits_at_k = {k: 0 for k in K_VALUES}
        for q in evaluable:
            gt = set(q["ground_truth_parent_indices"])
            if stage == "final":
                r = final_rank(q["final_parent_indices_ordered"], gt)
            else:
                r = best_rank(q["candidates"], gt, f"{stage}_rank")
            rrs.append(1.0 / r if r else 0.0)
            for k in K_VALUES:
                if r is not None and r <= k:
                    hits_at_k[k] += 1
        metrics[stage] = {
            "mrr": round(sum(rrs) / n, 4) if n else None,
            **{f"recall@{k}": round(hits_at_k[k] / n, 4) if n else None for k in K_VALUES},
        }
    return metrics


def run(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    manifest = data["manifest"]
    queries = data["queries"]
    stages_present = {
        "lexical": manifest.get("use_lexical", False),
        "dense": manifest.get("use_semantic", False),
        "rrf": True,
        "rerank": manifest.get("use_rerank", False),
    }
    limit = manifest["limit"]

    print(f"\n=== {manifest['config']} (limit={limit}, commit={manifest.get('git_commit')}) ===")

    attributions = {}
    for q in queries:
        label = attribute_failure(q, stages_present, limit)
        attributions[label] = attributions.get(label, 0) + 1
        marker = "OK " if label.startswith("found") else "FAIL"
        print(f"  [{marker}] {q['id']:5s} ({q['category']:>18s}): {label}")

    print("\n  Attribution summary:")
    for label, count in sorted(attributions.items(), key=lambda x: -x[1]):
        print(f"    {label:35s} {count}")

    stage_metrics = compute_stage_metrics(queries, stages_present)
    print(f"\n  Evaluable queries: {stage_metrics['n_evaluable']}/{stage_metrics['n_total']}")
    for stage in [s for s in RANK_STAGES if stages_present.get(s)] + ["final"]:
        m = stage_metrics[stage]
        recalls = ", ".join(f"R@{k}={m[f'recall@{k}']}" for k in K_VALUES)
        print(f"    {stage:8s} MRR={m['mrr']}  {recalls}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: uv run python evaluation/metrics.py <results.json> [more.json ...]")
        sys.exit(1)
    for arg in sys.argv[1:]:
        run(Path(arg))
