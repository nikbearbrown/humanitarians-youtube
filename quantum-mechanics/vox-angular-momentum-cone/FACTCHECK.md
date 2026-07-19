# FACTCHECK — vox-angular-momentum-cone

## Claims audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B01 | Quantum angular momentum refuses to point straight up even at maximum alignment | ✓ | Ch.06 §"Why the Angular Momentum Vector Cannot Fully Align" |
| B02 | At max orientation, vector sweeps a cone | ✓ | Ch.06 §cone diagram, Fig 6.3 |
| B03 | Total = hbar*sqrt(ell(ell+1)), max z = ell*hbar | ✓ | Ch.06 boxed spectrum result |
| B03 | These two numbers are never equal | ✓ | sqrt(ell(ell+1)) > ell for all finite ell≥0 (since ell+1>ell) |
| B06 | L^2 = Lx^2 + Ly^2 + Lz^2; each term non-negative | ✓ | Standard QM |
| B07 | Sideways components carry unavoidable spread in Lz eigenstate | ✓ | Ch.06: sigma_Lx = sigma_Ly = hbar*sqrt(ell/2) > 0 for ell>0 |
| B08 | The gap is hbar*root-ell (sideways contribution) | ✓ | Ch.06: <Lx^2>+<Ly^2> = hbar^2*ell, so sideways RMS ~ hbar*sqrt(ell) |
| B09 | Cone half-angle = arccos(ell / sqrt(ell(ell+1))) | ✓ | Ch.06 §cone text |
| B09 | For ell=1, half-angle ~35 degrees | minor | arccos(1/sqrt(2)) = 45 deg, not 35. Corrected below — see fix. |
| B10 | As ell->inf, cone narrows to zero | ✓ | Ch.06: half-angle -> 0 as ell->inf |
| B11 | No definite direction in space — not measurement disturbance | ✓ | Ch.06: Lx, Ly undefined in Lz eigenstate |
| B12 | ell=2 total = hbar*sqrt(6) ~ 2.45 hbar | ✓ | sqrt(2*3) = sqrt(6) ✓ |
| B12 | ell=2 max z = 2*hbar | ✓ | m_max = ell = 2 |
| B12 | ell=2 half-angle ~35 degrees | minor | arccos(2/sqrt(6)) = arccos(0.8165) = 35.26 deg ✓ (B09 was wrong; ell=1 gives 45 deg) |
| B13 | ell=10 half-angle ~18 degrees | ✓ (illustrative) | arccos(10/sqrt(110)) = arccos(0.9535) ≈ 17.5 deg ~ 18 deg ✓ |

### Fix for B09 narration
B09 says "For ell equals one, that is about 35 degrees" — this is wrong. ell=1 gives arccos(1/sqrt(2)) = 45 deg. 35 degrees is ell=2. Fix: change B09 to say "For ell equals two, that is about 35 degrees."

(Beat sheet B09 narration updated to ell=2 example.)

## Terms table

| Term | Debut beat | Prior beat creating need |
|------|-----------|--------------------------|
| angular momentum | B01 | — (assumed prior knowledge per card) |
| z-component / z-shadow | B02 | B01 (sets up the comparison) |
| hbar | B03 | B03 (introduced with magnitude formula) |
| ell (quantum number) | B03 | B02 (projection labeled ell*hbar) |
| cone / precession | B02 | B01 (leaning, sweeping) |
| sideways components (Lx, Ly) | B06 | B05 (Lz defined, now the rest) |
| quantum uncertainty | B07 | B06 (squares must be zero → can't be) |
| cone half-angle | B09 | B08 (the gap established) |
| classical limit | B10 | B09 (cone angle approach) |

## Illustrative numbers
- B12: ell=2 calculation is from the actual spectrum (not invented), labeled as a worked example
- B13: ell=10 half-angle is computed from actual formula, labeled illustrative
