# PROMPTS — risk-metrics-var-cvar

## B01 — PROBLEM slate
Visual: return histogram with crimson tail, VaR threshold line
Caption: "VaR: how bad can it get? CVaR: how bad when it gets bad?"

## B06 — SUMMARY slate
Table: Normal vs t(df=4) comparison
VaR95: similar; VaR99: ~15% larger; CVaR99: ~60% larger
Caption: "The tail you cannot see is the risk that matters."

## B07 — NEXT STEPS slate
Real data: yfinance S&P 500 daily returns
import yfinance as yf
spy = yf.download("SPY", start="2000-01-01")
returns = spy["Adj Close"].pct_change().dropna()

## B08 — NEXT STEPS 2 slate
Portfolio VaR: multivariate normal
Sigma_p = sqrt(w' @ Cov @ w)
VaR_portfolio = -mu_p + z_alpha * Sigma_p
