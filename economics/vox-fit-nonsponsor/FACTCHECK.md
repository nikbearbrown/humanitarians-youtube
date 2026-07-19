# FACTCHECK — vox-fit-nonsponsor
**Why Fit Can't Save a Non-Sponsor: The Bayesian Role Scorer**
Source chapter: `the-reallocation-engine/chapters/11-the-bayesian-role-scorer.md`

---

## Claims table

| Beat | Claim | Verdict | Source / Note |
|---|---|---|---|
| B01 | Near-perfect fit, live posting, fine timeline → engine says Skip | ILLUSTRATIVE | Card hook — illustrative scenario, not a real application |
| B02 | BrandCo composite 0.61 in an opaque scorer | ILLUSTRATIVE | From card exercise 5 (chapter 11). The 0.61 is an invented example used in the pedagogy audit exercise; labeled illustrative. |
| B03 | "Fit = 0.85" stated as the question card | ILLUSTRATIVE | Illustrative fit value from card content |
| B04 | Sponsorship and fit are weighted votes; liveness and timeline are multipliers (gates) | VERIFIED | Chapter 11: "Fit and sponsorship are votes. They contribute proportionally … Liveness and timeline are different in kind. They are gates." |
| B04 | Sponsorship weight 0.35, fit weight 0.30 | VERIFIED | Chapter 11: "sponsorship at 0.35 weight — contributes almost nothing … sponsorship 0.35, fit 0.30" and footnote [^weights]: "Composite form and weights (sponsorship ×0.35, fit ×0.30 …) from the system design document" — marked **[verify]** in chapter. Weights match chapter text exactly. |
| B04 | Decision threshold near 0.3 → Apply/Consider/Skip | VERIFIED | Chapter 11 footnote [^weights]: "decision threshold ≈0.3 that maps the composite to one of three recommendations: Apply, Consider, or Skip." |
| B05 | Sponsorship weighted highest because it causes invisible rejections, not because competence matters less | VERIFIED | Chapter 11: "The weighting is not a claim that sponsorship matters more than competence in the world. It is a claim that, for you, it is the factor most likely to cause an invisible rejection." |
| B06 | Cambridge biotech: sponsorship 0.9, fit 0.70, liveness ~1, timeline ~0.85 | VERIFIED | Chapter 11 worked case: "P(sponsorship) ≈ 0.9 … P(fit | CV, JD) ≈ 0.7 … Liveness ≈ 1 … Timeline factor ≈ 0.85." |
| B06 | Composite = sponsorship 0.9×0.35 + fit 0.70×0.30 = 0.315 + 0.21 → above threshold → Apply | VERIFIED (arithmetic) | 0.9×0.35 = 0.315; 0.70×0.30 = 0.21; sum = 0.525 before multipliers; liveness ~1 × timeline ~0.85 ≈ 0.446 → above 0.3 threshold. Chapter confirms: "Recommendation is Apply." |
| B07 | BrandCo: sponsorship 0.05 (same candidate, same fit 0.70) | ILLUSTRATIVE | Card text: "P(sponsorship) ~0.05" for BrandCo. Illustrative value consistent with card content. |
| B07 | Sponsorship term contributes 0.018 (0.05×0.35) instead of 0.315 | ILLUSTRATIVE (arithmetic) | 0.05×0.35 = 0.0175 ≈ 0.018. Arithmetic is correct. Illustrative because BrandCo P(sponsorship)=0.05 is illustrative. |
| B07 | Composite below threshold → Skip | ILLUSTRATIVE | 0.018 + 0.21 = 0.228 × (liveness × timeline) ≈ 0.194 → below 0.3. Arithmetic supports claim. Scenario is illustrative. |
| B08 | Fit was identical in both; only sponsorship changed | VERIFIED | Chapter 11: "The same graduate. The same fit of 0.7. The same liveness and timeline." |
| B09 | Fit is a vote; sponsorship's near-zero collapses weighted sum regardless of fit | VERIFIED | Chapter 11: "Fit is a vote; sponsorship's near-zero value collapses the weighted sum regardless of how high fit goes." |
| B10 | Illustrative example: biotech 0.315 contribution vs BrandCo 0.018 | ILLUSTRATIVE | Labeled illustrative. From card example seed. Arithmetic verified above. |
| B11 | Recap: "Fit is a vote. Sponsorship decides." | Derived | Summary of mechanism taught — not a quoted claim, pedagogically accurate. |

## Illustrative numbers

All numbers in B02, B07, B10 are **illustrative** — invented for pedagogical clarity, consistent with the chapter's worked examples and the card's example seed. The weights (0.35, 0.30) and threshold (0.3) are stated in the chapter and footnoted for pre-publication verification.

## Terms table (pedagogy audit input)

| Term | Beat it debuts | Beat that creates the need |
|---|---|---|
| Fit score | B01 (implicit), defined B04 | B01 — the cold-open mystery needs a name for fit |
| Weighted vote | B04 | B04 — the structure beat creates the need |
| Gate (multiplier) | B04 | B04 — contrast with vote introduced same beat |
| Sponsorship weight 0.35 | B04–B05 | B04 establishes structure; B05 explains why |
| Composite | B04 | B04 — output of the voting/gating structure |
| Threshold | B04 | B04 — needed to define Apply/Consider/Skip |
| Apply / Consider / Skip | B04 | B04 — the three-way output named with threshold |
| Invisible rejection | B05 | B05 — explains WHY sponsorship is dominant |
| Dominant term | B07–B08 | B06 shows the large term; B07 shows its collapse |

## Exclusion confirmations

- Eightfold AI lawsuit: **not mentioned anywhere** in narration, cards, or graphics.
- How the fit score is computed: referenced only as "CV compared to job description" (one clause), no algorithmic detail.
- Override mechanism: **not mentioned anywhere**.
- No Bayes formula on screen (the word "Bayesian" is in the title only, not an equation on screen).
