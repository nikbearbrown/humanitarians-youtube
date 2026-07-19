# FACTCHECK — vox-phasor-stationary

## Claim-by-claim audit

| Beat | Claim | Verdict | Source | Fix |
|------|-------|---------|--------|-----|
| B01 | "Physics calls it a stationary state" | ✓ | M-01 §In the Quantum Series: "This is why stationary states have definite energy" | — |
| B01 | "The wavefunction never stops spinning" | ✓ | M-01: "a phasor rotating at rate E/ħ" | — |
| B02 | "rotates at rate E over h-bar" | ✓ | M-01: "rotating at rate E/ħ" | — |
| B02 | "probability stays flat" | ✓ | M-01: "probability density |ψ(x,t)|² = |ψ(x)|² is time-independent" | — |
| B03 | "psi lives in the complex plane — real part and imaginary part" | ✓ | M-01 §Complex Arithmetic: z = a + bi | — |
| B04 | "time factor is e^{-iEt/ħ}" | ✓ | M-01: "The time-dependent factor for a stationary state of energy E is e^{-iEt/ħ}" | — |
| B04 | "unit arrow, length exactly one" | ✓ | M-01: "|e^{iθ}| = 1 for all real θ"; here exponent is purely imaginary so modulus = 1 | — |
| B05 | "probability is psi-star times psi, the modulus squared" | ✓ | M-01: "Born's rule gives |ψ|² = ψ*ψ" | — |
| B05 | "when you multiply a unit arrow by its conjugate, the phases cancel" | ✓ | e^{-iEt/ħ} · e^{+iEt/ħ} = e^0 = 1; M-01: |e^{iθ}|=1 follows from z·z* = |z|² | — |
| B06 | "psi rotates left, psi-star rotates right by the same amount" | ✓ | Conjugate of e^{-iEt/ħ} is e^{+iEt/ħ}; angles equal and opposite | — |
| B06 | "product stays pinned at the same real number" | ✓ | e^{-iEt/ħ}·e^{+iEt/ħ} = 1, a real constant | — |
| B07 | "spatial part ψ(x) carries all shape information; time factor is pure phase" | ✓ | M-01: separable form ψ(x,t) = ψ(x)·e^{-iEt/ħ} stated; time factor has |·|=1 | — |
| B09 | "hydrogen ground state, energy minus 13.6 eV" | ✓ | Standard result; M-13 mentions energy scales; M-01 uses it as context | Labeled illustrative |
| B09 | "phasor sweeps at 2 × 10^16 rad/s" | illustrative | E/ħ = 13.6 eV / (1.055×10^{-34} J·s) = 2.07×10^{16} rad/s ≈ 2×10^{16} rad/s ✓ | Labeled illustrative in narration |
| B09 | "Probability density: one Bohr radius, locked still" | ✓ | |ψ_{100}|² peaks at one Bohr radius; time-independent confirmed | Labeled illustrative |

## Terms table

| Term | Debut beat | Prior beat creating the need |
|------|-----------|------------------------------|
| stationary state | B01 | B01 (names the mystery) |
| phasor | B01 | B01 (arrow that spins = phasor defined by context) |
| complex plane | B03 | B01–B02 (viewer needs to know where the rotation happens) |
| modulus squared | B05 | B04 (viewer has seen unit arrow; needs to know what probability extracts from it) |
| probability density | B05 | B02 (probability staying flat mentioned; now named) |
| phase / pure phase | B07 | B05–B06 (viewer has seen phases cancel; now gets the name) |

## Illustrative numbers
- B09: Energy −13.6 eV (hydrogen ground state), rotation rate ~2×10^16 rad/s, peak density at one Bohr radius — all labeled illustrative; not derived in the reel, consistent with chapter source material.

## Exclusions confirmed
- No full TDSE derivation or evolution for superpositions — confirmed absent.
- No treatment of superposition interference term 2Re(ψ₁*ψ₂) — confirmed absent.
- Single eigenstate only — confirmed.
- No global vs. relative phase discussion — confirmed absent.
