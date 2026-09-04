# Match The Transport, Not The Key. — The MCP Integration Skill (Transports & Tool Names)

Four transport types, and each server uses exactly one. Stdio spawns a local
process for custom servers and local tools; SSE connects to a hosted server
and handles OAuth automatically — the type for official hosted services like
GitHub or Linear; HTTP calls a REST API with a token in the request headers;
WebSocket keeps a live, two-way connection open for real-time updates. Keep
server config in its own `.mcp.json` file, use the `CLAUDE_PLUGIN_ROOT`
variable for every path, and pre-allow the exact tool name — run `/mcp`
first to see it. Here's the catch: get one character wrong in that name and
the tool doesn't show up, no error, no warning. And for stdio or HTTP
servers, the required environment variables aren't checked until the first
real call, so a broken setup can look perfectly healthy right up until then.

**Topic:** MCP INTEGRATION · CLAUDE PLUGINS
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-mcp-integration

---

## Chapters

0:00 The naive framing: "what key does my plugin need?"
0:11 Four transport types
0:43 Portable paths, exact names
1:19 Wrong by one character
1:41 Carry-out
1:56 Your turn
2:19 Outro

---

## YOUR TURN

Paste this into Claude: Add a GitHub SSE MCP server and a local custom
stdio server to my plugin. Then check what it wrote: did it use
`.mcp.json`, kept separate from `plugin.json`? Does every path use the
`CLAUDE_PLUGIN_ROOT` variable instead of something hardcoded? And before it
pre-allows any tools, did it tell you to run `/mcp` first, to get the exact
names?

Run that today, on your own plugin idea, not the video's example.

---

## Deliberately not claimed

No claim about how Claude Code decides which transport to fall back to if a
configured connection fails — the source Skill doesn't document that, and
this video doesn't guess. No claim that every MCP server implementation
validates or fails to validate environment variables the same way; the
unvalidated-until-first-call gap described is a property of stdio/HTTP
servers as specified in this Skill version, not a claim about every possible
MCP server.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #MCP #LLM #HumanitariansAI #ProfessorBear

---
