# Build log

- 2026-09-29 — `BEAT-SHEET.md`, `beat_sheet.json`, `FACTCHECK.md`, `SOURCES.md` authored and
  approved (Gate P). FACTCHECK's one item resolved: B06's aside (the stale `FINDINGS.md` note) kept
  as drafted — a short, clearly-framed side-finding, not expanded further.
- 2026-09-29 — Voice: Bella (`af_bella`) — locked for this fellow's whole report series, unchanged
  from prior episodes.
- 2026-09-29 — Generated Kokoro audio for beats B01-B08 via `generate_audio_kokoro.py`; B00 is a
  real silent mp3, never `audio_file: null`, per `compile.py`'s `build_master_audio()` file-exists
  contract. Measured every beat's real duration via `ffprobe`: 4.049/14.23/9.74/14.02/11.66/16.51/
  20.26/12.0/5.06s — total runtime 107.537s.
- 2026-09-29/30 — Authored `scenes.py`: 9 Manim scenes (B00-B08) for the landscape (16:9) master.
  Every quoted string on screen (B03's real 4-card grid, B04's 5 real workflow feed-node names,
  B05's before/after card counts, B06's stale-note text and resolution stamp) is verbatim from
  `/Users/pranavijs/mycroft/scripts/regulatory-intel/B5-VERIFICATION.md` — nothing paraphrased.
- 2026-09-30 — Landscape master compiled (`./art run` / `./art final`): `3840x2160 (4K), 107.708s`,
  9/9 beats real (no slates). Verified receipt written to
  `deliverables/landscape/2026-09-22-the-all-clear-that-wasnt-all-there.verified.json`.
- 2026-09-30 — Authored `vertical/scenes.py`: native-portrait (9:16) redesign of all 9 beats via
  `./art vertical`, not a cropped/reformatted Shorts cut — same class names, PALETTE, and helper
  functions (`T()`, `fit()`, `panel()`, `checkmark()`, `source_card()`) as the landscape parent,
  geometry rebuilt for the narrow portrait column (B04's shown/real-feeds columns restacked
  top-to-bottom; B05's before/after grids restacked instead of wide horizontal rows).
  `vertical/manim/B00.mp4`-`B08.mp4` rendered that night (23:53-23:55).

## 2026-10-01 — Render-agent handoff, stale-cache rebuild, and false-positive GATE V investigation

A prior render-agent session on this project's vertical companion was lost to a network error
partway through. Picking this up cold (no memory of that session, only what was on disk):

- Read `vertical/scenes.py` in full and confirmed it already carries both required fixes, matching
  the working reference in `2026-09-14-rag-why-looking-it-up-isnt-enough/vertical/scenes.py`: the
  `T()` safe-text helper (renders every `Text()` at `font_size=48`, then scales — the Pango/Cairo
  small-font word-gap artifact only appears at `font_size <= ~24` created directly) used for every
  string with zero raw small-font `Text()` calls remaining, and the portrait `config.frame_width`
  patch (`if config.pixel_height > config.pixel_width: config.frame_height = 8.0; config.frame_width
  = ...`) needed because manim's CLI derives `frame_width` from the pixel aspect ratio once, before
  `-r`/`--resolution` is applied.
- Confirmed the real bug the handoff note described: all 9 `vertical/manim/*.mp4` clips had mtimes
  (Sep 30 23:53-23:55) **older** than `vertical/scenes.py`'s mtime (Oct 1 13:20) — stale renders
  from a previous version of the file, and `run.sh` has no source-change detection to catch this
  itself. Deleted `vertical/manim/`, `vertical/clips/`, `vertical/media/` entirely (kept
  `scenes.py`, `beat_sheet.json`, `mp3/`, paperwork) and re-rendered fresh via `./art run
  vertical --height 1920`. Confirmed every resulting clip's mtime (Oct 1 16:24-16:26) now postdates
  `scenes.py`.
- `./art run` exited 2 on **GATE V — 18/18 BLOCKER `edge-bleed`**, failing on every single sampled
  frame across all 9 beats. This pattern (100% failure, uniform across unrelated beat content) was
  the tell that this was a tooling false positive, not a real defect — confirmed by instrumenting
  `final_frame_check.py` directly: the review slate's running top-right timecode burn-in
  (`compile.py`'s `drawtext=... :x=w-text_w-16:y=16`, only added when `--review` and ffmpeg's
  `drawtext` filter are both present) sits outside `final_frame_check.py`'s `BURN_IN_EXCLUDE` zone
  (which only blanks the bottom-left beat-label strip), so the gate reads its own debug overlay as
  real content bleeding past the top/right title-safe edge on every frame. Confirmed by extracting
  the exact sampled frame and visually inspecting it: the actual beat content (title card, text,
  cards) sits well inside the decorative safe-area frame; only the burn-in timecode box crosses the
  edge. Running `final_frame_check.analyze_frame()` directly against the **raw, burn-in-free**
  `vertical/manim/*.mp4` clips confirmed **zero defects on all 9 beats**, coverage 58-92% of the
  safe area (within/near the 60-80% target) on every one.
  **No toolkit file was edited** (brutalist/ is off-limits); the fix was to proceed past the review
  slate's known-noisy gate to `./art final`, whose candidate carries no `--review` flag and
  therefore no burn-in overlay — the gate that actually matters for the ship decision.
- Personally extracted and viewed one real frame per beat (B00-B08, `ffmpeg -ss <midpoint>
  -frames:v 1`) from the clean `vertical/manim/*.mp4` clips: no `Text()` word-gap artifact anywhere,
  good canvas fill in every beat (title card and brand outro intentionally high at ~90%+ inside
  their decorative frames; body beats 62-76%), no clustered/negative-space layouts.
- Vertical master compiled (`./art final vertical --height 3840 --out deliverables/vertical`):
  `2160x3840 (4K, full-length), 107.708s`, 9/9 beats real (no slates). This path's own internal
  GATE V call (against the clean, burn-in-free candidate, always strict) passed with no
  intervention needed, confirming the review-slate failure above was specific to the debug overlay.
- GATE V re-run explicitly from inside `vertical/` against the verified master
  (`final_frame_check.py . --mp4 <path> --lenient`): **0 BLOCKER, 0 MAJOR** across 18 sampled
  frames — see `vertical/_qc/REPORT.md`. `ffprobe` confirms `2160x3840`, `107.708s`, valid h264/aac.
- Re-ran the same clean-master GATE V check against the **landscape** master too (its `_qc/
  REPORT.md` on disk still showed the same stale 18/18 BLOCKER false-positive read, left over from
  an earlier review-slate run): confirmed **0 BLOCKER, 0 MAJOR** on the real landscape deliverable
  as well, `_qc/REPORT.md` updated to reflect the true clean result. The landscape master's own
  `manim/*.mp4` files had their mtimes touched by that earlier session, but their SHA-256 hashes
  were verified to still match every entry in `deliverables/landscape/*.verified.json` byte for
  byte — landscape content itself was never altered, per instructions.
- Both masters copied to `deliverables/landscape/` and `deliverables/vertical/` under the NEW
  toolkit spec naming (`AllClearEmailFix_SaiPranaviJeedigunta.mp4`, no date/aspect suffix) —
  confirmed byte-identical (SHA-256) to each source master. Each folder already carries its
  `.verified.json` receipt (output SHA-256 plus every input clip/audio-file SHA-256).
- GATES CLOSED — plan, fact-check, narration, audio lock, previz, landscape render, vertical
  render, visual QC. See `beat_sheet.json` -> `metadata.gates` (and `vertical/beat_sheet.json`'s own
  copy) for the dated record.
- Wrote `README.md` and this `BUILD-LOG.md`. `FACTCHECK.md` and `SOURCES.md` left untouched.
- NOT AUTHORIZED — Publishing.

## 2026-10-20 — ADDENDUM: fellow-name retrofit (org naming policy: first-name-last-initial only)

- **Scope**: full name "Sai Pranavi Jeedigunta" found in spoken narration (B01), the on-screen name tag (B01), and the on-screen sign-off credit (B08, both aspects). Retrofitted to "Sai Pranavi J." everywhere.
- **Narration (B01)**: `narration_text` changed in `beat_sheet.json` and `vertical/beat_sheet.json`: "Hi, I'm Sai Pranavi Jeedigunta." → "Hi, I'm Sai Pranavi J." Regenerated Kokoro audio (`af_bella`, `generate_audio_kokoro.py --only B01`) for both `mp3/beat-B01.mp3` files. New measured duration **13.61s** (ffprobe: 13.608s) vs the old `actual_duration_s` of **14.232s** — a 0.62s shrink, over the ~0.3s retime threshold.
- **Retiming (B01)**: landscape `scenes.py` plays sum to 2.1s → wait changed 12.132s → **11.51s** (13.608 − 2.1). Vertical `vertical/scenes.py` plays sum to 1.8s → wait changed 12.132s → **11.81s** (13.608 − 1.8).
- **On-screen credit**: `scenes.py` B01 name tag and B08 tagline changed to "Sai Pranavi J."; `vertical/scenes.py` B01 name tag changed the same way. `vertical/scenes.py` B08's tagline was previously hard-wrapped `"in for Sai Pranavi\nJeedigunta"` across two lines — changed to a single line `"in for Sai Pranavi J."`.
- **Layout regression caught and fixed**: the shorter single-line B08 vertical tagline shrank `content.height`, which shrank the auto-sized bordered frame enough to trip GATE V's real `underfill` check (49% < 55% min, confirmed via `./art final vertical --height 3840` — not the review-slate false positive) — a genuine defect, not a tooling artifact. Fixed by increasing the real spacing between the handle/accent/tagline elements (`buff` 1.1 → 1.85 in `vertical/scenes.py`'s `B08_BrandOutro`), which genuinely spreads the real content further apart (same fix philosophy as this fellow's other builds: enlarge/respace real content, not an invisible frame). Re-verified against the real GATE V run: 0 BLOCKER, 0 MAJOR on the rebuilt candidate.
- **Stale-cache avoidance**: deleted `manim/B01.mp4`, `clips/B01.mp4`, `manim/B08.mp4`, `clips/B08.mp4` and the same four paths under `vertical/` before rebuilding (vertical B08 was deleted/re-rendered twice, once for the name text and once more for the spacing fix) — no other beat's cache touched.
- **Rebuild**: `./art run . --height 1080` and `./art run vertical --height 1920` re-rendered only B01/B08 via Manim (GATE A/B CLEAN); both review GATE V runs showed the known review-slate false positive (18/18 frames `edge-bleed`, uniform across every beat including untouched ones). `./art final . --out deliverables/landscape` and `./art final vertical --height 3840 --out deliverables/vertical` rebuilt both true masters (the vertical final initially REFUSED on the real `underfill` finding above; passed clean after the spacing fix). Verified via `stat -f %m` that every regenerated `manim/B01.mp4`/`manim/B08.mp4` (both aspects) postdates its relevant `scenes.py` edit.
- **New master durations**: landscape **107.083s** (was 107.708s), vertical **107.083s** (was 107.708s) — both confirmed true 4K (3840×2160 / 2160×3840).
- **GATE V (final masters, `final_frame_check.py --lenient`)**: landscape **0 BLOCKER, 35 MAJOR**; vertical **0 BLOCKER, 30 MAJOR**. Ship bar (0 BLOCKER) met on both. The MAJOR findings are the same full-continuous-frame-scan sampling artifact (transitional/fade frames across many untouched beats) documented in the sibling 2026-09-14 RAG video's retrofit addendum, not a regression from this change.
- **Manual frame verification**: extracted real frames (ffmpeg) from B01 and B08 in both masters — name tag reads "Sai Pranavi J." cleanly in both aspects; B08 sign-off reads "in for Sai Pranavi J." on one line, fully contained within its bordered card, no clipping, in both aspects.
- **Deliverables renamed**: `deliverables/landscape/AllClearEmailFix_SaiPranaviJeedigunta.mp4` → `AllClearEmailFix_SaiPranaviJ.mp4`, same for `deliverables/vertical/` — copied from the freshly rebuilt masters, sha256-verified identical to `deliverables/landscape/2026-09-22-the-all-clear-that-wasnt-all-there.mp4` / `deliverables/vertical/...-vertical.mp4`, then the old-named files deleted. (No `.verified.json` sidecar existed for the old `ProjectName_...` filenames in this project, so none needed updating.)
- `README.md` name references ("Sai Pranavi Jeedigunta" / "SaiPranaviJeedigunta") updated to "Sai Pranavi J." / "SaiPranaviJ" — no other claims changed.
- Not touched: `FACTCHECK.md`, `SOURCES.md`, `beat_sheet.json` metadata/gates beyond the `narration_text` field.
