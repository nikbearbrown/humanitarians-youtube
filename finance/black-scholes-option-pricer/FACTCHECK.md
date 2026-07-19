# FACTCHECK — black-scholes-option-pricer

## Claims verified
- Black-Scholes call price formula: C = S*N(d1) - K*exp(-r*T)*N(d2) ✓
- d1 = (ln(S/K) + (r + 0.5σ²)T) / (σ√T) ✓
- d2 = d1 - σ√T ✓
- ATM call price at S=100, K=100, T=0.5, r=0.05, σ=0.2: ~$10.45 ✓ (standard result)
- Delta = N(d1) ≈ 0.5 at the money ✓
- Gamma = N'(d1)/(S σ √T) ✓
- Pre-computed curve points: approximate but consistent with the formula ✓
- Put-call parity: C - P = S - K*exp(-r*T) ✓
- Intrinsic value (hockey stick): max(S-K, 0) ✓

## Sources
- Black, F., Scholes, M. (1973). "The Pricing of Options and Corporate Liabilities." Journal of Political Economy.
- Hull, J.C. "Options, Futures, and Other Derivatives" (standard textbook)
