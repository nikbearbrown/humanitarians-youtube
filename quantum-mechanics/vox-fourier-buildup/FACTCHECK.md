# FACTCHECK — vox-fourier-buildup

## B03 — Energy modes in a box
- Mode n has energy E_n = n^2 * pi^2 * hbar^2 / (2mL^2) = n^2 * E_1: CORRECT.
- Mode n = sin(n*pi*x/L) (satisfies zero boundary conditions at x=0, L): CORRECT.

## B05 — Fourier coefficient = Born-rule inner product
- c_n = <phi_n | psi> = integral_0^L phi_n*(x) psi(x) dx: CORRECT (orthonormal basis).
- P(E_n) = |c_n|^2: CORRECT (Born rule for discrete spectrum).
- This is the statement that {phi_n} is an orthonormal basis: CORRECT.

## B08 — Completeness and normalization
- psi(x) = sum_n c_n phi_n: CORRECT (completeness of eigenbasis).
- sum_n |c_n|^2 = 1: CORRECT (Parseval / normalization).

## B09 — Triangular spike coefficients
- psi(x) = x on [0,L/2] and L-x on [L/2,L] (normalized to L^2/6).
- c_n = (2/L) integral_0^L psi(x) sin(n*pi*x/L) dx
  For odd n: c_n = (8/(n^2*pi^2)) * sin(n*pi/2) / sqrt(L) [with normalization]
  The coefficient formula c_n proportional to 8/(n^2*pi^2)*sin(n*pi/2) is CORRECT.
- c_n = 0 for even n: CORRECT (sin(n*pi/2) = 0 for even n).
- |c_1|^2: With proper normalization of psi, |c_1|^2 = (8/pi^2)^2 / (sum of all |c_n|^2).
  Series sum: sum_{odd n} (8/(n^2*pi^2))^2 = (64/pi^4) * sum_{odd n} 1/n^4.
  sum_{odd n} 1/n^4 = pi^4/96. So sum |c_n|^2 = (64/pi^4)*(pi^4/96) = 64/96 = 2/3.
  But wait — this is the norm of the un-normalized spike. The normalized spike:
  ||psi||^2 = integral_0^L psi(x)^2 dx = L^3/12 * (2/L) factor from normalization... 
  
  Let me recheck directly. For psi(x) normalized such that integral |psi|^2 dx = 1:
  The triangular function f(x) on [0,L] has ||f||^2 = L^3/12 (integrating x^2 on [0,L/2]).
  Normalized: psi = f/||f|| = sqrt(12/L^3) * f(x).
  
  c_n = integral_0^L psi(x) phi_n(x) dx where phi_n = sqrt(2/L) sin(n*pi*x/L).
  For odd n: c_n = sqrt(12/L^3) * sqrt(2/L) * (4L^2/(n^2*pi^2)) * sin(n*pi/2)
           = sqrt(24/L^4) * 4L^2/(n^2*pi^2) * sin(n*pi/2)
           = (4*sqrt(24)/L^2)^{...}
  
  Actually: |c_1|^2 = (2/L)(12/L^3)(integral f(x)sin(pi x/L) dx)^2
  integral x*sin(pi*x/L) dx from 0 to L/2 = [L^2/pi^2*sin(pi*x/L) - Lx/pi*cos(pi*x/L)] from 0 to L/2
    = L^2/pi^2 * sin(pi/2) - L*(L/2)/pi * cos(pi/2) = L^2/pi^2
  By symmetry, same from L/2 to L. Total: 2L^2/pi^2.
  |c_1|^2 = (2/L)*(12/L^3)*(2L^2/pi^2)^2 = (24/L^4)*(4L^4/pi^4) = 96/pi^4 ≈ 0.987.
  So |c_1|^2 ≈ 0.99 is CORRECT (approximately).

VERDICT: All facts verified. Fourier-eigenstate correspondence, Born rule projection, completeness, and the triangular spike coefficient calculation are all correct.
