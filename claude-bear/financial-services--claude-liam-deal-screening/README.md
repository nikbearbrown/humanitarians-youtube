# Screens the Deal. Doesn't Decide It.

Ask Claude to screen a deal and it's tempting to picture it weighing the
opportunity the way a partner would — deciding whether the fund should
pursue it. That's not what's happening. Anthropic's `deal-screening` skill
is a folder Claude reads before it works: the SKILL.md inside is the full
instruction set, in plain language, with no hidden logic. The instructions
live in a Steps section, and Claude reads each step in order and runs it —
linear, one after another, unless a step itself says to branch. The
skill's job is specific: extract the deal's key metrics from inbound CIMs,
teasers, and broker materials, run them through a pass/fail framework
against the fund's investment criteria, and output a one-page screening
memo — the same way on every run. What isn't in the SKILL.md's steps isn't
part of the job. deal-screening doesn't decide if you should do the deal —
it runs the file's fixed checks on it, the same way every time.

**Topic:** DEAL-SCREENING · FINANCIAL SERVICES SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-deal-screening

---

## Chapters

0:00 The naive framing: "does it decide this deal?"
0:10 A skill is a folder
0:23 One step at a time
0:32 Screens, every time
0:51 Carry-out
1:01 Your turn
1:16 Outro

---

## YOUR TURN

Paste this into Claude: "I want to quickly screen inbound deal flow —
CIMs, teasers, and broker materials — against my fund's investment
criteria. Read the deal-screening skill and walk me through what you will
do before you do it."

That last clause matters — asking Claude to explain first surfaces the
actual steps it's about to run, before it runs them.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-deal-screening`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
extracts deal metrics and runs a fixed pass/fail framework from its
SKILL.md against stated investment criteria — it does not exercise
independent judgment about whether the deal is a good one, weigh
qualitative factors the steps don't specify, or make the call on whether
the fund should proceed. This script makes no claim about any specific
deal, fund, or investment criteria beyond the general mechanism (a written
procedure Claude reads and executes) and its one stated limit (only what
the file says).

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #FinTech #PrivateEquity #DealFlow #AIagents #HumanitariansAI #ProfessorBear #ClaudeBasics

---
