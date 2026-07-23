# FACTCHECK — vox-spinor-720

## Claims audit

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B02 | Classical vector returns to itself after 360° | ✓ | Standard classical mechanics; rotation matrix R(2π) = I |
| B04 | Classical rotation factor e^{iθ}; at θ=2π, factor=1 | ✓ | Standard rotation group SO(3); e^{i·2π} = 1 |
| B05 | Spin-½ rotation uses θ/2; at θ=2π, factor = e^{iπ} = −1 | ✓ | Chapter 07: "The critical feature is the factor of θ/2 — not θ. Set θ = 2π... Û(2π) = −I" |
| B07 | At θ=720°, spinor factor = e^{i·2π} = +1, state returns | ✓ | Chapter 07: "The state returns to itself only after 720°" |
| B08 | 1975: Werner, Colella, Overhauser, Eagen; neutron interferometry; fringe shifted by π | ✓ | Chapter 07: "In 1975, Werner, Colella, Overhauser, and Eagen split a beam of neutrons, rotated one path by 2π... The interference pattern shifted by exactly π" |
| B08 | Same year: Rauch et al. confirmed independently | ✓ | Chapter 07: "The same year, Rauch and collaborators confirmed it independently" |
| B10 | No classical spinning object behaves this way | ✓ | Chapter 07: "A classical spinning top returns to itself after 360°. Spin-1/2 does not." |
| B13 | Interference intensity I ∝ 1 + cos(θ/2); period 4π | ✓ | Standard result from two-path interferometry with one path rotated: I = |1 + e^{iθ/2}|²/4 = cos²(θ/4), or equivalently I ∝ 1 + cos(θ/2) with 4π period |

## Exclusions confirmed
- No SU(2)/SO(3) group theory discussion: absent ✓
- No Pauli-matrix exponential derivation: absent ✓ (mentioned as "rotation uses θ/2" only)
- No full neutron-interferometer optics: absent ✓

## Terms table
| Term | Debut beat | Prior beat creating need |
|------|-----------|--------------------------|
| spin-½ | B03 | B01 (title sets up the electron; B02 establishes classical comparison) |
| spinor | B06 | B05 (explained as "rotation uses θ/2") |
| neutron interferometry | B08 | B07 (sign flip at 360° established; need experimental confirmation) |

## Numbers
- B13: I ∝ 1 + cos(θ/2) — correct for two-path interferometer where one path acquires phase θ/2. Period = 4π. Confirmed experimentally by Werner et al. and Rauch et al. 1975.
