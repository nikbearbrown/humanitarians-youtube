# PROMPTS — black-scholes-option-pricer

## B01 — PROBLEM slate
Visual: title card with Black-Scholes formula, five inputs labeled
Text: "C = S·N(d1) − K·e^{−rT}·N(d2)"
Inputs: S (spot), K (strike), T (time), r (rate), σ (volatility)

## B06 — SUMMARY slate
Visual: two-column table — Greeks values at ATM
Delta=0.52, Gamma=0.04, Theta=-0.03/day, Vega=0.20, Rho=0.28
Caption: "5 Greeks. 5 risk dimensions. One formula."

## B07 — NEXT STEPS slate
Headline: "Try implied volatility inversion"
Steps:
1. Observe market call price
2. Solve for σ: scipy.optimize.brentq(BS_call - market_price, 0.01, 5.0)
3. Plot σ_implied vs strike → the vol smile

## B08 — NEXT STEPS 2 slate
Code: yfinance options chain pull
import yfinance as yf
ticker = yf.Ticker("SPY")
chain = ticker.option_chain("2025-01-17")
calls = chain.calls[["strike","lastPrice","impliedVolatility"]]
