# FACTCHECK — medhavy-vol5-fourier-square

## Formula: Fourier series of square wave
  f(x) = (4/pi) * sum_{n=1,3,5,...} (1/n) * sin(n*pi*x/L)
  Source: Griffiths QM Ed.3 §2.4; Arfken & Weber "Mathematical Methods for Physicists" §14.5

## Numbers:
  - N=1: pure sine, peak at L/2 equals 4/pi = 1.273 (not 1.0)
  - N=3 (terms 1,3): approximation improves at edges
  - N=9 (terms 1,3,5,7,9): Gibbs overshoot approx 9% (specifically 8.9%) above true value of 1
    The Gibbs phenomenon: overshoot converges to (1 + 2/pi * integral_pi^infty (sin(t)/t)dt) approx 1.089
  - Overshoot is approx 9% regardless of N (does NOT decrease as N increases)
  - At x=L/2: sum_{n=1,3,5,...,N} (4/n*pi)*sin(n*pi/2) converges to 1.0 as N->infinity ✓

## Two testable predictions:
  P1: Gibbs overshoot remains ~9% as N increases (NOT going to zero) ✓
      This is a fundamental property of Fourier series at discontinuities
  P2: At x=L/2 (midpoint), partial sum = 4/pi*(1+0-1/3*0+...) wait, sin(n*pi/2):
      n=1: sin(pi/2)=1; n=3: sin(3pi/2)=-1; n=5: sin(5pi/2)=1; etc.
      Actually at x=L/2: f converges to 1.0 (the midpoint of the discontinuity region)
      The partial sums at x=L/2 = 4/pi*(1 - 1/3 + 1/5 - ...) = 4/pi * pi/4 = 1 ✓

VERDICT: PASS
