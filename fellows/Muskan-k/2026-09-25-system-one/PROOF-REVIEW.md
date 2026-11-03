# Feedback: "System One." — Muskan (@HumanitariansAI), film 1

**Verdict:** clear-for-public. **Teaching 11/12.** Production gate **PASS.**
One line: *This film explains what a System One model is and delivers a genuinely
reusable mental model — because it defines the thing (typed decision, not text)
before any example and stress-tests it with a real boundary — but its worked
example uses illustrative values rather than a captured live call, and it never
puts its source on screen.*

## Rubric — does this explainer actually teach?

| Criterion | What it means | This cut |
|---|---|---|
| **Explicit framework** | organizing idea shown as structure *before* examples | **2** — B01 defines it (state → typed answer + probability) and B02 draws the LLM-vs-System-One split, both well before the refund example. |
| **Reusable rubric** | a viewer could apply the axes to a new case | **2** — "does it generate text you parse, or return a typed decision?" + B06's decide-vs-write test lets a viewer classify any tool. |
| **Worked example** | one case walked through the framework — the reasoning, not the conclusion | **1** — B05 walks the refund workflow (state → 3 typed questions → code routes), which is the method applied; but the values are illustrative (per the docs), not a captured Jev call. |
| **Falsifiability / edge case** | framework stress-tested against a boundary | **2** — B06 names what it is NOT (can't write replies, code, or explanations → that's an LLM); B04 adds the calibration boundary. |
| **Active task** | CTA requires structured *doing* | **2** — B08: find a chatbot you're parsing for a decision, write the typed question + the escalate threshold. Concrete and runnable. |
| **Friction** | viewer must resolve a tension, not just receive facts | **2** — B04 forces the reconcile: "95% doesn't mean this one is right" (calibration holds across groups, not per answer). |

**Total: 11 / 12** (ship bar is 8).

## Production gate (binary)
- **Evidence legible at assertion** — **PASS.** Held 4K cards; the definition, the
  three primitives, the calibration caveat, and the refund workflow are all on
  screen and legible when named.
- **Sources on screen** — **PASS, with a caveat.** The whole reel makes claims
  about one commercial product (TypeSafe's System One / Jev). The concepts are
  shown as artifacts (primitive cards, the workflow), but the *source* is never
  cited on screen. For a video that is entirely about one vendor's model, a small
  "Source: TypeSafe — System One docs" would make it pass its own "no source, no
  verdict" standard cleanly. Flagged below.
- **Side-by-side at comparison** — **PASS.** B02 (LLM vs System One) and B06
  (write vs decide) show both sides together, held.

Gate: **PASS.**

## The problem (single biggest fix)
The reel asserts specific facts about a named product with **no on-screen source**.
It's believable and shown as artifacts, but a skeptical viewer can't verify where
"calibrated," "Noul," or "jev-latest" come from.

## Do X next
1. **[EDIT]** Add a small source citation once — on B01 or the verdict: "Source:
   TypeSafe — System One docs." Closes the sources-on-screen gap.
2. **[RESHOOT / NEW SOURCE]** Make B05 a *captured* Jev call (real request + typed
   response) instead of illustrative values → worked-example goes to full strength
   (12/12). Optional under the free-pipeline REBUILD LAW; the current schematic ships.
3. **[EDIT]** Optional: note in B01 that Jev is **text-input only today** if you
   want to pre-empt "can it take images?" — currently omitted to avoid dating.

## What works (keep)
- **Framework-first.** "A typed decision, not text" lands before any example — the
  move most product explainers skip.
- **The calibration beat (B04).** "Confident ≠ correct; calibrated across groups"
  is the honest, memorable, rarely-taught point.
- **The decide-vs-write boundary (B06).** Tells the viewer exactly when NOT to use it.
- **The scaffolded handoff (B08)** — a real exercise with an escalate threshold.
- House fidelity: cream/ink/terracotta, EB Garamond, one accent per beat, legible 4K.
