# Claude, Financial Statements.

"Material variance" sounds like a judgment call — the kind of read an
experienced accountant makes by feel. It isn't, in a Claude skill.
`financial-statements` is a written spec: a `SKILL.md` file Claude reads
before it works, spelling out the job — build the income statement,
balance sheet, and cash flow statement, compare each period to the last,
and flag variances that cross a threshold the file itself sets. Ask for
financial statements covering the first quarter and Claude works the
Steps section top to bottom, linear, no branching unless a step says so.
Ask for that same quarter again and the flags come back identical — not
because Claude re-judged the numbers, but because the same steps ran a
second time. That cuts both ways: identical flags on identical input
isn't proof Claude understood the business, and a different flag next
quarter doesn't mean the rule changed — same steps, new numbers either
way.

**Topic:** FINANCIAL-STATEMENTS · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-financial-statements

---

## Chapters

0:00 Claude decides what's a material variance. Right?
0:11 No separate judgment module — one file spells out the job
0:31 Request in, steps in order, statements + flags out
0:50 Same steps, every time
1:18 Carry-out
1:30 Your turn
1:48 Outro

---

## YOUR TURN

"Open the financial-statements skill folder. Before you run anything, read
me the SKILL.md and tell me, in your own words, what makes a variance
count as material."

Why it's worth running: it forces Claude to surface the actual rule in
its own words before acting on it — the same explain-first habit that
turns "the AI decided this was material" into an auditable, written
threshold.

---

## Deliberately not claimed

Not the specific numeric threshold, GAAP line items, or exact output
layout the skill's SKILL.md defines for "material" — the source confirms
the skill's documented job (three statements, period comparison, variance
analysis, GAAP presentation/period-end lookups) but never that level of
detail, and no other copy of this skill's SKILL.md exists on this machine
to recover it. This reel does not invent it. Not a verdict on whether the
skill's design is good — that's Teardown territory; this reel states the
mechanism and stops.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
