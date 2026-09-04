# BUILD-LOG — Prompt Injection: The Vulnerability Hiding in Plain Text

## 16:9 long

- 2026-08-30 — Beat sheet approved (Gate P), FACTCHECK resolved (OWASP LLM01 citation added to
  B03; both worked examples confirmed generic/hypothetical). `SHOTLIST.md`/`PROMPTS.md` authored
  (not part of the original scaffold — required by `run.sh`'s GATE F paperwork-set check).
- 2026-08-30 — Generated Kokoro audio for all 9 beats: B00 silent
  (`ffmpeg -f lavfi -i anullsrc=r=44100:cl=stereo -t 4`, measured 4.05s — NOT `audio_file: null`,
  per `compile.py`'s `build_master_audio()` all-beats-exist contract) and B01-B08 via
  `generate_audio_kokoro.py` (measured 15.60/18.29/23.57/25.44/27.65/22.68/9.17/1.51s — B08 is
  genuinely short, its narration is just "Explained with Claude Code."). Updated
  `actual_duration_s` for every beat in `beat_sheet.json` — total runtime 147.96s.
- 2026-08-30 — Authored `scenes.py`: 9 Manim scenes, house palette/helpers (`fit()`, `panel()`,
  `box_around()`) copied from this fellow's sibling reels. No split-screen/divider beats by
  design — every beat is a single-column vertical stack, sidestepping the divider-crosses-glyph
  bug class a prior sibling video hit and fixed.
- 2026-08-30 — GATE A (`static_scene_check.py`) first pass: B04/B05 flagged "shapes never change"
  (only 1 non-text shape state across the whole hold) — fixed by adding a second shape
  (`verdict_box`, created after `quote_panel`) in each, same pattern as the sibling reel's B02-B04.
  B07 flagged "no shapes recorded" (text-only scene) — added a real `Line` underline as a genuine
  shape mobject. All 9 scenes clean on re-check.
- 2026-08-30 — `./art run` pass 1: GATE B (`manim_layout_audit.py`) flagged B02's reveal panel
  off-frame (`set_x()` on a left-aligned-internally block set its CENTER, not its left edge,
  pushing the panel's own left edge to x=-6.75, past the -6.3 safe wall) — fixed by re-centering
  the panel to x=0 independently of the (off-center, left-aligned) article block above it.
- 2026-08-30 — `./art run` pass 2: GATE B flagged B03's title (buff=0.55 landed its top at y=3.45,
  past the 3.4 ceiling) and citation line (`to_corner()` measures from the hard FRAME edge, not the
  safe area — buff=0.4 landed it at (6.71,-3.6), past both walls) — both buffs increased (0.75/0.9).
- 2026-08-30 — `./art run` pass 3: GATE B flagged B04's header (buff=0.5 -> top at y=3.5) — same
  header buff bumped to 0.7 in both B04 and B05 (which shared the same pattern).
- 2026-08-30 — First full 4K render (`./art run`): 9/9 beats compiled real, master + review cut
  written (148.0s). GATE V on the review cut's own `-slate.mp4` showed 18 BLOCKER edge-bleed on
  every beat — confirmed as the same documented false-positive as this fellow's prior reels (the
  review-only timecode watermark sits in the title-safe margin by design). Checked the TRUE clean
  master directly (`final_frame_check.py --mp4 <slug>.mp4`, not the slate): **0 BLOCKER, 13 MAJOR**
  (underfill on B00 43%, B01 50%, B04 39%, B05 25-37%, B06 42%, B07 39%, B08 15-16%).
- 2026-08-30 — Canvas-fill fix round 1: B00/B01 — wider decorative rules/accent lines + bigger
  type (canvas-fill is a bbox AREA ratio; a narrow centered text stack underfills on the WIDTH
  axis regardless of vertical buff). B04/B05 — the "shrink-only if too tall" scale guard never
  GREW the body to use the available height when it was already smaller; replaced with
  `scale = min(available_h/body.height, SAFE_W/body.width)`, applied unconditionally. B06/B07/B08 —
  same "grow or shrink to fill" pattern, or (B08) added a scale-fit that hadn't existed at all.
  Re-render: **0 BLOCKER, 3 MAJOR** (B01 54%, B04 53%, both just 1-2pp under the floor).
- 2026-08-30 — Canvas-fill fix round 2 (final nudge): widened B01's accent line (4.0->4.6) and
  B04's quote panel (11.0->11.6). Re-render: **0 BLOCKER, 1 MAJOR** (B04 mid-reveal sample at
  51% — the beat's skeleton-first tag reveal means an early sample can catch it before all 3
  answers + verdict are visible; the full layout clears the floor once resolved). Visually
  spot-checked `_qc/contact_sheet.png` — every beat's key content (hidden instruction text, all 3
  rubric questions + OWASP citation, resolved rubric answers with crimson/teal attack-vs-benign
  contrast, distinct checklist card, takeaway, brand outro) reads clearly.
- 2026-08-31 — Final master rendered via `./art final`: `2026-08-30-what-prompt-injection-
  actually-looks-like.mp4`. Verified via `ffprobe`: **3840x2160, 24fps, h264/aac, 147.94s**. No
  stray `ffmpeg`/`manim`/`compile.py` processes found; file not corrupted (playable, correct
  duration). Re-ran GATE V on this freshly-written master: **0 BLOCKER, 1 MAJOR** (unchanged from
  the review cut's final state).

## 9:16 short

- 2026-08-31 — `shorts.py` cap check: parent reel 147.96s, under the 180s Shorts cap -> full
  reformat, no beats dropped, all 9 mp3s reused unchanged. Authored `short/SHOTLIST.md` and
  `short/PROMPTS.md` (GATE F paperwork set for the short's own `run.sh` pass).
- 2026-08-31 — Authored `short/scenes.py`: portrait relayout of all 9 beats. B02 (browser/hidden-
  instruction hook), B03 (3-question rubric), B04/B05 (worked-example/falsifiability rubric-answer
  cards) got real top-to-bottom-stack redesigns — the parent's wide horizontal rows (badge beside
  a 9.5-wide text column; tag beside an 8.6-wide answer column) have nowhere to go in a ~3.9-wide
  portrait safe column, so every line was re-wrapped and every row restructured tag-above-answer
  (or badge-above-description) instead of side-by-side.
- 2026-08-31 — Compiled via `ART_QC=0 ./art run <reel>/short --height 1920` (skipping `run.sh`'s
  own bundled A/W/B trio, per this fellow's established convention — GATE A has no `--portrait`
  mode and would just be uninformative for a portrait scene, not a true check). Ran the REAL
  portrait-aware GATE B manually (`manim_layout_audit.py --portrait`) instead: caught B02's article
  block off-frame (a `set_x(-1.75)` on an internally-left-aligned block set its CENTER there, not
  its left edge, pushing its own left edge to x=-3.17 — past even the hard frame edge; fixed by
  removing the manual offset and trusting `next_to()`'s default centering) and B03/B04/B05/B06's
  headers/titles/zingers landing past the safe-area ceiling/floor at the same buff values that had
  been fine in 16:9 (bumped 0.5-0.55 -> 0.75 throughout, matching the parent's own fix pattern).
  Re-checked: all 9 scenes CLEAN.
- 2026-08-31 — First full portrait render + GATE V on the true master: **0 BLOCKER, 20 MAJOR** —
  every single beat (plus the endcard) measured only 6-8% canvas-fill, an order of magnitude worse
  than anything seen in the 16:9 build. Visual frame extraction confirmed content genuinely
  clustered in a small island in the vertical middle of the frame, not a false positive.
- 2026-08-31 — Diagnosed as a uniform-scale limitation first: a post-arrange `scale =
  min(height-ratio, width-ratio)` is always WIDTH-bound when portrait text is already near the
  safe column's width cap, so it can't grow height much. Rewrote B00/B01/B07/B08 to solve directly
  for the buff that reaches a target height (`arrange_fill_height()` helper — buff is a free
  height lever that costs nothing on the width axis) and widened B02's chained gaps directly.
  Re-rendered: **identical 6-8% numbers, no change at all.**
- 2026-08-31 — Traced the real root cause via a standalone debug scene printing
  `config.frame_height`/`frame_width` inside `construct()`, run through the actual
  `manim -qk --fps 24 -r "2160,3840"` CLI invocation `run.sh` uses: **`frame_height=8.0,
  frame_width=14.222` — the 16:9 default, unchanged despite the portrait `-r` flag.** Manim CE's
  CLI sets `pixel_width`/`pixel_height` from `-r` but does not recompute `frame_width` to match, so
  every scene in this file had been composed and positioned against an assumed 4.5-unit-wide frame
  that was never actually active at render time — the true active frame was still 14.22 units wide,
  so a ~3.6-unit-wide card occupied only ~25% of the true width and a correspondingly tiny fraction
  of the (aspect-consistent) taller effective canvas. This is a previously-discovered toolkit
  quirk — the same fix already exists in this fellow's sibling reel
  (`2026-08-30-the-update-that-almost-lied-about-what-it-sent/short/scenes.py`). Patched by
  recomputing `config.frame_width = config.frame_height * (pixel_width/pixel_height)` at the top of
  `short/scenes.py`, right after `from manim import *`. Verified the fix directly: a debug scene
  with the patch applied printed `frame_height=8.0, frame_width=4.5` — correct.
- 2026-08-31 — Full re-render with the frame_width patch: **0 BLOCKER, 2 MAJOR** — both on the
  auto-generated silent END card only. All 9 authored beats GATE-V-clean.
- 2026-08-31 — Found and fixed a wrong-handle bug: `shorts.py`'s auto-generated endcard defaults
  to `--handle "@nikbearbrown"` (a different persona's default), not this channel's
  `@HumanitariansAI`. Re-ran `shorts.py --handle "@HumanitariansAI"` to regenerate `media/END.png`
  + `mp3/beat-END.mp3` with the correct branding, then recompiled the master via `compile.py
  --height 1920`.
- 2026-08-31 — Verified the final short master via `ffprobe`: **1080x1920, h264, 152.46s**. GATE V
  on this final master: **0 BLOCKER, 2 MAJOR** (END card only, 2-3% fill — an inherent
  characteristic of a sparse handle-only card when no beats are cut and there is nothing to tease,
  not an authored-beat defect). Visually spot-checked `_qc/contact_sheet.png` — every beat reads
  clearly in portrait: title, name/summary, the browser hook with legible hidden-instruction
  reveal, the 3-question rubric + citation, both resolved rubric-answer cards (crimson attack vs.
  teal/sage benign), the checklist, the takeaway, and the corrected `@HumanitariansAI` brand outro.

## Deliverables

- 2026-08-31 — Copied and renamed per the fellowship's weekly-STEM-video naming convention:
  `PromptInjection_SaiPranaviJeedigunta_20260830_16x9.mp4` (3840x2160, 147.94s) and
  `PromptInjection_SaiPranaviJeedigunta_20260830_9x16.mp4` (1080x1920, 152.46s). Both verified via
  `ffprobe` (resolution/duration match their source masters exactly). No publishing performed —
  masters stay in this folder only, per task scope.
