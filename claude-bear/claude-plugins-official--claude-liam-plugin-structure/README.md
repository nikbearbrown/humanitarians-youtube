# Claude Plugins, Plugin Structure.

Inside a Claude Code plugin, a lot of paths point at the plugin's own files —
a hook's command, an MCP server's argument, a script reference. Write one of
those by hand, tested once on your own machine, and it looks correct right
up until the plugin installs somewhere else — at which point it silently
finds nothing. There's a variable for exactly this: `${CLAUDE_PLUGIN_ROOT}`.
It resolves, at runtime, to wherever this install actually landed, so a hook
command written as `$CLAUDE_PLUGIN_ROOT/scripts/check.sh` finds its script no
matter where the plugin lives — on your machine, or a teammate's, or anyone
else's. Along the way: the manifest, `plugin.json`, lives inside
`.claude-plugin/` and needs exactly one field, `name`, in kebab-case;
everything else — `commands/`, `agents/`, `skills/`, `hooks/`, an MCP server
file — lives at the plugin's own root, auto-discovered, no registration step.

**Topic:** PLUGIN STRUCTURE · CLAUDE PLUGINS
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-plugin-structure

---

## Chapters

0:00 A hook's path to its own plugin's script — should it be a fixed address?
0:12 One field, one level up — then a tempting shortcut
0:33 The anchor — one variable, resolved at runtime
0:54 A second machine, a second install
1:14 Carry-out
1:23 Your turn
1:44 Outro

---

## YOUR TURN

"Scaffold a plugin with a pre-tool-use hook that calls a helper script, and
an MCP server with a startup argument pointing at a local file."

Watch two things when Claude answers: does the hook's command path use
`${CLAUDE_PLUGIN_ROOT}`, or a path typed straight from this machine? And does
the MCP server's argument do the same?

---

## Deliberately not claimed

Not a verdict on whether the skill's own documentation should have led with
the portability rule, the `SKILL.md` naming requirement, or the MCP-restart
requirement — that's Teardown territory; this reel states the mechanism and
its silent failure mode, and stops. Not that every source gap gets a beat —
the source also names custom-path double-scanning and plugin-name collisions
across installs; this reel foregrounds the portable-path rule as the anchor.
Not a claim that a hardcoded path never works — it works, on the machine
that wrote it, before it breaks anywhere else.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudePlugins #ClaudeCode #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
