# BUILD LOG — hai-simple/behind-the-model--constitutional-ai-self-critique

Redo of `anthropics/youtube/behind-the-model/constitutional-ai-self-critique`
("Teaching an AI to Grade Its Own Homework", Teardown-register, `register:
"Teardown"`, `channel: "NikBearBrown"`, cold open a `ClaudeComposerAsk` direct-address
ask beat, four fully-written body beats, a handoff beat, `ClaudeTitleOutro`) as
`hai-simple` (Plain register, Humanitarians AI skin). Source folder untouched. Built
from scratch — the target reel dir contained only SUBJECT.json at the start of this
invocation.

## Source was fully written (unlike some redo sources)

Unlike a placeholder scaffold, the source `beat_sheet.json` had real, complete
narration in every body beat: B01 (three problems with human harmlessness labeling —
expensive, inconsistent, doesn't generalize), B02 (the CAI loop: sixteen principles,
red-team prompt, critique, revise), B03 (the four-step mechanism: elicit, critique,
revise, RLAIF), B04 (the result: matched RLHF on harmlessness, beat it on helpfulness,
auditable refusals). This redo kept every one of those facts unchanged and did the
compression work hai-simple's spine requires: turning a Teardown four-beat body into a
Plain six-beat body carrying stakes → wrong guess → break it (anchor planted) →
mechanism → mechanism/result → both directions + one flag (anchor payoff).

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. No verdict/judgment beat; the source's own framing
  ("what the paper treats as solved that practitioners still argue about," from the
  source B00's Teardown cold-open command) became this reel's required
  BOTH-DIRECTIONS + ONE-FLAG beat instead of a Teardown-style verdict.
- **Cold open:** source's `ClaudeComposerAsk` direct-address ask → `BrutalistHesitantWriter`.
  Writer types "Grading its own homework — isn't that cheating?", hesitates on
  "cheating", corrects to "checkable" — the reel's actual wrong guess (self-grading
  sounds like cheating/circular), picked up and answered by B03 (checked against one
  written rule, not the model's opinion).
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of source's
  `ClaudeTitleOutro`/`@NikBearBrown`.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **New anchor (not in source):** a numbered rubric card ("THE CONSTITUTION," 1–16,
  one principle highlighted — "choose the response least likely to help someone cause
  harm") planted at B03, returned identically at B06. The source had no single running
  visual; this reel introduces one to satisfy ANCHOR LAW while keeping every underlying
  fact (the four-step loop, the sixteen-principle list, the result) unchanged.
- **New both-directions/one-flag beat (B06, not in source):** required by hai-simple's
  BOTH-DIRECTIONS LAW and ONE-FLAG LAW, absent from the source's four-beat Teardown
  body. Direction A doubles as the one inference flag (matching human labels on
  harmlessness doesn't prove the critique step is unbiased, since the same model both
  answers and grades — flagged, not resolved). Direction B (beating helpfulness doesn't
  prove more-correct judgment, only fewer refusals) is drawn directly from the source
  Teardown cold-open's own framing of what remains argued about.

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this build was AI-VIDEO, pantry, or a human-drop slot (the
source's B00 was already `ClaudeComposerAsk`/REMOTION, not a puppet). Every beat in
this reel is REMOTION (B00, BCRY, BHTF, BOUT) or bespoke GRAPHIC/Manim (B01–B06), built
fresh in the humanitarians palette (`#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`).

## Real defects found and fixed during Gate V / Gate T (not just re-run)

1. **B04's "AI feedback, not human" caption rendered with a space-collapse glitch**
   ("Alfeedback, not human") on first Manim render, caught via mid-beat frame grab.
   Root-caused by rewording rather than guessing at a font/weight tweak: changed the
   caption to "feedback from the AI" (moves "AI" off the leading position); re-rendered
   and reverified via frame grab — reads correctly.
2. **B06's "answers AND grades" / "flagged, not resolved" captions had a mid-word
   space-insertion glitch** ("an swers AND g rad es") at font_size 14–15, AND the two
   labels sat close enough to visually collide (both near the same y-band at
   overlapping x-ranges) — caught via mid-beat frame grab. Root-caused to undersized
   text plus a `next_to()` on a multi-element group anchoring at an unpredictable
   vertical center; fixed by bumping both captions to font_size 20 with explicit
   two-line wrapping and repositioning each icon+label as an independent column with
   its own fixed coordinates. Re-rendered and reverified via frame grab — both read
   cleanly with no collision.
3. **GATE T (pixel type-check) FAILed three times across the fix cycle**, each a real,
   verified defect rather than a false-positive to exempt:
   - **B01**: a "DOESN'T GENERALIZE" label at font_size 17 (< 20px floor), and a
     `row.animate.set_opacity(0.4)` transition that dropped a caption to 2.75:1 local
     contrast against cream — both real. Fixed by bumping the label to font_size 20 and
     removing the opacity-dip transition entirely (the dim-then-reveal beat was
     decoration, not signal).
   - **B06 (round 1)**: min text-run 9px < 20px floor — the anchor rubric card's
     decorative placeholder dashes and "… 4–16 …" dots, shown at `scale=0.62`, fell
     below the floor. Fixed at the root by replacing the dash/dot placeholders with
     plain graphical bars/dots (`Rectangle`/`Dot`, not `Text`) so decoration can never
     trip a text-size check again, and by raising the rubric card's real text (numbers,
     principle line) to font sizes that clear the floor even when the card is shown
     small.
   - **B06 (round 2)**: after the font bump, the rubric card's number column ("1.", "2."
     …) overflowed past the card's left border — `lines.move_to(ORIGIN)` centered the
     now-wider text block without accounting for the fixed card width. Fixed by
     anchoring the lines block to the card's left edge with a fixed inset
     (`lines.align_to(card, LEFT).shift(RIGHT * 0.45)`) instead of centering blindly.
   - **B06 (round 3)**: the final caption below the anchor card overflowed the
     title-safe box at the bottom of frame — the card and its caption were positioned
     too low once the card's overall footprint grew. Fixed by moving the top-row icons
     up (freeing vertical room) and raising the card + final caption into the safe
     zone; reverified via frame grab that nothing collides with the top-row labels.
   Each fix was verified by direct frame pull before moving on, not assumed from the
   type-checker's text description alone. GATE T: PASS on the final run (0 FAILs across
   min-size, overflow, contrast, contrast-local, bbox-overlap, card-clip, kerning).

## Gates

- **TIMING LAW (B00):** narration 32 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **10.86s** (≥9s floor, ≥8s render floor). Correction
  ("cheating" → "checkable") verified fully typed and settled by end-of-clip via frame
  grab.
- **GATE AUDIO:** PASS, mean_volume **-24.0 dB** (well above the -40 dB floor), max_volume
  -2.9 dB.
- **Gate V (frame QC):** every GRAPHIC beat (B01–B06) checked at mid-beat and
  near-end timestamps across three fix cycles; three real defects found and fixed at
  the root (detailed above). Full-cut 4-second-spaced frame sweep (36 frames) plus
  targeted checks of all four Remotion beats (B00, BCRY, BHTF, BOUT) post-compile — all
  legible, safe inset, no text overlap, Humanitarians AI skin correct throughout
  (composer card, subscribe chip, outro title all read cleanly). The B03→B06 anchor
  (the rubric card, same highlighted principle) verified visually identical between
  both appearances.
- **GATE T (pixel type-check):** FAIL (2 beats) → FAIL (1 beat) → FAIL (1 beat,
  different check) → PASS, per the defect log above.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py` output
  (10/10 beats, no violations).
- **Motion histogram:** WARNING, graphic 6/10 (60%, over the ~40% pantry cap).
  Non-blocking and structural for this skill: B00 (writer), BCRY, BHTF, BOUT are
  REMOTION by the hai-simple spine itself, and at only 6 body beats this 10-beat reel
  necessarily runs higher than 40% on the graphic side. Same disposition as prior
  hai-simple precedents (e.g. `behind-the-model--claude-constitution-honesty-standard`).

## Output

`behind-the-model--constitutional-ai-self-critique.mp4` — 145.7s, 3840×2160, 10/10
beats real (no slate), audible narration throughout (mean -24.0 dB). This is the review
cut (COMPLETION LAW satisfied: mp4 mtime 13:15:24 newer than beat_sheet.json mtime
12:58:09, mean_volume verified via ffprobe/ffmpeg volumedetect independently of
compile's own GATE AUDIO report). `compile.py` forces a 4K master by default ("4K
LAW"), so no separate low-res pass exists for this cut. beat_sheet.json has not been
touched since this final compile.

## Delivery

Master born natively 3840×2160 via `compile.py`'s 4K LAW, copied directly to `-4k.mp4`
(no separate 4K re-render needed). Delivered via `deliver.py --push`: staged
`DELIVERY/behind-the-model--constitutional-ai-self-critique/` (4K mp4 + description)
for the Drive sync, and committed the text artifacts (README.md, beat_sheet.json,
SCRIPT.md, SUBJECT.json, BUILD-LOG.md, CARRY-OUT.md, QUESTION.md — no mp3/mp4) to
`humanitarians-youtube/claude-bear/behind-the-model--constitutional-ai-self-critique/`,
pushed clean (commit `cb583508`). Playlist: **Behind the Model** (direct family-prefix
match in `playlists.json`).
