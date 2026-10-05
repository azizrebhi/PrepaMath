import os
import uuid
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, Request
from openai import APIError, AsyncOpenAI
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import current_active_user
from app.database import get_async_session
from app.model import Conversation, Message, User
from app.rate_limit import limiter
from app.schema import AskRequest, AskResponse, ConversationOut, MessageOut
from app.services.tutor_graph import build_tutor_graph

open_ai_key = os.getenv("OPEN_AI_KEY")
client = AsyncOpenAI(api_key=open_ai_key)

router = APIRouter(
    prefix="/documents/{document_id}",
    tags=["answer"],
)

# Sized for a real student, not for abuse: a typical exchange here runs
# roughly 2-6k tokens (lesson + rest-of-section context + the answer) at
# gpt-4o-mini pricing (~$0.15/1M input, $0.60/1M output) — call it ~$0.002
# per question on the expensive end. 200k tokens/day is ~30-50 real
# questions for one student, while capping any single user's worst-case
# daily exposure at well under $1. Tune this against your own measured
# average cost per question once you have real usage, not this estimate.
DAILY_TOKEN_BUDGET = 200_000


@router.get("/conversation", response_model=ConversationOut)
async def get_latest_conversation(
    document_id: uuid.UUID,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
):
    """The frontend has no other way to know a conversation exists — nothing
    was fetching this before, which is why history vanished on every reload
    even though messages were already being saved correctly."""

    conversation = (
        await session.execute(
            select(Conversation)
            .where(Conversation.document_id == document_id, Conversation.user_id == user.id)
            .order_by(Conversation.created_at.desc())
        )
    ).scalars().first()

    if conversation is None:
        return ConversationOut(conversation_id=None, messages=[])

    messages = (
        await session.execute(
            select(Message)
            .where(Message.conversation_id == conversation.id)
            .order_by(Message.created_at)
        )
    ).scalars().all()

    return ConversationOut(
        conversation_id=conversation.id,
        messages=[MessageOut(role=m.role, content=m.content) for m in messages],
    )


@router.post("/ask", response_model=AskResponse)
@limiter.limit("10/minute")
async def ask_question(
    request: Request,
    document_id: uuid.UUID,
    payload: AskRequest,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
):
    # Checked first, before touching the conversation or spending anything —
    # a rolling 24h window (not "since midnight") so it can't be reset early
    # by waiting for a clock boundary.
    window_start = datetime.now(timezone.utc) - timedelta(hours=24)
    tokens_used_today = (
        await session.execute(
            select(func.coalesce(func.sum(Message.prompt_tokens + Message.completion_tokens), 0))
            .join(Conversation, Conversation.id == Message.conversation_id)
            .where(Conversation.user_id == user.id, Message.created_at >= window_start)
        )
    ).scalar_one()
    if tokens_used_today >= DAILY_TOKEN_BUDGET:
        raise HTTPException(
            status_code=429,
            detail="Limite quotidienne de questions atteinte. Réessaie demain.",
        )

    if payload.conversation_id is not None:
        conversation = (
            await session.execute(
                select(Conversation).where(
                    Conversation.id == payload.conversation_id,
                    Conversation.document_id == document_id,
                    Conversation.user_id == user.id,
                )
            )
        ).scalar_one_or_none()
        if conversation is None:
            raise HTTPException(status_code=404, detail="Conversation not found")
    else:
        conversation = Conversation(document_id=document_id, user_id=user.id)
        session.add(conversation)
        await session.flush()  # assigns conversation.id without committing yet

    prior_messages = (
        await session.execute(
            select(Message)
            .where(Message.conversation_id == conversation.id)
            .order_by(Message.created_at)
        )
    ).scalars().all()
    history = [{"role": m.role, "content": m.content} for m in prior_messages]

    graph = build_tutor_graph(session, client)
    try:
        result = await graph.ainvoke({
            "question": payload.query,
            "document_id": str(document_id),
            "part_id": str(payload.current_part_id),
            "lesson_chunk_ids": [str(cid) for cid in payload.current_chunk_ids],
            "lesson_content": "",
            "rest_of_section_content": "",
            "route": "",
            "context": "",
            "answer": "",
            "history": history,
            "prompt_tokens": 0,
            "completion_tokens": 0,
        })
    except APIError:
        # A transient OpenAI-side failure (timeout, connection drop, 5xx,
        # momentary rate limit on their end) shouldn't surface as a raw 500 —
        # roll back the conversation row flushed above so a failed first
        # question doesn't leave an empty conversation behind, then ask the
        # student to just retry rather than exposing the underlying error.
        await session.rollback()
        raise HTTPException(
            status_code=503,
            detail="Le service est temporairement indisponible. Réessaie dans un instant.",
        )

    session.add_all([
        Message(conversation_id=conversation.id, role="user", content=payload.query),
        Message(
            conversation_id=conversation.id,
            role="assistant",
            content=result["answer"],
            prompt_tokens=result["prompt_tokens"],
            completion_tokens=result["completion_tokens"],
        ),
    ])
    await session.commit()

    return AskResponse(answer=result["answer"], conversation_id=conversation.id)
