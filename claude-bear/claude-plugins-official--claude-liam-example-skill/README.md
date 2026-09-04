# Write Triggers, Not Topics. — The Example Skill (Claude Plugins)

A skill is one file: SKILL.md, inside a folder under skills. Frontmatter has
four fields — name, description, version, and license — and description is
the one that matters most, because it's what Claude reads to decide whether
to activate the skill at all, not a topic you're describing to a person.
The skill's own template states it directly: say it should be used when the
user asks a specific phrase, mentions a keyword, or discusses a topic area.
That's different from a command, which only runs when someone types the
slash, and different from an agent, which Claude spawns to handle a
subtask. Here's the catch: nothing explains how Claude actually matches
your description against a request, and the only testing advice — check
that it activates for expected queries — comes with no method for running
that check. So most authors write a description, ship it, and never
actually see whether it fires.

**Topic:** EXAMPLE SKILL · CLAUDE PLUGINS
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-example-skill

---

## Chapters

0:00 The naive framing: "does a topic description work?"
0:11 SKILL.md: four fields
0:35 Three activation modes
0:58 Write it, ship it, hope
1:20 Carry-out
1:29 Your turn
2:02 Outro

---

## YOUR TURN

Paste this into Claude: build a model-invoked skill for a plugin that helps
with database query optimization. Then check what comes back: does the
description name specific trigger phrases — a phrase someone might say, a
keyword, a topic — or does it just summarize what the skill does? Does it
include a "when to use" section with concrete examples? Did you check
whether it overlaps with any other skill's description? Are references,
examples, or helper scripts split into their own folders, or is everything
crammed into one file? And did you actually test it — hand Claude a
realistic query and watch whether the skill activates?

Run that today, on your own plugin idea, not the video's example.

---

## Deliberately not claimed

No claim about how Claude's matching mechanism actually works internally
(embedding similarity, keyword matching, or exact phrase detection) — the
source reference template doesn't document that, and this video doesn't
guess. No claim that the four-field frontmatter or the "when to use"
prose format is the only way to write a skill description; it's the
format this reference template specifies.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
