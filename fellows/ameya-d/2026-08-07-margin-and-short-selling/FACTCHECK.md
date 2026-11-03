# FACTCHECK.md — leverage-cuts-both-ways

Each on-screen / narrated claim, its verdict, and an independent re-derivation.
Source map in [SOURCES.md](SOURCES.md). Primary: Computational Finance Ch.6.

| Beat | Claim | Verdict | Check |
|------|-------|---------|-------|
| B00/B01 | Reg T initial margin = 50% | ✅ TRUE | §6.2 / §6.4 |
| B01 | $10k cash → $20k position, $10k loan (2:1) | ✅ TRUE | 10,000 / 0.50 = 20,000; loan = 20,000 − 10,000 = 10,000 |
| B01 | stock +10% → +$2,000 = +20% on cash | ✅ TRUE | 0.10 × 20,000 = 2,000; 2,000 / 10,000 = 20% |
| B02 | −20% → position $16,000 | ✅ TRUE | 20,000 × 0.80 = 16,000 |
| B02 | equity $10,000 → $6,000 | ✅ TRUE | 16,000 − 10,000 (loan fixed) = 6,000 |
| B02 | stock −20% = equity −40% | ✅ TRUE | (6,000 − 10,000)/10,000 = −40% |
| B02 | margin after drop = 37.5% | ✅ TRUE | 6,000 / 16,000 = 0.375 |
| B03 | maintenance margin 30% (illustrative broker level) | ✅ TRUE | §6.2 (FINRA floor 25%; brokers 30–40%) |
| B03 | margin call at $14,286 value | ✅ TRUE | call when (V−10,000)/V < 0.30 → V < 10,000/0.70 = 14,285.71 ≈ $14,286 (source: $14.29K) |
| B04 | long loss capped at −100% | ✅ TRUE | a long can only fall to $0 |
| B04 | short loss unbounded | ✅ TRUE | §6.3; price has no upper bound, so buy-back cost is unbounded |
| B04 | short squeeze definition | ✅ TRUE | §6.3 Risks table |
| B05 | "amplifies gains / losses / broker forces exit" | ✅ TRUE | synthesis of B01–B03 |
| B06 | handoff prompt (leverage ratio + margin-call price) | ✅ well-formed | uses §6.1/§6.2 formulas on viewer's own numbers |

## Deliberate omission (DOUBLE-CHECK LAW)
- **Short margin-call PRICE not shown.** Source Quick Reference says $72.92 for a
  $50 short, but re-derivation from the account identity
  (equity = proceeds + deposit − buy-back cost; call when equity/value < maint.)
  gives a different figure, and the source's two examples disagree with each
  other. An inconsistent source number is withheld rather than shown. The beat
  makes only the robust claim (unbounded loss), which is unambiguously correct.

**No model-version numbers or drift-prone live counts on screen.** Reg T (50%)
and FINRA maintenance floor (25%) are stable regulatory facts.
