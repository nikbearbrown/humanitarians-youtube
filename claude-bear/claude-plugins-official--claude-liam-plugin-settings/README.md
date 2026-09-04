# Restart Required. — The Plugin Settings Pattern

A Claude Code plugin's settings live in one file: `.claude/plugin-name.local.md`,
in the project root. It has two parts — YAML frontmatter for structured
settings, and a markdown body for prompts and instructions — and three
things read it: bash hooks, command files, and agent instructions. It's
built to fail safe: design the schema with sensible defaults first, guard
every hook with a quick-exit (check the file exists, check it's enabled,
otherwise exit immediately), and remember the gitignore entry is manual,
not automatic. One gap: a setting configured in one project never carries
over to any other project — there's no plugin-wide switch. And no change
takes effect until Claude Code restarts.

**Topic:** PLUGIN SETTINGS · CLAUDE PLUGINS
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-plugin-settings

---

## Chapters

0:00 The naive framing: "does it apply right now?"
0:13 Anatomy: the file
0:32 Built to fail safe
0:50 One gap
1:04 Carry-out
1:15 Your turn
1:35 Outro

---

## YOUR TURN

Open a Claude Code session and paste this: Add configurable settings to my
plugin: an enabled flag, a validation level, and a max-retries count. Watch
three things. Does the file land in a per-project location, kept out of
git? Does the code guard with a quick-exit — check the file exists, check
it's enabled, before doing anything else? And does everything still work
correctly when the settings file doesn't exist at all?

Run that today, on your own plugin idea, not the video's example.

---

## Deliberately not claimed

No claim about the exact bash parsing patterns (sed frontmatter extraction,
grep field extraction) that the source Skill documents — those are
implementation details for someone writing the hook's shell code, not
facts a general viewer needs to evaluate. No claim that every settings
file needs every frontmatter field the source lists; the pattern
supports structured settings, it doesn't mandate a fixed schema.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
