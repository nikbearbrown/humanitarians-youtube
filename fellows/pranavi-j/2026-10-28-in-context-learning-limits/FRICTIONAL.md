# Frictional log — In-Context Learning: What the Prompt Can (and Can't) Teach

*Written contemporaneously, as the build happens — not reconstructed after the fact.*

## 2026-10-28 — Start

Read the Calibration reference project
(`2026-10-21-calibration-why-confidence-isnt-accuracy/`) in full — `BEAT-SHEET.md`,
`FACTCHECK.md`, `SOURCES.md`, `PROMPTS.md`, `README.md`, `SHOTLIST.md`, `BUILD-LOG.md`, both
`scenes.py` files, `beat_sheet.json` — as the structural template, and skimmed the Filter reference
project's file list only to confirm shared toolkit mechanics (same file set, same gate sequence),
per the brief's instruction not to copy its content register.

Topic for this video: in-context learning (ICL) limits — what a model can and can't do when it's
only given examples/instructions in its prompt, no weight updates. Devised the rubric: a
3-question test mirroring this series' prior falsifiable rubrics (Calibration's "Bucket the
Claims / Count the Cases / Spot the Bluff", CoT's "Swap a Step / Hide a Hint / Strip It Out") —
**"Spot the Mapping / Shuffle the Set / Push Past the Window."** Worked example: a toy, invented
substitution rule taught purely via example pairs in a prompt (fully generic, no real
model/vendor). Falsifiability case: the same task reordered with one mapping flipped against the
model's likely pretrained prior — this is the beat most at risk of reading as a strawman, so kept
it structurally identical to B04 (same panel, same number of examples) and changed only the two
variables the rubric's test #2 actually names (order, one flipped mapping), per the house
falsifiability-stress-test requirement.

Confirmed via the toolkit's `CLAUDE.md`/`HOW-TO.md` and the Calibration reference's `BUILD-LOG.md`
that: (1) Manim always renders at the hardcoded native resolution from `run.sh`'s `-r` flag
regardless of `--height` (that only controls the compiled review cut), (2) `./art final`'s GATE V
step can crash with an unhelpful stderr and needs a manual `ffmpeg -f concat` reconstruction +
direct `final_frame_check.py --lenient` invocation as a documented workaround, (3) the vertical
companion needs a hand-authored `vertical/scenes.py` (the toolkit does not auto-generate portrait
Manim layouts), and (4) silent beats need a real silent mp3 (`ffmpeg anullsrc`) plus
`"audio_policy": "silence"` set explicitly, not just empty `narration_text`. Planned the build
order accordingly: beat sheet → Kokoro audio (measure real durations) → `scenes.py` tuned to those
durations → render/QC landscape → `./art vertical` scaffold → hand-author `vertical/scenes.py` →
render/QC vertical → manual final-master reconstruction for both aspects → GATE V direct
verification on the true final files.

## 2026-10-28 — Landscape low-res QC pass, a real timing bug caught by direct measurement

Generated Kokoro audio (`generate_audio_kokoro.py`, `af_bella`) for the 8 spoken beats; measured
durations (B01=14.64s ... B08=1.51s) landed close to, but not identical to, the draft
`estimated_duration_s` guesses — confirms again why the toolkit insists on audio-first timing.
Built a real silent B00 mp3 by hand (`ffmpeg -f lavfi -i anullsrc`, 4.104s measured).

Wrote `scenes.py` with new reel-specific helpers `pair_row()` / `example_panel()` (an
"INPUT -> OUTPUT" example-pair idiom, the running visual mechanism for this reel's toy
Caesar-shift rule) and hand-summed every beat's `self.play`/`self.wait` durations to match
`actual_duration_s` exactly.

Ran the fast low-resolution QC pass (`run.sh ... --height 480`) first. Result: GATE A/B clean on
all 9 beats first attempt. The review slate's GATE V pass, however, surfaced a REAL finding on
direct measurement, not the expected burn-in false positive: 17 BLOCKER (`edge-bleed`, the
expected pattern on 8 of 9 beats) but B02 showed 1 MAJOR (`empty-frame`) instead of its second
`edge-bleed` entry. Traced this to the beat's own content-to-overlay cross-fade: the first draft
held content on screen until t=10.0s, then FadeOut(0.5s)+FadeIn(0.6s) to the "Learning, or
locating?" overlay — GATE V's 50% steady-state sample (~10.63s into a 21.26s beat) landed ~0.13s
into the overlay's own FadeIn, while it was still nearly fully transparent. This is a real,
fixable pacing bug, not a tooling artifact: confirmed by hand-computing exactly where the 50%/85%
sample points fall relative to the transition's start/end times before touching the scene code.
Fixed by front-loading B02's early waits so the transition completes by t=7.1s (well clear of both
sample points), with the same total beat duration preserved (the saved 4.0s moved to the
post-transition hold). Deleted the stale `manim/B02.mp4` + its `media/videos/.../B02_*` partial
cache before re-rendering (per the documented stale-cache bug), re-ran, and the review slate came
back at the expected 18 BLOCKER / 0 MAJOR — the documented burn-in-strip false-positive pattern,
not a real defect, ready for direct verification against the true final candidate.

Confirmed via `ffprobe` that the Manim beats were already rendered at true 3840x2160 even during
the `--height 480` pass (the known `run.sh` behavior: `--height` only controls the compiled
review cut, Manim itself always renders at the hardcoded native `-r` resolution) — so no
redundant full-height Manim re-render was needed before building the true final landscape master.

## 2026-10-28 — Vertical scaffold, a real GATE A false positive, and 2 real margin warnings

Ran `./art vertical` (`shorts.py --vertical`) against the finished landscape reel: confirmed it
copies the parent's 9 mp3s and beat-sheet metadata into `vertical/` and correctly refuses to
auto-generate a portrait Manim layout for any GENERATED/manim beat (`[short] B0N GENERATED — no
cut; needs a portrait scene in short/scenes.py`) — exactly the documented contract, and exactly
why `vertical/scenes.py` was already hand-authored ahead of this step.

First vertical QC pass (`run.sh vertical --height 480`) hit a real **GATE A false positive**: B04
failed static pre-flight with "1 explicit coord(s) outside the frame, e.g. (0.0,-4.5) in move_to."
Grepped the actual `vertical/scenes.py` source for any literal `move_to([...])` call and found
none at all in the whole file — confirmed this is the exact documented stub-vs-real-Manim
divergence class of false positive (the static checker's render-free stub doesn't correctly apply
this file's portrait `config.frame_height`/`frame_width` patch, and reports a computed, not
literal, coordinate). Independently verified via the real pixel-true `manim_layout_audit.py
--portrait --class B04_ToyMappingWorkedExample`: **0 errors**, confirming the beat has no actual
out-of-frame content. Proceeded past GATE A for the vertical render using the documented
`ART_QC=0` escape hatch, with every beat independently re-verified via the real portrait auditor
(not just trusted from the escape hatch).

That same direct B04 audit also surfaced **2 real, small margin warnings** (not false positives):
the title "A made-up rule," measured 0.05 units past the +3.4 portrait safe top edge, and the
closing line "a pattern in reach was found." measured 0.1 units past the -3.4 safe bottom edge —
both from `to_edge()` buffs (0.55/0.5) too tight for this file's actual rendered text heights.
Fixed by bumping every title `to_edge(UP, buff=...)` to 0.7 and every closing
`to_edge(DOWN, buff=...)` to 0.68 across all of `vertical/scenes.py` (not just B04), matching the
sibling reel's own documented fix for the identical class of bug. Re-audited B04 directly:
**CLEAN, 0 errors, 0 warnings**. Independently re-audited the remaining 8 vertical beats the same
way before trusting the full vertical render.

## 2026-10-28 — A real indexing bug found by direct frame inspection (both aspects)

While independently re-auditing every vertical beat one at a time (not just trusting the GATE A/B
pass), B05 came back with a real `text-on-text` ERROR: the "FLIPPED" tag overlapping "GRI" by 77%.
Extracted a real rendered frame from the LANDSCAPE master at the same beat (`manim/B05.mp4`) and
found the same underlying bug visually: the flip-indicator box was a tiny dot around the SUN row's
output text ("VXQ"), and the "FLIPPED" tag floated off to the side, nowhere near the actual flipped
row (DOG -> GRI) — a real content-correctness bug, not just a layout-fit issue, present in BOTH
`scenes.py` and `vertical/scenes.py` identically. Root-caused to `example_panel()`'s return
contract: it returns `(VGroup(box, content), box, content)` where `content = VGroup(label, rows)`,
so `panel_content[1]` is already the full `rows` VGroup — but both B05 scenes wrote
`rows = panel_content[1][1]`, an extra index that actually selected the row's own 2nd element
(itself a sub-VGroup of 3 text mobjects), so `flipped_row = rows[flip_index]` (flip_index=2)
pulled out an unrelated text mobject from a different row entirely. The landscape GATE B audit had
not flagged this because the wide landscape layout happened to leave enough slack that nothing
visibly overlapped — a real bug that a pure layout-overlap checker can miss when there's enough
empty space to hide it in, caught only by looking at an actual extracted frame and checking it
against the beat's own intent (which row should be marked).

Fixed both files to `rows = panel_content[1]` (dropping the extra index). Landscape re-verified
CLEAN via a direct `manim_layout_audit.py` re-run and a second extracted frame showing the box and
tag now correctly marking the DOG -> GRI row. The vertical fix exposed a SECOND, genuine portrait-
only bug once the box was correctly positioned: placing "FLIPPED" directly below the (now correct)
flip_box, with the tight portrait row spacing (buff=0.16), caused it to land on the next row's text
("CAT -> FDW") instead — confirmed via `manim_layout_audit.py --portrait` (1 ERROR + 2 WARNING,
`->`/`FLIPPED` and `CAT`/`FDW` text-on-text). Fixed by moving the tag to sit below the WHOLE panel
instead of inline between rows, re-balancing the beat's `self.wait()` values by 0.1s to keep the
total duration exactly matched to `actual_duration_s` (27.17s). Re-audited: **CLEAN, 0 errors, 0
warnings.** Re-rendered both B05 beats from these fixes before rebuilding either aspect's true 4K
clips.

## 2026-10-28 — GATE V on the TRUE final candidates: a real landscape underfill, then a cluster of real vertical findings

Ran `final_frame_check.py --lenient` directly against the first true 4K landscape master (not the
review slate): **0 BLOCKER, 2 MAJOR** — B04's steady-state frame measured only 53% of the safe area
(min 55%) at both sample points, a genuine finding. Fixed with a real top/bottom framing rule
folded into B04's existing title-write/closing-write `self.play()` calls (no timing change). On
re-check the fix itself introduced a NEW real BLOCKER (not a tooling artifact): the rules' own
`buff` values (0.3/0.35 from the frame top/bottom edge) put them 0.1 units past the landscape safe
half-height of 3.6 — confirmed by computing the exact safe-area math from `final_frame_check.py`'s
own `SAFE` constants (1728x972 of a 1920x1080 reference, a flat 5% margin on every side, i.e. ±3.6
in Manim's 8-unit frame_height) rather than guessing. Fixed by widening the buff to 0.5 (edge at
±3.5, real 0.1-unit clearance). Re-verified: **0 BLOCKER, 0 MAJOR** on the true landscape candidate
(3840x2160, 173.375s).

The true vertical candidate's first GATE V pass came back far worse: **4 BLOCKER, 7 MAJOR** —
genuinely real findings (not the review-slate's burn-in-strip pattern, since there's no burn-in on
the true deliverable). Investigated every flagged beat by computing the EXACT sample timestamps
from `vertical/beat_sheet.json`'s own `render_duration_s` values (matching
`final_frame_check.py`'s own `beat_spans()`/`sample_beats()` logic exactly) and extracting real
frames at those times, rather than guessing from the contact-sheet thumbnail:

- **B01**: real `edge-bleed` top+bottom. Root cause: `frame = panel(width=4.0, height=7.4, ...)`
  is a VISIBLE bordered rectangle (`opacity=0.0` only zeroes the FILL, the gold stroke is still
  drawn — confirmed by the contact-sheet screenshots clearly showing every beat's bordered frame).
  Height 7.4 (half 3.7) genuinely exceeds the portrait safe half-height of 3.6. Fixed to
  height=7.0 (half 3.5). Also tightened B00's same-shaped frame (7.2 -> 7.0, since 7.2's half=3.6
  sat exactly ON the boundary with zero margin) pre-emptively.
- **B02**: `empty-frame` at 50%, `underfill` at 85% — the identical content-fade-out/overlay-
  fade-in transition-timing bug already found and fixed in the LANDSCAPE B02 earlier this build,
  never ported to `vertical/scenes.py`'s own, separately-authored B02. Applied the identical fix
  (front-loaded waits so the transition completes well before the 50%/85% sample points, total
  duration unchanged).
- **B03**: real `edge-bleed` left+right. Root cause: `test_card()`'s `head_t` (fit to `MAX_W-0.5`)
  plus the badge and the list_panel's own `+0.6` padding combined to a real half-width just over
  the portrait safe half-width of 2.025 (frame_width = 8*2160/3840 = 4.5, 5% margin = 0.225, safe
  half-width = 2.25-0.225). Fixed by tightening per-element width budgets (head_t to `MAX_W-0.9`,
  body_t to `MAX_W-0.4`) and the panel's own padding (+0.6 -> +0.3).
- **B06, B07, B08**: real `underfill` (53%, 53%, and a severe 42% respectively). B06 fixed the
  same way as landscape B04 (real top/bottom framing rules folded into existing plays, no timing
  change). B07 and B08's frames were SIZED FROM THEIR OWN SHORT TEXT CONTENT, which is why they
  underfilled a portrait canvas no matter how the text was arranged — fixed by sizing both frames
  from the portrait safe bounds themselves (fixed 4.0 x 7.0, matching B00/B01's own confirmed-safe
  dimensions) instead of the text's own size.

Re-verified every changed beat's exact timing sum (regexing each scene's `run_time=`/
`self.wait()` values) against its `actual_duration_s` before re-rendering — all 9 beats in both
files still match exactly, despite every fix above.

## 2026-10-28 — One more real vertical underfill, found on the SECOND true-candidate GATE V pass

Re-ran `final_frame_check.py --lenient` against the rebuilt true vertical candidate (ffprobe:
2160x3840, 173.375s — matching the landscape master's duration exactly): **0 BLOCKER, 2 MAJOR**,
both on B02 (`underfill`, 48% of the safe area, min 55%) — the content-fade/overlay-fade timing
fix had resolved B02's earlier empty-frame/underfill findings, but the overlay card itself (the
"Learning, or locating?" half of the beat) was simply too small for a portrait canvas. Rendered
B02 in isolation and extracted real frames at its own internal 50%/85% sample points (not the
absolute video timestamp — a beat rendered standalone has its own t=0) to confirm visually before
re-running the full pipeline: the qmark/text/rules genuinely only occupied the vertical-center
third of the frame. Fixed with real added size (qmark 120pt -> 160pt, overlay text 36pt -> 40pt,
inter-element buff 0.7 -> 0.9, rules widened 1.6 -> 1.9 units each side) — confirmed via a second
extracted frame that the overlay now spans roughly 70% of the frame height before trusting the
full true-4K rebuild. Verified the beat's total timing (21.26s) was unaffected by these
size-only changes before re-rendering.
