# SOURCES — rag-caching

Primary source: this project's own code and measurements — `PRODUCTION_NOTES.md`, `VIDEO_SCRIPT.md`, `benchmark.py`, `compare_embeddings.py`, `retrieval.py`, `rerank.py` — plus field-standard practice for the general-knowledge beats (KV cache, speculative decoding, ANN index families). No invented figures; every on-screen number traces to the project or is a widely-published default. Educational use.

## Claims & provenance
- Cache hit measured at ~0.002 ms vs a cold request ~1.3 s+ (benchmark.py; PRODUCTION_NOTES.md §3/§4).
- Layers: exact (question string → skips whole pipeline), semantic (embedding similarity → catches paraphrases), embedding (text hash), prompt/KV (stable prefix, ~90% cheaper reads). (§3)
- A too-loose semantic threshold serves the answer to a different question — needs eval rigor like retrieval. (§3)
- Invalidation is the hard part: TTL, or tag entries by source doc-id and purge on document update. Cost order: cache → route → trim → prompt-cache. (§3/§5)
