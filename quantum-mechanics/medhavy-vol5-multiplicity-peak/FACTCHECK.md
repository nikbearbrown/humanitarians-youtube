# FACTCHECK — medhavy-vol5-multiplicity-peak

## Formula: Omega(N,n) = C(N,n) = N! / (n! * (N-n)!)
  Source: Kittel & Kroemer "Thermal Physics" Ch.2; Reif "Fundamentals of Statistical and Thermal Physics" Ch.1

## Numbers:
  - N=10: C(10,5) = 252 ✓ (10!/(5!*5!) = 3628800/14400 = 252)
  - C(10,4) = 210 ✓ (10!/(4!*6!) = 3628800/17280 = 210)
  - Ratio: 252/210 = 1.20 (peak is 20% above next bin)
  - N=50: C(50,25) = 126,410,606,437,752 (very large peak)
    Peak/total = C(50,25)/2^50 ≈ 11.2% (quite sharp)
  - Stirling: C(N,N/2) ≈ 2^N / sqrt(pi*N/2) for large N ✓

## Two testable predictions:
  P1: Peak at exactly n=N/2 for any even N (symmetry of Pascal's triangle) ✓
  P2: C(10,5) = 252 exactly ✓

VERDICT: PASS
