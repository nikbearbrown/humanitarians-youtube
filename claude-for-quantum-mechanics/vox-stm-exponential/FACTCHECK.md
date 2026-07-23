# FACTCHECK — vox-stm-exponential

## Claims audit

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B02 | Binnig and Rohrer at IBM Zurich 1981 | ✓ | Chapter 10, PRL 49, 57 (1982) |
| B02 | 1 angstrom step changes current by ~7 | ✓ | Chapter 10: "e^2 ~7.4" |
| B07 | Tunneling probability falls as e^(-2 kappa d) | ✓ | WKB formula, Chapter 10 |
| B07 | kappa ~1 per angstrom for typical metals | ✓ | Chapter 10 |
| B07 | Each angstrom multiplies current by e^2 ~7.4 | ✓ | e^(2*1) = 7.39... |
| B13 | Work function 4 eV gives kappa = 1.02 per angstrom | ✓ | kappa = sqrt(2m*phi)/h-bar, 4 eV gives ~1.02 A^-1 |
| B13 | Gap 5 A: I_0; gap 6 A: I_0/7.4; gap 4 A: 7.4*I_0 | ✓ | exponential calculation |
| B13 | Atom 1 A above neighbors carries 7x more current | ✓ | Direct consequence of e^2 factor |

## Exclusions confirmed
- No kappa derivation from WKB: absent ✓
- No STM feedback electronics: absent ✓
- No surface reconstruction physics: absent ✓
- No scanning-mode details: absent ✓

## Terms table
| Term | Debut beat | Prior beat creating need |
|------|-----------|--------------------------|
| tunneling | B05 | B04 (classical expectation fails, gap is vacuum) |
| exponential decay | B07 | B06 (section card: "e to the minus 2 kappa d") |
| kappa | B07 | B07 (same beat as exponential, needed there) |

## Illustrative numbers
- B13: "I_0" and "I_0/7.4" and "7.4*I_0" are illustrative current values
- kappa = 1.02 A^-1 is exact calculation from 4 eV work function
- The 7x factor is accurate per chapter text
