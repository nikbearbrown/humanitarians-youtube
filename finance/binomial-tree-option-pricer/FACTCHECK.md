# FACTCHECK — binomial-tree-option-pricer

## Claims verified
- CRR model (Cox, Ross, Rubinstein 1979) ✓
- u = exp(sigma*sqrt(T/N)); d = 1/u ✓
- Risk-neutral prob p = (exp(r*dt) - d)/(u - d) ✓
- Backward induction: V = disc*(p*Vu + (1-p)*Vd) ✓
- European call at S=100, K=100, T=0.5, r=0.05, sigma=0.2, N=100 -> ~$10.45 (converges to B-S) ✓
- American put always >= European put due to early exercise premium ✓
- Longstaff-Schwartz (2001) is the standard Monte Carlo method for American options ✓

## Sources
- Cox, J., Ross, S., Rubinstein, M. (1979). "Option Pricing: A Simplified Approach." Journal of Financial Economics.
- Hull, J.C. "Options, Futures, and Other Derivatives."
