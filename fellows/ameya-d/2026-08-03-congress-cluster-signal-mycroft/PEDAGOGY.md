# PEDAGOGY.md — GATE P — congress-cluster-signal

**Skill:** cli-explainer · **Persona:** Liam, in for Ameya (Onyx, `am_onyx`) · **Channel:** @HumanitariansAI
**Register:** Teardown · **Est. runtime:** ~3:30 (16:9)

GATE P is a QUALITY gate: a human reviews the narration and pedagogy on this
sheet BEFORE any audio is generated. It is not a cost gate — Kokoro audio is free.

## The one thing a viewer should be able to DO after watching
Distinguish a *cluster* congressional buy (≥2 members converging on one ticker in
30 days) from a solo buy, and understand why the first carries a small, real edge
and the second doesn't — and why "copy Congress" apps overpromise.

## The through-line (problem → build → run → check → change → meaning → next)
1. **PROBLEM (B01):** The STOCK Act made congressional trades public; the popular
   claim is "Congress beats the market." Testable question: does mechanically
   copying their buys beat the index?
2. **BUILD 1 (B02–B03):** Strict per-trade market adjustment — 30-day return from
   the *disclosure* date minus SPY over the identical window (`market_adjusted.py`).
3. **RUN 1 (B04):** Aggregate BUY alpha = +0.13%. Congress rides the market.
4. **CHANGE (B05–B06):** The revision — tier every buy at entry by cluster
   convergence, no look-ahead (`backtest.py: tag_signal`).
5. **RUN 2 (B07):** Cluster tiers (STRONG/WATCH) earn positive alpha and ~50% win;
   solo goes negative and ~45%. The ~5-pt win gap is the result.
6. **MEANING (B08):** The edge is cluster *membership*, not the conviction score
   (WATCH > STRONG). A noise filter, not a profit engine. Not financial advice.
7. **NEXT (B09):** Viewer prompt — rerun the cluster test on the last 90 days of
   filings.

## Accuracy / honesty review (DOUBLE-CHECK LAW)
- All numbers sourced in `SOURCES.md`, traced to `RESEARCH_REPORT.md` and the
  actual code. ✔
- Code beats (B03, B06) show REAL trimmed source, not pseudocode — ACTUAL-CODE
  LAW. ✔
- Limitations stated in-reel: small magnitude, small-sample fragility (64 vs 108),
  score non-monotone, correlation not causation. ✔ (B08)
- Compliance line ("research/education only, not financial advice") spoken in
  B08. ✔ — this reel does NOT give personalized investment advice; it reports a
  published backtest.
- No drift-prone live figures or model version numbers on screen. ✔

## Revision requirement (cli-explainer)
16:9 cut contains one full revision cycle: B05 (change) → B06 (revised code) →
B07 (better/deeper output). ✔

## Narration review
Teardown register: explains the machinery (the subtraction, the entry-time
tiering), names the trade-off (edge is real but tiny; membership not conviction),
strips hype ("Congress beats the market" is examined, not parroted). Forbidden
phrases checked. IN-FOR-BEAR LAW: B00 and B10 sign off "Liam, in for Bear." ✔

---

**Reviewer:** Ameya Deshmukh (author of the underlying study)
**VERDICT: PASS**

> Narration is accurate to the paper, the code shown is real, limitations and the
> not-financial-advice caveat are spoken aloud, and the build reconstructs the
> actual pipeline. Cleared for audio generation.
