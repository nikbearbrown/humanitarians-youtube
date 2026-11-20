# BUILD-LOG — "How Old Is the Evidence?"

Built 2026-10-26, dated Friday 2026-09-25. Toolkit `brutalist.art` (`ai-explainer`),
Kokoro `am_onyx`, **cost $0.00**.

## Result

| Cut | Format | Runtime | Beats | Slates |
|---|---|---|---|---|
| 16:9 master | 3840×2160 | ~3:26 | 13 | 0 |
| 9:16 Short | 2160×3840 | ~2:21 | 8 + endcard | 0 |

## What QC caught

1. **The verdict was not reproducible from what was on screen.** B02 showed `verdict STALE` with no limits. Re-running the engine at the obvious limits (lag 10, age 45) returns **EXPIRED**, not STALE, because 92 days is past a 45 day age limit. The narration's "the engine calls it stale" is true only under supplied limits of lag 10 and age 120, which the screen never showed. Fixed by putting `limits supplied   lag 10 days, age 120 days` on the artifact, so the verdict can be reproduced. Numbers unchanged; they were already right.

## Toolkit work this build required

Three fixes to `brutalist.art`, all backwards compatible:

- **`ClaudeCodeBeat` had a hardcoded `python` badge.** A JavaScript file rendered with a
  PYTHON label. Added a `lang` prop defaulting to `python`, so every existing beat is
  unchanged.
- **Comment colouring only recognised `#`.** JavaScript `//` comments rendered as code.
  Now both are recognised. Python never starts a line with `//`, so nothing regressed.
- **The code card was a fixed slab at a fixed font size.** A three-line beat rendered as a
  mostly empty rectangle and a long line could run past the right edge. The type is now
  sized to whichever axis binds first and the card hugs the result, centred in its band.

Every code beat in these twelve reels was re-rendered against the fixed component so the
series is consistent.

## What was not done

Nothing was published, uploaded or sent. The masters stay in this folder until a human
moves them to the Drive, and no notification was issued to anyone.
