# SOURCES — screenshot-prompt-caching

Every on-screen claim, number, and code snippet mapped to its source.

## Core facts

| Claim | Value | Source |
|---|---|---|
| 50-turn task | exactly per card | video-ideas.md Candidate 3 example seed |
| 5 unique desktop states (A→E) | exactly per card | same |
| ~2000 tokens per screenshot | per card | same |
| Without caching: 50 × 2000 = 100,000 tokens | arithmetic verified | same |
| With caching: 5 × 2000 = 10,000 tokens | arithmetic verified | same |
| Savings: 90% | (100,000-10,000)/100,000 = 90% | derived from seed |
| cache_control={"type": "ephemeral"} | exact field name | computer-use-best-practices README.md |

## Beat-level citations

- B03 filmstrip: 50 turns, 5 unique states, MISS/HIT labeling — all from the card's example seed
- B03 token counters: 10,000 vs 100,000 — from the example seed arithmetic

Source credit shown on screen: "Source: Claude Quickstarts (Anthropic)"
