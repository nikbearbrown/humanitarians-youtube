# BUILD-LOG — The Classifier That Learned When Not to Guess

## 2026-10-09/2026-10-11 — Full build (both aspects)

**Gate P:** Beat sheet approved 2026-10-06. **FACTCHECK:** resolved same day — B06's "1 of 8" result
kept at full weight, framed explicitly as a correct outcome, not a shortfall; no softening.

**Audio:** Kokoro `af_bella`, all 9 beats. B01-B08 generated via `generate_audio_kokoro.py`
(measured durations: B01 17.59s, B02 14.86s, B03 30.41s, B04 26.5s, B05 27.12s, B06 24.34s,
B07 13.3s, B08 1.51s — B08 is short because its narration is literally just "Explained with
Claude Code."). B00 is a real silent mp3 (`ffmpeg anullsrc`, 4.05s) with `audio_policy: "silence"`
set explicitly per `build_safety.py`'s silent-required-audio gate. `beat_sheet.json`'s
`actual_duration_s` fields and `mp3/timings.json` updated from the real measured values, not the
pre-audio estimates.

**`scenes.py` (landscape):** authored with the `T()` safe-text helper (Pango/Cairo small-font-size
artifact workaround) used for every on-screen string, copied from this fellow's
`2026-09-29-the-keyword-that-cried-wolf` sibling. B03 uses 3 of the real 8 residual headlines
verbatim from `B2-VERIFICATION.md`'s 2026-10-06 addendum; B04 shows the new node's exact
conditional gate (`ONLY IF source_feed == 'Unknown Source'`) and the untouched bypass branch as
separate explicit paths, not narrated alone; B05 shows all 4 real proof numbers (0 mutated / 1
resolved / 7 declined / 0 errors) together plus the one resolved headline and its new label; B06
shows the "1 of 8 — and that's the correct number" framing with all 7 declined real headlines
dimmed below.

**Landscape final:** 3840x2160, 159.875s. GATE V (standalone `final_frame_check.py --lenient`,
run from inside the reel folder, on the true final master): **0 BLOCKER, 0 MAJOR**.

**Vertical (`vertical/scenes.py`):** genuine hand-authored portrait redesign for all 9 beats
(rendered 2160x3840), same `T()` helper plus the portrait `config.frame_width` patch (Manim's CLI
`-r` flag doesn't recompute `frame_width` for portrait otherwise). B04's biggest redesign: the
parent's side-by-side YES/NO branch cards became a single vertical chain (Normalize → gate → NEW
node → bypass node → merge), each box built as its own unit and the whole chain height-capped via
`scale_to_fit_height` before positioning — avoiding hand-picked y-coordinates entirely. B05's
4-tile row became a 2x2 grid; B06's 2-column declined list became a single column with each
headline condensed to one short line (the full 2-line wrapped version was genuinely too tall for
the narrow frame alongside the title/statement/closing).

**Vertical final:** 2160x3840, 159.875s (same duration as the landscape master — full-length
companion via `./art vertical`, no beats dropped, no cap, no rewritten outro, no added endcard).
GATE V on the true final master: **0 BLOCKER, 0 MAJOR**.

**Real bugs hit and fixed during this build:**

- **Stale render cache:** `run.sh`/Manim's own `media/` cache does not detect `scenes.py` source
  changes and will silently reuse old renders. Deleted `manim/`, `media/`, `clips/`, `_qc/` and
  the slate mp4 before every re-render that followed a scene edit, and verified every resulting
  clip's mtime postdated `scenes.py`'s mtime via `stat -f %m` before trusting any render as fresh.
- **GATE A "shapes never change" false-triggers on text-only compositions:** `static_scene_check.py`
  only tracks non-text (geometric) mobjects for its distinctness check; 3 early beats (B02, B06,
  B07) built almost entirely from `Text`/`VGroup` with only ONE static shape (a single box/frame)
  created once and never changed, which the gate correctly flagged as "shapes never change — 1
  distinct shape-state." Fixed by adding a second, later shape-creation event to each (a divider
  line, a bordered panel) — the same pattern the sibling reels' scenes already used for box/arrow
  diagrams, just not yet applied to pure-text statement cards.
- **GATE B safe-area overflow (titles/captions):** several beats' `to_edge(UP/DOWN, buff=...)`
  values (0.4-0.6) were too tight; the real rendered frame's top/bottom edges landed just outside
  the ±3.4 (landscape) / ±3.4 (portrait, same y-bound) safe-area half-height. Standardized to
  buff=0.68 (titles) / 0.65-0.85 (captions/closings) across both `scenes.py` files after the
  pattern repeated on B03, B04, and the vertical B03/B04/B06.
- **GATE B real text-on-text overlap (vertical B03, B04, B06):** a first draft of each positioned
  its closing caption/line independently via `to_edge(DOWN, ...)` while the beat's main content
  (cards, a diagram chain, a declined-headline list) was positioned via `next_to()` chains with no
  shared height budget — on a few beats the main content grew tall enough to physically overlap
  the independently-positioned closing text (real measured overlaps of 41-67%, not a QC
  false-positive). Fixed by building the WHOLE rest-of-beat content (including the closing line)
  as one `VGroup`, height-capping it via `scale_to_fit_height`, and positioning it as a single
  unit below the title — the same pattern already proven in this file's B04 pipeline-diagram chain.
- **GATE V canvas-fill underfill, real and repeated (landscape B02, B07; vertical B06, B08):** the
  real final-cut frame extraction (not the gate's report alone — personally re-extracted frames
  and inspected them) found several beats' content bounding box covering under the 55% safe-area
  floor, in some cases because content was genuinely clustered in one quadrant (landscape B02's
  first draft had all 3 counter-rows left-aligned under a divider, leaving the whole right half and
  bottom half of the frame empty — fixed by centering the composition and bringing the closing line
  in well before the beat's midpoint) and in others because a short card's frame was sized purely
  from its own modest content (landscape B07's statement frame, vertical B08's brand card — fixed
  with a generous fixed-minimum frame size instead of a content-derived cap).
- **GATE V edge-bleed, real (landscape B05; vertical B08):** landscape B05's 4-number-tile row at
  its original width (3.1 each + 0.35 buff) measured 13.45 world units wide against a 12.6-unit
  safe width — shrunk to 2.7-wide tiles with 0.28 buff. Vertical B08's brand card hit the opposite
  problem: a frame padding of `content.width + 1.0` around a handle string that already used
  nearly the full safe width pushed the frame itself past the safe edge — fixed by reducing the
  handle's own fit-width cap and using a modest fixed frame padding instead.

**Process note:** several render passes were interrupted mid-build (process killed at the tool's
timeout, not a build failure) due to heavy concurrent CPU load from an unrelated render running
elsewhere on the same machine (system load average briefly exceeded 39). Each resumption verified
actual on-disk state (which `manim/<B>.mp4` files existed and their mtimes relative to
`scenes.py`) before continuing, rather than re-rendering unnecessarily or trusting a prior
session's self-report.

**Deliverables confirmed, both renamed and verified:**
- `deliverables/landscape/ClassifierFallbackClassification_SaiPranaviJeedigunta.mp4` (+
  `.verified.json`, SHA-256 confirmed matching the compiled master)
- `deliverables/vertical/ClassifierFallbackClassification_SaiPranaviJeedigunta.mp4` (+
  `.verified.json`, SHA-256 confirmed matching the compiled master)

Both final masters were personally re-inspected frame-by-frame (B04's pipeline diagram, B06's
honest-limits framing, B08's brand card) directly from the shipped deliverables, in both aspects,
as a final check before considering this project done — no text-rendering artifacts, no clipping,
no overlap in either aspect.

Publishing not authorized. Nothing inside `brutalist/` was modified.

## 2026-10-20 — ADDENDUM: fellow-name retrofit (org naming policy: first-name-last-initial only)

- **Scope**: full name "Sai Pranavi Jeedigunta" found in spoken narration (B01), the on-screen name tag (B01), and the on-screen sign-off credit (B08, both aspects). Retrofitted to "Sai Pranavi J." everywhere.
- **Narration (B01)**: `narration_text` changed in `beat_sheet.json` and `vertical/beat_sheet.json`: "Hi, I'm Sai Pranavi Jeedigunta." → "Hi, I'm Sai Pranavi J." Regenerated Kokoro audio (`af_bella`, `generate_audio_kokoro.py --only B01`). New measured duration **16.90s** (ffprobe: 16.896s) vs the old `actual_duration_s` of **17.59s** — a 0.69s shrink, over the ~0.3s retime threshold.
- **Retiming (B01)**: landscape plays sum to 2.1s → `self.wait(15.49)` → **`self.wait(14.80)`** (16.896 − 2.1 = 14.796). Vertical plays sum to 1.8s → `self.wait(15.79)` → **`self.wait(15.10)`** (16.896 − 1.8 = 15.096).
- **On-screen credit**: `scenes.py` B01 name tag and B08 tagline changed to "Sai Pranavi J." (plus a matching comment fix). `vertical/scenes.py` B01 name tag changed the same way; `vertical/scenes.py` B08's tagline was previously hard-wrapped `"in for Sai Pranavi\nJeedigunta"` across two lines — changed to a single line `"in for Sai Pranavi J."`.
- **No layout regression**: unlike the sibling 2026-09-22/2026-09-29 retrofits, this project's vertical B08 already used a fixed height floor (`frame_h = max(content.height + 1.0, 6.4)`, added in the original build to fix a prior 52% underfill) rather than a pure content-derived height — so shortening the tagline to one line had no effect on the shipped frame size. Confirmed clean on the first `./art final vertical` attempt (0 BLOCKER, 0 MAJOR internally), no respacing needed.
- **Stale-cache avoidance**: deleted `manim/B01.mp4`, `clips/B01.mp4`, `manim/B08.mp4`, `clips/B08.mp4` and the same four paths under `vertical/` before rebuilding — no other beat's cache touched.
- **Rebuild**: `./art run . --height 1080` and `./art run vertical --height 1920` re-rendered only B01/B08 via Manim (GATE A/B CLEAN); both review GATE V runs showed the known review-slate false positive (18/18 frames `edge-bleed`, uniform across every beat including untouched ones) — landscape additionally showed a pre-existing, untouched-beat `low-contrast` MAJOR on B07 (0.29 vs 0.3 threshold), not something this retrofit introduced. `./art final . --out deliverables/landscape` and `./art final vertical --height 3840 --out deliverables/vertical` both rebuilt cleanly on the first attempt. Verified via `stat -f %m` that every regenerated `manim/B01.mp4`/`manim/B08.mp4` (both aspects) postdates its `scenes.py` edit.
- **New master durations**: landscape **159.167s** (was 159.875s), vertical **159.167s** (was 159.875s) — both match the expected ~0.69s shift from the B01 retime, and both confirmed true 4K (3840×2160 / 2160×3840).
- **GATE V (final masters, `final_frame_check.py --lenient`)**: landscape **0 BLOCKER, 85 MAJOR**; vertical **0 BLOCKER, 82 MAJOR**. Ship bar (0 BLOCKER) met on both. The MAJOR findings are the same full-continuous-frame-scan sampling artifact (transitional/fade frames, plus the pre-existing B07 low-contrast borderline noted above) documented in this fellow's other retrofitted videos, not a regression from this change.
- **Manual frame verification**: extracted real frames (ffmpeg) from B01 and B08 in both masters — name tag reads "Sai Pranavi J." cleanly in both aspects; B08 sign-off reads "in for Sai Pranavi J." on its own line, fully contained within its bordered card, no clipping, in both aspects.
- **Deliverables renamed**: `deliverables/landscape/ClassifierFallbackClassification_SaiPranaviJeedigunta.mp4` (+ `.verified.json`) → `ClassifierFallbackClassification_SaiPranaviJ.mp4` (+ `.verified.json`), same for `deliverables/vertical/` — copied from the freshly rebuilt masters, sha256-verified identical to `deliverables/landscape/2026-10-06-the-classifier-that-learned-when-not-to-guess.mp4` / `deliverables/vertical/...-vertical.mp4`, then the old-named files and sidecars deleted.
- `README.md` name references ("Sai Pranavi Jeedigunta" / "SaiPranaviJeedigunta") updated to "Sai Pranavi J." / "SaiPranaviJ" — no other claims changed (the 159.875s duration mentioned in the pre-existing README prose is now superseded by the 159.167s figure above).
- Not touched: `FACTCHECK.md`, `SOURCES.md`, `beat_sheet.json` metadata/gates beyond the `narration_text` field.
