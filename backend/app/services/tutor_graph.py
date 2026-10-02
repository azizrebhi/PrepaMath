import json
from typing import TypedDict, Annotated
import operator
from fastapi import  Depends

from openai import AsyncOpenAI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from langgraph.graph import StateGraph, START, END
from app.database import get_async_session

from app.model import DocumentParentChunk
from app.services.retrieval_pipeline import run_pipeline

ANSWER_MODEL = "gpt-4o-mini"

SYSTEM_PROMPT = (
    "Tu es un tuteur de mathématiques pour un étudiant de classe préparatoire. "
    "Réponds à la question de l'étudiant en te basant UNIQUEMENT sur le contexte "
    "fourni. Réponds en français, de façon claire et pédagogique. Pour toute "
    "formule mathématique, utilise exclusivement la syntaxe Markdown+LaTeX avec "
    "des délimiteurs dollar : $...$ pour les formules en ligne et $$...$$ pour "
    "les formules en bloc. N'utilise JAMAIS la syntaxe \\( ... \\) ou \\[ ... \\]."
)


class TutorState(TypedDict):
    question: str
    document_id: str
    part_id: str
    section_content: str
    route: str
    context: str
    answer: str
    history: Annotated[list, operator.add]


def build_tutor_graph(session: AsyncSession ,client: AsyncOpenAI):
    """Compiles a fresh tutor graph bound to this request's session/client.

    Nodes are defined inside this factory (closures over `session`/`client`)
    rather than as module-level functions, since the DB session is
    request-scoped in FastAPI — there's no global session to close over at
    import time. Compiling per request is cheap; no heavy work happens in
    `.compile()`.
    """

    async def load_section_node(state: TutorState) -> dict:
        chunks = (
            await session.execute(
                select(DocumentParentChunk)
                .where(DocumentParentChunk.part_id == state["part_id"])
                .order_by(DocumentParentChunk.parent_index)
            )
        ).scalars().all()
        section_text = "\n\n".join(
            f"[{c.chunk_type} {c.number or ''}]\n{c.content}" for c in chunks
        )
        return {"section_content": section_text}

    async def classify_node(state: TutorState) -> dict:
        prompt = (
            "Tu dois juger UNIQUEMENT si le texte ci-dessous aborde explicitement "
            "le sujet de la question — ignore tout ce que tu sais par ailleurs sur "
            "le sujet, même si tu serais capable d'y répondre toi-même. Si le "
            "texte ne traite pas explicitement de ce sujet précis, réponds "
            "'corpus', même si la question te semble simple.\n\n"
            f"Texte de la section actuelle :\n{state['section_content']}\n\n"
            f"Question de l'étudiant : {state['question']}\n\n"
            "Ce texte aborde-t-il explicitement le sujet de cette question ?"
        )
        completion = await client.chat.completions.create(
            model=ANSWER_MODEL,
            messages=[{"role": "user", "content": prompt}],
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "route_decision",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "route": {"type": "string", "enum": ["section", "corpus"]}
                        },
                        "required": ["route"],
                        "additionalProperties": False,
                    },
                    "strict": True,
                },
            },
        )
        decision = json.loads(completion.choices[0].message.content)
        return {"route": decision["route"]}

    async def corpus_retrieval_node(state: TutorState) -> dict:
        result = await run_pipeline(
            query=state["question"],
            session=session,
            limit=5,
            client=client,
            use_lexical=False,
            use_semantic=True,
            use_rerank=False,
            document_id=state["document_id"],
        )
        context = "\n\n---\n\n".join(r.content for r in result.results)
        return {"context": context}

    async def generate_node(state: TutorState) -> dict:
        # Section branch already has everything it needs in section_content —
        # corpus branch's context comes from corpus_retrieval_node instead.
        context = state["context"] if state["route"] == "corpus" else state["section_content"]
        messages = (
            [{"role": "system", "content": SYSTEM_PROMPT}]
            + state["history"]
            + [{"role": "user", "content": f"Contexte :\n{context}\n\nQuestion : {state['question']}"}]
        )
        completion = await client.chat.completions.create(model=ANSWER_MODEL, messages=messages)
        answer = completion.choices[0].message.content.strip()
        new_turn = [
            {"role": "user", "content": state["question"]},
            {"role": "assistant", "content": answer},
        ]
        return {"answer": answer, "history": new_turn}

    def route_after_classify(state: TutorState) -> str:
        return state["route"]

    graph = StateGraph(TutorState)
    graph.add_node("load_section_node", load_section_node)
    graph.add_node("classify_node", classify_node)
    graph.add_node("corpus_retrieval_node", corpus_retrieval_node)
    graph.add_node("generate_node", generate_node)

    graph.add_edge(START, "load_section_node")
    graph.add_edge("load_section_node", "classify_node")
    graph.add_conditional_edges(
        "classify_node",
        route_after_classify,
        {"section": "generate_node", "corpus": "corpus_retrieval_node"},
    )
    graph.add_edge("corpus_retrieval_node", "generate_node")
    graph.add_edge("generate_node", END)

    return graph.compile()

