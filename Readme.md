# PrepaMath Tutor

An AI tutor for French "classes préparatoires" (CPGE) mathematics — ingests real textbook chapters, lets a student browse them lesson-by-lesson, and answers questions grounded in whichever section they're currently reading, with full conversation history and a retrieval pipeline whose design choices are backed by a measured benchmark, not assumption.

**Status: active development, not deployed.** Two chapters are fully ingested and working end-to-end (ingestion → navigation → RAG Q&A → persisted chat); see [Known limitations](#known-limitations) and [Next steps](#next-steps) below for exactly what's missing before this is a finished product.

## Table of contents

- [Who this is for](#who-this-is-for)
- [The problem](#the-problem)
- [How it works](#how-it-works)
- [What makes this more than a RAG wrapper](#what-makes-this-more-than-a-rag-wrapper)
- [Tech stack](#tech-stack)
- [Project structure](#project-structure)
- [Getting started](#getting-started)
- [Known limitations](#known-limitations)
- [Next steps](#next-steps)

## Who this is for

**Students** in a French CPGE math track (MP/MPSI and similar) who want to read their course chapter by chapter and ask questions about exactly the section they're stuck on, instead of a generic chatbot that doesn't know what page they're on.

**Anyone reading this repo** — if you're here to evaluate the engineering rather than use the app: this README leads with the parts that show how the system was actually built and validated, not just what it does. In particular, [`evaluation/RESULTS.md`](backend/evaluation/RESULTS.md) is a from-scratch retrieval benchmark that found and fixed four real bugs (one of them silently corrupting a third of the ingested corpus) with before/after numbers for each — that document is the single best entry point if you want to see the engineering process rather than the feature list.

## The problem

Official CPGE math textbooks are long, dense, and proof-heavy. A student re-reading a chapter mid-exercise doesn't want a general-purpose chatbot that might answer from its own training data instead of the actual course — they want an answer grounded in *this exact textbook's* definitions and notation, scoped to *the section they're currently on*, with the freedom to also pull in an earlier definition from elsewhere in the chapter when the question genuinely needs it.

That scoping requirement — "answer from the current section, but don't wall off the rest of the chapter when it's actually relevant" — is the central design problem this project solves, and it's harder than it sounds (see the `classify_node` routing bug in [Next steps](#next-steps)).

## How it works

```
Source PDF
   │  (LlamaParse, external — produces raw markdown)
   ▼
task.py (ingestion CLI)
   │  structural chunking: Définition / Proposition / Théorème / Exercice / ...
   │  section detection: Roman-numeral + numbered-subsection headers → ChapterPart rows
   │  parent/child split: full statement+proof (parent) vs. bare statement (child)
   │  contextual summary (LLM) + embedding (OpenAI, per child chunk)
   ▼
Postgres + pgvector
   │  documents · chapter_part · document_parent_chunk · document_chunk (vector(384))
   │  conversation · message · user (fastapi-users)
   ▼
FastAPI backend
   ├─ /documents, /documents/{id}/parts, /documents/{id}/parts/{id}/chunks
   │     → chapter navigation, reads ChapterPart/DocumentParentChunk directly (no search)
   ├─ /retrieve
   │     → standalone dense-vector search endpoint (benchmarked in evaluation/)
   └─ /documents/{id}/ask  (LangGraph agent, app/services/tutor_graph.py)
         │
         ├─ load_section_node     : load the student's current ChapterPart in full
         ├─ classify_node (LLM)   : does the current section already cover this question?
         ├─ corpus_retrieval_node : if not → dense search across the whole chapter
         └─ generate_node (LLM)   : answer grounded in section content (+ corpus matches
                                     if routed there — section content is never fully
                                     dropped, so a misrouted question still has the
                                     current part as a fallback)
   ▼
React (Vite) frontend
   Welcome → chapter roadmap → per-chapter workspace:
     left panel  = section list + lesson-grouped reading view + exercises (with
                   solutions) in a separate popup, not interleaved with the course
     right panel = chat, scoped to whichever section is open, history persisted
                   server-side and restored on reload
```

## What makes this more than a RAG wrapper

A few decisions worth calling out specifically, because they're the parts that took actual debugging rather than following a tutorial:

- **The retrieval architecture is chosen by measurement, not by default.** [`evaluation/`](backend/evaluation) is a self-contained benchmark harness (49 hand-curated questions, validated against the live DB) that traces every candidate through every pipeline stage. It's what proved dense-only retrieval beats both hybrid (RRF-fused lexical+dense) and reranked (cross-encoder) on this corpus — the opposite of the "textbook hybrid architecture is always better" assumption — and it's what caught an ingestion bug that had silently duplicated **32% of one chapter's rows**. Full writeup with before/after metrics for all four findings: [`evaluation/RESULTS.md`](backend/evaluation/RESULTS.md).
- **Parent/child chunking.** What gets embedded and searched (`DocumentChunk`, the bare statement) is deliberately smaller and more precise than what gets handed to the LLM at answer time (`DocumentParentChunk`, the full statement + proof + examples). Searching short precise text and generating from full context are different jobs; one row can't optimally serve both.
- **Section-aware navigation that isn't search-derived.** `ChapterPart` rows are real structural sections (detected from the source's own Roman-numeral *and* nested numbered headers — see the two-level detection in `task.py`'s `find_sections`), not clusters inferred after the fact. The left panel reads a part's chunks directly; no embedding call is needed to render a lesson.
- **The "which section is this question about" problem is actively routed, not punted to the LLM's context window.** The classify → section-or-corpus split in `tutor_graph.py` exists specifically so "explain this part" and "what's the definition of X from two sections ago" get handled differently — and when that routing was wrong (see [Next steps](#next-steps)), the fix was a prompt rule plus a structural fallback, not a single patch.
- **Content quality bugs were treated as bugs, with evidence.** Several ingestion defects (duplicate unnumbered examples, a page-reference prefix silently breaking heading detection, chapter-section headers bleeding into adjacent chunk content) were root-caused against the actual stored markdown and fixed with before/after verification — not patched blind. See `evaluation/RESULTS.md` findings 1 and 4 for the two that were numerically measured; the section-boundary and heading-duplication fixes in `task.py` and the frontend's `LeftPanel.jsx` content-cleaning pipeline followed the same discipline.

## Tech stack

**Backend** — Python 3.11, FastAPI, SQLAlchemy 2.0 (async) + `asyncpg`, PostgreSQL with `pgvector`, Alembic migrations, `fastapi-users` (JWT + Google OAuth), LangGraph for the agentic answer flow, OpenAI API (`gpt-4o-mini` for generation/classification, `text-embedding-3-small` truncated to 384 dims), `sentence-transformers` cross-encoder (wired in, currently disabled — see evaluation), `tiktoken`, `uv` for dependency management.

**Frontend** — React 19, Vite, React Router, Tailwind CSS v4, `@tailwindcss/typography`, `react-markdown` + `remark-math` + `rehype-katex` for LaTeX rendering, `lucide-react` icons, `framer-motion`.

**Infra (provisioned, not yet all wired in)** — Docker Compose for local Postgres+pgvector and Redis. Redis and Celery are dependencies in `pyproject.toml` for a planned async ingestion queue; ingestion currently runs synchronously via CLI (`task.py`), so neither is actually exercised by the running app yet.

## Project structure

```
backend/
  main.py                      FastAPI app, CORS, router registration
  task.py                      Ingestion CLI: markdown → chunks → Postgres (the whole pipeline)
  app/
    model.py                   SQLAlchemy models (User, Document, ChapterPart,
                                DocumentParentChunk, DocumentChunk, Conversation, Message)
    schema.py                  Pydantic request/response schemas
    auth.py                    fastapi-users setup: JWT backend + Google OAuth
    database.py                Async session/engine setup
    routers/
      chapters.py               /documents, parts, and part-content endpoints
      retrieval.py               /retrieve — standalone dense-search endpoint
      answer.py                  /ask (LangGraph) + /conversation (history restore)
    services/
      retrieval_pipeline.py      lexical/dense/hybrid/rerank, flag-selectable
      rerank.py                  cross-encoder reranking (disabled by default)
      tutor_graph.py              LangGraph nodes: load_section → classify → (corpus) → generate
  evaluation/
    RESULTS.md                   the benchmark writeup — start here
    dataset.json                 49 hand-curated Q&A pairs with expected source chunks
    run_retrieval_eval.py, metrics.py, build_candidates.py, validate_dataset.py
  alembic/                       migrations

prepamath-frontend/
  src/
    pages/                       WelcomePage, RoadmapPage, ChapterWorkspacePage,
                                  LoginPage, RegisterPage, GoogleCallbackPage
    components/
      workspace/
        SplitPanel.jsx            resizable two-pane layout, holds shared selectedPartId
        LeftPanel.jsx              section list, lesson-grouped reading view,
                                   exercises popup, all markdown content-cleaning
        RightPanel.jsx             chat: ask, persist, and restore conversation history
      layout/                     AppShell, Navbar
      background/                 FloatingBackground
    context/AuthContext.jsx       JWT token storage/retrieval
```

## Getting started

### Prerequisites

- Python 3.11+ with [`uv`](https://docs.astral.sh/uv/)
- Node 18+
- Docker (for Postgres+pgvector and Redis)
- An OpenAI API key
- A Google OAuth client ID/secret (only needed if you want Google login to work)

### 1. Infra

```bash
cd backend
docker compose up -d        # Postgres+pgvector on :5432, Redis on :6379
```

### 2. Backend

Create `backend/.env`:

```
postgres_url=postgresql+asyncpg://prepamath:prepamath@localhost:5432/prepamath
SECRET_KEY=<any random string>
OPEN_AI_KEY=<your OpenAI key>
GOOGLE_CLIENT_ID=<optional>
GOOGLE_CLIENT_SECRET=<optional>
```

```bash
cd backend
uv sync
uv run alembic upgrade head
uv run uvicorn main:app --reload
```

### 3. Ingest a chapter

The two source textbook `.md` files are gitignored (copyrighted source material — see `.gitignore`), so you'll need your own LlamaParse-style markdown export of a chapter to ingest:

```bash
uv run python task.py path/to/chapter.md "Chapter Title"
```

This populates `documents`, `chapter_part`, `document_parent_chunk`, and `document_chunk` (including embeddings) for that chapter. Re-running assigns a fresh `document_id` each time — nothing is upserted in place.

### 4. Frontend

```bash
cd prepamath-frontend
npm install
npm run dev
```

Visit `http://localhost:5173`, register an account (or sign in with Google if configured), and open an ingested chapter from the roadmap.

### Running the evaluation harness

```bash
cd backend
uv run python evaluation/validate_dataset.py        # confirm dataset matches current DB
uv run python evaluation/run_retrieval_eval.py       # writes evaluation/results/*.json
uv run python evaluation/metrics.py evaluation/results/dense.json evaluation/results/hybrid.json evaluation/results/reranked.json
```

## Known limitations

Being direct about these rather than letting them surface as surprises:

- **Only 2 chapters are ingested** ("Réduction des endomorphismes", "Espaces vectoriels normés"), and the second is itself incomplete — the source `.md` for topology genuinely stops after "Comparaison de normes"; compacité, connexité par arcs, finite-dimension equivalence-of-norms, and series-in-normed-spaces (all required by the official CPGE syllabus for that chapter) aren't in the source file at all, confirmed by a direct text search, not an ingestion gap.
- **No automated tests.** Everything so far has been validated via the evaluation harness (for retrieval) and manual/scripted verification against the live DB (for ingestion fixes) — solid for what it covers, but there's no CI, no regression suite for the API or the LangGraph flow.
- **`/ask`'s `sources` field is always empty.** The response schema supports returning which chunks grounded an answer, but `answer.py` never populates it — the frontend's source-citation UI has nothing to render yet.
- **Reranking is implemented but disabled.** The cross-encoder model tested (`cross-encoder/mmarco-mMiniLMv2-L12-H384-v1`) measurably favors long passages over short precise definitions on this corpus (see `RESULTS.md` finding 3) — the code path is kept for a future model swap, not deleted.
- **Celery/Redis are provisioned, not used.** Ingestion runs synchronously via CLI; there's no background job queue wired up yet despite both being in `docker-compose.yml` and `pyproject.toml`.
- **Not deployed anywhere.** Local Docker Compose + `uvicorn --reload` + `vite dev` only.

## Next steps

Roughly in the order they'd unblock the most value:

### Content coverage
1. **Ingest the remaining official CPGE syllabus chapters** — the program spans ~15 chapters across two years (see the full program breakdown that drove the `ChapterPart` granularity redesign); only 2 are in the DB today.
2. **Source or re-export the missing back half of the topology chapter** (compacité, connexité, dimension finie, séries vectorielles) — needed to make that chapter's syllabus coverage actually complete rather than a syllabus match for roughly half the official content.
3. Extend `task.py`'s section-subsection detection (currently tuned against these two chapters' actual heading conventions) and re-verify against each new chapter with a dry run before committing to ingestion — the discipline that caught the empty-wrapper-section bug and the plural-heading bug should carry forward, not get skipped under time pressure.

### Retrieval quality
4. **Populate `AskResponse.sources`** in `answer.py` so the frontend can actually show which chunks grounded an answer — the schema and frontend UI both already expect this field, it's just never filled in.
5. **Re-run the reranker experiment with a different cross-encoder** better suited to short formal definitions (the current one's length bias is documented, not fixed) — `evaluation/` is built specifically so this is a rerun-and-compare, not a new harness.
6. Investigate whether a smarter lexical query construction (rather than OR-ing all terms) recovers any of hybrid retrieval's lost precision, now that the lexical channel itself is confirmed functional post-fix.
7. Add eval cases for the `classify_node` routing fix (self-referential "explique cette partie"-style questions) to `evaluation/dataset.json` or a parallel routing-specific eval — right now that fix is verified by code review and the bug report that triggered it, not by a regression suite.

### Product features
8. **Progress tracking** — which lessons/exercises a student has actually viewed, surfaced back in the section list (the UI already has a natural slot for this next to each section's row).
9. **Exercise difficulty/status** — the NeetCode-inspired side-nav redesign deliberately left out fake "solved"/"difficulty" concepts rather than fabricate them; if progress tracking lands, this becomes meaningful instead of decorative.
10. Cross-chapter retrieval/search from the roadmap page, not just within a single open chapter.

### Engineering hygiene
11. **Automated tests** — at minimum, API-level tests for `/ask`, `/documents/*`, and auth flows; a regression test replaying `evaluation/dataset.json`'s expected-source assertions against the live retrieval endpoint.
12. **Wire up Celery for ingestion** so adding a chapter doesn't block on a synchronous CLI run — the infra is already provisioned in `docker-compose.yml`.
13. **CI** — run the test suite (once it exists) and the evaluation harness's `validate_dataset.py` check on every PR, so a schema change that silently breaks the eval dataset's assumptions gets caught immediately.
14. **Deployment** — containerize the FastAPI app and the built frontend, move secrets out of local `.env` files, move the source `.md`/processed markdown to S3 (already anticipated in `Document.file_path`'s docstring as "Phase 9").
15. **Remove the temporary debug exception handler** in `main.py` (added to diagnose a Google OAuth 500 — it currently returns raw exception details in API responses, which is fine for local dev and wrong for anything public).
