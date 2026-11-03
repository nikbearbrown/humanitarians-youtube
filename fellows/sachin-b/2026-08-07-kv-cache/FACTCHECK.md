# FACTCHECK — "Claude, Cached."

| Claim (beat) | Verdict | Source / derivation |
|---|---|---|
| Attention needs the K/V of every past token (B01/B02) | ✓ | Definition of causal self-attention (Vaswani et al., 2017, "Attention Is All You Need") |
| Past tokens' K/V never change once computed (B02) | ✓ | Causal masking: position i's K/V depends only on tokens ≤ i — the entire justification for KV-caching in every production inference stack (HuggingFace `transformers` `use_cache`, vLLM) |
| Prefill computes K/V for the whole prompt in one parallel pass; decode is one token at a time (B03/B04) | ✓ | Standard two-phase description of autoregressive LLM inference (prefill/decode), per the vLLM paper ("PagedAttention", 2023) |
| Cache size grows linearly with tokens × layers × heads (B05) | ✓ | Direct consequence of storing one K/V pair per token per layer per head — a memory-accounting fact, not a benchmark |
| Long-context cost is dominated by cache memory, not "thinking harder" (B05/B06) | ✓ | Consistent with the motivation stated in PagedAttention and subsequent KV-cache-compression literature |

## Corrections applied

None needed. One disclosed simplification: B02-B04 illustrate a single
attention head/layer for clarity; B05's growth claim accounts for the real
multi-layer/multi-head total explicitly.

## Numbers on screen

None invented — B05's growth chart is a qualitative linear shape, not a
plotted dataset.
