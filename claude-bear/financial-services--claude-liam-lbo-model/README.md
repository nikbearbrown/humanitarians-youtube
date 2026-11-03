# Fills the Template, Doesn't Design the Deal. — The LBO-Model Skill (Anthropic Skills)

When Claude runs an Anthropic Skill, it doesn't design the task's output
the way an analyst would. A Skill is a folder — this one is lbo-model —
with a SKILL.md file inside it that is the full instruction set. Claude
reads the file's Steps section and executes each step, one at a time, in
the order written: linear, no branching unless a step says to branch.
Concretely, this Skill fills in a template's formulas, validates the
calculations against each other, and checks the formatting against a
professional standard — and because it reads the template's own structure
first, it can do that on whatever LBO template you hand it, not just one
fixed layout.

**Topic:** LBO-MODEL · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-lbo-model

---

## Chapters

0:00 The naive framing: "does Claude design the model?"
0:11 A skill is a folder
0:24 Steps, in order
0:35 Fills, validates, formats
0:52 Carry-out
1:05 Your turn
1:22 Outro

---

## YOUR TURN

Paste this into Claude: I want to fill in an LBO model template for a
leveraged buyout deal. Read the lbo-model skill and walk me through what
you will do before you do it.

That last clause matters — asking Claude to explain first, before it
runs, is what actually shows you the steps the file wrote for it. Run
that today, on a template you're actually working with.

---

## Deliberately not claimed

No claim about which specific cells, tabs, or formula conventions the
lbo-model Skill's SKILL.md actually specifies beyond its own frontmatter
description — the source `source_skill` path
(`/Users/bear/Documents/CoWork/.../lbo-model/SKILL.md`) doesn't resolve on
this machine, so this video keeps every claim at the level the source
narration actually and completely supports: the generic Skill-execution
mechanism (folder, SKILL.md, Steps section, linear execution) plus the
three concrete actions the skill's own description names (fill formulas,
validate calculations, check formatting) and its stated template
independence — not any Excel-mechanics detail the source never specified.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AnthropicSkills #ClaudeSkills #LLM #HumanitariansAI #ProfessorBear

---
