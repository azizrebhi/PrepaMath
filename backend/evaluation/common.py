"""Shared helpers for the evaluation harness: resolving dataset entries
(document title, chunk_type/number) against whatever is currently in the
database, so dataset.json survives re-ingestion (which assigns fresh UUIDs
and fresh parent_index values every run) instead of hardcoding either."""

from dataclasses import dataclass

from sqlalchemy import select

from app.model import Document, DocumentParentChunk


@dataclass
class ResolvedChunkRef:
    chunk_type: str
    number: str | None
    parent_index: int | None  # None if not found in the current DB
    parent_id: str | None
    content: str | None = None
    part_id: str | None = None


async def resolve_document_id(session, document_title: str) -> str | None:
    row = (
        await session.execute(
            select(Document.id).where(Document.title == document_title)
        )
    ).first()
    return str(row.id) if row else None


async def resolve_chunk_ref(
    session,
    document_id: str,
    chunk_type: str,
    number: str | None,
    content_snippet: str | None = None,
) -> ResolvedChunkRef:
    """Resolves a (chunk_type, number) ref to its current parent_index.

    When number is None, (chunk_type, number) is NOT necessarily unique —
    a chapter can legitimately have many distinct unnumbered Exemple/Remarque
    blocks (that ambiguity is exactly what the old ingestion collision bug
    used to hide by collapsing them all into one). In that case a
    content_snippet is required to disambiguate; without one, or if none of
    the candidates contain it, this returns not-found rather than guessing.
    """
    rows = (
        await session.execute(
            select(
                DocumentParentChunk.id,
                DocumentParentChunk.parent_index,
                DocumentParentChunk.content,
                DocumentParentChunk.part_id,
            )
            .where(
                DocumentParentChunk.document_id == document_id,
                DocumentParentChunk.chunk_type == chunk_type,
                DocumentParentChunk.number == number,
            )
        )
    ).all()

    if not rows:
        return ResolvedChunkRef(chunk_type, number, None, None)

    if len(rows) > 1 or (number is None and content_snippet):
        if not content_snippet:
            return ResolvedChunkRef(chunk_type, number, None, None)
        matches = [r for r in rows if content_snippet in r.content]
        if len(matches) != 1:
            return ResolvedChunkRef(chunk_type, number, None, None)
        row = matches[0]
    else:
        row = rows[0]

    return ResolvedChunkRef(
        chunk_type, number, row.parent_index, str(row.id), row.content,
        str(row.part_id) if row.part_id else None,
    )
