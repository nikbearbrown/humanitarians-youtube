# FACTCHECK — vox-step-reflection

| Claim | Beat | Verdict | Source |
|---|---|---|---|
| Classical ball off downhill step: zero reflection | B02 | PASS | Classical mechanics |
| Quantum particle at a step down can reflect even with E > V0 | B03, B05 | PASS | Chapter 6: reflection from a step when E > 0 |
| Wavelength is shorter on the higher-kinetic-energy side | B04 | PASS | Chapter 6: k = sqrt(2mE)/hbar, shorter lambda for larger E |
| Wave function must be continuous and have continuous derivative at boundary | B05 | PASS | Chapter 6: matching conditions |
| Boundary conditions force a split into transmitted + reflected waves | B05 | PASS | Chapter 6: general solution left and right |
| Impedance mismatch analogy for reflection | B06 | PASS | Chapter 6: same physics as EM/acoustic wave transmission |
| A gradual step reflects less than a sharp step | B07 | PASS | Standard result: adiabatic passage limit |
| A step down reflects as well as a step up for same |k| mismatch | B07 | PASS | R = ((k1-k2)/(k1+k2))^2 symmetric in sign change; step direction irrelevant for magnitude |
| R = ((k1-k2)/(k1+k2))^2 | B08 | PASS | Chapter 6: Eq. for step reflection coefficient |
| Electron 4 eV, step down 3 eV → far-side 7 eV | B09 | PASS | E_far = E + |V_step| = 4+3=7 eV for downward step |
| ~2% reflection for that case | B09 | PASS | k1 = sqrt(2m*4eV)/hbar, k2 = sqrt(2m*7eV)/hbar, ratio sqrt(4/7)≈0.756, R = ((1-0.756)/(1+0.756))^2 ≈ (0.244/1.756)^2 ≈ 0.0193 ≈ 2%; PASS (labeled illustrative) |
| Numbers in B09 labeled illustrative | B09 | illustrative |

## Exclusions confirmed absent
- No probability-current bookkeeping — absent
- No R/T amplitude algebra (only the final formula stated) — absent
- No evanescent-case detour — absent

## Terms table
| Term | Debut | Prior need |
|---|---|---|
| reflection | B01 | B01 (setup) |
| wave number / wavelength | B04 | B04 (quantum wave intro) |
| boundary conditions | B05 | B04 (wavelength mismatch) |
| impedance mismatch | B06 | B05 (split established) |
| reflection coefficient | B08 | B07 (sharpness dependence) |
