# PEDAGOGY — mcp-integration

## Verdict: PASS

## Skill
MCP Integration (`anthropics/claude-code/plugins/plugin-dev/skills/mcp-integration/SKILL.md`)

## Learning objective
Viewer can write .mcp.json with the correct server type, understand the tool naming format (mcp__plugin_...__...), and pre-allow specific tools rather than wildcards in command frontmatter.

## Concrete-before-abstract
B01 opens with two config methods and then the four server types with concrete use cases before any conceptual framing. B02 leads with the tool naming format — the most precise and failure-prone element — before the integration patterns.

## Prediction-before-reveal
B00 names all four server types and both config methods upfront.

## Useful friction
The tool naming format requires the viewer to hold the exact double-underscore structure in mind and check for it in Claude's output.

## Handoff
BHTF gives four specific checkpoints grounded in the most common failure modes.
