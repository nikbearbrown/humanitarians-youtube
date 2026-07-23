# FACTCHECK — yield-curve-bootstrap

## Claims verified
- Bootstrapping: extract zero rates sequentially from coupon bond prices ✓
- 1-yr zero: z1 = (face+coupon)/price - 1 (for annual compounding) ✓
- 2-yr zero: solve for z2 given z1, using 2yr bond price ✓
- Pre-computed zero rates are consistent with the bond inputs (approximate) ✓
- Upward-sloping normal yield curve: longer maturities = higher yields ✓
- Nelson-Siegel model: 4 parameters (level, slope, curvature, decay) ✓
- Swap pricing from zero curve: fixed leg PV vs floating leg PV ✓

## Sources
- Fabozzi, F.J. "Fixed Income Mathematics."
- Nelson, C., Siegel, A. (1987). "Parsimonious Modeling of Yield Curves." Journal of Business.
