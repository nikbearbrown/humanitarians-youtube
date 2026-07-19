# FACTCHECK — monte-carlo-portfolio

## Claims verified
- GBM discretization: S(t+dt) = S(t)*exp((mu-0.5*sigma^2)*dt + sigma*sqrt(dt)*Z) ✓
- Parameters: mu=0.07, sigma=0.15 are reasonable for a diversified equity portfolio ✓
- 10,000 paths over 30 years with monthly steps (360 steps) ✓
- Vectorized NumPy: np.cumsum along axis=1 for log-cumulative returns ✓
- Fan of paths showing P5/median/P95 is standard Monte Carlo output ✓
- Regime switching: clustering of volatility (sigma doubles) is a known stylized fact ✓
- 4% withdrawal rule is the standard retirement planning heuristic ✓

## Sources
- Glasserman, P. "Monte Carlo Methods in Financial Engineering." Springer.
- Hull, J.C. "Options, Futures, and Other Derivatives."
