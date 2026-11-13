# SOURCES — The Model Didn't Change. The World Did.

Reel `weekly_updates/2026-10-02-the-model-didnt-change-the-world-did/` · slug
`claude-sai-the-model-didnt-change-the-world-did` · week of 2026-10-02, second reel.

## Raw-material provenance

Sai chose the topic (MLOps — "a generic topic, not my project") and the
reference: **Chip Huyen, "MLOps guide"** (https://huyenchip.com/mlops/, updated
2025). From three proposed angles he picked data distribution shift and
monitoring, with the evidence run on real public data. The guide is a reading
list; its linked essay **"Data Distribution Shifts and Monitoring"** (Huyen,
2022) supplies the definitions. Every sentence attributed to Huyen was found
verbatim on the live page (`evidence/sources_check.out`). Every number on screen
comes from `evidence/drift_run.out`, a run made for this video.

## External sources

| Source | Used for |
|---|---|
| Chip Huyen, MLOps guide — https://huyenchip.com/mlops/ | B01: "Ops in MLOps comes from DevOps … To operationalize something means to bring it into production, which includes deploying, monitoring, and maintaining it." |
| Chip Huyen, "Data Distribution Shifts and Monitoring" (2022) — https://huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html | B03: covariate shift and concept drift definitions; the KS test as "a basic two-sample test". B04 framing: labels that arrive late (her "natural labels and feedback loop"). |
| ELEC2 — M. Harries (1999), normalised by A. Bifet; OpenML dataset 151 "electricity" — https://www.openml.org/d/151 | B00, B02, B04–B06: all figures. File `data/electricity.arff`, md5 `8ca97867d960ae029ae3a9ac2c923d34` = OpenML's checksum. |
| scikit-learn 1.8.0 `HistGradientBoostingClassifier`; SciPy 1.11.1 `ks_2samp`, `pearsonr` | The model and the statistics (`evidence/drift_run.py`). |

## Honesty log

| Issue | What was measured | What the reel does |
|---|---|---|
| Victoria columns missing in the training year | `vicprice`, `vicdemand`, `transfer` are one constant until row 17,424 (week 51.9); the 52-week training window includes one day (48 rows) of real values | The model uses the four NSW columns only. The all-seven variant (which *did* learn from that one day: scores moved up to 0.48 when reset) is reported in `drift_run.out` with the same pattern. |
| `date` column not monotone | decreases at rows 25487, 34895, 35231, 36239, 40703 | Not used; time = row order. Narration says "weeks after training", never a calendar date. |
| Day count | 45,312 rows / 48 = 944 days vs the description's 7 May 1996 – 5 Dec 1998 | Calendar span spoken only as "1996 to 1998". |
| "Better than either model" (first draft) | persistence > both models in 19 of 20 blocks, not 20 (the frozen model wins weeks 69–72, 0.849 vs 0.827) | Narration says "ahead of both models in nineteen blocks of twenty". |
| Persistence range (first draft "0.82–0.91") | 0.816–0.905 | On screen "0.82–0.90". |
| "No better than always guessing" (first draft) | 0.548 vs 0.544 | "barely better than" (B00), "level with" (B05, B06). |
| Huyen's cited Google study, 60 of 96 failures not ML | Not re-checked at its source | Not used. |
