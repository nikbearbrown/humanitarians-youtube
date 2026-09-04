# Bridging the Pixel Gap in Browser Automation — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a Teardown scaffold). Register: **Plain**.*
*Carry-out written first (CARRY-OUT.md). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (free Remotion, WRITER LAW — no puppet, no
Seedance). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer / stakes+wrong-guess | "Claude reports a click at 728, 364. You'd assume that's your screen's exact spot. It isn't — it's scaled. Why does a coordinate need scaling before it becomes a real click?" | Writer types "...my screen's exact spot — right?", corrects "exact" → "scaled" |
| B01 | 1 stakes / **4 anchor planted** | Here's why. Claude never sees your actual screen. It sees a resized copy — 16:9 screenshots get squeezed to exactly 1456 by 819 pixels before the model looks at them. Your real viewport, 1920 by 1080, is a different size entirely. Same button, two different coordinate spaces. | THE ANCHOR — two rectangles (1456×819 / 1920×1080), same button dot, different position in each |
| B02 | 2 wrong guess, **broken by a case** | The obvious guess: click at 728, 364 and be done — Claude already found the button. Try that on the real screen and you miss. The button never sat at 728, 364 in your 1920 by 1080 window; that was only its position in the smaller picture Claude saw. | Same anchor pair; raw (728,364) plotted unscaled onto the 1920×1080 rect — misses, struck |
| B03 | 3 mechanism (no flag — fully sourced) | The fix is the inverse of the resize ratio. Multiply by how much bigger your screen is: 1920 over 1456 for x, 1080 over 819 for y — both come out to about 1.32. Multiply Claude's coordinate by that, clamp it inside your screen's bounds, and you have the real click. | Formula card: `real_x = x × (viewport_w / 1456)`, `real_y = y × (viewport_h / 819)`, then clamp. Source: Claude Quickstarts (Anthropic) |
| B04 | **4 anchor payoff** / **5 both directions** | Apply that to Claude's number: 728 times 1920 over 1456 is 960. 364 by the same ratio is 480. Click there, and it lands exactly on the button. That math holds for the 16:9 screenshot Claude actually returns. Change the aspect ratio, and Claude resizes to a different fixed size — the ratio changes, but the same multiply-back idea still applies. | THE ANCHOR RETURNS — same rectangle pair, dot now lands on target; a third, non-16:9 rectangle beside it, struck, captioned "different lookup table" |
| **BCRY** | **6 carry-out** | A Claude coordinate isn't wrong — it's just measured on a smaller picture. Multiply back by the resize ratio, and the click lands exactly where you meant. | The sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me: "My model clicks at 700, 410 on a 1456 by 819 screenshot, but my real screen is 1920 by 1080 — write the scaling so the click lands exactly." Paste that into Claude. Does it clamp to the screen's edges? Does it handle a screen that isn't 16:9? Run it and find out. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | Bridging the Pixel Gap in Browser Automation. Liam, in for Bear. | OutroCTA |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; mechanism waits until B03 |
| Wrong guess surfaced *and falsified by a case* | B02 states the naive click-it-raw read, then breaks it: the raw (728,364) coordinate misses the button on the real 1920×1080 screen |
| Inference flags | **Zero.** Every claim (the 1456×819 resize target, the formula, the clamp) is a direct read of `coordinate_scaling.py` — see SOURCES.md. Per ONE-FLAG LAW, a fully-sourced explanation carries no flag |
| One anchor, planted early, paid off late | B01 → B04 (Claude's click at 728, 364, screen 1920×1080 → real click 960, 480) |
| Both failure directions | B04: the ratio-multiply holds for the 16:9 case Claude actually returns; it does NOT hold unmodified for a non-16:9 viewport, which needs a different documented size |
| No design judgment | B03 explains what the fix does, never whether `coordinate_scaling.py` was a good design |

## Deliberately not claimed

- **No claim about non-16:9 scaling mechanics.** The source code supports other
  aspect ratios via a `match_aspect_ratio` flag and a separate lookup table
  (`DOCUMENTED_SIZES`); this reel states that boundary exists (B04) without
  teaching that other table, which is a different mechanism.
- **The worked anchor numbers (728, 364) → (960, 480) are this reel's own**,
  chosen so the arithmetic is exact (1920/1456 = 1080/819 = 1.3186813...,
  728×that = 960.0 exactly, 364×that = 480.0 exactly) — not copied from the
  source scaffold's example, which carried a small rounding slip.
- **No accusation.** `coordinate_scaling.py`'s design choices are described,
  never judged — that's Teardown's lane, not Plain's.

## Handoff prompt (BHTF, read aloud)

> "My model clicks at (700, 410) on a 1456x819 screenshot but my screen is
> 1920x1080 — write the scaling and land the click exactly."

This is the source scaffold's own original worked prompt (kept verbatim as the
Your Turn ask, per redo law — the question and the underlying facts carry over
unchanged even though the anchor example inside the body was re-derived).

---
**GATE P — signed:** unattended build, no human gate for hai-simple (VOICE-LOCK.md: the slate cut IS the review).
