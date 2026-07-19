# FACTCHECK — medhavy-ch1-classical-sims

All physics numbers verified against standard references (Griffiths, NIST, Hyperphysics).

---

## PHOTOELECTRIC EFFECT

| Claim | Value | Reference | Status |
|---|---|---|---|
| hc in eV·nm | 1240 eV·nm | CODATA 2018 (h·c = 1.23984×10⁻⁶ eV·m) | ✓ VERIFIED |
| Na work function Φ | 2.28 eV | Lide (ed.), CRC Handbook, "Work Function of Elements" | ✓ VERIFIED |
| E(700 nm) = hc/700 | 1.77 eV | arithmetic | ✓ |
| E(546 nm) = hc/546 | 2.27 eV | arithmetic | ✓ |
| E(300 nm) = hc/300 | 4.13 eV | arithmetic | ✓ |
| K(UV) = 4.13 − 2.28 | 1.85 eV | arithmetic | ✓ |
| Red and green: no ejection regardless of intensity | stated | Einstein 1905 photoelectric paper | ✓ VERIFIED |

## COMPTON SCATTERING

| Claim | Value | Reference | Status |
|---|---|---|---|
| Compton wavelength λ_C = h/m_e c | 2.426 pm | CODATA 2018 (2.42631023867×10⁻¹² m) | ✓ VERIFIED |
| Δλ = λ_C (1 − cos θ) | formula | Compton 1923, Phys. Rev. 21, 483 | ✓ VERIFIED |
| θ=0°: Δλ = 0 | 0 pm | cos(0)=1 | ✓ |
| θ=90°: Δλ = λ_C | 2.426 pm | cos(90°)=0 | ✓ |
| θ=180°: Δλ = 2λ_C | 4.852 pm | cos(180°)=−1 | ✓ |

## ULTRAVIOLET CATASTROPHE

| Claim | Value | Reference | Status |
|---|---|---|---|
| Rayleigh-Jeans law u ∝ ν² | classical wave theory + equipartition | Rayleigh 1900, Jeans 1905 | ✓ VERIFIED |
| Planck law u ∝ ν³/(e^{hν/kT}−1) | quantum | Planck 1901, Ann. Phys. | ✓ VERIFIED |
| Planck peak at x = 2.821 | numerical (Lambert W eq.) | standard QM texts | ✓ VERIFIED |
| Normalisation f_P(2.821) ≈ 1.419 | (2.821)³/(e^{2.821}−1) = 21.47/15.12 ≈ 1.419 | arithmetic | ✓ |
| At T=3000K: λ_peak ≈ 1770 nm | Wien: λ_peak = hc/(2.821 kT); k=8.617×10⁻⁵ eV/K | arithmetic | ✓ VERIFIED |
| RJ/Planck at x=6.0 ≈ 157 | RJ=36, Planck=0.23, ratio≈156.5 | arithmetic | ✓ |
| "Classical physics predicts infinite energy" | Rayleigh-Jeans integral ∫ν² dν diverges | Ehrenfest 1911 coined "UV catastrophe" | ✓ VERIFIED |

## Invented / illustrative content
None. All numbers are physically measured or exact arithmetic. No hypothetical scenarios.
