# Build log

- 2026-08-31 — `BEAT-SHEET.md`, `beat_sheet.json`, `FACTCHECK.md`, `SOURCES.md` authored and
  approved (Gate P). Both FACTCHECK open items resolved: B06's "deliberate tradeoff" framing kept
  as drafted (no wording change); the "eighteen" count confirmed fine stated plainly (no on-screen
  date qualifier needed, same pattern as prior reports' live-snapshot counts).
- 2026-08-31 — Voice: Bella (`af_bella`) — locked for this fellow's whole report series, unchanged
  from the 3 prior episodes.
- 2026-09-07 — Generated Kokoro audio for beats B01-B08 via `generate_audio_kokoro.py`; generated
  a REAL silent mp3 for B00 (`ffmpeg -f lavfi -i anullsrc=r=44100:cl=stereo -t 4 -q:a 9 -acodec
  libmp3lame mp3/beat-B00.mp3`), never `audio_file: null`, per `compile.py`'s `build_master_audio()`
  file-exists contract. Measured every beat's real duration via `ffprobe` and wrote
  `actual_duration_s` into `beat_sheet.json` for all 9 beats: 4.05/15.02/9.98/21.67/25.25/22.70/
  20.69/8.02/4.22s — total runtime 131.6s.
- 2026-09-07 — Authored `scenes.py`: 9 Manim scenes (B00-B08), same PALETTE/MONO/`fit()`/`panel()`/
  `clear_of_divider()`/`box_around()` helpers as this fellow's closest sibling reel
  `2026-08-30-the-check-that-never-once-fired` (part 3 of the same Layer-1-hardening series; this
  reel is part 4) for house-style consistency. Every quoted string on screen (B03's XML fields,
  B04's two titles, B05's 5-feed table, B06's two example titles) is verbatim from
  `/Users/pranavijs/mycroft/scripts/regulatory-intel/UNKNOWN-SOURCE-INVESTIGATION.md` — nothing
  paraphrased. B03 (Federal Register `dc:creator` vs. Google News `<source>`) and B04 (recoverable
  vs. not-recoverable title) are this reel's side-by-side beats, using `clear_of_divider()` and
  verified against real measured Manim object bounds. B06's framing is FACTCHECK-locked: "LEFT
  OPEN -- BY DESIGN" — a deliberate, reasoned stopping point, never an unsolved bug or a "coming
  soon" promise.
- 2026-09-07 — Added `SHOTLIST.md` and `PROMPTS.md` (GATE F paperwork set; this reel needs no
  pantry assets — all 9 beats are self-contained Manim).
- 2026-09-07 — GATE A (`static_scene_check.py`) + GATE W (`wcag_margin_check.py --palette
  humanitarians`) run on all 9 scenes before any render. Found 1 real GATE A error: B06 had only 1
  distinct non-text shape-state across the hold ("shapes never change" repeated-animation check) —
  fixed by adding a `caption_underline` Line created later than `stamp_box`, same pattern as this
  fellow's sibling reels' B02/B03/B04. B07's benign "no shapes recorded — scene may be text-only"
  warning is expected for a pure statement card (same as every sibling reel's own B07), non-
  blocking. All other 8 scenes GATE A/W clean on the first pass.
- 2026-09-07 — First full 4K render (`./art run`): 9/9 beats compiled real (no slates). GATE V on
  the true clean master (not the watermarked `-slate.mp4`, which reproduces a known false-positive
  edge-bleed from its own timecode watermark): first pass **0 BLOCKER, 6 MAJOR** — real underfill
  defects, not the watermark artifact:
  - **B00 (title card):** measured only 36% canvas-fill (well under the 55% floor) — a 3-line
    title (longer than the sibling's 2-line title) with a tight 0.55 buff between rule/title/handle
    groups left too much empty safe area. Fixed with real measurement: font_size 68->84, rule
    half-width 3.4->4.2, VGroup buff 0.55->1.5 — but that first fix pushed the handle text OFF
    FRAME (GATE B caught `@HumanitariansAI` bottoming out at y=-4.17, past the -4.0 hard edge).
    Re-measured and reduced buff to 0.95, which cleared both the out-of-frame error and the
    underfill floor.
  - **B06 (honest limit):** measured 39% canvas-fill — a narrow single-column stack of short lines
    left too much empty safe-area width. Fixed with larger fonts (labels 25->27, examples 26->30,
    note 20->22) and wider inter-block buffs; re-measurement then caught the header top edge at
    y=3.45 (past the 3.4 safe ceiling) from the buff reduction elsewhere, fixed with a final
    header buff of 0.68 (then 0.62 in the short).
  - **B07 (takeaway):** measured 34% canvas-fill — line3's long sentence was scaled down hard by
    `fit()`'s width cap, shrinking its height contribution, and a 0.7 buff left the group too
    short overall. Fixed by shortening line3 ("Know exactly where to stop — and say so.") and
    using the sibling reel's own tuned recipe (font_size 54/56/38 buff 1.4), then pushed further
    (58/62/40, buff 2.0) once GATE V's second pass still measured 47% (under the floor).
  - Re-ran GATE A/W/B (via the fast `manim_layout_audit.py` low-quality dry-run) after each fix;
    all 3 scenes clean before recompiling.
- 2026-09-07 — Second full 4K render + GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**
  across all 18 sampled frames. Visually spot-checked `_qc/contact_sheet.png` — title card,
  exec-summary, the 18-item hook grid, the `dc:creator`/`<source>` field comparison, the two real
  title examples, the 5-feed results table, the "LEFT OPEN -- BY DESIGN" framing, and the takeaway
  statement all read clearly.
- 2026-09-07 — **Final master rendered** (`./art final`): `3840x2160 (4K), 131.58s`, verified with
  `ffprobe` (valid h264 stream, no corruption). GATE V on this true final master (run from inside
  the reel folder, `--mp4 <absolute-path>` explicit, `--lenient`): **0 BLOCKER, 0 MAJOR** across 18
  sampled frames.
- GATES CLOSED — plan, fact-check, narration, audio lock, previz, 16:9 render, visual QC. See
  `beat_sheet.json` -> `metadata.gates` for the dated record.

## 2026-09-07 — 9:16 Shorts derivative built (`short/`)

- `short/beat_sheet.json` and `short/scenes.py` scaffolded via `runtime/scripts/shorts.py` per THE
  SHORTS LAW: at 131.6s this reel is **under** the 180s Shorts cap, so the whole reel reformats
  16:9 -> 9:16 as-is — **0 beats dropped**, every beat's mp3 reused unchanged (symlinked from the
  parent's `mp3/`), plus a silent branded endcard (`media/END.png` + `mp3/beat-END.mp3`, 4.5s).
- `short/scenes.py` hand-authored: 9 portrait (1080x1920) Manim scenes, same class names/PALETTE/
  MONO/`fit()`/`box_around()` helpers as the parent, same per-beat animation timing (every
  `self.play`/`self.wait` matching the parent beat-for-beat, since the audio is identical) — only
  the geometry redesigned for the narrow portrait column. 3 real top/bottom-stack (or one-column
  mini-card) redesigns, as this build calls out: **B03** (Federal Register/Google News field
  comparison: parent's LEFT/RIGHT split -> portrait TOP/BOTTOM stack), **B04** (recoverable/
  not-recoverable titles: parent's LEFT/RIGHT split -> portrait TOP/BOTTOM stack), **B05**
  (five-feed results table: parent's 4-column table -> one mini-card per feed + a total row,
  stacked) — each using the file's own `clear_of_hdivider()` helper (the rotated analogue of the
  parent's `clear_of_divider()`). Added `short/SHOTLIST.md`; `short/PROMPTS.md` symlinked to the
  parent's (no pantry assets needed).
- GATE A (`static_scene_check.py`) + GATE W (`wcag_margin_check.py --palette humanitarians`) run on
  all 9 portrait scenes before any render: all 9 clean (B07's benign text-only warning, same as the
  16:9 parent, non-blocking).
- Ran the real portrait-aware GATE B (`manim_layout_audit.py --portrait --curve-strict`) per class
  manually before compiling — this is the authoritative pixel-true check for portrait geometry.
  Iterating against it (not eyeballing) caught 3 real layout bugs, each fixed and re-verified clean:
  - **B02 (unknown-source hook):** the closing caption ran past the safe floor (measured bottom
    y=-3.61, past -3.4). Fixed by tightening the grid/stamp/caption buffs (0.4/0.4/0.3 ->
    0.3/0.3/0.22) and trimming font sizes slightly.
  - **B05 (fix + proof table):** `--curve-strict` flagged "383 items" sitting on a curve — the
    gold `box_around()` padding (0.14) around the "18 -> 8" total exceeded the original 0.08 gap
    between it and "383 items" above it, so the box's own top stroke intruded into the text above.
    Fixed by widening that internal gap to 0.3 (comfortably more than the box's own padding).
  - **B06 (honest limit):** the closing caption ran past the safe floor (measured bottom y=-3.55).
    Fixed by tightening the header/categories/stamp/caption buffs; a follow-up pass then caught the
    header itself crossing the safe ceiling (y=3.5) from the tightened top buff, fixed with a
    final header buff of 0.62.
  - Re-ran GATE A/W/B after each fix; all 9 scenes clean before compiling.
- Compiled via `./art run <reel>/short --height 1920` (the bundled GATE A/W/B trio ran clean in
  portrait mode without needing the `ART_QC=0` workaround some sibling shorts required). 10/10
  slots filled (9 Manim beats + 1 STILL endcard), master + review cut written at 1080x1920, 136.1s.
- GATE V on the TRUE clean master (`final_frame_check.py . --mp4 <absolute-path> --lenient`, run
  from inside `short/`, not the watermarked `-slate.mp4`): first pass **0 BLOCKER, 4 MAJOR** — 2
  real (B08 measured exactly at the 55% floor, a marginal fail from float rounding) and 2 on the
  toolkit's own auto-generated silent END card (non-fixable without editing `brutalist/`, same
  documented exception as this fellow's sibling shorts).
  - **B08 fix:** bumped font sizes (62/34 -> 70/38) and buff (1.3 -> 1.55), re-verified clean via
    `manim_layout_audit.py --portrait --curve-strict`, cleared the stale `manim/B08.mp4` slot, and
    recompiled.
- Final GATE V result on the true short master (`--lenient`): **0 BLOCKER, 2 MAJOR** — both
  remaining on the toolkit's own auto-generated silent END card (a PIL-drawn branded card produced
  by `shorts.py`'s `endcard_png()`, fixed layout, not one of this reel's 9 Manim scenes and not
  editable without touching `brutalist/`, out of scope per this task) — **0 BLOCKER, 0 MAJOR on
  all 9 authored Manim beats (B00-B08)**, same outcome as this fellow's sibling shorts.
- Verified the final short master via `ffprobe`: **1080x1920, h264/aac, 136.1s**. Visually
  spot-checked `short/_qc/contact_sheet.png` — title card, exec-summary, the restacked 18-item
  hook grid, the stacked field-comparison redesign, the stacked recoverable/not-recoverable
  titles, the stacked five-feed mini-cards + total, the "LEFT OPEN -- BY DESIGN" framing, and the
  takeaway statement all read clearly in portrait.
- Short master: `short/2026-09-07-the-synonyms-the-classifier-never-learned-short.mp4` — 1080x1920,
  136.1s, 10/10 real beats, 0 BLOCKER / 0 MAJOR on all 9 authored scenes (2 MAJOR remaining on the
  non-Manim endcard, flagged above).
- NOT AUTHORIZED — Publishing.

## Deliverables renamed (2026-09-07)

- `Mycroft_SaiPranaviJeedigunta_20260907_16x9.mp4` (copy of the 16:9 master, 3840x2160, 131.58s)
- `Mycroft_SaiPranaviJeedigunta_20260907_9x16.mp4` (copy of the 9:16 short master, 1080x1920,
  136.1s)
