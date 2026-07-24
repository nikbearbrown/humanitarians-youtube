# BUILD-PROMPT — claude-liam-internal-comms

Skill teardown reel for the Anthropic `internal-comms` skill.
Channel: claude-liam · Voice: Kokoro af_kore · Format: 16:9 · Modifier: skill-teardown

## What this video covers
The internal-comms skill is a format router: 7 communication types (3P updates, company
newsletters, FAQ responses, status reports, leadership updates, project updates, incident reports)
mapped to 4 guideline files. Claude does not guess the format — it identifies the type, loads
the matching file, and follows its instructions exactly.

Key lesson: the 3P format is the most constrained. Always: one emoji + team name + dates +
Progress / Plans / Problems (1-3 sentences each, data-driven, 30-60s read).

## Beat map
- B00: ClaudeComposerAsk cold open — "Merhaba, Kore" greeting, 3P request, skill fires
- B01: InternalCommsAnatomy — 7 types mapped to 4 files + 3-step routing workflow
- B02: InternalComms3P — 3P format verbatim from examples/3p-updates.md + 4-step workflow
- B05: InternalCommsTell — teardown moment: router insight + gets-right/bites card columns
- BVDT: ClaudeVerdictArtifact — 6-line verdict
- BHTF: ClaudeComposerAsk handoff — "Your Turn" prompt with gate-check instructions
- BOUT: ClaudeTitleOutro — "Internal Comms · Kore, in for Humanitarians AI"

## Build commands (run from books/)
```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  anthropics/skills/youtube/claude-liam-internal-comms/

python3 brutalist-art/runtime/scripts/remotion_scenes.py \
  anthropics/skills/youtube/claude-liam-internal-comms/

python3 brutalist-art/runtime/scripts/compile.py \
  anthropics/skills/youtube/claude-liam-internal-comms/
```
