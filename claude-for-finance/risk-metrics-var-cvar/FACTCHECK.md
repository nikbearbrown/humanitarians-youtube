# FACTCHECK — risk-metrics-var-cvar

## Claims verified
- VaR at 95% = -5th percentile of return distribution ✓
- CVaR = expected loss given loss exceeds VaR ✓ (also known as Expected Shortfall)
- Historical VaR: non-parametric, uses empirical distribution ✓
- Parametric VaR under normality: -mu + z_alpha * sigma, z_95=1.645, z_99=2.326 ✓
- Student t with df=4 has heavier tails than normal ✓ (kurtosis = 6 vs 3)
- Basel III requires CVaR (Expected Shortfall) instead of VaR for trading book capital ✓
- GBM daily returns: mu=0.0003, sigma=0.01 are reasonable market parameters ✓

## Sources
- Jorion, P. "Value at Risk." McGraw-Hill.
- McNeil, A., Frey, R., Embrechts, P. "Quantitative Risk Management."
