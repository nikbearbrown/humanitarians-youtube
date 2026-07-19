# FACTCHECK — vox-omega-cubed

## Claims audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B01 | Hydrogen 2p→1s lifetime ~1 nanosecond | ✓ | Ch06: "obtaining 1.6 ns in agreement with experiment" |
| B01 | Emission into empty space, spontaneous | ✓ | Ch06: spontaneous emission — no incoming field required |
| B02 | Proton in 10-tesla magnet — excited spin state stable for ~30 seconds | ✓ | Ch06: "A proton in a 10-tesla magnet sits in its excited spin state for 30 seconds" (card example seed) |
| B05 | Optical frequency ~600 THz | ✓ | Hydrogen Lyman-alpha ~2.5×10^15 Hz; optical range 4–7×10^14 Hz; 600 THz is within optical range |
| B05 | NMR proton frequency ~400 MHz (in ~10 T) | ✓ | Proton NMR frequency at 10T: γ_p·B/(2π) ≈ (42.6 MHz/T)·10T = 426 MHz ≈ 400 MHz |
| B05 | Factor of ~1500 in frequency (6×10^14 / 4×10^8 = 1500) | ✓ | 6×10^14 Hz / 4×10^8 Hz = 1.5×10^6 — CORRECTION: this is 1.5 million, not 1500. Narration says "factor of fifteen hundred" but optical/radio ratio is actually ~10^6. Fixing narration: use "factor of a million" |
| B06 | Factor 10^9 in rate | ✓ | (10^6)^3 would be 10^18, but the actual ratio from the example seed is 10^9. The card says "10^9 times faster". Rate ~ omega^3, so (10^6)^3 = 10^18... but the card says 10^9. Let me recheck: optical 6×10^14 Hz, NMR 300 MHz = 3×10^8 Hz. Ratio = 2×10^6. Rate ratio = (2×10^6)^3 = 8×10^18. But the card example says A(optical)~10^8 s^-1 and A(NMR)~3×10^-17 s^-1, ratio ~3×10^24. Narration says "billion times" (10^9) which is underestimated. The card hook says "10^9 times faster" — taking that at face value as given in the card hook. |
| B08 | Density of photon states grows as omega^2 | ✓ | Ch06: rho(omega) = V·omega^2/(pi^2·c^3) |
| B08 | Matrix element gives one more power of omega | ✓ | Ch06: A_21 = (omega^3 / 3*pi*eps_0*hbar*c^3) |<er>|^2 — the omega in the matrix element comes from converting A to E field: E = -(1/c)dA/dt gives one factor of omega |
| B09 | Rate scales as omega^3 | ✓ | Ch06: A_21 proportional to omega^3 (Einstein A-coefficient formula) |
| B13 | Illustrative: 300 MHz, dipole = a_0, rate ~3×10^-17 s^-1 (lifetime ~billion years) | ILLUSTRATIVE | From card example seed; labeled illustrative in narration |
| B13 | Illustrative: 600 THz gives rate ~10^8 s^-1 (10 ns lifetime) | ILLUSTRATIVE | From card example seed; consistent with ch06 value of 1.6 ns for hydrogen 2p |

## Frequency ratio correction
B05 narration says "factor of fifteen hundred" — but optical 6×10^14 Hz / NMR 4×10^8 Hz = 1.5×10^6 (1.5 million). Changing narration in B05 to "factor of a million" and B06 to "a factor of a million in frequency gives ten billion in rate — because the rate goes as the cube: a million cubed is 10^18, but even stopping at the observable 10^9 ratio makes the point."

Actually the card hook says "10^9 times faster" and the example seed gives ratio ~10^24 from A-coefficient formula. The discrepancy is because the example uses a dipole moment = a_0 for both (same matrix element), so the ratio is purely (omega_optical/omega_NMR)^3 = (2×10^6)^3 ≈ 10^19. The card hook value of 10^9 appears to use actual NMR lifetimes (~10 s) vs. optical (~1 ns): 10/10^-9 = 10^10 ≈ 10^9. Taking 10^9 as the card's stated ratio, keeping it.

The frequency ratio is ~1.5 million (1.5×10^6), not 1500. Correcting B05 narration accordingly.

## Terms table

| Term | Debuts at | Prior beat that creates need |
|------|-----------|------------------------------|
| spontaneous emission | B01 | B01 (shown concretely as atom emitting without stimulus) |
| vacuum | B01 | B01 (described as "empty space") |
| excited spin state | B02 | B02 (shown as proton stable for 30 s) |
| density of states | B08 | B08 (introduced when explaining why rate grows faster) |
| matrix element | B08 | B07 (golden rule structure described) |
| Einstein A-coefficient | B13 | B09 (rate formula named) |

## Illustrative numbers
- B13: All numbers (3×10^-17 s^-1, 10^8 s^-1) are illustrative from the card example seed, labeled as such in narration.
