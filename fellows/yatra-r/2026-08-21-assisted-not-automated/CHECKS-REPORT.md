# CHECKS-REPORT — Assisted, Not Automated.

Written before the first compile, per the PROOF GATE.

```
24 SHOW / 0 justified-HOLD / 0 PUNT-flagged
Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Teaching arc

- **FRAMEWORK** ✓ — B01 sets the producing/deciding split before any figure is shown, and
  B05 supplies the reading instruction for the figures ("using AI" spans three very
  different behaviours). Both land before the first example.
- **WORKED EXAMPLE** ✓ — B12→B14 walks the framework through the Ahrefs figures: "some AI"
  vs "purely AI", then what that means at the top of search. The framework is visibly on
  screen while the example runs.
- **FALSIFIABILITY** ✓ — B19 is a full beat naming two observations that would overturn the
  conclusion: ranking systems penalising AI text directly, or the purely-automated share
  climbing out of the low single digits. Both tied to a cited figure.
- **SCAFFOLDED TASK** ✓ — B22 carries a real prompt plus a three-item rubric.
- **BOOKENDS** ✓ — B00 cold open · B21 verdict · B22 your turn · B23 title restate.
- **NO-SOURCE-NO-VERDICT** ✓ — and unusually literal here: every factual claim beat carries
  its citation on screen, and B20 is a dedicated sources card.

## Per-beat classification

All 24 classify SHOW. No bare CARDs — the four act cards are motion beats (rule wipe,
staggered title) rather than static text pages, so they clear the PPT TEST. No HOLDs: this
episode needs no archival photograph, which is also why it has no vox lane (see
`BUILD-LOG.md`).

## Legibility contract

- Every beat names its on-screen artifact in `shot.show`. ✓
- Comparisons held ≥2s — specified in the `show` blocks of B03, B07, B08, B12, B14, B18.
- Measured at QC: 22 of 24 rendered beats Gate V CLEAN, coverage 0.68–0.98, **zero
  edge-bleed** (max ink x=3647 against a safe edge of 3648).
- The two flags are `underfill` on B21 (verdict artifact, 0.50) and B23 (title outro, 0.06)
  — shipped fidelity components, accepted for the same reason as every previous reel in
  this series.

## Gate deviation

This episode does **not** meet the `deep-explainer` beat-mix contract: VOX 0% (required
20–25%) and MANIM 0% (required 25–40%), both blocked by the machine. Recorded in full in
`BUILD-LOG.md`, including what would unblock each lane. The label is not being defended.

## Constraint compliance — the seven supplied figures

Enforced three ways: **structurally** (every stat component requires a `source` string, and
values are strings rendered verbatim — never parsed or recomputed), **editorially** (a
dedicated sources card plus citations restated on the verdict card), and **by omission**
(no figure beyond the seven appears anywhere; everything else is ordinal or descriptive, per
instruction). Ledger in `FACTCHECK.md`.
