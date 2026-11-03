# Only Four of the Nine. — The Hook Development Skill (Prompt-Based Hooks)

Claude Code plugins can hook into the session lifecycle two ways: a
Prompt-Based hook, which sends context to Claude and lets it decide what to
do, or a Command hook, which runs a bash script and uses its exit code —
zero for success, two to block, anything else non-blocking. Prompt-Based is
the recommended type. But nine lifecycle events exist, and Prompt-Based
hooks only fire on four of them: PreToolUse, Stop, SubagentStop, and
UserPromptSubmit. Put one on PostToolUse, expecting it to review a tool's
output after the fact, and nothing happens — no error, no warning, it just
never runs. The two config formats aren't interchangeable either: plugin
hooks.json wraps everything under a description and a hooks key, while the
settings file skips that wrapper entirely.

**Topic:** HOOK DEVELOPMENT · CLAUDE PLUGINS
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-hook-development

---

## Chapters

0:00 The naive framing: "does it fire on any event?"
0:10 Two types, two formats
0:58 Nine events, four rules
1:38 The gap
1:59 Carry-out
2:09 Your turn
2:41 Outro

---

## YOUR TURN

Give Claude a plugin that logs every Write tool call to a JSON file, and
blocks any Write to a .env file. Watch four things: does the logging hook
(which fires after the write, on PostToolUse) use a Command hook, since
Prompt-Based won't run there? Does it use CLAUDE_PLUGIN_ROOT instead of a
hardcoded path? Does it use the plugin's hooks.json wrapper format, not the
flat settings format? And does it remind you to restart the session after
editing hooks.json?

Run that today, on your own plugin idea, not the video's example.

---

## Deliberately not claimed

No claim about why the restriction exists internally (why prompt hooks are
architecturally limited to four events rather than nine) — the source
Skill states the restriction, not the reason, and this video doesn't guess
at Anthropic's implementation. No claim that Command hooks are always the
better choice; the video states which four events support Prompt-Based
hooks and leaves the type choice, for events where both are legal, to the
plugin author.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no
account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and
Remotion (motion graphics). No human-performed audio or video in this
production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
