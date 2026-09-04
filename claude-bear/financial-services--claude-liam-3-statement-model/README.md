# How Does Claude Fill In a Financial Model?

Ask Claude to fill in a 3-statement financial model and it's tempting to
picture it reasoning about the business like an analyst — weighing what
revenue drivers matter, what assumptions are reasonable. That's not what's
happening. Anthropic's `3-statement-model` skill reads a written SKILL.md
and follows a fixed list of steps that link an existing Income Statement,
Balance Sheet, and Cash Flow Statement template together. Watch the
anchor: net income leaves the income statement, lands in retained earnings
on the balance sheet, and shows up again at the top of the cash flow
statement — the same link, every time. A model that ties out isn't the
same as a model that's right, and a blank line doesn't always mean the run
failed. A filled-in model is the numbers you gave it, linked by a fixed
set of steps — not Claude's financial judgment.

**Topic:** 3-STATEMENT-MODEL · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-3-statement-model

---

## Chapters

0:00 What fills in the model — judgment?
0:11 Judgment, or a written list?
0:29 One number, three statements
0:44 Tied out, not necessarily right
1:03 Carry-out
1:13 Your turn
1:32 Outro

---

## YOUR TURN

"Give Claude a simple set of assumptions — one revenue line, one expense, a
starting cash balance — and run the 3-statement-model skill to link the
three statements. Then change one assumption and watch which lines move
and which stay put."

That's the fastest way to see the linkage the skill actually performs,
instead of just trusting that it happened.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-3-statement-model`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
completes, populates, and links 3-statement financial model templates: it
does not decide what belongs in the model, invent assumptions, or reason
about the business beyond what the template and your inputs already
define. This script makes no claim about specific numbers, UI, or output
formats — only the general mechanism (a written procedure that links an
existing template) and its two failure directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #FinancialModeling #FinTech #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
