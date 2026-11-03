# PROMPT — "Claude, Nearest."

## The brief

Explain vector embeddings and ANN search: why "similar" text ends up as
nearby points in space, and how search finds them fast at scale. Second of
4 concept videos, paired to Week 2.

## Constraints given

| Constraint | Resolution |
|---|---|
| ≤3:00, "one insight" reel | Measured 1:34 |
| No invented numbers/benchmarks | Toy 2D map explicitly disclosed as a simplification |
| A falsifiability/limit beat | Approximate search can miss the true nearest neighbor |
| Persona | `claude-liam` (Kokoro `am_onyx`) |
| Skill | `ai-explainer` — executive-summary beat, ILLUSTRATE LAW |

## Structure

```
B00  cold open           similarity as a location
B01  executive summary   text -> vector -> distance
B02  framework           2D map, clustering by meaning
B03  worked example       a query and its nearest neighbors
B04  mechanism at scale   brute-force vs. graph hop
B05  falsifiability       approximate can miss
B06  verdict              recall/latency/memory, one knob
B07  handoff              measure recall yourself
B08  outro                title restate
```
