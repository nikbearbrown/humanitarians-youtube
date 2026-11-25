# PEDAGOGY.md — The Test That Couldn't Fail (GATE P)

**Reel:** `hai-the-test-that-couldnt-fail` · 26 beats · Bella (`af_bella`) · Humanitarians AI
**Source:** a CTGAN synthetic-data notebook (41 cells, executed, real outputs).
**Target:** ~6 minutes.

---

## 1. The argument

The notebook makes three claims — fidelity, utility, privacy — and reports success on all
three. Read literally, its own numbers do not support any of them. The reel walks each
claim to its actual result, then lands on the fair verdict: **CTGAN worked; the evaluation
is what failed.**

## 2. Every figure is recomputed, not quoted

`build_beat_sheet.py` re-runs the notebook's dataset code verbatim at its own seed (42)
and recomputes each number before writing the sheet. It carries three assertions that
**fail the build** if the reproduction ever stops matching the narration:

```python
assert CTRL_POS == 0 and CTRL_F1 == 0.0   # the control must stay degenerate
assert abs(BASE - 0.785) < 0.002          # narration quotes 0.785
assert MAXR < 0.015                       # narration says "under 0.014"
```

Verified at build time:

| Quantity | Value |
|---|---|
| base rate of "no diabetes" | **0.7847** (notebook's TSTR accuracy: 0.785) |
| max abs. correlation of any TSTR feature with the target | **0.0139** |
| control: train on real → test on real | acc **0.785**, F1 **0.000**, **0** positive predictions |
| `corr(BMI, BloodPressure)` | **−0.0034** |
| `corr(BMI, HealthRiskScore)` | **+0.3736** (real — via the Overweight threshold) |

The KS and chi-square values spoken in B08/B10/B12 are the notebook's **own printed
outputs**, quoted unchanged.

## 3. The four findings, and how each was established

**1 — The moving goalpost.** Cell 24 states the rule: *"High p-values (>0.05) suggest that
the synthetic and real data are statistically similar."* The printed result is
p = 0.0000 on six columns and 0.0003 on the seventh. Cell 26 then concludes success on a
different basis — *"All KS values are below 0.1"*. Same data, different criterion, chosen
after the fact. Both quotes are from the notebook.

**2 — A categorical test that cannot fail.** `chi2_contingency(pd.crosstab(real[col],
synthetic[col]))` tests row-wise association between two independently-generated columns,
which is absent by construction — not whether the marginals match. Demonstrated by
control: replacing the synthetic column with a *permutation of the real one* (identical
marginals by definition) still yields p = 0.5693 / 0.3430 / 0.5790. A test that passes on
matched and unmatched input alike is not evidence.

**3 — Accuracy that is the base rate.** TSTR accuracy 0.785 against a majority class of
0.7847, with F1 = 0.000, means the model predicted "no diabetes" for all 10,000 rows.
The notebook reads this as *"good analytical utility"*.

**4 — The missing control, and the root cause.** Training on **real** data scores
identically (0.785 / F1 0.000 / zero positives), so the synthetic data cannot be the
cause. The reason is upstream: the source columns are independent `np.random` draws, so
no feature correlates with the target above 0.0139. The notebook attributes the zero F1
to class imbalance and recommends resampling; resampling cannot create a relationship
that was never generated.

## 4. Where the reel is deliberately fair

- **B20 and the verdict state plainly that CTGAN is not at fault.** It reproduced the
  marginals it was given, which is what it was asked to do. The reel is a critique of an
  evaluation, not of the library or the technique.
- **B01 affirms the premise.** Synthetic data for privacy, scarcity and bias is presented
  as genuinely valuable, because it is.
- **B05 credits the derived columns.** Overweight, HighBP, HighCholesterol and
  HealthRiskScore *do* carry real structure. The reel says so rather than flattening the
  dataset to "all noise".

## 5. Known limitations of this critique

- **CTGAN was not retrained.** All findings concern the dataset and the evaluation, both
  of which are fully reproducible without a GPU. The KS/chi-square numbers are the
  notebook's own run and would shift slightly on a retrain; the *argument* does not depend
  on their exact values, only on the sign of the comparison.
- **`SynthParticleHist` is illustrative.** It renders ~460 particles with a synthetic
  spread chosen to match the reported KS magnitudes — it is not a plot of the notebook's
  actual samples.
- **`SynthCorrelationGrid` magnifies bars ~5,000×** so near-zero correlations are visible
  at all. The on-screen numerals are exact; the bar lengths are not to scale. The reel
  says this aloud in the spark line.
- **The privacy critique is methodological, not a demonstrated breach.** No membership
  inference attack was run. The claim is only that one minimum over 100M pairs, against an
  unsourced threshold and with no real-to-real baseline, does not establish privacy.

## 6. Attribution

No individual is named in narration or on screen. The build script runs a name guard over
the serialised sheet and reports CLEAN. The notebook carries a personal copyright line;
the reel discusses the work, not its author.

## 7. Verdict

```
VERDICT: PENDING — awaiting human sign-off.
```

Audio was generated with `--no-gate`, on the record. This reel makes critical claims about
a specific piece of work, so §3 and §5 deserve a careful read before it goes anywhere.
Replace this block with `VERDICT: PASS` and your date to sign it.
