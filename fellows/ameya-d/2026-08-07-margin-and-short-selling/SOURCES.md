# SOURCES — leverage-cuts-both-ways

Primary source: **Computational Finance with Excel, Python, and LLMs** (Nik Bear
Brown), Chapter 6 — *Investment Process: Margin Accounts and Short Selling*, in
this repo:
`Computational-Finance-with-Excel-Python-and-LLMs/Chapters/Introduction_to_Computational_Finance_Chapter_6.md`
and its cheat sheet `..._Chapter_6_Cheat_Sheet.md`.

DOUBLE-CHECK LAW: every on-screen number traces to the cheat sheet and was
re-derived independently (see FACTCHECK.md). No figure appears on screen that
isn't verified here.

| On screen | Source line |
|-----------|-------------|
| Reg T initial margin = 50% | §6.2 "Regulation T: Standard initial margin = 50%" |
| Maintenance margin (FINRA min 25%; brokers 30–40%; 30% used) | §6.2 "FINRA minimum: 25%; Broker: typically 30–40%" |
| $10k cash → $20k position, $10k loan (2:1) | §Quick Reference: "$10K cash, 50% margin → buy $20K" |
| −20% → $16k value, $10k loan, 37.5% margin | §Quick Reference: "$20K→$16K value, $10K loan, new margin 37.5%" |
| Margin call at $14,286 portfolio value | §Quick Reference: "Triggered at $14.29K value" (30% maintenance) |
| Margin call formula: Loan / (Shares × (1 − Maint.)) | §6.2 Margin Call Price |
| Equity = Value − Loan; margin % = Equity / Value | §6.1 Basic Margin Concepts |
| Short loss unbounded vs long capped at −100% | §6.3 Risks: "Unlimited Loss — prices can rise indefinitely, unlike long positions limited to 100% loss" |
| Short squeeze | §6.3 Risks: "Short Squeeze" |
| Return on margin / leverage ratio (handoff prompt) | §6.1 leverage_ratio; §Decision Tools "Long Position Leverage" |

## Corrections applied (DOUBLE-CHECK LAW)
- **Short margin-call price withheld.** The cheat sheet's Quick Reference quotes
  "$72.92/share" for a $50 short, but its own margin-call formulas produce
  different values, and the two worked examples disagree. Because the figure is
  not internally consistent in the source, it is **not shown on screen**. The
  short-selling beat teaches only the unambiguous, correct property: unbounded
  loss. Logged rather than guessed.
- Maintenance margin shown as 30% is labelled as an illustrative broker level
  (the regulatory floor is FINRA's 25%), matching the source's worked example.

*Educational use only — not financial advice.*
