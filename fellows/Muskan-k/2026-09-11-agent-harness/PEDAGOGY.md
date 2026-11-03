# PEDAGOGY — Agent Harness. (claude-hai · teaching explainer, ~3min)

**The ONE insight:** an "agent" isn't a smarter model — it's a model wrapped in
a **loop** (the harness) with **tools**, that **acts → observes the result →
decides again** until a stop condition. The harness is the part you actually
build and control. The tell vs a chatbot: **where's the loop, and who owns the
stop condition?**

**Audience (HAI):** learners who keep hearing "AI agent" and want a definition
they can apply to a real tool — not hype.

## Act structure (framework-first — built to pass PROOF)
- B00 hook (composer) — frames it as a *test you can run* ✓
- **B01 FRAMEWORK shown BEFORE any example** — agent = model + tools + the loop
  (the harness), as a hero flow diagram ✓
- **B02 THE LOOP** — decide → act → observe → repeat → stop (the mechanism) ✓
- **B03 worked example** — fix a failing test: run → fail → edit → run → green →
  stop; the loop turning on one real task ✓
- **B04 falsifiability / edge case** — chatbot (one turn, no tools, never sees a
  result) vs agent (acts, observes, loops). The friction beat ✓
- B05 why it matters — what the harness owns (tools/stop/errors/memory/guardrails);
  kept tight, not fact-recitation ✓
- B06 verdict (one-page rubric) · B07 HANDOFF (a *scaffolded* task: list the tools
  + write the stop condition) · B08 title outro ✓
- Body B01–B05 = 4K PIL cards; Claude UI only at B00/B06/B07/B08 (ILLUSTRATE LAW).

## PROOF rubric self-check (the six)
- Explicit framework before examples — B01 (lands ~15–18s) ✓
- Reusable rubric — B01 + B06: "where's the loop, who owns the stop?" ✓
- Worked example — B03 walks the reasoning of one real run ✓
- Falsifiability / edge case — B04 chatbot-vs-agent ✓
- Active task — B07 scaffold (tools + explicit stop condition) ✓
- Friction — B04 forces "real agent or costume?"; B07's stop condition is the hard part ✓
- Production gate: no invented stats or product names; claims are definitional;
  evidence on the cards, legible; verdict shows the rubric on screen.

## Correctness (DOUBLE-CHECK LAW — accurate, non-dating)
- No model names, version numbers, or benchmark counts.
- "Agent" defined by architecture (model + tools + observe-decide loop + stop),
  not by any product.
- The loop is described generically (decide/act/observe); the failing-test run is
  a canonical illustrative example, not a claim about a named tool.
- Harness responsibilities framed as categories, no invented metrics.

## Narration review (GATE P)
Listen for: does B01 land the definition BEFORE any example? Does B02 make
"observe" the load-bearing step? Does B04 make "where's the loop / who owns the
stop?" the memorable test? Is B07 a task the viewer can actually run?

VERDICT: PASS
