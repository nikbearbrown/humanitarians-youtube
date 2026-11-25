# PEDAGOGY + PROOF rubric — "Reordering, Not Retrieval" (week-14)

## Act structure (10 beats)
1. **B00 ASK** — is a roadmap just semantic search? the fair test is an ablation.
2. **B01 SETUP** — two arms (retrieval vs method); only difference is the graph.
3. **B02 METRICS** — insertion / broken deps / Kendall-tau / personalization, before any number.
4. **B03 INSERTION** — 34 / 31 prerequisite sections the graph pulls in.
5. **B04 ORDER BROKEN** — retrieval 20/14 broken (17/12 missing + 3/2 mis-ordered) vs method 0/0 (the figure).
6. **B05 REORDER** — Kendall tau −0.44 / 0.00; reshuffle, not insertion; overturns week 5.
7. **B06 PERSONALIZES** — core Jaccard 0.25; 0.615 with shared foundations.
8. **B07 ROBUST** — K-sweep {10,20,30}; method 0 at every K.
9. **B08 HONEST BOUNDARY** — general embedder; draft edges; authoritative CSV; no learning claim.
10. **B09 OUTRO/CTA** — delete it and measure what breaks; sign-off.

## PROOF rubric
- **P — Premise before proof:** B01–B02 give the two arms + metrics before any number (B03+). PASS.
- **R — Real, sourced figures:** every number verified against `ablation_graph_vs_retrieval.json` (FACT-CHECK.md). PASS.
- **O — One honest boundary:** B08 — general embedder, draft edges, mechanism not content, no learning claim. PASS.
- **O — One reusable framework:** to prove a component earns its place, remove it and measure the delta; pick metrics for what it's for; sweep the free parameter; let numbers update earlier claims. PASS.
- **F — Falsifiable / no overclaim:** draft edges never shown as approved; structural result scoped; no learning-outcome claim; photothermal tau stated as 0.0 (uncorrelated). PASS.

## Teaching checks
- Two arms + metrics shown before any number? (B01–B02) ✓
- B04 shows retrieval breaking the order vs method at zero? ✓
- B05 makes the Kendall-tau reorder point and notes it overturns week 5? ✓
- Robustness across K shown? (B07) ✓
- Draft edges never shown as approved; no learning-outcome claim? ✓
- Every figure CSV-reproducible (34/31, 17/12, 3/2, 0/0, −0.44/0.0, 0.25/0.615, K-sweep)? (FACT-CHECK.md) ✓

**VERDICT: PASS** — teaching + fact-check gates cleared; cleared for audio generation. Signed 2026-10-31.
