# Return Data. Serve HTML. — The Build MCP App Skill

An MCP app is a standard MCP server that also serves interactive UI —
rendered inline in the chat surface as an iframe. The two-part registration
pattern is the core of it: the tool declares a UI resource and its handler
returns plain data, not the HTML; a separately-registered resource serves
the widget's HTML with the exact MIME type constant. The host sees the
resource URI, fetches the resource, and renders it in an iframe, piping
the tool's return value in through an event. Before building a widget at
all, route correctly: elicitation is spec-native and covers most simple
inputs; build a widget only for searchable lists, visual previews, or
live-updating progress. Two mistakes produce the exact same blank
rectangle with no error message: serving the widget with the wrong MIME
type, or leaving the script bundle un-inlined so the content security
policy blocks it.

**Topic:** BUILD MCP APP · CLAUDE PLUGIN
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-build-mcp-app

---

## Chapters

0:00 The naive framing: "does my tool serve the HTML?"
0:10 Tool returns data · resource serves HTML
0:56 Route first: elicitation, widget, or text
1:44 Two causes, one blank rectangle
2:05 Carry-out
2:16 Your turn
2:52 Outro

---

## YOUR TURN

Paste this into Claude: Build an MCP app with a file-picker widget that
lets someone choose a file from a list a directory-scan tool returns.
Then check four things: does it use two-part registration (a tool with
`_meta.ui.resourceUri` plus a separate resource)? Does the resource use
the exact MIME type constant, not a hand-typed string? Is the ext-apps
bundle inlined at startup instead of pulled from a CDN? And does the tool
still return real text content alongside the widget?

Run that today, on your own MCP server, not just the video's example.

---

## Deliberately not claimed

No claim about how a host's rendering pipeline handles resources beyond
what the Build MCP App Skill documents (the two-part registration, the
exact MIME type constant, the mandatory bundle-inlining step). No claim
that every widget needs every App class method — `sendMessage`,
`updateModelContext`, `callServerTool`, and `openLink` are what's
available, not a checklist every widget must use.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #MCP #LLM #HumanitariansAI #ProfessorBear

---
