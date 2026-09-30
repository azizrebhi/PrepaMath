from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.auth import current_active_user

from app.database import get_async_session
from app.model import ChapterPart, Document, DocumentParentChunk, User
from app.schema import ChapterPartOut, DocumentOut, ChapterPartOutContent, DocumentParentChunkOut

router = APIRouter(
    prefix="/documents",
    tags=["chapters"],
)


@router.get("", response_model=list[DocumentOut])
async def list_documents(session: AsyncSession = Depends(get_async_session),
                         user: User = Depends(current_active_user)):
    """All ingested chapters — the roadmap/landing-page navigation source.

    Document ids change every re-ingestion (task.py assigns a fresh uuid4
    each run), so the frontend must always discover the current id here
    rather than hardcoding/bookmarking one.
    """
    documents = (
        await session.execute(select(Document).order_by(Document.created_at))
    ).scalars().all()
    return documents


@router.get("/{document_id}/parts", response_model=list[ChapterPartOut])
async def list_chapter_parts(
    document_id: UUID,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user)

):
    """Ordered sections of a chapter — the left-panel navigation source."""
    document_exists = (
        await session.execute(select(Document.id).where(Document.id == document_id))
    ).first()
    if document_exists is None:
        raise HTTPException(status_code=404, detail="Document not found")

    parts = (
        await session.execute(
            select(ChapterPart)
            .where(ChapterPart.document_id == document_id)
            .order_by(ChapterPart.order_index)
        )
    ).scalars().all()

    return parts



@router.get("/{document_id}/parts/{part_id}/chunks", response_model=ChapterPartOutContent)
async def get_chapter_part_content(
    document_id: UUID,
    part_id: UUID,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
):
    """A section's actual content — the chunks a student reads in the left panel."""
    part = (
        await session.execute(
            select(ChapterPart).where(
                ChapterPart.id == part_id,
                ChapterPart.document_id == document_id,
            )
        )
    ).scalar_one_or_none()
    if part is None:
        raise HTTPException(status_code=404, detail="Chapter part not found")

    chunks = (
        await session.execute(
            select(DocumentParentChunk)
            .where(DocumentParentChunk.part_id == part_id)
            .order_by(DocumentParentChunk.parent_index)
        )
    ).scalars().all()

    return ChapterPartOutContent(
        id=part.id,
        title=part.title,
        chunks=[DocumentParentChunkOut.model_validate(c, from_attributes=True) for c in chunks],
    )