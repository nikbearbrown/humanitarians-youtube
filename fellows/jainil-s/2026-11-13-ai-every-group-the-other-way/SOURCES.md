# SOURCES — Every Group Went The Other Way

Week ending 2026-11-13 · `ai-` track.

## Primary source — published, external

**Bickel, P. J., Hammel, E. A., & O'Connell, J. W. (1975). "Sex Bias in
Graduate Admissions: Data from Berkeley." *Science* 187(4175), 398–404.**

The six largest departments of the UC Berkeley 1973 graduate admissions round.
The same table is distributed with R as the `UCBAdmissions` dataset, which is
how it is most often checked.

This is the first reel in this series whose evidence is an outside
publication rather than a simulation written for the episode. The counts are
**transcribed from the published table; every rate is computed from those
counts** in `simpson_evidence.py`, so no percentage on screen can drift from
the number it came from.

**No sentence of the paper is quoted on screen.** Its conclusion is
paraphrased and attributed in B06. I could not retrieve the full text to
verify exact wording, and an approximate quotation is worse than an honest
paraphrase — see `FACTCHECK.md`.

## Supporting evidence — generated here

`simpson_evidence.py` also runs a seeded synthetic check answering what the
Berkeley table cannot: whether a reversal requires a confounder at all. Two
groups, two strata, group B genuinely better in **both** strata, varying only
how unevenly B is routed to the hard stratum.

Seed `20261113`, `numpy` only.

```bash
python simpson_evidence.py
```

Its figures are **not** shown in the reel — a synthetic number sitting beside
real data invites being read as part of it. The reel states only the
qualitative fact the simulation establishes: a reversal needs a confounder
correlated with both the grouping and the outcome.

## Method, stated plainly

- **Rates** are admits ÷ applicants, per department and per group.
- **Selectivity** is admits ÷ applicants for a department across both groups.
- **Application shares** are a group's applications to a department ÷ that
  group's total applications.
- **Standardisation** is direct standardisation: hold each department's
  group-specific rate fixed and reweight to the other group's application
  distribution. It answers "what if they had applied the same way", and
  nothing else.

## Not used

No screenshots, no lifted figures, no third-party charts — REBUILD LAW; every
graphic is a native Remotion scene driven by the arrays above. No claim about
litigation, and no modern re-analysis of the dataset.
