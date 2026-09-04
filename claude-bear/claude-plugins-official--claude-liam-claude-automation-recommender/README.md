# Recommend, Not Install. — The Claude Automation Recommender Skill

The Claude Automation Recommender is a read-only analysis skill: it scans
your codebase for signals — language and framework, existing Claude config,
test setup, CI files, database and API code — then recommends automations
across all five Claude Code extensibility types: Hooks (event-driven),
Subagents (parallel), Skills (deliberately invoked), Plugins (bundles), and
MCP Servers (external tools). It caps each category at one or two
recommendations, the most valuable pick rather than an exhaustive dump, and
tells you that you can ask for more. Here's the catch: recommending isn't
the same as handing you a runnable step. For a subagent, it points at a
template file instead of writing the scaffold inline. For a plugin, it
names the plugin but not the install command. It's read-only end to end —
it never edits your files, and it never finishes that last step either.

**Topic:** AUTOMATION RECOMMENDER · CLAUDE PLUGIN
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-claude-automation-recommender

---

## Chapters

0:00 The naive framing: "will Claude just build it?"
0:10 Five automation types
0:53 Analyze, then cap
1:31 Recommend, not install
1:52 Carry-out
2:02 Your turn
2:24 Outro

---

## YOUR TURN

Paste this into Claude, in any real project: Analyze this codebase and
recommend Claude Code automations. Then check two things the recommender
doesn't always give you: for any subagent it suggests, does it write the
actual agent file, or just point you at a template? And for any plugin,
does it give you the exact install command, or just the plugin's name?

Run that today, on your own project, not the video's example.

---

## Deliberately not claimed

No claim about how the skill ranks candidate signals when a codebase
matches multiple automation types at once — the source Skill doesn't
document an internal priority order beyond the one-to-two-per-category cap,
and this video doesn't guess one. No claim that every plugin or subagent
recommendation lacks a runnable command in every case; the gap described
(a template pointer for subagents, a name without an install command for
plugins) is the pattern the source Skill's own reference structure
produces, not an audit of every possible output it could generate.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
