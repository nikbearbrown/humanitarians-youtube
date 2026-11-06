# BUILD-LOG — Goodhart's Law: When the Proxy Stops Being the Target

## 2026-11-04 — Landscape build

**Gate P:** Beat sheet approved 2026-11-04. **FACTCHECK:** resolved same day — the mechanism
(Goodhart's Law / Campbell's Law, generically stated), the worked example (a textbook-level
call-center average-handle-time scenario, invented before/after numbers), and the
falsifiability/counterbalance case (the identical scenario with a tracked counterbalancing check
added) all confirmed fully qualitative, no real company/vendor named, no benchmark claimed, with
divergence/counterbalance claims kept hedged and generic per the Goodhart's-Law/metrics-design
literature. Confirmed distinct from this fellow's six prior videos: hallucination, tokenization,
lost-in-the-middle, chain-of-thought faithfulness, calibration, and in-context learning limits.

**Audio:** Kokoro `af_bella`, all 8 spoken beats generated via `generate_audio_kokoro.py` in one
pass (no retries needed). B00 a real silent mp3 (`ffmpeg anullsrc`, requested 4.104s, measured via
ffprobe at 4.128s — used the real measured value, not the requested one) with `audio_policy:
"silence"` set explicitly per `build_safety.py`'s silent-required-audio gate. `actual_duration_s`
written back to `beat_sheet.json` from real ffprobe measurements: B00=4.128 B01=13.78 B02=20.14
B03=29.06 B04=27.74 B05=26.93 B06=28.44 B07=17.33 B08=1.51 — total 169.06s narration/silence.
Measured durations landed noticeably off the pre-audio `estimated_duration_s` guesses in both
directions (B01 estimated 16s -> measured 13.78s; B07 estimated 14s -> measured 17.33s) — expected,
per the toolkit's audio-first rule.

**`scenes.py` (landscape):** authored with the `T()` safe-text helper for every on-screen string.
New helpers specific to this reel: `stat_row()` / `metric_panel()` — a "LABEL : VALUE" tracked-
metric idiom (a bordered panel holding one or more stat rows), the core recurring visual mechanism
for this reel, reused across B02 (the hook), B04 (the worked example), and B05 (the
falsifiability/counterbalance case). B03 shows all 3 tests (Name the Target / Find the Lever /
Watch the Coupling) fully, before any example, per the Legibility Contract. Pre-applied several
fixes already documented in both reference STEM reels' BUILD-LOGs from the start, rather than
re-discovering them: `metric_panel()`'s return contract indexed directly (`content[1]`, no extra
index — the exact `example_panel()` bug the ICL reel's BUILD-LOG documents), B02's pre-transition
waits front-loaded so the content-fade/overlay-fade transition completes well clear of GATE V's
50%/85% sample points (the exact empty-frame bug both prior reels hit), and 0.5-unit edge buffs on
every structure-beat framing rule (computed from `final_frame_check.py`'s own SAFE constants — a
flat 5% margin on an 8-unit frame_height, safe half-height 3.6 — not guessed).

### Real findings during this build

1. **Manim rendered at true native 3840x2160 regardless of `run.sh`'s `--height 480` flag
   (confirmed directly via `ffprobe` on every `manim/B0N.mp4`, matching both sibling reels'
   documented finding):** the fast low-res QC pass therefore produced true-4K Manim renders and
   true GATE A/B results on the first attempt — no redundant full-height re-render of the Manim
   stage was needed before building the landscape master.
2. **GATE A/B clean on all 9 beats on the first render attempt** — no static pre-flight or
   pixel-true layout-audit failures this build, landscape or (see below) vertical for most beats.
   Credited to pre-applying the known classes of bugs (safe-text helper, direct panel indexing,
   edge buffs, front-loaded transition waits) from the start rather than discovering them via a
   failed gate.
3. **Expected review-slate false positive, matching both sibling reels' documented finding exactly
   (18 BLOCKER, 2 per beat x 9 beats, `edge-bleed`):** the review slate's GATE V (`run.sh`'s
   embedded check against the `-slate.mp4` review cut) showed exactly 18 BLOCKER / 0 MAJOR — caused
   by the review cut's own burn-in global timecode (drawn top-right, outside
   `final_frame_check.py`'s `BURN_IN_EXCLUDE` zone, which only covers the bottom-left strip) sitting
   on every single sampled frame, not a real defect in the scene content. Per the documented
   workaround, did NOT trust this 18/0 result and verified directly against the TRUE final
   candidate before accepting anything as clean.
4. **The TRUE final landscape candidate passed GATE V clean on the FIRST attempt — 0 BLOCKER, 0
   MAJOR, no fix cycle needed this time:** built via `compile.py --height 2160 --out
   deliverables/landscape` directly (true 4K, no `--review` flag, so no burn-in strip). Because
   `FACTCHECK.md`/`SHOTLIST.md`/`PROMPTS.md` all existed, `compile.py`'s own embedded GATE V step
   (no `--lenient`, any BLOCKER *or* MAJOR refuses the write) ran to completion and wrote the
   candidate without raising — so the manual `ffmpeg -f concat` reconstruction workaround
   documented in both sibling reels' BUILD-LOGs was not needed this build (that workaround exists
   for when the embedded step crashes or when paperwork is missing; neither applied here). Still
   re-ran `final_frame_check.py --lenient` directly against the written candidate file (never the
   `-slate.mp4`) as an independent, explicit confirmation rather than trusting the embedded step's
   silent success alone — confirmed **0 BLOCKER, 0 MAJOR**.

5. **A real content-correctness bug found ONLY by extracting and looking at an actual rendered
   frame, not by any automated gate — landscape B05's "ON THE SCOREBOARD" tag overlapped the
   panel's own border:** `check_tag.next_to(check_box, RIGHT, buff=0.3)` placed the tag far enough
   right that it spilled across the metric panel's own rounded-rectangle stroke, since the panel's
   width is sized from its own content with no margin reserved for an appended tag. GATE V's
   bbox-based BLOCKER/MAJOR checks (edge-bleed vs. canvas edge, underfill vs. safe area) never
   flagged this — they are not overlap-aware, so one element overlapping a DIFFERENT element's
   border is invisible to them. `vertical/scenes.py`'s B05 did not have this bug (it already placed
   the tag below the whole panel, learned from the ICL reel's documented text-on-text bug at
   authoring time) — landscape and vertical had silently diverged. Fixed landscape to match:
   `check_tag.next_to(panel_group, DOWN, buff=0.3)`. Cleared the stale `manim/B05.mp4` cache (the
   documented bug) before re-rendering.
6. **That same fix introduced a real, newly-discovered underfill regression, caught by
   `compile.py`'s embedded GATE V step genuinely refusing the write (not a burn-in false positive —
   there is no burn-in on the true candidate):** moving the tag below the panel made B05's content
   column narrower than B04's; the TRUE candidate measured **0 BLOCKER, 2 MAJOR** (`underfill`, 48%
   of the safe area, min 55%, both `B05_50.png`/`B05_85.png`). Fixed with the same genuine
   framing-rule idiom B04 already used — a top rule folded into the title-write play, a bottom rule
   folded into the closing-write play, both at a 0.5-unit edge buff computed from
   `final_frame_check.py`'s own SAFE constants (not guessed) — zero change to the beat's total
   timing. Re-rendered, re-verified GATE A/B clean, rebuilt the true master a second time:
   `compile.py`'s embedded GATE V step succeeded; independently re-ran `final_frame_check.py
   --lenient` directly against the written candidate as a second confirmation: **0 BLOCKER, 0
   MAJOR**. Re-extracted real frames for both B04 and B05 and inspected them directly before
   trusting the fix — both clean.

**Landscape final:** `deliverables/landscape/GoodhartsLaw_SaiPranaviJ.mp4` — 3840x2160, 24fps,
h264/aac, **169.25s** (ffprobe; the 0.19s difference from the 169.06s raw audio sum is
`compile.py`'s documented pad-never-truncate frame-rounding of each beat's `render_duration_s` to
the nearest whole frame at 24fps). GATE V on the true clean master (`final_frame_check.py
--lenient`, run directly against the deliverable, not a `-slate.mp4` review cut): **0 BLOCKER, 0
MAJOR.**

## 2026-11-04 — Vertical build

Scaffolded via `./art vertical` (`shorts.py --vertical`): confirmed it copies the parent's 9 mp3s
and beat-sheet metadata into `vertical/` (with `aspect_ratio: "9:16"` correctly set) and correctly
refuses to auto-generate a portrait Manim layout for any GENERATED/manim beat — exactly the
documented contract. `vertical/scenes.py` was already hand-authored ahead of this step, with every
beat's `self.play`/`self.wait` timing cross-checked by regex against `scenes.py` and each
`actual_duration_s` (one real 0.2s mismatch on B05 found and fixed before rendering — see
`FRICTIONAL.md`).

### Real findings during the vertical build

1. **A real GATE A false positive on B04, matching the documented stub-vs-real-Manim divergence
   class exactly:** the static pre-flight checker reported "1 explicit coord(s) outside the frame"
   for a `move_to` call that does not exist anywhere in `vertical/scenes.py` (confirmed by direct
   grep) — the render-free static stub doesn't correctly apply this file's portrait
   `frame_height`/`frame_width` patch. Independently verified via the real pixel-true
   `manim_layout_audit.py --portrait --class B04_HandleTimeDivergence`, run against a real rendered
   copy of the scene: **CLEAN, 0 errors**. Proceeded past GATE A using the documented `ART_QC=0`
   escape hatch, then independently re-audited all 9 beats with the real portrait auditor
   afterward (not just trusted from the escape hatch) — **all 9 beats CLEAN**.
2. **A self-caused stale-render-cache bug, caught by the routine resolution check before it reached
   any deliverable:** the manual diagnostic render used to feed the real auditor above wrote into
   the same `vertical/media/videos/scenes/` tree the real `run.sh` render also uses (at a different,
   lower resolution). `run.sh`'s `find media/videos -name "$S.mp4"` slot-filler picked up that stale
   540x960 file for B04 instead of the real 2160x3840 render. Caught immediately by the routine
   per-beat `ffprobe` resolution check (every other beat read 2160x3840; B04 alone read 540x960).
   Fixed by deleting the stale cache directory and the stray slot, then re-slotting the correct file
   from the surviving true-resolution cache directory. Re-confirmed all 9 slotted beats at
   2160x3840 before compiling.
3. **The TRUE vertical candidate's GATE V passed clean on the first attempt** — `compile.py
   --height 3840 --out deliverables/vertical` succeeded with no BuildError (its embedded GATE V step
   found nothing blocking). Independently re-ran `final_frame_check.py --lenient` directly against
   the written candidate as explicit confirmation: **0 BLOCKER, 0 MAJOR**.
4. Re-extracted real frames from the finished vertical master at B02/B03/B04/B05/B07's steady-state
   timestamps and inspected them directly (not just trusted the gate) — all clean; B04/B05 in
   particular (the beats where landscape needed two real fixes) were correct from the first vertical
   render, since `vertical/scenes.py` had already placed the "ON THE SCOREBOARD" tag below the panel
   from the start.

**Vertical (`vertical/scenes.py`):** genuine hand-authored portrait redesign for all 9 beats
(`config.frame_height`/`frame_width` patched for portrait per the documented manim-CLI-ordering
bug, rendered 2160x3840), same `T()`/`panel()`/`box_around()`/`stat_row()`/`metric_panel()` helpers
copied verbatim (narrower fonts/padding), scaffolded via `./art vertical`. Every
`self.play`/`self.wait` duration matches `scenes.py` beat-for-beat (hand-verified per beat against
each `actual_duration_s` via a regex cross-check script), so the vertical master's total runtime
matches the landscape master's exactly — full-length, all 9 beats, no drops, no duration cap, no
added endcard, per `./art vertical`'s contract.

**Vertical final:** `deliverables/vertical/GoodhartsLaw_SaiPranaviJ.mp4` — 2160x3840, 24fps,
h264/aac, **169.25s** — identical duration to the landscape master (both masters share the same
per-beat `actual_duration_s`/`render_duration_s` timeline). GATE V on the true clean master
(`final_frame_check.py --lenient`, run directly against the deliverable): **0 BLOCKER, 0 MAJOR.**

**Deliverables confirmed (both masters, both GATE V clean, both ffprobe-verified):**
- `deliverables/landscape/GoodhartsLaw_SaiPranaviJ.mp4` — 3840x2160, 24fps, h264/aac, 169.25s.
  GATE V: 0 BLOCKER, 0 MAJOR.
- `deliverables/vertical/GoodhartsLaw_SaiPranaviJ.mp4` — 2160x3840, 24fps, h264/aac, 169.25s.
  GATE V: 0 BLOCKER, 0 MAJOR.

Both masters' durations match exactly (169.25s each, to the millisecond as reported by `ffprobe`).

Publishing not authorized — `beat_sheet.json`'s `publish` gate is marked ready-for-review, not
approved. Nothing inside `brutalist/` was modified.
