# FACTCHECK — vox-heavy-tail-yank

Source chapter: `books/computational-skepticism-for-ai/chapters/02-probability-uncertainty-and-the-confidence-illusion.md`  
Section: "When the Central Limit Theorem politely declines to help" (p. 444–469 in the chapter file)

---

## Claims audit

| Beat | Claim | Verdict | Source line / fix |
|---|---|---|---|
| B01 | Title: "One data point can beat a thousand-point average" | ✓ | Chapter p.463: "You compute the average of a thousand observations and the next observation moves the average by a lot." Stated in the chapter verbatim. |
| B02 | "After three hundred cases, the running average looks stable" | ✓ illustrative | The "looks stable" framing is the exact chapter point — the appearance of stability is the trap. Number (300) is illustrative, not cited. |
| B03 | "The average lurches — more than all three hundred combined" | ✓ mechanism | Valid for heavy-tailed distributions where one observation contributes more than N × mean_so_far. Illustrative framing, not a specific empirical number. |
| B04 | Question card phrasing | ✓ | Exact restatement of the chapter's question (p.463). |
| B05 | "The Central Limit Theorem promises: enough observations, and the mean settles" | ✓ | Chapter p.452: "a beautiful theorem ... the reason averages are useful." Named without full statement — exclusion honored. |
| B06 | "The theorem has a condition buried in it. Extreme events must be rare enough that each new one matters a little less than the last." | ✓ | Chapter p.452: "The theorem has two requirements buried in it ... finite variance." Paraphrased without the formal statement — exclusion honored. |
| B07 | Quote: "The next observation can move your average dramatically, no matter how many you have already collected." | ✓ | Chapter p.463: "the sample mean does not settle down as you collect more data. You compute the average of a thousand observations and the next observation moves the average by a lot." Quote is a close paraphrase made citable. |
| B08 | "Watch a running average from a well-behaved distribution ... The trace settles." | ✓ | Chapter p.452: "This is a beautiful theorem and it is the reason averages are useful." CLT behavior for Gaussian described accurately. |
| B09 | "From a heavy-tailed distribution, it doesn't settle ... The mean lurches." | ✓ | Chapter p.463: "In a heavy-tailed regime, the sample mean does not settle down as you collect more data." Exact chapter claim. |
| B10 | "Same observation count. Different distribution. On the left, the mean converges. On the right, the thousandth observation still moves it as much as the first." | ✓ mechanism | Chapter p.463: "the next observation moves the average by a lot" regardless of n. |
| B11 | "In a Gaussian, extreme values grow increasingly improbable. In a heavy-tailed world, they keep arriving — large enough to matter, every time." | ✓ | Chapter p.452: "finite variance breaks down in heavy-tailed distributions — distributions where extreme events are not rare enough for averaging to dampen them." |
| B12 | "average error cost ... does not converge" when loss distribution is heavy-tailed | ✓ | Chapter p.465: "a deployment evaluated on average loss is being evaluated on a quantity that does not converge in any useful sense." Direct chapter claim. |
| B13 | "Ninety-nine errors at thirty dollars. One error at three million." | ✓ illustrative | Illustrative number. Chapter (p.465) describes the structure: "most wrong outputs are minor inconveniences but one in a thousand kills a patient or wipes a database." Numbers are chosen to make the arithmetic transparent, labeled as illustrative. |
| B14 | "You need tail-aware metrics. Worst-case analysis." | ✓ | Chapter p.465: "You need tail-aware metrics. You need worst-case analysis." Near-verbatim from chapter. |
| B15 | EXAMPLE (illustrative): 10 documents / avg 0.3s + 1 outlier at 300s → new avg 27s (90×) | illustrative | Made-up scenario demonstrating the yank mechanism. Math: (10×0.3 + 300)/11 = 27.5s ✓. All details invented, no specific company or system claimed. |
| B16 | Endcard: "Averages converge when extremes are bounded. When they're not, the next observation can beat a thousand." | ✓ | Accurate summary of the chapter section's core claim. No book title or chapter number on screen. |

---

## Exclusion check

| Exclusion | Status | Confirmation |
|---|---|---|
| No proof that the Cauchy mean is undefined | ✓ CLEAR | Cauchy distribution is never named. Mechanism is "heavy-tailed" generically. No proof of undefined mean. |
| No CLT statement in full | ✓ CLEAR | CLT is named in B05 narration but only its conclusion ("mean settles") is stated. No formal statement, no independence/finite-variance axiom quoted formally. |
| No confidence-interval formulas | ✓ CLEAR | CI appears nowhere in narration, visuals, or card copy. |
| No power-law taxonomy | ✓ CLEAR | "Power-law" is not named. "Wealth/earthquakes list" does not appear. The single example is AI error-cost distribution. |

---

## Terms table

| Term | Debut beat | Earlier beat that created the need |
|---|---|---|
| running average | B02 | B01 (cold open hook — the viewer watches a trace being built and NEEDS a name for the quantity being plotted) |
| Central Limit Theorem (CLT) | B05 | B04 (question beat — viewer just learned that the mean can be beaten; now asks WHY anyone trusted it — the CLT is the answer to "why do people trust averages?") |
| finite variance (condition) | B06 | B05 (CLT beat — viewer just heard "the mean settles" and now needs to know WHEN it does; the condition is the answer) |
| heavy-tailed distribution | B06 | B05/B06 (the contrast: CLT requires finite variance → what breaks it? → heavy tails) |
| convergence (of the mean) | B08 | B07 (quote beat — viewer just heard "no matter how many"; now sees a concrete trace and NEEDS a word for "it stopped moving") |
| tail-aware metrics | B14 | B12/B13 (implication beats — viewer just saw that average metrics fail; now needs a word for the alternative) |

All terms debut AFTER the beat that made the viewer want a name for them. ✓
