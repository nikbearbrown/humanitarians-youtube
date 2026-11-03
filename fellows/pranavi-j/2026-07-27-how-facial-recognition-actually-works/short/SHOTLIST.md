# SHOTLIST — How Facial Recognition Actually Works (SHORT, 9:16)

Derived 2026-08-26 from the parent 16:9 reel via `runtime/scripts/shorts.py`.
Parent: 185.3s / 12 beats, ~5.3s over the 180s Shorts cap.

Auto-plan history: the FIRST auto-plan (no flags) proposed dropping B07
(EVIDENCE, 31.27s) — the single longest beat, but also the video's factual
backbone (the NIST FRVT demographic-accuracy findings). Re-ran with
`--keep B07` to protect it; the planner's next-best cut was B09
(WORKED-EXAMPLE, 26.86s), landing at ~179.0s — under the cap. Kept.

## ~170.0s (measured, all beats' actual mp3 durations + endcard) · 11 beats kept, 1 dropped

| Beat | Act | Medium | Source/Pattern | Duration | Notes |
|---|---|---|---|---|---|
| B00 | TITLE | manim | B00_TitleCard (short/scenes.py) | 4.60s | Silent title card, reuses parent's silent mp3. Narrowed rules/fit widths for portrait. |
| B01 | INTRO | manim | B01_ExecSummary (short/scenes.py) | 11.66s | Reuses parent's mp3. Narrowed fit widths; summary re-wrapped 2->3 lines. |
| B02 | HOOK | manim | B02_EverywhereHook (short/scenes.py) | 15.48s | Reuses parent's mp3. Context chips: horizontal row -> vertical column. |
| B03 | FRAMEWORK | manim | B03_FrameworkLens (short/scenes.py) | 11.81s | Reuses parent's mp3. Lens rows recentered (were off-frame at LEFT*4.6); gradient bar shrunk 8.4->3.0. |
| B04 | MECHANISM | manim | B04_PipelineMechanism (short/scenes.py) | 21.12s | Reuses parent's mp3. Pipeline: horizontal row of 4 boxes -> vertical column, arrows now point DOWN. Full redesign. |
| B05 | BENEFITS | manim | B05_LegitimateUses (short/scenes.py) | 15.14s | Reuses parent's mp3. Re-indented list, items re-wrapped to 2 lines each. |
| B06 | HARMS | manim | B06_HarmfulUses (short/scenes.py) | 12.38s | Reuses parent's mp3. Same treatment as B05. |
| B07 | EVIDENCE | manim | B07_NistEvidence (short/scenes.py) | 31.27s | Reuses parent's mp3. **Protected via --keep** (factual backbone). Two vertical side-by-side bars -> two horizontal bars stacked vertically. Full redesign. |
| B08 | FRAMEWORK-CALLBACK | manim | B08_FluencyTrap (short/scenes.py) | 12.77s | Reuses parent's mp3. Split panel: side-by-side (LEFT/RIGHT, ~4.4 units wide each) -> stacked top/bottom. Full redesign. |
| B09 | WORKED-EXAMPLE | — | — | 0s (DROPPED) | Cut by the auto-plan (protected B07 instead) to fit the 180s cap. No scene authored — the beat is not in this short. |
| B10 | CTA | manim | B10_YourTurn (short/scenes.py) | 17.30s | Reuses parent's mp3. Re-indented checklist, 2nd/3rd questions wrapped to 2 lines. |
| B11 | SIGN-OFF | manim | B11_BrandOutro (short/scenes.py) | 11.95s | **Narration REWRITTEN** by shorts.py (was 4.92s "in for..." sign-off; now explains what B09 covered and points to the long). Same brand card, narrowed, self.wait() re-tuned to the new duration. |
| END | — | card (silent) | media/END.png | 4.5s | Silent branded endcard, "Next:" line = the worked-example teaser text (--next override), handle @HumanitariansAI. |

## Geometry note (why every beat's scene.py class differs from the parent, not just a resize)

Manim's `frame_height` stays fixed at 8 units regardless of aspect ratio —
only `frame_width` shrinks for a narrower canvas (at 1080x1920, frame_width
is ~4.5 units vs. ~14.2 at 16:9). So every beat needed at minimum a
narrower-fit pass, and 4 beats needed a genuine structural redesign because
their parent layout was horizontal (arrange(RIGHT) or LEFT*n/RIGHT*n splits
wider than the real ~4.5-unit portrait frame):
- B02 (context chips: row -> column)
- B04 (pipeline diagram: row of 4 boxes -> vertical column, arrows DOWN)
- B07 (NIST bars: two vertical bars side-by-side -> two horizontal bars stacked)
- B08 (fluency-trap panel: side-by-side split -> stacked top/bottom)

## QC plan
Same gates as the parent (GATE A static pre-flight, GATE W WCAG/margin,
GATE B post-render layout audit, GATE V frame-level on the compiled cut) —
run with `ART_PALETTE=humanitarians` exported (this reel's palette; GATE W
defaults to `teardown` otherwise). GATE V is checked against the TRUE clean
master (`--mp4 short/<slug>.mp4`), never the `-slate.mp4` watermarked review
cut — that cut's timecode watermark produces a known false-positive
edge-bleed BLOCKER on every frame (documented in the parent reel's own
BUILD-LOG.md, confirmed again here).

IMPORTANT: GATE W's static margin check (`wcag_margin_check.py`) hardcodes
a 16:9 half-width (FRAME_X=7.1) regardless of `aspect_ratio` in
beat_sheet.json — it will not flag a mobject that overflows the real
~2.25-unit portrait half-width as long as it stays under its own 7.1
assumption. Every beat in `short/scenes.py` was hand-verified to stay
within a self-imposed x in [-2.0, 2.0] safe zone, confirmed against real
extracted frames (`ffmpeg -ss` sampling of the rendered mp4s), not by GATE
W alone.
