# FACTCHECK — rag-quantization

Every on-screen figure verified against the project or a published default:

- Storage = n_chunks × dims × 4B (float32); 1M × 768 ≈ 3 GB, 1M × 1536 ≈ 6 GB. (PRODUCTION_NOTES.md §1)
- Scalar quantization: int8 → 4× smaller, small recall loss. Binary: 1 bit/dim → 32× smaller, needs a rescoring pass. (§1)
- Rescore pattern: search compressed → shortlist → re-rank with full vectors (same idea as reranking).
- Project result: 384-dim model 88% vs 768-dim 76%, at half the storage and ~3× faster (compare_embeddings.py). Dimension is a cost decision, not only quality. (VIDEO_SCRIPT.md, §1)

Verdict: PASS — no unverifiable numbers on screen; general-knowledge beats are field-standard.
