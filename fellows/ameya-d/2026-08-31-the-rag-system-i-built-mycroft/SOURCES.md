# SOURCES — mycroft-rag-walkthrough

Weekly WORK video. Every number is machine-measured from this project
(`fin-disclosure-rag`). Educational use. Corpus is synthetic (no real disclosures).

| Claim in the reel | Source in this repo |
|---|---|
| 600 documents → 1,500 chunks → 25 exact-answer eval questions | `generate_corpus.py`, `chunking.py`, `eval_set.py`; `VIDEO_SCRIPT.md` header |
| Recursive chunking took retrieval MRR 0.833 → 1.000 | `run_eval.py`; `VIDEO_SCRIPT.md` results table |
| Chunk by data type (prose/tables/contracts) | `chunking.py`; `VIDEO_SCRIPT.md` Seg 2 |
| 384-dim model 88% hit vs 768-dim 76%; smaller wins on every axis | `compare_embeddings.py`; `VIDEO_SCRIPT.md` results table |
| Storage = n_chunks × dims × 4 bytes → halving dims halves storage | `PRODUCTION_NOTES.md` §1 |
| Hybrid (dense + BM25, RRF): MRR 0.655 → 0.810 (+24%), peak dense 0.2–0.3 | `weight_sweep.py`, `hybrid.py`; `VIDEO_SCRIPT.md` Seg 8 |
| Hit@5 ≈ 84% across the useful range while MRR climbs → ranking, not recall | `weight_sweep.py` sweep table; `VIDEO_SCRIPT.md` Seg 8 |
| RRF fuses by rank (1/(60+rank)), no score normalisation | `hybrid.py` `hybrid_search` (`rrf_k=60`) — shown verbatim in B07 |
| Per-stage latency: vector 4 ms · rerank 301 ms · generation 1288 ms | `benchmark.py`; `PRODUCTION_NOTES.md` §4; `VIDEO_SCRIPT.md` Seg 10 |
| Cache hit ≈ 0.002 ms | `benchmark.py`; `VIDEO_SCRIPT.md` results table |
| Vector search is ~0.2% of total latency | derived from the latency figures above |

No fabricated numbers. Figures shown on screen are the measured outputs of the
named scripts.
