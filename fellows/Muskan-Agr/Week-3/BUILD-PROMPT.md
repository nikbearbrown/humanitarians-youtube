# BUILD-PROMPT — "The Audit Can't Choose the Audience." (Week 3 of 4)

Paste into Claude Code from the `brutalist.art-main/` toolkit root:

```
Build the reel "humanitarians-ai-week3-stakeholder-strategy-hierarchy" — a 3-4
minute brutalist project-status video covering Week 3 of the Humanitarians AI
website UX/UI restructure (stakeholder insight strategy, a discussion guide of
open questions, and a structural hierarchy strategy).

Ground truth, read first:
1. reels/humanitarians-ai-week3-stakeholder-strategy-hierarchy/beat_sheet.json
   — 19 beats, narration final. B00 opens "Hello, I am Muskan Agrawal, and
   this video is a summary of ...".
2. .../scenes.py — read BUILD-LOG.md first. Three things are load-bearing and
   must not be "cleaned up": the maroon marks that land with each row (GATE A
   errors on any scene whose shape state never changes), the literal 0.6 in
   to_edge and literal font_size inside construct (GATE W's checker reads them
   off the AST), and chip_below() fitting rather than clamping.
3. .../SHOTLIST.md — the measured coordinate table.
4. .../SOURCES.md — where every number came from.
5. .../DISCUSSION-GUIDE.md — the full 40-question guide; the video shows nine.
6. .../assets/ — Week 1's six screenshots, reused. B04 uses 02, B06 uses 05.

Standing rule: never draw a proposed layout. The site is not shown altered.

Steps:
1. python3 runtime/scripts/generate_audio_kokoro.py reels/humanitarians-ai-week3-stakeholder-strategy-hierarchy
2. ./art run reels/humanitarians-ai-week3-stakeholder-strategy-hierarchy
   GATE A and GATE W were already reproduced in a sandbox against this exact
   scenes.py: 0 blocking errors, 0 warnings, 19/19 WCAG-clean. Any warning is
   new. On a GATE B failure read layout_audit.md for exact coordinates and
   nudge the specific wrong number. Never set ART_QC=0.
3. ./art todo reels/humanitarians-ai-week3-stakeholder-strategy-hierarchy
4. ./art final reels/humanitarians-ai-week3-stakeholder-strategy-hierarchy
   -> renders/humanitarians-ai-week3-stakeholder-strategy-hierarchy.mp4 at the
   TOOLKIT ROOT.
5. ./art shorts ... THEN VERIFY short/manim/ actually contains clips.
6. QC qc-sheet.png for all 19 beats. Confirm the three red boxes in B04 land on
   the three tier cards, the group box in B06 encloses all three buttons, and
   no chip touches an annotation box.
7. Report actual durations into BUILD-LOG.md and update the wps calibration.
   Never publish — local render for review.
```
