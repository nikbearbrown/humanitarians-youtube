# Feedback: "Agent Harness." — Muskan (@HumanitariansAI), film 2

**Verdict:** clear-for-public. **Teaching 10/12.** Production gate **PASS.**
One line: *This film attempts to teach what an AI agent actually is and largely
delivers a reusable test — because it defines "a model in a loop with tools"
before any example and stress-tests it against a chatbot — but its worked example
is a scripted card rather than a captured agent run, which caps its friction.*

## Where it improved vs film 1 ("Multimodal AI.")
| Criterion | Film 1 | Film 2 |
|---|---|---|
| Explicit framework | 2 | 2 |
| Reusable rubric | 2 | 2 |
| Worked example | 1 | 1 |
| Falsifiability / edge | 2 | 2 |
| Active task | 2 | 2 |
| Friction | 1 | 1 |
Same ship-quality shape; the worked-example/friction gap is a *standing* pattern
across both films (see note) — worth solving once, not per-film.

## Rubric — does this explainer actually teach?

| Criterion | What it means | This cut |
|---|---|---|
| **Explicit framework** | organizing idea shown as structure *before* examples | **2** — B01 "Model, Wrapped" defines agent = model + tools + the loop (the harness) at ~17s, before any example. |
| **Reusable rubric** | a viewer could apply the axes to a new case | **2** — B01 + B06: "where's the loop, and who owns the stop condition?" — a test applicable to any tool that calls itself an agent. |
| **Worked example** | one case walked through the framework live — the reasoning step | **1** — B03 walks a real task (fix a failing test: run → red → edit → run → green → stop), turn by turn. But it's asserted on a card, not a captured agent run — it teaches the shape, not a live artifact. |
| **Falsifiability / edge case** | framework stress-tested against a counterexample | **2** — B04 sets chatbot (one turn, no tools, never sees a result) against agent (acts, observes, loops), side-by-side. The exact case the hype blurs. |
| **Active task** | CTA requires structured *doing*, not "ask Claude" | **2** — B07: take a stepwise task, list the tools, and write the exact STOP condition. A real design exercise, not a pointer. |
| **Friction** | viewer must resolve a tension, not just receive facts | **1** — "real agent or costume?" is a genuine tension and the stop-condition task creates friction, but the reel resolves the tension for the viewer on screen rather than forcing it. |

**Total: 10 / 12** (ship bar is 8).

## Production gate (binary)
- **Evidence legible at the moment of assertion** — **PASS.** Held 4K cards; the
  definition, the loop, the run, and the chatbot/agent split are on screen and
  legible when the narration names them.
- **Sources on screen, not just voiced** — **PASS (n/a-heavy).** Definitional
  explainer; no external stats or product names to cite, nothing that dates.
- **Side-by-side at the moment of comparison** — **PASS.** B04 holds chatbot vs
  agent together at the moment of contrast.

Gate: **PASS.** The film passes its own standard.

## The problem (single biggest fix)
**B03 is a scripted illustration, not a captured agent run.** The card asserts the
turn sequence rather than showing a real harness looping (a real tool call, a real
observed result). That holds worked-example and friction at 1.

## Do X next
1. **[RESHOOT / NEW SOURCE]** Replace B03 with a real captured agent transcript —
   an actual tool call, the actual result it observed, the actual next action —
   shown as the artifact. Moves worked-example → 2 and friction → 2 (→ 12/12).
   Under REBUILD LAW / the free pipeline a native illustration is the sanctioned
   default, so this is an optional upgrade, not a blocker — the cut ships.
2. **[EDIT]** Sharpen the edge case: add a second failure mode to B04 or the
   verdict — "a loop with no stop condition is a runaway, not an agent" — so the
   test cuts both ways (no loop = chatbot; no stop = runaway).
3. **[EDIT]** B02/B05 portrait cards carry vertical negative space; raise the
   diagram block ~4–6% of frame height for tighter CANVAS-FILL if desired.

## What works (keep)
- **Framework-first + the loop diagram (B02).** Defining the loop as the mechanism,
  before any example, with the terracotta "repeat" arrow — the single clearest,
  most reusable idea in the film.
- **The chatbot-vs-agent tell (B04)** and the two questions ("where's the loop /
  who owns the stop?") — memorable and portable.
- **The handoff (B07)** forces the viewer to write a stop condition — the hardest,
  most instructive part of a harness.
- **House fidelity.** Cream/ink/terracotta, EB Garamond, one accent per beat,
  legible 4K, brand chip throughout.
