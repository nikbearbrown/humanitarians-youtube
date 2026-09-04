# MCP Builder.

Building a good MCP server doesn't start with code — it starts with research:
the protocol, the language, the tool list, before anything gets written. Every
tool then needs four things: a typed input schema (Zod in TypeScript, Pydantic
in Python), an output schema, four annotations (`readOnlyHint`,
`destructiveHint`, `idempotentHint`, `openWorldHint`), and an actionable error
message — named by one fixed pattern, prefix then action:
`github_create_issue`, `github_list_repos`. The skill's own proof standard is
ten evaluation questions, and they have to be read-only and verifiable — which
means a read-only tool like `github_list_repos` gets checked directly against
the real answer, while a tool that writes real state, like
`github_create_issue`, can't be proven the same way, even though it's exactly
the kind of call an agent gets asked to make.

**Topic:** MCP BUILDER · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/skills--claude-liam-mcp-builder

---

## Chapters

0:00 How do I research and build an MCP server for GitHub?
0:11 Research first, or it stalls
0:31 Every tool, four things — the anchor
0:57 The evaluation rule, both ways
1:26 Carry-out
1:39 Your turn
2:03 Outro

---

## YOUR TURN

"Build an MCP server for the OpenWeatherMap API. Use TypeScript and Zod.
Cover current weather, forecasts, and historical data. Follow the
mcp-builder skill."

Watch whether Claude opens with research — the MCP protocol, OpenWeatherMap's
own docs — before any implementation code. Then check each resulting tool for
a Zod input schema, an output schema, and all four annotations: read-only,
destructive, idempotent, open-world.

---

## Deliberately not claimed

Not a verdict on whether the read-only, verifiable evaluation standard is the
*right* one, or whether mcp-builder should have a separate proof path for
tools that write state — that's Teardown territory; this reel states the
mechanism and the asymmetry, and stops. Not a claim that TypeScript-over-Python
is a bad recommendation — it's stated as the skill's own default, not judged.
Not a full accounting of every phase at equal depth — project structure, the
API client, and the MCP Inspector review step are part of the source skill but
compressed out of this 7-beat Plain cut.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #MCP #ModelContextProtocol #AIagents #AgenticAI #ClaudeSkills #HumanitariansAI #ProfessorBear #ClaudeBasics

---
