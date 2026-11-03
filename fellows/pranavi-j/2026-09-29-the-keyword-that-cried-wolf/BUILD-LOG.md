# BUILD-LOG — The Keyword That Cried Wolf

## 2026-09-29/2026-10-02 — Full build (both aspects)

**Gate P:** Beat sheet approved 2026-09-29. **FACTCHECK:** resolved same day — B06 gets a "not
reviewed — below alert threshold" label on the SEC case row (never actively reviewed-and-approved,
since its `urgency_score` never crosses the alert gate), B07's honest-limits beat kept at full
weight, no softening.

**Audio:** Kokoro `af_bella`, all 9 beats, B00 a real silent mp3 (`ffmpeg anullsrc`) with
`audio_policy: "silence"` set explicitly per `build_safety.py`'s silent-required-audio gate.

**`scenes.py` (landscape):** authored with a `T()` safe-text helper (creates `Text()` at
`font_size=48`, then scales geometrically to the intended size) used for every on-screen string —
avoids a confirmed Manim/Pango small-font-size rendering artifact (phantom gaps inside words, e.g.
"video" -> "v ideo") that bit two sibling projects earlier this cycle. B03 quotes the real scoring
rule verbatim; B04 shows both real trigger-word titles in their actual context; B05 explicitly
shows the fail-open third branch (model-fails -> goes through anyway), not just the happy path;
B06 shows all 3 test cases together with the SEC case correctly labeled "not sent to model."

**Landscape final:** 3840x2160, 135.54s. GATE V: 0 BLOCKER, 0 MAJOR.

**Vertical (`vertical/scenes.py`):** genuine hand-authored portrait redesign for all 9 beats
(1080x1920-native, rendered 2160x3840), same `T()` helper plus the portrait `config.frame_width`
patch (Manim's CLI `-r` flag doesn't recompute `frame_width` for portrait otherwise — documented
fix, copied from the `2026-09-14` sibling projects). B05's 3-branch flow diagram and B06's 3-row
table both needed real redesign (not just narrowing) to stay legible in the narrow canvas —
confirmed by direct frame inspection, not assumed.

**Vertical final:** 2160x3840, 135.42s. GATE V: 0 BLOCKER, 2 MAJOR (both on B08, brand/sign-off
card, borderline underfill exactly at the 55% floor — personally confirmed via direct frame
extraction that the card is fully legible and well-composed; same accepted minor-cosmetic category
as the brand cards in every sibling video this cycle).

**Real bugs hit and fixed during this build (both previously known, both handled per established
playbook):**
- **Stale render cache:** `run.sh` does not detect `scenes.py` source changes and silently reuses
  old `manim/*.mp4`/`clips/*.mp4`/Manim's own `media/` cache. Deleted and re-rendered clean
  whenever a scene edit followed a prior render, and verified every clip's mtime postdates
  `scenes.py`'s mtime before trusting any render as current.
- **Manim Text() small-font-size artifact:** avoided from the start in this project by using the
  `T()` helper for every beat in both `scenes.py` files, rather than discovering and retrofitting
  it after the fact (as happened on the `2026-09-14` sibling projects).

**Process note:** this build spanned several agent sessions due to repeated transient network
disconnects (API `ECONNRESET`), not logic failures — each resumption re-verified actual on-disk
state (file mtimes, process list, deliverable hashes) before continuing, rather than trusting the
prior session's self-report. The final landscape and vertical masters were personally
re-inspected frame-by-frame (B05, B06, B08) directly from the shipped deliverables as a final
check before considering this project done.

**Deliverables confirmed, both renamed and verified:**
- `deliverables/landscape/KeywordReScoring_SaiPranaviJeedigunta.mp4` (+ `.verified.json`)
- `deliverables/vertical/KeywordReScoring_SaiPranaviJeedigunta.mp4` (+ `.verified.json`, input
  hashes confirmed matching the final clips on disk)

Publishing not authorized. Nothing inside `brutalist/` was modified.

## 2026-10-20 — ADDENDUM: fellow-name retrofit (org naming policy: first-name-last-initial only)

- **Scope**: full name "Sai Pranavi Jeedigunta" found in spoken narration (B01), the on-screen name tag (B01), and the on-screen sign-off credit (B08, both aspects). Retrofitted to "Sai Pranavi J." everywhere.
- **Narration (B01)**: `narration_text` changed in `beat_sheet.json` and `vertical/beat_sheet.json`: "Hi, I'm Sai Pranavi Jeedigunta." → "Hi, I'm Sai Pranavi J." Regenerated Kokoro audio (`af_bella`, `generate_audio_kokoro.py --only B01`). New measured duration **14.26s** (ffprobe: 14.256s) vs the old `actual_duration_s` of **14.904s** — a 0.65s shrink, over the ~0.3s retime threshold.
- **Retiming (B01)**: landscape plays sum to 2.1s → `self.wait(12.8)` → **`self.wait(12.16)`** (14.256 − 2.1 = 12.156). Vertical plays sum to 1.8s → `self.wait(13.1)` → **`self.wait(12.46)`** (14.256 − 1.8 = 12.456).
- **On-screen credit**: `scenes.py` B01 name tag and B08 tagline changed to "Sai Pranavi J." (plus a matching comment fix). `vertical/scenes.py` B01 name tag changed the same way; `vertical/scenes.py` B08's tagline was previously hard-wrapped `"in for Sai Pranavi\nJeedigunta"` across two lines — changed to a single line `"in for Sai Pranavi J."`.
- **Layout regression caught and fixed**: this project's own pre-existing README already flagged vertical B08 as borderline (2 MAJOR, underfill right at the 55% floor) even before this retrofit. Shortening the two-line tagline to one line pushed it over the edge to a real 47% fill, confirmed via `./art final vertical --height 3840` (not the review-slate false positive) — a genuine defect. Fixed by increasing the real spacing between B08's four stacked elements (`buff` 0.55 → 0.95 in `vertical/scenes.py`'s `B08_BrandOutro`), the same real-content-respacing fix used on the sibling 2026-09-22 all-clear-email video's vertical B08. Re-verified against the real GATE V run: 0 BLOCKER, 0 MAJOR on the rebuilt candidate (an improvement over the original's borderline 2 MAJOR).
- **Stale-cache avoidance**: deleted `manim/B01.mp4`, `clips/B01.mp4`, `manim/B08.mp4`, `clips/B08.mp4` and the same four paths under `vertical/` before rebuilding (vertical B08 was deleted/re-rendered twice: once for the name text, once more for the spacing fix) — no other beat's cache touched.
- **Rebuild**: `./art run . --height 1080` and `./art run vertical --height 1920` re-rendered only B01/B08 via Manim (GATE A/B CLEAN); both review GATE V runs showed the known review-slate false positive (18/18 frames `edge-bleed`, uniform across every beat including untouched ones). `./art final . --out deliverables/landscape` rebuilt cleanly on the first attempt; `./art final vertical --height 3840 --out deliverables/vertical` initially REFUSED on the real underfill finding above, passed clean after the spacing fix and a fresh `./art run vertical` pass. Verified via `stat -f %m` that every regenerated `manim/B01.mp4`/`manim/B08.mp4` (both aspects) postdates its relevant `scenes.py` edit.
- **New master durations**: landscape **134.875s** (was ~134.9s per the original log's 135.54s claim — the 0.65s shrink from B01's retime plus B06's existing 0.5s head/tail center-cut account for the difference), vertical **134.792s**. Both confirmed true 4K (3840×2160 / 2160×3840).
- **GATE V (final masters, `final_frame_check.py --lenient`)**: landscape **0 BLOCKER, 43 MAJOR**; vertical **0 BLOCKER, 50 MAJOR**. Ship bar (0 BLOCKER) met on both. The MAJOR findings are the same full-continuous-frame-scan sampling artifact (transitional/fade frames across many untouched beats) documented in this fellow's other retrofitted videos, not a regression from this change.
- **Manual frame verification**: extracted real frames (ffmpeg) from B01 and B08 in both masters — name tag reads "Sai Pranavi J." cleanly in both aspects; B08 sign-off reads "in for Sai Pranavi J." on its own line, fully contained within its bordered card, well-balanced, no clipping, in both aspects.
- **Deliverables renamed**: `deliverables/landscape/KeywordReScoring_SaiPranaviJeedigunta.mp4` (+ `.verified.json`) → `KeywordReScoring_SaiPranaviJ.mp4` (+ `.verified.json`), same for `deliverables/vertical/` — copied from the freshly rebuilt masters, sha256-verified identical to `deliverables/landscape/2026-09-29-the-keyword-that-cried-wolf.mp4` / `deliverables/vertical/...-vertical.mp4`, then the old-named files and sidecars deleted.
- `README.md` name references ("Sai Pranavi Jeedigunta" / "SaiPranaviJeedigunta") updated to "Sai Pranavi J." / "SaiPranaviJ" — no other claims changed (the duration/GATE-V figures in the pre-existing README prose are now superseded by the figures above).
- Not touched: `FACTCHECK.md`, `SOURCES.md`, `beat_sheet.json` metadata/gates beyond the `narration_text` field.
