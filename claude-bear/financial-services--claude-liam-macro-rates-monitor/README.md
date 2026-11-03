# Does Claude's Macro Rates Dashboard Predict Where Rates Are Headed?

Ask Claude for a macro rates monitor dashboard and it's tempting to picture it
forming its own view on where the economy is headed — reading the data like
an analyst and telling you what's coming. That's not what's happening.
Anthropic's `macro-rates-monitor` skill reads a written SKILL.md and combines
exactly four named inputs — macro indicators, the yield curve, inflation
breakevens, and swap rates — using the definitions already written for them.
Watch the anchor: one pull of market data moving through all four building
blocks, each waiting only for the definition the file gives it, before it
reaches the finished dashboard. Finishing the chain proves the four blocks
were combined the way the file defines them — nothing skipped, nothing
improvised. It doesn't prove the economic read inside the dashboard will hold
up, and a block that can't populate on missing data isn't evidence the other
blocks are wrong. A macro rates dashboard from Claude isn't an original
economic call — a finished dashboard means the combination ran correctly, not
that reality will follow it.

**Topic:** MACRO-RATES-MONITOR · ANTHROPIC SKILL
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/financial-services--claude-liam-macro-rates-monitor

---

## Chapters

0:00 Can Claude predict where rates go?
0:11 Forecast, or four inputs?
0:42 One package, four inputs
1:05 Finished, with a catch
1:30 Carry-out
1:47 Your turn
2:07 Outro

---

## YOUR TURN

"Pick a country or region you follow. Ask Claude to pull together a macro
rates read combining the yield curve shape, inflation breakevens, and swap
rates — and have it show you the definition it's using for each piece before
it combines them. Then ask it what the central bank will actually do next
quarter, and watch what it can and can't answer."

Watching the dashboard combine the four defined inputs cleanly, then watching
the same request stall on an actual forecast question, is the fastest way to
see the line between "combines what's defined" and "predicts what isn't."

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-macro-rates-monitor`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
combines macro indicators, the yield curve, inflation breakevens, and swap
rates into a dashboard as four named inputs, per a fixed procedure — it does
not check whether the economic read inside the dashboard is correct, only
that the four inputs were combined per their definitions. This script makes
no claim about any specific country, central bank, or dashboard layout —
only the general mechanism (a fixed four-input combination procedure) and
its two failure directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #FinTech #MacroEconomics #FixedIncome #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
