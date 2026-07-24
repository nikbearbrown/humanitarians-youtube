# BUILD-PROMPT — claude-liam-mcp-builder

Skill teardown reel for the Anthropic `mcp-builder` skill.
Channel: claude-liam · Voice: Kokoro af_kore · Format: 16:9 · Modifier: skill-teardown

## What this video covers
The mcp-builder skill guides building high-quality MCP servers through 4 phases: research,
implement, review/test, evaluate. TypeScript + Zod is the recommended stack. Quality is
measured by whether agents can complete real tasks — proven by a 10-question evaluation gate.

## Beat map
- B00: ClaudeComposerAsk cold open — "Konnichiwa, Kore" greeting, MCP server request, skill fires
- B01: McpBuilderAnatomy — 4 phases + 5 tool quality principles
- B02: McpBuilderToolAnatomy — tool anatomy: Zod schema, outputSchema, 4 annotations, naming rules
- B05: McpBuilderTell — teardown: quality bar insight + gets-right/bites card columns
- BVDT: ClaudeVerdictArtifact — 6-line verdict
- BHTF: ClaudeComposerAsk handoff — "Your Turn" with phase-gate check instructions
- BOUT: ClaudeTitleOutro — "MCP Builder · Kore, in for Humanitarians AI"

## Build commands (run from books/)
```bash
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  anthropics/skills/youtube/claude-liam-mcp-builder/

python3 brutalist-art/runtime/scripts/remotion_scenes.py \
  anthropics/skills/youtube/claude-liam-mcp-builder/

python3 brutalist-art/runtime/scripts/compile.py \
  anthropics/skills/youtube/claude-liam-mcp-builder/
```
