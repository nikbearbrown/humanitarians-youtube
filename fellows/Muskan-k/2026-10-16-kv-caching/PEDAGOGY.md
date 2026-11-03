# PEDAGOGY — KV Caching. (claude-hai · teaching explainer, ~2.5min)

**The ONE insight:** generation is token-by-token, and each token attends to every
previous token's **Key** and **Value** — so cache them once and **reuse** instead of
recomputing the whole history every step. The trade: **memory for speed.**

**Audience (HAI):** learners who use AI daily and want to understand why the first
token is slow, the rest stream, and long context gets expensive.

## Act structure (framework-first — built to pass PROOF)
- B00 hook (composer) — first word slow, rest fast; long chat pricier — one idea ✓
- **B01 SETUP** — token-by-token; each token attends to all prior ones, stored as K + V ✓
- **B02 CORE (the lesson)** — without a cache you recompute all past K/V every step;
  the KV cache stores once and reuses ✓
- **B03 worked example** — prefill vs decode: the pause is building the cache, the fast
  stream is reusing it ✓
- **B04 falsifiability / edge (the trade)** — the cache isn't free: it grows with
  length × layers, so memory is the bottleneck for long context / many users ✓
- B05 verdict · B06 handoff (watch the timing; reason about length→cost) · B07 outro ✓
- Body B01–B04 = 4K PIL cards; Claude UI only at B00/B05/B06/B07 (ILLUSTRATE LAW).

## PROOF rubric self-check
- Explicit framework before examples — B01 (setup) + B02 (recompute→reuse) ✓
- Reusable rubric — "cache trades compute for memory; length drives the cache" lets a
  viewer reason about cost/speed of any long-context use ✓
- Worked example — B03 (prefill/decode, the reasoning behind the timing) ✓
- Falsifiability / edge — B04 (the cache isn't free; memory is the real limit) ✓
- Active task — B06 (watch prefill→decode; reason length→cost) ✓
- Friction — B02 (the recompute waste) + B04 (the cost) ✓
- Production gate: qualitative mechanism only (no param counts, benchmarks, model
  names); the K/V, recompute→reuse, and the memory trade are the on-screen evidence.

## Correctness (DOUBLE-CHECK LAW — accurate, non-dating)
- Autoregressive, token-by-token generation; attention uses Query over Keys & Values.
- Without caching, K/V for the whole prefix are recomputed each step (redundant);
  KV cache stores per-token K/V and reuses them — only the new token's K/V is computed.
- Prefill (process the prompt, populate the cache) vs decode (generate reusing it) is
  the standard framing; "first token slow, then fast stream" follows from it.
- Cache memory grows with sequence length × layers (× heads), making it the dominant
  constraint for long context and batching. No specific byte/FLOP figures given.

## Narration review (GATE P)
Listen for: does B01 establish K + V BEFORE the cache? Does B02 land "reuse, don't
recompute"? Does B04 make "memory, not compute, runs out first" clear?

VERDICT: PASS 