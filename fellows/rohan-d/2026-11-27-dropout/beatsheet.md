# Dropout, One Silenced Unit at a Time — Beat Sheet

**Title:** Dropout, One Silenced Unit at a Time
**Slug:** claude-liam-dropout
**Channel:** claude-liam · **Persona:** Liam (in for Bear) · **Register:** Teardown · **Voice:** Kokoro `am_onyx`
**Format:** 16:9 long cut (3840×2160) + a native 9:16 cut (2160×3840), re-composed from the same beats, never a crop

Both cuts render from the beat sheets at true 4K. Durations are Kokoro-measured (`actual_duration_s`), not estimates; start times are cumulative and approximate.

## 16:9 — long cut (11 beats, 2:46 / 166.3s, 3840×2160)

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | ask | 0:00 | 15.9s | ClaudeComposerAsk | Cold open: the ask in the composer, answered with result lines |
| B01 | overview | 0:16 | 10.2s | BrutalistHesitantWriter | The overview, written and corrected on screen: Dropout breaks the network. → trains many networks |
| B02 | one mask | 0:26 | 12.1s | Manim B02_Mask | A random mask silences four of eight units. |
| B03 | scale up | 0:38 | 10.4s | Manim B03_Scale | Survivors double; the output is 38. |
| B04 | many masks | 0:49 | 12.6s | Manim B04_Average | Five noisy outputs around 36; 10,000 average 35.98. |
| B05 | why scale | 1:01 | 10.9s | Manim B05_WhyScale | Unscaled average 18; scaled average 36. |
| B06 | 256 networks | 1:12 | 16.3s | Manim B06_Crowd | 256 masks, one set of weights. |
| B07 | where it bites | 1:28 | 15.1s | Manim B07_Noise | Noise grows with the drop probability. |
| BVDT | verdict | 1:43 | 21.6s | ClaudeVerdictArtifact | Verdict page: Dropout, in six lines |
| BHTF | your turn | 2:05 | 36.0s | ClaudeComposerAsk | Your turn: the prompt typed in the composer, with check lines |
| BOUT | outro | 2:41 | 5.2s | ClaudeTitleOutro | Title restated, handle, mascot; spoken outro with a 1 s silent tail |

## 9:16 — vertical cut

Same beats and narration, re-composed natively for the tall frame (rows and columns instead of wide layouts). Its sources are in [`vertical/`](vertical/).
