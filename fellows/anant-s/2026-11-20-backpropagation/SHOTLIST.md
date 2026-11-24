# SHOTLIST — Backpropagation, One Error at a Time

| Beat | Act | Lane | Component / scene | Fill |
|---|---|---|---|---|
| B00 | ASK | Remotion | `ClaudeComposerAsk` | machine |
| B01 | BLUF | Remotion | `BrutalistHesitantWriter` | machine |
| B02 | FRAMEWORK | Manim | `B02_Chain`: the network as a chain of 4 ops, with local-slope tags | machine |
| B03 | FRAMEWORK | Manim | `B03_ChainRule`: MathTex chain rule with box spotlights per factor | machine |
| B04 | WORKED_EXAMPLE | Manim | `B04_Forward`: executed values fill forward | machine |
| B05 | WORKED_EXAMPLE | Manim | `B05_Backward`: gradients flow back, then one update step | machine |
| B06 | MECHANISM | Manim | `B06_Check`: finite difference vs backprop, then cost bars | machine |
| B07 | FALSIFIABILITY | Manim | `B07_Vanishing`: 10 sigmoid layers with gradient bars on a log scale | machine |
| BVDT | VERDICT | Remotion | `ClaudeVerdictArtifact` (6 lines) | machine |
| BHTF | YOUR_TURN | Remotion | `ClaudeComposerAsk` (Your turn.) | machine |
| BOUT | OUTRO | Remotion | `ClaudeTitleOutro` (locked) | machine |

The pantry is empty by design: every visual is computed.

**Library-first.** Nothing general exists for a computational-graph chain, and moving gradients are Manim's lane. The chain, chain-rule and cost visuals follow film 1's house style: cream background, EB Garamond, one terracotta accent per beat.
