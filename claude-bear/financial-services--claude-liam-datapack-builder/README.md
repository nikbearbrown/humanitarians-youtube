# Builds the Data Pack. Doesn't Calculate the Numbers.

Ask Claude to build a financial services data pack and it's tempting to
picture it running the analysis itself — crunching the numbers the way an
analyst would. That's not what's happening. Anthropic's `datapack-builder`
skill is a folder Claude reads before it works: the SKILL.md inside is the
full instruction set, in plain language, with no hidden logic. The
instructions live in a Steps section, and Claude reads each step in order
and runs it — linear, one after another, unless a step itself says to
branch. The skill's job is specific: pull financial data from CIMs,
offering memorandums, SEC filings, web search, or MCP servers, and
standardize it into one investment-committee-ready Excel workbook —
consistent structure, proper formatting, assumptions documented. It's built
for M&A due diligence and portfolio reporting, not for running the
calculations itself or reworking a data pack that's already finished. What
isn't in the SKILL.md's steps isn't part of the job. datapack-builder
doesn't calculate your numbers — it extracts and standardizes them into one
workbook, the same way every time.

**Topic:** DATAPACK-BUILDER · FINANCIAL SERVICES SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-datapack-builder

---

## Chapters

0:00 The naive framing: "does it calculate my financials?"
0:13 A skill is a folder
0:26 One step at a time
0:35 Standardizes, every time
1:01 Carry-out
1:08 Your turn
1:28 Outro

---

## YOUR TURN

Paste this into Claude: "I want to build a financial services data pack
from a CIM, an offering memorandum, and SEC filings for an investment
committee review. Read the datapack-builder skill and walk me through what
you will do before you do it."

That last clause matters — asking Claude to explain first surfaces the
actual steps it's about to run, before it runs them.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-datapack-builder`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
extracts and standardizes financial data by executing a fixed set of steps
from its SKILL.md — it does not exercise independent judgment about the
analysis, invent numbers not given to it, or decide what belongs in the
workbook beyond what the steps specify. This script makes no claim about
any specific deal, company, or data pack beyond the general mechanism (a
written procedure Claude reads and executes) and its one stated limit
(only what the file says, and not the calculations themselves).

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #FinTech #MandA #InvestmentBanking #AIagents #HumanitariansAI #ProfessorBear #ClaudeBasics

---
