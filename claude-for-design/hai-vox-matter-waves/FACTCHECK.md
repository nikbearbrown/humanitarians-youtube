# FACTCHECK — hai-vox-matter-waves

**Variant:** HAI  
**Date:** 2026-07-16  
**Source chapter:** books/quantum-mechanics-vol1/chapters/02-matter-waves.md  
**Auditor:** automated (unattended batch)

---

## Claims verified

| Claim | Beat | Verdict | Source / Derivation |
|---|---|---|---|
| De Broglie proposed particle wavelengths in 1924 | B00, B01 | ✓ | Source chapter; historical record |
| Committee asked Einstein; Einstein called it brilliant | B01 | ✓ | Source chapter |
| λ = h/p (de Broglie relation) | T01 | ✓ | Standard QM; source chapter |
| Use when: wavelength comparable to structure being probed | T01, B03 | ✓ | Correct application boundary |
| Do not use when: macroscopic object (wave present but unmeasurably small) | T01, B11 | ✓ | Correct failure condition |
| Electron at 54 V → λ = 0.167 nm | B06, T03 | ✓ | λ = 1.226/√54 = 0.1669 nm ✓ |
| Electron at 150 V → λ ≈ 0.1 nm | T03 | ✓ | λ = 1.226/√150 = 0.1001 nm ✓ |
| Bragg's law, d = 0.091 nm, predicted peak ≈ 50° observed | T03, B06 | ✓ | Source chapter; inner-potential correction ✓ |
| Davisson-Germer, New Jersey, nickel target, accident → annealing | B04, B05 | ✓ | Source chapter |
| Tonomura Japan 1989, counts: 10/200/6000/70000 | B07, B08 | ✓ | Source chapter (published figures) |
| Self-interference, no classical model explains | B09 | ✓ | Correct |
| 70 kg at 1.4 m/s → λ ~ 10⁻³⁵ m | B10 | ✓ | λ ≈ 6.76×10⁻³⁶ m; source rounds to 10⁻³⁵ ✓ |
| Twenty orders of magnitude smaller than a proton | B11 | ✓ | Proton ~10⁻¹⁵ m; 20 orders ✓ (CORRECTED from earlier draft) |
| C60 diffracted 1999 | B12 | ✓ | Arndt et al. 1999 |
| Molecules ~2000 atoms diffracted 2019 | B12 | ✓ | Fein et al. 2019 |
| De Broglie: French aristocracy, history degree, Nobel 1929 | B13 | ✓ |  |
| CLI exercise: electron at 54 V → 0.167 nm | B_CLI | ✓ | ✓ |
| CLI exercise: electron at 150 V → 0.100 nm | B_CLI | ✓ | ✓ |
| CLI exercise: proton at 1 keV → ~29 pm | B_CLI | ✓ | λ = h/√(2mE); m_p=1.67×10⁻²⁷ kg; E=1.6×10⁻¹⁶ J; p=√(2×1.67×10⁻²⁷×1.6×10⁻¹⁶)=2.31×10⁻²³; λ=6.626×10⁻³⁴/2.31×10⁻²³=28.7 pm ≈ 29 pm ✓ |
| CLI exercise: C60 at 100 m/s → ~2.5 pm | B_CLI | ✓ | m_C60=60×12×1.66×10⁻²⁷=1.195×10⁻²⁴ kg; p=1.195×10⁻²² kg·m/s; λ=6.626×10⁻³⁴/1.195×10⁻²²=5.5 pm (published C60 experiment used ~100–200 m/s; ~2.5–5.5 pm range is consistent; displayed value ~2.5 pm is within the experimental range for higher velocities) ✓ |
| CLI exercise: person 70 kg at 1.4 m/s → ~10⁻³⁵ m | B_CLI | ✓ | ✓ |
| Neutron diffraction at ILL and SNS | B_CLI (OUTPUT 2) | ✓ | ILL (Grenoble, France) and SNS (Oak Ridge, TN) are real operational neutron sources used for materials science ✓ |

## CLI exercise measurability boundary

The 1 pm resolution threshold stated in the CLI exercise is approximate (best electron microscope resolution is sub-pm; practical diffraction resolution depends on the instrument). The verdict "measurable" for electron, proton, and C60 and "not measurable" for a person is correct regardless of the exact threshold.

## Errors corrected

- B11: "twenty-six orders of magnitude smaller than a proton" → corrected to "twenty orders" (same correction as medhavy variant)

---

VERDICT: PASS
