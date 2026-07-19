# FACTCHECK — vox-fair-three-ways

Source of record: `books/computational-skepticism-for-ai/chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md` (the three definitions, "The arithmetic," and the impossibility theorem).
Every number verified by direct computation 2026-07-06 via Chouldechova's relation **v/(1−v) = p/(1−p) · t/f** (PPV v, base rate p, TPR t, FPR f). One chapter erratum found — see the end.

## The theorem and its provenance

| Beat | Claim | Verdict | Basis |
|---|---|---|---|
| B01/B06 | "a theorem — proved twice in the same year… two teams independently" | ✓ | Kleinberg, Mullainathan & Raghavan, "Inherent Trade-Offs in the Fair Determination of Risk Scores" (arXiv Sept 2016); Chouldechova, "Fair Prediction with Disparate Impact" (arXiv Oct 2016). Independent, both 2016 preprints. Chapter states the same. |
| B06 | "when the groups' base rates differ, no model can satisfy all three" | ✓ | The theorem's condition, exactly. Escape hatches (perfect prediction, equal base rates) are stated in B10. |
| B03–B05 | the three definitions in plain words (equal yes-rates / equal error rates / honest score) | ✓ | Faithful plain-language renderings of demographic parity, equalized odds, calibration parity. The formal names never appear on screen or in narration — prerequisite-friendly, and the exclusion on algebra is honored. |
| B10 | "the only exits are a perfect model or identical base rates" | ✓ | Chapter: "The only escape is p_a = p_b … or perfect prediction (TPR = 1, FPR = 0)." |
| B11 | "two audits… opposite verdicts, both did the math right… which fairness should win" | ✓, case withheld | This is the COMPAS/ProPublica-vs-Northpointe lesson stated generically — chapter: "They were having a values disagreement about which definition of fairness should win." The case itself is excluded by the card; the generic framing preserves the lesson without the litigation history. |

## The numbers — all recomputed

Base rates: p_A = 0.6, p_B = 0.3 (the chapter's worked example).

**Equalized-odds state (B08)** — chapter table CONSISTENT, used as printed:
- TPR .70/.70, FPR .15/.15 (thresholds .5/.6)
- PPV_A: 0.6/0.4 × 0.70/0.15 = 7.00 → v = 7/8 = **0.875 ≈ .88** ✓
- PPV_B: 0.3/0.7 × 0.70/0.15 = 2.00 → v = 2/3 = **0.667 ≈ .67** ✓

**Honest-score / calibration state (B07, B09)** — chapter table INCONSISTENT, corrected:
- Chapter prints Group B: TPR .50, FPR .10, PPV .83. The relation gives 0.3/0.7 × 0.50/0.10 = 2.143 → v = **0.68**, not .83. The printed row cannot exist.
- Film's corrected set: A: TPR .83, FPR .20 → v = 0.6/0.4 × 4.15 = 6.225 → **PPV .86** ✓. B: TPR .50, FPR **.04** → 0.3/0.7 × 12.5 = 5.357 → v = 5.357/6.357 = **0.84 ≈ .86**. (FPR .0346 gives exactly .861; .04 rounds the screen value honestly — PPV renders as .86/.86 with the B-side truly .84–.86 depending on rounding. If Bear wants exactitude, print PPV as ".86 / .85" or set FPR_B = .035.)
- **Recommendation at the gate:** either print FPR_B as ".035" (which makes PPV exactly .86/.86) or accept ".04" with the honestly-rounded PPV ".86/.84". The scene code uses .04 → PPV .86/.84 (computed .862/.843). If the near-equal-but-not-identical PPV bothers at review, switch FPR_B to .035 — one-line change in vox_scenes.py HONEST dict.

## Exclusions honored

No Chouldechova algebra on screen (the relation lives HERE, not in the film) · no COMPAS/ProPublica/Northpointe names · no individual or counterfactual fairness · no GE index · no debiasing toolkit · formal metric names (demographic parity, equalized odds, calibration) never spoken — plain words only.

## Rendering honesty checks

- Blue/terracotta are GROUP IDENTITY colors here, morally neutral — unlike other films in this series where terracotta means "bad." The beat sheet's color_semantics note flags this; do not let the palette imply one group is the problem.
- B03/B05 isotype rows are countable-true: 4-of-10 and 4-of-10; 7-of-10 and 7-of-10.
- B07's two distributions must differ ONLY in where the mass sits (A right, B left) — same curve family, same area; the base-rate difference is the only asymmetry.
- B08/B09: the SAME table transforms — numbers never teleport, they Transform, so the viewer sees which dial moves when the threshold does. The threshold line's position change (.5 → .6 → .5) must be visible.
- B10's triangle must show TWO different pick-two configurations — one configuration would read as "this pair is special"; the rotation is what makes it a theorem.
- No real institution, dataset, or defendant on any plate; B02's form is anonymous by design.

## Chapter errata (feed back to the book)

- **"The arithmetic" section, calibration-satisfying table (fig 7.2 area): Group B row is arithmetically impossible.** With p=0.3, TPR=.50, FPR=.10, the chapter's own Chouldechova relation gives PPV = 0.68, not the printed 0.83. Fix: either FPR_B → 0.035 (keeps PPV ≈ .86, matching the equal-PPV story) or PPV_B → 0.68 (keeps the printed error rates but then the table no longer demonstrates calibration parity). The first fix preserves the table's pedagogical point.
- The equalized-odds table checks out exactly (.875/.667).
