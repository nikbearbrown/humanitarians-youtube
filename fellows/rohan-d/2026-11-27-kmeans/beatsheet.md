# K-Means, One Reassignment at a Time — Beat Sheet

**Title:** K-Means, One Reassignment at a Time
**Slug:** claude-liam-kmeans
**Channel:** claude-liam · **Persona:** Liam (in for Bear) · **Register:** Teardown · **Voice:** Kokoro `am_onyx`
**Format:** 16:9 long cut (3840×2160) + a native 9:16 cut (2160×3840), re-composed from the same beats, never a crop

Both cuts render from the beat sheets at true 4K. Durations are Kokoro-measured (`actual_duration_s`), not estimates; start times are cumulative and approximate.

## 16:9 — long cut (11 beats, 2:59 / 179.1s, 3840×2160)

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | ask | 0:00 | 13.9s | ClaudeComposerAsk | Cold open: the ask in the composer, answered with result lines |
| B01 | overview | 0:14 | 11.2s | BrutalistHesitantWriter | The overview, written and corrected on screen: K-means finds the true groups. → settles on a stable guess |
| B02 | the start | 0:25 | 9.4s | Manim B02_Start | Seven points and two starting centers. |
| B03 | assign | 0:35 | 11.1s | Manim B03_Assign | Each point joins its nearest center. |
| B04 | update | 0:46 | 13.2s | Manim B04_Update | Each center moves to the mean of its group. |
| B05 | repeat | 0:59 | 6.7s | Manim B05_Repeat | A second assignment changes nothing. |
| B06 | inertia | 1:06 | 13.2s | Manim B06_Inertia | Inertia falls from 19.25 to 8.53 and never rises. |
| B07 | where it bites | 1:19 | 17.1s | Manim B07_BadStart | Two starts settle on two different stable splits. |
| BVDT | verdict | 1:36 | 29.1s | ClaudeVerdictArtifact | Verdict page: K-means, in six lines |
| BHTF | your turn | 2:05 | 49.0s | ClaudeComposerAsk | Your turn: the prompt typed in the composer, with check lines |
| BOUT | outro | 2:54 | 5.1s | ClaudeTitleOutro | Title restated, handle, mascot; spoken outro with a 1 s silent tail |

## 9:16 — vertical cut

Same beats and narration, re-composed natively for the tall frame (rows and columns instead of wide layouts). Its sources are in [`vertical/`](vertical/).
