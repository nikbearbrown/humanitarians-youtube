# FACTCHECK — rag-vector-search

Every on-screen figure verified against the project or a published default:

- Brute force in the project: ~4 ms over 1,500 vectors; O(n·d) — dies at ~10M. (PRODUCTION_NOTES.md §2)
- Flat: exact, good < ~100k vectors. HNSW: multi-layer proximity graph, ~O(log n), high recall, high RAM (Chroma/Qdrant/Weaviate default). IVF: k-means clusters, nprobe tunes recall/speed. IVF-PQ: + product quantization for huge corpora. (§2)
- Storage: n × dims × 4B; 1M × 768 × 4B ≈ 3 GB. (§1)
- k-means centroid routing on the Boehringer system ≈ hand-rolled IVF. (§2)

Verdict: PASS — no unverifiable numbers on screen; general-knowledge beats are field-standard.
