# FACTCHECK — rag-caching

Every on-screen figure verified against the project or a published default:

- Cache hit measured at ~0.002 ms vs a cold request ~1.3 s+ (benchmark.py; PRODUCTION_NOTES.md §3/§4).
- Layers: exact (question string → skips whole pipeline), semantic (embedding similarity → catches paraphrases), embedding (text hash), prompt/KV (stable prefix, ~90% cheaper reads). (§3)
- A too-loose semantic threshold serves the answer to a different question — needs eval rigor like retrieval. (§3)
- Invalidation is the hard part: TTL, or tag entries by source doc-id and purge on document update. Cost order: cache → route → trim → prompt-cache. (§3/§5)

Verdict: PASS — no unverifiable numbers on screen; general-knowledge beats are field-standard.
