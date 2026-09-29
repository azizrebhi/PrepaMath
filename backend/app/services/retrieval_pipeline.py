"""
Core hybrid-retrieval pipeline (lexical + semantic -> RRF -> rerank ->
parent expansion/dedup), extracted so both the `/retrieve` API route and the
offline evaluation harness (see `evaluation/`) call the exact same code path.

When `trace=True`, every candidate seen at any stage is recorded with its
per-stage rank/score so a query can be debugged end to end: dense_rank,
lexical_rank, rrf_score/rrf_rank, rerank_score/rerank_rank, and whether it
survived the final parent-dedup step. Nothing about the non-trace behavior
changes versus the original inline implementation in the router.
"""

import re
from dataclasses import dataclass, field

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.concurrency import run_in_threadpool
from openai import AsyncOpenAI

from app.model import Document, DocumentChunk, DocumentParentChunk
from app.schema import RetrievedChunk
from app.services.rerank import rerank_chunks_scored

RRF_K = 60
CANDIDATE_POOL_SIZE = 20

EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIMENSION = 384

_WORD_RE = re.compile(r"[^\W\d_]+", re.UNICODE)


def _lexical_query_text(query: str) -> str:
    """websearch_to_tsquery ANDs every term by default — fine for a short
    keyword search, but a full natural-language question (10+ words) then
    requires ALL of them to co-occur in one short chunk, which essentially
    never happens (measured: 0/580 lexical hits across a 29-question eval
    before this fix). OR-ing the query's own words instead lets any single
    matching term through; ts_rank still favors chunks matching more of
    them, so relative ranking is preserved without the all-or-nothing gate.
    French stopwords are dropped by the 'french' text search config itself
    when parsing the resulting tsquery, so no separate stopword list is
    needed here.
    """
    words = _WORD_RE.findall(query)
    return " OR ".join(words) if words else query


@dataclass
class CandidateTrace:
    child_id: str
    parent_id: str | None
    parent_index: int | None
    content: str
    dense_rank: int | None = None
    lexical_rank: int | None = None
    rrf_score: float | None = None
    rrf_rank: int | None = None
    rerank_score: float | None = None
    rerank_rank: int | None = None
    survived_parent_dedup: bool | None = None
    in_final: bool = False


@dataclass
class PipelineResult:
    results: list[RetrievedChunk]
    candidates: dict[str, CandidateTrace] = field(default_factory=dict)


async def run_pipeline(
    query: str,
    session: AsyncSession,
    limit: int,
    client: AsyncOpenAI,
    trace: bool = False,
    use_lexical: bool = True,
    use_semantic: bool = True,
    # Measured via evaluation/metrics.py on a 29-question benchmark: this
    # cross-encoder (cross-encoder/mmarco-mMiniLMv2-L12-H384-v1) lowers MRR
    # 0.658->0.569 and R@10 0.862->0.793 on this corpus. Root-caused to a
    # length/style bias — it consistently favors long, keyword-dense
    # passages over short, precise definitions (confirmed reproducible even
    # when reranking against parent content instead of child content, so
    # it isn't a pairing issue). Off by default until a better-suited model
    # is validated by the harness to actually help; the code path is kept
    # for that future A/B test.
    use_rerank: bool = False,
    document_id: str | None = None,
) -> PipelineResult:
    if not use_lexical and not use_semantic:
        raise ValueError("At least one of use_lexical/use_semantic must be enabled")

    candidates: dict[str, CandidateTrace] = {}

    def get_or_create(row) -> CandidateTrace:
        key = str(row.id)
        if key not in candidates:
            candidates[key] = CandidateTrace(
                child_id=key,
                parent_id=str(row.parent_id) if row.parent_id is not None else None,
                # Set at ingest time to the parent's own parent_index (task.py),
                # so the child row already carries it — no extra join needed.
                parent_index=row.chunk_index,
                content=row.content,
            )
        return candidates[key]

    # ============================================================
    # 1. LEXICAL SEARCH
    # ============================================================
    lexical_rows = []
    if use_lexical:
        ts_query = func.websearch_to_tsquery("french", _lexical_query_text(query))
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
            .where(ts_vector.op("@@")(ts_query))
            .order_by(lex_rank.desc())
            .limit(CANDIDATE_POOL_SIZE)
        )
        if document_id is not None:
            lexical_stmt = lexical_stmt.where(DocumentChunk.document_id == document_id)
        lexical_rows = (await session.execute(lexical_stmt)).all()

    for rank, row in enumerate(lexical_rows, start=1):
        get_or_create(row).lexical_rank = rank

    # ============================================================
    # 2. SEMANTIC SEARCH
    # ============================================================
    semantic_rows = []
    if use_semantic:
        response = await client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=query,
            dimensions=EMBEDDING_DIMENSION,
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
            .where(DocumentChunk.embedding.is_not(None))
            .order_by(sem_distance.asc())
            .limit(CANDIDATE_POOL_SIZE)
        )
        if document_id is not None:
            semantic_stmt = semantic_stmt.where(DocumentChunk.document_id == document_id)
        semantic_rows = (await session.execute(semantic_stmt)).all()

    for rank, row in enumerate(semantic_rows, start=1):
        get_or_create(row).dense_rank = rank

    # ============================================================
    # 3. RECIPROCAL RANK FUSION
    # ============================================================
    fused: dict[str, dict] = {}

    for rank, row in enumerate(lexical_rows, start=1):
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
        fused[key]["rrf_score"] += 1.0 / (RRF_K + rank)

    for rank, row in enumerate(semantic_rows, start=1):
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
        fused[key]["rrf_score"] += 1.0 / (RRF_K + rank)

    # ============================================================
    # 4. GET RRF CANDIDATES
    # ============================================================
    rrf_candidates = sorted(
        fused.values(), key=lambda x: x["rrf_score"], reverse=True
    )[:CANDIDATE_POOL_SIZE]

    for rank, item in enumerate(rrf_candidates, start=1):
        c = candidates[str(item["id"])]
        c.rrf_score = item["rrf_score"]
        c.rrf_rank = rank

    # ============================================================
    # 5. CROSS-ENCODER RERANKING
    # ============================================================
    if use_rerank:
        scored = await run_in_threadpool(rerank_chunks_scored, query, rrf_candidates)
        for rank, (item, score) in enumerate(scored, start=1):
            c = candidates[str(item["id"])]
            c.rerank_score = float(score)
            c.rerank_rank = rank
        ranked = [item for item, _ in scored][:limit]
    else:
        ranked = rrf_candidates[:limit]

    # ============================================================
    # 6. PARENT EXPANSION
    # ============================================================
    parent_ids = list({
        item["parent_id"] for item in ranked if item.get("parent_id") is not None
    })

    parent_map = {}
    if parent_ids:
        parent_rows = (
            await session.execute(
                select(DocumentParentChunk.id, DocumentParentChunk.content)
                .where(DocumentParentChunk.id.in_(parent_ids))
            )
        ).all()
        parent_map = {row.id: row.content for row in parent_rows}

    # ============================================================
    # 7. DEDUPLICATION + CONTENT EXPANSION
    # ============================================================
    seen_parents = set()
    results = []

    for item in ranked:
        parent_id = item.get("parent_id")
        c = candidates[str(item["id"])]

        if parent_id is not None:
            if parent_id in seen_parents:
                c.survived_parent_dedup = False
                continue
            seen_parents.add(parent_id)

        c.survived_parent_dedup = True
        c.in_final = True

        expanded_content = parent_map.get(parent_id, item["content"])
        results.append(
            RetrievedChunk(
                document_id=item["document_id"],
                chunk_index=item["chunk_index"],
                content=expanded_content,
            )
        )

    return PipelineResult(results=results, candidates=candidates if trace else {})
