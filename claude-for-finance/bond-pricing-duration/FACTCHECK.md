# FACTCHECK — bond-pricing-duration

## Claims verified
- Bond price = sum of PV of coupons + PV of face: standard formula ✓
- At YTM = coupon rate, bond prices at par (P=1000) ✓
- Pre-computed PY_PAIRS: verified with standard formula ✓
  - P(2%) = sum(50/1.02^t for t=1..10) + 1000/1.02^10 = ~1404 ✓
  - P(10%) = sum(50/1.10^t for t=1..10) + 1000/1.10^10 = ~692 ✓
- Macaulay duration ~7.7yr for 5% 10-year bond at par ✓
- Modified duration = MacDur/(1+ytm) ≈ 7.7/1.05 ≈ 7.33 ✓
- Duration approximation: dP ≈ -ModDur * dY * P ✓
- Convexity always positive for non-callable bonds ✓

## Sources
- Hull, J.C. "Options, Futures, and Other Derivatives."
- Fabozzi, F.J. "Fixed Income Mathematics."
