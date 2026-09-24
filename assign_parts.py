"""
Assign top-level chapter parts to DocumentParentChunk records.

Workflow:

1. Preview detected top-level section boundaries:

    uv run python assign_parts.py suggest <document_id>

2. Review the output and fill BOUNDARIES below.

3. Apply the reviewed boundaries:

    uv run python assign_parts.py apply <document_id>

The script is intentionally conservative:
- Only Markdown headings (# or ##) are considered.
- Only Roman-numbered top-level sections I, II, III, IV, V are considered.
- Numbered subsections such as "1 Définition..." are ignored.
- Repeated page headers / plain-text occurrences are ignored.
- Duplicate top-level headings are deduplicated.
"""

import asyncio
import re
import sys
import uuid

from sqlalchemy import select

from app.database import async_session_maker
from app.model import ChapterPart, Document, DocumentParentChunk


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# The actual document uses inconsistent heading levels:
#
#   ## I Sous-espaces stables...
#   # II Éléments propres
#   # III Endomorphismes...
#   ## IV Endomorphismes...
#   # V Utilisations...
#
# Therefore we accept both # and ##.
#
# IMPORTANT:
# We require a Markdown heading and a Roman numeral.
# This automatically ignores:
#
#   II Éléments propres
#
# when it appears as a plain page header.
#
# It also ignores:
#
#   ## 1 Définition...
#
# because that starts with an Arabic number.
TOP_LEVEL_SECTION_PATTERN = re.compile(
    r"^#{1,2}[ \t]+"
    r"\*{0,2}"
    r"(I|II|III|IV|V)"
    r"[ \t]+"
    r"(.+?)"
    r"\*{0,2}"
    r"[ \t]*$",
    re.MULTILINE,
)


# Used only as a fallback when a heading is not literally contained
# inside a parent chunk.
PARENT_PREFIX_LENGTH = 200


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def clean_title(title: str) -> str:
    """
    Normalize a detected heading title.

    Examples:

        "Endomorphismes et matrices **diagonalisables**"
            ->
        "Endomorphismes et matrices diagonalisables"
    """

    title = title.strip()

    # Remove Markdown emphasis.
    title = re.sub(r"\*\*(.*?)\*\*", r"\1", title)
    title = re.sub(r"\*(.*?)\*", r"\1", title)

    # Remove trailing whitespace.
    title = title.strip()

    return title


def normalize_for_matching(text: str) -> str:
    """
    Normalize text for loose comparison.

    This is only used when determining whether a heading occurs
    inside a parent chunk.
    """

    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Normalize Markdown bold markers.
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)

    # Normalize whitespace.
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def get_heading_candidates(markdown: str):
    """
    Return unique top-level section candidates.

    The raw Markdown contains repeated page headers, and III appears
    twice as an actual Markdown heading because of the PDF conversion.

    We keep only the first real occurrence of each Roman section.
    """

    candidates = []
    seen_numerals = set()

    for match in TOP_LEVEL_SECTION_PATTERN.finditer(markdown):
        numeral = match.group(1)
        title = clean_title(match.group(2))

        # Ignore duplicate occurrences of the same top-level section.
        if numeral in seen_numerals:
            continue

        seen_numerals.add(numeral)

        candidates.append(
            {
                "numeral": numeral,
                "title": title,
                "position": match.start(),
                "line": markdown.count("\n", 0, match.start()) + 1,
            }
        )

    return candidates


def find_parent_containing_heading(
    heading_position: int,
    heading_text: str,
    parents,
):
    """
    First try to find the parent chunk that literally contains the heading.

    This is the preferred strategy because the heading itself normally
    belongs to the section it introduces.

    Returns:
        parent_index or None
    """

    normalized_heading = normalize_for_matching(heading_text)

    for parent in parents:
        content = parent.content or ""

        if normalized_heading in normalize_for_matching(content):
            return parent.parent_index

    return None


def locate_parent_positions(markdown: str, parents):
    """
    Locate each parent chunk approximately in the raw Markdown.

    We search sequentially instead of using:

        markdown.find(snippet, heading_position)

    independently for every heading.

    Sequential searching prevents repeated text such as:

        "II Éléments propres"

    from constantly resolving to the first occurrence in the document.

    Returns:

        {
            parent_index: start_position,
            ...
        }
    """

    positions = {}

    cursor = 0

    for parent in parents:
        content = (parent.content or "").strip()

        if not content:
            continue

        lines = [
            line.strip()
            for line in content.splitlines()
            if line.strip()
        ]

        if not lines:
            continue

        # Use a reasonably long prefix to reduce accidental matches.
        prefix = "\n".join(lines[:3])[:PARENT_PREFIX_LENGTH]

        position = markdown.find(prefix, cursor)

        if position == -1:
            # Fallback: first non-empty line.
            first_line = lines[0][:PARENT_PREFIX_LENGTH]
            position = markdown.find(first_line, cursor)

        if position == -1:
            # We cannot reliably locate this parent.
            # Do not fabricate a position.
            continue

        positions[parent.parent_index] = position

        cursor = position + max(len(prefix), 1)

    return positions


def find_closest_parent_after_heading(
    heading_position: int,
    parent_positions: dict[int, int],
):
    """
    Fallback strategy.

    Find the first parent whose start position is after the heading.

    This is only used if the heading itself could not be found inside
    a parent chunk.
    """

    candidates = [
        (position, parent_index)
        for parent_index, position in parent_positions.items()
        if position >= heading_position
    ]

    if not candidates:
        return None

    candidates.sort()
    return candidates[0][1]


# ---------------------------------------------------------------------------
# Suggest mode
# ---------------------------------------------------------------------------

async def suggest(document_id: str):
    async with async_session_maker() as session:

        doc = (
            await session.execute(
                select(Document).where(
                    Document.id == uuid.UUID(document_id)
                )
            )
        ).scalar_one()

        parents = (
            await session.execute(
                select(DocumentParentChunk)
                .where(
                    DocumentParentChunk.document_id == doc.id
                )
                .order_by(DocumentParentChunk.parent_index)
            )
        ).scalars().all()

        markdown = doc.parsed_markdown or ""

        print("Scanning Markdown for top-level section headings...\n")

        candidates = get_heading_candidates(markdown)

        if not candidates:
            print("No top-level section headings were detected.")
            return

        print(f"Detected {len(candidates)} unique top-level sections.\n")

        # Locate parent chunks once.
        parent_positions = locate_parent_positions(
            markdown,
            parents,
        )

        for candidate in candidates:

            numeral = candidate["numeral"]
            title = candidate["title"]
            position = candidate["position"]
            line = candidate["line"]

            # Reconstruct the actual heading text.
            heading_text = f"{numeral} {title}"

            # Preferred:
            # the parent chunk actually containing the heading.
            parent_index = find_parent_containing_heading(
                heading_position=position,
                heading_text=heading_text,
                parents=parents,
            )

            mapping_method = "heading contained in parent"

            # Fallback:
            # first parent beginning after the heading.
            if parent_index is None:
                parent_index = find_closest_parent_after_heading(
                    heading_position=position,
                    parent_positions=parent_positions,
                )

                mapping_method = "first parent after heading"

            print(
                f"  line {line:<5} "
                f"parent_index >= {parent_index!s:<4} "
                f"[{mapping_method}] "
                f"'{numeral} {title}'"
            )

        print(
            "\nOnly the top-level Roman-numbered Markdown headings above "
            "should normally become ChapterParts."
        )

        print(
            "\nReview the boundaries manually, then fill BOUNDARIES "
            "at the bottom of this file."
        )

        print(
            "\nExample:"
        )

        print(
            'BOUNDARIES = ['
        )

        for candidate in candidates:
            numeral = candidate["numeral"]
            title = candidate["title"]
            position = candidate["position"]

            parent_index = find_parent_containing_heading(
                heading_position=position,
                heading_text=f"{numeral} {title}",
                parents=parents,
            )

            if parent_index is None:
                parent_index = find_closest_parent_after_heading(
                    heading_position=position,
                    parent_positions=parent_positions,
                )

            print(
                f'    ({parent_index}, "{title}"),'
            )

        print("]")


# ---------------------------------------------------------------------------
# Apply mode
# ---------------------------------------------------------------------------

async def apply(
    document_id: str,
    boundaries: list[tuple[int, str]],
):
    """
    boundaries:

        [
            (parent_index_start, title),
            ...
        ]

    Must be sorted ascending by parent_index_start.

    Every parent chunk from one boundary until the next boundary
    belongs to that ChapterPart.
    """

    if not boundaries:
        print(
            "BOUNDARIES is empty — fill it in after reviewing "
            "`suggest` output."
        )
        return

    # Defensive validation.
    boundaries = sorted(boundaries, key=lambda x: x[0])

    async with async_session_maker() as session:

        doc_uuid = uuid.UUID(document_id)

        parents = (
            await session.execute(
                select(DocumentParentChunk)
                .where(
                    DocumentParentChunk.document_id == doc_uuid
                )
                .order_by(DocumentParentChunk.parent_index)
            )
        ).scalars().all()

        if not parents:
            print("No parent chunks found for this document.")
            return

        # ---------------------------------------------------------------
        # Create ChapterParts
        # ---------------------------------------------------------------

        parts = []

        for order_index, (start_index, title) in enumerate(boundaries):

            part = ChapterPart(
                id=uuid.uuid4(),
                document_id=doc_uuid,
                title=title,
                order_index=order_index,
            )

            parts.append(
                (
                    start_index,
                    part,
                )
            )

            session.add(part)

        await session.flush()

        # ---------------------------------------------------------------
        # Assign parent chunks
        # ---------------------------------------------------------------

        assigned = 0

        for parent in parents:

            matching_part = None

            for start_index, part in parts:

                if parent.parent_index >= start_index:
                    matching_part = part
                else:
                    break

            if matching_part is not None:
                parent.part_id = matching_part.id
                assigned += 1

        await session.commit()

        print(
            f"Created {len(parts)} parts, "
            f"assigned {assigned}/{len(parents)} parent chunks."
        )


# ---------------------------------------------------------------------------
# MANUAL BOUNDARIES
# ---------------------------------------------------------------------------
#
# DO NOT fill these with guessed indices.
#
# First run:
#
#     uv run python assign_parts.py suggest <document_id>
#
# Then copy the verified parent indices here.
#
# The expected structure for THIS document is:
#
#   I   Sous-espaces stables et endomorphismes induits
#   II  Éléments propres
#   III Endomorphismes et matrices diagonalisables
#   IV  Endomorphismes et matrices trigonalisables
#   V   Utilisations des polynômes annulateurs
#
# The "1 ...", "2 ...", etc. sections inside II and V are NOT
# top-level ChapterParts. They remain inside their parent Part.
#
# ---------------------------------------------------------------------------

BOUNDARIES: list[tuple[int, str]] = [
    # Example only — replace with the actual output from `suggest`:
    #
    # (0, "Sous-espaces stables et endomorphismes induits"),
    # (8, "Éléments propres"),
    # (25, "Endomorphismes et matrices diagonalisables"),
    # (32, "Endomorphismes et matrices trigonalisables"),
    # (36, "Utilisations des polynômes annulateurs"),
]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage:")
        print(
            "  uv run python assign_parts.py "
            "suggest <document_id>"
        )
        print(
            "  uv run python assign_parts.py "
            "apply <document_id>"
        )
        sys.exit(1)

    mode = sys.argv[1]
    document_id = sys.argv[2]

    if mode == "suggest":

        asyncio.run(
            suggest(document_id)
        )

    elif mode == "apply":

        asyncio.run(
            apply(
                document_id,
                BOUNDARIES,
            )
        )

    else:

        print(
            f"Unknown mode '{mode}', "
            "expected 'suggest' or 'apply'."
        )

        sys.exit(1)

















        curl -X 'POST' \
  'http://127.0.0.1:8000/retrieve/' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "query": "Comment montrer qu'\''un endomorphisme qui stabilise tous les sous-espaces est une homothétie ?",
  "limit": 5
}'
Request URL
http://127.0.0.1:8000/retrieve/
Server response
Code	Details
200	
Response body
Download
{
  "query": "Comment montrer qu'un endomorphisme qui stabilise tous les sous-espaces est une homothétie ?",
  "results": [
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 169,
      "content": "## **Théorème 68**\n> Lorsqu'il existe un polynôme scindé annulant $u$, c'est-à-dire lorsque le polynôme minimal de $u$ est scindé, alors $E$ peut se décomposer en une somme directe de sous-espaces stables par $u$ sur chacun desquels $u$ induit la somme d'une homothétie et d'un endomorphisme nilpotent.\n\nDémonstration page 129\n\n--- Solution (Théorème 68) ---\n\n**Théorème 68** Si $u$ est annulé par un polynôme scindé $\\prod_{i=1}^r (X - \\lambda_i)^{\\alpha_i}$ où les scalaires $\\lambda_1, \\dots, \\lambda_r$ sont distincts deux à deux, alors le lemme des noyaux permet d’écrire :\n\n$$\\text{Ker } P(u) = \\bigoplus_{k=1}^r \\text{Ker } (u - \\lambda_i \\text{ Id})^{\\alpha_i}.$$\n\nPour tout $i \\in [\\![1, r]\\!]$, le sous-espace vectoriel $E_i = \\text{Ker } (u - \\lambda_i \\text{ Id})^{\\alpha_i}$ est stable par $u$ et l’endomorphisme $u_i$ induit par $u$ sur $E_i$ vérifie $(u_i - \\lambda_i \\text{ Id}_{E_i})^{\\alpha_i} = 0$. Ainsi, l’endomorphisme $n_i = u_i - \\lambda_i \\text{ Id}_{E_i}$ est nilpotent et $u_i$ est la somme de l’homothétie $\\lambda_i \\text{ Id}_{E_i}$ et d’un endomorphismes nilpotent.\n\nL’endomorphisme induit $u_i$ est donc la somme d’une homothétie et d’un endomorphisme nilpotent.\n\n\n\n## S'entraîner et approfondir"
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 207,
      "content": "**2.3** Soit $E$ un espace vectoriel de dimension finie.\nDéterminer les endomorphismes stabilisant tous les hyperplans de $E$.\n\n--- Solution (Exercice 2.3) ---\n\n**2.3** Il est clair que les homothéties stabilisent les hyperplans.\n\nRéciproquement, soit $u$ un endomorphisme stabilisant tous les hyperplans, on va prouver qu'il s'agit d'une homothétie en établissant que, pour tout vecteur $x \\in E$, la famille $(x, u(x))$ est liée (voir l'exercice 1 de la page 65).\n\nSupposons par l'absurde, qu'il existe un vecteur $x$ non nul tel que $u(x)$ n'appartienne pas à $Kx$. La famille $(x, u(x))$ est alors libre, on peut donc la compléter en une base $(x, u(x), e_3, \\dots, e_n)$ de $E$. L'endomorphisme $u$ ne stabilise donc pas l'hyperplan $Vect(x, e_3, \\dots, e_n)$, ce qui est absurde.\n\nAinsi, si $u$ stabilise les hyperplans, alors $u$ est une homothétie.\n\n\n***Solution des exercices***"
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 174,
      "content": "## **Exercice 4**\n\n1. Pour tout $i \\in [1, n]$, le sous-espace $E_i$ est stable par $u \\in L(E)$ si, et seulement s'il existe $\\lambda_i \\in K$ tel que $u(e_i) = \\lambda_i e_i$. Les endomorphismes cherchés sont donc ceux dont la matrice dans la base $B$ est diagonale.\n2. Les espaces $F_i$ sont stables par $u$ si, et seulement si, pour tout $i \\in [1, n]$, $u(e_i) \\in F_i$. Les endomorphismes cherchés sont donc ceux dont la matrice dans la base $B$ est triangulaire supérieure."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 19,
      "content": "## **Proposition 5**\nSi les endomorphismes $u$ et $v$ commutent, c’est-à-dire si $u \\circ v = v \\circ u$, alors les sous-espaces propres de l’un sont stables par l’autre.\n\n**Démonstration.** Soit $\\lambda$ une valeur propre de $u$ ; comme $u$ et $v$ commutent, il en est de même de $(u - \\lambda \\text{Id}_E)$ et $v$. D’après la proposition 1 de la page 65, $E_\\lambda(u) = \\text{Ker}(u - \\lambda \\text{Id}_E)$ est stable par $v$. $\\square$"
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 4,
      "content": "**Proposition 2**\nSi $F$ est un sous-espace vectoriel de $E$ engendré par une famille $(e_i)_{i \\in I}$, alors $F$ est stable par $u$ si, et seulement si :\n$$\\forall i \\in I \\quad u(e_i) \\in F.$$\n\nDémonstration page 108\n\n--- Solution (Proposition 2) ---\n\n## **Proposition 2**\n\n- Supposons $F$ stable par $u$. Pour tout $i \\in I$, comme $e_i \\in F$ et $F$ est stable par $u$, on a $u(e_i) \\in F$.\n- Réciproquement, supposons que, pour tout $i \\in I$, $u(e_i) \\in F$ et montrons que $F$ est stable par $u$. Soit $x \\in F$, il existe une famille de scalaires presque nulle, $(\\lambda_i)_{i \\in I}$, telle que $x = \\sum_{i \\in I} \\lambda_i e_i$. Par linéarité de $u$, on a $u(x) = \\sum_{i \\in I} \\lambda_i u(e_i)$ **donc** $u(x) \\in F$. Par suite, $F$ est stable par $u$."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 208,
      "content": "**2.4** Soit $F$ un sous-espace vectoriel de $E$ et $\\mathcal{L}_F(E)$ l'ensemble des endomorphismes stabilisant $F$.\n1. Montrer que l'application $\\varphi : u \\mapsto u_F$ est un morphisme d'algèbres de $\\mathcal{L}_F(E)$ vers $\\mathcal{L}(F)$.\n2. On suppose $F$ de dimension finie. Montrer que l'inverse de tout élément inversible $u$ de $\\mathcal{L}_F(E)$ stabilise aussi $F$ et que l'on a :\n$$(u^{-1})_F = (u_F)^{-1}.$$\n3. En considérant l'endomorphisme de $\\mathbb{K}(X)$ qui à $P$ associe $XP$, prouver que le résultat de la question précédente est faux si $F$ n'est pas de dimension finie.\n4. On suppose que $F$ possède un supplémentaire.\nMontrer que le morphisme $u \\mapsto u_F$ de $\\mathcal{L}_F(E)$ vers $\\mathcal{L}(F)$ est surjectif.\n\n$\\star$ **2.5** Soit $u$ et $v$ deux endomorphismes d'un espace vectoriel $E$ de dimension finie tels que $v$ soit nilpotent et vérifie $u \\circ v = v \\circ u$. Montrer que l'on a :\n$$\\det(u + v) = \\det u.$$\n\n--- Solution (Exercice 2.4) ---\n\n**2.4** 1. Il est évident que $\\text{Id}_E$ appartient à $\\mathcal{L}_F(E)$ et que l’on a $\\varphi(\\text{Id}_E) = \\text{Id}_F$.\nSoit $(*u, v*) \\in \\mathcal{L}_F(E)^2$ et $(\\alpha, \\beta) \\in \\mathbb{K}^2$.\nPour tout $x \\in F$, on a $u(x) \\in F$, $v(x) \\in F$ et par suite $(\\alpha u + \\beta v)(x) \\in F$.\nL’application $\\alpha u + \\beta v$ appartient donc à $\\mathcal{L}_F(E)$ et $(\\alpha u + \\beta v)_F = \\alpha u_F + \\beta v_F$.\nAinsi, $\\mathcal{L}_F(E)$ est un sous-espace vectoriel de $\\mathcal{L}(E)$ et $\\varphi$ est linéaire.\nSoit $(*u, v*) \\in \\mathcal{L}_F(E)^2$.\nPour tout $x \\in F$, on a $v(x) \\in F$ puis $u(v(x)) \\in F$. Ainsi $u \\circ v$ appartient à $\\mathcal{L}_F(E)$ et $(u \\circ v)(x) = u_F(v_F(x))$, donc $(u \\circ v)_F = u_F \\circ v_F$.\nPar suite, $\\mathcal{L}_F(E)$ est une algèbre et $\\varphi$ est un morphisme d’algèbres de $\\mathcal{L}_F(E)$ vers $\\mathcal{L}(F)$.\n\n2. Soit $u$ appartenant à $\\mathcal{L}_F(E) \\cap \\mathcal{GL}(E)$. L’endomorphisme induit $u_F$ est injectif (car $\\text{Ker } u_F = F \\cap \\text{Ker } u$). Comme $F$ est de dimension finie, le théorème du rang s’applique et implique la surjectivité et donc la bijectivité de $u_F$.\nPour tout $x$ de $F$, l’unique antécédent $u^{-1}(x)$ de $x$ par $u$ appartient donc à $F$. Ainsi, $u^{-1}$ appartient à $\\mathcal{L}_F(E)$. La relation $u \\circ u^{-1} = u^{-1} \\circ u = \\text{Id}_E$ entraîne :\n$$u_F \\circ (u^{-1})_F = (u^{-1})_F \\circ u_F = \\text{Id}_F,$$\npuis $(u^{-1})_F = (u_F)^{-1}$.\n\n3. L’endomorphisme $u : Q \\mapsto XQ$, de l’espace des fractions rationnelles $\\mathbb{K}(X)$, est inversible et stabilise $F = \\mathbb{K}[X]$ mais l’endomorphisme induit $u_F$ n’est pas surjectif car l’unité 1 n’appartient pas à l’image de $\\mathbb{K}[X]$ par $u$. Le résultat de la question précédente n’est donc pas vrai si $F$ n’est pas de dimension finie.\n\n4. Supposons que le sous-espace vectoriel $F$ possède un supplémentaire que l’on notera $G$ et notons $p$ la projection de $E$ sur $F$ parallèlement à $G$.\nSoit $v \\in \\mathcal{L}(F)$. L’application $u : E \\to *E, x* \\mapsto v \\circ p(x)$ est un élément de $\\mathcal{L}_F(E)$ et $u_F = v$ ; ce qui prouve la surjectivité de $\\varphi$."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 7,
      "content": "**Définition 2**\nSoit $F$ un sous-espace vectoriel stable par $u$. On appelle **endomorphisme induit** par $u$ sur $F$ l'endomorphisme $u_F \\in \\mathcal{L}(F)$ défini par :\n$$\\forall x \\in F \\quad u_F(x) = u(x),$$\n\n\n# Chapitre 2. *Réduction des endomorphismes*\n\n**Attention** On ne peut parler d'endomorphisme induit par $u$ sur un sous-espace vectoriel $F$ que dans la mesure où $F$ est *stable par* $u$. Dans ce cas, on distinguera soigneusement l'endomorphisme induit $u_F$, qui est une application linéaire de $F$ vers $F$, de la restriction $u|_F$ qui est une application linéaire de $F$ vers $E$."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 219,
      "content": "**2.16** Déterminer les sous-espaces stables par l’endomorphisme $u$ canoniquement associé à la matrice réelle :\n$$A = \\begin{pmatrix} 0 & 1 & 1 \\\\ 1 & 0 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}.$$\n\n--- Solution (Exercice 2.16) ---\n\n**2.16** Le polynôme caractéristique de $A$ est $\\chi_A(X) = (X - 1)^2(X + 1)$ et les sous espaces propres sont $E_1 = \\mathbb{R}e_1$ et $E_{-1} = \\mathbb{R}e_{-1}$ avec :\n\n$$e_1 = \\begin{pmatrix} 1 \\\\ 1 \\\\ 0 \\end{pmatrix} \\quad \\text{et} \\quad e_{-1} = \\begin{pmatrix} -1 \\\\ 1 \\\\ 0 \\end{pmatrix}.$$\n\nSoit $F$ un sous-espaces stable par l’endomorphisme $u$.\n\n*   Si $F$ est de dimension 0 ou 3, il est respectivement égal à $\\{0\\}$ ou $\\mathbb{R}^3$.\n*   Si $F$ est de dimension 1, alors $F$ est une droite engendrée par un vecteur propre de $A$ c’est-à-dire $F = \\mathbb{R}e_1$ ou $F = \\mathbb{R}e_{-1}$.\n*   Si $F$ est de dimension 2, le polynôme caractéristique de l’endomorphisme induit est un polynôme de degré deux divisant $\\chi_A$.\n    Il vaut donc $(X - 1)^2$ ou $(X - 1)(X + 1)$.\n    Dans le premier cas, $F$ est contenu dans le noyau de $(A - I_3)^2$ qui est égal au plan d’équation $2x - 2y - z = 0$.\n    Dans le second cas, $F$ contient un vecteur propre associé à 1 et un vecteur propre associé à $-1$. Il est donc égal à $\\mathbb{R}e_1 \\oplus \\mathbb{R}e_{-1}$.\n\nAinsi, les sous-espaces stables par $u$ sont $\\{0\\}$, $\\mathbb{R}^3$, $\\mathbb{R}e_1$, $\\mathbb{R}e_{-1}$, $\\mathbb{R}e_1 \\oplus \\mathbb{R}e_{-1}$ et le plan d’équation $2x - 2y - z = 0$."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 196,
      "content": "## **Exercice 31**\n\n1. • Si $p = 0$, on a $\\pi_p = X$.\n   • Si $p = \\text{Id}_E$, on a $\\pi_p = X - 1$.\n   • Dans les autres cas, comme $p$ n’est pas une homothétie et vérifie $p^2 = p$, on a $\\pi_p = X^2 - X$.\n\n2. • Si $s = \\text{Id}_E$, on a $\\pi_s = X - 1$.\n   • Si $s = -\\text{Id}_E$, on a $\\pi_s = X + 1$.\n   • Dans les autres cas, comme $s$ n’est pas une homothétie et vérifie $s^2 = \\text{Id}_E$, on a $\\pi_s = X^2 - 1$.\n\n\n**_Démonstrations et solutions des exercices du cours_**"
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 157,
      "content": "### **Corollaire 61**\nSoit $u \\in \\mathcal{L}(E)$ diagonalisable et $F$ un sous-espace vectoriel de $E$ stable par $u$. L'endomorphisme induit par $u$ sur $F$ est alors diagonalisable.\n\n\nDémonstration page 127\n\n\nOn dit qu'une famille $(u_i)_{i \\in I}$ d'endomorphismes de $E$ est *simultanément diagonalisable* s'il existe une base $\\mathcal{B}$ de $E$ dans laquelle les matrices des $u_i$ sont diagonales.\nUne telle base s'appelle alors une base de *diagonalisation simultanée*.\n\n**p.127** | **Exercice 37** Montrer qu'une famille d'endomorphismes de $E$ est simultanément diagonalisable si, et seulement si, elle est composée d'endomorphismes diagonalisables commutant deux à deux.\n\n--- Solution (Corollaire 61) ---\n\n**Corollaire 61** En effet, d'après le théorème 60 le polynôme minimal $\\pi_u$ de $u$ est scindé à racines simples et, comme $\\pi_u(u_F) = 0$, on déduit du même théorème que $u_F$ est diagonalisable."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 148,
      "content": "### **Théorème 56 (Théorème de Cayley-Hamilton)**\nSoit $u \\in \\mathcal{L}(E)$ avec $E$ de dimension **finie**.\nLe polynôme caractéristique de $u$ annule $u$, c’est-à-dire $\\chi_u(u) = 0$.\n\n**Principe de démonstration.** On utilise le lemme précédent, puis les exercices 17 de la page 81 et 33 de la page précédente sur les matrices compagnons.\n<mark>Démonstration (non exigible) page 124</mark>\n\n**Attention** Comme il fait intervenir le polynôme caractéristique de $u \\in \\mathcal{L}(E)$, le théorème de Cayley-Hamilton n’a de sens que si $E$ est de dimension **finie**.\n\n--- Solution (Théorème 56) ---\n\n**Théorème 56** Soit $x \\in E \\setminus \\{0\\}$ et $F_x$ le plus petit sous-espace vectoriel de $E$ stable par $u$ et contenant $x$ dont on note $p$ la dimension. D'après le lemme précédent, $\\left( u^k(x) \\right)_{0 \\le k \\le p-1}$ est une base de $F_x$ donc il existe $(a_0, \\dots, a_{p-1}) \\in \\mathbb{K}^p$ tel que\n$u^p(x) = - \\sum_{k=0}^{p-1} a_k u^k(x)$. Il en résulte que la matrice de l'endomorphisme induit $u_{F_x}$ par $u$ sur $F_x$ dans la base $\\left( u^k(x) \\right)_{0 \\le k \\le p-1}$ est une matrice compagnon.\nOr, d'après les exercices 17 et 33, si $A$ est une matrice compagnon, alors $\\pi_A = \\chi_A$. Par conséquent, $\\pi_{u_{F_x}} = \\chi_{u_{F_x}}$. D'après la proposition 32, $\\chi_{u_{F_x}}$ divise $\\chi_u$ donc $\\chi_u(u_{F_x}) = 0$. Comme $x \\in E_x$, on peut écrire :\n$$\\chi_u(u)(x) = \\chi_u(u_{F_x})(x) = 0.$$\nCette dernière égalité a été établie pour tout $x \\in E \\setminus \\{0\\}$. On en déduit que $\\chi_u(u) = 0$."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 3,
      "content": "**Proposition 1**\nSi les endomorphismes $u$ et $v$ commutent, c'est-à-dire si $u \\circ v = v \\circ u$, alors $\\text{Ker } v$ et $\\text{Im } v$ sont stables par $u$.\n\nDémonstration page 108\n\n--- Solution (Proposition 1) ---\n\n## **Proposition 1**\n\n- Soit $x \\in Ker  v$ ; on a $v(u(x)) = v \\circ u(x) = u \\circ v(x) = u(0) = 0$ **donc** $u(x)$ appartient à $Ker  v$. Ainsi, $Ker  v$ est stable par $u$.\n- Soit $y \\in Im  v$ ; il existe $x \\in E$ tel **que** $y = v(x)$.\n  Par suite $u(y) = u \\circ v(x) = v \\circ u(x) = v(u(x)) \\in Im  v$ ; **donc** $Im  v$ est stable par $u$."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 0,
      "content": "### **Définition 1**\n> Un sous-espace vectoriel $F$ de $E$ est dit **stable** par $u$ si $u(F) \\subset F$.\n>\n> On dit aussi que $u$ **stabilise** $F$."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 81,
      "content": "### **Proposition 32**\n> Si $F$ est un sous-espace vectoriel de $E$ stable par $u$, alors le polynôme caractéristique, $\\chi_{u_F}$, de l'endomorphisme induit par $u$ sur $F$ divise $\\chi_u$.\n\n**Principe de démonstration.** Calculer le polynôme caractéristique de la matrice de $u$ dans une base adaptée à $F$ (base de $F$ complétée en une base de $E$). \n<span style=\"border: 1px solid black; border-radius: 10px; padding: 2px 10px;\">Démonstration page 114</span>\n\n--- Solution (Proposition 32) ---\n\n**Proposition 32** Soit $p$ la dimension de $F$ et $\\mathcal{B} = (e_1, \\dots, e_n)$ une base de $E$ adaptée à $F$, c'est-à-dire telle que $\\mathcal{B}_F = (e_1, \\dots, e_p)$ soit une base de $F$.\n\nLa matrice de $u$ dans $\\mathcal{B}$ est alors de la forme $\\begin{pmatrix} A & B \\\\ 0 & D \\end{pmatrix}$, où $A$ est la matrice de $u_F$ dans la base $\\mathcal{B}_F$. Le polynôme caractéristique de $u$, égal à $\\chi_A(X)\\chi_D(X)$ est donc divisible par le polynôme caractéristique $\\chi_A(X)$ de $u_F$."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 25,
      "content": "**Proposition 9**\nSi $F$ est un sous-espace vectoriel de $E$ stable par $u$, les valeurs propres de l'endomorphisme $u_F$ induit par $u$ sur $F$ sont les valeurs propres $\\lambda$ de $u$ telles que $E_\\lambda(u) \\cap F \\neq \\{0\\}$. On a alors :\n$$E_\\lambda(u_F) = E_\\lambda(u) \\cap F.$$\n\n**Démonstration.** Par définition $E_\\lambda(u_F) = \\{x \\in F \\mid u_F(x) = \\lambda x\\}$ donc :\n$$E_\\lambda(u_F) = \\{x \\in F \\mid u(x) = \\lambda x\\} = F \\cap E_\\lambda(u). \\quad \\square$$\n\n## 2 Rappels sur les matrices semblables\n\nDans cette partie, $E$ est supposé de dimension finie $n$.\nLes résultats rappelés ont été vus en première année ; leurs démonstrations ne seront donc pas redonnées."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 134,
      "content": "**Exercice 29** (Approfondissement)\n\nOn veut montrer qu’un endomorphisme est trigonalisable si, et seulement s’il est annulé par un polynôme scindé.\n1. Montrer par récurrence sur la dimension de $E$ que si un endomorphisme $u$ de $E$ est annulé par un polynôme scindé, alors il est trigonalisable.\n2. Montrer que si $u$ est un endomorphisme trigonalisable de $E$, alors $\\chi_u$ annule $u$.\n3. Conclure.\n\n--- Solution (Exercice 29) ---\n\n## **Exercice 29**\n\n1. Le résultat est immédiat si $E$ est de dimension 1.\n\n   Supposons désormais le résultat vrai pour tout espace vectoriel de dimension $\\dim E - 1$ et considérons un endomorphisme $u$ annulé par un polynôme scindé $P(X) = \\prod_{k=1}^{m} (X - \\beta_k)$. La relation $(u - \\beta_1 \\text{Id}_E) \\circ \\dots \\circ (u - \\beta_m \\text{Id}_E) = 0$ implique alors qu'il existe $i \\in [\\![1, m]\\!]$ tel que $(u - \\beta_i \\text{Id}_E)$ soit non inversible. L'endomorphisme non injectif $(u - \\beta_i \\text{Id}_E)$ est alors d'image $F$ strictement contenue dans $E$. Choisissons alors un hyperplan $H$ de $E$ contenant $F$.\n\n   Comme $F = \\text{Im}(u - \\beta_i \\text{Id}_E) \\subset H$, l'hyperplan $H$ est stable par $(u - \\beta_i \\text{Id}_E)$ et donc par $u$. L'endomorphisme induit $u_H$ vérifie $P(u_H) = 0$ ; il est donc annulé par un polynôme scindé et, par hypothèse de récurrence, trigonalisable.\n\n   Il existe donc une base $\\mathcal{B}'$ de $H$ dans laquelle la matrice de $u_H$ est triangulaire supérieure. Dans toute base $\\mathcal{B}$ de $E$, obtenue en complétant $\\mathcal{B}'$ par un seul vecteur, la matrice de $u$ est triangulaire supérieure ; ce qui conclut la récurrence.\n\n\n# Chapitre 2. Réduction des endomorphismes\n\n2. Supposons que la matrice de $u$ dans la base $\\mathcal{B} = (e_1, \\dots, e_n)$ soit de la forme :\n\n$$\n\\begin{pmatrix}\n\\alpha_1 & \\cdots & \\cdots & * \\\\\n0 & \\ddots & & \\vdots \\\\\n\\vdots & \\ddots & \\ddots & \\vdots \\\\\n0 & \\cdots & 0 & \\alpha_n\n\\end{pmatrix}\n$$\n\nNotons alors $F_i$ le sous-espace vectoriel $\\text{Vect}(e_1, \\dots, e_i)$. Les relations\n$$(u - \\alpha_i \\text{Id}_E)(e_i) \\in F_{i-1} \\quad \\text{et} \\quad \\forall k \\in [\\![1, i - 1]\\!] \\quad u(e_k) \\in F_{i-1}$$\nmontrent que l’on a $(u - \\alpha_i \\text{Id}_E)(F_i) \\subset F_{i-1}$ pour tout $i$. Le sous-espace vectoriel :\n$$(u - \\alpha_1 \\text{Id}_E) \\circ \\dots \\circ (u - \\alpha_n \\text{Id}_E)(F_n)$$\nest donc contenu dans :\n$$(u - \\alpha_1 \\text{Id}_E) \\circ \\dots \\circ (u - \\alpha_{n-1} \\text{Id}_E)(F_{n-1})$$\net par itération dans $(u - \\alpha_1 \\text{Id}_E)(F_1)$ qui est réduit à $\\{0\\}$. On a donc $\\chi_u(u) = 0$.\n\n3. D’après la question précédente et le théorème 48 de la page 93, si $u$ est un endomorphisme trigonalisable de $E$, alors il est annulé par un polynôme scindé. La réciproque ayant été montrée à la première question, l’équivalence est prouvée."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 198,
      "content": "**Exercice 34** Notons $F_x = \\text{Vect} \\left( \\left( u^k(x) \\right)_{k \\in \\mathbb{N}} \\right)$.\n\n*   Si $F$ est un sous-espace vectoriel de $E$ stable par $u$ et contenant $x$, on a :\n    $$\\forall k \\in \\mathbb{N} \\quad u^k(x) \\in F,$$\n    donc $F_x \\subset F$. Comme $F_x$ est stable par $u$ et contient $x$, $F_x$ est le plus petit sous-espace vectoriel de $E$ stable par $u$ et contenant $x$.\n\n*   La famille de $F_x$, $\\left( u^k(x) \\right)_{0 \\le k \\le p}$, contient $p$ éléments, il suffit donc de montrer qu'elle est génératrice pour conclure.\n    Soit $y \\in F_x$. Il existe $P \\in \\mathbb{K}[X]$ tel que $y = P(u)(x)$.\n    Par ailleurs, la famille à $p+1$ éléments, $\\left( u^k(x) \\right)_{0 \\le k \\le p}$, est liée donc il existe $T \\in \\mathbb{K}_p[X]$ non nul tel que $T(u)(x) = 0$.\n    On effectue la division euclidienne de $P$ par $T$ :\n    $$P = QT + R \\quad \\text{avec} \\quad \\deg(R) *< p.*$$\n    On en déduit $y = P(u)(x) = Q(u) \\circ T(u)(x) + R(u)(x)$. Comme $T(u)(x) = 0$ et $\\deg(R) < p - 1$, on a alors $y \\in \\text{Vect} \\left( \\left( u^k(x) \\right)_{0 \\le k \\le p-1} \\right)$.\n    En conclusion, la famille $\\left( u^k(x) \\right)_{0 \\le k \\le p-1}$ engendre $F_x$, c'est donc une base."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 44,
      "content": "## **Proposition 17**\nPour tout $(*P, Q*) \\in \\mathbb{K}[X]^2$, les endomorphismes $P(u)$ et $Q(u)$ commutent.\nEn particulier, pour tout $P \\in \\mathbb{K}[X]$, $\\text{Im } P(u)$ et $\\text{Ker } P(u)$ sont des sous-espaces stables par $u$.\n\n**Démonstration.** Le fait que pour tout couple d'entiers $(k, \\ell)$, les endomorphismes $u^k$ et $u^\\ell$ commutent, permet d'obtenir l'égalité $P(u) \\circ Q(u) = Q(u) \\circ P(u)$.\nIl suffit alors d'appliquer la proposition 1 de la page 65 à $v = P(u)$ qui commute avec $u$. $\\square$"
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 9,
      "content": "## Corollaire 3 (**Traduction matricielle de la stabilité**)\n\nSoit $F$ un sous-espace vectoriel de $E$ de dimension $p$ et $B = (e_1, \\dots, e_n)$ une base de $E$ adaptée à $F$, c'est-à-dire telle que $B' = (e_1, \\dots, e_p)$ soit une base de $F$.\n\nL'endomorphisme $u$ stabilise $F$ si, et seulement si, sa matrice dans la base $B$ est de la forme $\\begin{pmatrix} A & C \\\\ 0 & B \\end{pmatrix}$, avec $A \\in M_p(K)$.\n\nDans ce cas, $A$ est la matrice dans la base $B'$ de l'endomorphisme induit $u_F$.\n\n>Démonstration page 108<\n\n--- Solution (Corollaire 3) ---\n\n## **Corollaire 3**\n\n**Comme** $(e_1, \\dots, e_p)$ est une base de $F$, l'espace vectoriel $F$ est stable par $u \\in L(E)$ si, et seulement si, $\\forall j \\in [1, p]$ $u(e_j) \\in F$ c'est-à-dire si, et seulement si, les $p$ premières colonnes de la matrice de $u$ dans la base $B$ ont leurs $n-p$ derniers coefficients nuls, c'est-à-dire si, et seulement si, cette matrice est de la forme :\n\n$$\n\\begin{pmatrix}\nA & C \\\\\n0 & B\n\\end{pmatrix} \\quad avec \\quad A \\in M_p(K).\n$$\n\nL'interprétation de $A$ est alors claire."
    },
    {
      "document_id": "bdcc1c74-7b21-4403-a7e9-4095f19b4019",
      "chunk_index": 200,
      "content": "**Exercice 36**\n*   Commençons par le montrer pour $r = 2$. D'après le théorème de Bézout, il existe $(U_1, U_2) \\in \\mathbb{K}[X]^2$ tel que $P_1 U_1 + P_2 U_2 = 1$.\n    On a donc $P_1(u) \\circ U_1(u) + P_2(u) \\circ U_2(u) = \\text{Id}_E$ ce qui, pour tout $x \\in E$ donne :\n    $$x = \\underbrace{P_2(u) \\circ U_2(u)(x)}_{\\in \\text{Ker } P_1(u)} + \\underbrace{P_1(u) \\circ U_1(u)(x)}_{\\in \\text{Ker } P_2(u)}.$$\n\n\n# Chapitre 2. *Réduction des endomorphismes*\n\nAinsi, les projections associées à la décomposition :\n$$ Ker  P(u) = Ker  P_1(u) \\oplus Ker  P_2(u) $$\nsont les endomorphismes $(U_1 P_1)(u)$ et $(U_2 P_2)(u)$.\n\n- Soit $r \\geqslant 3$ tel que le résultat soit vrai au rang $r-1$. Considérons $(P_1, \\dots, P_r)$, une famille de $r$ polynômes deux à deux premiers entre eux, et $P = \\prod_{k=1}^{r} P_k$ tel que $P(u) = 0$.\n\nOn pose alors $Q = \\prod_{k=1}^{r-1} P_k$ ; les polynômes $Q$ et $P_r$ sont premiers entre eux (car si un polynôme irréductible divise $Q$ et $P_r$, il divise l'un des $P_k$, avec $k \\in I[1, r-1]$, et $P_r$, ce qui est contraire aux hypothèses).\n\nD'après le premier point, on a $E = Ker  Q(u) \\oplus Ker  P_r(u)$ et il existe des polynômes $Q_1$ et $Q_2$ tels que $Q_1(u)$ soit la projection sur $Ker  Q(u)$ et $Q_2(u)$, celle sur $Ker  P_r(u)$.\n\nSi l'on considère $\\tilde{u}$ l'endomorphisme induit par $u$ sur $Ker  Q(u)$, alors $Q(\\tilde{u}) = 0$.\n\nD'après l'hypothèse de récurrence, on a $Ker  Q(\\tilde{u}) = \\bigoplus_{k=1}^{r-1} Ker  P_k(\\tilde{u})$ et, pour tout $i \\in I[1, r]$, il existe un polynôme $R_i$ tel que , $R_i(\\tilde{u})$ soit la projection sur $Ker  P_i(\\tilde{u})$.\n\nSoit $x \\in E$. Considérons sa décomposition $x = x_1 + \\dots + x_r$ dans la somme directe $\\bigoplus_{k=1}^{r} Ker  P_k(u)$. Le vecteur $x' = x_1 + \\dots + x_{r-1}$ appartient à $Ker  Q(\\tilde{u}) = Ker  Q(u)$. De plus, pour tout $i \\in I[1, r-1]$, $x_i$ appartient à $Ker  P_i(u) = Ker  P_i(\\tilde{u})$ (car $Ker  P_i(\\tilde{u}) = Ker  P_i(u) \\cap Ker  Q(u)$) donc :\n$$ x_i = R_i(\\tilde{u})(x') = R_i(u)(x') = R_i(u)(Q_1(u)). $$\n\nPar conséquent, pour tout $i \\in I[1, r-1]$, la projection sur $Ker  P_i(u)$ est $R_i Q(u)$ ; c'est donc un polynôme en $u$. Celle sur $Ker  P_r(u)$ étant égale à $Q_2(u)$, cela achève la récurrence."
    }
  ]
}