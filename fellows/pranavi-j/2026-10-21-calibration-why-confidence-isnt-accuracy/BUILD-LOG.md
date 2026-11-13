# BUILD-LOG — Calibration: Why Confidence Isn't Accuracy

## 2026-10-21 — Full build (both aspects)

**Gate P:** Beat sheet approved 2026-10-21. **FACTCHECK:** resolved same day — the mechanism (model
calibration, a well-documented, generically-named property of predictive models), the worked
example (a generic "~90% confident" answer bucket that's actually right 60% of the time), and the
falsifiability case (a different "~90% confident" bucket that's actually right ~90% of the time)
all confirmed fully qualitative, no real model/vendor named, no benchmark claimed, round numbers
chosen for teaching clarity only. Confirmed distinct from this fellow's two closest-adjacent prior
videos: `2026-09-22-hallucination-why-sounding-sure-isnt-being-right` (fabrication, not confidence
calibration) and `2026-10-15-chain-of-thought-why-the-reasoning-isnt-always-the-reason` (reasoning
traces, not confidence numbers).

**Audio:** Kokoro `af_bella`, all 8 spoken beats generated via `generate_audio_kokoro.py`. B00 a
real silent mp3 (`ffmpeg anullsrc`, 4.049s) with `audio_policy: "silence"` set explicitly per
`build_safety.py`'s silent-required-audio gate (the script correctly skips synthesizing B00 rather
than producing empty narration — the silent mp3 has to be created by hand). `actual_duration_s`
written back to `beat_sheet.json` from real ffprobe measurements: B00=4.049 B01=14.33 B02=15.94
B03=29.35 B04=25.63 B05=23.66 B06=21.17 B07=11.64 B08=1.51 — total 147.28s narration/silence (the
compiled masters run 147.5s after the pipeline's own 24fps frame-quantization of each beat's render
duration).

**`scenes.py` (landscape):** authored with the `T()` safe-text helper (creates `Text()` at
`font_size=48`, then scales geometrically to the intended size) used for every on-screen string —
avoids the confirmed Manim/Pango small-font-size rendering artifact. New helpers specific to this
reel: `answer_chip()` / `chip_row()` / `stat_bar()` / `confidence_card()` — a confidence-bucket chip
row and a stated-vs-actual bar pair, used across B02 (the hook's two same-confidence answer cards),
B04 (the overconfident worked example), and B05 (the well-calibrated falsifiability case). B03
shows all 3 tests (Bucket the Claims / Count the Cases / Spot the Bluff) fully, before any example,
per the Legibility Contract.

### Real bugs hit and fixed during this build

1. **Manim always renders at the hardcoded native resolution regardless of `run.sh`'s `--height`
   flag (discovered early, not a defect):** `run.sh` invokes `manim -r "3840,2160"` (or
   `"2160,3840"` for 9:16, read from `beat_sheet.json`'s `aspect_ratio`) unconditionally; the
   `--height` flag only controls the compiled *review* cut's resolution. An initial "fast QC pass"
   at `--height 480` had therefore already produced true-4K Manim renders and true GATE A/B results
   — the later full `--height 2160` run re-rendered the same 9 beats at the same resolution
   (redundant compute, not a correctness issue).
2. **`./art final` crash with an empty, uninformative stderr (both aspects, matches the pattern
   this fellow's sibling reels already root-caused):** `compile.py`'s own error wrapper printed
   "[art] command failed: ... final_frame_check.py ..." with nothing after it on both aspects —
   the wrapper only surfaces `stderr`, while `final_frame_check.py`'s real diagnostics print to
   `stdout`, and the temp candidate directory is deleted by its own `tempfile.TemporaryDirectory`
   context manager before it can be inspected. Worked around by manually reconstructing the true
   final master (`ffmpeg -f concat -safe 0 -i clips/concat.txt -i clips/_work/master.wav -map 0:v
   -map 1:a -c:v libx264 -preset fast -crf 16 -pix_fmt yuv420p -c:a aac -shortest <out>.mp4`) using
   the already-rendered `clips/*.mp4` (regenerated at true 4K by first letting `./art final` itself
   run far enough to rebuild them), then invoking `final_frame_check.py --lenient` directly against
   that manual candidate with full output visible.
3. **A first manual-reconstruction attempt used `compile.py`'s own CLI default `--height` (720),
   not 4K (landscape, caught before trusting the candidate):** calling `compile.py` directly
   (bypassing the `art` wrapper, which injects `--height 2160` itself when none is given) produced
   a 1280x720 candidate — caught via a plain `ffprobe` check before running GATE V against it, not
   assumed correct from the command having "worked."
4. **GATE V canvas-fill MAJORs on B02 and B05, invisible on the review slate (landscape, true-
   candidate-only findings):** the review slate's own GATE V pass showed 0 MAJOR, but the true
   final candidate measured B02's setup phase at 41% of the safe area (min 55%, narrow side-by-side
   cards in a short vertical band) and B05's steady-state frame at 54% (just under). Fixed with
   genuine added content mass (bigger cards, wider buffs, a real framing rule) confirmed via direct
   `final_frame_check.py --lenient` re-measurement each round, not assumed clean.
5. **A real new bug introduced while fixing #4 (landscape B02's overlay, caught by direct
   measurement, not a false positive):** the first fix attempt enlarged the overlay's qmark (140→
   165pt) and buff (1.6→1.9) across 5 separately-arranged elements (2 text lines counted
   separately). Queried Manim's own `Text().height` directly afterward and found the total arranged
   height (~10.3 units) exceeded the 8-unit-tall frame entirely — the top/bottom accent rules were
   pushed completely outside the camera view, confirmed by extracting a real rendered frame and
   finding them genuinely absent (not just clipped-looking). Fixed by combining the 2 text lines
   into one sub-group (reducing the main arrange to 4 elements) and choosing qmark=150pt/buff=1.1
   from real queried heights (predicted total height 6.01 of 8, fits with margin) before
   re-rendering — confirmed correct on the first retry.
6. **GATE A static-check false positive on landscape B05 (confirmed non-blocking, matches the
   sibling reels' documented stub-vs-real-Manim divergence):** after the chained-`next_to()`
   geometry fix for #4, GATE A's render-free stub flagged an out-of-frame coordinate that does not
   exist anywhere in the scene source. Independently confirmed as a false positive via the real
   pixel-true `manim_layout_audit.py` (0 errors) before trusting the geometry, and used the
   documented `ART_QC=0` escape hatch to get a real render out for direct inspection.
7. **Portrait `vertical/scenes.py`, 9 edge-overshoot warnings across B02-B06 (both titles and
   closing lines) and a stat-bar width overflow (B04/B05):** `to_edge()` buffs of 0.4-0.6 put
   several titles/closings 0.05-0.2 units past the ±3.4 portrait safe half-height; `stat_bar()`'s
   width=2.5 row measured half-width 1.99 against the ±1.95 portrait safe half-width. Fixed by
   bumping every title/closing buff to 0.7 and narrowing `stat_bar()` to width=2.0 with smaller
   fonts/tighter internal buff (half-width ~1.62) — all confirmed via the real portrait auditor
   (`manim_layout_audit.py --portrait`), not assumed from the numbers alone.
8. **GATE V BLOCKER on vertical B07 — a genuine edge-bleed bug, not review-slate noise (true-
   candidate-only finding):** extracted a real frame and found the card's own bordered frame
   (content width 3.4 + 0.7 padding = 4.1) wider than the portrait safe width (3.9 total,
   ±1.95) by 0.1 units on each side — the longest line (fit to the file's MAX_W=3.4 budget exactly)
   pushed the frame itself past the safe margin. Fixed by shrinking the frame's own padding
   (0.7→0.25), confirmed by re-querying Manim's real widths before re-rendering, not the text size.
9. **GATE V MAJORs on vertical B02 and B08 (true-candidate-only findings):** B08's sign-off card
   measured 41-44% of the safe area (4 short lines at buff=0.5); B02's setup phase measured 49%
   (short, narrow card stack). Both fixed with genuine added content mass (bigger fonts/cards, wider
   buffs, a real framing rule for B02) — each fix's expected safe-area coverage computed by directly
   querying Manim's own `Text`/`RoundedRectangle`/`VGroup` dimensions via a standalone Python
   snippet (no render needed) before re-rendering, confirming both the area score and that no new
   overflow was introduced.
10. **Stale render cache (both aspects, every round that touched `scenes.py`):** `run.sh`/
    `compile.py` do not detect `scenes.py` source changes and will silently reuse old cached
    `manim/*.mp4`/`clips/*.mp4`. Deleted the affected beats' cached files (never the whole folder
    wholesale, to avoid unnecessary re-renders) before every re-render that followed a scene edit.

**Landscape final:** 3840x2160, 24fps, h264/aac, 147.5s. GATE V on the true clean master (manually
reconstructed per bug #2's workaround, verified via `final_frame_check.py --lenient` run directly
against it): **0 BLOCKER, 0 MAJOR**.

**Vertical (`vertical/scenes.py`):** genuine hand-authored portrait redesign for all 9 beats
(`config.frame_height`/`frame_width` patched for portrait per the documented manim-CLI-ordering
bug, rendered 2160x3840), same `T()`/`panel()`/`box_around()` helpers copied verbatim, plus
portrait-specific redesigns of this reel's own confidence-bucket helpers: `chip_grid()` (the
landscape `chip_row()`'s 10 chips wrapped into 2 rows of 5 instead of 1 long row, to fit the narrow
canvas), narrower `stat_bar()`/`confidence_card()`. B02's side-by-side confidence cards restacked
top/bottom; B04/B05's side-by-side bucket/bars restacked top/bottom where needed. Every element
chained via `next_to()` off the block above it (never a hand-picked absolute y-coordinate), per the
sibling reels' documented lesson that absolute coordinates don't survive a from-scratch portrait
redesign once real rendered heights combine. Every `self.play`/`self.wait` duration matches
`scenes.py` beat-for-beat (hand-verified per beat against each `actual_duration_s`), so the vertical
master's total runtime is identical to the landscape master's (147.5s both) — full-length, all 9
beats, no drops, no duration cap, no added endcard, per `./art vertical`'s contract.

**Vertical final:** 2160x3840, 24fps, h264/aac, 147.5s. GATE V on the true clean master (same
manual-reconstruction workaround as landscape, verified via `final_frame_check.py --lenient`):
**0 BLOCKER, 0 MAJOR**.

**Process note:** every render step in this build was run as a background command past the
harness's own foreground timeout (Manim's 4K renders routinely ran several minutes per full 9-beat
pass), and all were waited out to completion via their completion notifications before continuing
— none were treated as done until their actual log output or resulting files were inspected. Both
final masters were personally re-inspected via extracted real frames (not just the automated gate
reports) at every beat that had a geometry fix applied during this build (B02, B04, B05, B07, B08
in both aspects) as part of fixing each issue, plus a full contact-sheet review of all 9 beats in
both aspects as a final visual check — no text-rendering artifacts, no clipping, no low-contrast
text found on any inspected frame in the final masters.

**Deliverables confirmed, both renamed and verified (SHA-256 matched against the source render
before and after copy):**
- `deliverables/landscape/CalibrationConfidence_SaiPranaviJ.mp4` (+ `.verified.json`) — 3840x2160,
  24fps, 147.5s
- `deliverables/vertical/CalibrationConfidence_SaiPranaviJ.mp4` (+ `.verified.json`) — 2160x3840,
  24fps, 147.5s

GATE V re-run directly against both final deliverable files (via `final_frame_check.py --mp4
<path> --lenient`, run from inside each reel folder): **0 BLOCKER, 0 MAJOR on both.**

Publishing not authorized — `beat_sheet.json`'s `publish` gate is marked ready-for-review, not
approved. Nothing inside `brutalist/` was modified.
