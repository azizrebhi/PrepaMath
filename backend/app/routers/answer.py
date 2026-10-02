import os
import uuid

from fastapi import APIRouter, Depends, HTTPException
from openai import AsyncOpenAI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import current_active_user
from app.database import get_async_session
from app.model import Conversation, Message, User
from app.schema import AskRequest, AskResponse
from app.services.tutor_graph import build_tutor_graph

open_ai_key = os.getenv("OPEN_AI_KEY")
client = AsyncOpenAI(api_key=open_ai_key)

router = APIRouter(
    prefix="/documents/{document_id}",
    tags=["answer"],
)


@router.post("/ask", response_model=AskResponse)
async def ask_question(
    document_id: uuid.UUID,
    payload: AskRequest,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
):
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
    result = await graph.ainvoke({
        "question": payload.query,
        "document_id": str(document_id),
        "part_id": str(payload.current_part_id),
        "section_content": "",
        "route": "",
        "context": "",
        "answer": "",
        "history": history,
    })

    session.add_all([
        Message(conversation_id=conversation.id, role="user", content=payload.query),
        Message(conversation_id=conversation.id, role="assistant", content=result["answer"]),
    ])
    await session.commit()

    return AskResponse(answer=result["answer"], conversation_id=conversation.id)
