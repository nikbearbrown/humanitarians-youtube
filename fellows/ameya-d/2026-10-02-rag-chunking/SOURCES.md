# SOURCES - rag-chunking

Primary source: this project's own code and measurements in VIDEO_SCRIPT.md (all numbers real, from 600 docs to 1,500 chunks) plus chunking.py / token_demo.py / build_index.py. No invented figures. Educational use.

## Claims & provenance
- Step size = chunk_size minus overlap (VIDEO_SCRIPT.md SEGMENT 2, chunking.py).
- Same 400/50 settings: fixed splitter -> 8 chunks, recursive -> 10 (recursive stops at boundaries, won't pack to the limit).
- Real 1,500-chunk distribution is bimodal: min 67, max 388, mean 202, median 104 - chunk_size is a ceiling, not a target.
- Chunk by data type; the isolation test: if a chunk can't be understood alone, the chunking is wrong.
