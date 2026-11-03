# FACTCHECK — mycroft-rag-walkthrough

14 on-screen / narrated claims audited against the repo. No fabricated figures.

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | 600 documents | ✅ | `generate_corpus.py`; `VIDEO_SCRIPT.md` header |
| 2 | 1,500 chunks | ✅ | `chunking.py` output; `VIDEO_SCRIPT.md` header |
| 3 | 25 exact-answer eval questions (golden set) | ✅ | `eval_set.py`; `VIDEO_SCRIPT.md` header |
| 4 | Recursive chunking: MRR 0.833 → 1.000 | ✅ | `run_eval.py`; results table |
| 5 | 384-dim model → 88% hit rate | ✅ | `compare_embeddings.py`; results table |
| 6 | 768-dim model → 76% hit rate | ✅ | `compare_embeddings.py`; results table |
| 7 | Smaller model: half the storage, ~3x faster, better retrieval | ✅ | `compare_embeddings.py`; `PRODUCTION_NOTES.md` §1 storage math |
| 8 | Hybrid MRR 0.655 (dense alone) → 0.810 (best mix), +24% | ✅ | `weight_sweep.py`; `VIDEO_SCRIPT.md` Seg 8 |
| 9 | Peak around dense weight 0.2–0.3 | ✅ | `weight_sweep.py` sweep table (0.2 & 0.3 → 0.810) |
| 10 | Hit@5 ≈ 84% across that range while MRR climbs | ✅ | `weight_sweep.py` (0.0–0.3 → 84% hit; MRR 0.75→0.81) |
| 11 | RRF code shown is the real `hybrid.py` | ✅ | Verbatim `hybrid_search` (comments added; logic identical) |
| 12 | Latency: vector 4 ms / rerank 301 ms / generation 1288 ms | ✅ | `benchmark.py`; `PRODUCTION_NOTES.md` §4 |
| 13 | Cache hit ≈ 0.002 ms | ✅ | `benchmark.py`; results table |
| 14 | Vector search ≈ 0.2% of total latency | ✅ | 4 / (4+301+1288) ≈ 0.25% → stated as ~0.2% |

**Nuance logged (B05):** the +24% headline is dense-only → best hybrid mix; the
"hit rate barely moves" point is scoped to the 0.0–0.3 dense-weight range (where
hit@5 ≈ 84%), not the entire sweep — narration says "across that range," matching
the data. **Disclosure:** corpus is synthetic; no real company disclosures used.
