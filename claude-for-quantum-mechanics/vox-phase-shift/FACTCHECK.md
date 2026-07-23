# FACTCHECK — vox-phase-shift

## Claims audit

| Beat | Claim | Verdict | Source / note |
|------|-------|---------|---------------|
| B01 | Scattered wave crests shift compared to free-particle reference | ✓ | Ch07 p.2: "phase shift … the phase by which the potential has shifted the outgoing wave relative to a free particle" |
| B01 | That shift is the signature of the force | ✓ | Ch07: phase shifts encode all elastic scattering info for central potentials |
| B02 | Attractive vs. repulsive distinguishable by crest positions | ✓ | Ch07 p.3: "An attractive potential draws the wave closer to the origin, advancing the phase, so δ_ℓ > 0. A repulsive potential pushes the wave outward, so δ_ℓ < 0." |
| B04 | Far from scatterer, scattered wave looks like free-particle wave shifted in phase | ✓ | Ch07 eq. for u_ℓ: sin(kr − ℓπ/2 + δ_ℓ)/kr |
| B04 | Phase shift measured by comparing to reference wave with no scatterer | ✓ | Standard definition: δ_ℓ is the shift relative to free-particle sin(kr − ℓπ/2) |
| B05 | Same wavelength, same energy — just displaced | ✓ | Far-field: same k, same λ = 2π/k; only phase is shifted |
| B05 | Displacement in wave-cycle units is phase shift delta | ✓ | δ_ℓ in radians; 2π radians = one full cycle |
| B06 | Positive delta = crests ahead; negative delta = crests behind | ✓ | Ch07: δ > 0 attractive (crests advanced), δ < 0 repulsive (crests retarded) |
| B07 | Attractive well: particle faster inside, shorter wavelength inside | ✓ | Classical analogy holds: E_tot = KE + PE; lower PE in well → higher KE → faster → shorter λ inside. Ch07 uses this to justify δ > 0 for attractive |
| B07 | More wave cycles crammed in → crests ahead → positive delta | ✓ | Standard derivation; consistent with Ch07 sign convention |
| B08 | Repulsive barrier: particle slower inside, longer wavelength inside | ✓ | Higher PE in barrier → lower KE → slower → longer λ inside |
| B08 | Fewer cycles in same space → crests behind → negative delta | ✓ | Ch07 sign: δ < 0 for repulsive |
| B09 | Stronger attractive well → larger positive phase shift | ✓ | Deeper well → more KE gained → more phase accumulated inside → larger δ |
| B09 | Deeper repulsive barrier → larger negative phase shift | ✓ | Larger barrier → more KE lost → fewer cycles inside → more negative δ |
| B10 | At delta = ±90 degrees, scattering maximally strong — resonance | ✓ | Ch07: σ_ℓ ∝ sin²δ_ℓ; maximum at δ_ℓ = ±π/2 = unitarity limit |
| B10 | "unitarity allows" — correctly scoped as maximum allowed by probability conservation | ✓ | Ch07: "bounded by the unitarity limit 4π(2ℓ+1)/k²" |
| B11 | Every elastic scattering problem → phase shifts per angular-momentum channel | ✓ | Ch07: "every elastic scattering problem with spherical symmetry reduces to determining the phase shifts" |
| B11 | Measure scattered intensity at angles → extract phase shifts → reconstruct force | ✓ | Standard inverse scattering — phase-shift analysis (PSA) in nuclear physics |
| B12 | Proton-proton scattering phase shifts used to map nuclear force before theory | ✓ | Historical fact: PSA of pp scattering data in 1950s-60s; consistent with Ch07 |
| B13 | Illustrative example: 2 eV well, 0.5 nm radius, 1 eV electron → ~30 deg phase shift | ILLUSTRATIVE | Made-up round numbers for pedagogical illustration; labeled illustrative |
| B13 | Inside attractive well: electron faster, wavelength shorter, crests advance → positive delta | ✓ | Consistent with mechanism beats B07-B09 |
| B13 | Same geometry but barrier: electron slower, crests fall behind → negative delta | ✓ | Sign flip from well to barrier is exact |

## Terms table

| Term | Debut beat | Prior need created by |
|------|------------|----------------------|
| phase shift (delta) | B05 | B04 (introduces comparison to reference wave, creates need for a name for the displacement) |
| reference wave / free particle wave | B04 | B01 (mystery wave shifts — need to compare to something) |
| angular-momentum channel | B11 | B09 (size/sign of delta encodes strength/type — implies one delta per channel) |
| resonance | B10 | B09 (maximum scattering hinted) |
| scattering length | NOT USED | excluded per card |
| Levinson theorem | NOT USED | excluded per card |
| partial-wave sum formula | NOT USED | excluded per card |
| cross-section formula | NOT USED | excluded per card |

## Exclusion confirmation
- "no partial-wave-sum formula" — f(θ) = 1/k Σ (2ℓ+1) e^{iδ} sinδ P_ℓ appears nowhere
- "no cross-section derivation" — σ = 4π/k² Σ sin²δ_ℓ appears nowhere
- "no Levinson theorem" — appears nowhere

## Illustrative numbers (B13)
- "two electron-volts, radius half a nanometer, kinetic energy one electron-volt, phase shift about thirty degrees" — all illustrative, reasonable order of magnitude for a nuclear/atomic-scale well. Labeled illustrative in narration ("Illustrative:").
