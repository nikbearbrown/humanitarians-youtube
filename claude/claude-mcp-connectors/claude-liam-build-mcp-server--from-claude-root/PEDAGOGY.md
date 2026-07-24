# PEDAGOGY — claude-liam-build-mcp-server

## Skill reviewed
`anthropics/claude-plugins-official/plugins/mcp-server-dev/skills/build-mcp-server/SKILL.md`

## What learners will be able to do
- Apply discovery-before-code: ask four questions before any scaffolding
- Choose the right deployment model: remote HTTP (default), MCPB (local machine required), local stdio (prototype only)
- Apply the right tool-design pattern: one-per-action (<15) vs search+execute (large surface)
- Pick the right framework: TypeScript SDK vs FastMCP (jlowin's PyPI 3.x, not the frozen 1.0)
- Use elicitation correctly with a capability check and fallback
- Know when to hand off to build-mcp-app or build-mcpb

## What makes this teachable
The deployment model ranking is opinionated (remote HTTP default with a clear "unless" rule).
The tool-design pattern split (15-tool threshold) is a concrete rule, not a vague guideline.
The seven-scenario decision matrix gives Claude a complete picture for any plausible combination.
The hand-off structure (Phase 5) makes the skill's scope clear — it's a router, not a builder.

## Gaps the teardown surfaces
- Elicitation capability check requirement buried mid-paragraph — SDK throws without it
- FastMCP version disambiguation (jlowin's PyPI 3.x vs frozen 1.0 in official mcp SDK) is a single sentence
- Tool description quality deferred entirely to references/tool-design.md, not inline
- CIMD vs DCR OAuth distinction mentioned but fully deferred to references/auth.md
- "Load Claude docs first" invariant has no enforcement — Phase 1 questions follow immediately

## VERDICT: PASS

Discovery-before-code structure, opinionated deployment ranking, and tool-design pattern split
are all complete and actionable. Teardown adds value by surfacing the elicitation capability
check and the FastMCP version confusion prominently.
