# SOURCES - rag-embeddings

Primary source: this project's own code and measurements in VIDEO_SCRIPT.md (all numbers real, from 600 docs to 1,500 chunks) plus chunking.py / token_demo.py / build_index.py. No invented figures. Educational use.

## Claims & provenance
- The model makes one vector per token: tokens (7,) -> (7, 384) -> mean pool -> chunk vector (384,) (VIDEO_SCRIPT.md SEGMENT 4).
- Batching: 64 separate matmuls 14.924 ms vs 1 batched matmul 1.181 ms = 12.6x speedup.
- Arithmetic is identical: 75,497,472 ops looped or batched - the bottleneck is memory bandwidth, not math.
- Batch is the biggest index-time win (batch_size 64-256, one argument); stream in shards; content-hash for incremental re-embed.
