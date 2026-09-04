# PROMPT — "Claude, Ringed."

## The brief

Explain consistent hashing: the ring, minimal remapping, and virtual
nodes. Third of 4 concept videos, paired to Week 3. Explicitly relevant to
system-design interview prep.

## Constraints given

| Constraint | Resolution |
|---|---|
| ≤3:00, "one insight" reel | Measured 1:33 |
| No invented numbers/benchmarks | Only quantitative claim ("~1/N keys move") is a structural property of the algorithm |
| A falsifiability/limit beat | Uneven load at small N, fixed by virtual nodes |
| Persona | `claude-liam` (Kokoro `am_onyx`) |
| Skill | `ai-explainer` — executive-summary beat, ILLUSTRATE LAW |

## Structure

```
B00  cold open           mechanism, not buzzword
B01  executive summary   one circle, servers and keys
B02  framework           the ring
B03  worked example      four keys, assigned
B04  dynamic case        add a 5th server
B05  falsifiability      uneven arcs at small N
B06  verdict             virtual nodes required
B07  handoff             build it, measure it
B08  outro               title restate
```
