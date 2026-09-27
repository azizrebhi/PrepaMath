"""
Lists ingested structural units grouped by chunk_type, to speed up curating
more dataset.json entries without re-reading the source .md by hand.

Usage:
    uv run python evaluation/build_candidates.py "Réduction des endomorphismes"
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from sqlalchemy import select

from app.database import async_session_maker
from app.model import DocumentParentChunk
from evaluation.common import resolve_document_id


async def main(document_title: str) -> int:
    async with async_session_maker() as session:
        document_id = await resolve_document_id(session, document_title)
        if document_id is None:
            print(f"No document titled {document_title!r} found.")
            return 1

        rows = (
            await session.execute(
                select(
                    DocumentParentChunk.chunk_type,
                    DocumentParentChunk.number,
                    DocumentParentChunk.parent_index,
                    DocumentParentChunk.content,
                )
                .where(DocumentParentChunk.document_id == document_id)
                .order_by(DocumentParentChunk.chunk_type, DocumentParentChunk.parent_index)
            )
        ).all()

        by_type: dict[str, list] = {}
        for row in rows:
            by_type.setdefault(row.chunk_type, []).append(row)

        for chunk_type, items in sorted(by_type.items()):
            print(f"\n=== {chunk_type} ({len(items)} units) ===")
            for row in items:
                label = f"{chunk_type} {row.number}" if row.number else chunk_type
                preview = row.content.replace("\n", " ")[:100]
                print(f"  [parent_index={row.parent_index}] {label}: {preview}...")

    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: uv run python evaluation/build_candidates.py "<document title>"')
        sys.exit(1)
    sys.exit(asyncio.run(main(sys.argv[1])))
