"""brute_force_search.py — exact nearest-neighbour search, timed as the
collection grows.

Cycle 1 of the CLI reel. The absolute milliseconds are machine-specific; the
SHAPE is the point. Every comparison still has to happen, so once the
collection is large enough that fixed overhead stops dominating, cost tracks
collection size roughly linearly.
"""
import time

import numpy as np

from corpus import DIM, make_corpus, new_run

K = 10
N_QUERIES = 20
SIZES = (1_000, 10_000, 100_000)


def brute_force(db: np.ndarray, q: np.ndarray, k: int = K) -> np.ndarray:
    """Compare the query against EVERY stored vector. Exact — never misses."""
    sims = db @ q                          # one dot product per stored vector
    top = np.argpartition(-sims, k)[:k]
    return top[np.argsort(-sims[top])]


if __name__ == "__main__":
    rng, projection = new_run()
    queries = make_corpus(N_QUERIES, rng, projection)

    print(f"exact (brute-force) search · dim={DIM} · top-{K}")
    print(f"{'vectors':>9}  {'ms/query':>9}  {'compared/query':>15}")

    for n in SIZES:
        db = make_corpus(n, rng, projection)

        for q in queries[:3]:              # warm up
            brute_force(db, q)

        t0 = time.perf_counter()
        for q in queries:
            brute_force(db, q)
        ms = (time.perf_counter() - t0) / N_QUERIES * 1000

        print(f"{n:>9,}  {ms:>9.2f}  {n:>15,}")
