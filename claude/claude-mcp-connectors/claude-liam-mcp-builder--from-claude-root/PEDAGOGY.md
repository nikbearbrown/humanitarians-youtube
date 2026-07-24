# PEDAGOGY — claude-liam-mcp-builder

Skill: `mcp-builder` · Modifier: `skill-teardown`

## PREDICT (viewer question before watching)
"I know MCP is how Claude connects to external services — but what makes an MCP server *good* versus just functional?"

## What the viewer will learn
1. The skill follows 4 phases: research/planning → implementation → review/test → create evaluations
2. TypeScript + Zod is the recommended stack; streamable HTTP for remote, stdio for local
3. Tool quality is measured by how well it enables real-world task completion — naming, descriptions, and error messages matter as much as coverage

## CONFIRM (what the reel reveals)
- TRIGGER: "build an MCP server", "integrate X API with Claude", "create MCP tools"
- 4-phase workflow: research → implement → review → evaluate
- Tool design rules: consistent prefix naming (e.g. github_create_issue), Zod schemas, outputSchema + structuredContent, actionable errors
- Evaluation standard: 10 independent, read-only, complex, realistic, verifiable questions in XML format

## LAWS CHECKED
- ✅ TRIGGER is clear: "build MCP server" / "integrate API with Claude" / "create MCP tools"
- ✅ SELF-DEMO: B02 shows verbatim tool anatomy from SKILL.md (Zod schema, annotations, outputSchema)
- ✅ HANDOFF LAW: BHTF narration reads prompt aloud AND explains what to watch for
- ✅ ILLUSTRATE LAW: UI only at B00 and BHTF bookends
- ✅ ASK→RESULT law: B00 shows ask + TRIGGER + result

## VERDICT: PASS
