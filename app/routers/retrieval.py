from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from app.model  import Document, DocumentChunk, DocumentParentChunk
from app.schema import RetrieveResponse, RetrieveRequest, RetrievedChunk 
from app.database import get_async_session
from openai import AsyncOpenAI

from sqlalchemy import select, func, or_
from fastapi import APIRouter, Depends, HTTPException ,Query
import os 

open_ai_key = os.getenv("OPEN_AI_KEY")
client = AsyncOpenAI(api_key=open_ai_key)

router=APIRouter(prefix="/retrieve",tags=["retrieve"])
@router.post("/", response_model=RetrieveResponse)
async def create_session(
    payload: RetrieveRequest,
    session: AsyncSession = Depends(get_async_session)
    ):

    ts_query = func.websearch_to_tsquery("french", payload.query)
    ts_vector = func.to_tsvector("french", DocumentChunk.content)
    lex_rank = func.ts_rank(ts_vector, ts_query)
    
    lexical_stmt = (
        select(
            DocumentChunk.id,
            DocumentChunk.document_id,
            DocumentChunk.parent_id,
            DocumentChunk.chunk_index,
            DocumentChunk.content,
            lex_rank.label("lex_rank"),
        )
        .join(Document, Document.id == DocumentChunk.document_id)
        .where(
            ts_vector.op("@@")(ts_query),
        )
        .order_by(lex_rank.desc())
        .limit(20)
    )
    lexical_rows = (await session.execute(lexical_stmt)).all()
    
    # --- 4. Semantic Search Block (Vector Embeddings) ---
    response = await client.embeddings.create(
        model="text-embedding-3-small",
        input=payload.query,
        dimensions=384 
    )
    query_embedding = response.data[0].embedding
    sem_distance = DocumentChunk.embedding.cosine_distance(query_embedding)

    semantic_stmt = (
        select(
            DocumentChunk.id,
            DocumentChunk.document_id,
            DocumentChunk.parent_id,
            DocumentChunk.chunk_index,
            DocumentChunk.content,
            sem_distance.label("distance"),
        )
        .join(Document, Document.id == DocumentChunk.document_id)
        .where(
            
            DocumentChunk.embedding.is_not(None),
        )
        .order_by(sem_distance.asc())
        .limit(20)
    )
    semantic_rows = (await session.execute(semantic_stmt)).all()
    
    # --- 5. Reciprocal Rank Fusion (RRF) ---
    RRF_K = 60
    fused: dict[str, dict] = {}

    for rank, r in enumerate(lexical_rows, start=1):
        key = str(r.id)
        if key not in fused:
            fused[key] = {
                "document_id": r.document_id,
                "parent_id": r.parent_id,
                "chunk_index": r.chunk_index,
                "content": r.content,
                "score": 0.0,
            }
        fused[key]["score"] += 1.0 / (RRF_K + rank)

    for rank, r in enumerate(semantic_rows, start=1):
        key = str(r.id)
        if key not in fused:
            fused[key] = {
                "document_id": r.document_id,
                "parent_id": r.parent_id,  # Fixed: Restored missing parent tracking column parameter
                "chunk_index": r.chunk_index,
                "content": r.content,
                "score": 0.0,
            }
        fused[key]["score"] += 1.0 / (RRF_K + rank)
        
    # Get top 20 fused candidates
    top = sorted(fused.values(), key=lambda x: x["score"], reverse=True)[:20]
    
    # --- 6. Parent Hierarchical Map Expansion Block ---
    parent_ids = list({item["parent_id"] for item in top if item.get("parent_id") is not None})

    parent_map = {}
    if parent_ids:
        parent_rows = (await session.execute(
            select(DocumentParentChunk.id, DocumentParentChunk.content)
            .where(DocumentParentChunk.id.in_(parent_ids))
        )).all()
        parent_map = {row.id: row.content for row in parent_rows}

    # Deduplicate matching pages/parents cleanly
    seen_parents = set()
    results = []
    
    for item in top:
        pid = item.get("parent_id")
        if pid is not None:
            if pid in seen_parents:
                continue
            seen_parents.add(pid)

        # Swaps tiny child text string with the macro parental chunk content
        expanded_content = parent_map.get(pid, item["content"])
        results.append(
            RetrievedChunk(
                document_id=item["document_id"],
                chunk_index=item["chunk_index"],
                content=expanded_content,
            )
        )
    
    return RetrieveResponse(query=payload.query, results=results)


