# PEDAGOGY.md — GATE P — leverage-cuts-both-ways

**Skill:** ai-explainer (short) · **Persona:** Liam, in for Ameya (Onyx, `am_onyx`) · **Channel:** @HumanitariansAI
**Register:** Teardown · **Source:** Computational Finance with Excel, Python & LLMs — Ch.6 (Margin & Short Selling)
**Est. runtime:** ~2:30 (16:9)

GATE P is a QUALITY gate: a human reviews the narration and pedagogy BEFORE any
audio is generated. Not a cost gate — Kokoro audio is free.

## The one thing a viewer should be able to DO after watching
Explain why margin amplifies losses more than the stock's own move, describe what
triggers a margin call, and state why a short position's loss is unbounded while a
long position's is capped at 100%.

## The through-line (promise → trap → forced exit → the mirror → verdict)
1. **B01 promise:** 50% Reg T margin → 2:1 leverage; +10% stock = +20% on cash.
2. **B02 trap:** the loan is fixed, so a −20% stock move is a −40% equity hit.
3. **B03 forced exit:** maintenance margin (30%) → margin call at $14,286 value; the broker controls the exit.
4. **B04 the mirror:** short selling profits when price falls, but loss is unbounded (vs long capped at −100%) → short squeeze.
5. **B05 verdict:** a multiplier, not a strategy.

## Honesty / scope
- All figures sourced from the Ch.6 cheat sheet and independently verified — see [FACTCHECK.md](FACTCHECK.md).
- **Deliberately NOT shown:** the short-selling margin-call *price* — the source
  quotes $72.92 but its own formulas yield different values; per DOUBLE-CHECK LAW
  no disputed number goes on screen. Short selling is taught via the unambiguous,
  correct point (unlimited downside).
- Educational only — not financial advice. Reg T (50%) and FINRA maintenance
  minimum (25%; brokers typically 30–40%) are stated as the rules, with 30% used
  as an illustrative broker maintenance level.

## SHOW-DON'T-TELL check
Every body beat (B01–B05) is a Manim illustration whose motion enacts the
narration (boxes compose, bars diverge, the call fires on the line-cross). The
Claude UI appears only at the cold open (B00), the handoff (B06), and the outro
(B07) — ILLUSTRATE LAW satisfied.

---

**PEDAGOGY VERDICT: PASS** — narration reviewed; numbers verified and sourced;
show-don't-tell and illustrate laws satisfied; cleared for audio generation.
