# BUILD-PROMPT — Why AI-Generated Code Still Needs a Human Who Understands the System

Reproducible context/prompt this video was built from. Paste into Claude Code
from `/Users/pranavijs/humanitarians-youtube/` to rebuild or extend this reel.

```
Build (or rebuild) the ai-explainer reel "Why AI-Generated Code Still Needs a
Human Who Understands the System" for fellow Sai Pranavi Jeedigunta — Film 1
of a new general-AI-topic series.

Original brief: teach a reusable rubric for how much scrutiny an AI-suggested
code fix needs, structured per the PROOF.md protocol (framework shown before
any example, a worked example, a falsifiability case, a scaffolded CTA).
Cover, in order: (1) hook on a fix that looks correct but still crashes
production, (2) the 3-question rubric — Trace / Consequence / Why — shown in
full before any example, (3) a worked example walking all three questions
against a code fix, (4) a falsifiability case (a low-stakes date-formatter
function) showing the rubric scales with consequence rather than mandating
blanket distrust, (5) a concrete 3-step viewer task, (6) close, callback to
the hook.

IMPORTANT — the worked example is deliberately a generic, illustrative code
pattern (a hand-escaped SQL insert vs. a parameterized-query fix), not
attributed to a specific real incident or repo. This was a fellow decision
(2026-08-17) after an earlier draft considered sourcing it from real Project 29
(`mycroft`) engineering work; see FACTCHECK.md for why that was set aside.
Do not attribute this example to any real codebase when building or narrating it.

Ground truth, read first:
1. fellows/sai-pranavi-j/2026-08-17-why-ai-generated-code-still-needs-a-human/BEAT-SHEET.md
   — the narrative beat sheet (premise, legibility contract, 6 beats, production gate self-check).
2. fellows/sai-pranavi-j/2026-08-17-why-ai-generated-code-still-needs-a-human/beat_sheet.json
   — the same plan in the pipeline's structured schema (voice af_bella / hai persona / @HumanitariansAI).
3. fellows/sai-pranavi-j/2026-08-17-why-ai-generated-code-still-needs-a-human/{FACTCHECK.md,SOURCES.md,PEDAGOGY.md}
   — fact-check status and the no-fabrication note on the worked example.
4. brutalist/ (toolkit, installed at /Users/pranavijs/humanitarians-youtube/brutalist)
   — the free Kokoro/Manim/Remotion engine. Never edit toolkit files; only
   read/run its scripts. Video output lives ONLY in this fellows/ folder.

Steps (none done yet for this cut):
1. Fellow approval of BEAT-SHEET.md / beat_sheet.json (Gate P) before any
   audio generation.
2. Resolve the open compliance item: no channel/fellow sign-off beat exists
   yet (see BUILD-LOG.md) — decide whether to add one before narration lock.
3. Author scenes.py (6 Manim scenes, B00-B05).
4. Audio: python3 <toolkit>/runtime/scripts/generate_audio_kokoro.py
   <this-reel-folder> — voice af_bella. Measure actual durations (the master
   clock); never hand-adjust timing.
5. Compile the review cut: <toolkit>/art run <this-reel-folder> --height 1080.
6. Check GATE A/W (static pre-flight) on every new scenes.py class before
   the first full run.
7. QC by looking at frames (contact sheet + the true clean master, not just
   the review cut, which carries a review-only timecode watermark that
   causes a known false-positive "edge-bleed" on GATE V).
8. ./art final <this-reel-folder> once all beats are real media, not slates.

Report and STOP. Never publish — the master stays in this reel folder;
publishing is a separate human decision, and this repo's own .gitignore
excludes *.mp3/*.mp4 from git (paperwork only gets committed).
```
