# FACTCHECK — Bayes' Theorem: The Positive That's Usually Wrong

**Verdicts**
- ✓ verified
- minor: true, with a qualifier
- CORRECTED: wrong in the draft or brief, now fixed
- WRONG

"Executed" means the number was produced by `demo/bayes_demo.py`, which uses exact `fractions.Fraction` arithmetic and asserts every relation below. The run is recorded in `demo/RUN-LOG.txt`.

**Hashes**
- Script: sha256 `9d72b9a1e8cd160a…d1d77`
- Evidence: `6bcda52ea4fdcdaf…71eb61`

`make_sheet.py` asserts every spoken number against `evidence.json` before writing the sheet.

| # | Beat | Claim | Verdict | Source / check | Fix |
|---|---|---|---|---|---|
| 1 | brief | "99%-accurate test" | CORRECTED | 99% is the **sensitivity**. Overall accuracy is (99 + 9,405)/10,000 = **95.04%** (executed). | Narration says "a test that catches ninety-nine percent of cases" throughout. Title changed (see #2). |
| 2 | title | "the 99%-accurate test that's usually wrong" | CORRECTED | The test is right 95% of the time overall. What is usually wrong is a **positive** (5/6 of positives are false). | Title is "Bayes' Theorem: The Positive That's Usually Wrong". Open question for the human. |
| 3 | brief | A 1,000-person grid | CORRECTED | At 1,000 people the rates give 9.9 true positives and 49.5 false positives, which are not whole people. `bayes_demo.py` asserts whole counts. | 10,000 people (a 100 × 100 grid). Every count is whole. |
| 4 | B01 | Doctors and students at Harvard teaching hospitals mostly got this puzzle wrong | ✓ | Casscells, Schoenberger & Graboys, *NEJM* 299 (1978) 999–1001: 60 respondents (20 house officers, 20 students, 20 attendings), 11 correct (18%), modal answer 95% (27/60). Figures are as reported in Manrai et al., *JAMA Intern Med* 174 (2014) 991–993, which replicated it at 14/61 correct. | Their puzzle used prevalence 1/1,000 and a 5% false-positive rate; see #5. |
| 5 | B01 | "this exact puzzle" | CORRECTED | Casscells used 1/1,000 and 5%, not our 1% / 99% / 95%. It is the same *kind* of puzzle. | Narration now "this kind of puzzle"; card line "a puzzle like this". |
| 6 | B01 | Screening tests, spam filters and fraud alerts all raise flags that come with a percentage | minor | Each is a binary detector with a reported error rate. Not every product shows its percentage to the user. | Kept as a general statement. No product is named, so the claim won't date. |
| 7 | B02/B13 | A 99% sensitivity does not make a positive 99% sure | ✓ executed | P(D\|+) = 1/6 ≠ 0.99 | — |
| 8 | B03 | Definitions of base rate, sensitivity and specificity | ✓ | Altman & Bland, *BMJ* 1994; Sackett et al. 1991 ch. 4 | — |
| 9 | B11 | 10,000 × 1% = 100 sick; 99 caught, 1 missed | ✓ executed | 100 × 99/100 = 99 | — |
| 10 | B12 | 9,900 healthy; 95% cleared = 9,405; 5% = 495 false positives | ✓ executed | 9,900 × 1/20 = 495 | — |
| 11 | B12 | "Five times as many as the sick people it caught" | ✓ | 495 / 99 = 5 exactly | — |
| 12 | B14/B15 | 594 positives (27 × 22 block) | ✓ executed | 99 + 495 = 594 = 27 × 22 | — |
| 13 | B15 | 99/594 = 1/6; five of six positives are healthy | ✓ executed | gcd(99, 594) = 99 | — |
| 14 | B15 | "≈ 16.67%" chip | ✓ executed | 1/6 = 0.16667 | — |
| 15 | B16 | 99/10,000 = 0.99 × 0.01 = P(+\|D)P(D) | ✓ executed | asserted in script | — |
| 16 | B16 | 594/10,000 = P(+) = 0.0594 | ✓ executed | 0.99·0.01 + 0.05·0.99 = 0.0099 + 0.0495 | — |
| 17 | B16 | Bayes' theorem "flips a conditional chance by weighing in how common each side is" | ✓ | P(A\|B) = P(B\|A)·P(A)/P(B). The ratio P(A)/P(B) is the "how common each side is". | — |
| 18 | B17 | 0.99 × 0.01 / 0.0594 = 1/6 | ✓ executed | 0.0099 / 0.0594 = 1/6 | — |
| 19 | B17 | "Swap its sides and you get a different number" | ✓ | P(+\|D) = 0.99 vs P(D\|+) = 0.1667 | — |
| 20 | B18 | From 1 in 100 to 1 in 6 | ✓ executed | prior 1/100, posterior 1/6. Odds 1:99 → 1:5 (LR+ = 19.8). | — |
| 21 | B18 | Healthy outnumber the sick 99 to 1 | ✓ | 9,900 : 100 | — |
| 22 | B19 | Base rate 1/1,000 gives "about two percent" | ✓ executed | 11/566 = 1.94% | — |
| 23 | B19 | 1/10 gives "about sixty-nine percent" | ✓ executed | 11/16 = 68.75% | — |
| 24 | B19 | 1/2 gives "ninety-five" | ✓ executed | 99/104 = 95.19% | — |
| 25 | BHTF | After two positives, "about four in five", because the first answer became the new base rate | ✓ executed | 99/124 = 79.84% under independence. Applying the 1/6 prior with the same test gives the same 99/124 (sequential = joint). | — |
| 26 | BHTF | Per million: 9,801 sick and 2,475 healthy positive twice | ✓ executed | 10,000·0.99² and 990,000·0.05² | — |
| 27 | BHTF | "A real repeat test often isn't [independent]" | minor | Repeat-test errors are often correlated: the same cross-reacting condition, or the same lab method (Sackett et al. ch. 4). "Often" is a hedge, not a measured rate. | Kept as a caution in the rubric. |
| 28 | B16 | Named after Thomas Bayes | ✓ | Bayes & Price, *Phil. Trans.* 53 (1763). Not said on screen beyond the name. | — |
| 29 | sim | Seeded simulation of 100,000 people agrees | ✓ executed | Seed 20261122: 978 sick, 976 TP, 4,872 FP, PPV 0.1669 vs exact 0.1667. \|err\| 0.0002 < 1 SE (0.0049). | — |

## Algebra checks (MATH-TYPESETTING.md)

**Bars and direction**
- P(D\|+) and P(+\|D) are different quantities. Every MathTex keeps the conditioning event on the right of the bar.
- The TANGENT's values claim (P(B\|A) ≠ P(A\|B)) holds for these numbers. It is not a general inequality; the two are equal when P(A) = P(B).
- For that reason the narration says "you get a different number" about *this* case, and the dim caption should read "here" rather than "always". Noted for scenes.py.

**Total probability**
- P(+) = P(+\|D)P(D) + P(+\|¬D)P(¬D) = 0.0099 + 0.0495 = 0.0594 ✓
- The denominator is the sum over *both* groups. The B16 morph must show 594 = 99 + 495, not 594 = 99 × 6.

**Domains**
- Every probability lies in [0, 1].
- P(+) > 0 is required for the division. Here it is 0.0594.

**Equality vs approximation**
- 1/6 is exact. "≈ 16.67%" is rounded and is shown with ≈.
- The base-rate points "about two" and "about sixty-nine" are rounded. On screen they are 1.94% and 68.75%.

**Numeric case:** 0.99 × 0.01 / 0.0594 = 0.0099 / 0.0594 = 1/6 ✓ (exact Fraction in the script).

**Generalization step (B16)**
- Renaming D → A and + → B is a relabeling, not a derivation.
- The equation is stated for any events with P(B) > 0. The film does not claim to prove it; the counts illustrate it (pedagogy §3: explain, don't derive).

## Format conversion, 2026-11-24 (appended; the rows above are unchanged)

The film was converted from TL;DR to ai-explainer. TL;DR beats B00–B03 are retired, so the Casscells / Harvard claim (rows 4–6) and the Terms card (row 8) are no longer in the film. The body (B10–B19), BVDT, BHTF and BOUT are unchanged, so their rows still apply. Narration approval: the original narration and its post-approval edits (2026-11-22/23); the new B00 and B01 on 2026-11-24, by Anant.

| # | Beat | Claim | Verdict | Source / check | Fix |
|---|---|---|---|---|---|
| 30 | B00 (spoken) | "a test that catches ninety-nine percent of cases says I'm positive" | ✓ | Row 1: 99% is the sensitivity; "catches 99% of cases" is the corrected wording | — |
| 31 | B00 (spoken) | "How likely is it that I'm actually sick? Show me with real numbers." | EXEMPT | The ask: a question | — |
| 32 | B00 (on screen) | "the answer: about 1 in 6, not 99%" | ✓ executed | Row 13: 99/594 = 1/6 | — |
| 33 | B00 (on screen) | "sensitivity: the test catches 99 of every 100 sick people" | ✓ executed | Rows 8–9 | — |
| 34 | B00 (on screen) | "base rate: only 1 in 100 people have the disease" | ✓ executed | Row 9: 10,000 × 1% = 100 | — |
| 35 | B01 | "A positive test can still be a false alarm." | ✓ executed | Rows 10, 13: 495 of 594 positives are healthy | — |
| 36 | B01 | "When a disease is rare, false alarms from the healthy outnumber the real cases." | ✓ executed | Rows 10–11: 495 vs 99 (5×) at a 1% base rate. It does not hold at 50% (row 24), which is why the line says "when rare". | — |
| 37 | B01 | "What decides it is the base rate: how common the disease is." | ✓ (minor) | Rows 22–24: with the same test, the base rate moves the answer from 1.94% to 95.19%. Specificity matters too, but the film does not vary it. | — |
