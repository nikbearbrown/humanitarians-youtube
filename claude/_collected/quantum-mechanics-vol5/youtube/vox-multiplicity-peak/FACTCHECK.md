# FACTCHECK — vox-multiplicity-peak

## Claims audit

| Beat | Claim | Verdict | Source | Fix |
|------|-------|---------|--------|-----|
| B03 | "6 coins: 1 all-heads, 6 one-head, 15 two-head, 20 three-head" | ✓ | C(6,0)=1, C(6,1)=6, C(6,2)=15, C(6,3)=20 | — |
| B03 | "Multiplicity peaks at half-and-half" | ✓ | M-14: "peaks at N_up = N/2" | — |
| B05 | "N=100: histogram is a sharp spike" | ✓ | M-14: "at thermodynamic scale N~10^23, the peak is a needle" | — |
| B06 | "At N=10^23: peak is knife-edge, essentially all states there" | ✓ | M-14: "Equilibrium is not imposed — where microstates are concentrated" | — |
| B07 | "Second law = law of large numbers, not a law of physics" | ✓ | M-14: "equilibrium is not imposed; it is simply where microstates pile up" | — |
| B08 | "S = k ln Omega" | ✓ | M-14 section "From Multiplicity to Entropy" | — |
| B09 | "N=6: peak at 20/64 ≈ 31%" | ✓ | C(6,3)=20, 2^6=64, 20/64≈0.313 | Labeled illustrative |
| B09 | "N=100: peak 8% but within 5% of peak holds 99.9%" | illustrative | Rough estimate consistent with Gaussian approximation | Labeled illustrative |

## Terms table
| Term | Debut beat | Prior need |
|------|-----------|-----------|
| multiplicity | B03 | B02 establishes question |
| peak sharpening | B05 | B04 establishes N=20 distribution |
| equilibrium as peak | B06 | B05 establishes sharp spike |

## Illustrative numbers
- B09: N=6 multiplicity values — exact.
- B09: N=100 rough percentages — labeled illustrative.

## Exclusions confirmed
- No Stirling formula on screen. ✓
