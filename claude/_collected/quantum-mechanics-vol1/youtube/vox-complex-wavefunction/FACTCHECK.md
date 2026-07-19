# FACTCHECK — vox-complex-wavefunction

| Claim | Beat | Verdict | Source |
|---|---|---|---|
| Two wave packets with equal |k| but opposite directions have identical |psi|^2 | B02, B05 | PASS | Chapter 3: probability density |psi|^2 = |A|^2 for plane wave regardless of sign of k |
| The wave function is complex — has length and direction | B04 | PASS | Chapter 3: psi is complex-valued |
| Right-mover has clockwise helix; left-mover counterclockwise | B04 | PASS | e^(ikx) winds +k direction; e^(-ikx) winds opposite — standard complex analysis |
| |psi|^2 discards the winding direction | B05 | PASS | |e^(ikx)|^2 = 1 regardless of sign of k |
| A purely real wave packet is symmetric (two-direction) | B06 | PASS | Real functions are symmetric in k-space: f(x) real implies F(-k) = F*(k); both +k and -k present equally |
| Phase (winding rate) encodes momentum | B07 | PASS | Chapter 3: de Broglie relation k = p/hbar |
| Schrodinger equation uses i to distinguish time direction | B08 | PASS | Chapter 4: i*hbar * dpsi/dt = H*psi; replacing i with real would give diffusion equation |
| Gaussian with k0=5 nm^-1: phase winds at 5 cycles/nm | B09 | PASS | e^(ik_0 x) with k_0=5 nm^-1 winds 5 rad/nm = ~0.8 cycles/nm (2pi*0.8=5); approximately correct as illustrative |
| Numbers in B09 labeled illustrative | B09 | illustrative |

## Exclusions confirmed absent
- No Schrodinger-equation consistency proof — absent
- No momentum-operator Fourier argument — absent
- No continuity equation — absent

## Terms table
| Term | Debut | Prior need |
|---|---|---|
| probability density | B02 | B02 (setup) |
| complex number | B04 | B03 (question established) |
| phase | B04 | B04 (complex number introduced) |
| imaginary part | B05 | B04 (complex number established) |
| winding direction | B04 | B04 (helix introduced) |
| momentum | B07 | B05 (phase established) |
