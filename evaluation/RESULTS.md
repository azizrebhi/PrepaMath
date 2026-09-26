# Retrieval Benchmark Results

A from-scratch evaluation harness (`evaluation/`) built to answer a concrete question — *does each stage of this hybrid RAG pipeline (lexical → dense → RRF fusion → cross-encoder rerank) actually help?* — rather than assuming a textbook architecture is automatically the right one. It traces every candidate through every pipeline stage (`app/services/retrieval_pipeline.py`) so a failure can be attributed to a specific stage instead of treated as a black box.

**Corpus**: 2 chapters of a French "prépa" linear algebra / topology course ("Réduction des endomorphismes", "Espaces vectoriels normés"), ingested via `task.py` into Postgres/pgvector. **Dataset**: 48 hand-curated questions (`evaluation/dataset.json`) spanning definitions, theorems, proofs, exercises, terminology-shifted phrasing, multi-hop questions, and section-scoped questions — validated against the live DB so ground truth can't silently point at content that doesn't exist (`evaluation/validate_dataset.py`).

## Finding 1 — An ingestion bug was silently duplicating a third of the corpus

`task.py` keyed unnumbered structural units (bare `Exemples`/`Remarques` headings, no number) by `(chunk_type, None)`. Every new unnumbered block overwrote the previous one in-place, so only the *last* `Exemple` and the *last* `Remarque` in a chapter ever survived ingestion — duplicated across every position the overwritten ones used to occupy.

Measured directly against the corrupted DB before the fix: **74 of 234 rows (32%)** in the first chapter were exact duplicates of just two surviving blocks; dozens of distinct worked examples/remarks were completely unretrievable.

| | before fix | after fix |
|---|---|---|
| MRR | 0.573 | **0.658** |
| R@10 | 0.821 | **0.862** |
| Ingestion-gap probes (`q23`-`q25`) | all failed | **all found** |

Fixed by keying unnumbered units by position instead of type, plus three related bugs found the same way: a repeated running-header regex that missed 4 of 5 real formatting variants in the source, chapter-intro text silently dropped because chunking only started at the first recognized heading, and a truncation cap that undid a deliberate "keep multi-part exercises whole" exemption. See `evaluation/results/before_dense.json` / `before_hybrid.json` for the pre-fix baseline.

## Finding 2 — The lexical channel was dead weight; fixing it didn't help hybrid retrieval

`websearch_to_tsquery` ANDs every word in the input by default. Fed a full natural-language question (10+ words), it requires *all* of them to co-occur in one short chunk — which essentially never happens. Measured: **0 of 580 candidates**, across every query in an initial 29-question run, ever came from the lexical stage. Hybrid search was running as dense-only, silently, the whole time.

Fix: OR the query's own words together before calling `websearch_to_tsquery` (PostgreSQL's own French stopword handling still applies to each term), plus added the missing GIN index on `to_tsvector('french', content)` that made the channel worth calling at all. Lexical search is no longer dead — it independently resolves real matches (MRR 0.234, R@10 0.542 on its own) — but:

| config (48 questions, 2 chapters) | MRR | R@10 |
|---|---|---|
| **dense-only** | **0.667** | **0.896** |
| hybrid (RRF: lexical + dense) | 0.482 | 0.813 |
| reranked (hybrid + cross-encoder) | 0.531 | 0.813 |

RRF-fusing the now-functional-but-broader lexical signal into dense rankings measurably *hurts* — chunks that only match a couple of generic terms lexically get enough combined RRF score to outrank chunks dense search alone ranked highly. This isn't a case of "fix the bug, get the win": it's a case of "fix the bug, then measure whether the resulting design is actually better," and here it wasn't.

## Finding 3 — The cross-encoder reranker favors long passages over short precise definitions

Direct evidence, `q01` ("Comment définit-on un sous-espace vectoriel stable...?"): the exact textbook definition ranked #2 by dense search dropped to rank #12 after reranking — pushed below a much longer, keyword-dense example passage that happens to repeat "sous-espace", "stable", "endomorphisme" many times. Reproduced on 3+ queries; confirmed **not** a query/passage-pairing bug by re-testing with parent content instead of child content (`Définition 1` still ranked last of 9 candidates either way).

`cross-encoder/mmarco-mMiniLMv2-L12-H384-v1` (a small, MS-MARCO-tuned multilingual model) appears to have a genuine length/style bias against terse formal definitions in this domain. Reranking is disabled by default (`app/services/retrieval_pipeline.py`) pending a better-suited model; the code path is kept for that future A/B test via this same harness.

## Current production config

`app/routers/retrieval.py` uses **dense-only retrieval** (`use_lexical=False`, `use_rerank=False`), chosen because it's what the benchmark actually measured as best — not the default architectural assumption. All three configs remain available behind flags in `run_pipeline` for future experimentation, and this harness (`evaluation/run_retrieval_eval.py` + `metrics.py`) is what any future change should be validated against before being trusted.

## Reproducing these numbers

```
uv run python evaluation/validate_dataset.py        # confirm dataset matches current DB
uv run python evaluation/run_retrieval_eval.py       # writes evaluation/results/{dense,hybrid,reranked}.json
uv run python evaluation/metrics.py evaluation/results/dense.json evaluation/results/hybrid.json evaluation/results/reranked.json
```
