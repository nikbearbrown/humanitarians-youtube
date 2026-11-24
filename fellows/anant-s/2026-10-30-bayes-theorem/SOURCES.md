# SOURCES — Bayes' Theorem: The Positive That's Usually Wrong

There is no single source chapter. `SOURCE.md` in this folder was written for the film, fact-checked, and read in full on 2026-11-22. It is the material that `tldr-sections-bayes.md` sections. Under the BOOKLOOP law, none of the sources below are named on screen or in narration.

## References
1. T. Bayes and R. Price, "An Essay towards Solving a Problem in the Doctrine of Chances", *Phil. Trans. R. Soc. Lond.* 53 (1763), 370–418.
2. P.-S. Laplace, "Mémoire sur la probabilité des causes par les événements" (1774). See also S. M. Stigler, *The History of Statistics* (Harvard UP, 1986), ch. 3.
3. D. G. Altman and J. M. Bland, "Diagnostic tests 2: predictive values", *BMJ* 309 (1994), 102. Definitions of PPV, sensitivity and specificity.
4. D. L. Sackett, R. B. Haynes, G. H. Guyatt and P. Tugwell, *Clinical Epidemiology*, 2nd ed. (Little, Brown, 1991), ch. 4. Covers predictive value and the effect of prevalence.
5. G. Gigerenzer and U. Hoffrage, "How to improve Bayesian reasoning without instruction: Frequency formats", *Psychological Review* 102(4) (1995), 684–704. This is the basis for the representation choice (natural frequencies).
6. W. Casscells, A. Schoenberger and T. B. Graboys, "Interpretation by physicians of clinical laboratory results", *NEJM* 299(18) (1978), 999–1001, doi:10.1056/NEJM197811022991808. Cited for B01.
7. A. K. Manrai et al., "Medicine's uncomfortable relationship with math: calculating positive predictive value", *JAMA Internal Medicine* 174(6) (2014), 991–993, PMC4955674. Replication; source of the Casscells result figures (11/60 correct, modal answer 95%).

**Verification note:** the Casscells result figures were confirmed through the Manrai 2014 replication's summary of the original. The NEJM full text was not opened (paywalled). The design figures (60 participants, Harvard teaching hospitals) appear in the NEJM abstract metadata.

## Executable evidence
- **Script:** `demo/bayes_demo.py`, standard library only. It uses `fractions.Fraction` for exact counts and `random.Random(20261122)` for the 100,000-person simulation.
- **Outputs:** the script writes `demo/evidence.json` and `demo/RUN-LOG.txt`.
- **Run environment:** Python 3.12.13 (toolkit `.venv`), Windows 11.
- **Hashes:** script sha256 `9d72b9a1e8cd160ae0b981b3e2f94dcf507bba0e5713603685fdcafe8bce1d77`; evidence sha256 `6bcda52ea4fdcdaf330d629a4b4ebf4359ea6638428954744225aaf72071eb61`.
- **Sheet:** `make_sheet.py` reads every on-screen number from `evidence.json` and asserts every spoken number against it.

## Corrections applied (DOUBLE-CHECK law)
These are listed in FACTCHECK #1–#5:
- "99%-accurate" became "catches 99% of cases". The overall accuracy is 95.04%.
- The title moved from "test … usually wrong" to "positive … usually wrong".
- The population went from 1,000 to 10,000, so every count is a whole person.
- B01 changed "this exact puzzle" to "this kind of puzzle", because Casscells used 1/1,000 and 5%.

## Seeds
- **Hesitant writer:** `tldr-bayes-theorem`.
- **Simulation:** `random.Random(20261122)`.
- **False-positive positions in the grid:** to be seeded in `scenes.py`. Proposed: `random.Random("tldr-bayes-theorem-fp")`, sampling 495 of the 9,900 healthy cells.
- **Outro mascot and polarity:** seeded by the slug `tldr-bayes-theorem`.
