# SHOTLIST — Softmax and Temperature, Explained

| Beat | Act | Lane | Component / scene | Shot type × source | Fill |
|---|---|---|---|---|---|
| B00 | ASK | Remotion | `ClaudeComposerAsk` (Bonjour, Liam) | GRAPHIC × remotion | machine |
| B01 | BLUF | Remotion | `BrutalistHesitantWriter`: "picks the likeliest word" corrected to "rolls weighted dice" | GRAPHIC × remotion | machine |
| B02 | FRAMEWORK | Manim | `B02_Machine`: prompt → model → logits → softmax → probabilities → sampler → loop | GRAPHIC × own | machine |
| B03 | FRAMEWORK | Manim | `B03_Formula`: MathTex softmax-with-T, box spotlight plus glossary per symbol | GRAPHIC × own | machine |
| B04 | WORKED_EXAMPLE | Manim | `B04_WorkedT1`: table token \| z \| eᶻ \| p fills in formula order; p becomes bars | GRAPHIC × own | machine |
| B05 | MECHANISM | Manim | `B05_TempSweep`: five bars morph as a dial sweeps 0.2 → 1 → 2; rank badges fixed | GRAPHIC × own | machine |
| B06 | MECHANISM | Manim | `B06_Rolls`: 0–1 probability strip, seeded tick, the same 20 rolls on three strips plus word-chip rows | GRAPHIC × own | machine |
| B07 | FALSIFIABILITY | Manim | `B07_TenThousand`: predicted outlines vs counted bars, 10,000 draws, three panels | GRAPHIC × own | machine |
| B08 | MECHANISM | Manim | `B08_Greedy`: the strip collapses as T → 0; MathTex limit; 20 × "mat" | GRAPHIC × own | machine |
| B09 | FALSIFIABILITY | Manim | `B09_WrongRanking`: constructed Sydney/Canberra bars, "wrong" counter, fixed ranks | GRAPHIC × own | machine |
| BVDT | VERDICT | Remotion | `ClaudeVerdictArtifact` (6 lines) | GRAPHIC × remotion | machine |
| BHTF | YOUR_TURN | Remotion | `ClaudeComposerAsk` (Your turn.) | GRAPHIC × remotion | machine |
| BOUT | OUTRO | Remotion | `ClaudeTitleOutro` (locked) | GRAPHIC × remotion | machine |

The pantry is empty by design: every visual is computed (EXECUTABLE-EVIDENCE.md). There are no stills and no AI footage.

**Motion languages** (budget: none in more than about 40% of beats):
- composer: 2 of 13
- hesitant writer: 1
- node diagram: 1
- equation spotlight: 1
- table: 1
- morphing bars: 3 (B05, B07, B09), 23%
- probability strip: 2 (B06, B08)
- verdict card: 1
- outro: 1

**Library-first (GATE L), 2026-11-22.** All queries ran with `scene_search.py --no-log`, so nothing was written to the toolkit.
- **"softmax":** no match. A genuine miss.
- **"probability bars reshaping as a temperature knob turns":** ReqBars and TtEffectBars. Both are reel-local, with static two-series props. Neither morphs.
- **"sampling dice weighted random draw":** TeachClaudeFig3 and ValuesCompressionFunnel. Film-specific, with only a `sparkLine` prop.
- **"stacked probability strip with a dart landing":** FinanceStackedBar (derived text, finance periods) and ExecutedData (tables). Neither drops a sample tick.
- **"bar chart counts observed versus predicted":** BarChart (single-series, teal accent, which conflicts with the Claude palette) and DoodleChart (banned).
- **"equation with symbol glossary spotlight":** SeisSpotlightOpen and HorrorEquation. Wrong brand and wrong purpose.
- **"pipeline prompt model logits probabilities next token loop":** CCHarnessMap, which is concentric rings for cc-explainer, not a left-to-right loop.

**Decision:** Manim for all eight body beats, like film 1. The beats need quantities that move on the spoken word (morphing bars, falling ticks, a collapsing strip), and that is Manim's lane. A reusable `SoftmaxBars` component would be a library candidate later. That is not built here, because this session may not write inside the toolkit.
