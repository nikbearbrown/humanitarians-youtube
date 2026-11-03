# A Plan, Not a Guess. — The Claude Margin Analyzer Skill

When you ask Claude to check your profit margins, it isn't improvising a
method from scratch — it's following a written plan. A Skill is a folder
Claude reads before it works: this one is margin-analyzer, and its SKILL.md
file holds the whole instruction set in plain language, no hidden code.
The instructions live in a numbered Steps section, executed straight
through, no branching unless a step says otherwise. That's what makes
margin-analyzer a plan and not a guess — every run checks the numbers the
same way, in the same order, which is what makes the result repeatable.
It's also the limit: anything the plan doesn't cover, the skill doesn't do.

**Topic:** MARGIN-ANALYZER · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-margin-analyzer

---

## Chapters

0:00 The naive framing: "does Claude invent a plan for my margins?"
0:09 A skill is a folder
0:26 Steps, in order
0:36 Repeatable — and limited
0:50 Carry-out
0:58 Your turn
1:17 Outro

---

## YOUR TURN

Paste this into Claude: I want a repeatable way to check profit margins
across a list of products, using the cost and price for each one. Write me
a short, numbered set of steps — like a Skill file — that says exactly
what to check, in what order, so running it twice on the same numbers
gives the same answer. Then tell me one thing that plan wouldn't catch.

Run that today, on your own product list, not the video's example.

---

## Deliberately not claimed

The margin-analyzer Skill's own SKILL.md — what it specifically checks,
step by step — was not available to this production (see BUILD-LOG.md).
This video states only what its name and small-business category support
(checking profit margins) and flags that inference once on screen, plus
the generic Skill mechanism its source teardown states directly: a
folder Claude reads, a SKILL.md instruction set, and a numbered, linear
Steps section. No specific business logic (formulas, fields, thresholds)
is claimed.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
