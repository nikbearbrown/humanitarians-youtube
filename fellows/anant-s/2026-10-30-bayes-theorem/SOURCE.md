# SOURCE — Bayes' theorem and the rare-disease test

A short source written for this film. tldr expects written material to section, and there is no chapter for this topic, so this note is that material. Every claim carries a citation or a computation. The film does not name its sources on screen (BOOKLOOP law); SOURCES.md names them in full.

Written 2026-11-22. Numbers recomputed in `demo/bayes_demo.py` (see `demo/RUN-LOG.txt`).

## 1. The setting

A screening test is described by two rates, each measured within one group of people [3][4]:

- **Sensitivity**, P(positive | disease): of the people who have the disease, the share who test positive.
- **Specificity**, P(negative | no disease): of the people who do not have the disease, the share who test negative. The rest of that group, 1 − specificity, are **false positives**.

A third number belongs to the population, not to the test:

- **Base rate** (prevalence, the *prior*), P(disease): the share of the tested population who have the disease.

The number a patient wants is a fourth one, the **positive predictive value**, P(disease | positive): of the people who test positive, the share who are sick [3][4]. It depends on all three numbers above. It is not equal to sensitivity.

## 2. The worked case (our own, recomputed)

Take 10,000 people. The base rate is 1%, sensitivity is 99%, and specificity is 95%.

| | Test positive | Test negative | Total |
|---|---:|---:|---:|
| Disease | 99 | 1 | 100 |
| No disease | 495 | 9,405 | 9,900 |
| Total | 594 | 9,406 | 10,000 |

P(disease | positive) = 99 / 594 = **1/6 ≈ 16.7%**. Five of every six positives are false alarms.

The population is 10,000, not 1,000, because these rates give whole people only at 10,000. At 1,000 people the sick-and-positive count would be 9.9.

The test's overall accuracy, (99 + 9,405) / 10,000, is **95.04%**. "99%" describes only its sensitivity. That is why the film says "a test that catches 99% of cases" rather than "a 99%-accurate test".

## 3. Bayes' theorem, built from the counts

Divide every count in the table by the 10,000 total, and the counts become probabilities:

- 99 / 10,000 = P(positive | disease) · P(disease) = 0.99 × 0.01
- 594 / 10,000 = P(positive) = 0.99 × 0.01 + 0.05 × 0.99 (law of total probability)

So 99 / 594 is

  P(D | +) = P(+ | D) · P(D) / P(+),

which is Bayes' theorem, P(A | B) = P(B | A) P(A) / P(B), with A = disease and B = positive [1][2]. The theorem is named after Thomas Bayes. His essay was published after his death by Richard Price in 1763 [1]. Laplace stated the rule in its general form independently [2].

## 4. Why the counts help

Gigerenzer and Hoffrage (1995) found that people who had no training solve this kind of problem far more often when it is stated as **natural frequencies** ("99 of 100 sick people test positive") than as probabilities ("sensitivity 0.99") [5]. In their report, up to 50% of inferences followed a Bayesian algorithm in frequency formats, against far fewer in probability formats. This film's grid representation follows that finding.

## 5. How often the misreading happens

Casscells, Schoenberger and Graboys (1978) asked 60 people at four Harvard Medical School teaching hospitals (20 house officers, 20 fourth-year students and 20 attending physicians) a version of this question: prevalence 1/1,000, false-positive rate 5%. Only 11 of the 60 (18%) gave the correct answer, about 2%. The most common answer, given by 27 of the 60, was 95% [6]. Manrai et al. (2014) repeated the question and found 14 of 61 correct (23%). Again the most common answer was 95%, given by 27 [7].

## 6. The base rate moves the answer

The same test (99% / 95%) gives different values of P(D | +) depending on the base rate (exact fractions, `demo/evidence.json`):

| Base rate | P(D \| +) |
|---:|---:|
| 0.1% | 11/566 ≈ 1.9% |
| 1% | 1/6 ≈ 16.7% |
| 10% | 11/16 = 68.75% |
| 50% | 99/104 ≈ 95.2% |

## 7. A second positive (the transfer exercise, not taught in the film)

Suppose the two test runs have independent errors. That is an assumption, and repeated tests on one person often violate it [4]. Under it, a second positive multiplies the odds by the same likelihood ratio, 0.99 / 0.05 = 19.8:

- After one positive the odds are 1 : 5 (P = 1/6).
- After a second positive the odds are 19.8 : 5, so P = 99/124 ≈ 79.8%.

In counts for 1,000,000 people: 9,801 sick and 2,475 healthy people test positive twice.

## References
1. T. Bayes and R. Price, "An Essay towards Solving a Problem in the Doctrine of Chances", *Philosophical Transactions of the Royal Society of London* 53 (1763), 370–418.
2. P.-S. Laplace, "Mémoire sur la probabilité des causes par les événements" (1774). See also S. M. Stigler, *The History of Statistics* (Harvard, 1986), ch. 3.
3. D. G. Altman and J. M. Bland, "Diagnostic tests 2: predictive values", *BMJ* 309 (1994), 102.
4. D. L. Sackett, R. B. Haynes, G. H. Guyatt and P. Tugwell, *Clinical Epidemiology: A Basic Science for Clinical Medicine*, 2nd ed. (Little, Brown, 1991), ch. 4.
5. G. Gigerenzer and U. Hoffrage, "How to improve Bayesian reasoning without instruction: Frequency formats", *Psychological Review* 102(4) (1995), 684–704.
6. W. Casscells, A. Schoenberger and T. B. Graboys, "Interpretation by physicians of clinical laboratory results", *New England Journal of Medicine* 299(18) (1978), 999–1001. doi:10.1056/NEJM197811022991808.
7. A. K. Manrai, G. Bhatia, J. Strymish, I. S. Kohane and S. H. Jain, "Medicine's uncomfortable relationship with math: calculating positive predictive value", *JAMA Internal Medicine* 174(6) (2014), 991–993. PMC4955674.
