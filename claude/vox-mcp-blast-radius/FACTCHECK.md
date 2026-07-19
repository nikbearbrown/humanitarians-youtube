# FACTCHECK — vox-mcp-blast-radius

## Claim 1
**Narration:** "MCP servers expose two kinds of capability: resources and tools. Resources are read-only — the agent can fetch data. Tools are callable functions that change external state."

**Source:** Chapter 06 (mcp-and-external-capabilities.md): "MCP exposes two fundamental capability types: Resources (read-only data the agent can access, like files, database records, or API responses) and Tools (callable functions that can change external state — create a ticket, send a message, update a record)."

**Verdict:** VERIFIED — exact match.

## Claim 2
**Narration:** "Both look identical in a server's description. Most users evaluate a server by its advertised purpose — not by inspecting which capabilities are read-only and which can write."

**Source:** Chapter 06: "The problem is that resources and tools look nearly identical in a server manifest — both appear as capability entries. Most users read the server description ('project management integration') without inspecting whether individual capabilities are resources or tools."

**Verdict:** VERIFIED — consistent.

## Claim 3 (calendar example)
**Narration:** Calendar assistant server with 'calendar access' description, hidden create/delete tools, agent sends invite to external clients.

**Source:** Candidate 08 card (video-ideas.md): "A team connects a 'calendar assistant' MCP server to help with scheduling research. The server description says 'calendar access.' Underneath: it has read events (resource) and create/delete events (tool). An agent asked to 'find a meeting time for next week' creates a calendar invite and sends it to three external clients before the human sees it."

**Verdict:** VERIFIED — canonical example seed.

## Claim 4
**Narration:** "Every MCP connection adds to the action surface."

**Source:** Chapter 06: "Each MCP server connection adds to the agent's action surface — the set of things the agent can do if its reasoning leads it there."

**Verdict:** VERIFIED — exact match.

## Exclusions confirmed
- No MCP wire protocol details ✓
- No OWASP MCP Top 10 full list ✓
- No prompt injection via tool results deep-dive ✓
