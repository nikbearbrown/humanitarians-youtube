# FACTCHECK — Where the Error Lives

Source of record: `github.com/Kenny0bi/hive-index` at commit `04d9e14`. Every figure
was **computed in this session** by running the repo's own `hive.ivfpq.IVFPQ`, not
taken from its README (docs/EXECUTABLE-EVIDENCE.md).

Reproduce: the first 100,000 vectors of SIFT1M base and the first 1,000 queries
(Hugging Face mirror named in `data/get_data.sh`), exact ground truth by brute
force, `IVFPQ(dim=128, nlist=256, m=8, seed=0)`, k = 10. Build took 695 s. For each
setting, recall@10 is measured, and separately **coverage**: the share of each
query's true 10 neighbours that lie inside the cells being searched.

| # | Claim | Beat | Verdict | Measured |
|---|---|---|---|---|
| 1 | Each vector is 128 numbers, 512 bytes | B02 | TRUE | 128 x float32 |
| 2 | Compressed to 8 bytes, 64 times smaller | B02 | TRUE | m = 8 one-byte codes; 512 / 8 = 64 |
| 3 | Vectors are sorted into 256 cells | B02 | TRUE | nlist = 256 |
| 4 | Each piece is the nearest of 256 learned patterns | B03 | TRUE | codebooks shape (8, 256, 16) |
| 5 | The search measures to the stand-in, not the vector | B03 | TRUE | see algebra check below |
| 6 | 1 cell: 30 percent of true neighbours | B04 | TRUE | recall 0.3026 |
| 7 | 4 cells: 42 percent | B04 | TRUE | 0.4244 (README: 0.4244) |
| 8 | 16 cells: 46 percent | B04 | TRUE | 0.4591 (README: 0.4591) |
| 9 | 128 cells: still 46 percent | B04 | TRUE | 0.4596 |
| 10 | Seven times slower at 128 cells than at 16 | B04 | TRUE | 285.5 / 38.8 = 7.4 queries/s ratio |
| 11 | From 16 to 128 cells recall moves 0.05 points | B04 | TRUE | 45.91 to 45.96 |
| 12 | At 128 cells every true neighbour is inside the search | B05 | TRUE | coverage 1.0000 |
| 13 | Re-checking only the top 10 changes nothing | B06 | TRUE | 0.4595 at rerank 10 = 0.4595 at rerank 0 |
| 14 | Top 100 re-check: 46 to 93 percent | B06 | TRUE | 0.9295 (README: 0.9295) |
| 15 | Top 50: 83.6 percent; top 200: 97.6 percent | B06 | TRUE | 0.8362; 0.9759 |
| 16 | Almost no cost in speed | B06 | TRUE | 74.4 queries/s without, 75.1 with top-100 re-check |
| 17 | The fix comes from the same paper | B06 | TRUE | Jegou, Douze, Schmid 2011, IVFADC+R |

## Full sweep (64 cells unless stated)
| setting | recall | coverage | queries/s |
|---|---|---|---|
| 1 cell | 0.3026 | 0.4121 | 2,480.6 |
| 2 cells | 0.3764 | 0.5985 | 1,707.7 |
| 4 cells | 0.4244 | 0.7707 | 975.8 |
| 8 cells | 0.4491 | 0.9006 | 549.0 |
| 16 cells | 0.4591 | 0.9720 | 285.5 |
| 32 cells | 0.4597 | 0.9966 | 135.5 |
| 64 cells | 0.4595 | 0.9998 | 74.4 |
| 128 cells | 0.4596 | 1.0000 | 38.8 |
| re-check top 10 | 0.4595 | 0.9998 | 75.0 |
| re-check top 25 | 0.6917 | 0.9998 | 74.3 |
| re-check top 50 | 0.8362 | 0.9998 | 75.5 |
| re-check top 100 | 0.9295 | 0.9998 | 75.1 |
| re-check top 200 | 0.9759 | 0.9998 | 73.2 |

## Algebra check (MATH-TYPESETTING.md)
On screen: `x̂ = μ_c + (c_{1,k_1}, …, c_{8,k_8})` and `‖q − x‖² ≈ ‖q − x̂‖²`.
- The repo's lookup-table distance (`lut[j, code_j]` summed over 8 subspaces) was
  compared with ‖q − x̂‖² computed directly from the reconstruction, on 5,000
  vectors: worst relative gap 2.3 x 10^-7 (float32 rounding). So the search's
  distance is exactly the distance to the stand-in.
- The approximation sign is correct: for vector 35, ‖q − x‖² = 254,202 against
  ‖q − x̂‖² = 235,219.
- μ_c is the centre of the vector's cell; k_j is one byte (0 to 255).

## Deliberately not claimed
- Not that IVF-PQ is broken; the ceiling and the fix are both in the paper.
- Not that the re-check is free; it needs the original vectors stored.
- The analogy to AI-written text is about the shape of the problem only.

## First-person claims added in the script revision (18 Nov 2026)

The narration was rewritten to describe what I did. Each new claim about my own work traces to the record:

| Claim | Source |
|---|---|
| The index is built from a 2011 paper | Jegou, Douze, Schmid 2011 |
