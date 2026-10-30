# BUILD-LOG — "Planning and Decomposition"

Built 2026-10-26, dated Friday 2026-09-04. Toolkit `brutalist.art` (`ai-explainer`),
Kokoro `am_onyx`, **cost $0.00**.

## Result

| Cut | Format | Runtime | Beats | Slates |
|---|---|---|---|---|
| 16:9 master | 3840×2160 | ~3:41 | 13 | 0 |
| 9:16 Short | 2160×3840 | ~2:35 | 8 + endcard | 0 |

## What QC caught

1. **An em dash survived in the narration of BOUT.** House style forbids it: it reads as a pause the voice does not take. Rewritten by hand into a full stop or a colon rather than swapped for a comma, since the sentence wanted the stronger break. The affected beat's audio was regenerated and the reel recompiled in both aspect ratios, because new words mean a new duration and the measured duration is what every other beat is cut against. Found by scanning all 489 narration lines in the batch for em dashes, spoken week or episode numbers, and back-references, rather than by re-reading the four sheets I happened to have open.

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
