# Matched, Not Invented. — The Design System Skill

A skill is a folder Claude reads before it works — this one is called
design-system, and its SKILL.md holds the full instruction set in plain
language, no hidden logic. The pipeline lives in the Steps section: Claude
reads each step in order, then executes it, linearly, unless a step says
otherwise. This particular skill has exactly one job: audit, document, or
extend a design system — checking for naming inconsistencies or hardcoded
values across components, writing documentation for a component's
variants, states, and accessibility notes, or designing a new pattern that
fits the system already there. All of it lives inside that one file's
script, and nothing outside it is invented from scratch. design-system
doesn't invent a new look — it checks your components against the patterns
already in your codebase, and matches or extends what is already there.

**Topic:** DESIGN-SYSTEM · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-design-system

---

## Chapters

0:00 The naive framing: "does taste keep it consistent?"
0:11 A skill is a folder
0:24 Read then execute
0:32 One file, one job
0:53 Carry-out
1:01 Your turn
1:17 Outro

---

## YOUR TURN

Paste this into Claude: Audit my design system for naming inconsistencies
and hardcoded values. Walk me through your plan before you act. That last
clause matters — explaining the plan first surfaces the real constraint
logic, not just a recommendation.

Run that today, on your own project's components, not the video's example.

---

## Deliberately not claimed

No claim about how Claude decides *which* skill to dispatch for a given
request — the source Skill documents its own trigger conditions (naming
inconsistencies, hardcoded values, component documentation, new-pattern
design), not the general dispatch mechanism across all skills. No claim
that every Anthropic skill is built this same way; the folder/SKILL.md/
Steps-section shape described here is this skill's actual structure, not a
claim about the format in general.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
