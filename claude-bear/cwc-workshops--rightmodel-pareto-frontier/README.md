# The Pareto Frontier: Finding the Cheapest Model That Solves Your Task

Opus, Sonnet, and Haiku can all do your task, at three different prices and
three different accuracies — and testing all three on real traffic before
you decide is expensive. The natural read is to grab Opus for the accuracy,
or grab Haiku for the price. On a real eval, both extremes usually lose:
in a customer-support classification example, Opus's extra accuracy costs
double Sonnet's price for the same job, while Haiku saves three cents but
drops eight points of accuracy. Finding the actual answer takes a sweep —
run every model on the same eval suite, plot accuracy against cost, and
look for the pareto frontier: the models where you can't buy more accuracy
without paying more, or cut cost without losing it. In the worked example,
Sonnet sits on the frontier and saves $4,000 per 100,000 calls over Opus.
But the frontier is task-specific: need 95% or higher, and Opus is the only
point that clears it; if 82% is enough, Haiku is the frontier model and
Sonnet's extra accuracy is money left on the table.

**Topic:** CLAUDE BASICS · PARETO FRONTIER
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/cwc-workshops--rightmodel-pareto-frontier

---

## Chapters

0:00 The naive framing: "just pick the smartest model?"
0:11 Stakes: three models, one task, expensive to try all three
0:19 The wrong guess: grab an extreme (accuracy or price)
0:26 The anchor: the pareto frontier, abstract
0:34 Broken, with a case: both extremes lose on a real task
0:46 Mechanism: the sweep — same suite, two numbers per model
0:54 Mechanism: non-dominated — the frontier rule
1:03 The one flag: illustrative cost/quality numbers
1:18 The anchor returns: real dots on the frontier
1:30 Both directions (A): high threshold, Opus only
1:39 Both directions (B): low threshold, Haiku wins
1:47 Carry-out
1:56 Your turn
2:07 Outro

---

## YOUR TURN

Sweep my task across Opus, Sonnet, and Haiku, plot cost vs accuracy, and
tell me which model sits on the pareto frontier for me.

Run that today, against your own task and your own eval.

---

## Deliberately not claimed

The cost table (Opus $15/$75, Sonnet $3/$15, Haiku $0.25/$1.25 per million
tokens in/out) and the 98/90/82% quality figures are the source reel's own
illustrative worked example, not live current Anthropic pricing — the
source narration self-flagged this ("check current pricing before you
build"), and this redo keeps that exact caveat rather than presenting the
numbers as current fact. Everywhere else, the frontier *method* — sweep,
plot, non-dominated point — is stated as a general mechanism, not this
reel's inference. The source Teardown cut's three philosophical framings
(Popper/Hume/Plato lenses) and its verdict language are dropped entirely;
this redo keeps only the underlying facts they were built on. See
BUILD-LOG.md for the full account.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no
account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and
Remotion (motion graphics). No human-performed audio or video in this
production.*

#AI #ClaudeAI #ClaudeModels #ModelSelection #ParetoFrontier #LLM #HumanitariansAI #ProfessorBear

---
