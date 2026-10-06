"""
Automated post-ingestion sanity checks — encodes every ingestion bug class
found and fixed during this project's debugging history, so the SAME class
of bug is caught by a script the moment it recurs in a new chapter, instead
of waiting for a human to manually read far enough to notice it.

This does not guarantee a new chapter has zero bugs — the source PDF
extraction is inconsistent enough that a genuinely novel formatting quirk
can still slip through. What it guarantees is that every *previously seen*
bug shape gets caught automatically and immediately, so the only bugs left
to find manually are the ones nobody has ever seen before.

Checks:
  1. Near-empty parent content — the Corollaire 9/10 duplicate-heading bug
     (a unit whose body, after its own heading, is suspiciously short/empty).
  2. A heading pattern appearing again INSIDE a chunk's own content — the
     Exercice-11-merged-into-Proposition-14 bug (one chunk's content
     contains what looks like the start of a different numbered item).
  3. Leftover extraction markup surviving into final content — <mark>,
     <button>, a literal "p.NNN" page prefix, or ">...<"/"<button>...</button>"
     wrapping around "Démonstration page N" (three different real shapes
     already found for the same underlying noise).
  4. An odd number of "**" in a single chunk — a strong signal of a split
     bold span (the "** Démonstration.**" bug class), even in chunk types
     this script doesn't specifically know to check for the word itself.
  5. Duplicate content rows (the original unnumbered Exemple/Remarque
     collision bug class).

Usage:
    uv run python evaluation/validate_ingestion.py <document_id>
    uv run python evaluation/validate_ingestion.py --all
"""

import argparse
import asyncio
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.database import async_session_maker
from app.model import Document, DocumentParentChunk
from sqlalchemy import select
from task import HEADING_PATTERN

MARKUP_PATTERNS = {
    "<mark> tag survived": re.compile(r"<mark\b", re.IGNORECASE),
    "<button> tag survived": re.compile(r"<button\b", re.IGNORECASE),
    "bare 'p.NNN' page prefix mid-content": re.compile(r"(?<!^)\bp\.\d{2,4}\b", re.MULTILINE),
    "angle-bracket-wrapped page reference": re.compile(r">Démonstration page \d+<"),
}

MIN_BODY_CHARS_BY_TYPE = {
    "Définition": 15,
    "Proposition": 10,
    "Théorème": 10,
    "Corollaire": 10,
    "Lemme": 10,
    "Exercice": 15,
}


def body_after_own_heading(content: str) -> str:
    """Strips just this chunk's own first-line heading, same shape
    HEADING_PATTERN matches at ingestion time, to inspect what's left."""
    m = HEADING_PATTERN.match(content)
    if not m:
        return content
    return content[m.end():].lstrip("\n ").strip()


async def validate_document(session, doc) -> list[str]:
    issues = []
    rows = (
        await session.execute(
            select(DocumentParentChunk).where(DocumentParentChunk.document_id == doc.id)
        )
    ).scalars().all()

    seen_content = set()
    for r in rows:
        label = f"{r.chunk_type} {r.number or ''}".strip()

        # Check 1: near-empty body for types that should always have real content.
        min_len = MIN_BODY_CHARS_BY_TYPE.get(r.chunk_type)
        if min_len is not None:
            # Only check up to the first merge marker — a unit that's
            # legitimately short BEFORE a "--- Solution ---" merge is fine;
            # this check is about the FIRST occurrence being empty, same
            # shape as the Corollaire 9/10 bug.
            first_segment = r.content.split("--- Solution (")[0]
            body = body_after_own_heading(first_segment)
            if len(body) < min_len:
                issues.append(f"[{label}] suspiciously short body ({len(body)} chars) before heading — possible duplicate-heading bug: {body!r}")

        # Check 2: a heading for a DIFFERENT (type, number) appears inside this chunk's own content, not at the start.
        # split_oversized_parent() suffixes numbers with "-partN" ("Exercice
        # 7-part1") for token-budget splits, and a split-off part legitimately
        # re-mentions its own base number (e.g. the solution text's own
        # repeated heading) — strip that suffix before comparing so a part
        # doesn't flag itself as a merge bug.
        own_number = (r.number or "").split("-part")[0] or None
        for m in HEADING_PATTERN.finditer(r.content):
            if m.start() == 0:
                continue
            found_type, found_number = m.group(1), m.group(2)
            if (found_type, found_number) != (r.chunk_type, own_number) and found_number is not None:
                issues.append(f"[{label}] contains what looks like a different heading mid-content at offset {m.start()}: {m.group(0)!r} — possible chunk-merge bug")

        # Check 3: leftover extraction markup.
        for name, pattern in MARKUP_PATTERNS.items():
            if pattern.search(r.content):
                issues.append(f"[{label}] {name}")

        # Check 4: odd number of ** — a likely split bold span.
        if r.content.count("**") % 2 != 0:
            issues.append(f"[{label}] odd count of '**' ({r.content.count('**')}) — likely split bold span")

        seen_content.add(r.content)

    # Check 5: duplicate content (the original collision bug class).
    all_content = [r.content for r in rows]
    if len(all_content) != len(set(all_content)):
        issues.append(f"{len(all_content) - len(set(all_content))} duplicate content row(s) found")

    return issues


async def main(document_id: str | None, check_all: bool) -> None:
    async with async_session_maker() as session:
        if check_all:
            docs = (await session.execute(select(Document))).scalars().all()
        else:
            docs = (await session.execute(select(Document).where(Document.id == document_id))).scalars().all()

        for doc in docs:
            print(f"\n=== {doc.title} ({doc.id}) ===")
            issues = await validate_document(session, doc)
            if not issues:
                print("  No issues found.")
            else:
                for issue in issues:
                    print(f"  [!] {issue}")
                print(f"  -> {len(issues)} issue(s) total")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("document_id", nargs="?", default=None)
    parser.add_argument("--all", action="store_true", dest="check_all")
    args = parser.parse_args()
    if not args.check_all and not args.document_id:
        parser.error("provide a document_id or --all")
    asyncio.run(main(args.document_id, args.check_all))
