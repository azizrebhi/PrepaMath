"""
Validates evaluation/dataset.json against whatever is currently ingested.

Every relevant_chunks entry is resolved by (chunk_type, number) against the
live DB. Entries marked expected_ingestion_gap=true are reported separately
from real dataset errors — they're deliberate probes of the known
unnumbered Exemple/Remarque overwrite bug in task.py, and are *expected* to
fail to resolve until that bug is fixed and the chapter is re-ingested.

Usage:
    uv run python evaluation/validate_dataset.py
"""

import asyncio
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.database import async_session_maker
from evaluation.common import resolve_chunk_ref, resolve_document_id

DATASET_PATH = Path(__file__).parent / "dataset.json"


async def main() -> int:
    dataset = json.loads(DATASET_PATH.read_text(encoding="utf-8"))

    unexpected_failures = []
    expected_gaps = []
    snippet_mismatches = []
    ok_count = 0

    doc_id_cache: dict[str, str | None] = {}

    async with async_session_maker() as session:
        for q in dataset["questions"]:
            title = q["document_title"]
            if title not in doc_id_cache:
                doc_id_cache[title] = await resolve_document_id(session, title)
            document_id = doc_id_cache[title]
            if document_id is None:
                print(f"FATAL: document_title {title!r} (question {q['id']}) not found in DB. "
                      f"Has it been ingested?")
                return 1

            expected_gap = q.get("expected_ingestion_gap", False)
            snippet = q.get("content_snippet")

            for ref in q["relevant_chunks"]:
                resolved = await resolve_chunk_ref(
                    session, document_id, ref["chunk_type"], ref.get("number"),
                    content_snippet=snippet,
                )

                if resolved.parent_index is None:
                    entry = (q["id"], ref["chunk_type"], ref.get("number"))
                    if expected_gap:
                        expected_gaps.append(entry)
                    else:
                        unexpected_failures.append(entry)
                    continue

                ok_count += 1
                if snippet and resolved.content and snippet not in resolved.content:
                    snippet_mismatches.append(
                        (q["id"], ref["chunk_type"], ref.get("number"), resolved.parent_index)
                    )

    print(f"Resolved OK: {ok_count}")
    print(f"Expected ingestion-gap failures (probes working as intended): {len(expected_gaps)}")
    for entry in expected_gaps:
        print(f"  - {entry}")

    if snippet_mismatches:
        print(f"\nSnippet mismatches (resolved, but content_snippet not found — check for drift): "
              f"{len(snippet_mismatches)}")
        for entry in snippet_mismatches:
            print(f"  - {entry}")

    if unexpected_failures:
        print(f"\nUNEXPECTED failures (not marked expected_ingestion_gap): {len(unexpected_failures)}")
        for entry in unexpected_failures:
            print(f"  - {entry}")
        return 1

    print("\nDataset valid.")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
