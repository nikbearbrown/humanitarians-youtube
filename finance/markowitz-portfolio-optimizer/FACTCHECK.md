# FACTCHECK — markowitz-portfolio-optimizer

## Claims verified
- Markowitz (1952) mean-variance optimization - Nobel Prize 1990 ✓
- Min-variance: minimize w'Cw s.t. sum(w)=1, w>=0 ✓
- Max-Sharpe: maximize (w'mu - rf)/sqrt(w'Cw) ✓
- SLSQP method in scipy.optimize.minimize handles this class of problems ✓
- Efficient frontier is the upper edge of the feasible region ✓
- Pre-computed frontier points are consistent with the asset inputs ✓
- Ledoit-Wolf shrinkage is a standard method for estimating large covariance matrices ✓

## Sources
- Markowitz, H. (1952). "Portfolio Selection." Journal of Finance.
- Sharpe, W.F. (1966). "Mutual Fund Performance." Journal of Business.
