# PEDAGOGY — mcp-integration

## Skill summary
mcp-integration connects Claude Code plugins to external services via Model Context Protocol. Four transport types (stdio, SSE, HTTP, WebSocket), two config methods (.mcp.json vs inline plugin.json mcpServers), a verbose tool naming convention, and OAuth/token/env var authentication patterns.

## What Claude will learn
- Four MCP transport types and when to choose each
- .mcp.json over inline mcpServers for multi-server plugins
- ${CLAUDE_PLUGIN_ROOT} for portable paths
- Tool name format that must match exactly in frontmatter pre-allow lists
- OAuth is automatic for SSE; tokens in env vars for HTTP/stdio
- /mcp and --debug for discovery and debugging
- Security: no hardcoded tokens, HTTPS/WSS only, specific not wildcard pre-allow

## Pedagogical assessment
Content is concrete (config JSON examples, explicit trade-offs between types), has clear security guidance, and covers the full lifecycle from load to tool call. The tool name format is a genuine gotcha worth emphasizing. Abstention vs guessing is well handled via the /mcp discovery command.

## VERDICT: PASS
