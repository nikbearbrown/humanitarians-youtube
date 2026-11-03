# SHOTLIST — hussain-bond-pricing-duration (16:9 master)

| Beat | Act | Fill | Source |
|---|---|---|---|
| B00 | INTRO (cold open) | Remotion `ClaudeComposerAsk` | media/B00.mp4 |
| B01 | PROBLEM | Manim `B01_ProblemSetup` | manim/B01.mp4 |
| B02 | CLI — ask | Remotion `ClaudeComposerAsk` | media/B02.mp4 |
| B03 | CODE | Remotion `ClaudeCodeBeat` | media/B03.mp4 |
| B04 | OUTPUT — run | Manim `B04_PriceYieldCurve` | manim/B04.mp4 |
| B05 | CLI — change (revision) | Remotion `ClaudeComposerAsk` | media/B05.mp4 |
| B06 | CODE — diff | Remotion `ClaudeCodeBeat` | media/B06.mp4 |
| B07 | OUTPUT — better | Manim `B07_ConvexityCompare` | manim/B07.mp4 |
| B08 | SUMMARY | Remotion `ClaudeVerdictArtifact` | media/B08.mp4 |
| B09 | NEXT STEPS (handoff) | Remotion `ClaudeComposerAsk` | media/B09.mp4 |
| B10 | OUTRO | Remotion `ClaudeTitleOutro` | media/B10.mp4 |

11 beats, all machine-fillable — no human pantry slots required for the 16:9 master.

## 9:16 derivation
`./art shorts <reel>` reformats this master (all beats fit comfortably under the
3:00 Shorts cap, so no beats are cut). Remotion beats auto-rewire to their
`*916` compositions (ONDA CHECK); Manim beats (B01, B04, B07) need portrait
layouts in `short/scenes.py` — see that file once generated.
