# Frictional log — Calibration: Why Confidence Isn't Accuracy

*Written contemporaneously, as the build happens, per the process change committed to in
`research-plan.md` for this period (no reconstruction-after-the-fact this time).*

## 2026-10-21 — Start

Studied the two most recent STEM-explainer folders in this series
(`2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason`,
`2026-10-06-lost-in-the-middle-why-more-context-isnt-better`) end to end — `BEAT-SHEET.md`,
`FACTCHECK.md`, `beat_sheet.json`, `scenes.py` (both aspects), `BUILD-LOG.md`, `README.md` — before
writing anything for this project, per the house convention of framework-first teaching plus a
falsifiability stress-test beat.

Topic for this video: model calibration (does a model's stated/implied confidence track how often
it's actually right), explicitly distinct from this fellow's earlier hallucination video
(`2026-09-22-hallucination-why-sounding-sure-isnt-being-right`, which is about fabrication, not
confidence-to-accuracy correspondence) and from the chain-of-thought-faithfulness video just built.
Framework devised: a 3-question test — **Bucket the Claims / Count the Cases / Spot the Bluff** —
mirroring the testable, falsifiable shape of this series' prior rubrics (CoT's "Swap a Step / Hide
a Hint / Strip It Out", Lost-in-the-Middle's 3-question rubric).

Confirmed via `./art --list` and `docs/FELLOWS-SUBMISSION.md` that the toolkit's vertical pipeline
(`./art vertical`) auto-derives `vertical/beat_sheet.json` and copies narration mp3s from the parent
once the landscape beat sheet + audio exist — it does not auto-generate a portrait Manim scene for
"generated"/manim beats (it logs `native portrait scene` as a blocked item per beat and expects a
hand-authored `vertical/scenes.py`, matching exactly what the two reference `BUILD-LOG.md`s
describe). Planned the build order accordingly: beat sheet → Kokoro audio (measure real durations)
→ `scenes.py` tuned to those durations → `./art vertical` to scaffold `vertical/` → hand-author
`vertical/scenes.py` → render/compile/verify both aspects.

## 2026-10-21 — Audio generation and first low-res QC pass

Generated Kokoro audio (`generate_audio_kokoro.py`, `af_bella`) for all 8 spoken beats; measured
durations (B01=14.33s ... B08=1.51s) landed close to, but not identical to, the draft
`estimated_duration_s` guesses in the beat sheet — confirms why the toolkit insists on audio-first
timing rather than guessing. B00 is silent by design; `generate_audio_kokoro.py` correctly skips
it ("SKIPPED — source audio / intentional silence") rather than synthesizing empty narration, so a
real silent mp3 had to be created by hand via `ffmpeg -f lavfi -i anullsrc` (4.049s measured),
matching the known toolkit requirement that a silent title-card beat needs a real silent audio
file plus `"audio_policy": "silence"` in the beat sheet, not just an empty `narration_text`.

Wrote `scenes.py` with every beat's `self.play`/`self.wait` durations hand-summed to match
`actual_duration_s` exactly (verified beat-by-beat by hand: e.g. B04's plays 4.3s + waits 6.1s +
final wait 15.23s = 25.63s measured). New reel-specific helpers: `answer_chip()` / `chip_row()` /
`stat_bar()` / `confidence_card()` — a confidence-bucket chip row and a stated-vs-actual bar pair,
reused across B02/B04/B05, the same two-group-return pattern (track + fill kept separate, not one
flattened VGroup) as the sibling reels' `build_chain()`, specifically to avoid that exact
flattened-VGroup indexing bug documented in the chain-of-thought reel's BUILD-LOG before it could
recur here.

Ran a fast low-resolution QC pass first (`run.sh ... --height 480`, not the full 4K height) to
catch any GATE A (render-free static check) or GATE B (post-render pixel-true layout audit) issues
quickly before committing to a slow 4K render. Result: **all 9 beats CLEAN on both GATE A and
GATE B**, first attempt — no stale-coordinate or shape-distinctness false positives hit this time,
likely because the confidence-bucket helpers (chips, bars) use real distinct shapes per beat by
construction (unlike the sibling reel's B03, which needed a retrofit badge to pass GATE A's
shape-distinctness check — built the badge in from the start here instead). The review slate's own
GATE V pass showed the expected, already-documented false positive: 18 BLOCKER (`edge-bleed`,
exactly 2 per beat x 9 beats) from the review cut's burn-in timecode/label strip sitting outside
`final_frame_check.py`'s `BURN_IN_EXCLUDE` zone — not a real defect, matching the sibling reels'
documented finding exactly. MAJOR=0 at this resolution, though the sibling reels' BUILD-LOGs
record that GATE V's canvas-fill (area) check only reliably catches real underfill on the TRUE
final candidate, not the review slate or a downscaled QC pass — so this is encouraging but not
proof of a clean final master; will re-verify directly against the true final candidate before
calling this done, per that same documented lesson.

Wrote `vertical/scenes.py` by hand (all 9 beats), reusing the exact same `self.play`/`self.wait`
timings as the landscape file so total vertical runtime matches landscape exactly. Portrait-
specific redesigns: B02's side-by-side confidence cards restacked top/bottom; B04/B05's 10-chip
single row restacked into a 2x5 grid (`chip_grid()`) since a single row of 10 chips doesn't fit the
narrow MAX_W budget; all bars narrowed from width 5.4 to 2.5. Every element chained via `next_to()`
off the block above it (never a hand-picked absolute y-coordinate), per the sibling reels'
documented lesson that absolute coordinates don't survive a from-scratch portrait redesign once
real rendered heights combine.

## 2026-10-21 — Landscape full 4K render, GATE A/B clean, GATE V underfill + a real overflow bug

Ran the full 9-beat landscape pipeline at true 4K (`run.sh ... --height 2160`). Learned partway
through that Manim itself always renders at the hardcoded native resolution
(`manim -r "3840,2160"`/`"2160,3840"` per `aspect_ratio` in `beat_sheet.json`) regardless of
`run.sh`'s own `--height` flag — that flag only controls the compiled *review* cut's output height,
not the actual Manim render. So the earlier "fast QC pass" at `--height 480` had already rendered
true 4K GATE A/B results; this full run re-rendered the same 9 beats at the same resolution
(redundant compute, not a mistake in the earlier result). All 9 beats CLEAN on GATE A (render-free
static check) and GATE B (post-render pixel-true layout audit), both passes.

`./art final . --out deliverables/landscape` hit the exact documented opaque crash (REFUSED, empty
diagnostic, no stderr) — confirmed this is the same pre-existing `compile.py`/`final_frame_check.py`
diagnostics-visibility bug this fellow's sibling reels already root-caused (temp candidate dir
deleted before inspection, real diagnostics on stdout not surfaced by the wrapper). Worked around by
manually reconstructing the true final master (`ffmpeg -f concat ... clips/concat.txt +
clips/_work/master.wav`) and running `final_frame_check.py --lenient` directly against it. First
manual attempt used `compile.py`'s own CLI default `--height` (720) by mistake, producing a 1280x720
candidate — caught via `ffprobe` before trusting it, re-ran `./art final` properly (which injects
`--height 2160` itself) to regenerate true-4K `clips/*.mp4`, then redid the manual reconstruction
correctly.

GATE V on the true candidate (not the review slate, which showed 0 MAJOR) found real underfill:
B02 at 41-42% of the safe area (min 55%) and B05 at 54% (just under). Root-caused directly rather
than guessing: queried Manim's own `Text(...).height`/`.width` via a standalone Python snippet
(no video render needed) to compute exact bounding-box dimensions before touching the file a second
time. First fix attempt for B02 (bigger cards, enlarged qmark 140→165, enlarged buff 1.6→1.9)
introduced a **real new bug**, not a false positive: querying the actual heights afterward showed
the enlarged overlay group's total height (~10.3 units with 5 separately-arranged elements) exceeded
the 8-unit frame entirely, so the top/bottom accent rules were pushed completely outside the camera
view — confirmed by extracting a real rendered frame directly (`ffmpeg -ss ... -frames:v 1`) and
finding the rules genuinely absent, not just clipped-looking. Re-did the fix properly: combined the
two overlay text lines into one sub-group (so the main `arrange()` has 4 elements, not 5), queried
real heights for a qmark=150/buff=1.1 combination, confirmed by calculation the whole group's height
(6.01 units) and vertical extent (±3.0) fit safely inside the 6.8-unit safe height before re-rendering
— this is the same "measure, don't guess" discipline used for audio-locked timing, applied to layout
geometry too. Re-rendered B02 only (manim/clips cache deleted first), re-verified via the real
pixel-true `manim_layout_audit.py` (0 errors), recompiled, and GATE V on the true candidate came back
**0 BLOCKER, 0 MAJOR** on the full 147.5s landscape master. Also hit (and worked around via the
documented `ART_QC=0` escape hatch) a GATE A render-free-stub false positive on B05 flagging an
out-of-frame coordinate that doesn't exist in the scene source — independently confirmed via the
real pixel-true auditor (0 errors) before trusting the geometry, matching the sibling reels'
documented stub-vs-real-Manim divergence for chained `next_to()` layouts.

Landscape final: `deliverables/landscape/CalibrationConfidence_SaiPranaviJ.mp4`, 3840x2160, 24fps,
147.5s, SHA-256 verified identical between the render and the renamed deliverable, GATE V 0
BLOCKER / 0 MAJOR on the true final candidate (not the review slate).

## 2026-10-21 — Vertical full 4K render, two real geometry bugs caught via direct measurement

Ran `./art vertical .` to scaffold `vertical/beat_sheet.json` (auto-derived from the parent) and
copy all 9 narration mp3s byte-for-byte — confirmed it does NOT auto-generate portrait Manim scenes
for "generated" beats (logs each as a blocked "native portrait scene" item), matching what the
sibling reels' BUILD-LOGs describe; `vertical/scenes.py` had already been hand-authored earlier
this session with this expectation. Rendered all 9 portrait beats at true 4K
(`run.sh vertical --height 3840`, `manim -r "2160,3840"` hardcoded per the toolkit's own aspect-
based resolution logic). Used the documented `ART_QC=0` escape hatch up front for the whole
portrait pass (not just one beat this time) since GATE A's render-free stub is known to diverge
from real Manim on chained `next_to()` portrait layouts — independently verified every beat via the
real pixel-true `manim_layout_audit.py --portrait` instead (all 9 CLEAN on the first pass, 0 errors
across the board for B00/B01/B08; a handful of WARN-level edge overshoots on B02-B06's titles and
closing lines, all from `to_edge()` buffs of 0.4-0.6 that were a little too tight for the ±3.4 safe
half-height — fixed by bumping all of them to buff=0.7 in one pass, then re-verified 0 warnings).

Also caught a genuine stat-bar width overflow in the same pass: B04/B05's STATED/ACTUAL bar rows
(width=2.5) measured half-width 1.99 against the portrait ±1.95 safe half-width — queried Manim's
own `Text`/`Rectangle` widths directly (not guessed) to find a width=2.0/smaller-font/tighter-buff
combination that lands at half-width ~1.62, comfortably inside.

GATE V on the true vertical candidate (reconstructed the same manual way as the landscape master)
first came back with **2 real BLOCKER + 3 real MAJOR**, not review-slate noise this time:

- **B07 edge-bleed (BLOCKER, a genuine bug, not a false positive):** extracted a real frame and
  found the bold final line ("accuracy, across many cases.", fit to the file's MAX_W=3.4 budget)
  made the card's own bordered frame (content width + 0.7 padding = 4.1) wider than the portrait
  safe area (±1.95, i.e. 3.9 total) by 0.1 units — the card's gold border itself was bleeding past
  the safe margin, confirmed by querying Manim's real widths rather than eyeballing the frame.
  Fixed by shrinking the frame's own padding (0.7 → 0.25), not the text, since the text was already
  correctly sized.
- **B08 underfill (MAJOR, 41-44%):** the sign-off card's 4 stacked lines at buff=0.5 only reached
  ~44% of the safe area. Queried real heights for a bigger-font/wider-buff version before
  re-rendering and confirmed by calculation (~74% area, well inside the safe band both ways) rather
  than guessing a second time.
- **B02 underfill (MAJOR, 49%):** the portrait setup-phase composition (title + 2 stacked cards +
  tag) was both too short and too narrow. Enlarged the cards, widened the inter-block buffs, and
  added a real framing rule below the tag (mirroring the landscape fix for the same beat) — computed
  the resulting bounding box by hand (~66% area) before re-rendering, and confirmed its actual
  position stays ~1.3 units clear of the bottom safe edge (no new overflow risk introduced).

Re-rendered only the affected beats (B02, B07, B08) after each fix, re-verified each via the real
auditor (0 errors), recompiled, and GATE V on the true vertical candidate came back **0 BLOCKER, 0
MAJOR** — matching the landscape master, both full 147.5s, both true 4K.

The pattern across this whole build: every geometry fix after the first round was done by directly
querying Manim's own `Text()`/`Rectangle()`/`VGroup()` width/height properties via a standalone
Python snippet (no video render needed) and computing the expected safe-area coverage *before*
re-rendering, rather than enlarging something and hoping — this caught the B02 overlay overflow bug
(landscape) before it would have otherwise required a second full guess-and-check round.

Vertical final: `deliverables/vertical/CalibrationConfidence_SaiPranaviJ.mp4`, 2160x3840, 24fps,
147.5s (identical runtime to the landscape master, all 9 beats, no drops), SHA-256 verified,
GATE V 0 BLOCKER / 0 MAJOR on the true final candidate.

Publishing not authorized — `beat_sheet.json`'s `publish` gate stays ready-for-review, not
approved. Nothing inside `brutalist/` was modified.
