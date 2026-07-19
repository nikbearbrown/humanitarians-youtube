# BUILD-PROMPT — claude-liam-collage-ads
# "Claude, Collaged." | collage-ads skill teardown
# Built: 2026-07-18 | Kokoro am_onyx | 225.9s

## Standalone rebuild instructions

```bash
cd /Users/bear/Documents/CoWork/bear-textbooks/books/brutalist-art
python3 runtime/scripts/generate_audio_kokoro.py youtube/claude-liam-collage-ads
python3 runtime/scripts/remotion_scenes.py youtube/claude-liam-collage-ads
python3 runtime/scripts/compile.py youtube/claude-liam-collage-ads --height 1080
open youtube/claude-liam-collage-ads/claude-liam-collage-ads.mp4
```

## Key decisions
- **Self-demo**: Phase A decode of a hypothetical MORNING BREW coffee ad → collage JSON spec. All JSON fields populated per SKILL.md schema. Label treatment follows the "burned in at generation, never via arcads_add_text_overlay" rule. No Arcads MCP calls needed for Phase A.
- **Greeting**: Cześć (Polish) — unique in this batch run.
- **Title**: "Claude, Collaged." — the independently-editable JSON spec is the artifact.
- **MINOR-COSMETIC**: B04 ClaudeCodeBeat 3.7× slow-mo (10s Remotion clip stretched to 37.5s narration) — known, non-blocking.
