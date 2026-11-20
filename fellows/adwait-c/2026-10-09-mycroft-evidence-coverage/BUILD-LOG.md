# BUILD-LOG — "Citations Nobody Checks"

Built 2026-10-26, dated Friday 2026-10-09. Toolkit `brutalist.art` (`ai-explainer`),
Kokoro `am_onyx`, **cost $0.00**.

## Result

| Cut | Format | Runtime | Beats | Slates |
|---|---|---|---|---|
| 16:9 master | 3840×2160 | ~3:36 | 13 | 0 |
| 9:16 Short | 2160×3840 | ~2:31 | 8 + endcard | 0 |

## What QC caught

1. **The per-claim split was fabricated.** B05 and B07 showed revenue 6, cogs 5, opex 5, payroll 5. The real run is revenue 6, opex 9, cogs 3, payroll 3. Both sum to 21, which is exactly why it survived the first pass: the headline figure was right and the breakdown was not. Caught by re-running `cli coverage` and reading `per_claim` rather than trusting the beat sheet. Both beats re-rendered.

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
