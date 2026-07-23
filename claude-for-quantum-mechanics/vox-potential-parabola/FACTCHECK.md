# FACTCHECK — vox-potential-parabola

## Claim-by-claim audit

| Beat | Claim | Verdict | Source | Fix |
|------|-------|---------|--------|-----|
| B01 | "The quantum harmonic oscillator is everywhere — molecular bonds, crystal lattices, trapped atoms" | ✓ | M-04: "Every molecular bond, every lattice site, every potential well behaves like a QHO to leading order" | — |
| B02 | "A perfect parabola predicts quantum energy levels equally spaced" | ✓ | Standard QM: E_n = hbar*omega*(n+1/2), equally spaced | — |
| B04 | "Taylor-expand about its minimum. First derivative is zero — that is what minimum means" | ✓ | M-04: "V(x) = V(x0) + V'(x0)(x-x0) + (1/2)V''(x0)(x-x0)^2 + ... The linear term vanishes at a minimum" | — |
| B04 | "The linear term dies. What is left is a quadratic" | ✓ | M-04: "Dropping cubic and higher terms gives a harmonic potential with k_eff = V''(x0)" | — |
| B06 | "The effective spring constant is the second derivative of the potential at the minimum" | ✓ | M-04: "k_eff = V''(x0)" | — |
| B09 | "Morse potential for a diatomic bond — asymmetric and anharmonic" | ✓ | M-04 Exercise 3 mentions Morse potential explicitly | — |
| B09 | "Displacements under 0.05 nanometers" | illustrative | Reasonable scale for molecular bond harmonic range; labeled illustrative | Labeled illustrative |

## Terms table

| Term | Debut beat | Prior beat creating the need |
|------|-----------|------------------------------|
| potential well | B01 | B01 introduces the energy landscape |
| Taylor expansion | B04 | B03 establishes the need to understand well shapes |
| spring constant / k_eff | B06 | B05-B06 viewer has seen parabola emerge; needs a name for the curvature |
| harmonic oscillator | B07 | B06 establishes parabola = spring = harmonic oscillator |

## Illustrative numbers
- B09: Morse potential with displacements < 0.05 nm as harmonic range — illustrative, labeled.

## Exclusions confirmed
- No full Taylor coefficients on screen — confirmed absent.
- No series expansion algebra — confirmed absent.
