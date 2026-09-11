# FACTCHECK — rag-reranking

13 on-screen / narrated claims audited against the repo. No fabricated figures.

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | A bi-encoder encodes query and document separately, so document vectors precompute | ✅ | Standard; `hybrid.py` stores `embeddings` and compares at query time |
| 2 | A cross-encoder reads query + passage together and cannot be precomputed | ✅ | `rerank.py` docstring; `predict([(query, text), ...])` |
| 3 | Reranker = `cross-encoder/ms-marco-MiniLM-L-6-v2` | ✅ | `rerank.py` `CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")` |
| 4 | The reranker returns the top 3 | ✅ | `rerank.py` `rerank(query, candidates, top_n=3)` |
| 5 | Code shown in B05 is the real function | ✅ | Verbatim from `rerank.py` (comments added, logic identical) |
| 6 | First-stage retrieval ≈ 4 ms | ✅ | `benchmark.py`; `VIDEO_SCRIPT.md` Seg 10 (`retrieve 4.0 ms`) |
| 7 | Rerank pass ≈ 301 ms | ✅ | `benchmark.py`; `VIDEO_SCRIPT.md` (`rerank 301.5 ms`) |
| 8 | Generation ≈ 1288 ms (over a thousand) | ✅ | `benchmark.py`; `VIDEO_SCRIPT.md` Seg 10 |
| 9 | Reranking is bounded — a shortlist, never the corpus | ✅ | `rerank.py` operates on the retrieved `candidates`, not all chunks |
| 10 | "retrieve 20, rerank to 3" two-stage shape | ✅ | `hybrid_search(..., k=20)` → `rerank(..., top_n=3)` |
| 11 | Rerank lets you send fewer, better chunks (context trim) | ✅ | `PRODUCTION_NOTES.md` §5.3 |
| 12 | Worth it when correctness matters; skippable for low-stakes chat | ✅ | `VIDEO_SCRIPT.md` Seg 10 |
| 13 | "the retriever finds; the reranker decides" (framing, not a metric) | ✅ | Editorial summary of #1–#4; no numeric claim |

**Corrections log:** none required. Narration avoids any model-version or dated
count that would age the video.
