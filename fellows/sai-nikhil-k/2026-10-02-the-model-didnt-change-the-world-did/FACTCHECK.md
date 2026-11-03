# FACTCHECK — The Model Didn't Change. The World Did.

Figure by figure: claim → where → how verified → result. All numbers are from
`evidence/drift_run.out` / `drift_run.csv` (run 2026-10-02) and are re-asserted
by `build_beats.py --check` before the sheet is written.

## Environment

Python 3.11.5 · numpy 1.24.4 · pandas 2.2.3 · SciPy 1.11.1 · scikit-learn 1.8.0 ·
Apple M2 Pro (arm64). Deterministic: `random_state=0`, no sampling.

## Data (B02, B06)

| Claim | Verified |
|---|---|
| ELEC2, Australia's (NSW) electricity market, 1996 to 1998, every half hour, price UP or DOWN | OpenML 151 description: 45,312 instances, 7 May 1996 – 5 Dec 1998, 30-minute periods, class = NSW price relative to its 24-hour moving average |
| the file is OpenML's | md5 `8ca97867d960ae029ae3a9ac2c923d34` asserted in `drift_run.py` |

## The decay (B00, B02, B06)

| Spoken / on screen | Measured |
|---|---|
| "the next four weeks, eighty-four percent" · 0.838 | weeks 1–4 after: 0.8381 |
| "then sixty-three" · 0.629 | weeks 5–8: 0.6287 |
| "by week forty-eight, fifty-five" · 0.548 | weeks 45–48: 0.5484 (the minimum of 20 blocks) |
| "always guessing down scores fifty-four" · 0.544 | majority class in weeks 45–48: 0.5443 (DOWN) |
| "eleven months later … barely better than always guessing" | weeks 45–48 ≈ 10.5–11 months after training; 0.548 vs 0.544 |
| 12 consecutive blocks below 0.75 | weeks 5–8 … 49–52 (`drift_run.out` summary) |

## The names (B03) — algebra

| Row | Expression | Check |
|---|---|---|
| 1 | P_live(X) ≠ P_train(X) | Huyen (2022), verbatim: "Covariate shift is when P(X) changes, but P(Y\|X) remains the same." |
| 2 | P_live(Y∣X) ≠ P_train(Y∣X) | Huyen (2022), verbatim: "Concept drift is when P(Y\|X) changes, but P(X) remains the same." |
| 3 | D = sup_s ∣F_train(s) − F_live(s)∣ | the two-sample KS statistic; `drift_run.py` asserts `scipy.stats.ks_2samp(...).statistic` equals a by-hand sup over the pooled sample points, to 1e-12, on every block |

"Here D rose from 0.14 to 0.81 and fell to 0.08" — KS on the frozen model's scores
P(UP): first block 0.142, max 0.809 (weeks 49–52), min 0.084 (weeks 61–64).
D ∈ [0, 1] asserted. KS is one-dimensional (Huyen notes the limit); it is applied
to one dimension, the model's score.

"The prices it saw after the freeze were not the prices it learned on" — KS on
`nswprice`, training year vs block: 0.220 in the first block, up to 0.923.

### Rendered-frame review (MATH-TYPESETTING.md)

**16:9 (`media/B03.mp4`, 3840×2160)** — reviewed at each reveal (1.70 s, 6.84 s,
10.27 s) and at 15/50/95%:
- Rows 1–2: subscripts "live"/"train" upright, ≠ correct, the conditional bar in
  P(Y∣X) full height; no tofu; rows span ~5–95% of the width, inside title-safe.
- Row 3: first pass wrote `\sup_{s}`, which mathtext sets with the s *under*
  "sup" — it sat on the note's first line. Rewritten as `\mathrm{sup}_{s}` (same
  meaning, inline subscript) and re-rendered; |·| bars full height.

**9:16 (`vertical/media/B03.mp4`, 2160×3840, `TypesetMath916`)** — reviewed at
15/50/95% and in the clean vertical's GATE V sheet: same glyphs as 16:9, inline
sup_s, nothing clipped. Ink height of rows 214 / 169 / 151 px = 5.6 / 4.4 / 3.9%
of frame height (floor 2%).

`ExecutedData916` (B02 portrait): row text 60 px of ink without descenders, the
same component and type size as the signed-off 2026-09-25 and 2026-10-02 (Gavia)
verticals (75 px there, with descenders). Logged, not changed.

## The alarm (B04, B06)

| Claim | Measured |
|---|---|
| "the answer arrives in thirty minutes" | ELEC2's label is the next half-hour's UP/DOWN; persistence = predict the previous row's label |
| "copying the last one averages eighty-six percent" | mean persistence over 20 blocks 0.859 (median 0.862); range 0.816–0.905 → on screen "0.82–0.90" |
| "ahead of both models in nineteen blocks of twenty" | persistence > max(frozen, retrained) in 19 of 20 (frozen wins weeks 69–72, 0.849 vs 0.827) |
| "that gap rose as the accuracy fell, and fell as it came back" · r = −0.85 | Pearson r(KS on scores, frozen accuracy) over 20 blocks = −0.853, p = 1.7e-06 |
| "without a single label" | the KS uses the model's scores on training rows and on block rows only |

## The fix? (B05, B06)

| Claim | Measured |
|---|---|
| "refit every four weeks on the year before" | `retrained`: same recipe refit on the 52 weeks before each block |
| "never fell below sixty-two percent" · worst 0.623 | min retrained 0.6227 (weeks 61–64) |
| "against fifty-five frozen" · worst 0.548 | min frozen 0.5484 |
| "a year after the freeze, prices came back … the frozen model came back with them, to eighty-five" | KS on price 0.141 at weeks 61–64; frozen accuracy 0.849 at weeks 69–72 (its maximum) |
| "lost seven blocks of twenty" · beat frozen in 12 | retrained > frozen in 12, frozen > retrained in 7, one tie (weeks 1–4, same model) |

## Claims deliberately softened or left out

- No claim that the KS alarm leads the decay; it moves in the same blocks.
- No cause is asserted for the price change (market events are not in the data).
- Huyen's cited "60 of 96 failures" is not used.
