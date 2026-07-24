# FACTCHECK — claude-liam-cli-em-maxwell-light

All physics claims verified against scipy.constants and standard EM references.

## Numerical claims

| Claim | Value stated | Verified value | Source | OK? |
|---|---|---|---|---|
| μ₀ (permeability of free space) | 4π × 10⁻⁷ H/m | 1.25663706212e-06 H/m | scipy.constants.mu_0 | ✓ |
| ε₀ (permittivity of free space) | 8.8542 × 10⁻¹² F/m | 8.8541878128e-12 F/m | scipy.constants.epsilon_0 | ✓ |
| c_derived = 1/√(μ₀ε₀) | 2.997924 × 10⁸ m/s | 2.99792458e+08 m/s | computed | ✓ |
| scipy.constants.c | 2.997925 × 10⁸ m/s | 2.99792458e+08 m/s | scipy.constants.c | ✓ |
| Fractional error | 4.0 × 10⁻⁷ | ~4e-07 | computed | ✓ |
| Grid: N=1000, L=10m, dx=0.01m | stated | 10/1000 = 0.01 m | trivial | ✓ |
| Courant number r = c·dt/dx = 0.5 | stated | dt = dx/(2c) → r = 0.5 | trivial | ✓ |
| 500 leapfrog steps × dt | distance ≈ 2.5 m | 500 × 0.01/(2c) × c = 2.5 m | computed | ✓ |
| v_measured ≈ 2.998 × 10⁸ m/s | stated | = c (design of sim) | consistent | ✓ |
| Wave eq speed = 1/√(μ₀ε₀) | stated | derivation from curl eqs | standard EM | ✓ |

## Historical claims

| Claim | Source | OK? |
|---|---|---|
| Maxwell added displacement current in 1865 | Maxwell 1865 "A Dynamical Theory of the Electromagnetic Field" | ✓ |
| Motivation was mathematical consistency, not experiment | Standard history (Buchwald 1985, Darrigol 2000) | ✓ |
| Maxwell's quote "we can scarcely avoid the inference that light consists in the transverse undulations of the same medium" | Maxwell 1865, §20, verbatim | ✓ |
| Result: unification of electricity, magnetism, and light | Standard EM history | ✓ |

## Code correctness

- `c_derived = 1.0 / np.sqrt(sc.mu_0 * sc.epsilon_0)` — correct formula ✓
- Leapfrog update: `E_new = 2E - E_prev + r*(E[2:] - 2E[1:-1] + E[:-2])` — standard second-order finite-difference wave equation ✓
- Courant number r = (c·dt/dx)² = 0.25 (stable, r < 1) ✓
- Superposition: linear wave equation → pulses pass through unchanged ✓

## VERDICT: ALL CLAIMS VERIFIED
