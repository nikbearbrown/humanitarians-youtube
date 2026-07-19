# FACTCHECK — vox-hydrogen-cloud

## Claims verified

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | Bohr model: electron on a circle, one exact radius | CORRECT | Bohr 1913 |
| B02 | Ground-state Bohr radius a₀ = 0.053 nm | CORRECT | a₀ = 5.29×10⁻¹¹ m = 0.0529 nm ✓ |
| B04 | P(r) = r²e^{−2r/a₀} × constant | CORRECT | P(r) = (4/a₀³)r²e^{−2r/a₀} ✓ |
| B05 | dP/dr = 0 → r_peak = a₀ | CORRECT | dP/dr = (4/a₀³)(2r − 2r²/a₀)e^{−2r/a₀} = 0 → r = a₀ ✓ |
| B07 | ⟨r⟩ = 3a₀/2 | CORRECT | ∫r·P(r)dr = (4/a₀³)∫r³e^{−2r/a₀}dr = (4/a₀³)·6/(2/a₀)⁴ = (4/a₀³)·6a₀⁴/16 = 3a₀/2 ✓ |
| B13 | r_peak = a₀ = 0.053 nm | CORRECT | 5.29×10⁻¹¹ m = 0.0529 nm ✓ |
| B13 | ⟨r⟩ = 3a₀/2 = 0.079 nm | CORRECT | 3×0.0529/2 = 0.0794 nm ✓ |
| B13 | Gap = 0.026 nm | CORRECT | 0.0794 − 0.0529 = 0.0265 nm ✓ |
| B11 | Bohr got energies right because a₀ is the length scale | CORRECT | Chapter 06 §"Bohr's Luck" |

## Calculation check: ⟨r⟩

⟨r⟩ = (4/a₀³) ∫₀^∞ r³ e^{−2r/a₀} dr
     = (4/a₀³) × 3!/(2/a₀)⁴
     = (4/a₀³) × 6 × a₀⁴/16
     = 24/(16a₀³) × a₀⁴
     = (3/2) a₀  ✓

## Exclusions honored
- No radial Schrödinger derivation
- No normalization algebra (A = 2/a₀^{3/2})
- No SO(4) symmetry
- No spherical harmonic machinery

## VERDICT: PASS
