# What Actually Happens When Claude "Initiates Coverage"?

Ask Claude to initiate coverage on a stock and it's tempting to picture it
generating the whole research report in one continuous pass. That's not
what's happening. Anthropic's `initiating-coverage` skill reads a written
SKILL.md and runs exactly five fixed tasks, in order — company research,
financial modeling, valuation analysis, chart generation, final report
assembly — each one executed individually with its prerequisite verified
first. Watch the anchor: one ticker's coverage package moving through all
five task-cards, each waiting for the one before it to hand over a
verified deliverable before it starts. Finishing the chain proves the
order was respected — no step ran on a missing input. It doesn't prove
the analysis inside each step was sound, and a task refusing to start on
a missing deliverable isn't evidence the earlier research was bad.
Initiating coverage doesn't mean Claude writes a report in one pass — a
finished report means the chain completed end to end, not that a person
checked the assumptions inside it.

**Topic:** INITIATING-COVERAGE · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-initiating-coverage

---

## Chapters

0:00 What produces the report — instantly?
0:11 One pass, or five tasks?
0:39 One package, five tasks
1:06 Finished, with a catch
1:35 Carry-out
1:51 Your turn
2:10 Outro

---

## YOUR TURN

"Pick a public company you know. Ask Claude to research the company,
sketch a simple financial projection, then value it from that
projection — and have it show you each step's output before starting the
next. Then ask it to skip straight to the valuation without the
projection step, and watch what happens."

Watching a step refuse to produce something real when its input is
missing is the fastest way to see that the workflow enforces order and
dependency, rather than just trusting that it does.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-initiating-coverage`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
runs company research, financial modeling, valuation analysis, chart
generation, and final report assembly as five ordered tasks with verified
prerequisites — it does not check whether the analysis inside any task is
correct, only that the dependency chain was respected. This script makes
no claim about any specific company, ticker, or report format — only the
general mechanism (a dependency-gated five-task pipeline) and its two
failure directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #FinTech #EquityResearch #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
