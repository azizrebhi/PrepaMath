import os
import logging
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from fastapi.concurrency import run_in_threadpool
from openai import AsyncOpenAI

from app.model import (
    Document,
    DocumentChunk,
    DocumentParentChunk,
)
from app.schema import (
    RetrieveResponse,
    RetrieveRequest,
    RetrievedChunk,
)
from app.database import get_async_session
from app.services.rerank import rerank_chunks

# ============================================================
# LOGGING CONFIGURATION
# ============================================================
logger = logging.getLogger("app.retrieve")
logger.setLevel(logging.INFO)

# Standardize stream logging to console if not globally configured
if not logger.handlers:
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


open_ai_key = os.getenv("OPEN_AI_KEY")

client = AsyncOpenAI(
    api_key=open_ai_key
)

router = APIRouter(
    prefix="/retrieve",
    tags=["retrieve"],
)


@router.post("/", response_model=RetrieveResponse)
async def create_session(
    payload: RetrieveRequest,
    session: AsyncSession = Depends(get_async_session),
):

    # ============================================================
    # 1. LEXICAL SEARCH
    # ============================================================

    ts_query = func.websearch_to_tsquery(
        "french",
        payload.query,
    )

    ts_vector = func.to_tsvector(
        "french",
        DocumentChunk.content,
    )

    lex_rank = func.ts_rank(
        ts_vector,
        ts_query,
    )

    lexical_stmt = (
        select(
            DocumentChunk.id,
            DocumentChunk.document_id,
            DocumentChunk.parent_id,
            DocumentChunk.chunk_index,
            DocumentChunk.content,
            lex_rank.label("lex_rank"),
        )
        .join(
            Document,
            Document.id == DocumentChunk.document_id,
        )
        .where(
            ts_vector.op("@@")(ts_query),
        )
        .order_by(
            lex_rank.desc()
        )
        .limit(20)
    )

    lexical_rows = (
        await session.execute(lexical_stmt)
    ).all()


    # ============================================================
    # 2. SEMANTIC SEARCH
    # ============================================================

    response = await client.embeddings.create(
        model="text-embedding-3-small",
        input=payload.query,
        dimensions=384,
    )

    query_embedding = response.data[0].embedding

    sem_distance = (
        DocumentChunk.embedding.cosine_distance(
            query_embedding
        )
    )

    semantic_stmt = (
        select(
            DocumentChunk.id,
            DocumentChunk.document_id,
            DocumentChunk.parent_id,
            DocumentChunk.chunk_index,
            DocumentChunk.content,
            sem_distance.label("distance"),
        )
        .join(
            Document,
            Document.id == DocumentChunk.document_id,
        )
        .where(
            DocumentChunk.embedding.is_not(None),
        )
        .order_by(
            sem_distance.asc()
        )
        .limit(20)
    )

    semantic_rows = (
        await session.execute(semantic_stmt)
    ).all()


    # ============================================================
    # 3. RECIPROCAL RANK FUSION
    # ============================================================

    RRF_K = 60

    fused = {}

    # -------------------------
    # Lexical rankings
    # -------------------------

    for rank, row in enumerate(
        lexical_rows,
        start=1,
    ):

        key = str(row.id)

        if key not in fused:

            fused[key] = {
                "id": row.id,
                "document_id": row.document_id,
                "parent_id": row.parent_id,
                "chunk_index": row.chunk_index,
                "content": row.content,
                "rrf_score": 0.0,
            }

        fused[key]["rrf_score"] += (
            1.0 / (RRF_K + rank)
        )


    # -------------------------
    # Semantic rankings
    # -------------------------

    for rank, row in enumerate(
        semantic_rows,
        start=1,
    ):

        key = str(row.id)

        if key not in fused:

            fused[key] = {
                "id": row.id,
                "document_id": row.document_id,
                "parent_id": row.parent_id,
                "chunk_index": row.chunk_index,
                "content": row.content,
                "rrf_score": 0.0,
            }

        fused[key]["rrf_score"] += (
            1.0 / (RRF_K + rank)
        )


    # ============================================================
    # 4. GET RRF CANDIDATES
    # ============================================================

    rrf_candidates = sorted(
        fused.values(),
        key=lambda x: x["rrf_score"],
        reverse=True,
    )[:20]

    # Map chunks to their pre-rerank positions (1-indexed base)
    rrf_rank_mapping = {
        str(item["id"]): rank 
        for rank, item in enumerate(rrf_candidates, start=1)
    }


    # ============================================================
    # 5. CROSS-ENCODER RERANKING
    # ============================================================

    reranked = await run_in_threadpool(
        rerank_chunks,
        payload.query,
        rrf_candidates,
        payload.limit,
    )

    # ------------------------------------------------------------
    # DEBUG METRICS: ORDER COMPONENT ANALYSIS
    # ------------------------------------------------------------
    logger.info(f"--- Rerank Delta Analysis [Query: '{payload.query}'] ---")
    
    for final_rank, item in enumerate(reranked, start=1):
        chunk_id = str(item["id"])
        initial_rank = rrf_rank_mapping.get(chunk_id, "N/A")
        
        if initial_rank != "N/A":
            diff = initial_rank - final_rank
            if diff > 0:
                movement_str = f"Moved up:   +{diff}"
            elif diff < 0:
                movement_str = f"Moved down:  {diff}"
            else:
                movement_str = "No change"
        else:
            movement_str = "Chunk fell outside top 20 pre-rerank window"

        logger.info(
            f"Final Rank {final_rank:02d} | "
            f"Chunk ID: {chunk_id:<6} | "
            f"Initial RRF Rank: {initial_rank:<2} | "
            f"[{movement_str}]"
        )
    logger.info("------------------------------------------------------------")


    # ============================================================
    # 6. PARENT EXPANSION
    # ============================================================

    parent_ids = list({
        item["parent_id"]
        for item in reranked
        if item.get("parent_id") is not None
    })

    parent_map = {}

    if parent_ids:

        parent_rows = (
            await session.execute(
                select(
                    DocumentParentChunk.id,
                    DocumentParentChunk.content,
                )
                .where(
                    DocumentParentChunk.id.in_(parent_ids)
                )
            )
        ).all()

        parent_map = {
            row.id: row.content
            for row in parent_rows
        }


    # ============================================================
    # 7. DEDUPLICATION + CONTENT EXPANSION
    # ============================================================

    seen_parents = set()

    results = []

    for item in reranked:

        parent_id = item.get("parent_id")

        if parent_id is not None:

            if parent_id in seen_parents:
                continue

            seen_parents.add(parent_id)

        expanded_content = parent_map.get(
            parent_id,
            item["content"],
        )

        results.append(
            RetrievedChunk(
                document_id=item["document_id"],
                chunk_index=item["chunk_index"],
                content=expanded_content,
            )
        )


    # ============================================================
    # 8. RESPONSE
    # ============================================================

    return RetrieveResponse(
        query=payload.query,
        results=results,
    )
