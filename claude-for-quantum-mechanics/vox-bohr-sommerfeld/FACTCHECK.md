# FACTCHECK — vox-bohr-sommerfeld

## Claims audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B01 | Harmonic oscillator traces an ellipse in (x,p) phase space | ✓ | Ch04: "For the harmonic oscillator, the classical orbit at energy E is an ellipse in phase space with area 2πE/ω" |
| B04 | Original Bohr-Sommerfeld: ∮ p dx = nh | ✓ | Ch04: "The original 1913-1916 Bohr-Sommerfeld rule had nh without this correction" |
| B05 | Actual QM spectrum: E_n = (n+½)ℏω | ✓ | Ch04: exact harmonic oscillator result |
| B07 | Each turning point contributes a π/4 Maslov phase | ✓ | Ch04: "Each turning point contributes this phase shift" (π/4) |
| B08 | Two turning points → total phase = π/2 → adds h/2 to action integral | ✓ | Ch04: "The ½ is the combined Maslov correction from both turning points (π/4 each, totaling h/2)" |
| B09 | Ground state (n=0): orbit area = h/2, not zero | ✓ | Ch04: "For n=0, it is the only term — without it, the predicted ground-state energy is zero" |
| B11 | Half enforces uncertainty principle; can't squeeze both x and p to zero | ✓ | Standard QM; consistent with ch04 context |
| B12 | Liquid helium doesn't freeze at atmospheric pressure due to zero-point motion | ✓ | Standard physics; consistent with context |
| B13 | ω = 10¹³ rad/s → E_zp = ℏω/2 ≈ 33 meV | ILLUSTRATIVE | ℏ = 1.055×10⁻³⁴, ω = 10¹³ → ℏω = 1.055×10⁻²¹ J → /2 = 5.27×10⁻²² J = 3.3×10⁻³ eV = 3.3 meV. Wait: 5.27e-22 / 1.602e-19 = 3.3×10⁻³ eV = 3.3 meV, not 33 meV. |

## Illustrative numbers fix — B13
ω = 10¹³ rad/s:
- ℏω/2 = (1.055×10⁻³⁴ × 10¹³) / 2 = 5.28×10⁻²² J
- In eV: 5.28×10⁻²² / 1.602×10⁻¹⁹ = 3.3×10⁻³ eV = 3.3 meV

For 33 meV, need ω = 10¹⁴ rad/s (near-infrared):
- ℏω/2 = (1.055×10⁻³⁴ × 10¹⁴) / 2 = 5.28×10⁻²¹ J = 33 meV ✓

CORRECTION: Use ω = 10¹⁴ rad/s (near-infrared range, reasonable for molecular vibration) for E_zp ≈ 33 meV. Update narration.

## Terms table

| Term | Debuts at | Prior beat creates need |
|------|-----------|------------------------|
| phase space | B01 | B01 (orbit concept) |
| Bohr-Sommerfeld | B04 | B03 (question established) |
| turning point | B07 | B05/B06 (mechanism needed) |
| Maslov index | B07 | B07 (introduced with turning-point concept) |
| zero-point energy | B09 | B08 (after mechanism) |
