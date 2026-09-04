# PROMPT — "Claude, Cached."

## The brief

Explain the KV-cache: why LLM text generation speeds up after the first
token — a real systems-level mechanism behind why "thinking" feels slow but
streaming feels fast. One of 4 CS/ML concept videos requested for the
weekly STEM-video slot, paired to Week 1.

## Constraints given

| Constraint | Resolution |
|---|---|
| ≤3:00, "one insight" reel | Measured 1:35 |
| No invented numbers/benchmarks | Every claim is a structural property (causal masking, K/V dimensionality), not a measured figure |
| A falsifiability/limit beat | Unbounded cache growth — the real cost of the mechanism |
| Persona | `claude-liam` (Kokoro `am_onyx`) |
| Skill | `ai-explainer` — mandatory executive-summary beat, ILLUSTRATE LAW (UI only at bookends) |

## Structure

```
B00  cold open              the felt experience, named
B01  executive summary      cache K/V, don't recompute
B02  framework              every token makes a K/V; the past is fixed
B03  worked example         prefill — the whole prompt, one pass
B04  worked example         decode — one token, attends to the cache
B05  falsifiability         the cache only ever grows
B06  verdict                compute traded for memory
B07  handoff                measure prefill vs. decode yourself
B08  outro                  title restate
```
