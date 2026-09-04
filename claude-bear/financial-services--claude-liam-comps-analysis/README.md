# Follows the File, Not Its Own Reasoning. — The Comps-Analysis Skill (Anthropic Skills)

When Claude runs an Anthropic Skill, it doesn't reason its way through the
task the way an analyst would. A Skill is a folder — this one is
comps-analysis — with a SKILL.md file inside it that is the full
instruction set. Claude reads the file's Steps section and executes each
step, one at a time, in the order written: linear, no branching unless a
step says to branch. That's what makes it a specification rather than a
suggestion. Run it on the same input twice and you get the same output,
both times — but step outside what the file actually says, and there's
nothing written down to fall back on.

**Topic:** COMPS-ANALYSIS · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-comps-analysis

---

## Chapters

0:00 The naive framing: "does Claude reason through it?"
0:11 A skill is a folder
0:23 Steps, in order
0:34 Spec, not suggestion
0:49 Carry-out
0:59 Your turn
1:15 Outro

---

## YOUR TURN

Paste this into Claude: I want to run a comps analysis on a public
company. Read the comps-analysis skill and walk me through what you will
do before you do it.

That last clause matters — asking Claude to explain first, before it runs,
is what actually shows you the steps the file wrote for it. Run that
today, on a company you're actually curious about.

---

## Deliberately not claimed

No claim about which specific financial multiples or data sources the
comps-analysis Skill computes — the source reel's own generated script had
an unfilled template placeholder exactly where that detail would have gone
(confirmed against the source's `PEDAGOGY.md`, which logs only "Batch
build — skill teardown format", and the source's `source_skill` path,
which doesn't resolve on this machine), so this video keeps every claim at
the level the source actually supports: the generic Skill-execution
mechanism (folder, SKILL.md, Steps section, linear execution, and the
determinism/limit that follows from it) — not the comps-analysis-specific
mechanics that were never actually specified.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #AnthropicSkills #ClaudeSkills #LLM #HumanitariansAI #ProfessorBear

---
