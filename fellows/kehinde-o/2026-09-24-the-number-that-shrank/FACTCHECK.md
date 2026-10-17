# FACTCHECK — The Number That Shrank

Source of record: `github.com/Kenny0bi/adverse-event-pipeline`, the committed outputs of
its 2024 run. Every figure below was **recomputed in this session** from those files, not
copied from the repo README (docs/EXECUTABLE-EVIDENCE.md).

Files read: `results/summary.json`, `results/positive_controls.csv`,
`results/signals_top1000.csv`.

| # | Claim on screen or spoken | Beat | Verdict | Where it comes from |
|---|---|---|---|---|
| 1 | 1,619,665 raw reports parsed | B02 | TRUE | README run table, four 2024 quarters |
| 2 | 1,214,808 deduplicated cases | B02 | TRUE | `summary.json` `cases` |
| 3 | 472,082 drug-event pairs scored | B02 | TRUE | `summary.json` `pairs_scored` |
| 4 | Pairs need at least three co-reports to be scored | B02 | TRUE | Pipeline detect stage, N >= 3 rule |
| 5 | Expected count = (drug total x event total) / grand total | B03 | TRUE | Standard 2x2 independence expectation |
| 6 | Warfarin with GI haemorrhage: 62 observed, 2.9 expected | B03, B04 | TRUE | `positive_controls.csv`: a=62, expected=2.925216 |
| 7 | After shrinkage 99 percent of the warfarin ratio survives | B04 | TRUE | EBGM 20.954 / crude 21.195 = 98.9 percent |
| 8 | Esculin with heart sounds: 16 observed, crude ratio 55,218 | B04 | TRUE | `signals_top1000.csv`: a=16, expected=0.000290 |
| 9 | After shrinkage 4 percent of the esculin ratio survives | B04 | TRUE | EBGM 2208.7 / crude 55218.5 = 4.0 percent |
| 10 | Six positive controls, all four methods, all found | B05 | TRUE | `positive_controls.csv`, `n_methods_signal` = 4 on all six rows |
| 11 | The run halts if a positive control fails to resurface | B05 | TRUE | Pipeline gate, detect stage |
| 12 | 77 of the top 100 signals shift by more than 1.5x after age/sex adjustment | B06 | TRUE | `summary.json` `confounded_in_top` = 77 |

## Arithmetic stated in the reel
- 1,214,808 / 1,619,665 = 0.750. AttritionChain survival 0.750. Checked.
- 472,082 / 1,214,808 = 0.389. AttritionChain survival 0.389. Checked.
- 62 / 2.925216 = 21.195 crude. EBGM 20.954. Ratio 0.989, shown as 99 percent. Checked.
- 16 / 0.000290 = 55,218.5 crude. EBGM 2,208.7. Ratio 0.040, shown as 4 percent. Checked.

## Math typesetting (docs/MATH-TYPESETTING.md)
B03 renders two structured SVG rows via `runtime/scripts/typeset_math.py`, not text:
- `E_{ij} = N_{i.} N_{.j} / N_{..}` with a real fraction bar and proper indices
- `RR = N_{ij} / E_{ij}` with a real fraction bar

Algebra check: free indices i (drug) and j (event) on both sides; no bound indices. The
expectation is the standard independence expectation for a 2x2 contingency table.
Numerical case, verified against the repo output: warfarin (i) with gastrointestinal
haemorrhage (j) gives expected 2.925216 and observed 62, so RR = 21.195.

## Deliberately not claimed
- No clinical advice, and no claim that any named drug causes any named effect.
  Disproportionality is not causality. The B03 conditions line states that reporting is
  voluntary and that N counts reports, not patients.
- Esculin appears only as an example of thin evidence. It is not a safety claim.
- No claim that this pipeline outperforms the regulators' own systems. It implements the
  same four published methods.
