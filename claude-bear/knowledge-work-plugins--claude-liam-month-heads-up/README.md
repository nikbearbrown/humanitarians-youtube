# Claude, Month Heads Up.

A named Claude skill like `month-heads-up` isn't code Claude wrote on the
fly — open the folder and there's no hidden script computing the cash-flow
numbers. One item sits there: a `SKILL.md` file, about two kilobytes of
plain language. Claude reads that file itself and treats it as the
program. The pipeline lives in the Steps section, and Claude runs it top
to bottom — linear, no branching unless a step says so. Ask for the month
check on the 25th with the default 30-day horizon, and it reads the file,
works through each step in order, and flags what needs attention before
month-end. Ask for that same 30-day check again and the answer comes back
identical — not because Claude re-examined the cash flow with fresh
judgment, but because the exact same steps ran a second time. Switch the
horizon to 60 days instead, and the output changes — not because the
logic changed, but because a different input ran through those same fixed
steps.

**Topic:** MONTH-HEADS-UP · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-month-heads-up

---

## Chapters

0:00 Claude built the month-heads-up skill. Right?
0:12 No hidden script — one item, that's all
0:26 Request in, steps in order, output out
0:43 Same steps, every time
1:10 Carry-out
1:24 Your turn
1:43 Outro

---

## YOUR TURN

"Open the month-heads-up skill folder. Before you run anything, read me
the SKILL.md and tell me, in your own words, what steps it says to
follow, in order."

Why it's worth running: it forces Claude to surface the actual instruction
set in its own words before acting on it — the same explain-first habit
that makes a deterministic skill auditable rather than a black box.

---

## Deliberately not claimed

Not how month-heads-up computes a cash-flow outlook — the source states
only that Claude reads the Steps section and executes it in order, never
the arithmetic behind "cash-flow outlook," and this reel doesn't invent
it either. Not a verdict on whether the skill's design is good — that's
Teardown territory; this reel states the mechanism and stops.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
