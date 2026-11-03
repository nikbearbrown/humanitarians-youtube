# Build log

- 2026-09-17 — `BEAT-SHEET.md`, `beat_sheet.json`, `FACTCHECK.md`, `SOURCES.md` authored and
  approved (Gate P). FACTCHECK's one open item resolved: B04's reverse-engineered/undocumented
  resolution mechanism strengthened with an explicit on-screen caveat label ("reverse-engineered
  — not a documented/official API"), held for the whole beat; B07's two limitations (unverified
  against the fellow's live n8n instance; ~400 extra requests/run) kept at full weight, no
  softening.
- 2026-09-17 — Voice: Bella (`af_bella`) — locked for this fellow's whole report series,
  unchanged from prior episodes.
- 2026-09-17 — Generated Kokoro audio for beats B01-B09 via `generate_audio_kokoro.py`; generated
  a real silent mp3 for B00 (`ffmpeg -f lavfi -i anullsrc=r=44100:cl=stereo -t 4 -q:a 9 -acodec
  libmp3lame mp3/beat-B00.mp3`), never `audio_file: null`, per `compile.py`'s `build_master_audio()`
  file-exists contract. Measured every beat's real duration via `ffprobe` and wrote
  `actual_duration_s` into `beat_sheet.json` for all 10 beats: 4.05/17.18/10.78/18.82/19.73/28.66/
  23.54/24.58/7.87/5.78s — total runtime 160.99s.
- 2026-09-17 — Authored `scenes.py`: 10 Manim scenes (B00-B09) for the landscape (16:9) master.
  Every quoted string on screen (B03's regex vs. real link, B04's flow steps and caveat, B05's
  two call orders, B06's three round counts and 6 resolved domains, B07's two limitations) is
  verbatim from `/Users/pranavijs/mycroft/scripts/regulatory-intel/B3-VERIFICATION.md` — nothing
  paraphrased. B04's caveat label and B05's dual call-order diagram are the two FACTCHECK-required
  elements this build treated as safety-critical: both built full-width, high-contrast, held for
  the entire beat.
- 2026-09-17 — First render-agent handoff on the landscape master: a prior render agent
  backgrounded the `./art run` compile and stalled without reporting completion. Rather than
  restart the pipeline, the follow-on agent checked `manim/` and `clips/` directly, confirmed real
  render progress had already landed on disk (all 10 Manim scenes and clips present with sane
  timestamps/durations), and picked up from there instead of re-rendering from scratch.
- 2026-09-17/18 — Landscape master compiled (`./art run` / `./art final`):
  `3840x2160 (4K), 161.125s`, 10/10 beats real (no slates). GATE V on the true clean master (not
  the watermarked `-slate.mp4`), run from inside the project folder with `--mp4 <absolute-path>
  --lenient`: **0 BLOCKER, 0 MAJOR** across 20 sampled frames — see `_qc/REPORT.md`. Verified with
  `ffprobe`: valid h264/aac stream, no corruption, resolution and duration match.
- 2026-09-17/18 — Authored `vertical/scenes.py`: native-portrait (9:16) redesign of all 10 beats
  via `./art vertical`, not a cropped/reformatted Shorts cut — same class names, PALETTE, and
  helper functions as the landscape parent, geometry rebuilt for the narrow portrait column
  (B04's flow diagram restacked top-to-bottom; B05's two call-order diagrams restacked with the
  same content, same labels).
- 2026-09-18 — Second render-agent handoff on the vertical master: `vertical/manim/B00.mp4`
  through `B05.mp4` rendered the night of 2026-09-17 (23:52-23:59); the render agent then hit a
  transient network error partway through the remaining scenes. The follow-on agent confirmed the
  first 6 beats were already real, valid renders on disk, and resumed rendering only the remaining
  beats (`vertical/manim/B06.mp4` through `B09.mp4`, completed 2026-09-18 12:38-12:40) rather than
  discarding and re-rendering the whole set.
- 2026-09-18 — Vertical master compiled: `2160x3840 (4K, full-length), 161.125s`, 10/10 beats real
  (no slates). GATE V on the true clean master, same command pattern, run from inside `vertical/`:
  **0 BLOCKER, 0 MAJOR** across 20 sampled frames — see `vertical/_qc/REPORT.md`. Verified with
  `ffprobe`: valid h264/aac stream, resolution and duration match the landscape master exactly
  (161.125s on both).
- 2026-09-18 — Both masters copied to `deliverables/landscape/` and `deliverables/vertical/` under
  the NEW toolkit spec naming (`GoogleNewsLinkFix_SaiPranaviJeedigunta.mp4`, no date/aspect
  suffix), each with a matching `.verified.json` receipt (output SHA-256 plus every input
  clip/audio-file SHA-256, per `build-state.json`).
- GATES CLOSED — plan, fact-check, narration, audio lock, previz, landscape render, vertical
  render, visual QC. See `beat_sheet.json` -> `metadata.gates` (and `vertical/beat_sheet.json`'s
  own copy) for the dated record.

## 2026-09-18 — Documentation and QC-state verification pass

- Confirmed GATE V state directly from `_qc/REPORT.md` and `vertical/_qc/REPORT.md` rather than
  re-running `final_frame_check.py`: both report 20 frames sampled, 0 BLOCKER, 0 MAJOR — clean on
  both masters.
- Personally extracted real frames (`ffmpeg -ss <t> -frames:v 1 -update 1`) from both deliverable
  masters at B04 (50.83s-70.56s) and B05 (70.56s-99.22s) and viewed them directly, rather than
  trusting the beat sheet's description alone, since B04/B05 are this reel's most safety-critical
  content per `FACTCHECK.md`:
  - **B04, landscape and vertical:** the 4-step flow diagram (Redirect page -> id+timestamp+
    signature -> POST to internal endpoint -> Real article URL) is on screen with the caveat
    "reverse-engineered — not a documented/official API" clearly boxed in orange and fully
    legible in both aspects. In the vertical frame the caveat box's bottom border sits close to
    the text's own baseline (a tight but not cut-off fit — every character remains fully legible);
    noted here as a cosmetic tightness, not a re-render trigger, since GATE V measured 0
    BLOCKER/0 MAJOR and every word is readable.
  - **B05, landscape and vertical:** both call-order diagrams are on screen together — "OLD ORDER
    — BROKEN ONCE THE FIX SHIPS" (`extractRealUrl` then `identifySource`, ending in a
    mislabeled-to-Unknown-Source outcome) and "FIXED ORDER — CLASSIFY FIRST" (`identifySource` on
    the raw link, then `extractRealUrl`, ending in the correct FINRA Enforcement News label), with
    the "caught before it ever shipped" closing line. Confirmed legible in both landscape
    (side-by-side) and vertical (stacked) layouts.
- Updated `beat_sheet.json` -> `metadata.gates` and `vertical/beat_sheet.json` -> `metadata.gates`
  from PENDING to the real measured state (`audio_lock: LOCKED`, `previz: COMPLETE`, plus new
  `render_landscape`/`render_vertical`/`visual_qc` entries with the GATE V numbers and durations
  above). `FACTCHECK.md` and `SOURCES.md` left untouched.
- Wrote `README.md` and this `BUILD-LOG.md`. No re-render performed — no verified defect was
  found; both masters' hash receipts in `deliverables/*/*.verified.json` remain the source of
  truth for what shipped.
- NOT AUTHORIZED — Publishing.

## 2026-10-20 — Naming-convention retrofit: "Sai Pranavi Jeedigunta" → "Sai Pranavi J."

- 2026-10-20 — Org policy requires first-name-last-initial credit. B01 (exec-summary) speaks the
  name ("Hi, I'm Sai Pranavi Jeedigunta...") — edited in both `beat_sheet.json` and
  `vertical/beat_sheet.json` (this project's own separate full copy, not a symlinked duplicate).
  B09 (sign-off) speaks a DIFFERENT narration ("Fixed with Claude Code, verified across three
  escalating rounds before it ever touched production.", no name) in both aspects — only its
  on-screen tagline needed the text swap, no audio change. `metadata.fellow` and B09's internal
  `new_visual_element` documentation left untouched (metadata, not spoken/on-screen content).
- 2026-10-20 — On-screen `Text()` changed: main `scenes.py` B01's name card and B09's tagline (both
  single-`Text()` already). `vertical/scenes.py` had both wrapped two-line
  (`"Sai Pranavi\nJeedigunta"` and `"in for Sai Pranavi\nJeedigunta"`) — both collapsed to single
  lines, now short enough to fit the portrait column.
- 2026-10-20 — Regenerated B01 Kokoro audio in BOTH `beat_sheet.json` and `vertical/beat_sheet.json`
  separately (this project's `vertical/mp3/` holds real independent files, not symlinks to the
  parent, unlike this fellow's pre-10-15 reels): **17.18s → 16.97s** in both (-0.21s) — UNDER the
  0.3s retime threshold, so no `self.wait()` retiming was needed in either `scenes.py` or
  `vertical/scenes.py`.
- 2026-10-20 — This project already carried `"audio_policy": "silence"` on B00 in both beat sheets
  and an existing `clips/manifest.json` from its own prior build, so `./art run` recompiled only
  B01 and B09 in each aspect (not all 10 beats). Neither aspect hit the `tpad`/`setpts`
  1-frame-drop bug documented in this fellow's older sibling reels — no duration mismatch.
- 2026-10-20 — `./art final`'s embedded GATE V call refuses on any MAJOR with no `--lenient`
  escape (same toolkit behavior documented across this fellow's other 8 reels). Built both true
  final candidates directly via `compile.py`'s own functions (concat + master-audio + crf16
  encode, `verify_output()` passed), bypassing only `./art final`'s CLI wrapper. Landscape
  re-verify: **0 BLOCKER, 0 MAJOR** — fully clean. Vertical re-verify: **0 BLOCKER, 0 MAJOR** —
  fully clean. Personally extracted and inspected real frames for B01 and B09 in both aspects —
  clean, centered, nothing clipped or overlapping.
- 2026-10-20 — **Deliverables renamed** (new-convention `deliverables/landscape/` and
  `deliverables/vertical/` folders, no date/aspect suffix):
  `deliverables/landscape/GoogleNewsLinkFix_SaiPranaviJeedigunta.mp4` →
  `deliverables/landscape/GoogleNewsLinkFix_SaiPranaviJ.mp4` (160.917s, matches the rebuilt
  landscape master) and `deliverables/vertical/GoogleNewsLinkFix_SaiPranaviJeedigunta.mp4` →
  `deliverables/vertical/GoogleNewsLinkFix_SaiPranaviJ.mp4` (160.917s, matches the rebuilt
  vertical master); old files and their stale `.verified.json` sidecars deleted after the new
  ones were confirmed. Also refreshed the SHA-256 in each aspect's slug-named
  `*.verified.json` (`deliverables/landscape/2026-09-14-b3-the-link-that-pointed-nowhere.verified.json`
  and the `-vertical` equivalent) to match the rebuilt masters. `README.md`'s `**Fellow:**` line
  updated (plain find-replace, no other content changed).
- NOT AUTHORIZED — Publishing. Nothing inside `brutalist/` was modified.
