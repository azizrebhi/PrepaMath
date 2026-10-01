import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pgvector.sqlalchemy import Vector
from fastapi_users.db import SQLAlchemyBaseOAuthAccountTableUUID , SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped ,relationship



class Base(DeclarativeBase):
    pass

class OauthAccount(SQLAlchemyBaseOAuthAccountTableUUID,Base):
    pass 

class User(SQLAlchemyBaseUserTableUUID,Base):
    oauth_accounts: Mapped[list[OauthAccount]]=relationship(
        "OauthAccount",lazy="joined"
    )


class Document(Base):
    """One ingested source. Trimmed for now — no user_id, no quality, no
    chapter_number yet, since nothing uses them at this stage. We'll add
    those back in Phase 6 (users/conversations) and Phase 9 (S3)."""

    __tablename__ = "documents"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String, nullable=False)

    # For now this is just the local path to the already-processed .md file.
    # Becomes an S3 key in Phase 9.
    file_path: Mapped[str] = mapped_column(String(255), nullable=False)

    # Plain string for now, not an enum yet — upgrade later if you need
    # stricter validation.
    status: Mapped[str] = mapped_column(String(20), default="pending", nullable=False)

    parsed_markdown: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )


class DocumentParentChunk(Base):
    """The full structural unit (statement + démonstration + examples),
    handed to the LLM at answer time. Never embedded directly."""

    __tablename__ = "document_parent_chunk"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    document_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("documents.id"), nullable=False, index=True
    )
    parent_index: Mapped[int] = mapped_column(Integer, nullable=False)

    # Which section (ChapterPart) this chunk falls under, for left-panel
    # navigation. Nullable: front-matter (chapter title/intro, before the
    # first detected section) doesn't belong to any section.
    part_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True), ForeignKey("chapter_part.id"), nullable=True, index=True
    )

    chunk_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    number: Mapped[str | None] = mapped_column(String(20), nullable=True)

    content: Mapped[str] = mapped_column(Text, nullable=False)
    token_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    page_start: Mapped[int | None] = mapped_column(Integer, nullable=True)
    page_end: Mapped[int | None] = mapped_column(Integer, nullable=True)

    __table_args__ = (
        UniqueConstraint("document_id", "parent_index", name="uq_document_parent_chunk"),
    )


class DocumentChunk(Base):
    """The bare statement — small and precise, this is what's embedded and
    searched. On retrieval, its parent's full text goes to the LLM."""

    __tablename__ = "document_chunk"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    document_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("documents.id"), nullable=False, index=True
    )
    parent_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True), ForeignKey("document_parent_chunk.id"), nullable=True, index=True
    )
    chunk_index: Mapped[int] = mapped_column(nullable=False)

    chunk_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    number: Mapped[str | None] = mapped_column(String(20), nullable=True)

    content: Mapped[str] = mapped_column(Text, nullable=False)

    # The bare statement, shown to the user / passed downstream unmodified.
    # The context_summary below is ONLY used to enrich what gets embedded —
    # it is never shown as-is.
    context_summary: Mapped[str | None] = mapped_column(Text, nullable=True)

    token_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    page_start: Mapped[int | None] = mapped_column(Integer, nullable=True)
    page_end: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # 384 dims: text-embedding-3-small, truncated via the `dimensions` param.
    embedding: Mapped[list[float] | None] = mapped_column(Vector(384), nullable=True)

    __table_args__ = (
        UniqueConstraint("document_id", "chunk_index", name="uq_document_chunk"),
    )
class ChapterPart(Base):
    """
    One 'page' of a chapter as the student will navigate it — a curated,
    contiguous run of DocumentParentChunk rows (e.g. one book section like
    'Éléments propres'), NOT auto-derived from search. In-page Q&A reads
    directly from a part's own chunks; no embedding/search call needed for
    that flow. Search/embeddings remain for cross-references and
    whole-book search — see DocumentChunk, unchanged.
    """
 
    __tablename__ = "chapter_part"
 
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    document_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("documents.id"), nullable=False, index=True
    )
    title: Mapped[str] = mapped_column(String, nullable=False)
    order_index: Mapped[int] = mapped_column(Integer, nullable=False)
 
    __table_args__ = (
        UniqueConstraint("document_id", "order_index", name="uq_chapter_part_order"),
    )

class Conversation(Base):
    __tablename__ = "conversation"
    id: Mapped[uuid.UUID]=mapped_column(
        UUID(as_uuid=True),primary_key=True,default=uuid.uuid4
    )
    document_id:Mapped[uuid.UUID]= mapped_column(
        UUID(as_uuid=True),ForeignKey("documents.id"),nullable=False, index=True
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True) , ForeignKey("user.id"),nullable=False , index=True
    )
    created_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

class Message(Base):
    """One turn in a Conversation - both the student's question and the
    tutor's answer get their own row, in order."""

    __tablename__ = "message"

    id: Mapped[uuid.UUID] = mapped_column(
    UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    conversation_id: Mapped[uuid.UUID] = mapped_column(
UUID(as_uuid=True), ForeignKey("conversation.id"), nullable=False, index=True )

    role: Mapped[str] = mapped_column(String(20), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    
