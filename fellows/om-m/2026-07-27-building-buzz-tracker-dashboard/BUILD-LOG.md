# Build log

- 2026-07-26 — Full build completed via the brutalist-art toolkit: 19/19 beats filled (4 Remotion
  cards/graphics, 15 real-screenshot stills from `pantry/`), Kokoro voice `am_onyx`, cut = master.
- 2026-07-26 — Revision history per `beat_sheet.json` metadata note: 4 revisions total — dropped
  Ken Burns/zoom motion and a tests beat (rev. 2); locked `fit=pad` (no cropping), consolidated
  imagery (rev. 3); reframed the dashboard beats against prior weeks, split the score-formula beat
  from the workflow beat, and baked title bars into two composite images via Pillow (rev. 4).
- 2026-07-26 — Gate P (pedagogy/narration structure): PASS — see `PEDAGOGY.md` (carried over from
  the original build, unmodified).
- 2026-07-27 — Migrated the necessary source files into this repository (`beat_sheet.json`,
  `PEDAGOGY.md`, small reconstructable assets: `pantry/`, `media/*.png` + `*.source.txt`,
  `clips/_work/*.png`, `clips/{audio.txt,concat.txt,manifest.json,master.m4a}`,
  `mp3/timings.json`). Authored `README.md`, `BUILD-PROMPT.md`, `FACTCHECK.md`, `SOURCES.md` to
  match this repository's fellows-folder convention (see `fellows/maya-r/` for the reference
  shape). Left `TYPECHECK.md` out of this repo copy — not part of any established convention seen
  elsewhere in this repository; available in the original build folder if it should be added.
- OPEN GATE — Author (Om Mali) confirmation of the 13 author-asserted claims in `FACTCHECK.md`.
  These describe a private system nobody else can independently verify.
- NOT AUTHORIZED — Publishing. The rendered MP4 and per-beat audio/video files are intentionally
  not part of this repo copy (see `README.md`); they remain in the original build location.
- 2026-08-01 — Revision 5, via the brutalist-art toolkit: inserted a new executive-summary beat
  ("Hi, I'm Om Mali...", act EXECUTIVE SUMMARY) immediately after the cold open, at the author's
  request, so a first-time viewer gets a stated reason to keep watching before the pipeline
  walkthrough begins. All beats from the former B01 onward renumbered up by one (B01→B02 … B18→B19).
  Narration text was human-drafted, then human-confirmed word-for-word (including a no-dash/no-hyphen
  correction) before Kokoro synthesis — no fabricated content. Kokoro voice `am_onyx` unchanged.
  Re-rendered all 5 Remotion CARD/GRAPHIC beats (B00, B01, B02, B03, B19) since only the 15 STILL
  screenshots were carried into this repo copy, not the CARD mp4s (per the "reconstructable assets"
  note above) — recompiled fresh rather than reused. Recompiled master at 3840x2160 (matching the
  existing spec), 20/20 beats filled, runtime 348.0s (was 331.9s). `Mycroft_OmMali_27_07_2026.mp4`
  replaced in place; the pre-revision file was not retained separately.
- 2026-08-01 — Revision 6, via the brutalist-art toolkit: reversed the opening order at the
  author's request — the video now opens with the personal intro ("Hi, I'm Om Mali...") first,
  then the project cold-open description second. Implemented as a content swap between the B00
  and B01 slots (narration text, card headline/eyebrow, and duration all swapped), not a
  renumbering — B02 onward is unaffected. Both beats' Kokoro narration (`am_onyx`) and Remotion
  cards were regenerated to match their new content (exact durations swapped: B00 16.19s, B01
  14.53s). Recompiled master, 20/20 beats filled, runtime unchanged at 348.0s.
  `Mycroft_OmMali_27_07_2026.mp4` replaced in place again; the pre-revision-6 file was not
  retained separately.
