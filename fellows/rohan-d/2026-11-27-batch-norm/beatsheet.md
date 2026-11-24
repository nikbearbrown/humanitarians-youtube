# Batch Normalization, One Rescale at a Time — Beat Sheet

**Title:** Batch Normalization, One Rescale at a Time
**Slug:** claude-liam-batch-norm
**Channel:** claude-liam · **Persona:** Liam (in for Bear) · **Register:** Teardown · **Voice:** Kokoro `am_onyx`
**Format:** 16:9 long cut (3840×2160) + a native 9:16 cut (2160×3840), re-composed from the same beats, never a crop

Both cuts render from the beat sheets at true 4K. Durations are Kokoro-measured (`actual_duration_s`), not estimates; start times are cumulative and approximate.

## 16:9 — long cut (11 beats, 3:00 / 179.6s, 3840×2160)

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | ask | 0:00 | 14.4s | ClaudeComposerAsk | Cold open: the ask in the composer, answered with result lines |
| B01 | overview | 0:14 | 11.4s | BrutalistHesitantWriter | The overview, written and corrected on screen: Normalization just tidies the numbers. → reshapes the landscape |
| B02 | two scales | 0:26 | 12.6s | Manim B02_Scales | Two rows of identical dots with numbers a hundred times apart. |
| B03 | normalize A | 0:38 | 14.6s | Manim B03_Normalize | Subtract the mean, then divide by the spread. |
| B04 | normalize B | 0:53 | 9.9s | Manim B04_Same | Both features normalize to the same four numbers. |
| B05 | the valley | 1:03 | 19.0s | Manim B05_Valley | Condition number 3,182,113 against 1.4; 4 steps against over 100,000. |
| B06 | gamma and beta | 1:22 | 18.2s | Manim B06_GammaBeta | Learnable scale and shift undo the rescale if needed. |
| B07 | where it bites | 1:40 | 13.3s | Manim B07_SmallBatch | Small batches give noisy statistics; a batch of one gives zeros. |
| BVDT | verdict | 1:53 | 21.1s | ClaudeVerdictArtifact | Verdict page: Batch normalization, in six lines |
| BHTF | your turn | 2:15 | 39.6s | ClaudeComposerAsk | Your turn: the prompt typed in the composer, with check lines |
| BOUT | outro | 2:54 | 5.5s | ClaudeTitleOutro | Title restated, handle, mascot; spoken outro with a 1 s silent tail |

## 9:16 — vertical cut

Same beats and narration, re-composed natively for the tall frame (rows and columns instead of wide layouts). Its sources are in [`vertical/`](vertical/).
