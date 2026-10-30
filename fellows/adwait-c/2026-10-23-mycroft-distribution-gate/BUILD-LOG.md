# BUILD-LOG — "May This Leave the System?"

Built 2026-10-26, dated Friday 2026-10-23. Toolkit `brutalist.art` (`ai-explainer`),
Kokoro `am_onyx`, **cost $0.00**.

## Result

| Cut | Format | Runtime | Beats | Slates |
|---|---|---|---|---|
| 16:9 master | 3840×2160 | ~3:35 | 13 | 0 |
| 9:16 Short | 2160×3840 | ~2:28 | 8 + endcard | 0 |

## What QC caught

1. **B03 miscounted the gate and dropped its own point.** It showed four BLOCKED lines under the heading "Four conditions, four refusals". The gate has five conditions, and called with nothing the fifth **clears**, because no disagreement log means nobody dissented. That asymmetry is the subject of B07, so omitting it here contradicted the video. All five lines are now shown, the heading reads "Four refuse. One clears on nothing.", and the narration was rewritten and its audio regenerated.

2. **A named approver was shown without saying it is a fixture.** B05 displayed `approved by Dana Whitfield, Controller` with no qualifier, in a beat a viewer reads as a real approval record. Now labelled `(fixture)` on screen. The same label was added to the materiality video's four-attempt beat.

3. B07's two cards overlapped: a two-line sub pushed one card past its slot. Subs shortened to one line each.

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
