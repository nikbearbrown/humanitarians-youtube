# FACTCHECK - rag-tokenization

Every on-screen figure verified against VIDEO_SCRIPT.md / the project:

- 'the cat sat on a mat' = 6 tokens; '$4,829.17 EBITDA Q3x' = 13 tokens - same 20 chars (VIDEO_SCRIPT.md SEGMENT 3).
- '##' marks a continuation of the previous token; EBITDA fractures; $4,829.17 = 7 tokens for 9 chars.
- Chars/token: business prose ~8.00, English ~4.00, dense finance ~1.67 - financial text tokenizes 2-3x worse.
- all-mpnet-base-v2 silently discards past 384 tokens (no warning); measure and chunk by tokens, not characters.

Verdict: PASS - all numbers trace to the project.
