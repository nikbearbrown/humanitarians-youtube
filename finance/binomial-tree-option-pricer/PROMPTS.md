# PROMPTS — binomial-tree-option-pricer

## B01 — PROBLEM slate
Visual: binomial tree branching, converging to B-S price
Caption: "Discrete time. Continuous limit. Same answer."

## B06 — SUMMARY slate
Table: N=5 ($8.12), N=10 ($9.45), N=20 ($10.12), N=50 ($10.38), N=100 ($10.43), B-S ($10.45)
American put premium: ~$0.18 vs European at N=100

## B07 — NEXT STEPS slate
Headline: "Try trinomial tree or Longstaff-Schwartz"
Trinomial: faster convergence (3 branches)
LS Monte Carlo: regression-based continuation value

## B08 — NEXT STEPS 2 slate
Barrier option on binomial tree:
for j in range(step+1):
    if S_val(step, j) > barrier:
        V[j] = 0  # barrier knocked out
