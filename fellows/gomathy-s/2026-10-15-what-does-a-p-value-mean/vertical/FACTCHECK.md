# FACTCHECK — p-value

| # | Beat | Claim | Verdict | Source |
|---|---|---|---|---|
| 1 | B00–B03, B09 | p-value = probability of data at least as extreme as observed, assuming the null and the model | ✓ PASS (plain paraphrase, INFERENCE noted) | ASA definition |
| 2 | B04 | P(X ≥ 9), X ~ Binomial(10, ½) = 11/1024 ≈ 0.0107 | ✓ PASS — computed; one-sided (two-sided 22/1024 ≈ 0.021) | `scenes.py` assert |
| 3 | B05 | Not P(hypothesis true); not effect size or importance | ✓ PASS — verbatim principles 2, 5 | ASA |
| 4 | B06 | SD 10. n = 50,000/group, Δ = 0.2: z = 3.16, two-sided p ≈ 0.0016 (shown 0.002). n = 10/group, Δ = 5: t = 1.118, df 18, two-sided p ≈ 0.278 (shown 0.28) | ✓ PASS — computed (scipy t-test for the small study; normal approx for the huge one) | ILLUSTRATIVE |
| 5 | B07 | Don't decide on a threshold alone; p alone isn't good evidence | ✓ PASS — principles 3, 6 | ASA |
| 6 | B08 | Full reporting; report effect size and its interval | ✓ PASS — principle 4; CI row is INFERENCE | ASA |

Algebra checked separately from typography (MATH-TYPESETTING.md):
B04 equality 11/1024 is exact; "≈ 0.011" is a rounding (0.01074). B06 "≈"
on both p-values. Details: `SOURCES.md`.
