# Two Resolutions, One Click — The macOS Coordinate Roundtrip — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a Teardown scaffold). Register: **Plain**.*
*Carry-out written first (CARRY-OUT.md). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (free Remotion, WRITER LAW — no puppet, no
Seedance). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer / stakes+wrong-guess | "Claude clicks at 630, 420. You'd guess that's your screen's exact pixel. It isn't — it's scaled, because macOS Retina screenshots get resized before Claude ever sees them. Where does the real click land?" | Writer types "Claude clicks at (630, 420) on my screens exact spot right?", hesitates on "exact", corrects to "scaled" |
| B01 | 1 stakes / **4 anchor planted** | Here's why macOS needs its own transform. A Retina screenshot's native pixels — 2560 by 1600 on many MacBook Pros — are far bigger than the API's image budget: the long edge has to stay under 1568 pixels, and the image can't cut into more than 1568 of its 28 by 28 tiles. The reference implementation resizes first, down to 1344 by 840, before Claude ever looks. Same button, two different coordinate spaces. | THE ANCHOR — two rectangles (2560×1600 native / 1344×840 sent), same button dot, bridged by a question mark |
| B02 | 2 wrong guess, **broken by a case** | The obvious guess: take Claude's number and click it directly — Claude clearly saw the button. Try that on the real 2560 by 1600 screen and you miss badly. 630, 420 was never the button's real position on your screen — that was only where it sat in the smaller, resized picture Claude was looking at. | Same anchor pair; raw (630, 420) carried straight onto the 2560×1600 rectangle — misses, struck |
| B03 | 3 mechanism (no flag — fully sourced) | The fix ports the API's own resize algorithm: a binary search for the largest width and height that keep the same aspect ratio, the long edge under 1568 pixels, and the tile count under 1568. For a 2560 by 1600 screen, that's 1344 by 840. Record those sent dimensions — they're the denominator of the inverse: real equals model, times native, divided by sent. | Formula card: `real = model × (native / sent)`, worked to 1344×840. Source: Claude Quickstarts (Anthropic) |
| B04 | **4 anchor payoff** / **5 both directions** | Run it on Claude's own click: 630 times 2560 over 1344 is 1200. 420 times 1600 over 840 is 800. The click lands exactly on the button. That inverse only matters when a resize actually happened. If a screenshot already fits the budget, target underscore image underscore size leaves it unchanged — sent equals native, and there's nothing left to multiply back. | THE ANCHOR RETURNS — same rectangle pair, dot now lands on target; a second small card beside it: "already fits the budget → sent = native, nothing to invert" |
| **BCRY** | **6 carry-out** | A Claude coordinate on macOS isn't wrong — it's measured on a resized copy of your Retina screen. Multiply back by native over sent, and the click lands exactly where you meant. | The sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me: "My MacBook's screenshot is 2560 by 1600, but Claude sees it resized to 1344 by 840 — write the inverse transform so a click Claude makes lands on my real screen." Paste that into Claude. Does it handle a screen that isn't the same shape as mine? Does it recompute the transform if I plug in an external monitor? Run it and find out. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Two Resolutions, One Click — The macOS Coordinate Roundtrip. Liam, in for Bear. | OutroCTA |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; mechanism waits until B03 |
| Wrong guess surfaced *and falsified by a case* | B02 states the naive click-it-raw read, then breaks it: the raw (630, 420) coordinate misses the button on the real 2560×1600 screen |
| Inference flags | **Zero.** The mechanism and constraints are a direct read of `image.py`/`constants.py`; the worked numbers apply those constraints exactly — see SOURCES.md |
| One anchor, planted early, paid off late | B01 → B04 (Claude's click at 630, 420 on 1344×840 → real click 1200, 800 on 2560×1600) |
| Both failure directions | B04: the ratio-multiply holds whenever a resize actually happened; it flips when the screenshot already fits the budget — then sent = native and there's nothing to invert |
| No design judgment | B03 explains what the fix does, never whether `image.py` was a good design |

## Deliberately not claimed

- **No claim about non-macOS platforms, batched tool calls, or trajectory recording** —
  the source scaffold's own scope note, carried forward as this reel's exclusion.
- **The worked anchor numbers ((630, 420) → (1200, 800), sent 1344×840) are this
  reel's own**, derived directly from the documented constraints — not copied from
  the source scaffold's example, whose native/sent pair (2560×1600 → 1456×819) mixed
  two different aspect ratios and so could not have come from `target_image_size()`.
- **No accusation.** `image.py`'s design choices are described, never judged —
  that's Teardown's lane, not Plain's.

## Handoff prompt (BHTF, read aloud)

> "My MacBook's screenshot is 2560x1600, but Claude sees it resized to 1344x840 —
> write the inverse transform so a click Claude makes lands on my real screen."

This reel's own worked prompt (the source scaffold's original prompt reused the
same inconsistent 1456×819 figure as its cold open, so it is not carried forward
verbatim — see SOURCES.md).

---
**GATE P — signed:** unattended build, no human gate for hai-simple (VOICE-LOCK.md: the slate cut IS the review).
