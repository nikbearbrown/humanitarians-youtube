# Only What The File Says. — The Architecture Skill (ADR Decisions)

A skill is a folder Claude reads before it works — this one is called
architecture, and its SKILL.md holds the full instruction set in plain
language, no hidden logic. The pipeline lives in the Steps section: Claude
reads each step in order, then executes it, linearly, unless a step says
otherwise. This particular skill has exactly one job: create or evaluate an
architecture decision record — choosing between technologies, documenting
a trade-off, reviewing a design proposal, or designing a new component from
constraints. All of it lives inside that one file's script, and nothing
outside it is covered. A skill runs the same steps every time you call it
— never a step beyond what its file wrote down.

**Topic:** ARCHITECTURE · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-architecture

---

## Chapters

0:00 The naive framing: "does judgment write the call?"
0:10 A skill is a folder
0:23 Read then execute
0:32 One file, one job
0:48 Carry-out
0:54 Your turn
1:08 Outro

---

## YOUR TURN

Paste this into Claude: Create an ADR for choosing between two technologies
for my project. Walk me through your plan before you act. That last clause
matters — explaining the plan first surfaces the real constraint logic, not
just a recommendation.

Run that today, on your own project's technology choice, not the video's
example.

---

## Deliberately not claimed

No claim about how Claude decides *which* skill to dispatch for a given
request — the source Skill documents its own trigger conditions (choosing
between technologies, documenting a trade-off, reviewing a proposal,
designing from constraints), not the general dispatch mechanism across all
skills. No claim that every Anthropic skill is built this same way; the
folder/SKILL.md/Steps-section shape described here is this skill's actual
structure, not a claim about the format in general.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #LLM #HumanitariansAI #ProfessorBear

---
