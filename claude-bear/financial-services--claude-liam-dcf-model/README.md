# Is Claude's DCF Number Its Own Judgment?

Ask Claude to build a DCF valuation and it's tempting to picture it forming
an opinion about the company — the way an analyst who's studied the
business reaches a conclusion. That's not what's happening. Anthropic's
`dcf-model` skill retrieves financial data, projects cash flows, and
discounts them back to today using a fixed formula built around one
number: the discount rate, WACC. Watch the anchor: turn that dial, and the
valuation follows it every time — the same dial a sensitivity analysis
turns, again and again. A number that swings a lot for a small assumption
change isn't a broken model — the input was never precise to begin with.
And a number that holds steady doesn't prove it's right either — the
terminal value, which usually carries most of the total, is still just a
guess about the distant future. A DCF number is Claude running your
assumptions through a formula, not its opinion of what a company is worth.

**Topic:** DCF-MODEL · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-dcf-model

---

## Chapters

0:00 What decides what it's worth — judgment?
0:11 Judgment, or a formula?
0:32 One dial, one number
0:46 The same dial, turned again
1:08 Carry-out
1:19 Your turn
1:40 Outro

---

## YOUR TURN

"Give Claude a simple set of DCF assumptions — a growth rate, a discount
rate, a terminal growth rate — and ask it to run the dcf-model skill and
value a hypothetical company. Then change only the discount rate by one
point and watch how far the number moves."

That's the fastest way to see how much of a DCF number is assumption
rather than analysis — instead of trusting the precision of the output.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-dcf-model`) in the Plain register for a general audience. The
underlying facts are unchanged from the source: the skill retrieves
financial data, builds cash flow projections with WACC calculations, runs
a sensitivity analysis, and outputs an Excel model — it does not form an
independent opinion about the company, invent growth assumptions, or
reason about the business beyond what it was given. This script makes no
claim about any specific company, dollar figure, or spreadsheet UI — only
the general mechanism (a formula that converts assumptions into a number)
and its two failure directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #FinancialModeling #DCF #FinTech #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
