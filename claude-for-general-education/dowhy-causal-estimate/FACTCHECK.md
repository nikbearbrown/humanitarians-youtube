# FACTCHECK — dowhy-causal-estimate

- DoWhy library: open-source Microsoft Research causal inference library (correct).
- Synthetic DGP: Z→T, Z→Y, T→Y with true T→Y=0.5 — standard confounding simulation.
- Naive estimate > true effect when Z positively affects both T and Y: correct (positive confounding).
- Partial adjustment (one of two confounders) leaves residual bias: correct — remaining confounder still induces bias.
- All values synthetic; no real study data.
