"""Week 8 evidence run for 'Where the Error Lives'.

Reproduces the IVF-PQ half of benchmarks/anncomp.py with the same settings
(N=100,000 SIFT, 1,000 queries, k=10, nlist=256, m=8, seed=0), and adds the
measurement the video's claim rests on: for each nprobe, how many of the true
neighbours are inside the scanned cells (coverage, the ceiling for ANY search
over those cells) versus how many the 8-byte codes return (recall).
"""
import json, os, sys, time
from pathlib import Path
import numpy as np

# Point HIVE_INDEX at a clone of github.com/Kenny0bi/hive-index with
# data/sift_base.fvecs (first 100,000 rows suffice) and data/sift_query.fvecs.
REPO = Path(os.environ.get("HIVE_INDEX", "hive-index")).expanduser()
sys.path.insert(0, str(REPO))
from hive.ivfpq import IVFPQ
from tests.test_hnsw import read_fvecs

N, NQ, K = 100_000, 1000, 10
OUT = Path(__file__).with_name("evidence.json")

base = read_fvecs(REPO / "data/sift_base.fvecs")[:N].copy()
queries = read_fvecs(REPO / "data/sift_query.fvecs")[:NQ].copy()
print(f"base {base.shape} {base.dtype}, queries {queries.shape}", flush=True)

# exact ground truth by brute force (|a|^2 - 2ab + |b|^2 in float64; same
# answer as the repo's direct difference, without a 2.5 GB intermediate)
t0 = time.perf_counter()
b64 = base.astype(np.float64); bn = (b64 ** 2).sum(1)
gt = np.empty((NQ, K), dtype=np.int64)
for s in range(0, NQ, 100):
    q = queries[s:s+100].astype(np.float64)
    d = bn[None, :] - 2 * q @ b64.T + (q ** 2).sum(1)[:, None]
    gt[s:s+100] = np.argsort(d, axis=1)[:, :K]
print(f"ground truth in {time.perf_counter()-t0:.1f}s", flush=True)

t0 = time.perf_counter()
ix = IVFPQ(dim=128, nlist=256, m=8, seed=0)
ix.train(base); ix.add(base)
build_s = time.perf_counter() - t0
print(f"IVF-PQ trained+added in {build_s:,.0f}s", flush=True)

# which cell each base vector lives in
cell_of = np.empty(N, dtype=np.int64)
for c, (ids, _) in enumerate(ix.lists):
    cell_of[ids] = c

def run(nprobe, rerank):
    hits = cover = 0
    t0 = time.perf_counter()
    for qi, q in enumerate(queries):
        got = [p for p, _ in ix.search(q, k=K, nprobe=nprobe, rerank=rerank)]
        hits += len(set(got) & set(gt[qi]))
        cd = ((ix.coarse - q) ** 2).sum(-1)
        cells = set(np.argsort(cd)[:nprobe].tolist())
        cover += sum(1 for t in gt[qi] if cell_of[t] in cells)
    dt = time.perf_counter() - t0
    return hits / (NQ * K), cover / (NQ * K), NQ / dt

rows = []
for nprobe in [1, 2, 4, 8, 16, 32, 64, 128]:
    r, cov, qps = run(nprobe, 0)
    rows.append({"nprobe": nprobe, "rerank": 0, "recall": round(r, 4),
                 "coverage": round(cov, 4), "qps": round(qps, 1)})
    print(rows[-1], flush=True)
for rr in [10, 25, 50, 100, 200]:
    r, cov, qps = run(64, rr)
    rows.append({"nprobe": 64, "rerank": rr, "recall": round(r, 4),
                 "coverage": round(cov, 4), "qps": round(qps, 1)})
    print(rows[-1], flush=True)

result = {
    "settings": {"N": N, "NQ": NQ, "K": K, "nlist": 256, "m": 8, "seed": 0},
    "bytes_per_vector_raw": 128 * 4,
    "bytes_per_vector_code": int(ix.m),
    "compression": (128 * 4) // ix.m,
    "build_s": round(build_s, 1),
    "rows": rows,
}
OUT.write_text(json.dumps(result, indent=1))
print("done ->", OUT, flush=True)
