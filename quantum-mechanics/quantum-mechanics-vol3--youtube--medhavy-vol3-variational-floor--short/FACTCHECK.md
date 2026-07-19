# FACTCHECK — medhavy-vol3-variational-floor/short

All physics facts verified against:
- Griffiths, *Introduction to Quantum Mechanics*, 3rd ed., §8.2 (Helium atom variational calculation)
- NIST Atomic Spectra Database (helium ground state energy)

## Claims verified

| Claim | Source | Status |
|---|---|---|
| E(Z*) = 27.2 eV × (Z*² − 3.375 Z*) | Griffiths Eq. 8.27 | PASS |
| 3.375 = 27/8 (combining −2Z and +5/8 with Z=2) | algebra | PASS |
| Minimum at Z* = 27/16 = 1.6875 | dE/dZ*=0 → Z*=27/16 | PASS |
| E_min ≈ −77.5 eV | 27.2×(1.6875²−3.375×1.6875)=−77.49 eV | PASS |
| True ground state E₀ = −79.0 eV | NIST (−79.005 eV) | PASS |
| Variational principle: E(Z*) ≥ E₀ | Griffiths §8.1 | PASS |
| Gap = 1.5 eV (−77.5 − (−79.0)) | arithmetic | PASS |

## Verdict: APPROVED
