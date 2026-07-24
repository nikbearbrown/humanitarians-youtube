# BUILD-PROMPT — Claude, Debunked?

Paste into Claude Code from `books/` (typically `claude --dangerously-skip-permissions`):

```
Rebuild the nbb claude-explainer reel "Claude, Debunked?" with Bear's real voice.

Ground truth, read first:
1. brutalist-art/youtube/claude-debunked/beat_sheet.json — the master; narration approved (GATE P for this text only).
2. brutalist-art/youtube/claude-debunked/PEDAGOGY.md + NARRATION-GATE-P.md + FACTCHECK-THE-FACTCHECK.md — the gates and the sourced verdicts.
3. brutalist-art/skills/make/ai-explainer/SKILL.md + brutalist-art/CLAUDE-BRAND.md — the laws incl. ILLUSTRATE LAW (the wheel is UI-legal: it's the artifact under audit; its focus state must differ every beat).
4. brutalist-art/youtube/claude-debunked/remotion-src/ — Debunked.tsx + Wheel.tsx (EcosystemWheel with grade/startAt/focus props) + debunked_data.json.

Steps:
1. Audio: python3 runtime/scripts/generate_audio.py youtube/claude-debunked/ from brutalist-art/ — ELEVENLABS_VOICE_NIKBEARBROWN. ffprobe → actual_duration_s; conform frames = ceil((mp3 + 0.4) * 30); regenerate debunked_data.json timings.
2. Render at --scale=1.5 → youtube/claude-debunked/media/final-cut.mp4 (16:9 — replaces the partial 1000x1200 wheel fragment, which stays as media/ecosystem-wheel-graded.mp4). No caption bar.
3. QC: ffprobe; stills of B00 (result lines), B01 assemble, B02 real-focus, B03 stale-focus + Fable card, B04 invented-focus, B06 twist (Marketplace/Security highlighted + verdict strip), verdict page, handoff, outro.
4. Report and STOP. Never publish. Route per YouTube.json conventions.
```
