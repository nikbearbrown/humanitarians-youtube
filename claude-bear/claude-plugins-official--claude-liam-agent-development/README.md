# Describe When, Not What. — The Agent Development Skill (Prose Triggers)

An agent file is two things: YAML frontmatter, then a markdown system-prompt
body. Frontmatter has five fields — name, description, model, color, and
tools — and description is the one that matters most, because it's loaded
into context whenever the agent is registered, so it's what decides whether
Claude dispatches this agent at all. The format here states it directly:
"Use this agent when...", then "Typical triggers include" two to four
concrete scenarios, then a pointer to a When to invoke section in the body.
Two different jobs: the description is for Claude's dispatch decision; the
body's own When to invoke section is for the agent once it's already
running. Here's the catch: nothing keeps the two in sync — if the trigger
scenarios change and only one location gets updated, a scenario that only
lives in the stale one never even gets checked at dispatch time.

**Topic:** AGENT DEVELOPMENT · CLAUDE CODE PLUGIN
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-plugins-official--claude-liam-agent-development

---

## Chapters

0:00 The naive framing: "does listing skills work?"
0:10 Frontmatter: five fields
0:48 Two locations, one job each
1:23 The sync problem
1:49 Carry-out
1:59 Your turn
2:22 Outro

---

## YOUR TURN

Paste this into Claude: Create an agent for my plugin that reviews pull
request diffs for security issues. Then check the description Claude wrote:
does it say "Use this agent when..." with two to four concrete trigger
scenarios, or does it just list what the agent does? Does the body have a
When to invoke section with worked scenarios? Are the tools it picked the
minimum needed — probably Read and Bash, not Write?

Run that today, on your own plugin idea, not the video's example.

---

## Deliberately not claimed

No claim about how Claude's dispatch mechanism decides between candidate
agents internally (pattern-match vs. model judgment) — the source Skill
doesn't document that, and this video doesn't guess. No claim that the
two-location prose-trigger format is the only way to write an agent
description; it's the format this particular Skill version specifies, and
the maintenance-coupling cost described is a property of that specific
two-location design, not a claim about every possible agent file.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
