# Agentic Routing and Answer-Quality Evaluation

`evaluation/RESULTS.md` answers "does retrieval find the right chunk?" This document answers two different questions that retrieval eval can't: *does the agent's routing decision (`classify_node`) actually route correctly*, and *is the final generated answer any good?* Both need a different methodology than retrieval eval — routing is a labeled classification problem, and answer quality has no single correct string to diff against, so it's scored by an LLM judge instead.

**Harness**: `evaluation/run_routing_eval.py` (routing only, calls `classify_route()` from `app/services/tutor_graph.py` directly — the exact function production uses, not a reimplementation) and `evaluation/run_agent_eval.py` (routing + answer quality together, invoking the real compiled graph via `build_tutor_graph(...).ainvoke(...)`, same code path as `/ask`).

## The first attempt was a degenerate eval, and that's worth explaining

The obvious first move was to label `dataset.json`'s existing 49 questions with their "correct route" and call it a routing eval. Doing this mechanically produces **46 "section" labels out of 49** — because that dataset was built for retrieval eval, where every question is paired with exactly the chunk that answers it. Assume the student is looking at that chunk (the only assumption the file supports) and of course the content on screen answers the question; there's no real judgment being tested. A router that *always* guessed `"section"` would score identically. **A routing decision isn't a property of the question alone — it's a property of (question, currently displayed content), and a dataset that never varies the second half of that pair can't test routing.**

These 46/3 labels are still recorded on `dataset.json` (`expected_route` field) and used in the combined eval below, but only as a floor-level sanity check, not as the real routing signal — see Finding 1.

## Finding 1 — A separate adversarial dataset was required, and it found a real bug

`evaluation/routing_cases.json` (12 cases) was built specifically to vary displayed content independently from the question, with each case targeting a named failure mode: obviously-local and obviously-mismatched sanity checks, a near-identical-looking wrong section, an explicit "explain this passage" exception path, a genuinely ambiguous case (excluded from scoring rather than forced to a label), and — the category that matters — content that *mentions* a question's topic without actually answering it.

**Result: 10/11 correct (90.9%)**, 1 case excluded as ambiguous.

| expected → predicted | count |
|---|---|
| section → section | 5 |
| corpus → corpus | 5 |
| corpus → section | 1 |

The one failure (`r05`) is exactly the case built to catch it: shown a theorem that uses the word "stable" repeatedly (proving `Ker v`/`Im v` are stable subspaces when `u`,`v` commute) but never actually defines what "stable" means in general, then asked for the general definition — the router said `"section"` when the real definition lives elsewhere. It was fooled by vocabulary overlap, not genuine comprehension. The same trap run in reverse (`r06` — shown the general definition, asked the specific commuting-endomorphisms question) passed, so the weakness is directional, not a blanket failure.

## Finding 2 — The same root cause showed up independently in a second, unrelated eval

The combined agent eval (below) re-used `dataset.json`'s 46/3 labels as a floor check and got **45/49 (91.8%) route accuracy** — higher than it might look, since this is the "easy" dataset. The four misses (`q19`, `q23`, `q29`, `q45`) all fail in the *same direction* (expected `"section"`, got `"corpus"`), and `q23` is `dataset.json`'s own `terminology_shift` case — built months earlier, for retrieval eval, specifically to ask about "hyperplans" when the source text says "sous-espaces vectoriels."

This is the mirror image of Finding 1's failure: there, shared vocabulary caused a false `"section"`; here, a vocabulary *mismatch* caused a false `"corpus"` even though the content genuinely answers the question. **Two independently-designed evals, built weeks apart for different purposes, converged on the same mechanism**: `classify_node`'s "does this text explicitly address the question" instruction leans on surface wording more than semantic comprehension, failing in both directions depending on which way the wording drifts.

**A validating side-effect, not a separate finding**: `q23`'s route was "wrong" by label, but its final answer still scored 5/5 faithfulness and 5/5 relevancy (see below) — the misroute sent it to corpus search instead of the local chunk, and corpus search, being real semantic search over the real document, found the right content anyway. A routing error here didn't propagate into an answer-quality error, because the fallback path is a real search, not a dead end.

## Finding 3 — A conversation-history-blind routing gap, discovered while building the harness, not predicted in advance

While building `routing_cases.json`'s `followup_needs_history` case, reading `classify_node`'s actual prompt (`app/services/tutor_graph.py`) showed it receives only `lesson_content` and the current `question` — **never conversation history**. A pronoun-dependent follow-up ("and if F isn't finite-dimensional, does that change anything?") is structurally unanswerable correctly by the router regardless of how good it is, since it's missing information it would need. This case (`r11`) is tracked separately in the results rather than scored as a normal pass/fail — whatever it outputs isn't a meaningful signal about routing quality, it's a signal about a missing input.

## Answer-quality evaluation (RAGAS-style LLM-as-judge)

**Methodology**: for each of `dataset.json`'s 49 questions, the real graph is invoked end-to-end (classify → retrieve → generate), then the final answer is scored by `gpt-4o` — deliberately a different, stronger model than the `gpt-4o-mini` that generates, to avoid the documented self-grading leniency bias of using a model to judge its own output. Two independent scores (1-5), never blended into one number, since they catch different failure modes:

- **Faithfulness** — is every claim in the answer actually supported by the retrieved context (catches hallucination)
- **Answer relevancy** — does the answer actually address the question asked (catches evasive/off-topic answers)

A third, deterministic check (not LLM-judged — a plain regex) verifies the system prompt's LaTeX rule: never `\( \)` or `\[ \]`, only `$...$`/`$$...$$`.

**Results, 49 questions:**

| Metric | Result |
|---|---|
| Route accuracy | 45/49 (91.8%) |
| Avg. faithfulness | 4.94 / 5 |
| Avg. answer relevancy | 4.92 / 5 |
| LaTeX-syntax violations | 1 / 49 |

**The scores aren't a rubber stamp** — worth stating explicitly, since a judge that always returns 5/5 would be worthless. The weakest case, `q21` (characteristic polynomial of a rank-1 endomorphism via its trace), scored faithfulness 4 / relevancy 3, with the judge's own stated reason: the answer added a specific matrix-representation detail not actually present in the retrieved context, and wasn't as tightly scoped to "via the trace" as the question asked. Specific, legible, differentiated feedback — not a generic low score.

**The one LaTeX violation** (`q24`): the model wrote `\( u_F(F) \)` instead of `$u_F(F)$` once across 49 real generations — confirms the system prompt's instruction isn't 100% self-enforcing even though it's followed almost every time, which is the reason this check exists as a separate mechanical pass rather than being folded into the LLM judge's job.

## What this changes about the production system

Nothing yet — these are measurements, not fixes. The concrete next step these findings point to: soften or extend `classify_node`'s prompt (e.g., a few-shot example of a paraphrased/terminology-shifted question that should still route `"section"`) to push it toward semantic matching rather than lexical matching, then re-run this exact harness to measure whether it actually helped — the same "fix it, then measure, don't assume" discipline `RESULTS.md`'s Finding 2 already established for retrieval.

## Reproducing these numbers

```
uv run python evaluation/run_routing_eval.py        # writes evaluation/results/routing_eval.json
uv run python evaluation/run_agent_eval.py           # writes evaluation/results/agent_eval.json (all 49 questions; --limit N for a subset)
```
