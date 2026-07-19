# FACTCHECK — vox-angular-momentum-ell

## Claims audit

| Beat | Claim | Verdict | Source |
|------|-------|---------|--------|
| B01 | The eigenvalue of L-squared is ell(ell+1)h-bar-squared | ✓ | Chapter 7; standard QM |
| B02 | Maximum L-z eigenvalue is ell*h-bar | ✓ | Chapter 7 |
| B04 | m-values run from -ell to +ell in integer steps | ✓ | Chapter 7 |
| B05 | L-squared = L-x-squared + L-y-squared + L-z-squared | ✓ | Standard definition |
| B07 | Expanding L-minus times L-plus produces a cross-term -h-bar*L-z | ✓ | Chapter 7, commutator algebra |
| B09 | Top-rung condition: L-plus kills the state, fixes eigenvalue as ell(ell+1) | ✓ | Chapter 7 |
| B13 | For ell=2: naive guess 4 h-bar-squared, actual 6 h-bar-squared | ✓ | 2×3=6, standard d-orbital |
| B13 | Extra 2 h-bar-squared from commutator cross-term | ✓ | Chapter 7 |
| B13 | Five m-values for ell=2: -2,-1,0,1,2 | ✓ | Standard |

## Exclusions confirmed
- No Lie-algebra representation theory: absent ✓
- No Clebsch-Gordan addition: absent ✓  
- No spherical harmonics derivation: absent ✓
- No half-integer spin: orbital only, ell=2 example ✓

## Terms table
| Term | Debut beat | Prior beat creating need |
|------|-----------|--------------------------|
| eigenvalue | B01 | B01 (shown as the gap formula setup) |
| L-squared | B02 | B01 (mentioned in setup) |
| m-values / ladder | B04 | B03 (question beat sets context) |
| commutator | B07 | B06 (section card: "commutator creates extra term") |
| raising operator | B07 | B06 (mechanism card) |
| top rung | B09 | B07 (ladder concept established) |

## Illustrative numbers
- B13: ell=2 d-orbital example is illustrative context but ell(ell+1) = 6 is mathematically exact, labeled illustrative on card
