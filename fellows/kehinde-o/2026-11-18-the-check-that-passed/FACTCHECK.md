# FACTCHECK — The Check That Passed

Source of record: `github.com/Kenny0bi/pulse-recsys` at commit `a776c94`. Every figure
computed in this session; results in `evidence.json`.

How: MovieLens 25M fetched with the repo's `data/get_data.sh` (structural validation:
25,000,096 lines). Prepared with the repo's `pulse/data.py`; output matches the repo's
`data/prepare.log` exactly (11,177,829 train, 169,923 test, 148,745 users, 17,102 items,
same cutoff). `evidence_run.py` mirrors `benchmarks/train_all.py` (6 epochs, batch 4,096,
dim 64, batch seed 1, model seed 0, same dedupe, same evaluation) for the popularity
counter and the two-tower with `item_freq=None` (no logQ) and `item_freq=popularity`
(logQ). It writes here, not into the repo's tracked `assets/`. Gradient check:
`tests/test_models.py::test_twotower_gradcheck`, run unmodified.

| # | Claim | Beat | Verdict | Measured |
|---|---|---|---|---|
| 1 | 25 million real ratings | B01 | TRUE | 25,000,095 ratings |
| 2 | The gradient check passed | B01, B03 | TRUE | max error 1.27e-06 (threshold 1e-5) |
| 3 | 6,198 test users, films after the cutoff | B02 | TRUE | eval_users 6,198; temporal split |
| 4 | Popularity counter: 5.8% | B02, B06 | TRUE | recall@10 0.0585 |
| 5 | My model: 3.1% | B02, B06 | TRUE | recall@10 0.0313 |
| 6 | 1.2% of top-ten slots on the 100 most popular films | B04, B06 | TRUE | 0.0121, first 2,000 eval users |
| 7 | The fix is from a 2019 Google paper | B05 | TRUE | Yi et al. 2019 (RecSys) |
| 8 | Subtracted in training only; plain score at recommendation | B05 | TRUE | `train_step` vs `item_vectors`/`user_vectors` |
| 9 | With logQ: 8.6% | B06 | TRUE | recall@10 0.0858 |
| 10 | 47% above the popularity counter | B06 | TRUE | 0.0858 / 0.0585 = 1.47 |
| 11 | A quarter of top-ten slots on the 100 most popular | B06 | TRUE | 0.255 |

## Algebra check
On screen: p(i | u) = exp(s(u,i) - log q_i) / sum over j in B of exp(s(u,j) - log q_j).
Code: `logits = (u @ v.T) / temp; logits = logits - self.logq[items][None, :]`, then softmax
across the batch with the positive on the diagonal. s is cosine similarity over temperature;
q = item frequency / total.

## A discrepancy in the source repository
The README reports the two-tower without logQ at recall@10 0.018, "three times worse than a
popularity counter". The current code with only `item_freq=None` gives 0.0313. The fixed
model (0.0858) and the counter (0.0585) match the README. The README's failing run likely
differed in more than logQ. Reported to the author; the video uses the measured figure.

## Deliberately not claimed
- Not "three times worse"; measured, about half the counter's recall.

## First-person claims added in the script revision (18 Nov 2026)

The narration was rewritten to describe what I did. Each new claim about my own work traces to the record:

| Claim | Source |
|---|---|
| The fix comes from a 2019 Google paper | Yi et al. 2019, RecSys |
