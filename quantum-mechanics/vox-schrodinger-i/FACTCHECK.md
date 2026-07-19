# FACTCHECK — vox-schrodinger-i

Source: quantum-mechanics-a-companion-guide/chapters/03-the-schrodinger-equation.md

---

## Claims audit

| Beat | Claim | Verdict | Source / Fix |
|------|-------|---------|--------------|
| B02 | Two equations — wave version vs diffusion version — are nearly identical | ✓ | Ch.3 § "The plausibility argument": "without it [i], the equation becomes the diffusion equation" |
| B03 | The only structural difference is the factor of i | ✓ | Ch.3: removing i from iℏ∂ψ/∂t = -(ℏ²/2m)∂²ψ/∂x² gives ∂ψ/∂t = (ℏ/2m)∂²ψ/∂x² — the diffusion equation |
| B05 | Diffusion spreads irreversibly; a blob of heat never contracts spontaneously | ✓ | Standard thermodynamics; Ch.3 confirms: "Solutions spread irreversibly; a localized initial condition smooths out and never recovers." |
| B07 | Without i, the electron packet dissolves (spreads) irreversibly | ✓ | Ch.3: "without it, the equation becomes … the diffusion equation. Solutions spread irreversibly." |
| B09 | Without i, time-derivative and space-derivative contributions add in the same direction, causing diffusion | ✓ | Algebraic fact: without i the equation is purely real diffusion; both ∂t and ∂²x terms have real coefficients and push amplitude outward. |
| B10 | The i rotates the time-derivative contribution 90° in the complex plane; the two terms then interfere, producing wave propagation | ✓ | Ch.3 plausibility argument: i converts -iω → E/ℏ making the time evolution a phase rotation; standard QM result. |
| B11 | The total probability stays exactly 1 because of the i (normalization preserved) | ✓ | Ch.3 § "Normalization is preserved": "The bracket is zero. Normalization is preserved." — depends on Hermiticity of H, which requires i in the kinetic term. |
| B11 | Without i, probability would leak away | ✓ | Without i, ∂t∫|ψ|²dx ≠ 0 in general; diffusion equation does not conserve probability in the quantum-mechanical sense. |
| B13 | Without i, an electron released in a 1-nanometer pocket smears to 10 nm in 3 femtoseconds | illustrative | Numbers from card's Example seed: "its probability cloud hits 10 nm width in 3 femtoseconds" — labeled illustrative per card. |
| B13 | Without i, no interference, no spectral lines, no atoms | ✓ | Ch.3: without wave propagation and phase coherence, interference is impossible and the Bohr frequency cross-terms vanish. |
| B15 | With Schrödinger equation, coherent pulse crosses 5 nm gap and arrives at detector | illustrative | From card's Example seed; labeled illustrative. |
| B15 | Diffusion version: width hits 10 nm in 3 fs | illustrative | From card's Example seed; labeled illustrative. |

## Exclusions confirmed
- No plausibility-argument derivation of the full equation: ✓ (narration never derives iℏ∂ψ/∂t = Hψ step-by-step)
- No Hamiltonian formalism: ✓ (Ĥ never appears on screen)
- No complex number introduction from scratch: ✓
- No interpretation of ψ: ✓

---

## Terms table

| Term | Debut beat | Prior beat that created the need |
|------|-----------|----------------------------------|
| wave (wave packet) | B02 | B01 (electron released, sets up "what does it do?") |
| diffusion / diffusion equation | B05 | B02 (contrasting equation introduced) |
| amplitude | B07 | B05 (diffusion spreads something; B02 wave has something) |
| imaginary unit i | B03 | B02 (two equations shown, difference needs naming) |
| probability / Born rule | B11 | B10 (mechanism of the i established, now consequence) |
| coherent / coherent propagation | B10 | B09 (diffusion vs wave contrast set up) |

All terms debut after the beat that created the viewer's need for them. Vocabulary law: PASS.
