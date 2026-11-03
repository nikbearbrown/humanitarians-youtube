# PEDAGOGY — Mixture of Experts. (claude-hai · teaching explainer, ~2.5min)

**The ONE insight:** MoE pulls **capacity apart from cost**. Many expert sub-networks
plus a router that picks a few per token — so the model's **total** params (capacity,
all in memory) can be huge while its **active** params (compute per token) stay small.
The catch: every expert still has to live in memory.

**Audience (HAI):** learners who see giant parameter counts and need to know what they
actually cost to run.

## Act structure (framework-first — built to pass PROOF)
- B00 hook (composer) — huge model, small cost: how? ✓
- **B01 FRAMEWORK** — many experts + a router; only a few run per token (dense vs MoE) ✓
- **B02 THE REFRAME (rubric)** — total params (capacity, memory) vs active params (compute) ✓
- **B03 worked example** — one token routed to the top-2 experts; next token picks others ✓
- **B04 falsifiability / edge (the trade)** — all experts in memory, routing imbalance,
  "not smarter, cheaper per token" ✓
- B05 verdict · B06 handoff (read total vs active) · B07 outro ✓
- Body B01–B04 = 4K PIL cards; Claude UI only at B00/B05/B06/B07 (ILLUSTRATE LAW).

## PROOF rubric self-check
- Explicit framework before examples — B01 + B02 ✓
- Reusable rubric — "total vs active params" lets a viewer judge any model's real cost ✓
- Worked example — B03 (one token's routing, the reasoning) ✓
- Falsifiability / edge — B04 (MoE isn't free; memory + routing are the costs) ✓
- Active task — B06 (ask for a model's active-per-token count, not just total) ✓
- Friction — B02 / B04 force separating capacity from cost, and "not smarter" ✓
- Production gate: qualitative only (no param counts, benchmarks, model names);
  top-2 routing flagged as an illustrative typical; the diagrams are the evidence.

## Correctness (DOUBLE-CHECK LAW — accurate, non-dating)
- Dense model: all parameters active per token. MoE: experts + a gating/router; top-k
  (commonly 1–2) experts run per token; outputs combined. "Top 2 of dozens" is
  illustrative, not a claim about a specific model.
- Total params = sum of all experts (capacity, must be resident in memory/VRAM).
  Active params = only the routed experts (sets compute + latency).
- Costs are real: all experts occupy memory even when idle (serving is memory-heavy);
  routers can collapse onto a few experts, needing load-balancing during training.
- No FLOPs, no parameter counts, no model names — kept qualitative to avoid dating.

## Narration review (GATE P)
Listen for: does B02 land "total vs active" as the lens BEFORE the routing example?
Does B04 make clear MoE trades memory for compute (not "smarter")? Is B06 a question
the viewer can actually ask of a real model?

VERDICT: PASS 