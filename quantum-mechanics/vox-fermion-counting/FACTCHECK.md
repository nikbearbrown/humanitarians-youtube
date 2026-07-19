# FACTCHECK — vox-fermion-counting

## Claims audit

| Beat | Claim | Verdict | Source | Fix |
|------|-------|---------|--------|-----|
| B03 | "Two distinguishable particles, two states: 4 arrangements" | ✓ | M-14 table: "Maxwell-Boltzmann: 4" | — |
| B04 | "Identical bosons: 3 arrangements" | ✓ | M-14 table: "Bose-Einstein: 3" | — |
| B05 | "Fermion wavefunction is antisymmetric under particle exchange" | ✓ | Standard QM; M-14 section "Identical Particles" | — |
| B05 | "Double occupancy gives wavefunction = its own negative → must be zero" | ✓ | Slater determinant vanishes when phi_a = phi_b | — |
| B06 | "Identical fermions, two states: 1 arrangement" | ✓ | M-14 table: "Fermi-Dirac: 1" | — |
| B07 | "Pauli exclusion = zero amplitude, not a prohibition posted on a wall" | ✓ | Standard QM interpretation | — |
| B08 | "Electrons fill shells one per spin state — periodic table structure" | ✓ | Standard consequence of Pauli exclusion | — |
| B09 | "Three fermions, two states: impossible" | ✓ | Can't place 3 fermions in 2 states without double-occupancy | Labeled illustrative |
| B09 | "Three classical particles, two states: 8 configurations" | ✓ | 2^3 = 8 for distinguishable particles | Labeled illustrative |
| B09 | "Three identical bosons, two states: 4 configurations" | ✓ | (0,3),(1,2),(2,1),(3,0) = 4 | Labeled illustrative |

## Terms table
| Term | Debut beat | Prior need |
|------|-----------|-----------|
| Maxwell-Boltzmann | B03 | B02 establishes counting puzzle |
| Bose-Einstein | B04 | B03 establishes classical baseline |
| antisymmetric wavefunction | B05 | B04 establishes indistinguishability |
| Pauli exclusion | B06 | B05 establishes antisymmetry mechanism |

## Illustrative numbers
- B09: 2 particles, 2 states: MB=4, BE=3, FD=1 — consistent with chapter table.
- B09: 3 particles, 2 states: MB=8, BE=4, FD=0 — consistent with Pauli.

## Exclusions confirmed
- No Slater determinant formula on screen. ✓
- No Gibbs paradox derivation. ✓
- No connection to superconductivity or BEC. ✓
