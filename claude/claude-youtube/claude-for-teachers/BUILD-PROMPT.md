# BUILD-PROMPT — Claude, For Teachers

Paste into Claude Code from `books/` (typically `claude --dangerously-skip-permissions`):

```
Rebuild the nbb claude-explainer reel "Claude, For Teachers" with Bear's real voice.

Ground truth, read first:
1. brutalist-art/youtube/claude-for-teachers/beat_sheet.json — the master; narration approved (GATE P passed for this text only).
2. brutalist-art/youtube/claude-for-teachers/PEDAGOGY.md + NARRATION-GATE-P.md — the gates.
3. brutalist-art/skills/make/ai-explainer/SKILL.md + brutalist-art/CLAUDE-BRAND.md — the laws, INCLUDING the new ILLUSTRATE LAW (UI only where the UI is the subject; B04 is the one UI-legal inner beat — Cowork is the subject).
4. brutalist-art/youtube/claude-for-teachers/remotion-src/ — the working composition (Teachers.tsx + TeachersIllu.tsx + shared Illustrations/deckPatterns from medhavy_com/youtube/mcp/remotion-src/).

Steps:
1. Audio: python3 runtime/scripts/generate_audio.py youtube/claude-for-teachers/ from brutalist-art/ — ELEVENLABS_VOICE_NIKBEARBROWN. ffprobe each mp3 → actual_duration_s; conform frames = ceil((mp3 + 0.4) * 30).
2. Render at --scale=1.5 → youtube/claude-for-teachers/media/final-cut.mp4 (replaces the espeak previz). No caption bar.
3. QC: ffprobe; stills of B00 (result lines visible), B01–B05 (each a DIFFERENT visual scheme — that's the ILLUSTRATE LAW check), verdict, handoff, outro. One terracotta accent per beat.
4. Report and STOP. Never publish. Route to the "Claude for Education" playlist per YouTube.json conventions.
```
