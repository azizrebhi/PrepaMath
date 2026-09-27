from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_session
from app.model import ChapterPart, Document
from app.schema import ChapterPartOut

router = APIRouter(
    prefix="/documents",
    tags=["chapters"],
)


@router.get("/{document_id}/parts", response_model=list[ChapterPartOut])
async def list_chapter_parts(
    document_id: UUID,
    session: AsyncSession = Depends(get_async_session),
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
