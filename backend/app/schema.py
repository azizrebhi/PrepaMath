from pydantic import BaseModel ,Field
from uuid import UUID
from fastapi_users import schemas



class UserRead(schemas.BaseUser[UUID]):
    pass

class UserCreate(schemas.BaseUserCreate):
    pass

class AskRequest(BaseModel):
    query: str
    current_part_id: UUID
    # The specific lesson's chunk ids within current_part_id, i.e. what's
    # actually on screen — narrower than the whole section. Optional so an
    # older client that doesn't send this still gets the pre-existing
    # whole-section behavior rather than a validation error.
    current_chunk_ids: list[UUID] = Field(default_factory=list)
    conversation_id: UUID | None = None


class Source(BaseModel):
    chunk_type: str
    number: str | None
    statement: str


class AskResponse(BaseModel):
    answer: str
    conversation_id: UUID
    sources: list[Source] = []


class MessageOut(BaseModel):
    role: str
    content: str


class ConversationOut(BaseModel):
    conversation_id: UUID | None
    messages: list[MessageOut] = []

class RetrieveRequest(BaseModel):
    query: str = Field(min_length=2)
    limit: int = Field(default=10, ge=1, le=20)
    

class RetrievedChunk(BaseModel):
    document_id: UUID
    chunk_index: int
    content: str

class RetrieveResponse(BaseModel):
    query: str
    results: list[RetrievedChunk]


class ChapterPartOut(BaseModel):
    id: UUID
    title: str
    order_index: int


class DocumentOut(BaseModel):
    id: UUID
    title: str
    status: str

class DocumentParentChunkOut(BaseModel):
    id: UUID
    parent_index: int
    chunk_type: str | None
    number: str | None
    content: str


class ChapterPartOutContent(BaseModel):
    id: UUID
    title: str
    chunks: list[DocumentParentChunkOut]