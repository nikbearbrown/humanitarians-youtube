"""ann_search.py — an approximate index over the same 100,000 vectors.

Cycle 2 of the CLI reel: the revision. Same collection, same queries, same
top-10 — but a query no longer touches every stored vector.

This builds an INVERTED-FILE (IVF) index, one of the ANN index families
Chapter 5 names. Vectors are grouped into cells by k-means; a query is compared
against the 256 cell centroids first, then only against the vectors inside the
nearest `nprobe` cells. Everything else is skipped, unexamined.

The chapter walks through HNSW, a GRAPH-based index, instead. The mechanism
differs — hopping down a hierarchy of graphs vs. probing a few cells — but the
idea under test is the one the chapter is making: narrow the search space
rather than scan it, and pay for the speed in recall.

Recall@10 is measured against the brute-force answer, so the cost of
approximating is reported rather than assumed, and `nprobe` is swept because
the chapter's real claim is that this tradeoff is a DIAL, not a fixed penalty.
"""
import time

import numpy as np

from corpus import make_corpus, new_run, unit

K = 10
N = 100_000
N_QUERIES = 20
SIZES = (1_000, 10_000, 100_000)
KMEANS_ITERS = 12
NPROBE = 4                      # cells probed per query, held fixed across sizes
NPROBE_SWEEP = (1, 4, 16, 32)


def n_cells(n: int) -> int:
    """Standard IVF sizing: about sqrt(n) cells, so each holds about sqrt(n)
    vectors. With nprobe fixed, comparisons per query then grow like sqrt(n)
    rather than n — which is the whole claim under test."""
    return max(4, int(round(n ** 0.5)))


def brute_force(db, q, k=K):
    sims = db @ q
    top = np.argpartition(-sims, k)[:k]
    return top[np.argsort(-sims[top])]


def fit_cells(db, rng, cells):
    """Lloyd's algorithm on a subsample — the index BUILD, paid once."""
    sample_n = min(len(db), max(cells * 40, 2_000))
    sample = db[rng.choice(len(db), sample_n, replace=False)]
    centroids = sample[rng.choice(sample_n, cells, replace=False)].copy()
    for _ in range(KMEANS_ITERS):
        assign = np.argmax(sample @ centroids.T, axis=1)
        for c in range(cells):
            members = sample[assign == c]
            if len(members):
                centroids[c] = members.mean(axis=0)
        centroids = unit(centroids)
    return centroids


def build_lists(db, centroids):
    """The inverted file: cell id -> the row ids that live in it."""
    assign = np.argmax(db @ centroids.T, axis=1)
    return [np.flatnonzero(assign == c) for c in range(len(centroids))]


def ivf_search(db, centroids, lists, q, nprobe, k=K):
    """Rank the cells, then scan ONLY the nearest nprobe of them."""
    near = np.argpartition(-(centroids @ q), nprobe)[:nprobe]
    cand = np.concatenate([lists[c] for c in near])
    sims = db[cand] @ q
    top = np.argpartition(-sims, k)[:k]
    return cand[top[np.argsort(-sims[top])]]


def scanned_per_query(centroids, lists, queries, nprobe):
    return int(np.mean([
        sum(len(lists[c]) for c in
            np.argpartition(-(centroids @ q), nprobe)[:nprobe])
        for q in queries]))


def recall_at_k(hits, truth):
    return float(np.mean([len(set(h.tolist()) & set(t.tolist())) / K
                          for h, t in zip(hits, truth)]))


if __name__ == "__main__":
    rng, projection = new_run()
    queries = make_corpus(N_QUERIES, rng, projection)

    # ── TABLE 1 · how cost grows with the collection ────────────────────────
    # Brute force compares against everything: n per query.
    # IVF sizes its cells as sqrt(n) and probes a fixed few, so it compares
    # against roughly sqrt(n) — the growth rate is the claim, not the ms.
    print("how cost grows · exact vs approximate · top-10\n")
    print(f"{'vectors':>9}  {'exact cmp':>10}  {'IVF cmp':>8}  "
          f"{'exact ms':>9}  {'IVF ms':>7}  {'recall':>7}")

    for n in SIZES:
        db = make_corpus(n, rng, projection)
        cells = n_cells(n)
        centroids = fit_cells(db, rng, cells)
        lists = build_lists(db, centroids)

        truth = [brute_force(db, q) for q in queries]
        hits = [ivf_search(db, centroids, lists, q, NPROBE) for q in queries]

        t0 = time.perf_counter()
        for q in queries:
            brute_force(db, q)
        exact_ms = (time.perf_counter() - t0) / N_QUERIES * 1000

        t0 = time.perf_counter()
        for q in queries:
            ivf_search(db, centroids, lists, q, NPROBE)
        ivf_ms = (time.perf_counter() - t0) / N_QUERIES * 1000

        print(f"{n:>9,}  {n:>10,}  "
              f"{scanned_per_query(centroids, lists, queries, NPROBE):>8,}  "
              f"{exact_ms:>9.2f}  {ivf_ms:>7.2f}  "
              f"{recall_at_k(hits, truth):>7.3f}")

    # ── TABLE 2 · the dial, at full scale ───────────────────────────────────
    # Same index, same 100,000 vectors. Only nprobe changes. This is the
    # chapter's real claim: the accuracy you give up is a setting, not a
    # surprise.
    db = make_corpus(N, rng, projection)
    cells = n_cells(N)
    centroids = fit_cells(db, rng, cells)
    lists = build_lists(db, centroids)
    truth = [brute_force(db, q) for q in queries]

    print(f"\nthe dial · {N:,} vectors · {cells} cells · top-10\n")
    print(f"{'nprobe':>6}  {'compared':>9}  {'of total':>9}  {'recall@10':>10}")
    for nprobe in NPROBE_SWEEP:
        hits = [ivf_search(db, centroids, lists, q, nprobe) for q in queries]
        scanned = scanned_per_query(centroids, lists, queries, nprobe)
        print(f"{nprobe:>6}  {scanned:>9,}  {scanned / N:>8.1%}  "
              f"{recall_at_k(hits, truth):>10.3f}")
