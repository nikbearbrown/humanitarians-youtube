# Decide First. — The Build MCP Server Skill (Deployment & Tool Design)

When you ask Claude to build an MCP server, it doesn't start writing code —
it asks four questions first: deployment, users, how many actions, and
auth. There are three deployment paths, ranked by preference: remote HTTP
wins by default for anything wrapping a cloud API, MCPB packages a server
for local distribution when it must touch the user's machine, and local
stdio is fine for prototypes but painful to distribute. Tool design has two
patterns: one tool per action under about fifteen operations, or
search-plus-execute for large surfaces so the context window doesn't
flood. And once the server exists, Claude picks a tool by reading its
description, not its name — a description that just restates the tool's
name leaves similar tools indistinguishable.

**Topic:** BUILD MCP SERVER · CLAUDE PLUGIN
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-build-mcp-server

---

## Chapters

0:00 The naive framing: "what do I code first?"
0:09 Three deployment paths
1:01 Two tool-design patterns
1:54 The description decides
2:14 Carry-out
2:25 Your turn
2:58 Outro

---

## YOUR TURN

Paste this into Claude: Build an MCP server that wraps the GitHub API —
tools for creating issues, searching repositories, and getting pull
request details. Then watch four things: does it ask discovery questions
before writing any code, or start scaffolding right away? Does it
recommend remote HTTP as the default, and say why? Does it use one tool
per action, since three tools is well under the search-plus-execute
threshold? And are the tool descriptions specific enough to tell
create-issue apart from update-issue?

Run that today, on your own API idea, not the video's example.

---

## Deliberately not claimed

No claim about how Claude's internal dispatch mechanism scores tool
descriptions against each other — the source Skill doesn't document that
mechanism, and this video doesn't guess; it only states that the
description is what Claude reads. No claim that three deployment paths or
two tool-design patterns are the only ways to build an MCP server; they're
the paths and patterns this particular Skill version recommends.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #MCP #LLM #HumanitariansAI #ProfessorBear

---
