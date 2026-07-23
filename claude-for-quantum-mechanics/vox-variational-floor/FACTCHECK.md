# FACTCHECK — vox-variational-floor

## Claims audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B02 | Hylleraas 1929, one parameter, −77.5 eV; exact −78.98 eV; error ~2% | ✓ | Ch03: "With a single variational parameter, Hylleraas obtained −77.5 eV. Experiment gave −78.98 eV, an error of about 2%" |
| B04 | Any state is a superposition of exact eigenstates | ✓ | Ch03: proof uses expansion |psi> = sum c_n |n> |
| B05 | Energy expectation = weighted average; weights = |c_n|², sum to 1 | ✓ | Ch03: normalization gives sum |c_n|² = 1 |
| B07 | Each E_n >= E_0 by definition of ground state | ✓ | Ch03: "The inequality holds because every E_n >= E_0" |
| B08 | <H> >= E_0 × sum(weights) = E_0 | ✓ | Ch03: direct consequence |
| B11 | One-sided guarantee — always above the truth | ✓ | Ch03: "The method cannot go below" |
| B12 | Getting below exact energy signals calculation error | ✓ | Ch03: "If we minimize over a trial family and obtain a result below the known exact energy, we have made an error" |
| B13 | Hydrogen exact = −0.5 Hartree; four Gaussian basis gives −0.4993 Hartree, error 0.14% | ILLUSTRATIVE | Ch03: "Using four Gaussian basis functions ... the generalized eigenvalue problem gives E_V = −0.4993 Hartree — an error of only 0.14%" — from chapter, labeled illustrative |

## Terms table

| Term | Debuts at | Prior beat creates need |
|------|-----------|------------------------|
| trial wave function | B01 | B01 (concept introduced with helium) |
| ground-state energy | B01 | B01 (what we're bounding) |
| eigenstate | B04 | B03 (need to understand why bound holds) |
| variational method | B09 | B07/B08 (after mechanism explained) |
| Hartree | B13 | B13 (illustrative example only) |
