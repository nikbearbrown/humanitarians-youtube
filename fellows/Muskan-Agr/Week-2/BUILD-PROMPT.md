# BUILD-PROMPT — "Opinions Don't Ship. Numbers Do." (Week 2 of 4)

Paste into Claude Code (or any coding agent) from the `brutalist.art-main/`
toolkit root:

```
Build the reel "humanitarians-ai-week2-typography-hero-concepting" — a 3-4
minute brutalist project-status video covering Week 2 of the Humanitarians AI
website UX/UI restructure (navigation and footer link-level audit, typography
system refinement, WCAG contrast finding, accent-colour discipline, and hero
concepting).

Ground truth, read first:
1. reels/humanitarians-ai-week2-typography-hero-concepting/beat_sheet.json —
   the master. 17 beats, narration final. B00 must open with the presenter
   line "Hello, I am Muskan Agrawal, and this video is a summary of ...".
2. .../scenes.py — every beat's Manim scene. Read BUILD-LOG.md first: it
   records why the ladder rungs carry tick squares (GATE A), why to_edge and
   font_size take literals (GATE W), and why chip_below fits rather than
   clamps (GATE B).
3. .../SHOTLIST.md — the measured coordinate table.
4. .../SOURCES.md — where every on-screen number came from.
5. .../assets/ — the six Week 1 screenshots, reused unchanged.

Steps:
1. Audio (the master clock):
   python3 runtime/scripts/generate_audio_kokoro.py reels/humanitarians-ai-week2-typography-hero-concepting
   Voice: am_onyx. Measure actual_duration_s per beat; scene timings
   auto-retime/freeze-pad to match. Do not hand-edit scene waits to chase it.
2. Draft compile: ./art run reels/humanitarians-ai-week2-typography-hero-concepting
   Renders 17 scenes at 3840x2160 / 24fps and runs GATE A, W, B.
   GATE A and GATE W were already reproduced in a sandbox against this exact
   scenes.py: 0 blocking errors, 7 non-blocking warnings, 17/17 WCAG-clean.
   If GATE B fails, read layout_audit.md for the exact box coordinates and
   nudge the specific number that is wrong. Never set ART_QC=0.
3. ./art todo reels/humanitarians-ai-week2-typography-hero-concepting
4. Clean 4K master: ./art final reels/humanitarians-ai-week2-typography-hero-concepting
   -> renders/humanitarians-ai-week2-typography-hero-concepting.mp4 at the
   TOOLKIT ROOT (no -cut suffix, not inside the reel folder).
5. 9:16: ./art shorts reels/humanitarians-ai-week2-typography-hero-concepting
   THEN VERIFY: short/manim/ must contain clips and a vertical master must
   exist. On Week 1 this step scaffolded short/ and rendered nothing, and the
   miss went unnoticed.
6. QC: eyeball qc-sheet.png for all 17 beats. Confirm the four red boxes in
   B12 land on the four maroon buttons, the B13 area boxes hug the video and
   the message column, and no overlay chip touches an annotation box.
7. Report actual per-beat durations + total runtime back into BUILD-LOG.md,
   and update the words-per-second calibration if it has moved.
   Never publish — this stays a local render for review.
```
