# BUILD-PROMPT — AI+1 (AI+1 series 1/4)

Paste into Claude Code from `books/` (typically `claude --dangerously-skip-permissions`):

```
Rebuild the AI+1 video "AI+1" with the real HAI voice.

Ground truth, read first:
1. humanitarians-ai/youtube/ai1/ai1-overview/beat_sheet.json — the master. Narration, greeting "Hi, HAI", props, callout geometry are approved — do not rewrite.
2. humanitarians-ai/youtube/ai1/ai1-overview/PEDAGOGY.md and NARRATION-GATE-P.md — GATE P passed for this narration text only; any narration edit reopens the gate.
3. humanitarians-ai/youtube/ai1/ai1-overview/decisions.json — change design choices ONLY by ID, patch-not-regenerate.
4. brutalist-art/skills/make/claude-explainer/SKILL.md + brutalist-art/CLAUDE-BRAND.md — the laws. Channel claude-hai: chip @HumanitariansAI, register Pragmatist.

Steps:
1. Audio: python3 runtime/scripts/generate_audio.py humanitarians-ai/youtube/ai1/ai1-overview/ from brutalist-art/ — voice kokoro af_heart (override ELEVENLABS_VOICE_HUMANITARIANS). ffprobe each mp3 → actual_duration_s into the beat sheet.
2. Composition: humanitarians-ai/youtube/ai1/remotion-src/ (PitchReelAi1 pattern — per-beat props in the beat sheet's shots, callout geometry in metadata.callout_items, chip @HumanitariansAI). Conform frames = ceil((mp3 + 0.4) * 30). No caption bar.
3. Render at --scale=1.5 → humanitarians-ai/youtube/ai1/ai1-overview/media/final-cut.mp4.
4. QC: ffprobe; stills of B00, one claim beat, the PREDICT beat, the verdict, the handoff, the outro — one terracotta accent, spark lines present, phase gate on the verdict, "Your turn." on the handoff, title restated.
5. Report and STOP. Never publish.
```

