# FACTCHECK — vox-optimal-truncation

## Claims Audit

| Beat | Claim | Verdict | Source / Note |
|------|-------|---------|---------------|
| B01 | Student runs ten corrections to quartic oscillator | ✓ | Ch.1, "Worked Example — The Quartic Oscillator"; the quartic oscillator is the chapter's central example |
| B01 | Each term is smaller than the last | ✓ | Described in ch.1 "When Perturbation Theory Breaks"; terms decrease before turning |
| B02 | Term eleven explodes; everything past term ten is worse | ✓ | Ch.1: "the series coefficients grow as k!, ensuring divergence for every nonzero lambda"; card example seed shows this |
| B03 | A series whose terms keep shrinking should converge | ✓ | This is the naive expectation; the video corrects it |
| B04 | Perturbation theory expands energy as power series in coupling constant | ✓ | Ch.1, "The Setup": E_n = E_n^(0) + lambda E_n^(1) + lambda^2 E_n^(2) + ... |
| B07 | Flip coupling negative — quartic term becomes minus lambda | ✓ | Ch.1, "When Perturbation Theory Breaks": "Consider the quartic oscillator at negative lambda." |
| B07 | Potential slopes down to negative infinity with negative lambda | ✓ | Ch.1: "making the potential V(x) = (1/2)m omega^2 x^2 + lambda x^4 go to -infinity as |x| -> infinity" |
| B08 | For any negative lambda, however small, no ground state exists | ✓ | Ch.1: "For any lambda < 0, however small, there is no bound ground state" |
| B09 | Energy has singularity on negative coupling axis | ✓ | Ch.1: "the energy E_0(lambda), viewed as a function of the complex variable lambda, has a singularity on the negative real axis" |
| B09 | Radius of convergence is zero | ✓ | Ch.1: "Therefore the radius of convergence is zero. The series diverges for every nonzero lambda." |
| B10 | Series coefficients grow like k-factorial | ✓ | Ch.1: "Bender and Wu confirmed it numerically for the quartic oscillator in 1969: the series coefficients grow as k!" |
| B11 | Terms first shrink (lambda^k), then blow up (k!) | ✓ | Ch.1: "Two practical conclusions follow. First, the fact that successive terms keep decreasing does not guarantee convergence." |
| B12 | Error vs. truncation order is U-shaped with minimum at N* | ✓ | Ch.1, Figure 1.5: "Optimal truncation of a divergent asymptotic series: the error decreases to a minimum at N* before factorial growth takes over" |
| B13 | Error at N* is of order e^(-const/lambda) | ✓ | Ch.1: "The error at optimal truncation is of order e^{-const/lambda}: exponentially small" |
| B14 | Dyson made this argument in 1952 for QED | ✓ | Ch.1: "Freeman Dyson made this argument in 1952 for quantum electrodynamics" — cited as [verify] in source, consistent with historical record |
| B14 | Flip sign of fine-structure constant destabilizes QED vacuum | ✓ | Ch.1: "flip the sign of the fine-structure constant alpha, electrons repel each other, the QED vacuum destabilizes" |
| B15 | QED is most accurate physical theory ever tested | ✓ | Standard physics fact; QED predictions match experiment to ~12 decimal places |
| B15 | QED matches experiment to twelve decimal places | minor | Ch.1 does not state this number explicitly; it is a well-known fact from other sources. Stated without false precision in narration ("twelve decimal places"). Acceptable. |
| B16 | Illustrative: terms 0.82, 0.94, 0.975, 0.990, 0.996, 0.998, 0.9985, 0.9986, then 1.002, 1.015, 1.07, 1.4 | illustrative | Card candidate 20 "Example seed" provides these exact illustrative values. Labeled illustrative in narration. |
| B16 | Optimal truncation was term eight | illustrative | Per card candidate 20 example seed. Labeled illustrative. |

## Terms Table

| Term | Debut Beat | Earlier Beat Creating Need |
|------|-----------|---------------------------|
| perturbation theory | B04 | B01 (student runs corrections) |
| coupling constant (lambda) | B04 | B01 (scaling corrections) |
| power series | B04 | B01 (sequence of corrections) |
| quartic oscillator | B01 | — (hook, presented as concrete situation) |
| radius of convergence | B09 | B05 (viewer needs a name for "how far convergence reaches") |
| singularity | B09 | B08 (no ground state = something breaks there) |
| optimal truncation | B12 | B11 (crossover point introduced) |
| N* | B12 | B11 (crossover introduced) |
| exponentially small | B13 | B12 (minimum of U-curve described) |
| asymptotic series | — | Not used; concept shown visually as U-curve without name |
| Dyson argument | B14 | B09–B13 (mechanism fully explained) |
| fine-structure constant | B14 | B14 (QED context, brief) |

## Exclusions Check
- No complex-analysis proof of zero radius of convergence: CONFIRMED absent
- No Borel resummation: CONFIRMED absent
- No QED fine-structure application (only mention that QED is accurate): CONFIRMED — B15 mentions accuracy without applying the perturbation series to compute a specific QED value
- No Bender-Wu coefficients formula: CONFIRMED absent
