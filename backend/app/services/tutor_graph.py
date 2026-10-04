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
    "formule mathématique, aussi courte soit-elle — même un seul symbole isolé "
    "comme $\\lambda$, $A$ ou $X$ — utilise exclusivement la syntaxe "
    "Markdown+LaTeX avec des délimiteurs dollar : $...$ pour les formules en "
    "ligne et $$...$$ pour les formules en bloc. N'utilise JAMAIS la syntaxe "
    "\\( ... \\) ou \\[ ... \\], et n'écris JAMAIS un symbole mathématique entre "
    "parenthèses sans signes dollar : par exemple, n'écris jamais « la matrice "
    "( A ) » ou « le scalaire ( \\lambda ) » — écris toujours « la matrice $A$ » "
    "ou « le scalaire $\\lambda$ »."
)


class TutorState(TypedDict):
    question: str
    document_id: str
    part_id: str
    # Chunk ids of the specific lesson on screen within part_id — narrower
    # than the whole section. May be empty (older client, or none matched),
    # in which case load_section_node falls back to treating the whole
    # section as "the lesson", same as before this field existed.
    lesson_chunk_ids: list[str]
    lesson_content: str
    rest_of_section_content: str
    route: str
    context: str
    answer: str
    history: Annotated[list, operator.add]
    # Three different OpenAI calls can happen per question (classify, the
    # corpus embedding, generate) — each node reports only its own usage,
    # and operator.add sums them across however many of the three actually
    # ran, the same way `history` already accumulates across nodes.
    prompt_tokens: Annotated[int, operator.add]
    completion_tokens: Annotated[int, operator.add]


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

        lesson_ids = set(state["lesson_chunk_ids"])
        lesson_chunks = [c for c in chunks if str(c.id) in lesson_ids]
        if not lesson_chunks:
            # No ids sent, or none matched (stale selection) — fall back to
            # the whole section as "the lesson" rather than sending nothing.
            lesson_chunks = chunks
        lesson_chunk_id_set = {c.id for c in lesson_chunks}
        rest_chunks = [c for c in chunks if c.id not in lesson_chunk_id_set]

        def render(chunk_list):
            return "\n\n".join(
                f"[{c.chunk_type} {c.number or ''}]\n{c.content}" for c in chunk_list
            )

        return {
            "lesson_content": render(lesson_chunks),
            "rest_of_section_content": render(rest_chunks),
        }

    async def classify_node(state: TutorState) -> dict:
        prompt = (
            "Tu dois juger UNIQUEMENT si le texte ci-dessous aborde explicitement "
            "le sujet de la question — ignore tout ce que tu sais par ailleurs sur "
            "le sujet, même si tu serais capable d'y répondre toi-même. Si le "
            "texte ne traite pas explicitement de ce sujet précis, réponds "
            "'corpus', même si la question te semble simple.\n\n"
            "Exception : si la question est une demande générique qui se réfère "
            "au passage actuellement affiché plutôt qu'à un sujet précis "
            "(par exemple « explique cette partie », « résume ce passage », "
            "« reformule ça », « je ne comprends pas ce passage »), réponds "
            "toujours 'section' — une telle question n'a pas de sujet externe à "
            "rechercher, elle porte par définition sur le texte déjà fourni.\n\n"
            f"Texte actuellement affiché à l'étudiant :\n{state['lesson_content']}\n\n"
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
        return {
            "route": decision["route"],
            "prompt_tokens": completion.usage.prompt_tokens,
            "completion_tokens": completion.usage.completion_tokens,
        }

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
        # Embeddings have no "completion" side — the whole cost is input.
        return {"context": context, "prompt_tokens": result.embedding_tokens}

    async def generate_node(state: TutorState) -> dict:
        # The lesson on screen is always the primary grounding. The rest of
        # the section is always included too, but clearly secondary — this
        # keeps answers precisely scoped to what the student is looking at
        # instead of treating the whole (now much larger, post-split) section
        # as equally relevant. Corpus matches, when routed there, are
        # tertiary — a misclassified self-referential question ("explique
        # cette partie") still has the lesson and section as a fallback
        # rather than losing them entirely to an unrelated corpus match.
        context_parts = [
            f"Passage actuellement affiché à l'étudiant :\n{state['lesson_content']}"
        ]
        if state["rest_of_section_content"]:
            context_parts.append(
                f"Reste de la section (contexte complémentaire, moins prioritaire) "
                f":\n{state['rest_of_section_content']}"
            )
        if state["route"] == "corpus":
            context_parts.append(
                f"Autres passages du cours pouvant être pertinents :\n{state['context']}"
            )
        context = "\n\n---\n\n".join(context_parts)
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
        return {
            "answer": answer,
            "history": new_turn,
            "prompt_tokens": completion.usage.prompt_tokens,
            "completion_tokens": completion.usage.completion_tokens,
        }

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

