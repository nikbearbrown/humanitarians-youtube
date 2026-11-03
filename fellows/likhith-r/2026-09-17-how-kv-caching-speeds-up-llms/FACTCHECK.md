# FACTCHECK — KV Caching

Status: claims checked by Claude Code against the primary sources in SOURCES.md and local executable evidence. Signed off by Likhith: I watched both the 16:9 and 9:16 cuts, went through each claim below against the linked sources, and I'm satisfied the video is accurate and looks good.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B02/B05 | A chatbot pauses before its first word; reading the prompt (filling the cache) is that pause | PASS (softened) | The prefill pass processes every prompt token and writes their K/V before the first output token (Pope et al. 2022 §2) | Queueing/network also add latency; the reel names prefill as *the* model-side pause, no timings shown |
| 2 | B03 | Without a cache, each new token recomputes attention over every earlier token | PASS | Autoregressive decoding re-runs the full causal pass over the prefix if nothing is saved | Counter 1,3,6…21 = Σ t for 6 tokens (exact) |
| 3 | B04 | Each token makes a query, key and value; past keys and values never change | PASS | Vaswani et al. 2017 §3.2; with a causal mask a token's K/V depend only on itself and earlier tokens, so appending tokens never changes them | "earlier tokens never look at later ones" on screen |
| 4 | B06 | Each new token computes only its own q, k, v; K and V for the rest come from the cache | PASS | Standard incremental decoding; verified numerically (row 7) | Weights labelled illustrative |
| 5 | B06 | o_t = softmax(q_t Kᵀ / √d) V, with K and V read from the cache (rows 1…t, including the new k_t, v_t) | PASS | Scaled dot-product attention (Vaswani §3.2.1) restricted to the new query row; d = key width; K includes the new k_t | Typeset via typeset_math.py (outlined SVG) |
| 6 | B07 | Per new token, work drops from quadratic to roughly linear in length | PASS | Query-key scores at position t: t(t+1)/2 recomputing causal attention vs t with the cache; K/V projections t vs 1 | "roughly" kept: the cached step still reads t cached vectors |
| 7 | B07 | 55 vs 10, 5,050 vs 100, 500,500 vs 1,000; "500× less" | PASS | evidence/kv_cache_toy.py; ratio (t+1)/2 = 500.5 at t=1000 shown exactly as "500.5×" | Also: cached vs uncached outputs agree to 4.44e-16 (same answer, less work) |
| 8 | B08 | Cache memory grows with every token; Llama 2 7B shape: 0.5 MiB/token, 2 GiB at 4,096 tokens | PASS | 2 × 32 layers × 32 heads × 128 × 2 B = 524,288 B/token (Touvron et al. 2023: 7B has 32 layers, d_model 4096, 32 heads, no GQA); ×4096 = 2 GiB | "one conversation, 16-bit" on screen; per-sequence, batch multiplies it |
| 9 | B09 | Why text streams fast after the first word, and why long contexts eat memory | CORRECTED | Brief point 7 said LLMs "get faster per-token as a response goes on". With a cache, per-token time is roughly steady after the first token (it even creeps up slightly as the cache grows); what grows is the saving vs. no cache | Narration/verdict say "streams fast after the first word" instead |

## Algebra checks
- Σ_{t=1}^{12} t(t+1)/2 = C(14,3) = 364 ✓ (script: 364); Σ_{t=1}^{12} t = 78 ✓ (script: 78).
- Per-step ratio t(t+1)/2 ÷ t = (t+1)/2 → 5.5, 50.5, 500.5 ✓ (shown "5.5× / 50.5× / 500.5× less").
- Memory formula 2·L·H·d_head·b·n: factor 2 = K and V; n = tokens; b = bytes per value (2 for fp16).
