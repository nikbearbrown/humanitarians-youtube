# PROMPTS — hussain-bond-pricing-duration

## B02 — CLI ask (bond_pricer.py)
claude "Write bond_pricer.py: face=1000, coupon_rate=0.05, maturity=10 years,
YTM=range(0.02,0.11,0.01). Compute price, Macaulay duration, modified
duration. Verify: price=1000 at YTM=5%. Print table:
YTM | Price | Mac Duration | Mod Duration."

## B05 — CLI change (convexity revision)
claude "update bond_pricer.py:
  -> add a convexity measure
  -> compare duration-only vs duration+convexity approximation
  -> for a 2% yield shock (up and down), show the approximation error"

## B09 — Your Turn handoff
claude "Build a two-bond portfolio (a 2-year bond and a 10-year bond),
compute the portfolio's blended duration and convexity, then size a 10-year
Treasury futures position that neutralizes the portfolio's duration. Report
the leftover convexity mismatch."
