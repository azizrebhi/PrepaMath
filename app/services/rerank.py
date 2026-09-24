from sentence_transformers import CrossEncoder

RERANK_MODEL_NAME = "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1"
reranker = CrossEncoder(RERANK_MODEL_NAME)

def rerank_chunks(
    query: str,
    chunks: list[dict],
    top_n: int = 5,) -> list[dict]:

    if not chunks:
        return []

    pairs = [(query, chunk["content"])for chunk in chunks]

    scores = reranker.predict(pairs)

    scored = list(zip(chunks, scores))

    scored.sort(
        key=lambda x: float(x[1]),
        reverse=True,
    )

    return [
        chunk
        for chunk, _ in scored[:top_n]
    ]