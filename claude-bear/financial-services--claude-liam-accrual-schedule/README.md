# How Does Claude Build an Accrual Schedule?

Ask Claude to build a period-end accrual schedule and it's tempting to
picture it deciding, from its own accounting judgment, which expenses and
revenues belong in the close. That's not what's happening. Anthropic's
`accrual-schedule` skill reads a written SKILL.md and, for each accrual,
computes the entry and cites the support document that backs it — nothing
more. Watch the anchor: a December utility bill that won't be billed
until January — identified, computed, cited, drafted — then it stops,
waiting for approval. A drafted JE with a citation isn't the same as a
correct entry, and an accrual with no draft this period doesn't always
mean something broke. A drafted accrual JE is the numbers you gave it,
tied to cited support — not Claude's judgment about what you owe.

**Topic:** ACCRUAL-SCHEDULE · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-accrual-schedule

---

## Chapters

0:00 What decides an accrual — judgment?
0:11 Judgment, or a written procedure?
0:29 One accrual, four stops
0:47 Drafted, waiting
1:10 Carry-out
1:21 Your turn
1:42 Outro

---

## YOUR TURN

"Give Claude one expense that belongs in this period's close, with the
invoice or contract as its support, and ask it to run the
accrual-schedule skill: compute the entry, cite that document, and draft
the JE. Then remove the supporting document and ask it to try the same
accrual again."

Watching what happens when the cited document disappears is the fastest
way to see that the skill computes from support, instead of judgment —
rather than just trusting that it does.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-accrual-schedule`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
builds the period-end accrual schedule by computing an entry and citing
its support for each accrual — it does not decide what counts as an
accrual, invent dollar amounts, or exercise accounting judgment beyond
what the template and your inputs already define. This script makes no
claim about specific accounts, ledgers, or UI — only the general
mechanism (a written procedure that computes and cites) and its two
failure directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #Accounting #FinTech #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
