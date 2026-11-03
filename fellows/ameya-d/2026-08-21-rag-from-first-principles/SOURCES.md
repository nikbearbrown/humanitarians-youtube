# SOURCES — rag-from-first-principles

Primary source: `VIDEO_SCRIPT.md` (this repo) — "RAG From First Principles," a
measured build over 600 synthetic financial-disclosure documents. Every figure is
tied to a generating script in this repo (see the script's Appendix B and
[FACTCHECK.md](FACTCHECK.md)).

Generating scripts referenced on screen or in narration:
- chunking.py — chunk_text (B03/B04)
- build_index.py / build_index_v2.py / build_index_big.py — chunking + embedding (B05/B09/B10)
- token_demo.py — tokenization ratios (B06)
- pad_demo.py — attention-mask pooling delta (B09)
- retrieval.py — cosine + top-k (B11/B12)
- dilution_demo.py — pooling dilution (B13)
- run_eval.py — hit rate / MRR (B15)
- compare_embeddings.py — model comparison (B16)
- weight_sweep.py — hybrid weight sweep (B17/B18)
- benchmark.py — per-stage latency + cache (B19/B20)

Code shown (B03/B11/B12) is real, trimmed to the teaching lines.

*Educational — a measurement walkthrough, not production code.*
