from pydantic import BaseModel ,Field
from uuid import UUID



class AskRequest(BaseModel):
    query: str


class Source(BaseModel):
    chunk_type: str
    number: str | None
    statement: str


class AskResponse(BaseModel):
    answer: str
    sources: list[Source]

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