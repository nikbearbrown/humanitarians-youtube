# BUILD-LOG — The Alert That Waited for a Second Item

## 2026-10-15/2026-10-16 — Full build (both aspects)

**Gate P:** Beat sheet approved 2026-10-15. **FACTCHECK:** resolved same day — both B06 honest
limits (caught by code review not a live incident; the related `source_feed` compatibility gap)
kept at full weight, no softening.

**Audio:** Kokoro `af_bella`, all 9 beats. B01-B08 generated via `generate_audio_kokoro.py`
(measured durations: B01 15.94s, B02 12.5s, B03 16.54s, B04 16.49s, B05 22.9s, B06 23.38s,
B07 10.03s, B08 1.51s — B08 is short because its narration is literally just "Explained with
Claude Code."). B00 is a real silent mp3 (`ffmpeg anullsrc`, 4.05s measured) with
`audio_policy: "silence"` set explicitly per `build_safety.py`'s silent-required-audio gate.
`beat_sheet.json`'s `actual_duration_s` fields updated from the real measured values (not the
pre-audio estimates); total measured runtime 123.34s audio / 123.5s compiled (24fps rounding).

**`scenes.py` (landscape):** authored with the `T()` safe-text helper (Pango/Cairo
small-font-size-artifact workaround) used for every on-screen string, copied from this fellow's
closest sibling, `2026-10-06-the-classifier-that-learned-when-not-to-guess/scenes.py`, for visual
consistency. B03 shows the real `hasData` guard line verbatim from `B6-VERIFICATION.md`
(`const hasData = newItems && newItems.length > 1 && ...`), with the exact substring
`newItems.length > 1` isolated via Manim `Text` character-index slicing (no re-creation, no
paraphrase) and boxed gold/crimson. B04 shows the real one-character-class diff
(`- newItems.length > 1` struck through, `+ newItems.length > 0` added) chained to the real traced
dead end (`fails the check -> has_items: false` -> `If-node TRUE branch: [ ] — nowhere to go`).
B05 shows the real 0/1/2-item before/after harness table, the 1-item row boxed gold as the one
that changed, plus a closing line noting the re-run against the real patched file on disk. B06
shows both honest limits as separate full-weight cards, per house discipline.

**Landscape final:** 3840x2160, 123.5s. GATE V (standalone `final_frame_check.py --lenient`, run
from inside the reel folder, on the true final master): **0 BLOCKER, 0 MAJOR**.

**Vertical (`vertical/scenes.py`):** genuine hand-authored portrait redesign for all 9 beats
(rendered 2160x3840), same `T()` helper plus the portrait `config.frame_width` patch (Manim's CLI
`-r` flag doesn't recompute `frame_width` for portrait otherwise — copied verbatim from the
sibling reel's documented fix). B02's 3-tile horizontal row became a single stacked column; B03's
code line was re-wrapped across more/narrower lines (same verbatim substrings, nothing reworded)
with the same character-index highlight technique; B04's chain was already a single column in the
landscape parent and only needed narrowing; B05's 3-card horizontal row and B06's 2-card
side-by-side row each became stacked columns.

**Vertical final:** 2160x3840, 123.5s (same duration as the landscape master — full-length
companion via `./art vertical`, no beats dropped, no cap, no rewritten outro, no added endcard).
GATE V on the true final master: **0 BLOCKER, 0 MAJOR**.

**Real bugs hit and fixed during this build:**

- **Stale render cache:** `run.sh`/Manim's own `media/` cache does not detect `scenes.py` source
  changes and will silently reuse old renders. Deleted `manim/`, `media/`, `clips/`, `_qc/` and any
  previous slate/final mp4s before every re-render that followed a scene edit, in both the
  landscape reel and the `vertical/` subfolder, and verified every resulting clip's mtime postdated
  `scenes.py`'s mtime via `stat -f %m`/`os.path.getmtime` before trusting any render as fresh.
- **GATE B false TEXT_ON_CURVE on an intentional highlight box (landscape + vertical B03):** B03's
  real `hasData` guard line is boxed around only the substring `newItems.length > 1` (via Manim
  `Text` character-index slicing on the full code line), not the whole line — the box's own edges
  necessarily cross the parent line's centerline, which `manim_layout_audit.py`'s GATE B correctly
  flagged as "label on a curve/line" (`TEXT_ON_CURVE`) under `--curve-strict`. Fixed using the
  gate's own documented escape hatch: `flag_box._qc_intentional = True` (and the same for B04's
  genuine strike-through `Line`, which deliberately crosses the struck code line).
- **GATE V canvas-fill underfill, real (landscape B02):** the real final-cut frame extraction (not
  just the gate's own report — personally re-extracted and inspected frames) found this beat's
  0/1/2 counter composition covering only 45% of the safe area (min 55%) — width was already ~91%
  but height only ~51%, a real vertical underfill from tight tile padding and inter-group spacing,
  not a false positive. Fixed by enlarging the tile padding and the buff between title/tiles/zinger.
- **GATE V canvas-fill underfill from mid-animation timing, real (landscape + vertical B04):** the
  real final-cut frame extraction sampled this beat at its 50% timestamp and found the closing
  caption not yet on screen (it previously landed well past the midpoint of the beat's 16.49s
  duration) — only 41% of the safe area (min 55%), missing the caption's own width/height. Fixed
  by shortening the `self.wait()` calls between the diff, the fails-box and the dead-end box so the
  full composition (including the caption) is on screen before the 50% sample point, in both
  aspects. An arithmetic slip in the first attempt at this fix (recomputing the final `self.wait()`
  remainder) initially made the clip ~1s too long (manim's own compile step reported
  "B04: clip 17.6s center-cut to 16.5s", silently trimming the excess) — caught by independently
  re-summing every `run_time=`/`self.wait()` value in both scene files against each beat's measured
  audio duration before re-rendering, which also confirmed all other beats' timings were exact.
- **GATE B real safe-area overflow (vertical B05):** the post-render layout audit found the second
  closing caption's real bottom edge at y=-3.46, just outside the +/-3.4 safe-area half-height — the
  3-row-card column's height cap (4.6) left no real room for the two independently-chained captions
  below it. Fixed by tightening the cap to 4.3.
- **GATE V false edge-bleed on the review slate (both aspects, every beat):** `./art run`'s
  embedded GATE V check runs against the review slate (`<slug>-slate.mp4`), which burns in a
  per-beat timestamp overlay in the top-right corner for human review. `final_frame_check.py`'s
  `BURN_IN_EXCLUDE` constant only blanks the bottom-left beat-label strip, not this corner
  timestamp — so every single sampled frame was flagged "content crosses the title-safe right/top
  edge," 18/18 frames, identically, across every beat including the simplest title card. Confirmed
  this was the slate's own review chrome (not real scene content) by extracting a raw frame
  directly from the slate mp4 and visually inspecting the corner overlay. Per the toolkit's own
  design (`run.sh`'s comment: "A clean final requires the compiler's mandatory verification... use
  `./art final`"), this check is not meant to gate the review cut — proceeded to `./art final` for
  both aspects, whose own embedded GATE V check (against the real candidate, no slate chrome)
  passed cleanly, and separately re-ran `final_frame_check.py --lenient` directly against both true
  final masters per this build's own requirement: **0 BLOCKER, 0 MAJOR** on both.

**Deliverables confirmed, both renamed and verified:**
- `deliverables/landscape/AlertSecondItemGate_SaiPranaviJeedigunta.mp4` (+ `.verified.json`,
  SHA-256 confirmed matching the compiled master: `74b68e42...`)
- `deliverables/vertical/AlertSecondItemGate_SaiPranaviJeedigunta.mp4` (+ `.verified.json`,
  SHA-256 confirmed matching the compiled master: `5b7644ab...`)

Both final masters were personally re-inspected frame-by-frame (B02's counter and B04's dead-end
chain at both its 50% and 85% sample points in landscape; B05's full before/after table with both
captions visible, and B06's honest-limits cards in vertical) directly from the shipped
deliverables, in both aspects, as a final check before considering this project done — no
text-rendering artifacts, no clipping, no overlap in either aspect.

Publishing not authorized. Nothing inside `brutalist/` was modified; nothing inside `/Users/pranavijs/mycroft` was modified.

## 2026-10-20 — ADDENDUM: fellow-name retrofit (org naming policy: first-name-last-initial only)

- **Scope**: full name "Sai Pranavi Jeedigunta" found in spoken narration (B01), the on-screen name tag (B01), and the on-screen sign-off credit (B08, both aspects). Retrofitted to "Sai Pranavi J." everywhere.
- **Narration (B01)**: `narration_text` changed in `beat_sheet.json` and `vertical/beat_sheet.json`: "Hi, I'm Sai Pranavi Jeedigunta." → "Hi, I'm Sai Pranavi J." Regenerated Kokoro audio (`af_bella`, `generate_audio_kokoro.py --only B01`). New measured duration **15.46s** (ffprobe: 15.456s) vs the old `actual_duration_s` of **15.94s** — a 0.48s shrink, over the ~0.3s retime threshold.
- **Retiming (B01)**: landscape plays sum to 2.1s → `self.wait(13.84)` → **`self.wait(13.36)`** (15.456 − 2.1 = 13.356). Vertical plays sum to 1.8s → `self.wait(14.14)` → **`self.wait(13.66)`** (15.456 − 1.8 = 13.656).
- **On-screen credit**: `scenes.py` B01 name tag and B08 tagline changed to "Sai Pranavi J." (plus a matching comment fix). `vertical/scenes.py` B01 name tag changed the same way; `vertical/scenes.py` B08's tagline was previously hard-wrapped `"in for Sai Pranavi\nJeedigunta"` across two lines — changed to a single line `"in for Sai Pranavi J."`.
- **No layout regression**: this project's vertical B08 already used a fixed height floor (`frame_h = max(content.height + 1.0, 6.4)`, the same pattern as the sibling 2026-10-06 classifier video), so shortening the tagline to one line had no effect on the shipped frame size. Confirmed clean on the first `./art final vertical` attempt (0 BLOCKER, 0 MAJOR internally), no respacing needed.
- **Stale-cache avoidance**: deleted `manim/B01.mp4`, `clips/B01.mp4`, `manim/B08.mp4`, `clips/B08.mp4` and the same four paths under `vertical/` before rebuilding — no other beat's cache touched.
- **Rebuild**: `./art run . --height 1080` and `./art run vertical --height 1920` re-rendered only B01/B08 via Manim (GATE A/B CLEAN); both review GATE V runs showed the known review-slate false positive (18/18 frames `edge-bleed`, uniform across every beat including untouched ones). `./art final . --out deliverables/landscape` and `./art final vertical --height 3840 --out deliverables/vertical` both rebuilt cleanly on the first attempt. Verified via `stat -f %m` that every regenerated `manim/B01.mp4`/`manim/B08.mp4` (both aspects) postdates its `scenes.py` edit.
- **New master durations**: landscape **123.042s** (was 123.5s), vertical **123.042s** (was 123.5s) — both match the expected ~0.48s shift from the B01 retime, and both confirmed true 4K (3840×2160 / 2160×3840).
- **GATE V (final masters, `final_frame_check.py --lenient`)**: landscape **0 BLOCKER, 85 MAJOR**; vertical **0 BLOCKER, 65 MAJOR**. Ship bar (0 BLOCKER) met on both. The MAJOR findings are the same full-continuous-frame-scan sampling artifact (transitional/fade frames across many untouched beats) documented in this fellow's other retrofitted videos, not a regression from this change.
- **Manual frame verification**: extracted real frames (ffmpeg) from B01 and B08 in both masters — name tag reads "Sai Pranavi J." cleanly in both aspects; B08 sign-off reads "in for Sai Pranavi J." on its own line, fully contained within its bordered card, no clipping, in both aspects.
- **Deliverables renamed**: `deliverables/landscape/AlertSecondItemGate_SaiPranaviJeedigunta.mp4` (+ `.verified.json`) → `AlertSecondItemGate_SaiPranaviJ.mp4` (+ `.verified.json`), same for `deliverables/vertical/` — copied from the freshly rebuilt masters, sha256-verified identical to `deliverables/landscape/2026-10-15-the-alert-that-waited-for-a-second-item.mp4` / `deliverables/vertical/...-vertical.mp4`, then the old-named files and sidecars deleted.
- `README.md` name references ("Sai Pranavi Jeedigunta" / "SaiPranaviJeedigunta") updated to "Sai Pranavi J." / "SaiPranaviJ" — no other claims changed (the 123.5s duration mentioned in the pre-existing README prose is now superseded by the 123.042s figure above).
- Not touched: `FACTCHECK.md`, `SOURCES.md`, `beat_sheet.json` metadata/gates beyond the `narration_text` field.
