# FACTCHECK - rag-chunking

Every on-screen figure verified against VIDEO_SCRIPT.md / the project:

- Step size = chunk_size minus overlap (VIDEO_SCRIPT.md SEGMENT 2, chunking.py).
- Same 400/50 settings: fixed splitter -> 8 chunks, recursive -> 10 (recursive stops at boundaries, won't pack to the limit).
- Real 1,500-chunk distribution is bimodal: min 67, max 388, mean 202, median 104 - chunk_size is a ceiling, not a target.
- Chunk by data type; the isolation test: if a chunk can't be understood alone, the chunking is wrong.

Verdict: PASS - all numbers trace to the project.
