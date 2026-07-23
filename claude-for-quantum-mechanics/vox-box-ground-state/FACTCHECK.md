# FACTCHECK — vox-box-ground-state

## Claims audit

| Claim | Beat | Verdict | Source |
|---|---|---|---|
| Classical marble in box can sit still with zero energy | B01, B02 | PASS | Classical mechanics baseline |
| Quantum particle's lowest energy is above zero | B01, B03 | PASS | Chapter 5: E1 = π²ℏ²/2mL² > 0 |
| Wavefunction must vanish at both walls | B04 | PASS | Chapter 5: boundary conditions ψ(0)=0, ψ(L)=0 |
| Ground state is a half-wavelength sine arch | B05, B06 | PASS | Chapter 5: ψ1 = √(2/L)sin(πx/L), one half-period |
| Curved wavefunction implies momentum | B07 | PASS | Chapter 5: p = ℏk, curvature is spatial frequency |
| Tighter box → higher ground state energy | B08 | PASS | Chapter 5: E1 ∝ 1/L², so smaller L → larger E1 |
| Flat line at zero means no particle | B09 | PASS | Chapter 5: ψ=0 everywhere means no particle |
| Ground state for 1 nm box ≈ 0.38 eV | B10 | PASS | Chapter 5: E1 ≈ 0.377 eV for L=1nm electron |
| Visible light carries ~2 eV | B10 | PASS | Standard photon energy: λ=620nm → 2.0 eV |
| Numbers in B10 are illustrative | B10 | illustrative — labeled "illustrative example" |

## Exclusions confirmed absent
- No eight-step boundary-value derivation (the kL=nπ algebra) — absent
- No normalization constant √(2/L) — absent
- No n² spectrum table — absent

## Terms table
| Term | Debut beat | Prior beat creating need |
|---|---|---|
| wavefunction | B04 | B03 (quantum particle → need to describe it) |
| boundary condition | B04 | B04 (walls force zero — shown visually) |
| ground state | B06 | B05 (minimum arch described → needs name) |
| momentum | B07 | B07 (curvature established → momentum named) |
| kinetic energy | B08 | B07 (momentum named → energy follows) |
| electron-volts | B10 | B10 (illustrative example — unit introduced with comparison) |
