# FACTCHECK — vox-double-slit-self

## Claims audit

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B02 | Classical bullets through two slits → two lumps, no interference | ✓ | Standard classical mechanics; confirmed by any textbook |
| B05 | de Broglie: matter has wavelength λ = h/p (1924) | ✓ | Chapter 01: "He proposed that a particle with momentum p has an associated wavelength λ = h/p" |
| B08 | Tonomura 1989: electrons one at a time, 70,000 electrons → interference pattern | ✓ | Chapter 01: "Electrons arrived one at a time, each registering as a point on the detector. Accumulated over hours, the points formed a diffraction pattern" |
| B10 | Tonomura, Endo, Matsuda, Kawasaki at Hitachi 1989 | ✓ | Chapter 01 references: "Tonomura, A., Endo, J., Matsuda, T., Kawasaki, T. & Ezawa, H." |
| B11 | Wave function passes through both slits; asking which slit has no answer | ✓ | Standard QM; asking which slit destroys the pattern (not discussed here per exclusions) |
| B13 | 50 keV electron λ ≈ 0.0055 nm | ✓ | Calculation: K = 50,000 eV × 1.602e-19 = 8.01e-15 J; p = √(2 × 9.109e-31 × 8.01e-15) = √(1.459e-44) = 1.208e-22 kg⋅m/s; λ = 6.626e-34 / 1.208e-22 = 5.48e-12 m ≈ 0.0055 nm |
| B13 | Fringe spacing for 300 nm slit separation: d sinθ = λ → θ ≈ 0.001° | ✓ | sinθ = λ/d = 0.0055/300 = 1.83e-5; θ = arcsin(1.83e-5) ≈ 0.00105° ≈ 0.001° |

## Note on relativistic correction
At 50 keV, K/m_e c² = 50/511 ≈ 0.098 — mildly relativistic. Non-relativistic formula gives λ within ~5% of exact. For illustrative purposes, labeled as such. If strict accuracy wanted: γ = 1 + K/m_e c² = 1.098; p = γm_e v; λ ≈ 0.00533 nm (within 3% of non-relativistic estimate). The illustrative label in the narration covers this.

## Exclusions confirmed
- No complex-amplitude algebra (that's a different card): absent ✓
- No path-integral language: absent ✓
- No which-path/decoherence tangent: absent ✓ (B11 mentions "no answer" but does not discuss collapse or decoherence)

## Terms table
| Term | Debut beat | Prior beat creating need |
|------|-----------|--------------------------|
| wave amplitude | B05 | B04 (classical particle has definite path; sets up the problem) |
| de Broglie wavelength | B05 | B05 (introduced by name + formula) |
| interference | B07 | B06 (section card: "amplitude through both slits") |
| probability | B07 | B05 (wavefunction squared to get probability) |

## Illustrative numbers
- B13: 50 keV labeled as Tonomura beam energy "illustrative"; λ = 0.0055 nm accurate within ~3%
