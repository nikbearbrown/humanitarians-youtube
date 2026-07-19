# FACTCHECK -- evaluate-mcp-server
Source chapter: `claude-agentic-ai/chapters/06-mcp-and-external-capabilities.md`

## Claims audit
| Claim | Verdict | Source / note |
|---|---|---|
| MCP servers extend agent capabilities beyond the base model | SUPPORTED | Chapter 06 on MCP as capability extension mechanism |
| Connecting a server with write capabilities grants those capabilities to the agent | SUPPORTED | Chapter 06 on connection as capability grant |
| Blast radius and reversibility are key dimensions for MCP server review | SUPPORTED | Chapter 06 on pre-connection evaluation criteria |
| External email capability introduces prompt injection risk via external content | SUPPORTED | Chapter 06 on injection vectors through external-facing tools |
| Server A read-only vs Server B read-write for status report task | ILLUSTRATIVE | Adapted from ch.06 worked example. Synthetic server comparison. |

## Exclusions confirmed
- MCP protocol implementation details: not mentioned, evaluation only
- OWASP MCP Top 10 full walkthrough: not mentioned, focused on blast radius and reversibility dimensions
- Custom server development: not mentioned, evaluation of existing servers only

## Terms table
| Term | Debut beat | Prior beat creating the need |
|---|---|---|
| MCP server | B01 | B01 establishes the connection decision as an approval gate |
| Blast radius | B01 | B01 frames the risk of over-capable server connection |
| Prompt injection | B06 | B05 CHANGE introduces Server C with external email -- the vector |
| Approval gate | B02 | B01 names connection as the moment that determines downstream risk |
