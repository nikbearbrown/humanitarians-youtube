# Why Attention Divides By The Square Root — Beat Sheet

**Title:** Why Attention Divides By The Square Root
**Slug:** tldr-attention-scaling
**Channel:** claude-liam · **Persona:** Liam (in for Bear) · **Register:** Teardown · **Voice:** Kokoro `am_onyx`
**Format:** 16:9 long cut (3840×2160) + a native 9:16 cut (2160×3840), re-composed from the same beats, never a crop

Both cuts render from the beat sheets at true 4K. Durations are Kokoro-measured (`actual_duration_s`), not estimates; start times are cumulative and approximate.

## 16:9 — long cut (16 beats, 3:41 / 220.8s, 3840×2160)

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | tldr · what | 0:00 | 18.0s | ClaudeTldrWhat | TL;DR card one: what the film is about |
| B01 | tldr · why | 0:18 | 14.8s | ClaudeTldrWhy | TL;DR card two: why you should care |
| B02 | the question | 0:33 | 9.6s | BrutalistHesitantWriter | The overview, written and corrected on screen: Why does attention divide its scores by a number you could pick by hand? → the square root of the vector length |
| B03 | terms | 0:42 | 14.0s | ClaudeDefinitions | Terms card: the vocabulary the film uses |
| B10 | learn 1 · HOOK | 0:56 | 14.7s | Manim B10_SixBars | Six bars (keys) with weights from the seeded run; a length readout sweeps 4 → 512 and the bars snap to one-hot. |
| B11 | learn 1 · INSTANCE | 1:11 | 14.1s | Manim B11_ScoresSpread | Number line with six dots (seeded instance); a length readout steps through four values; a counter shows the average largest weight. |
| B12 | learn 1 · INSTANCE | 1:25 | 12.9s | Manim B12_FlatEnds | Softmax curve with dots parked at length 4, then 512 on its flat ends; a slope readout labelled 'our measure'. |
| B13 | learn 1 · NAIVE | 1:38 | 12.8s | Manim B13_FixedTen | Three panels of six bars (lengths 4, 64, 2048) after dividing by 10, with the uniform line at 0.167. |
| B14 | learn 1 · SHIFT | 1:51 | 13.1s | Manim B14_WidthVsLength | Plot of score-cloud width versus length with six measured points landing on a square-root curve; a HOLD on 'commit'. |
| B15 | learn 1 · TRANSFORM | 2:04 | 6.1s | Manim B15_Fold | The length-512 dots shrink in place onto a width-1 band (same dots, same labels); the six bars beneath morph from one-hot to [0.027 0.356 0.278 0.085 0.103 0.151]. |
| B16 | learn 1 · ABSTRACTION | 2:10 | 13.2s | Manim B16_NameIt | The width band from B15 turns into the equation: Var(q·k)=d_k, then the divided form; both typeset as MathText SVG, revealed one line at a time. |
| B17 | learn 1 · TANGENT | 2:23 | 15.9s | Manim B17_ReadIt | Split stage: equation persists on the main side; side band writes the sentence, the claim, the Role glossary (q, k random variables; d a fixed count) and the d=512 check. |
| B18 | learn 1 · PAYOFF | 2:39 | 12.0s | Manim B18_SixBarsBack | The same six bars as B10: raw one-hot beside the scaled spread, same objects, same labels. |
| BVDT | verdict | 2:51 | 17.7s | ClaudeVerdictArtifact | Verdict page: Why Attention Divides By The Square Root |
| BHTF | your turn | 3:09 | 27.4s | ClaudeComposerAsk | Your turn: the prompt typed in the composer, with check lines |
| BOUT | outro | 3:36 | 4.6s | ClaudeTitleOutro | Title restated, handle, mascot; spoken outro with a 1 s silent tail |

## 9:16 — vertical cut

Same beats and narration, re-composed natively for the tall frame (rows and columns instead of wide layouts). Its sources are in [`vertical/`](vertical/).
