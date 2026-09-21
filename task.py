"""
Ingests an already-processed Markdown file (Docling output) into the
database: cleans known extraction artifacts, splits into structural
parent/child chunks, generates a short contextual summary per child,
embeds, and stores everything.

Usage:
    uv run python ingest_markdown.py <path_to_markdown_file> "<document title>"
"""

import asyncio
import os
import re
import sys
import uuid

import tiktoken
from dotenv import load_dotenv
from openai import AsyncOpenAI

from app.database import async_session_maker
from app.model import Document, DocumentChunk, DocumentParentChunk

load_dotenv()

EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIMENSION = 384
CONTEXT_MODEL = "gpt-4o-mini"

client = AsyncOpenAI(api_key=os.getenv("OPEN_AI_KEY"))


# ---------------------------------------------------------------------------
# Cleaning
#
# Known extraction artifacts in this book's PDFs:
#   - "✞ ✝ ☎ ✆" are leftover box-drawing glyphs from a LaTeX package used to
#     frame Remarque/Exemple boxes. Pure noise, strip them.
#   - Blackboard-bold letters (𝕂, ℝ, ℕ, ℂ) extract as a plain "I" followed
#     by the ordinary letter, since the double-struck glyph has no single
#     Unicode codepoint in this PDF's embedded font.
#   - Some decorative-font headings (the chapter title, and — we found in
#     THIS file specifically — "Exemple(s)" labels) extract as garbled
#     strings of random-looking capitals. We do NOT attempt to byte-repair
#     these here: the mapping is inconsistent per-heading and not worth the
#     fragility. Practical effect: an "Exemple" block simply won't match
#     HEADING_PATTERN below and folds into whichever theorem/definition
#     precedes it, which is a reasonable default since it's supporting
#     content for that statement anyway.
# ---------------------------------------------------------------------------
_BOX_GLYPHS = {"✞", "✝", "☎", "✆"}

_BLACKBOARD_MAP = {
    r"\bI K\b": "𝕂",
    r"\bI R\b": "ℝ",
    r"\bI N\b": "ℕ",
    r"\bI C\b": "ℂ",
}


def normalize_blackboard_bold(text: str) -> str:
    for pattern, repl in _BLACKBOARD_MAP.items():
        text = re.sub(pattern, repl, text)
    return text


def clean_markdown(md_text: str) -> str:
    kept_lines = []

    for line in md_text.splitlines():
        stripped = line.strip()

        if not stripped:
            kept_lines.append(line)
            continue

        if stripped in _BOX_GLYPHS:
            continue

        # All-caps garbled running headers/footers (the decorative-font
        # artifacts), heuristically: long, fully uppercase, no lowercase.
        if stripped.isupper() and not any(c.islower() for c in stripped) and len(stripped) > 3:
            continue

        if re.fullmatch(r"[A-Z]{2}", stripped):
            continue

        kept_lines.append(line)

    cleaned = "\n".join(kept_lines)
    cleaned = normalize_blackboard_bold(cleaned)

    return cleaned


# ---------------------------------------------------------------------------
# Structural chunking
#
# Docling emits headings as "## Définition 1", "## Proposition 5", etc.
# The optional "#{1,3}" prefix absorbs the markdown marker whether or not
# it's present. The number group is optional too, since "Point méthode"
# and some "Remarque"/"Théorème (Nom du théorème)" blocks carry no plain
# digit numbering.
# ---------------------------------------------------------------------------
HEADING_PATTERN = re.compile(
    r"^(?:#{1,3}\s*)?"
    r"(Définition|Théorème|Proposition|Exercice|Corollaire|Lemme|Remarque|Point méthode)"
    r"(?:\s+(\d+(?:\.\d+)?))?",
    re.MULTILINE,
)


def split_statement_from_block(
    body_text: str,
    chunk_type: str,
    tokenizer,
    max_statement_tokens: int = 120,
) -> str:
    """
    Pulls the bare statement out of the text AFTER a heading (the heading
    itself, e.g. "## Proposition 62", is already stripped by the caller —
    see chunk_by_structure's use of match.end()).

    Most block types: statement ends at the first "Démonstration" marker,
    or the first blank-line paragraph break, whichever comes first.

    Exercices: often contain multiple numbered sub-questions (1. ..., 2. ...)
    each separated by a blank line. Taking only the first paragraph would
    silently truncate the exercise down to its first sub-question, so for
    exercises we keep the whole thing up to an optional trailing
    "Indication" hint section instead.

    Some headings (mostly in the book's end-of-chapter "solutions" section,
    which repeats each item's number as its own heading before giving only
    the proof — no restated statement) have NOTHING before "Démonstration".
    In that case candidate ends up empty; rather than silently produce an
    empty/heading-only chunk, we fall back to the start of the proof itself
    so the chunk still carries real, searchable content.
    """

    demo_split = re.split(r"\n\s*Démonstration", body_text, maxsplit=1)
    candidate = demo_split[0].strip()

    if chunk_type == "Exercice":
        indication_split = re.split(r"\n\s*Indication", candidate, maxsplit=1)
        statement = indication_split[0].strip()
    else:
        paragraphs = [p.strip() for p in candidate.split("\n\n") if p.strip()]
        statement = paragraphs[0] if paragraphs else ""

    if not statement:
        # Likely a solutions-section entry: heading immediately followed by
        # "Démonstration" with no restated statement. Use the proof's own
        # opening instead of leaving this chunk empty.
        statement = body_text.strip()

    tokens = tokenizer.encode(statement)
    if len(tokens) > max_statement_tokens:
        statement = tokenizer.decode(tokens[:max_statement_tokens])

    return statement.strip()


def chunk_by_structure(markdown_text: str, tokenizer) -> list[dict]:
    """
    Splits cleaned markdown into structural units. Each unit carries both
    a PARENT payload (the full block, heading included) and a CHILD
    payload (the bare statement, heading excluded).

    This book repeats certain (chunk_type, number) pairs: once as the real
    statement in the main "cours" text, and again later in a "Démonstrations
    et solutions des exercices du cours" section, where the heading is
    followed only by the proof/solution, no restated statement. Verified
    against real data (Exercice 1, Proposition 62) that these repeats are
    genuinely the same item's statement + solution, not two unrelated items
    that happen to share a number — so a second occurrence of a
    (chunk_type, number) pair is merged into the FIRST occurrence's parent
    content (as its solution/démonstration) rather than becoming its own
    top-level unit. The child (embedded, searchable) stays just the
    original clean statement either way — a solution fragment should never
    be the thing retrieval matches against.

    NOTE: if a later, separate "Exercices" section in this book restarts
    its own numbering from 1, this heuristic would incorrectly merge an
    unrelated exercise into an earlier one with the same number. Worth
    re-checking duplicate counts after processing the full document before
    trusting this blindly on other chapters.
    """

    matches = list(HEADING_PATTERN.finditer(markdown_text))
    units_by_key: dict[tuple[str, str | None], dict] = {}
    ordered_keys: list[tuple[str, str | None]] = []

    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(markdown_text)

        block = markdown_text[start:end].strip()

        # Slice off exactly the matched heading text (e.g. "## Proposition
        # 62"), not a fixed number of lines — this correctly handles both
        # "heading and content on the same line" and "heading, then a
        # blank line, then content" without accidentally keeping or
        # dropping either format's real content.
        body_after_heading = markdown_text[match.end():end].strip()

        chunk_type = match.group(1)
        number = match.group(2)  # may be None

        key = (chunk_type, number)

        if number is not None and key in units_by_key:
            # Second occurrence of a numbered heading — treat as the
            # solution/démonstration for the first occurrence, fold it
            # into that unit's parent rather than creating a new one.
            existing = units_by_key[key]
            existing["parent_content"] = (
                f"{existing['parent_content']}\n\n"
                f"--- Solution ({chunk_type} {number}) ---\n\n{block}"
            )
            existing["parent_tokens"] = len(tokenizer.encode(existing["parent_content"]))
            continue

        statement = split_statement_from_block(body_after_heading, chunk_type, tokenizer)

        unit = {
            "chunk_type": chunk_type,
            "number": number,
            "parent_content": block,
            "parent_tokens": len(tokenizer.encode(block)),
            "child_content": statement,
            "child_tokens": len(tokenizer.encode(statement)),
        }

        units_by_key[key] = unit
        ordered_keys.append(key)

    return [units_by_key[k] for k in ordered_keys]


# ---------------------------------------------------------------------------
# Contextual retrieval: one short LLM-written summary per child, generated
# once at ingest time, used only to enrich what gets embedded. This is what
# lets a vaguely-phrased student question still match a terse book
# statement that never uses the student's wording.
# ---------------------------------------------------------------------------
CONTEXT_SYSTEM_PROMPT = (
    "You situate a short math-course excerpt within its chapter. "
    "Given the chapter title and a chunk, write ONE short sentence (max 40 "
    "words), in French, describing what this chunk states and where it sits "
    "in the chapter (e.g. which concept it builds on). Do not restate the "
    "chunk itself, do not add extra commentary, and do not use markdown."
)


async def generate_context_summary(
    chunk_type: str,
    number: str | None,
    statement: str,
    chapter_title: str,
) -> str:
    label = f"{chunk_type} {number}" if number else chunk_type
    user_prompt = f"Chapitre : {chapter_title}\nBloc : {label}\nContenu : {statement}"

    try:
        response = await client.chat.completions.create(
            model=CONTEXT_MODEL,
            messages=[
                {"role": "system", "content": CONTEXT_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=80,
            temperature=0,
        )
        return response.choices[0].message.content.strip()
    except Exception as exc:
        print(f"  [warn] context summary failed for {label}: {exc}")
        return ""


# ---------------------------------------------------------------------------
# Main ingestion flow
# ---------------------------------------------------------------------------
async def ingest_markdown_file(markdown_path: str, title: str):
    if not os.path.isfile(markdown_path):
        raise FileNotFoundError(f"Markdown file does not exist: {markdown_path}")

    with open(markdown_path, "r", encoding="utf-8") as f:
        raw_markdown = f.read()

    print(f"Loaded {len(raw_markdown)} chars from {markdown_path}")

    parsed_markdown = clean_markdown(raw_markdown)
    tokenizer = tiktoken.get_encoding("cl100k_base")

    units = chunk_by_structure(parsed_markdown, tokenizer)
    print(f"Chunked into {len(units)} structural units")

    if not units:
        print("[warn] No structural headings matched — check HEADING_PATTERN "
              "against this document's actual heading format before proceeding.")
        return

    # Quick sanity print so you can eyeball quality before it hits the DB.
    for u in units[:5]:
        label = f"{u['chunk_type']} {u['number']}" if u["number"] else u["chunk_type"]
        preview = u["child_content"][:80].replace("\n", " ")
        print(f"  [{label}] {preview}...")

    async with async_session_maker() as session:
        document = Document(
            id=uuid.uuid4(),
            title=title,
            file_path=markdown_path,
            status="processing",
            parsed_markdown=parsed_markdown,
        )
        session.add(document)
        await session.flush()  # get document.id without committing yet

        print("Generating contextual summaries (one LLM call per unit)...")
        context_summaries = []
        for i, unit in enumerate(units):
            summary = await generate_context_summary(
                chunk_type=unit["chunk_type"],
                number=unit["number"],
                statement=unit["child_content"],
                chapter_title=title,
            )
            context_summaries.append(summary)
            if (i + 1) % 10 == 0:
                print(f"  ...{i + 1}/{len(units)}")

        print("Generating embeddings...")
        embedding_inputs = [
            f"{summary}\n\n{unit['child_content']}" if summary else unit["child_content"]
            for unit, summary in zip(units, context_summaries)
        ]

        embedding_response = await client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=embedding_inputs,
            dimensions=EMBEDDING_DIMENSION,
        )

        if len(embedding_response.data) != len(units):
            raise RuntimeError(
                f"Embedding count mismatch: expected {len(units)}, "
                f"got {len(embedding_response.data)}"
            )

        parent_rows = []
        for idx, unit in enumerate(units):
            parent_rows.append(
                DocumentParentChunk(
                    id=uuid.uuid4(),
                    document_id=document.id,
                    parent_index=idx,
                    chunk_type=unit["chunk_type"],
                    number=unit["number"],
                    content=unit["parent_content"],
                    token_count=unit["parent_tokens"],
                )
            )
        session.add_all(parent_rows)
        await session.flush()  # get parent_row.id values

        child_rows = []
        for unit, parent_row, data_item, summary in zip(
            units, parent_rows, embedding_response.data, context_summaries
        ):
            child_rows.append(
                DocumentChunk(
                    id=uuid.uuid4(),
                    document_id=document.id,
                    parent_id=parent_row.id,
                    chunk_index=parent_row.parent_index,
                    chunk_type=unit["chunk_type"],
                    number=unit["number"],
                    content=unit["child_content"],
                    context_summary=summary or None,
                    token_count=unit["child_tokens"],
                    embedding=data_item.embedding,
                )
            )
        session.add_all(child_rows)

        document.status = "ready"
        await session.commit()

        print(f"Done. document_id={document.id} "
              f"parents={len(parent_rows)} children={len(child_rows)}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: uv run python ingest_markdown.py <path_to_markdown_file> "<title>"')
        sys.exit(1)

    asyncio.run(ingest_markdown_file(sys.argv[1], sys.argv[2]))