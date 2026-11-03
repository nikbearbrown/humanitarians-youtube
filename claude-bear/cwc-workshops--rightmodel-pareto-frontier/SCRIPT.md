# SCRIPT — The Pareto Frontier: Finding the Cheapest Model That Solves Your Task

*Reel: cwc-workshops--rightmodel-pareto-frontier*
*Skill: `hai-simple`. Register: **Plain** — explain, then stop.*
*Voice: Liam (Kokoro am_onyx), in for Bear.*
*Redo of: `anthropics/cwc-workshops/youtube/rightmodel-pareto-frontier` (Teardown → Plain; same worked example and numbers, judgment removed).*

---

## B00 — HESITANT WRITER (Remotion)

*(Writer types the naive claim, hesitates on "smartest", corrects to
"frontier", then lands the real question.)*

**Liam:** "A newcomer might think the smartest model is always the right
pick. It's not the smartest — it's the frontier: the cheapest model that
still clears your bar. So which model actually belongs there?"

---

## S01 — Stakes

Three Claude models can do your task — Opus, Sonnet, Haiku — and trying all
three, on real traffic, before you decide is expensive.

---

## S02 — Wrong Guess (planted)

The natural read: grab Opus for the accuracy, or grab Haiku for the price.
Either extreme feels like the safe choice.

---

## S03 — ANCHOR PLANTED

*(THE ANCHOR. This exact frontier-curve composition returns at S08, abstract
here, with real dots there.)*

Hold onto one shape: the pareto frontier — the curve of models where you
can't buy more accuracy without paying more, or cut cost without losing it.

---

## S04 — Break the Wrong Guess

Test a real task — customer-support classification — and both extremes lose:
Opus's extra accuracy costs double Sonnet's price for the same job; Haiku
saves three cents but drops eight points.

---

## S05 — Mechanism (part 1)

Finding the frontier takes a sweep: run every model on the same eval suite,
and record two numbers per model — accuracy, and cost per call.

---

## S06 — Mechanism (part 2)

Plot accuracy against cost. A model sits on the frontier only if no other
model beats it on one axis without losing on the other.

---

## S07 — Mechanism (part 3 — ONE FLAG)

*(THE ONE FLAG — these are the source's own illustrative numbers, marked
relative, not live pricing.)*

The plain numbers for this example: Opus runs fifteen dollars in, seventy-five
out per million tokens; Sonnet, three and fifteen; Haiku, a quarter and a
dollar-twenty-five. Quality: ninety-eight, ninety, eighty-two percent. Check
current pricing before you decide — these numbers move.

---

## S08 — ANCHOR PAYOFF

*(THE FRONTIER CURVE RETURNS — same shape as S03, now with real dots.)*

Same shape, real dots: Haiku, one cent, eighty-two percent. Sonnet, four
cents, ninety percent — on the frontier. Opus, eight cents, ninety-eight.
Sonnet saves four thousand dollars per hundred thousand calls.

---

## S09 — Both Directions (A)

Need ninety-five percent or higher? The frontier only has one point that
clears it — Opus. There, the extra cost is the price of the accuracy you
actually need.

---

## S10 — Both Directions (B)

Eighty-two percent is enough for your task? Then Haiku is the frontier
point, and Sonnet's extra accuracy is money you didn't need to spend.

---

## BCRY — Carry-Out (Remotion)

The right model isn't the smartest one or the cheapest one — it's whichever
one sits on the frontier for your task, and a sweep is the only way to find
it.

---

## BHTF — Your Turn (Remotion)

Your turn. Here's the prompt — read it with me: "Sweep my task across Opus,
Sonnet, and Haiku, plot cost versus accuracy, and tell me which model sits
on the pareto frontier for me." Liam, in for Bear.

---

## BOUT — Outro (Remotion)

The Pareto Frontier: Finding the Cheapest Model That Solves Your Task. Liam,
in for Bear.

---

## Six-move audit

| Move | Beat | Law |
|---|---|---|
| 1 stakes first | S01 | ✓ |
| 2 wrong guess, falsified by a case | S02 (planted) → S04 (broken by: the customer-support eval, where both extremes are dominated) | WRONG-GUESS LAW ✓ |
| 3 mechanism | S05–S07 | ✓ |
| 4 anchor planted + paid off | S03 → S08 (the frontier curve, abstract then with real dots) | ANCHOR LAW ✓ |
| 5 both directions | S09 + S10 | BOTH-DIRECTIONS LAW ✓ |
| 6 carry-out | BCRY | CARRY-OUT LAW ✓ |
| one flag | S07 | see below |

## Deliberately not claimed

- **One flag, at S07.** The per-million-token cost table and the 98/90/82%
  quality figures are the source reel's own worked example, not live,
  current Anthropic pricing. The source narration already self-flagged this
  ("These numbers are relative. Always check current pricing before you
  build. Cost is a variable, not a constraint." — source B05); this redo
  keeps that exact caveat, compressed into S07, rather than presenting the
  figures as current fact. Everywhere else in the reel, the frontier
  *method* — sweep, plot, non-dominated point — is asserted as a general
  mechanism, not an inference, so no further flags are used.
- **No design judgment.** The source Teardown cut carries three "lens" moves
  (Popper: the sweep can overturn the obvious pick; Hume: pricing confidence
  is a property of the current market, not permanent; Plato: the frontier
  artifact isn't the decision itself). This redo keeps the underlying facts
  those moves were built on — S04's "not always obvious before the sweep,"
  S07's pricing caveat — but drops the philosophical framing and the verdict
  language entirely, per Plain register.
- **No invented model names or UI.** Opus, Sonnet, and Haiku, and the
  cost/quality figures, are exactly the source's own worked example. Nothing
  new is invented.
- **Beat count: 14** (B00 + S01–S10 + BCRY + BHTF + BOUT), matching the
  hai-simple lineage's documented shape. The source Teardown cut runs
  B00–B10 + BVDT/BHTF/BOUT (14 beats including bookends); this redo
  re-segments the same worked example onto Plain's mandatory
  wrong-guess/anchor/both-directions/one-flag structure rather than padding
  with new claims.
