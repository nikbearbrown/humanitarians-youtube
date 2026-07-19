# FACTCHECK — vox-larmor-precession

## Claims audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B01 | Every MRI scanner uses proton spin precession | ✓ | Ch.07: "omega_L = gamma*B is the equation that every MRI scanner runs on" |
| B02 | Proton spin in z-field tilts and circles like a tilted top | ✓ | Ch.07 Larmor precession section |
| B03 | z-component stays exactly fixed during precession | ✓ | Ch.07: "The polar angle never changes. Only the azimuth moves" |
| B06 | The Larmor precession arises from differential phase advance of up/down eigenstates | ✓ | Ch.07: time evolution e^{-iomega_L t/2} on up, e^{+iomega_L t/2} on down |
| B07 | Larmor frequency: omega = gamma * B | ✓ | Ch.07: boxed result omega_L = gamma*B_0 |
| B07 | Gamma depends on the particle species | ✓ | Ch.07: gamma_e ≈ 28 GHz/T for electron, gamma_p ≈ 42.58 MHz/T for proton |
| B09 | Proton at 1.5 T precesses at 63.9 MHz | ✓ | Ch.07 table: 1.5 T → 63.87 MHz ≈ 63.9 MHz |
| B09 | At 3 T, rate doubles to 127.7 MHz | ✓ | Ch.07: 3.0 T research MRI → 127.7 MHz |
| B10 | Spin at 60° tilt: z-component = hbar*cos(60°) = hbar/2 | ✓ | Lz = hbar*(1/2)*cos(theta) = hbar/2 for theta=60° ✓ |
| B10 | Transverse signal oscillates at exactly 63.9 MHz | ✓ (illustrative) | From Larmor precession formula at 1.5 T |

## Terms table

| Term | Debut beat | Prior beat creating need |
|------|-----------|--------------------------|
| spin / proton spin | B01 | — (hook) |
| Bloch sphere / precession | B02 | B01 (circling established) |
| z-component frozen | B03 | B02 (two aspects separated) |
| Larmor frequency | B07 | B06 (mechanism explained) |
| gyromagnetic ratio (gamma) | B07 | B07 (introduced with formula) |
| MHz | B09 | B07 (frequency concept established) |

## Illustrative numbers
- B10: specific setup (physicist, 60° tilt, 1.5 T) labeled illustrative; numbers computed from chapter formulas
