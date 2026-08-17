# BUILD-PROMPT — The Pipeline That Was Lying to Me

Reproducible context/prompt this video was built from. Paste into Claude Code
from `/Users/pranavijs/humanitarians-youtube/` to rebuild or extend this reel.

```
Build (or rebuild) the ai-explainer reel "The Pipeline That Was Lying to Me"
for the Humanitarians AI Fellows weekly-report series.

Ground truth, read first:
1. fellows/sai-pranavi-j/2026-07-26-recovering-the-silently-dropped-filings/beat_sheet.json
   — the master beat sheet (7 beats, ~90s, voice af_bella / hai persona / @HumanitariansAI).
2. fellows/sai-pranavi-j/2026-07-26-recovering-the-silently-dropped-filings/{FACTCHECK.md,SOURCES.md,PEDAGOGY.md}
   — the signed gates.
3. /Users/pranavijs/mycroft/scripts/regulatory-intel/FINDINGS.md — the primary
   evidence for every measured claim (297->370 items, +73 recovered, the four
   named recovered filings, the 370-item parameterized-insert stress test).
4. brutalist/ (toolkit, installed at /Users/pranavijs/humanitarians-youtube/brutalist)
   — the free Kokoro/Manim/Remotion engine. Never edit toolkit files; only
   read/run its scripts. Video output lives ONLY in this fellows/ folder.

Steps:
1. Audio: python3 <toolkit>/runtime/scripts/generate_audio_kokoro.py
   <this-reel-folder> — voice af_bella. Measure actual durations (the master
   clock); never hand-adjust timing.
2. Compile the review cut: <toolkit>/art run <this-reel-folder>.
3. ./art todo <this-reel-folder> — see which beats are honest slates (Manim/
   Remotion not yet built, or vox stills not yet dropped into pantry/) vs.
   fully rendered.
4. QC by looking at frames (not just the mp4 probe).
5. ./art final <this-reel-folder> once all beats are real media, not slates.

Report and STOP. Never publish — the master stays in this reel folder;
publishing is a separate human decision.
```
