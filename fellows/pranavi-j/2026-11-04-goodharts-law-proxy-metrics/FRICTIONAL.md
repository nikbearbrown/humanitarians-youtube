# Frictional log — Goodhart's Law: When the Proxy Stops Being the Target

*Written contemporaneously, as the build happens — not reconstructed after the fact.*

## 2026-11-03/04 — Start

Read both reference STEM reels in full as the structural template —
`2026-10-28-in-context-learning-limits/` (closest structural match: `BEAT-SHEET.md`,
`BUILD-LOG.md`, `FRICTIONAL.md`, `scenes.py` + `vertical/scenes.py`, `beat_sheet.json` +
`vertical/beat_sheet.json`, `FACTCHECK.md`, `SOURCES.md`, `SHOTLIST.md`, `PROMPTS.md`, `README.md`)
and `2026-10-21-calibration-why-confidence-isnt-accuracy/` (second reference, same format) — plus
the toolkit's `CLAUDE.md`, `HOW-TO.md`, `docs/FELLOWS-SUBMISSION.md`, `runtime/scripts/run.sh`, and
`runtime/scripts/compile.py` to confirm exactly how `./art run` / `./art final` / `./art vertical`
actually work end to end (slot precedence, GATE sequence, the `--out` render-target rule, and the
`deliverables/landscape|vertical/` convention — confirmed this is a manual-copy convention per
`FELLOWS-SUBMISSION.md`, not something `compile.py` writes on its own).

Topic: Goodhart's Law / proxy metrics. Devised the rubric: a 3-question test mirroring this
series' prior falsifiable rubrics (Calibration's "Bucket the Claims / Count the Cases / Spot the
Bluff", ICL's "Spot the Mapping / Shuffle the Set / Push Past the Window") — **"Name the Target /
Find the Lever / Watch the Coupling."** Worked example: a textbook-level call-center illustration
(average handle time gamed against an unwatched real target), fully generic, no real
company/vendor. Falsifiability case: designed per the brief's explicit requirement that this be a
case where the proxy does NOT diverge — chose the "counterbalancing check" condition the brief
names explicitly, and made it structurally identical to B04 (same panel, same invented numbers,
same gaming pressure), changing only whether the real target is framed as tracked ("ON THE
SCOREBOARD") — the single variable the rubric's own test (#2 Find the Lever / #3 Watch the
Coupling) actually names, per the house falsifiability-stress-test requirement confirmed in both
reference `BUILD-LOG.md`s.

Confirmed via `build_safety.py` that this project's `beat_sheet.json` metadata does NOT trip
`is_fellows()` (no `profile`/`skill`/`kind` == "fellows", no `voice_policy` ==
"persistent-fellow-selected") — matching the reference projects exactly, so no `metadata.approvals`
block is required for `compile.py --review`/`--final` to proceed; confirmed this by reading
`build_safety.py` directly rather than assuming it from the reference beat sheets' absence of an
`approvals` key.

Planned the build order per both references' documented lesson set: beat sheet → Kokoro audio
(measure real durations) → `scenes.py` tuned to those exact durations → render/QC landscape →
`./art vertical` scaffold → hand-author `vertical/scenes.py` → render/QC vertical → manual
final-master reconstruction for both aspects (the documented `./art final` GATE V workaround) →
GATE V direct verification on the true final candidates. Pre-applied several already-documented
fixes from the start rather than re-discovering them: `T()` safe-text helper for every on-screen
string, `metric_panel()`'s return contract indexed directly as `content[1]` (no extra index — the
exact bug both prior `BUILD-LOG.md`s document in `example_panel()`), front-loaded B02 pre-transition
waits (the exact empty-frame GATE V bug both priors hit), and 0.5-unit edge buffs on all
structure-beat framing rules (the exact edge-bleed GATE V bug the ICL reel's vertical B01 hit).

## 2026-11-04 — Beat sheet, audio

Authored `beat_sheet.json` (9 beats, same act structure as both references:
TITLE/EXEC-SUMMARY/HOOK/FRAMEWORK/WORKED-EXAMPLE/FALSIFIABILITY/SCAFFOLDED-TASK/TAKEAWAY/SIGN-OFF).
Ran `generate_audio_kokoro.py` (`af_bella`) for the 8 spoken beats; measured durations landed close
to, but not identical to, the draft `estimated_duration_s` guesses (e.g. B01 estimated 16s, measured
13.78s; B07 estimated 14s, measured 17.33s) — confirms again why the toolkit insists on audio-first
timing rather than hand-guessing. Built a real silent B00 mp3 by hand (`ffmpeg -f lavfi -i
anullsrc=r=48000:cl=stereo -t 4.104`), measured via `ffprobe` at 4.128s (not exactly the requested
4.104 — mp3 frame-boundary rounding — used the REAL measured 4.128s, not the requested value, in
`beat_sheet.json` and in `scenes.py`'s timing comments, per the audio-first rule: measure, don't
assume). Total measured runtime: 4.128+13.78+20.14+29.06+27.74+26.93+28.44+17.33+1.51 = 169.06s.

Wrote `scenes.py` with the new reel-specific helpers `stat_row()` / `metric_panel()` (a
"LABEL : VALUE" tracked-metric idiom, the core recurring visual mechanism for this reel), hand-
summed every beat's `self.play`/`self.wait` durations to match each measured `actual_duration_s`
exactly up front (B03's three mid-card holds had to be shortened from the ICL reel's 9.0s each to
7.0s each, since this reel's B03 narration — 29.06s — runs noticeably shorter than ICL's 35.21s).

## 2026-11-04 — Landscape render, GATE A/B/V clean on the first pass

Ran the low-res QC pass (`run.sh ... --height 480`). GATE A/B clean on all 9 beats first attempt —
no static pre-flight or pixel-true layout-audit failures. Confirmed via `ffprobe` that every
`manim/B0N.mp4` was already true native 3840x2160 despite the `--height 480` flag (the documented
`run.sh` behavior). The review slate's GATE V came back at exactly 18 BLOCKER / 0 MAJOR — the
documented burn-in false-positive pattern from both reference reels, not trusted at face value.

Built the TRUE final landscape master directly (`compile.py --height 2160 --out
deliverables/landscape`, no `--review`): it succeeded on the first attempt with no BuildError,
meaning `compile.py`'s own embedded GATE V step (no `--lenient`) found nothing blocking. Re-ran
`final_frame_check.py --lenient` directly against the written candidate as an independent
confirmation (never trusting the embedded step's silent success alone): **0 BLOCKER, 0 MAJOR** —
genuinely clean on the first true-candidate pass, no fix cycle needed for the initial build.

## 2026-11-04 — A real bug found only by extracting and looking at actual frames, not by any automated gate

Per the brief's instruction not to assume a clean automated pass means a clean deliverable,
extracted real frames from both finished masters at several beats' steady-state timestamps before
calling the build done. B02, B03, and B07 looked clean on direct inspection. **B04 and B05 did
NOT**: in the landscape B05 frame, the "ON THE SCOREBOARD" tag (placed `next_to(check_box, RIGHT,
buff=0.3)`) visibly spilled across the panel's own rounded-rectangle border — the panel's width is
sized from its own content, leaving no margin for a tag appended further to the right once that
content included the two-row metric panel. **GATE V's BLOCKER/MAJOR checks never caught this** —
it's a bbox-based heuristic (edge-bleed vs. the canvas edge, underfill vs. the safe area), not an
overlap-aware check, so a tag overlapping a DIFFERENT on-screen element's border is invisible to
it. The identical construction in `vertical/scenes.py`'s B05 did NOT have this bug — that file
already placed the tag below the whole panel (learned from the ICL reel's documented text-on-text
bug at authoring time), so landscape and vertical had diverged in a way neither gate caught.

Fixed by moving landscape B05's `check_tag` to `next_to(panel_group, DOWN, buff=0.3)`, matching the
already-correct vertical construction. Cleared the stale `manim/B05.mp4` + its `media/videos/...`
cache (the documented stale-cache bug) before re-rendering. Re-ran GATE A/B (clean) and rebuilt the
true landscape master — this time `compile.py`'s embedded GATE V step genuinely REFUSED the write:
**0 BLOCKER, 2 MAJOR**, both `underfill` (48% of the safe area, min 55%) on `B05_50.png`/`B05_85.png`.
A real, newly-introduced regression: moving the tag below the panel made the whole beat's content
column narrower, and B05 (unlike B04) had never carried a top/bottom framing rule. Fixed with the
same genuine-content-mass idiom B04 already used (a top rule folded into the title-write play, a
bottom rule folded into the closing-write play, both at the same 0.5-unit edge buff computed from
`final_frame_check.py`'s own SAFE constants) — not a padding trick, and no change to the beat's
total timing.

Cleared the stale B05 cache a second time, re-rendered (GATE A/B clean, review slate back to the
expected 18/0 false-positive pattern), and rebuilt the true landscape master a second time:
`compile.py`'s embedded GATE V step succeeded. Independently re-ran `final_frame_check.py --lenient`
directly against the written candidate: **0 BLOCKER, 0 MAJOR**. Re-extracted real frames for both
B04 and B05 from the renamed deliverable and looked at them directly — both clean, the "ON THE
SCOREBOARD" tag now sits cleanly below the panel with no overlap, and the panel/rule composition
fills the frame comparably to B04. Landscape final: `deliverables/landscape/
GoodhartsLaw_SaiPranaviJ.mp4` — 3840x2160, 24fps, h264/aac, 169.25s, GATE V 0 BLOCKER/0 MAJOR.

Takeaway for this build: GATE V's bbox-based checks (edge-bleed, underfill, low-contrast) do NOT
catch element-on-element overlap that stays within the overall bounding box — that class of bug is
only caught by actually looking at an extracted frame, exactly as the brief warned. It is also easy
to fix one real bug (the overlap) and introduce a second real regression (underfill) in the same
edit, which is why every fix in this build was re-verified both by the automated gate AND by a
fresh extracted frame before being trusted.

## 2026-11-04 — Vertical build: real GATE A false positive, confirmed via the real portrait auditor

Ran `./art vertical` (`shorts.py --vertical`) against the finished landscape reel: confirmed it
copies the parent's 9 mp3s and beat-sheet metadata (with `aspect_ratio: "9:16"`, `kind: "vertical"`
correctly set in `vertical/beat_sheet.json`) and correctly refuses to auto-generate a portrait Manim
layout for any GENERATED/manim beat — exactly the documented contract, and exactly why
`vertical/scenes.py` was already hand-authored ahead of this step. Cross-checked every beat's
`run_time=`/`self.wait()` sum in `vertical/scenes.py` against `scenes.py` and each beat's
`actual_duration_s` via a small regex script before rendering anything — one real mismatch found
(vertical B05 came out 0.2s longer than landscape B05, from an extra 0.3+0.3 split-into-two-plays
for `Create(check_box)`+`FadeIn(check_tag)` that landscape combined into a single 0.4 play) — fixed
by rebalancing to 0.2+0.2, re-verified exact match (26.930s both files) before rendering.

First vertical QC pass (`run.sh vertical --height 480`) hit a **real GATE A false positive**: B04
failed static pre-flight with "1 explicit coord(s) outside the frame, e.g. (0.0,-4.3) in move_to."
Grepped `vertical/scenes.py` for any literal `move_to([...])` call and found none anywhere in the
file — confirmed this is the exact documented stub-vs-real-Manim divergence class of false positive
(the static checker's render-free stub doesn't correctly apply this file's portrait
`config.frame_height`/`frame_width` patch). Independently verified via the real pixel-true
`manim_layout_audit.py --portrait --class B04_HandleTimeDivergence` run directly against a real,
separately-rendered copy of the scene: **CLEAN, 0 errors**. Proceeded past GATE A for the vertical
render using the documented `ART_QC=0` escape hatch, with every one of the 9 beats independently
re-verified via the real portrait auditor afterward (not just trusted from the escape hatch) — all
9 beats came back CLEAN.

**Self-caused stale-cache bug, caught and fixed before it reached the deliverable:** the manual
diagnostic render of B04 (used to feed the real portrait auditor above) wrote into the SAME
`vertical/media/videos/scenes/` tree the real `run.sh` render also uses, at a different resolution
(540x960, a quick diagnostic pass). `run.sh`'s own `find media/videos -name "$S.mp4"` slot-filler
picked up that stale low-res file instead of the real 2160x3840 render for B04 — caught immediately
by the routine post-render `ffprobe` resolution check (every other beat read 2160x3840; B04 alone
read 540x960). Fixed by deleting the stale `960p24` cache directory and the stray `manim/B04.mp4`,
then re-slotting the correct `2160x3840` file from the surviving `3840p24` cache directory. Lesson
logged: any manual diagnostic render of a reel's own `scenes.py` should go through a scratch
directory, not the reel's own `media/videos/`, to avoid contaminating the next real render's slot
resolution.

Built the true 4K vertical master directly (`compile.py --height 3840 --out
deliverables/vertical`): succeeded on the first attempt, no BuildError, meaning `compile.py`'s own
embedded GATE V step found nothing blocking. Independently re-ran `final_frame_check.py --lenient`
directly against the written candidate: **0 BLOCKER, 0 MAJOR** — confirmed genuinely clean, not
assumed from the embedded step's silent success. ffprobe: 2160x3840, 24fps, h264/aac, 169.25s —
identical duration to the landscape master to the millisecond.

Vertical final: `deliverables/vertical/GoodhartsLaw_SaiPranaviJ.mp4` — 2160x3840, 24fps, h264/aac,
169.25s, GATE V 0 BLOCKER/0 MAJOR. Both masters' B04/B05 frames re-extracted and inspected directly
(not just gate-checked) before considering the build done — both aspects clean, no overlap, no
underfill, legible mechanism in both B04 (DIVERGED) and B05 (CAUGHT — STAYS HONEST).
