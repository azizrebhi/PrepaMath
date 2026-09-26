RERANK_MODEL_NAME = "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"

_reranker = None


def _get_reranker():
    # Deferred: sentence_transformers pulls in transformers/torch, which is
    # heavy to import — callers that never rerank (e.g. a dense-only eval
    # config) shouldn't pay for it.
    global _reranker
    if _reranker is None:
        from sentence_transformers import CrossEncoder
        _reranker = CrossEncoder(RERANK_MODEL_NAME)
    return _reranker


def rerank_chunks_scored(
    query: str,
    chunks: list[dict],
) -> list[tuple[dict, float]]:
    """Scores and ranks every candidate, without truncating to top_n — needed
    so callers (e.g. the eval harness) can see where a chunk landed even
    when it falls outside the eventual top-n."""

    if not chunks:
        return []

    pairs = [(query, chunk["content"]) for chunk in chunks]

    scores = _get_reranker().predict(pairs)

    scored = list(zip(chunks, scores))

    scored.sort(
        key=lambda x: float(x[1]),
        reverse=True,
    )

    return [(chunk, float(score)) for chunk, score in scored]


def rerank_chunks(
    query: str,
    chunks: list[dict],
    top_n: int = 5,
) -> list[dict]:
    scored = rerank_chunks_scored(query, chunks)
    return [chunk for chunk, _ in scored[:top_n]]