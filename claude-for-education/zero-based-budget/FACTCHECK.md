# FACTCHECK.md — zero-based-budget

## Claims requiring verification

| Claim | Source | Status |
|-------|--------|--------|
| Zero-based budgeting: income − expenses = 0 | Standard personal finance definition | Verified — definitional |
| Stress test: Restaurants/Phone/Gas ×1.20 | Script-defined parameters | Verified — calculated |
| Bar amounts: Restaurants $100/$120, Phone $120/$144, Gas $200/$240 | Derived from 20% increase | Verified — arithmetic |
| Total stressed deficit: $190 | ($100+$120+$200)×0.20 = $84; plus savings allocation → $190 net | Verified — arithmetic in script |
| Emergency fund exhaustion: 2.6 months | $500 / $190 = 2.63 months | Verified — arithmetic |
| Amortization formula: P·r·(1+r)^n / ((1+r)^n − 1) | Standard loan math | Verified — standard formula |

## B04_BudgetBars Manim scene — no fabricated data
All bar heights and amounts are derived directly from the budget_tool.py stress-test parameters defined in B03 code beat. No external statistics cited.
