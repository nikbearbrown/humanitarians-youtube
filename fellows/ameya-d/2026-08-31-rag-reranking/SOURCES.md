# SOURCES — rag-reranking

Every figure and claim traces to this project (`fin-disclosure-rag`), not to
outside marketing copy. Educational use.

| Claim in the reel | Source in this repo |
|---|---|
| Cross-encoder reads (query, passage) together; cannot be precomputed | `rerank.py` docstring + `CrossEncoder.predict(pairs)` |
| Reranker model = `cross-encoder/ms-marco-MiniLM-L-6-v2`, returns top-3 | `rerank.py` (`get_reranker`, `rerank(..., top_n=3)`) |
| First-stage retrieval is fast because vectors are precomputed | `retrieval.py`, `hybrid.py` (`dense_search` over stored embeddings) |
| Per-stage latency: vector search ~4 ms · rerank ~301 ms · generation ~1288 ms | `benchmark.py`; `PRODUCTION_NOTES.md` §4; `VIDEO_SCRIPT.md` Seg 10 |
| Rerank is bounded — you score a shortlist (~20), never the corpus | `rerank.py` (candidates list); `PRODUCTION_NOTES.md` §4 |
| Reranking is justified when correctness matters, questionable for low-stakes chat | `VIDEO_SCRIPT.md` Seg 10 |
| Rerank lets you send 3 strong chunks instead of 10 mediocre ones (context trim) | `PRODUCTION_NOTES.md` §5 item 3 |

No invented numbers. Where a figure is machine-measured it is labelled as such;
where it is standard practice (bi- vs cross-encoder roles) it is presented as
common knowledge, phrased in the project's own terms.
