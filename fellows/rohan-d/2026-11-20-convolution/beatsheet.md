# Convolution, One Window at a Time — Beat Sheet

**Title:** Convolution, One Window at a Time
**Slug:** claude-liam-convolution
**Channel:** claude-liam · **Persona:** Liam (in for Bear) · **Register:** Teardown · **Voice:** Kokoro `am_onyx`
**Format:** 16:9 long cut (3840×2160) + a native 9:16 cut (2160×3840), re-composed from the same beats, never a crop

Both cuts render from the beat sheets at true 4K. Durations are Kokoro-measured (`actual_duration_s`), not estimates; start times are cumulative and approximate.

## 16:9 — long cut (11 beats, 2:43 / 163.0s, 3840×2160)

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | ask | 0:00 | 15.5s | ClaudeComposerAsk | Cold open: the ask in the composer, answered with result lines |
| B01 | overview | 0:16 | 10.4s | BrutalistHesitantWriter | The overview, written and corrected on screen: A convolution reads the whole image. → slides a small window |
| B02 | the image | 0:26 | 11.1s | Manim B02_Image | A six by six image with one vertical edge. |
| B03 | one window | 0:37 | 12.4s | Manim B03_Window | One window: multiply pixel by weight, add. |
| B04 | slide it | 0:49 | 13.8s | Manim B04_Slide | Sliding the window along the top row fills the output with 0, 27, 27, 0. |
| B05 | the map | 1:03 | 9.8s | Manim B05_Map | The whole output map lights up along the edge. |
| B06 | shared weights | 1:13 | 16.4s | Manim B06_Share | Nine shared weights against 576. |
| B07 | where it bites | 1:29 | 10.6s | Manim B07_Shrink | Each unpadded 3x3 layer shrinks the map by two. |
| BVDT | verdict | 1:40 | 18.9s | ClaudeVerdictArtifact | Verdict page: Convolution, in six lines |
| BHTF | your turn | 1:59 | 39.2s | ClaudeComposerAsk | Your turn: the prompt typed in the composer, with check lines |
| BOUT | outro | 2:38 | 4.8s | ClaudeTitleOutro | Title restated, handle, mascot; spoken outro with a 1 s silent tail |

## 9:16 — vertical cut

Same beats and narration, re-composed natively for the tall frame (rows and columns instead of wide layouts). Its sources are in [`vertical/`](vertical/).
