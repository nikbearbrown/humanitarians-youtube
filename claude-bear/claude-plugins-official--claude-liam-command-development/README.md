# For Claude, Not For You. — The Command Development Skill

A slash command is a Markdown file with YAML frontmatter, and its body is a
directive TO Claude — not a message to the user. Commands live in three
places: project commands, shared with the team and available only in that
project; personal commands, available in every project; and plugin
commands, bundled with an installed plugin. Frontmatter carries five
fields: description, allowed-tools, model, argument-hint, and
disable-model-invocation. Arguments come two ways — dollar-ARGUMENTS
captures everything as one string, dollar-1/dollar-2 capture individual
pieces — and an at-sign reads a file, static or argument-driven. Plugin
commands get CLAUDE_PLUGIN_ROOT for portable, hardcode-free paths. One gap:
the most useful dynamic trick — inline bash execution — isn't shown where
you'd look for it.

**Topic:** COMMAND DEVELOPMENT · CLAUDE PLUGIN
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-command-development

---

## Chapters

0:00 The naive framing: "is it written for the user?"
0:10 Anatomy: locations + fields
0:33 Arguments + file refs
1:09 One gap
1:28 Carry-out
1:35 Your turn
2:09 Outro

---

## YOUR TURN

Open a Claude Code session and paste this: Create a slash command called
review-pr that takes a PR number as an argument, reads the changed files,
and reviews them for code quality. Watch four things. Does the command body
tell Claude what to do, or describe what will happen to you? Does it use
dollar-ARGUMENTS or dollar-1 for the PR number, with argument-hint set?
Does it use allowed-tools to restrict what it can touch? And if you ask it
to add bash execution to pull the PR diff dynamically, does it show you the
syntax inline, or send you to a reference file?

Run that today, on your own plugin idea, not the video's example.

---

## Deliberately not claimed

No claim about how "flat vs. namespaced" file layouts get chosen — the
source Skill doesn't compare that decision inline, and this video doesn't
guess at it. No claim that every command needs every frontmatter field;
the five fields are the complete set the format supports, not a checklist
every command must fill in.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
