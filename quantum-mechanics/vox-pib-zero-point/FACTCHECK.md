# FACTCHECK — vox-pib-zero-point

## Claims audit

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B02 | Ground state energy is not at zero | ✓ | Chapter 04: "The lowest one sits above the bottom of the box, not at it" |
| B05 | Wavefunction must go to zero at walls | ✓ | Chapter 04: "Apply the boundary conditions: ψ(0) = 0 kills the cosine, ψ(L) = 0 requires kL = nπ" |
| B05 | Ground state fits one half-wavelength | ✓ | Chapter 04: "The wave functions are standing waves in the box: sin(nπx/L) fits exactly n half-wavelengths" |
| B07 | Curvature is kinetic energy (Schrodinger) | ✓ | Chapter 04: Schrodinger equation d²ψ/dx² = -(2mE/ℏ²)ψ; curvature ∝ E |
| B08 | Energy scales as 1/L² | ✓ | Chapter 04: E_1 = π²ℏ²/(2mL²) — explicitly 1/L² |
| B10 | Liquid helium refuses to freeze at absolute zero | ✓ | Chapter 04: "Liquid helium refuses to freeze at atmospheric pressure all the way to absolute zero because the zero-point motion of the helium atoms is enough to prevent them from locking into a lattice" |
| B13 | E_1 ≈ 1.5 eV for L = 0.5 nm | ✓ | Calculation: π²(1.055e-34)²/(2×9.109e-31×(0.5e-9)²) = 2.41e-19 J ≈ 1.51 eV |
| B13 | Double box width: E_1 drops by factor of 4 | ✓ | E_1 ∝ 1/L², double L → E_1/4 ≈ 0.38 eV |

## Exclusions confirmed
- No full boundary-value derivation: absent ✓
- No normalization constant: absent ✓
- No n² spectrum table (E_2, E_3, ...): absent ✓
- No uncertainty-principle algebra beyond one plain sentence: absent ✓

## Terms table
| Term | Debut beat | Prior beat creating need |
|------|-----------|--------------------------|
| wavefunction | B05 | B04 (classical particle can be stopped; quantum wave can't) |
| boundary condition | B05 | B05 (same beat: introduced as the constraint) |
| zero-point energy | B02 | B02 (name given to the energy gap) |
| curvature | B07 | B06 (section card quotes "curvature is kinetic energy") |

## Illustrative numbers
- B13: L = 0.5 nm is labeled illustrative
- E_1 ≈ 1.5 eV is an accurate calculation (exact: 1.506 eV)
- Double-width box: E_1 ≈ 0.37 eV is accurate (0.376 eV)
