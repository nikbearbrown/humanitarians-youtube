# BUILD-PROMPT — "Before You Rebuild, You Read the Room." (Week 1 of 4)

Paste into Claude Code (or any coding agent) from the `brutalist.art-main/` toolkit root:

```
Build the reel "humanitarians-ai-week1-diagnostic-audit" — a 3-4 minute
brutalist-style project-status video covering Week 1 of the Humanitarians AI
website UX/UI restructure (heuristic audit, competitive benchmark,
typography research, and the pivot from full-rebuild to targeted fixes).

Ground truth, read first:
1. reels/humanitarians-ai-week1-diagnostic-audit/beat_sheet.json — the master.
   14 beats, narration text already final (this is the presenter's own
   script from the video brief — no fact-check gate needed on the narration
   itself; FACTCHECK.md instead verifies the ON-SCREEN annotation claims
   against the actual screenshot pixels).
2. reels/humanitarians-ai-week1-diagnostic-audit/scenes.py — every beat's
   Manim scene. Read BUILD-LOG.md first for why this reel uses Manim for
   every beat (including the "plain screenshot" ones) instead of the
   toolkit's Remotion annotation plane.
3. reels/humanitarians-ai-week1-diagnostic-audit/assets/ — the six source
   screenshots (01_hero_section.jpg through 06_footer.jpg), already placed.
4. SHOTLIST.md — which screenshot feeds which beat, and the exact
   normalized crop/annotation coordinates used in scenes.py.

Steps:
1. Audio (the master clock):
   python3 runtime/scripts/generate_audio_kokoro.py reels/humanitarians-ai-week1-diagnostic-audit
   Voice: am_onyx (Onyx). Measure actual_duration_s per beat via ffprobe;
   the Manim scene durations are approximate and will auto-retime/freeze-pad
   to match (compile.py's slow-to-fit + tpad logic) — do not hand-edit
   scene timing to chase this, regenerate audio if timing feels wrong.
2. Draft compile: ./art run reels/humanitarians-ai-week1-diagnostic-audit
   This renders all 14 Manim scenes at native 4K (3840x2160, 24fps) and
   assembles a review cut. GATE A (static pre-flight) and GATE W (WCAG
   contrast + margins + text-overlap) run automatically — if either fails
   on a scene, fix the scene; do not set ART_QC=0 to skip past a real
   contrast/overlap problem.
3. Check what's outstanding: ./art todo reels/humanitarians-ai-week1-diagnostic-audit
4. Clean 4K master: ./art final reels/humanitarians-ai-week1-diagnostic-audit
   → humanitarians-ai-week1-diagnostic-audit-cut.mp4 (3840x2160, 16:9).
5. 9:16 short: ./art shorts reels/humanitarians-ai-week1-diagnostic-audit
   → derives the portrait cut from the same beat sheet.
6. QC: eyeball qc-sheet.png (compile.py's mid-frame contact sheet) for all
   14 beats. Confirm: hero screenshot legible at both ends of B03/B09's
   annotation, the type-scale ladder in B08 doesn't clip at 4K, and no
   overlay chip sits on top of a button it's supposed to be readable over.
7. Report actual per-beat durations + total runtime back into BUILD-LOG.md.
   Never publish — this stays a local render for review.
```
