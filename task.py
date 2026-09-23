"""
Ingests an already-processed Markdown file (LlamaParse output) into the
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
MAX_PARENT_TOKENS = 1500  # safety net — see split_oversized_parent below

client = AsyncOpenAI(api_key=os.getenv("OPEN_AI_KEY"))


# ---------------------------------------------------------------------------
# Cleaning
#
# LlamaParse does NOT have Docling's decorative-font corruption issue (no
# garbled chapter titles, no garbled "Exemples"/"Remarques" — verified by
# direct comparison against the same passages in both outputs). What it
# does still leave behind:
#   - Repeated running headers/footers: a bare page number on its own
#     line, and "Chapitre N. *<chapter name>*" repeated at every page break.
#   - Markdown image placeholders, e.g. "![icon: ...](page_2_image_1.jpg)".
#   - One observed stray HTML artifact leaking into LaTeX: <sub>...</sub>
#     tags inside a formula (e.g. "\\bigoplus_{<sub>k=1</sub>}").
#   - "✞ ✝ ☎ ✆" box-drawing remnants — kept as a defensive no-op strip in
#     case they appear; not confirmed present in this source.
# The blackboard-bold "I K" -> 𝕂 fix from the Docling version is no longer
# needed (LlamaParse already emits \mathbb{K} etc. directly) but is left in
# as a harmless no-op safety net.
# ---------------------------------------------------------------------------
_BOX_GLYPHS = {"✞", "✝", "☎", "✆"}

_BLACKBOARD_MAP = {
    r"\bI K\b": "𝕂",
    r"\bI R\b": "ℝ",
    r"\bI N\b": "ℕ",
    r"\bI C\b": "ℂ",
}

# A line that's exactly "Chapitre <num>. <italicized or bold chapter name>"
# and nothing else — the repeated running header. Generic on purpose (no
# hardcoded chapter name) so it works on other chapters too.
_RUNNING_HEADER = re.compile(r"^Chapitre\s+\d+\.\s*\*{1,2}.*\*{1,2}\s*$")

# A line that's just a bare page number.
_BARE_PAGE_NUMBER = re.compile(r"^\d{1,4}$")

# Markdown image placeholders — pure layout noise for our purposes.
_IMAGE_PLACEHOLDER = re.compile(r"!\[[^\]]*\]\([^)]*\)")

# Stray HTML tags observed leaking into LaTeX formulas.
_STRAY_HTML_TAGS = re.compile(r"</?su[bp]>")


def normalize_blackboard_bold(text: str) -> str:
    for pattern, repl in _BLACKBOARD_MAP.items():
        text = re.sub(pattern, repl, text)
    return text


def clean_markdown(md_text: str) -> str:
    text = _IMAGE_PLACEHOLDER.sub("", md_text)
    text = _STRAY_HTML_TAGS.sub("", text)

    kept_lines = []
    for line in text.splitlines():
        stripped = line.strip()

        if not stripped:
            kept_lines.append(line)
            continue

        if stripped in _BOX_GLYPHS:
            continue

        if _RUNNING_HEADER.match(stripped):
            continue

        if _BARE_PAGE_NUMBER.match(stripped):
            continue

        kept_lines.append(line)

    cleaned = "\n".join(kept_lines)
    cleaned = normalize_blackboard_bold(cleaned)

    return cleaned


# ---------------------------------------------------------------------------
# Structural chunking
#
# LlamaParse headings vary in level ("##" or "###") and are often, but not
# always, wrapped in bold markers: "### **Définition 1**", "## Remarques"
# (no bold), "## **Théorème 68**". The pattern below optionally consumes
# "#" markers, then optional "**" on both sides of the label and number
# independently, so it matches all observed variants.
#
# "Exemple(s)" and "Remarque(s)" are now included — they extract cleanly
# under LlamaParse, unlike under Docling. Both singular/plural forms are
# matched and normalized to a canonical singular chunk_type afterward.
# ---------------------------------------------------------------------------
HEADING_PATTERN = re.compile(
    r"^(?:#{1,3}\s*)?"
    r"\*{0,2}"
    r"(Définition|Théorème|Proposition|Exercice|Corollaire|Lemme|"
    r"Remarques?|Exemples?|Point méthode)"
    r"(?:[ \t]+(\d+(?:\.\d+)?))?"
    r"\*{0,2}",
    re.MULTILINE,
)

# The end-of-chapter "S'entraîner et approfondir" section: each exercise is
# a bold number at line start, numbered <chapter>.<exercise>, e.g.
# "**2.1** Soit u ∈ L(E)..." — never uses the word "Exercice" at all.
TRAINING_EXERCISE_PATTERN = re.compile(
    r"^\*{0,2}(\d+\.\d+)\*{0,2}\s+(?=\S)",
    re.MULTILINE,
)

# Multi-part block types: like Exercice, these can contain several
# numbered sub-items (1. ..., 2. ...) separated by blank lines. Taking
# only the first paragraph would truncate them, same issue we found with
# Exercice under Docling.
_MULTI_PART_TYPES = {"Exercice", "Exemple", "Remarque"}

_CANONICAL_TYPE = {
    "Exemples": "Exemple",
    "Remarques": "Remarque",
}


def normalize_chunk_type(raw_type: str) -> str:
    return _CANONICAL_TYPE.get(raw_type, raw_type)


def find_all_headings(markdown_text: str) -> list[tuple[int, int, str, str | None]]:
    """
    Combines both heading formats into one position-sorted list of
    (start, end_of_heading_match, chunk_type, number) tuples.
    """

    found: list[tuple[int, int, str, str | None]] = []

    for m in HEADING_PATTERN.finditer(markdown_text):
        found.append((m.start(), m.end(), normalize_chunk_type(m.group(1)), m.group(2)))

    for m in TRAINING_EXERCISE_PATTERN.finditer(markdown_text):
        found.append((m.start(), m.end(), "Exercice", m.group(1)))

    found.sort(key=lambda x: x[0])
    return found


def split_statement_from_block(
    body_text: str,
    chunk_type: str,
    tokenizer,
    max_statement_tokens: int = 120,
) -> str:
    """
    Pulls the bare statement out of the text AFTER a heading (the heading
    itself is already stripped by the caller — see chunk_by_structure's
    use of heading_end).

    Most block types: statement ends at the first "Démonstration" marker,
    or the first blank-line paragraph break, whichever comes first.

    Multi-part types (Exercice, Exemple, Remarque): can contain several
    numbered sub-items across paragraph breaks — keep the whole thing up
    to an optional trailing "Indication" hint section, rather than
    truncating to just the first sub-item.

    Some headings (the solutions-section entries, which repeat an item's
    number before giving only its proof) have nothing before
    "Démonstration". Rather than produce an empty/heading-only chunk, we
    fall back to the start of the proof itself.
    """

    demo_split = re.split(r"\n\s*Démonstration", body_text, maxsplit=1)
    candidate = demo_split[0].strip()

    if chunk_type in _MULTI_PART_TYPES:
        indication_split = re.split(r"\n\s*Indication", candidate, maxsplit=1)
        statement = indication_split[0].strip()
    else:
        paragraphs = [p.strip() for p in candidate.split("\n\n") if p.strip()]
        statement = paragraphs[0] if paragraphs else ""

    if not statement:
        statement = body_text.strip()

    tokens = tokenizer.encode(statement)
    if len(tokens) > max_statement_tokens:
        statement = tokenizer.decode(tokens[:max_statement_tokens])

    return statement.strip()


def split_oversized_parent(unit: dict, tokenizer, max_tokens: int = MAX_PARENT_TOKENS) -> list[dict]:
    """
    Safety net for any block that ends up unexpectedly large — e.g. if a
    heading format we haven't seen yet causes HEADING_PATTERN to miss a
    long stretch of the document. Splits on paragraph boundaries into
    several smaller parents, each within max_tokens. Does not fix the root
    cause — just guarantees no single chunk can blow up an LLM's context
    window or exceed the embedding model's input limit. Logs when it
    triggers, since that's a signal worth investigating.
    """

    if unit["parent_tokens"] <= max_tokens:
        return [unit]

    print(
        f"  [warn] oversized parent ({unit['chunk_type']} {unit['number']}, "
        f"{unit['parent_tokens']} tokens) — splitting as a safety net. "
        f"This usually means HEADING_PATTERN missed real headings nearby."
    )

    paragraphs = [p for p in unit["parent_content"].split("\n\n") if p.strip()]

    sub_chunks: list[str] = []
    current: list[str] = []
    current_tokens = 0

    for para in paragraphs:
        para_tokens = len(tokenizer.encode(para))
        if current and current_tokens + para_tokens > max_tokens:
            sub_chunks.append("\n\n".join(current))
            current = []
            current_tokens = 0
        current.append(para)
        current_tokens += para_tokens

    if current:
        sub_chunks.append("\n\n".join(current))

    split_units = []
    for i, sub_content in enumerate(sub_chunks, start=1):
        sub_number = f"{unit['number']}-part{i}" if unit["number"] else f"part{i}"
        sub_tokens = tokenizer.encode(sub_content)
        child_cap = min(120, len(sub_tokens))
        child_content = tokenizer.decode(sub_tokens[:child_cap]).strip()

        split_units.append(
            {
                "chunk_type": unit["chunk_type"],
                "number": sub_number,
                "parent_content": sub_content,
                "parent_tokens": len(sub_tokens),
                "child_content": child_content,
                "child_tokens": child_cap,
            }
        )

    return split_units


def chunk_by_structure(markdown_text: str, tokenizer) -> list[dict]:
    """
    Splits cleaned markdown into structural units. Each unit carries both
    a PARENT payload (full block, heading included) and a CHILD payload
    (bare statement, heading excluded).

    Repeated (chunk_type, number) pairs — the solutions-section entries —
    are merged into the FIRST occurrence's parent as a tagged solution
    block, rather than becoming their own top-level unit. Verified against
    real data (Exercice 1, Proposition 62 under the Docling source) that
    these repeats are genuinely the same item's statement + solution.
    """

    matches = find_all_headings(markdown_text)
    units_by_key: dict[tuple[str, str | None], dict] = {}
    ordered_keys: list[tuple[str, str | None]] = []

    for i, (start, heading_end, chunk_type, number) in enumerate(matches):
        end = matches[i + 1][0] if i + 1 < len(matches) else len(markdown_text)

        block = markdown_text[start:end].strip()
        body_after_heading = markdown_text[heading_end:end].strip()

        key = (chunk_type, number)

        if number is not None and key in units_by_key:
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

    final_units = []
    for key in ordered_keys:
        final_units.extend(split_oversized_parent(units_by_key[key], tokenizer))

    return final_units


# ---------------------------------------------------------------------------
# Contextual retrieval — one short LLM-written summary per child, generated
# once at ingest time, used only to enrich what gets embedded.
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
        await session.flush()

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
        await session.flush()

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