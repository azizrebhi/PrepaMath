import os

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from openai import AsyncOpenAI

from app.schema import (
    RetrieveResponse,
    RetrieveRequest,
)
from app.auth import current_active_user
from app.database import get_async_session
from app.services.retrieval_pipeline import run_pipeline
from app.model import User
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
    user: User = Depends(current_active_user)
):
    # Config picked from evaluation/metrics.py results on the benchmark
    # dataset: dense-only currently beats both hybrid (RRF-fusing a lexical
    # channel that, even fixed, dilutes ranking with broader/noisier
    # matches) and reranked (cross-encoder favors long passages over short
    # precise definitions). See app/services/retrieval_pipeline.py and
    # evaluation/results/ for the numbers behind this.
    result = await run_pipeline(
        query=payload.query,
        session=session,
        limit=payload.limit,
        client=client,
        use_lexical=False,
        use_semantic=True,
        use_rerank=False,
    )

    return RetrieveResponse(
        query=payload.query,
        results=result.results,
    )
