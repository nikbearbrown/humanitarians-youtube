# PEDAGOGY — "Claude, Nearest."

Narration sign-off record. Audience: a smart non-technical-to-intermediate
viewer who has used a "semantic search" or RAG product and never had the
geometry explained.

## The one thing this video has to land

**Similarity became a distance, and distance is expensive to compute
exactly at scale — so real systems trade a little accuracy for a lot of
speed, on purpose.** The viewer should leave able to explain why a search
result can be "close enough" rather than "the actual nearest."

## Act structure

| | |
|---|---|
| B00 cold open | ✓ Reframes "similar" as a geometry question before any mechanism |
| B01 executive summary | ✓ One breath: text → vector → distance = similarity |
| B02 framework | ✓ The 2D toy map, stated as a simplification, before any example |
| B03 worked example | ✓ A concrete query and its real nearest neighbors |
| B04 mechanism at scale | ✓ Brute-force vs. graph-hop, shown side by side |
| B05 falsifiability | ✓ Real limit: approximate search can return the wrong neighbor — a named trade-off |
| B06 verdict | ✓ Recall/latency/memory named explicitly as one coupled knob |
| B07 handoff | ✓ A measurable task (recall against brute-force ground truth) |
| B08 outro | ✓ Title restate + sign-off |

## Why a toy 2D map, not a real embedding plot

Real embeddings live in hundreds of dimensions — unplottable directly. The
2D map is explicitly disclosed as a simplification (not a claim about any
specific model's actual geometry) so the mechanism (distance = similarity)
stays teachable without misrepresenting real embedding spaces.
