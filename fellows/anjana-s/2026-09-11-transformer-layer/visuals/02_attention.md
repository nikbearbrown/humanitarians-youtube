# Beat 2 — Self-Attention

**Visual type:** Remotion
**Duration:** ~13 seconds

## What the viewer sees

Inside the expanded layer. The "revenue" token is center stage. The other sentence tokens (we, expect, growth, to, moderate) are arranged in a horizontal row nearby.

**QKV split (0-3s):**
Three vectors split out from "revenue," each a different color and direction:
- Q (query): gold arrow pointing outward, labeled "Q: What should I attend to?"
- K (key): blue arrow
- V (value): green arrow

The other tokens also briefly show their K and V vectors, dimmer and smaller. Every token has keys and values. Only "revenue" is actively querying right now.

**Attention scores (3-8s):**
The gold Q arrow from "revenue" reaches out to each other token's blue K arrow. Where they meet, a score appears:

- "revenue" → "growth": **0.42** (thick bright line)
- "revenue" → "moderate": **0.31** (medium line)
- "revenue" → "expect": **0.15** (thin line)
- "revenue" → "we": **0.07** (faint line)
- "revenue" → "to": **0.05** (barely visible line)

The lines visually convey relevance: thick = important, thin = irrelevant. A small "softmax" label appears briefly as the scores normalize.

**Weighted sum (8-13s):**
Each token's green V vector scales in size based on its attention score. "Growth" has a large V. "We" has a tiny V. All scaled V vectors flow toward "revenue" and merge into a single new vector.

The "revenue" block updates. Its glow changes subtly from the original. It looks the same, but it now carries context from the entire sentence.

Label: "Same word. New meaning. Context-aware."

## Technical notes

- QKV colors: Q=gold, K=blue, V=green. Keep consistent
- Line thickness directly maps to attention score, the visual IS the data
- The weighted sum merging animation should feel like information flowing inward
- The "revenue" block changing glow subtly conveys that the representation updated
- Simplified to single-head attention for clarity
