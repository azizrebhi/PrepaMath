import os

from fastapi import APIRouter, Depends
from openai import AsyncOpenAI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import current_active_user
from app.database import get_async_session
from app.model import DocumentParentChunk, User
from app.schema import AskRequest, AskResponse, Source
from app.services.retrieval_pipeline import run_pipeline

open_ai_key = os.getenv("OPEN_AI_KEY")
client = AsyncOpenAI(api_key=open_ai_key)

router = APIRouter(
    prefix="/documents/{document_id}",
    tags=["answer"],
)

ANSWER_MODEL = "gpt-4o-mini"
ANSWER_LIMIT = 5  # fewer than /retrieve's default — this feeds an LLM prompt, not a results list

SYSTEM_PROMPT = (
    "Tu es un tuteur de mathématiques pour un étudiant de classe préparatoire. "
    "Réponds à la question de l'étudiant en te basant UNIQUEMENT sur les extraits "
    "de cours fournis ci-dessous. Si les extraits ne suffisent pas pour répondre "
    "complètement, dis-le clairement plutôt que d'inventer une réponse. Réponds "
    "en français, de façon claire et pédagogique. Pour toute formule "
    "mathématique, utilise exclusivement la syntaxe Markdown+LaTeX avec des "
    "délimiteurs dollar : $...$ pour les formules en ligne et $$...$$ pour les "
    "formules en bloc. N'utilise JAMAIS la syntaxe \\( ... \\) ou \\[ ... \\]."
)


@router.post("/ask", response_model=AskResponse)
async def ask_question(
    document_id: str,
    payload: AskRequest,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_active_user),
):
    # Retrieval only — same pipeline /retrieve uses, scoped to this document
    # so a question in one chapter can't surface an answer from another.
    result = await run_pipeline(
        query=payload.query,
        session=session,
        limit=ANSWER_LIMIT,
        client=client,
        document_id=document_id,
    )

    # run_pipeline's RetrievedChunk doesn't carry chunk_type/number (that
    # contract is shared with /retrieve and the eval harness — left alone).
    # One extra lookup here gets real citation labels instead of generic ones.
    chunk_indices = [r.chunk_index for r in result.results]
    parent_by_index = {}
    if chunk_indices:
        parent_rows = (
            await session.execute(
                select(
                    DocumentParentChunk.parent_index,
                    DocumentParentChunk.chunk_type,
                    DocumentParentChunk.number,
                    DocumentParentChunk.content,
                ).where(
                    DocumentParentChunk.document_id == document_id,
                    DocumentParentChunk.parent_index.in_(chunk_indices),
                )
            )
        ).all()
        parent_by_index = {row.parent_index: row for row in parent_rows}

    sources = []
    context_blocks = []
    for r in result.results:
        row = parent_by_index.get(r.chunk_index)
        chunk_type = row.chunk_type if row else "Extrait"
        number = row.number if row else None
        statement = row.content if row else r.content
        label = f"{chunk_type} {number}" if number else chunk_type

        sources.append(Source(chunk_type=chunk_type, number=number, statement=statement))
        context_blocks.append(f"[{label}]\n{statement}")

    context_text = "\n\n---\n\n".join(context_blocks) if context_blocks else "(aucun extrait trouvé)"

    completion = await client.chat.completions.create(
        model=ANSWER_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Extraits de cours :\n\n{context_text}\n\nQuestion : {payload.query}",
            },
        ],
        temperature=0.2,
    )

    answer = completion.choices[0].message.content.strip()

    return AskResponse(answer=answer, sources=sources)
