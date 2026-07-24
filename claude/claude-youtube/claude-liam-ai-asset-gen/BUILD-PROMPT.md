# BUILD-PROMPT — claude-liam-ai-asset-gen
# "Claude, Generated." | ai-asset-gen skill teardown
# Built: 2026-07-18 | Kokoro af_kore | 190.7s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-ai-asset-gen
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-ai-asset-gen
python3 runtime/scripts/compile.py youtube/claude-liam-ai-asset-gen --height 1080
open youtube/claude-liam-ai-asset-gen/claude-liam-ai-asset-gen.mp4
```

## Key decisions
- **Self-demo**: Model selection decision tree — free phase before any Higgsfield API spend. Shows GPT Image 2 selection for a banner brief with typography requirement.
- **Greeting**: Dia dhuit (Irish) — unique in this batch run.
- **Title**: "Claude, Generated." — the model-selection decision is the artifact; the command is the output.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 2.71× slow-mo (10s Remotion clip stretched to 27.3s narration) — known, non-blocking.
