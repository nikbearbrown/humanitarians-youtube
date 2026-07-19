# PROMPTS — markowitz-portfolio-optimizer

## B01 — PROBLEM slate
Visual: risk-return space with a scatter of random portfolios and a curved frontier
Caption: "Below the frontier: suboptimal. On it: efficient."

## B06 — SUMMARY slate
Table: unconstrained Sharpe=0.47 vs constrained (40% cap) Sharpe=0.41
Caption: "Constraints always cost. The question is how much."

## B07 — NEXT STEPS slate
Headline: "Try real assets + Ledoit-Wolf shrinkage"
from sklearn.covariance import LedoitWolf
lw = LedoitWolf().fit(returns)
cov_shrunk = lw.covariance_

## B08 — NEXT STEPS 2 slate
Add beta-neutral constraint:
constraints.append({'type': 'eq', 'fun': lambda w: w @ betas})
