# SOURCES — rag-vector-search

Primary source: this project's own code and measurements — `PRODUCTION_NOTES.md`, `VIDEO_SCRIPT.md`, `benchmark.py`, `compare_embeddings.py`, `retrieval.py`, `rerank.py` — plus field-standard practice for the general-knowledge beats (KV cache, speculative decoding, ANN index families). No invented figures; every on-screen number traces to the project or is a widely-published default. Educational use.

## Claims & provenance
- Brute force in the project: ~4 ms over 1,500 vectors; O(n·d) — dies at ~10M. (PRODUCTION_NOTES.md §2)
- Flat: exact, good < ~100k vectors. HNSW: multi-layer proximity graph, ~O(log n), high recall, high RAM (Chroma/Qdrant/Weaviate default). IVF: k-means clusters, nprobe tunes recall/speed. IVF-PQ: + product quantization for huge corpora. (§2)
- Storage: n × dims × 4B; 1M × 768 × 4B ≈ 3 GB. (§1)
- k-means centroid routing on the Boehringer system ≈ hand-rolled IVF. (§2)
