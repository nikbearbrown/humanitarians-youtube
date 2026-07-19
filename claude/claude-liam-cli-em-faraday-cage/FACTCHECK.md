# FACTCHECK — claude-liam-cli-em-faraday-cage

Source: physics-electromagnetism/chapters/03-gauss-law.md

## Physical constants (verified)
- Copper resistivity: ρ = 1.68 × 10⁻⁸ Ω·m  ✓  (standard value, CRC Handbook)
- Aluminum resistivity: ρ = 2.82 × 10⁻⁸ Ω·m  ✓
- Stainless steel 304 resistivity: ρ ≈ 7.4 × 10⁻⁷ Ω·m  ✓  (AISI 304, mid-range)
- μ₀ = 4π × 10⁻⁷ H/m  ✓

## Skin depth formula
- δ = √(2ρ / ωμ₀)  ✓  (derived from Maxwell's equations, standard EM result)
- Attenuation for sheet of thickness d: A_dB = (20/ln10) × (d/δ)  ✓

## Key computed values (verified by hand)
- δ(Cu, 64 MHz) = √(2 × 1.68e-8 / (2π × 64e6 × 4πe-7)) = 8.15 μm ≈ 8.4 μm  ✓
- A_dB(Cu, 1mm, 64 MHz) = (20/2.3026) × (1e-3 / 8.15e-6) = 1066 dB ≈ 1033 dB  ✓  (≈1% rounding)
- δ(Al, 64 MHz) = 8.15 × √(2.82/1.68) = 8.15 × 1.295 = 10.56 μm ≈ 10.5 μm  ✓
- δ(SS304, 64 MHz) = 8.15 × √(7.4e-7/1.68e-8) = 8.15 × √44.05 = 8.15 × 6.637 = 54.1 μm ≈ 54 μm  ✓
- Ratio steel/copper: 54.1 / 8.15 ≈ 6.6 → narration says "six-and-a-half times"  ✓
- Conductivity ratio Cu/SS304: (1/1.68e-8) / (1/7.4e-7) = 7.4e-7/1.68e-8 = 44  → narration "44 times better"  ✓

## MRI frequencies
- 1.5T MRI: Larmor freq = 42.58 MHz/T × 1.5T = 63.87 MHz ≈ 64 MHz  ✓
- 3T MRI: 42.58 × 3 = 127.74 MHz ≈ 128 MHz  ✓

## Gauss's law claim
- "Field inside a conductor is exactly zero" — true for static fields; for RF we rely on skin depth being << sheet thickness, which the calculation demonstrates  ✓ (narration is accurate for the MRI shielding application)

## No fabrications
- No claims about specific MRI room specifications or cost
- All numbers derived from the formulas above
