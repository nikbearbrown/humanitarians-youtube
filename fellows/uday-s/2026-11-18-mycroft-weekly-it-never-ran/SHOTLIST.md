# SHOTLIST — It Never Ran

12 beats · measured Kokoro `am_onyx` · 223.9s (3:44) · 3840x2160

| Beat | Act | Source | Measured | Frame |
|---|---|---|---|---|
| B00 | INTRO | remotion `ClaudeComposerAsk` | 13.14s | composer; the week's ask answered in three lines; author's name spoken |
| B01 | PROBLEM | manim | 21.31s | before/after loader cards, connector down to "the output: byte for byte identical", then the conclusion line |
| B02 | FRAMEWORK | manim | 17.30s | three numbered question cards, the third in terracotta |
| B03 | CLI | remotion `ClaudeComposerAsk` | 6.04s | the instrumentation ask |
| B04 | CODE | remotion `ClaudeCodeBeat` | 13.08s | the runner construction, verbatim from the parent commit, with the caret under `.replace(/\n/g, '\n')` |
| B05 | OUTPUT | manim | 30.07s | **HERO** — three stacked panels, each with its real interpreter output; the third shows no error at all |
| B06 | OUTPUT | manim | 21.35s | four-step vertical flow (throws → catch → fallback → correct answer) with the 2026-10-09 chip below |
| B07 | OUTPUT | manim | 20.03s | the "4" stat card over the "not touched, on purpose" panel |
| B08 | FALSIFIABILITY | manim | 34.21s | three ticked verified rows in a box, over the terracotta totals comparison |
| B09 | SUMMARY | manim | 32.46s | the 8 added subsystems, the deliberate exclusions, the untested-version chip |
| B10 | NEXT STEPS | remotion `ClaudeComposerAsk` | 13.61s | the scaffolded prompt with a GOOD/BAD discriminator |
| B11 | OUTRO | remotion `ClaudeTitleOutro` | 1.26s | title restate |

## Motion

Every Manim beat is `build`, `reveal` or `resolve`. B04's motion is labelled
**reveal** (it reveals code line by line), not `fade` — the motion cap counts
`fade` against the reel and the label would be inaccurate anyway.

## Composition rule applied throughout

Every multi-element Manim beat is **stacked**, not laid out in a wide row,
except B02, whose three cards are tall enough that the row is not width-limited.
This is the fix for the repeated underfill MAJORs in earlier episodes: a wide,
short group cannot be scaled up by `fit()` and leaves dead bands.

## Claude UI appears only in B00, B03, B04, B10, B11

Per the ILLUSTRATE LAW. Every evidence beat is a data animation.
