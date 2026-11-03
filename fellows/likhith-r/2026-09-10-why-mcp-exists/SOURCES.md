# SOURCES — Why MCP Exists

Primary: Anthropic, "Introducing the Model Context Protocol", 2024-11-25 — https://www.anthropic.com/news/model-context-protocol
Specification: Model Context Protocol spec (tools: `tools/list`, `tools/call`, `notifications/tools/list_changed`; JSON-RPC 2.0 messages) — https://modelcontextprotocol.io/specification
SDK used for evidence: MCP Python SDK `mcp==2.2.0` (run in a throwaway `uv` env; not a toolkit dependency).
Brief supplied by the requester (Likhith); the 7 points were checked against the primary sources (2026-09-28).

## Executable evidence
- `evidence/mcp_discovery.py` → `evidence/mcp_discovery.out.txt`. A toy calendar MCP server (stdio) and a client; the client calls `list_tools()` (JSON-RPC `tools/list`) against v1 (2 tools) and v2 (3 tools) with the same client code.
- B05 shows the v1 response verbatim (names, descriptions, required inputs). B06 shows v1 → v2 (`cancel_event` added).

## Corrections / de-sensationalising
- MCP does not remove auth. Each MCP server still authenticates to the API it wraps; MCP standardises the agent-facing side. Stated on the B09 verdict card ("The server still talks to the real API, auth included").
- "No custom integration code per tool" is true from the agent's side. Someone still writes each server once (often the tool vendor). B04 says "each tool becomes one server"; the count "3 + 4 = 7, each built once" makes that explicit.
- "3 × 4 = 12" vs "3 + 4 = 7" is arithmetic on the illustrative example shown, not a measured statistic.
- Tool names, auth schemes, formats and doc types in B03/B07 are illustrative and labelled so on screen.
- The payment-terminal analogy (B08) is the requester's. Anthropic's own docs use a USB-C analogy; both are analogies, labelled as such.
- Removed version numbers and adoption counts that would date the video.
