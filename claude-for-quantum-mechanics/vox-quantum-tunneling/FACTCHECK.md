# FACTCHECK — vox-quantum-tunneling

## Claims audit

| Claim | Beat | Verdict | Source |
|---|---|---|---|
| Classical: E < V → total reflection | B02 | PASS | Classical mechanics; chapter 6 confirms |
| Quantum: some fraction transmits when E < V | B03 | PASS | Chapter 6: T > 0 from tunneling |
| Wavefunction decays exponentially inside barrier | B04 | PASS | Chapter 6: psi ~ e^(-kappa*x) inside barrier |
| Exponential never reaches exactly zero | B05 | PASS | Mathematical fact; chapter 6 states this |
| T ~ e^(-2*kappa*L) | B06 | PASS | Chapter 6: WKB approximation, thick barrier limit |
| Transmitted particle has same energy as incident | B07 | PASS | Chapter 6: elastic tunneling, no energy change |
| Alpha decay runs on tunneling | B08 | PASS | Chapter 6: Gamow's theory explicitly mentioned |
| STM uses tunneling (exponential sensitivity) | B08 | PASS | Chapter 6: one angstrom changes current by ~7-10x |
| T ~ 10^-4 for 1 eV electron, 5 eV barrier, 5 A wide | B09 | PASS | Chapter 6: worked calculation gives T ≈ 9.1×10^-5 |
| Numbers in B09 labeled illustrative | B09 | illustrative |

## Exclusions confirmed absent
- No sinh^2 exact formula — absent
- No four-region matching algebra — absent
- "Borrowed energy" framing debunked in B07, not used elsewhere — PASS

## Terms table
| Term | Debut beat | Prior beat creating need |
|---|---|---|
| wavefunction | B04 | B03 (quantum particle needs description) |
| exponential decay | B04 | B04 (wavefunction inside barrier — shown) |
| tunneling | B05 | B05 (transmitted wave emerges → needs name) |
| classically forbidden | B06 | B06 (kappa formula context) |
| transmission | B06 | B05 (fraction that emerges needs quantification) |
