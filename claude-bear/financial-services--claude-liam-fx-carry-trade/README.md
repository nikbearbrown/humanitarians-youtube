# Is Claude Calculating an FX Carry Trade, or Following a Skill?

Ask Claude to evaluate an FX carry trade and it's tempting to picture it
calculating the trade itself — weighing the market like an analyst. That's
not what's happening. Anthropic's `fx-carry-trade` skill reads a written
SKILL.md and follows its Steps section in order, combining spot rates,
forward points, interest rate differentials, volatility surface analysis,
and historical price trends exactly as specified. Give it those same
inputs and it returns the same result every time; ask it something the
file doesn't cover and it has nothing to say. A skill is a spec Claude
follows exactly — not judgment, not intuition — and everything it does
traces back to what's written in that one file.

**Topic:** FX CARRY TRADE · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-fx-carry-trade

---

## Chapters

0:00 Ask Claude to evaluate a carry trade
0:12 A skill is a folder
0:25 The pipeline: read, execute, return
0:33 What the skill does
0:53 Carry-out
1:01 Your turn
1:20 Outro

---

## YOUR TURN

"I want to evaluate an FX carry trade using spot rates, forward points,
interest rate differentials, volatility, and historical price trends.
Walk me through what you'll check, step by step, before you calculate
anything."

That's the fastest way to see which inputs the skill actually checks,
instead of just trusting that it happened.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-fx-carry-trade`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
evaluates FX carry trade opportunities by combining spot rates, forward
points, interest rate differentials, volatility surface analysis, and
historical price trends; it does not exercise financial judgment, does
not source live market data itself, and only covers what its SKILL.md
specifies. This script makes no claim about specific trades, returns, or
investment outcomes — only the general mechanism (a written specification
Claude follows exactly) and its scope.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ForeignExchange #FX #FinTech #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics
