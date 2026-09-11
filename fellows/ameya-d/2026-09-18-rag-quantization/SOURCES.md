# SOURCES — rag-quantization

Primary source: this project's own code and measurements — `PRODUCTION_NOTES.md`, `VIDEO_SCRIPT.md`, `benchmark.py`, `compare_embeddings.py`, `retrieval.py`, `rerank.py` — plus field-standard practice for the general-knowledge beats (KV cache, speculative decoding, ANN index families). No invented figures; every on-screen number traces to the project or is a widely-published default. Educational use.

## Claims & provenance
- Storage = n_chunks × dims × 4B (float32); 1M × 768 ≈ 3 GB, 1M × 1536 ≈ 6 GB. (PRODUCTION_NOTES.md §1)
- Scalar quantization: int8 → 4× smaller, small recall loss. Binary: 1 bit/dim → 32× smaller, needs a rescoring pass. (§1)
- Rescore pattern: search compressed → shortlist → re-rank with full vectors (same idea as reranking).
- Project result: 384-dim model 88% vs 768-dim 76%, at half the storage and ~3× faster (compare_embeddings.py). Dimension is a cost decision, not only quality. (VIDEO_SCRIPT.md, §1)
