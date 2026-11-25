# SHOTLIST — Gradient Descent, One Step at a Time

| Beat | Act | Lane | Component / scene | Shot type × source | Fill |
|---|---|---|---|---|---|
| B00 | ASK | Remotion | `ClaudeComposerAsk` | GRAPHIC × remotion | machine |
| B01 | BLUF | Remotion | `BrutalistHesitantWriter` | GRAPHIC × remotion | machine |
| B02 | FRAMEWORK | Manim | `B02_Landscape` — the bowl, the ball, the tangent slope, the step arrow | GRAPHIC × own | machine |
| B03 | FRAMEWORK | Manim | `B03_UpdateRule` — MathTex update rule with a moving spotlight and glossary labels | GRAPHIC × own | machine |
| B04 | WORKED_EXAMPLE | Manim | `B04_FiveSteps` — the ball steps with a table of executed values | GRAPHIC × own | machine |
| B05 | FALSIFIABILITY | Manim | `B05_StepSize` — three bowls (η = 0.01 / 0.1 / 1.1) side by side | GRAPHIC × own | machine |
| B06 | FALSIFIABILITY | Manim | `B06_TwoValleys` — non-convex loss, the ball stops in the shallow valley | GRAPHIC × own | machine |
| B07 | MECHANISM | Manim | `B07_Batches` — contour map with full-batch and mini-batch paths | GRAPHIC × own | machine |
| BVDT | VERDICT | Remotion | `ClaudeVerdictArtifact` | GRAPHIC × remotion | machine |
| BHTF | YOUR_TURN | Remotion | `ClaudeComposerAsk` (Your turn.) | GRAPHIC × remotion | machine |
| BOUT | OUTRO | Remotion | `ClaudeTitleOutro` (locked) | GRAPHIC × remotion | machine |

The pantry is empty by design: every visual is computed (EXECUTABLE-EVIDENCE.md). There are no stills and no AI footage.

**Library-first (GATE L), 2026-11-22.**
- Queries tried: "ball rolling down a loss curve", "equation with symbol glossary", "three side-by-side panels", "contour plot optimization path", "line chart of loss over steps".
- The hits were film-specific figures with hard-coded content (CodingAgentsFig2Gradient, TeachClaudeFig*, CadencesFig6Tide) that expose only a `sparkLine` prop, so none can be reused.
- The general components `TypesetMath` and `ExecutedData` were considered. Manim was chosen instead because the equation needs a moving spotlight and the table must step in sync with the ball, and "quantities that move" is Manim's lane in the explainer doctrine.
