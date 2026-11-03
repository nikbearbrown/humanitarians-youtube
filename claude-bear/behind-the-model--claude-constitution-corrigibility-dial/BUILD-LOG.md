# BUILD LOG — hai-simple/behind-the-model--claude-constitution-corrigibility-dial

Redo of `anthropics/youtube/behind-the-model/claude-constitution-corrigibility-dial`
("The Dial Just Off Full Obedience", Teardown-register, 16 beats, ~330s) as
`hai-simple` (Plain register, Humanitarians AI skin). Source folder untouched. Built
from scratch — the target reel dir contained only SUBJECT.json at the start of this
invocation.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Body compressed from the source's five acts + worked
  example (16 beats total) to one idea per beat (10 beats: B00 writer + B01–B06 body +
  BCRY + BHTF + BOUT). The source's four-value ranking (safe > ethical > adherent >
  helpful, A11) is not restated as its own beat — Plain-register compression keeps the
  disposition-dial argument as the one idea; the ranking is a supporting detail, not the
  load-bearing point.
- **Cold open:** source's `ClaudeComposerAsk` direct-address ask → `BrutalistHesitantWriter`.
  Writer types "Shouldn't a good AI always trust its own judgment?", hesitates on
  "judgment", corrects to "willingness to be shut down" — the reel's actual wrong guess
  (good values = trust your own judgment), picked up and falsified by B03.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of source's
  `ClaudeTitleOutro`/`@NikBearBrown`.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** unchanged. The shutdown-order setup, the unverifiable-values break,
  the corrigibility-dial mechanism, the four-quadrant cost/benefit argument, the
  unconditional hardcoded limits, and the compromised-hierarchy both-directions clause
  all carried from the source, reworded for register.

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this compression was AI-VIDEO, pantry, or a human-drop slot.
The source's existing `CorrigibilityDial` / `CorrigibilityMatrix` / `CorrigibilityValueLadder`
Remotion components were found via GATE L (`./art scenes`) but deliberately NOT reused —
they render in fixed Claude-brand tokens (`#FAF9F5`/`#3D3929`/`#D97757`) with no palette
override, and hai-simple's channel-skin law calls for the humanitarians palette
throughout, not just at the outro. Built fresh Manim scenes instead
(`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`), matching the precedent set by prior
`hai-simple` redos (e.g. `books--claude-liam-enterprise-search`). Every beat in this
reel is REMOTION (B00, BCRY, BHTF, BOUT) or bespoke GRAPHIC/Manim (B01–B06).

## Two real defects found and fixed during Gate V (not just re-run)

1. **B01/B06 shared `_order_card()` helper — text overflowed the card border.** First
   render of B01 showed "SHUTDOWN ORDER" and the subtitle line both wider than the
   3.2-unit-wide card, spilling past the rounded-rectangle stroke on both sides
   (caught via `ffmpeg` frame grab at ~0.85× beat duration). Root cause: the card size
   was a fixed guess, not derived from the label it had to contain. Fixed by rebuilding
   `_order_card()` to size the card from the label's measured `get_width()`/`get_height()`
   plus fixed padding, and added a `scale` parameter so B06's smaller reuse of the same
   anchor object scales the whole group (card + text) together instead of drifting out
   of sync. Re-rendered both B01 and B06, reverified via frame grabs — text fully
   contained, no overlap.
2. **B06 bottom row — unrendered emoji glyph, text overlap, and an off-canvas arrow.**
   The lightning-bolt emoji (`⚡`) used for the "compromised order" flag rendered as a
   blank filled rectangle (the font has no glyph for it); the "credentials don't check
   out" label sat close enough to the (pre-fix, oversized) order card to visually
   collide with it; and the arrow to "MORE CAUTIOUS, NOT LESS" terminated on top of that
   text instead of stopping short of it, with the text's right edge crowding the frame's
   safe inset. Fixed by replacing the emoji with a drawn terracotta triangle + "!" (no
   font-glyph dependency), rebuilding the bottom row's horizontal layout with explicit
   x-coordinates budgeted against the 3840×2160 canvas's safe area, shrinking the reused
   order card to `scale=0.72`, and shortening the arrow to end with clearance before the
   response text. Re-rendered, reverified via frame grabs — no overlap, everything
   within the safe inset.

Both fixes were applied and reverified with frame grabs (`ffmpeg -ss <t> -frames:v 1`)
at both a mid-beat and near-end timestamp before recompiling, not assumed from a
duration match alone.

## Gates

- **TIMING LAW (B00):** narration 32 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **10.37s** (≥9s floor, ≥8s render floor). First remotion_scenes.py
  invocation timed out mid-render at the harness's 2-minute default and left a truncated
  `media/B00.mp4` (`moov atom not found`, confirmed via `ffprobe`); deleted and
  re-rendered with `--only B00` under a longer foreground timeout — clean file on the
  second attempt. Correction ("judgment" → "willingness to be shut down") verified
  fully typed and settled by end-of-clip via frame grab.
- **GATE AUDIO:** PASS, mean_volume **-23.9 dB** (well above the -40 dB floor), max_volume
  -3.0 dB.
- **Gate V (frame QC):** every GRAPHIC beat (B01–B06) checked at a mid-beat and a
  near-end timestamp before and after fixes; two real defects found (B01/B06 card
  overflow, B06 emoji/overlap/off-canvas) and fixed at the root, detailed above. B02–B05
  clean on first review. Full-cut 4-second-spaced frame sweep (37 frames) plus targeted
  checks of the three Remotion beats (BCRY, BHTF, BOUT) post-compile — all legible, safe
  inset, no overlap, Humanitarians AI skin correct throughout (composer card, subscribe
  chip, outro title all read cleanly).
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output
  (10/10 beats, no violations).
- **Motion histogram:** WARNING, graphic 6/10 (60%, over the ~40% pantry cap).
  Non-blocking and structural for this skill: B00 (writer), BCRY, BHTF, BOUT are
  REMOTION by the hai-simple spine itself, and at only 6 body beats this 10-beat reel
  necessarily runs higher than 40% on the graphic side. Same disposition as sibling
  redos' histogram warnings on the other side of the ratio.

## Output

`behind-the-model--claude-constitution-corrigibility-dial.mp4` — 146.8s, 3840×2160,
10/10 beats real (no slate), audible narration throughout (mean -23.9 dB). This is the
review cut (COMPLETION LAW satisfied: newer than `beat_sheet.json`, mean_volume
verified via ffprobe/compile GATE AUDIO). `compile.py` forces a 4K master by default
("4K LAW"), so no separate low-res pass exists for this cut.

## Remotion pipeline notes for future invocations

`runtime/scripts/remotion_scenes.py` and `runtime/scripts/compile.py` both regularly
run past the harness's 2-minute default Bash timeout on a 10-beat reel with a 4K
forced master; both must be invoked with an explicit longer timeout (used 600000ms)
and run in the FOREGROUND per the COMPLETION LAW — never backgrounded, since a
timed-out background render can leave a truncated, undetected-corrupt media file (as
happened here with the first B00 attempt) while the orchestrating process has already
moved on.
