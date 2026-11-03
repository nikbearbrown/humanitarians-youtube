# BUILD-PROMPT — "Move the Part That Isn't Blocked." (Week 4 of 4)

Paste into Claude Code from the `brutalist.art-main/` toolkit root:

```
Build the reel "humanitarians-ai-week4-navigation-cleanup-handoff" — a 3-4
minute brutalist project-status video covering Week 4 of the Humanitarians AI
website UX/UI restructure (navigation and footer link cleanup done with the
developer, plus a four-part design-to-development collaboration framework).

Ground truth, read first:
1. reels/humanitarians-ai-week4-navigation-cleanup-handoff/beat_sheet.json —
   20 beats, narration final. B00 opens "Hello, I am Muskan Agrawal, and this
   video is a summary of ...".
2. .../scenes.py — read BUILD-LOG.md first. Load-bearing, do not "clean up":
   the maroon marks and rules that appear on cue (GATE A errors on any scene
   whose shape state never changes), literal 0.6 in to_edge and literal
   font_size inside construct (GATE W reads them off the AST), no "" spacer
   lines in any text stack (Week 3 shipped a 100%-overlap GATE B failure that
   way), and SAFE_BUFF_X = 0.85 because the audit's horizontal safe area is
   +/-6.3, not the +/-6.51 SAFE_BUFF alone allows.
3. .../SOURCES.md — in particular the live-site status table. The cleanup is
   DECIDED, NOT DEPLOYED, and B08 says so on screen. Do not soften that.
4. .../SHOTLIST.md — the measured coordinate and the geometry pre-check.
5. .../assets/ — only 06_footer.jpg is used (B04).

Standing rules: never draw a proposed layout; never use Line() for a
strikethrough; name no individual (the developer is unnamed pending a spelling
confirmation).

Steps:
1. python3 runtime/scripts/generate_audio_kokoro.py reels/humanitarians-ai-week4-navigation-cleanup-handoff
2. ./art run reels/humanitarians-ai-week4-navigation-cleanup-handoff
   GATE A and GATE W were reproduced in a sandbox against this exact
   scenes.py: 0 blocking errors, 0 warnings, 20/20 WCAG-clean. Anything
   printed is new. On a GATE B failure read layout_audit.md for the exact
   coordinates. Never set ART_QC=0.
3. ./art todo reels/humanitarians-ai-week4-navigation-cleanup-handoff
4. ./art final reels/humanitarians-ai-week4-navigation-cleanup-handoff
   -> renders/humanitarians-ai-week4-navigation-cleanup-handoff.mp4 at the
   TOOLKIT ROOT.
5. ./art shorts ... THEN VERIFY short/manim/ contains clips.
6. QC qc-sheet.png for all 20 beats. Confirm the B04 box lands on the footer's
   Projects column and no chip touches it.
7. Report actual durations into BUILD-LOG.md and update the wps calibration.
   Never publish — local render for review.
```
