# BUILD-PROMPT — Who was Albert Einstein? (claude-liam)

Paste into Claude Code, run from `books/` with `--dangerously-skip-permissions`:

```
Build the claude-liam explainer reel at books/physics-modern-physics/youtube/claude-liam-who-was-albert-einstein.

Steps (do NOT re-author — all content is final):
1. python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py physics-modern-physics/youtube/claude-liam-who-was-albert-einstein --no-gate
2. ART_QC=1 bash brutalist-art/runtime/scripts/run.sh physics-modern-physics/youtube/claude-liam-who-was-albert-einstein
3. python3 brutalist-art/runtime/scripts/compile.py physics-modern-physics/youtube/claude-liam-who-was-albert-einstein --allow-slates

Report the two output paths:
  physics-modern-physics/youtube/claude-liam-who-was-albert-einstein/who-was-albert-einstein-slate.mp4
  physics-modern-physics/youtube/claude-liam-who-was-albert-einstein/who-was-albert-einstein.mp4

Never publish. Never delete any ElevenLabs mp3 (44.1kHz) or any human-supplied mp4.
Voice: Kokoro af_kore (free, local). Brand: claude-liam / @HumanitariansAI.
Outro title must preserve "?" — "Who was Albert Einstein?"
```
