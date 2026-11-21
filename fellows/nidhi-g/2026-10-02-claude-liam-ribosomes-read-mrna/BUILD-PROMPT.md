# BUILD-PROMPT — claude-liam-ribosomes-read-mrna

Paste into Claude Code, started in the `gemma_brutalist` toolkit folder:

> Rebuild the review cut of `C:\Users\nidhi\Downloads\brutalist-vids\claude-liam-ribosomes-read-mrna`
> following `skills/make/ai-explainer/SKILL.md`. Do not edit the beat sheet's narration or facts.
> 1. Gate check: confirm FACTCHECK.md, SHOTLIST.md and PROMPTS.md exist, and that every beat in
>    beat_sheet.json has a `shot.show` block.
> 2. Audio: `python3 runtime/scripts/generate_audio_kokoro.py <reel> --speed 1.1` (the cut was timed at 1.1).
> 3. Render + compile: `./art run <reel>` (Manim B02–B08 from scenes.py, Remotion bookends).
> 4. Visual QC: read `_qc/REPORT.md` and look at `_qc/contact_sheet.png` and the frames. Fix scene sources
>    until there are zero BLOCKER and zero MAJOR defects.
> 5. Report: the measured duration, which beats rendered and which slated, and any QC findings.
> Never run `./art final` and never publish. This brief is a review cut only.

Windows prerequisites: venv active (`source .venv/Scripts/activate`), `PYTHONUTF8=1` and `ART_NO_DRAWTEXT=1` set.
