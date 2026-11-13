"""hybrid_search.py — dense retrieval, and Reciprocal Rank Fusion over both.

Cycle 2 of the CLI reel: the revision. Same 12 passages, same two queries.

Dense retrieval uses REAL all-MiniLM-L6-v2 embeddings (see encoder.py — the
weights come from the local HuggingFace cache and the forward pass is run in
numpy, because sentence-transformers is not installed here). Nothing about the
similarity scores is hand-tuned.

Fusion is Reciprocal Rank Fusion exactly as Cormack, Clarke & Buettcher (2009)
define it: each candidate scores the sum of 1/(k + rank) over the ranked lists
it appears in, with k = 60. RRF deliberately uses RANKS, not scores — BM25
scores and cosine similarities are not on a comparable scale, and ranks sidestep
that without any per-system weight tuning.
"""
from bm25_search import BM25
from corpus import GOLD, PASSAGES, QUERIES
from encoder import MiniLM

RRF_K = 60


def rrf(rankings, k: int = RRF_K):
    """rankings: list of ranked id lists (best first) -> fused {id: score}."""
    fused = {}
    for ranked in rankings:
        for rank, pid in enumerate(ranked, 1):
            fused[pid] = fused.get(pid, 0.0) + 1.0 / (k + rank)
    return fused


def top(d, n=3):
    return sorted(d.items(), key=lambda r: -r[1])[:n]


if __name__ == "__main__":
    ids = list(PASSAGES)
    bm25 = BM25(PASSAGES)
    model = MiniLM()

    doc_vecs = model.encode([PASSAGES[i] for i in ids])

    print(f"sparse (BM25) vs dense (all-MiniLM-L6-v2) vs hybrid (RRF k={RRF_K})")
    print(f"{len(PASSAGES)} passages · gold for both queries: {GOLD}\n")

    verdicts = {}
    for kind, q in QUERIES:
        qv = model.encode([q])[0]

        sparse_ranked = [pid for pid, _ in
                         sorted(((ids[i], bm25.score(q, i)) for i in range(len(ids))),
                                key=lambda r: -r[1])]
        dense_scores = {ids[i]: float(doc_vecs[i] @ qv) for i in range(len(ids))}
        dense_ranked = [pid for pid, _ in sorted(dense_scores.items(), key=lambda r: -r[1])]

        fused = rrf([sparse_ranked, dense_ranked])

        print(f"[{kind}] {q}")
        print(f"   sparse top-3   {', '.join(sparse_ranked[:3])}")
        print("   dense  top-3   " + ", ".join(
            f"{pid} {dense_scores[pid]:.3f}" for pid in dense_ranked[:3]))
        print("   hybrid top-3   " + ", ".join(
            f"{pid} {sc:.5f}" for pid, sc in top(fused)))
        # show the fusion arithmetic for the gold passage and whatever beat it,
        # because when RRF loses, the margin is the whole story
        winner = top(fused)[0][0]
        if winner != GOLD:
            for pid in (winner, GOLD):
                sr = sparse_ranked.index(pid) + 1
                dr = dense_ranked.index(pid) + 1
                print(f"     {pid}: sparse #{sr} + dense #{dr} -> "
                      f"1/{RRF_K + sr} + 1/{RRF_K + dr} = {fused[pid]:.5f}")

        v = {
            "sparse": sparse_ranked[0] == GOLD,
            "dense": dense_ranked[0] == GOLD,
            "hybrid": top(fused)[0][0] == GOLD,
        }
        verdicts[kind] = v
        print("   => " + "  ".join(
            f"{name}: {'HIT ' if ok else 'MISS'}" for name, ok in v.items()) + "\n")

    print("top-1 hit on the gold passage:")
    print(f"{'method':<8} {'exact code':>12} {'paraphrase':>12} {'both':>6}")
    for name in ("sparse", "dense", "hybrid"):
        a = verdicts["exact code"][name]
        b = verdicts["paraphrase"][name]
        tick = lambda x: "HIT" if x else "MISS"
        print(f"{name:<8} {tick(a):>12} {tick(b):>12} {('YES' if a and b else 'no'):>6}")
