# SOURCES — KV Caching

Brief supplied by the requester (Likhith), 7 points; each checked against the sources below (retrieved 2026-09-28).

- Vaswani et al., "Attention Is All You Need", NeurIPS 2017 — https://arxiv.org/abs/1706.03762 (queries, keys, values; scaled dot-product attention; causal masking in the decoder).
- Pope et al., "Efficiently Scaling Transformer Inference", 2022 — https://arxiv.org/abs/2211.05102 (prefill vs. decode; the KV cache and its memory cost growing with context and batch).
- Touvron et al., "Llama 2: Open Foundation and Fine-Tuned Chat Models", 2023 — https://arxiv.org/abs/2307.09288 (7B: 32 layers, 32 heads, d_model 4096; GQA used only in the larger models).

## Evidence (executed, not typed)
- `evidence/kv_cache_toy.py` → `evidence/kv_cache_toy.out.txt` — numpy, seed 7, single-head causal attention, 12 tokens.
  Decodes the same sequence with and without a cache; outputs agree to 4.44e-16. Counts K/V projections (78 vs 12) and query-key scores (364 vs 78).
  B07's per-position counts and B08's bytes-per-token are that script's printed output. sha256 recorded at the end of the .out.txt.
- `evidence/math.json` — outlined SVG equation rows from `runtime/scripts/typeset_math.py` (matplotlib mathtext, STIX; matplotlib installed into the local .venv for this build).

## Corrections / de-sensationalising
- Brief point 7 "LLMs get faster per-token as a response goes on" → corrected: after the first token, each token is roughly steady-cost; the cache is why it's fast, not accelerating. See FACTCHECK #9.
- Brief point 1 "slow to start": the pause is attributed to prefill (reading the prompt and filling the cache) — the model-side cause; no latency numbers are shown.
- Brief point 5 "quadratic → closer to linear per new token": kept, with the exact counts shown and "roughly" in the narration.
- Brief point 6: memory figure uses one published model shape and is captioned; batch size and grouped-query attention change it (named in the Your Turn output lines).
- The running example ("The cat sat on the" → "mat"), the chat reply, attention weights and vector shades are illustrative and labelled.
