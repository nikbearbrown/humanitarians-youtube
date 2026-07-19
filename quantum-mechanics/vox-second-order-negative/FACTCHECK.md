# FACTCHECK — vox-second-order-negative

## Claims audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B01 | Electric field on hydrogen: first-order correction zero by symmetry | ✓ | Ch01 p.1 — E^(1) = <n^(0)|H'|n^(0)>; for H ground state and linear Stark field, integrand is odd in z so integral vanishes by parity |
| B01 | Second-order correction comes out negative | ✓ | Ch01 — "The second-order correction to the ground-state energy is always negative, for any perturbation whatsoever." |
| B02 | Quartic bump gives negative second-order correction | ✓ | Ch01 — general theorem; quartic oscillator is the worked example |
| B04 | Second-order correction is a sum over all other levels | ✓ | Ch01: E_n^(2) = sum_{m≠n} |<m|H'|n>|^2 / (E_n^(0) - E_m^(0)) |
| B05 | Numerator is squared magnitude, never negative | ✓ | |<m|H'|n>|^2 ≥ 0 by definition of squared absolute value |
| B06 | Every excited level sits above the ground state | ✓ | Definition: ground state = lowest energy eigenstate |
| B08 | Each term: positive numerator / negative denominator = negative | ✓ | For ground state n=0: E_0 - E_m < 0 for all m≠0; numerator ≥ 0; so each term ≤ 0 |
| B09 | Sum is always negative regardless of perturbation | ✓ | Ch01: "regardless of the specific form of the perturbation" |
| B11 | Variational principle: any trial state gives energy above ground state | ✓ | Ch03 (variational principle) — this is correct but only tangentially stated; the connection is valid |
| B13 | Illustrative linear tilt terms: -0.031, -0.0014, -0.00018 (units epsilon^2) | ILLUSTRATIVE | Taken from card example seed; labeled illustrative in narration |
| B13 | Total for linear tilt: -0.034 epsilon^2; quadratic tilt also negative | ILLUSTRATIVE | From card example seed; labeled illustrative in narration |
| B14 | "The ground state has no levels below it" — always negative | ✓ | Core theorem, Ch01 |

All exclusions confirmed absent:
- No derivation of second-order formula ✓
- No sum-over-states computation shown ✓
- No variational upper bound comparison detailed ✓
- No excited-state behavior discussed ✓

## Terms table

| Term | Debuts at | Prior beat that creates need |
|------|-----------|------------------------------|
| perturbation | B01 | B01 (introduced via concrete example) |
| second-order correction | B01 | B01 (named when the mystery appears) |
| matrix element | B04 | B04 (introduced when describing the formula structure) |
| ground state | B01 | B01 (used without prior—universally known prerequisite) |
| excited level / excited state | B06 | B06 (introduced when explaining why denominator is negative) |

## Illustrative numbers
- B13: all numbers (−0.031, −0.0014, −0.00018, −0.034) are illustrative from the card's example seed, labeled as such in narration.
