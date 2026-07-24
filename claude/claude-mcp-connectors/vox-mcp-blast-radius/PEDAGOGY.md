# PEDAGOGY — vox-mcp-blast-radius

## Learning objective
Viewer understands that connecting an MCP server by its advertised purpose is not enough — the tool list (not the description) determines the actual blast radius, and tools that can write external state need explicit review before connection.

## Act structure
- **COLD OPEN (B01–B02):** Production ticket autonomously marked complete after server connection — no thesis stated.
- **THE QUESTION (B03):** On-screen question: "Why did a read-intent connection create autonomous write-capability?"
- **MECHANISM (B04–B05):** Resources vs tools split — both in same server manifest, most users only read the description. Mechanism card: "The advertised purpose does not determine the blast radius. The tool list does."
- **EXAMPLE (B06):** Calendar assistant server — "calendar access" description hides create/delete tools. Agent sends external invite.
- **PRACTICE (B07–B08):** Two-column compare shows description-only vs tool-list evaluation. Checklist: open tool list → label read/write → disable write tools not needed.
- **RECAP (B09):** Endcard — mechanism sentence, not book title.

## Prerequisite check
Card states: "Understanding that agents can connect to external services; no MCP protocol knowledge required." Film uses plain language for all MCP concepts. ✓

## Exclusion check
- No MCP wire protocol details ✓
- No OWASP MCP Top 10 full list ✓
- No prompt injection via tool results deep-dive ✓

## Pacing
~130s (2:10) — fits 2–3 min band. ✓

## Single question test
One mechanism: description ≠ blast radius; tool list determines what can change. One question on screen. ✓

VERDICT: PASS
