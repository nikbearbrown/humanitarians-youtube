# PROMPTS — rolling-correlation

## B01 — PROBLEM slate
Visual: correlation matrix golden (normal) morphing to crimson (crisis)
Caption: "Correlations spike to 1 in a crisis. Diversification fails."

## B06 — SUMMARY slate
Table: 60d vs 120d window: crisis detection lag + false alarm rate
EWMA lambda=0.94: the RiskMetrics compromise

## B07 — NEXT STEPS slate
EWMA update: C_t = lambda*C_{t-1} + (1-lambda)*r_t*r_t.T
lambda=0.94 for daily data (RiskMetrics standard)

## B08 — NEXT STEPS 2 slate
Stress test: use crisis correlation matrix
portfolio_var_crisis = w.T @ Sigma_crisis @ w
compare to normal: how much does VaR increase?
