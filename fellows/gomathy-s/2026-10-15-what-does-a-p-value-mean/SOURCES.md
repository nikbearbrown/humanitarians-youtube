# SOURCES.md — p-value

Primary source, checked 2026-10-15:

**Wasserstein, R. L., & Lazar, N. A. (2016). The ASA Statement on p-Values:
Context, Process, and Purpose. *The American Statistician*, 70(2), 129–133.**
https://doi.org/10.1080/00031305.2016.1154108
(metadata confirmed via Crossref; the publisher page refused automated access).

- Six principles: verbatim against the ASA's own release,
  https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf
- Informal definition: verbatim as quoted from the statement in J. Utts,
  "Understanding p-values" (slides), https://ics.uci.edu/~jutts/UnderstandingP-Values
  — "Informally, a p-value is the probability under a specified statistical
  model that a statistical summary of the data (e.g., the sample mean
  difference between two compared groups) would be equal to or more extreme
  than its observed value."

The six principles (verbatim):

1. P-values can indicate how incompatible the data are with a specified statistical model.
2. P-values do not measure the probability that the studied hypothesis is true, or the probability that the data were produced by random chance alone.
3. Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold.
4. Proper inference requires full reporting and transparency.
5. A p-value, or statistical significance, does not measure the size of an effect or the importance of a result.
6. By itself, a p-value does not provide a good measure of evidence regarding a model or hypothesis.

| Beat | Claim | Source |
|---|---|---|
| B00 | "A study says p is zero point zero three." | **ILLUSTRATIVE** — invented number, spoken only, never on screen. |
| B00 output / B01 / B09 | A p-value is how likely data this extreme would be if there were no real effect. | Informal definition above. **INFERENCE (plain-language paraphrase):** "if there's no real effect" stands in for "under a specified statistical model" — the model includes the null hypothesis *and* its other assumptions. B02 and B09 ("Assumes null and model") put the second half back on screen. |
| B02 | Assume no effect (the null hypothesis) and that the model holds. | Definition ("under a specified statistical model"); principle 1. Utts's slides list the model as the null hypothesis plus assumptions such as randomness and no missing data. |
| B03 | If the null is true, the share of outcomes at least this extreme is the p-value. | Definition ("equal to or more extreme than its observed value"). Curve and marker are **ILLUSTRATIVE** — a one-tailed sketch, no data. |
| B04 | Nine heads in ten fair flips: P(X ≥ 9) = 11/1024 ≈ 0.011. | **ILLUSTRATIVE**, computed in `scenes.py` (C(10,9)+C(10,10) = 11; 2¹⁰ = 1024). **This is a ONE-SIDED p-value** ("nine or more heads"). The two-sided p-value (9+ heads *or* 9+ tails) is 22/1024 ≈ 0.021, about 2%. |
| B05 | Not the chance you're right; not the size or importance of the effect. | Principles 2 and 5. "The chance you're right" is a plain paraphrase of "the probability that the studied hypothesis is true". |
| B06 | A huge study can give a tiny effect a tiny p; a small study can give a big effect a large p. | Consequence of principle 5. **ILLUSTRATIVE** numbers, computed (FACTCHECK.md). |
| B07 | p under 0.05 isn't proof; never decide on a threshold alone. | Principles 3 and 6. The ASA release also quotes Wasserstein on a "post p<0.05 era". |
| B08 | Report the effect size, its uncertainty (confidence interval), and every test you ran. | Principle 4 (full reporting and transparency). **INFERENCE:** the effect-size / confidence-interval row paraphrases the statement's note that statisticians supplement p-values with other approaches (the release lists confidence intervals among them); it is not one of the six principles. |
| B10 | Prompt for the viewer. | Not a factual claim. |

## Corrections applied (DOUBLE-CHECK LAW)

- First-draft wording "if nothing were going on" / "how surprising" replaced in
  script review with "if there's no real effect" / "how likely data this
  extreme" — closer to the definition.
- B04's 11/1024 is logged as one-sided (two-sided ≈ 2%), per review.
- No "statistically significant" anywhere on screen: the reel teaches the
  ASA's caution rather than the label.
