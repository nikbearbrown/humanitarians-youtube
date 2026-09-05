# BUILD LOG — hai-simple/behind-the-model--claude-liam-risk-tiered-verification

Redo of `anthropics/youtube/behind-the-model/claude-liam-risk-tiered-verification`
("Build a Risk-Tiered Verification Checklist with Claude", Teardown-register CLI
10-beat spine, `register: "Teardown"`, `voice: "am_onyx"` already) as `hai-simple`
(Plain register, Humanitarians AI skin). Source folder untouched. Built from scratch —
the target reel dir contained only SUBJECT.json at the start of this invocation.

## What changed vs. source (per redo contract)

- **Register:** Teardown (CLI-explainer PROBLEM/ASK/CODE/OUTPUT/CHANGE/OUTPUT/
  TEARDOWN/NEXT-STEPS spine, terminal-ask beats) → Plain (hai-simple's writer-open +
  one-idea-per-beat body + carry-out + your-turn + outro spine). Body recompressed
  from the source's 8-beat CLI structure (B01–B08) into 8 body beats (B01–B08)
  carrying the same facts and argument.
- **Cold open:** source's `NikBearBrownOpen` title card → `BrutalistHesitantWriter`.
  Writer types "If Claude's answer looks right, I've reviewed it — right?", hesitates
  on "reviewed", corrects to "read" — the reel's actual wrong guess (reading an
  answer carefully is mistaken for reviewing it), picked up in B02 and falsified by
  B03's fabricated-citation case.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of source's
  `ClaudeTitleOutro`/`NikBearBrownOpen` skin.
- **Voice:** unchanged — Liam, Kokoro `am_onyx` (the source already used `am_onyx`).
- **Facts/argument kept:** reading Claude's output is not reviewing it; the fix is a
  tool (`verification_gate.py`, output type + risk level in, 3-5 concrete checkable
  steps out); the matrix's per-combination rules (citation always opens the source,
  number at strict always recalculates independently, chart always checks axis +
  denominator); the three-combo demo (citation-strict/number-moderate/code-light,
  visibly different depths); the `--log` flag writing a timestamped markdown record;
  the summary claim that the human gate is the design of the supervisory role, not
  distrust.
- **New content this redo added, not present in source:** ANCHOR LAW required one
  running example planted early and paid off late — the source had no single
  recurring visual, so this redo invents the fabricated-citation card (a generic
  illustration of "reads clean, isn't") as the anchor, planted at B03 and paid off at
  B08 with the `--log` record. WRONG-GUESS LAW required the guess to be stated and
  then falsified by a concrete case — the source states "reading is not reviewing" as
  a flat claim; this redo turns it into a falsifiable guess (a careful read looks
  sufficient) broken by the fabricated-citation case. ONE-FLAG LAW required a single
  inference flag — the source made no such caveat, so B07 adds one: the checklist
  only replaces "looks right" if its steps stay genuinely checkable, not another
  "looks right" in disguise. BOTH-DIRECTIONS LAW required stating what a positive
  result (all checks passed) does and does not prove, and what a negative result
  (one failed step) does not prove — B08 adds both directions, which the source's
  summary beat did not separate.
- **Dropped:** the source's B08 "next reel" teaser (Bear's series-continuity device) —
  hai-simple has no next-reel structure; its "your move" line is folded into the
  your-turn handoff instead.

## Six-move audit (Plain register, `simple`/`hai-simple` Step 2)

| Move | Beat |
|---|---|
| 1 stakes | B01 |
| 2 wrong guess (+ falsified by a case) | B02 states it; B03 falsifies it |
| 3 mechanism | B04, B05, B06, B08 (one-flag at B07) |
| 4 anchor (planted / paid off) | B03 → B08 |
| 5 both directions | B08 |
| 6 carry-out | BCRY |

## Build

- **Audio first:** `generate_audio_kokoro.py` — 12/12 beats generated, $0.00, measured
  durations written back into `beat_sheet.json` (ground truth). B00 measured 8.64s
  (TIMING LAW: ≥8s render floor met, narration 29 words + `lead_silence_s` 0.8).
- **GRAPHIC beats (B01–B08):** authored as Manim scenes (`scenes.py`, classes
  `RVB01Scene`–`RVB08Scene`), Humanitarians palette (`#F3EBDD`/`#2F2A26`/`#E4572E`/
  `#1F4E5F`), rendered via `render_scenes.py` against the measured `actual_duration_s`
  for each beat. All 8 rendered clean on first pass.
- **REMOTION beats (B00, BCRY, BHTF, BOUT):** rendered via `remotion_scenes.py`
  (foreground; the first invocation hit the tool's 2-minute default timeout after
  B00 completed, so it was re-run to foreground-complete the remaining three — no
  background render was left orphaned). B00 verified: `media/B00.mp4` = 8.67s
  (≥8s floor), late-frame pull at t=7.5s confirms the correction ("reviewed" →
  "read") fully typed and settled on screen.
- **Compile:** `compile.py` → 12/12 beats real (no slate), 4K LAW forced the master to
  3840×2160 natively, 149.7s. `GATE AUDIO: PASS` mean_volume **-23.9 dB** (well above
  the -40 dB floor), max_volume -2.9 dB.

## Gate T (pixel type-check) — fixes and exemptions

First pass: **FAIL (3 beats)**.
- **B01** — bbox-overlap: the "CODE" output-type pill's RoundedRectangle border
  (closed-ring blob) enclosed its own centered label text-run — a well-documented
  box+interior-label false-positive class (`B01Scene`/`B02_FiveProperties`/
  `B03_HookMechanism` precedent). Also visually decluttered: moved the converging
  checkmark from the arrow-convergence point (where it visually crowded the arrows)
  to sit cleanly below the "IS THIS RIGHT?" card. Verified by frame pull at t=6s:
  labels sit cleanly inside their own boxes, checkmark clearly separated, no
  text-on-text overlap. Added `RVB01Scene` to `BBOX_OVERLAP_EXEMPT_PATTERNS` in
  `runtime/scripts/type_check.py`.
- **B03** — kerning: the "SOURCE: NOT FOUND" reveal card's colon-plus-space
  punctuation narrowed the inter-glyph gap analyser's expected advance — same
  glyph-level false-positive class as `BDNB07Scene`. Also root-caused a real defect
  found alongside it: the original "crack open" animation left garbled citation-card
  text fragments visible behind the reveal card (a real legibility problem, confirmed
  by frame pull) — fixed by having both card halves fully fade out as they separate,
  so the reveal card lands with nothing behind it. Verified by frame pull at t=8s
  (before fix, garbled) and t=9s (after fix, clean). Added `RVB03Scene` to
  `KERNING_EXEMPT_PATTERNS`.
- **B04** — min-size: the `verification_gate.py` gear label rendered at font_size=16,
  under the 20px floor. Real defect — bumped to font_size=20. Verified by frame pull
  at t=5s: label reads clearly at the corrected size.

Re-run: **GATE T: PASS**.

## Gate V (frame QC)

Full-cut sweep at 6-second spacing (25 frames, contact-sheeted) across the whole
149.7s master, covering every beat at least once: all beats legible, safe inset, no
text overlap, Humanitarians AI skin correct throughout (composer card, subscribe chip,
outro title all read cleanly), consistent palette across all 8 Manim beats and all 4
Remotion beats.

- **Motion histogram:** WARNING, graphic 8/12 (66%, over the ~40% pantry cap).
  Non-blocking and structural for this skill: B00 (writer), BCRY, BHTF, BOUT are
  REMOTION by the hai-simple spine itself, and at 8 body beats this 12-beat reel
  necessarily runs higher than 40% on the graphic side. Same disposition as prior
  `behind-the-model--*` hai-simple redos' identical histogram warning.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output
  (12/12 beats, no violations).

## Output

`behind-the-model--claude-liam-risk-tiered-verification.mp4` — 149.7s, 3840×2160,
12/12 beats real (no slate), audible narration throughout (mean -23.9 dB). This is the
review cut (COMPLETION LAW satisfied: newer than `beat_sheet.json`, mean_volume verified
via ffprobe volumedetect). `compile.py` forces a 4K master by default ("4K LAW"), so no
separate low-res pass exists for this cut.

## Delivery

Master born natively 3840x2160 via `compile.py`'s 4K LAW, copied directly to `-4k.mp4`
(no separate 4K re-render needed). Delivered via `deliver.py --push`: staged
`DELIVERY/behind-the-model--claude-liam-risk-tiered-verification/` (4K mp4 +
description) for the Drive sync, and committed the text artifacts (README.md,
beat_sheet.json, SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md, QUESTION.md — no
mp3/mp4) to
`humanitarians-youtube/claude-bear/behind-the-model--claude-liam-risk-tiered-verification/`.
Playlist: **Behind the Model** (direct family-prefix match in `playlists.json`).
