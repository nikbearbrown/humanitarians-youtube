# BUILD-LOG — Tokenization: Why AI Can't Count the Letters in Its Own Words

## 2026-10-02 — Full build (both aspects)

**Gate P:** Beat sheet approved 2026-10-02 (see `BEAT-SHEET.md`). **FACTCHECK:** resolved same day
— fully generic worked example, no real model/vendor named or benchmarked (see `FACTCHECK.md`).

**Audio:** Kokoro `af_bella`, all 9 beats. B00 a real silent mp3 (`ffmpeg anullsrc`, 4.056s) with
`audio_policy: "silence"` set explicitly per `build_safety.py`'s silent-required-audio gate. B01–B08
generated via `generate_audio_kokoro.py`; every duration measured via `ffprobe`, written back to
`beat_sheet.json`'s `actual_duration_s` fields. Total measured runtime: 121.04s (both aspects).

**Illustrative word:** "strawberry", counting the letter "R" — chosen because it plausibly
BPE-splits into 3 sub-word chunks, has a repeated letter worth counting (3 R's), and mirrors the
well-known "how many R's" class of example `BEAT-SHEET.md` references, without naming or
benchmarking any specific real model. The same word and same 3-chunk split (STRAW / BER / RY) are
reused across B03/B04/B05 per the Legibility Contract. B04's illustrative miscounted tally:
STRAW→1 R, BER→1 R, RY→0 R (model treats "RY" as one opaque chunk and misses the R inside it) = 2,
versus the true count of 3. B05's falsifiability case spells the same word letter-by-letter
(S-T-R-A-W-B-E-R-R-Y), each letter its own token, count = 3, matching the true count — same word,
same model, only the granularity changed.

**`scenes.py` (landscape):** authored with the `T()` safe-text helper (creates `Text()` at
`font_size=48`, then scales geometrically to the intended size) used for every on-screen string —
avoids the confirmed Manim/Pango small-font-size rendering artifact (phantom gaps inside words,
e.g. "video" → "v ideo") documented in this fellow's sibling reels. Style/palette/helpers (PALETTE,
`T()`, `fit()`, `panel()`, `box_around()`, plus a new `token_chunk()` idiom for this reel's
word-splitting beats) copied from `2026-09-29-the-keyword-that-cried-wolf` and
`2026-09-22-the-all-clear-that-wasnt-all-there` for visual consistency across the series.

**Landscape final:** 3840x2160, 121.17s. GATE V (on the true final master, `--lenient`): 0 BLOCKER,
0 MAJOR. Personally re-inspected frame extractions from B05 (spelled-out fix) and B08 (brand
outro) directly from the shipped deliverable — clean text rendering, no artifacts, good composition.

**Vertical (`vertical/scenes.py`):** genuine hand-authored portrait redesign for all 9 beats
(rendered natively at 2160x3840 via the portrait `config.frame_width` patch — Manim's CLI `-r` flag
doesn't recompute `frame_width` for portrait otherwise; copied from this fellow's sibling reels'
documented fix). B02's two task cards (LEFT/RIGHT → TOP/BOTTOM stack), B04's model/true count boxes
(side-by-side → TOP/BOTTOM stack with the mismatch sign between them), and B05's 10-letter token
row (single row → two rows of 5, STRAW / BERRY split) needed real redesign, not just narrowing, to
stay legible in the narrow canvas.

**Vertical final:** 2160x3840, 121.17s — same duration as landscape, all 9 beats present, no
dropped beats, no duration cap (built via `./art vertical`, not the Shorts-style cut). GATE V (on
the true final master, `--lenient`): 0 BLOCKER, 0 MAJOR. Personally re-inspected frame extractions
from B05 and B08 directly from the shipped deliverable.

**Real bugs hit and fixed during this build:**
- **Timing arithmetic errors (landscape B02, B06):** two beats' hand-computed `self.wait()`
  remainders were wrong (a dropped addend in the "waits above" tally), causing B02's rendered clip
  to come out 1.0s longer than its measured Kokoro audio and B06's 0.5s longer. Caught by comparing
  each scene's `run_time=`/`self.wait()` sum (via a small script) against the beat's measured
  `actual_duration_s`, not by trusting the inline comments. Both fixed to match exactly.
- **GATE B layout error (landscape B05):** the "✓ MATCHES TRUE COUNT" checkmark line, placed below
  the model's-count box whenever it was too wide to fit beside it, landed with its real bottom edge
  at y=-3.6, outside the ±3.4 safe-area half-height — confirmed via `manim_layout_audit.py`'s
  real rendered-frame measurement, not a guessed margin. Fixed by raising the count box and always
  placing the checkmark below (removing the width-dependent branch).
- **GATE V canvas-fill underfill (landscape B03, B05, B06, B08):** the true final candidate (built
  without review-cut overlays, to isolate real content from the known slate-only false positive
  below) measured real underfill — B03 37%, B05 54%, B06 42%, B08 31% of the safe area (floor 55%).
  Fixed by adding a generously sized bordered frame (same idiom as B00/B01/B07) to B03/B05, enlarging
  B06's checklist card to a fixed generous size independent of its rows' own tight bounds, and
  bumping B08's font sizes/line spacing (same fix already proven on this fellow's sibling reels'
  brand-card beat). Re-verified via a direct (no-overlay) candidate build before trusting `./art final`.
- **GATE B layout errors from the B06 canvas-fill fix (2 rounds):** enlarging B06's card first
  pushed its bottom rounded corner under the closing line below, then (after raising the card)
  pushed its top corner under the title above. Fixed by trimming the card to a shorter, ORIGIN-
  centered size that clears both with real margin on the actual rendered frame.
- **GATE B off-hard-frame coordinate (vertical B05):** the first draft chained 5 `next_to()` calls
  (title → letter rows → caption → count box → checkmark), and `static_scene_check.py` caught an
  explicit resulting coordinate at y=-4.6 — off the HARD bottom edge (±4.0), not just the safe
  margin. Fixed with the proven pattern from this fellow's sibling reels: build every piece first,
  group them into one `VGroup`, arrange, cap the total height via `scale_to_fit_height`, then
  position the whole block with a single `next_to` call.
- **GATE B text-on-curve (vertical B02):** the "Wildly different reliability." zinger line landed
  directly on the bottom task card's own rounded corner — the panels' natural stacked height (5.3)
  was under the old 5.4 scale-down ceiling and so never actually got capped. Lowered the ceiling to
  4.6 so the group reliably scales down and clears the zinger with real margin.
- **Stale render cache:** `run.sh` does not detect `scenes.py` source changes and silently reuses
  old `manim/*.mp4`/`clips/*.mp4`/Manim's own `media/` cache. Deleted and re-rendered clean whenever
  a scene edit followed a prior render, and verified via `stat -f %m` that every resulting clip's
  mtime postdates `scenes.py`'s mtime before trusting any render as current.
- **GATE V false positive on the review slate cut (both aspects, confirmed non-blocking):** every
  `./art run` compiled review cut failed GATE V with 18/18 BLOCKER "edge-bleed" findings. Traced to
  `final_frame_check.py`'s `BURN_IN_EXCLUDE` region only covering the bottom-left beat-label strip,
  not the top-right review-cut timestamp overlay (`compile.py`'s `--review`-only `drawtext` burn-in)
  — confirmed by building a clean candidate (concatenated `clips/*.mp4` directly, no review overlay)
  and re-running the same check, which came back BLOCKER=0 immediately. This is a known artifact of
  the review slate, not the true final deliverable; `./art final` (which never draws review labels)
  was used for both actual masters and gated clean on its own internal (strict) GATE V check.

**Deliverables confirmed, both renamed and verified:**
- `deliverables/landscape/Tokenization_SaiPranaviJeedigunta.mp4` (3840x2160, 121.17s) +
  `.verified.json`
- `deliverables/vertical/Tokenization_SaiPranaviJeedigunta.mp4` (2160x3840, 121.17s) +
  `.verified.json`

Publishing not authorized. Nothing inside `brutalist/` was modified.

## 2026-10-20 — ADDENDUM: fellow-name retrofit (org naming policy: first-name-last-initial only)

- **Scope**: full name "Sai Pranavi Jeedigunta" found in spoken narration (B01), the on-screen name tag (B01), and the on-screen sign-off credit (B08, both aspects). Retrofitted to "Sai Pranavi J." everywhere.
- **Narration (B01)**: `narration_text` changed in `beat_sheet.json` and `vertical/beat_sheet.json`: "Hi, I'm Sai Pranavi Jeedigunta." → "Hi, I'm Sai Pranavi J." Regenerated Kokoro audio (`af_bella`, `generate_audio_kokoro.py --only B01`). New measured duration **13.56s** vs the old `actual_duration_s` of **14.09s** — a 0.53s shrink, over the ~0.3s retime threshold.
- **Retiming (B01)**: landscape plays sum to 2.1s → `self.wait(11.99)` → **`self.wait(11.46)`** (13.56 − 2.1 = 11.46). Vertical plays sum to 1.8s → `self.wait(12.29)` → **`self.wait(11.76)`** (13.56 − 1.8 = 11.76).
- **On-screen credit**: `scenes.py` B01 name tag and B08 tagline changed to "Sai Pranavi J." (plus a matching comment fix). `vertical/scenes.py` B01 name tag changed the same way; `vertical/scenes.py` B08's tagline was previously hard-wrapped `"in for Sai Pranavi\nJeedigunta"` across two lines — changed to a single line `"in for Sai Pranavi J."`.
- **Layout regression caught and fixed**: shortening the two-line B08 vertical tagline to one line reduced `content.height` enough to drop the real candidate's canvas-fill just under the 55% floor (measured 55% displayed, i.e. marginally below after rounding) — confirmed via `./art final vertical --height 3840` (not the review-slate false positive). Fixed with a small real-spacing increase (`buff` 0.5 → 0.75 in `vertical/scenes.py`'s `B08_BrandOutro`, the same real-content-respacing fix used on this fellow's other retrofitted sibling videos). Re-verified against the real GATE V run: 0 BLOCKER, 0 MAJOR on the rebuilt candidate. (An initial frame extracted mid-animation looked like it had a broken border — re-extracted at a later timestamp once the beat's `Create(frame)` animation had settled, confirming the border renders complete and clean; not a real defect.)
- **Stale-cache avoidance**: deleted `manim/B01.mp4`, `clips/B01.mp4`, `manim/B08.mp4`, `clips/B08.mp4` and the same four paths under `vertical/` before rebuilding (vertical B08 was deleted/re-rendered twice: once for the name text, once more for the spacing fix) — no other beat's cache touched.
- **Rebuild**: `./art run . --height 1080` and `./art run vertical --height 1920` re-rendered only B01/B08 via Manim (GATE A/B CLEAN); both review GATE V runs showed the known review-slate false positive (18/18 frames `edge-bleed`, uniform across every beat including untouched ones). `./art final . --out deliverables/landscape` rebuilt cleanly on the first attempt; `./art final vertical --height 3840 --out deliverables/vertical` initially REFUSED on the real underfill finding above, passed clean after the spacing fix and a fresh `./art run vertical` pass. Verified via `stat -f %m` that every regenerated `manim/B01.mp4`/`manim/B08.mp4` (both aspects) postdates its relevant `scenes.py` edit.
- **New master durations**: landscape **120.625s**, vertical **120.625s** (both down from the original 121.17s by the expected ~0.53s B01 shrink). Both confirmed true 4K (3840×2160 / 2160×3840).
- **GATE V (final masters, `final_frame_check.py --lenient`)**: landscape **0 BLOCKER, 35 MAJOR**; vertical **0 BLOCKER, 31 MAJOR**. Ship bar (0 BLOCKER) met on both. The MAJOR findings are the same full-continuous-frame-scan sampling artifact (transitional/fade frames across many untouched beats) documented in this fellow's other retrofitted videos, not a regression from this change.
- **Manual frame verification**: extracted real frames (ffmpeg) from B01 and B08 in both masters — name tag reads "Sai Pranavi J." cleanly in both aspects; B08 sign-off reads "in for Sai Pranavi J." on its own line, fully contained within its bordered card, no clipping, in both aspects.
- **Deliverables renamed**: `deliverables/landscape/Tokenization_SaiPranaviJeedigunta.mp4` (+ `.verified.json`) → `Tokenization_SaiPranaviJ.mp4` (+ `.verified.json`), same for `deliverables/vertical/` — copied from the freshly rebuilt masters, sha256-verified identical to `deliverables/landscape/2026-09-29-tokenization-why-ai-cant-count-its-own-letters.mp4` / `deliverables/vertical/...-vertical.mp4`, then the old-named files and sidecars deleted.
- `README.md` name references ("Sai Pranavi Jeedigunta" / "SaiPranaviJeedigunta") updated to "Sai Pranavi J." / "SaiPranaviJ" — no other claims changed (the 121.17s duration mentioned in the pre-existing README prose is now superseded by the 120.625s figure above).
- Not touched: `FACTCHECK.md`, `SOURCES.md`, `beat_sheet.json` metadata/gates beyond the `narration_text` field.
