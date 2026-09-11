# SOURCES - rag-tokenization

Primary source: this project's own code and measurements in VIDEO_SCRIPT.md (all numbers real, from 600 docs to 1,500 chunks) plus chunking.py / token_demo.py / build_index.py. No invented figures. Educational use.

## Claims & provenance
- 'the cat sat on a mat' = 6 tokens; '$4,829.17 EBITDA Q3x' = 13 tokens - same 20 chars (VIDEO_SCRIPT.md SEGMENT 3).
- '##' marks a continuation of the previous token; EBITDA fractures; $4,829.17 = 7 tokens for 9 chars.
- Chars/token: business prose ~8.00, English ~4.00, dense finance ~1.67 - financial text tokenizes 2-3x worse.
- all-mpnet-base-v2 silently discards past 384 tokens (no warning); measure and chunk by tokens, not characters.
