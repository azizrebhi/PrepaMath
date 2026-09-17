from sqlalchemy import Enum as SAEnum, Column, Integer, Float, Text, String, DateTime, ForeignKey, UniqueConstraint, Boolean
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from pgvector.sqlalchemy import Vector
from datetime import datetime, timezone
import uuid
from enum import StrEnum


class MessageRole(StrEnum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class DOCUMENTSTATUS(StrEnum):
    READY = "ready"
    PENDING = "pending"
    FAILED = "failed"
    PROCESSING = "processing"


class SourceQuality(StrEnum):
    CLEAN = "clean"
    SCANNED = "scanned"
    MESSY = "messy"


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )


class Message(Base):
    __tablename__ = "message"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )
    role: Mapped[MessageRole] = mapped_column(
        SAEnum(
            MessageRole,
            name="message_role_enum",
            native_enum=True,
            validate_strings=True,
        ),
        nullable=False,
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)

    # perf metrics captured per assistant message — this is your evaluation
    # and resume-metrics source (p50/p99 latency, cache hit rate over time)
    latency_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)
    cache_hit: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    model: Mapped[str | None] = mapped_column(String(100), nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )


class Document(Base):
    """One ingested source: a chapter-split PDF of the Tout-en-un book,
    a scanned notes PDF, an exercise sheet, etc."""
    __tablename__ = "documents"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    title: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )
    source_type: Mapped[str] = mapped_column(String(255), nullable=False)  # 'book' | 'scanned_notes' | 'slides' | 'exam'
    quality: Mapped[SourceQuality] = mapped_column(
        SAEnum(
            SourceQuality,
            name="source_quality_enum",
            native_enum=True,
            validate_strings=True,
        ),
        default=SourceQuality.CLEAN,
        nullable=False,
    )
    chapter_number: Mapped[int | None] = mapped_column(Integer, nullable=True)  # e.g. 2 for "chap02_reduction..."
    status: Mapped[DOCUMENTSTATUS] = mapped_column(
        SAEnum(
            DOCUMENTSTATUS,
            name="document_status_enum",
            native_enum=True,
            validate_strings=True,
        ),
        default=DOCUMENTSTATUS.PENDING,
        nullable=False,
    )
    file_path: Mapped[str] = mapped_column(String(255), nullable=False)#Local right now but next version we add S3 bucket 
    parsed_markdown: Mapped[str | None] = mapped_column(Text, nullable=True) #full text right now but later we add S3 bucket 
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )


class DocumentParentChunk(Base):
    """The full unit sent to the LLM: statement + démonstration + exemples.
    Never embedded directly — only its children are."""
    __tablename__ = "document_parent_chunk"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    document_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("documents.id"), nullable=False, index=True
    )
    parent_index: Mapped[int] = mapped_column(Integer, nullable=False)

    chunk_type: Mapped[str | None] = mapped_column(String(50), nullable=True)  # 'Définition' | 'Théorème' | 'Proposition' | 'Exercice' | 'prose'
    number: Mapped[str | None] = mapped_column(String(20), nullable=True)      # the book's own numbering, e.g. "4.3"

    content: Mapped[str] = mapped_column(Text, nullable=False)
    token_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    page_start: Mapped[int | None] = mapped_column(Integer, nullable=True)
    page_end: Mapped[int | None] = mapped_column(Integer, nullable=True)

    __table_args__ = (
        UniqueConstraint("document_id", "parent_index", name="uq_document_parent_chunk"),
    )


class DocumentChunk(Base):
    """The bare statement — small, precise, this is what gets embedded and
    searched. On retrieval, its parent's full text is what goes to the LLM."""
    __tablename__ = "document_chunk"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    document_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("documents.id"), nullable=False
    )
    parent_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True), ForeignKey("document_parent_chunk.id"), nullable=True, index=True
    )
    chunk_index: Mapped[int] = mapped_column(nullable=False)

    chunk_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    number: Mapped[str | None] = mapped_column(String(20), nullable=True)

    content: Mapped[str] = mapped_column(Text, nullable=False)

    token_count: Mapped[int | None] = mapped_column(Integer, nullable=True)
    page_start: Mapped[int | None] = mapped_column(Integer, nullable=True)
    page_end: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # dimension matches your embedding model — 384 here (e.g. a small
    # sentence-transformers model); bump to 1536 if you switch to
    # text-embedding-3-small. Pick once, don't change mid-project without
    # a re-embed migration.
    embedding: Mapped[list[float] | None] = mapped_column(Vector(384), nullable=True)

    __table_args__ = (
        UniqueConstraint("document_id", "chunk_index", name="uq_document_chunk"),
    )


class MessageSource(Base):
    """Which chunks were retrieved and cited for a given assistant message —
    your retrieval-precision evaluation data, plus what powers in-answer
    citations back to the book."""
    __tablename__ = "message_source"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    message_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("message.id"), nullable=False
    )
    chunk_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("document_chunk.id"), nullable=False
    )
    rank: Mapped[int] = mapped_column(Integer, nullable=False)   # 1 = top retrieved result
    score: Mapped[float] = mapped_column(Float, nullable=False)  # cosine similarity at retrieval time
    citation_text: Mapped[str] = mapped_column(String(255), nullable=False)  # e.g. "Théorème 4.3, p.312"
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    __table_args__ = (UniqueConstraint("message_id", "chunk_id", name="uq_message_chunk"),)


class Feedback(Base):
    """Thumbs up/down on an assistant message — ties back to MessageSource
    so you can measure retrieval precision against real user judgment."""
    __tablename__ = "feedback"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    message_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("message.id"), nullable=False
    )
    rating: Mapped[int] = mapped_column(Integer, nullable=False)  # -1 or 1
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )