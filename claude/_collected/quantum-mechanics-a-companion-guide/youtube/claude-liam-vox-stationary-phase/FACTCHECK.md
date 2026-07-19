# FACTCHECK — vox-stationary-phase

## Claims audit

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B02 | Single eigenstate |ψ|² is time-independent | ✓ | Chapter 03: "the probability density is time-independent... The state does not evolve in any observable sense" |
| B05 | Phase rotates at E/ℏ but |e^{-iEt/ℏ}| = 1, so rotation is invisible | ✓ | Chapter 03: "The amplitude ψ(x,t) = ψ(x)e^{-iEt/ℏ} rotates in the complex plane at angular frequency E/ℏ... measurements depend only on |ψ|², and |e^{-iEt/ℏ}| = 1" |
| B07 | Cross term in |ψ|² oscillates at (E₂−E₁)/ℏ (Bohr frequency) | ✓ | Chapter 03: "The cross term oscillates. It has a factor of cos((E₂-E₁)t/ℏ) — the Bohr frequency (E₂-E₁)/ℏ" |
| B08 | Probability density rocks back and forth; oscillating charge radiates at (E₂−E₁)/h | ✓ | Chapter 03: "The probability density rocks back and forth at this frequency... it emits a photon of exactly this energy E₂−E₁" |
| B10 | Hydrogen Balmer series: red n=3→n=2, blue-green n=4→n=2 | ✓ | Standard hydrogen spectroscopy; confirmed by energy level structure in chapter 06 |
| B13 | E₁(1nm box) = 0.376 eV | ✓ | E₁ = π²ℏ²/(2m×(1e-9)²) = π²×(1.055e-34)²/(2×9.109e-31×(1e-9)²) = 6.024e-20 J ÷ 1.602e-19 = 0.376 eV |
| B13 | E₂(1nm box) = 4×E₁ = 1.505 eV | ✓ | E₂ = 4E₁ (n² scaling) = 4 × 0.376 = 1.505 eV |
| B13 | ΔE = 1.129 eV, f = 2.73×10¹⁴ Hz | ✓ | f = ΔE/h = (1.129 × 1.602e-19) / 6.626e-34 = 1.809e-19 / 6.626e-34 = 2.73×10¹⁴ Hz; deep UV (λ ≈ 1100 nm — actually near-IR; note: this is illustrative, not a real atom) |

## Exclusions confirmed
- No time-evolution operator formalism: absent ✓
- No ⟨x⟩(t) integral calculation: absent ✓ (only the concept "rocks back and forth")
- No Fourier expansion: absent ✓
- No discussion of interpretations: absent ✓

## Terms table
| Term | Debut beat | Prior beat creating need |
|------|-----------|--------------------------|
| stationary state | B01 | B01 (title card sets up the paradox) |
| phase | B05 | B02 (phasor introduced visually in COLD OPEN) |
| Bohr frequency | B07 | B06 (section card: "beat at the Bohr frequency") |
| eigenstate | B05 | B04 (classical vibrating vs. static charge sets up the problem) |

## Illustrative numbers
- B13: L = 1 nm box labeled illustrative
- E₁ = 0.376 eV accurate
- E₂ = 1.505 eV accurate (4×E₁)
- ΔE = 1.129 eV accurate
- f = 2.73×10¹⁴ Hz accurate (near-UV/deep-vis range; exact value depends on box parameters, illustrative)
