# BUILD-PROMPT — How Facial Recognition Actually Works (And When It Shouldn't)

Reproducible context/prompt this video was built from. Paste into Claude Code
from `/Users/pranavijs/humanitarians-youtube/` to rebuild or extend this reel.

```
Build (or rebuild) the ai-explainer reel "How Facial Recognition Actually
Works (And When It Shouldn't)" for fellow Sai Pranavi Jeedigunta.

Original brief (scoped down from a 5-minute deep-explainer to a 3-minute
ai-explainer): first-person narration ("I", not "we"), balanced tone, not
advocating a policy position. Cover, in order: (1) frame as a current,
actively-debated topic, (2) explain the actual mechanism — detection,
embedding, comparison, similarity score, not a binary match, (3) legitimate
uses, (4) harmful/unnecessary uses, (5) NIST FRVT demographic-effects
findings, cited directly, including the industry-aligned dissenting view,
(6) connect to the "fluency trap" framing, (7) close on proportional
scrutiny, not a verdict on the technology itself.

Ground truth, read first:
1. fellows/sai-pranavi-j/2026-07-27-how-facial-recognition-actually-works/beat_sheet.json
   — the master beat sheet (8 beats, voice af_bella / hai persona / @HumanitariansAI).
2. fellows/sai-pranavi-j/2026-07-27-how-facial-recognition-actually-works/{FACTCHECK.md,SOURCES.md,PEDAGOGY.md}
   — the signed gates and the primary source (NISTIR 8280).
3. brutalist/ (toolkit, installed at /Users/pranavijs/humanitarians-youtube/brutalist)
   — the free Kokoro/Manim/Remotion engine. Never edit toolkit files; only
   read/run its scripts. Video output lives ONLY in this fellows/ folder.

Steps:
1. Audio: python3 <toolkit>/runtime/scripts/generate_audio_kokoro.py
   <this-reel-folder> — voice af_bella. Measure actual durations (the master
   clock); never hand-adjust timing.
2. Compile the review cut: <toolkit>/art run <this-reel-folder> --height 1080.
3. Check GATE A/W (static pre-flight) on every new scenes.py class before
   the first full run — cheaper to catch shape-distinctness and margin
   issues before a render than after.
4. QC by looking at frames (contact sheet + the true clean master, not just
   the review cut, which carries a review-only timecode watermark that
   causes a known false-positive "edge-bleed" on GATE V).
5. ./art final <this-reel-folder> once all beats are real media, not slates.

Report and STOP. Never publish — the master stays in this reel folder;
publishing is a separate human decision, and this repo's own .gitignore
excludes *.mp3/*.mp4 from git (paperwork only gets committed).
```
