# BUILD-PROMPT.md — claude-liam-hawthorne-effect

Paste this entire prompt into a fresh Claude Code session (cwd: `books/`) to rebuild
the final cut end-to-end from source.

---

## Rebuild prompt

```
Build the 16:9 claude-explainer video "Claude, Observed" from the MBA Management book,
Chapter 1 — the Hawthorne Effect.

Reel directory: mba-management/youtube/claude-liam-hawthorne-effect/
Beat sheet:     mba-management/youtube/claude-liam-hawthorne-effect/beat_sheet.json
Scenes file:    mba-management/youtube/claude-liam-hawthorne-effect/scenes.py
Source chapter: mba-management/chapters/01-management-and-organizational-behavior.md

Channel: claude-liam (am_onyx, @NikBearBrown, Teardown register)
Pipeline: FREE only — Kokoro TTS, no ElevenLabs, no Higgsfield, no git push.
No approval pauses needed (no paid spend possible).

PRE-READ before touching files:
  brutalist-art/AGENTS.md
  brutalist-art/CLAUDE-BRAND.md
  brutalist-art/skills/make/claude-explainer/SKILL.md

STEPS (run from books/):

1. Generate Kokoro audio (measures actual_duration_s):
   python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
     mba-management/youtube/claude-liam-hawthorne-effect

2. Render all Remotion beats (B00,B01,B03,B05,B07,B10,B12,B15,B16,B17):
   python3 brutalist-art/runtime/scripts/remotion_scenes.py \
     mba-management/youtube/claude-liam-hawthorne-effect

3. Render all Manim scenes (from inside the reel dir, ART_FACTS=0 to bypass Gate F
   since FACTCHECK.md / SHOTLIST.md / PROMPTS.md already exist):
   cd mba-management/youtube/claude-liam-hawthorne-effect
   ART_FACTS=0 manim scenes.py B02_BrokenExperiment -p --resolution=1080 --fps=24
   ART_FACTS=0 manim scenes.py B04_Reanalysis -p --resolution=1080 --fps=24
   ART_FACTS=0 manim scenes.py B06_FiveFunctions -p --resolution=1080 --fps=24
   ART_FACTS=0 manim scenes.py B08_ManagementPyramid -p --resolution=1080 --fps=24
   ART_FACTS=0 manim scenes.py B09_SkillsTriangle -p --resolution=1080 --fps=24
   ART_FACTS=0 manim scenes.py B11_ManagementTimeline -p --resolution=1080 --fps=24
   ART_FACTS=0 manim scenes.py B13_FiveBlockDiagnostic -p --resolution=1080 --fps=24
   cd ../../..
   Then move each render to manim/B02.mp4, manim/B04.mp4, etc.

4. Compile review cut:
   python3 brutalist-art/runtime/scripts/compile.py \
     mba-management/youtube/claude-liam-hawthorne-effect

5. Visual QC — sample frames, check 8-point rubric (palette, logo, readable text,
   correct beat order, no UI wallpaper in body beats).

6. Final cut (clean master, no QC overlay):
   python3 brutalist-art/runtime/scripts/compile.py \
     mba-management/youtube/claude-liam-hawthorne-effect --final

7. Probe output:
   ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 \
     mba-management/youtube/claude-liam-hawthorne-effect/mp4/claude-liam-hawthorne-effect.mp4

LAWS enforced in beat_sheet.json (do not alter beat order):
  COLD OPEN LAW: beats[0] = B00 ClaudeComposerAsk
  IN-FOR-BEAR LAW: B00 opens "This is Liam, in for Bear."
  ASK→RESULT LAW: ClaudeComposerAsk ask before every Manim figure
  ILLUSTRATE LAW: no UI chrome in body beats (B14 = CARD, no ClaudeComposerAsk)
  HANDOFF LAW: B16 = "Your turn." reads prompt verbatim
  OUTRO LAW: beats[-1] = B17 ClaudeTitleOutro
  FIGURE RULES: B02 + B04 qualitative only (no invented numbers)
```
