> The code behind this file is in `experiment/` in this folder (the superseded first run, `measurements_v1/`, is kept locally).

# Week 30 — Measurements (corrected 2026-11-08)

**Read this first.** The first version of this file (kept in `measurements_v1/`) said both sides did the same elementwise work. They did not:
the recurrent side evaluated 5 gate functions per hidden unit per step (three sigmoids, two tanh), the parallel side 2. The multiply-add
arithmetic was equal; the elementwise part was not, and that inflated the headline ratio. It was found while fact-checking the film, before
anything was published. The code is fixed (`measure_*.c`: the parallel side now evaluates the same 5 per unit, independent of its neighbours),
the numbers below are the corrected ones, and `FACTCHECK.md` lists every figure in the films that changes.

Controlled setup: **same weight matrix (390 by 512 = 199,680 weights: 128 hidden units, 262 inputs, four gates), same total multiply-adds
(19,968,000 over 100 steps), same elementwise gate work.** Only the dependency differs.
- **Recurrent:** T steps, each a matrix-vector product that needs the previous step's hidden state, then the five gate evaluations per unit.
- **Parallel:** the same matrix applied to T independent rows (what a convolution does with one filter at every position), then the same five gate
  evaluations per unit and row.
One thread, float32, batch 1, one Apple-silicon laptop, compiled C. Not an embedded chip. Each program reports the median of 21 to 41 timed runs;
the tables give the median and range over 5 to 10 separate runs of the program, because run-to-run variation on this machine is about 10 to 20%.

## Results at 100 steps (20 million multiply-adds), full step (equal gate work)
| Kernel (how well it can overlap independent rows) | Recurrent | Parallel | Ratio, median (range over runs) |
|---|---|---|---|
| Scalar loops, no vectorisation (`measure_scalar.c`) | 6.11 ms | 6.37 ms | 0.98x (0.96 to 1.02) |
| Vectorised loops, no reuse | 1.83 ms | 1.85 ms | 1.00x (0.93 to 1.03) |
| Vectorised, 4 rows per weight load (`measure_reuse.c`, RB=4) | 1.84 ms | 1.40 ms | 1.33x (1.29 to 1.33) |
| Vectorised, 8 rows per weight load (RB=8) | 1.86 ms | 1.38 ms | 1.34x (1.28 to 1.37) |
| Vectorised, 16 rows per weight load (RB=16) | 1.90 ms | 1.37 ms | 1.34x (1.33 to 1.41) |
| Optimized matrix multiply vs matrix-vector (`measure_dependency.c`, Accelerate) | 0.362 ms | 0.098 ms | **3.7x (2.9 to 3.7)** |

## Optimized multiply across sequence length (full step, 10 runs)
| Steps | 10 | 25 | 50 | 100 | 200 | 400 |
|---|---|---|---|---|---|---|
| Recurrent ms | 0.036 | 0.090 | 0.181 | 0.362 | 0.726 | 1.454 |
| Parallel ms | 0.012 | 0.027 | 0.052 | 0.098 | 0.194 | 0.383 |
| Ratio, median | 3.0 | 3.3 | 3.5 | 3.7 | 3.8 | 3.8 |

The 100-step ratio was 2.9 to 3.7 over all 18 runs of the corrected program (the ten-run table above spans 3.3 to 3.7; two earlier single runs gave 2.9 and 3.0), so quote it as about 3.5, not as a precise figure. From 25 to 400 steps the recurrent time grows 16.2 times (16 times the steps). The ratio stays between 3.3 and 3.8 (the 10-step row is dominated by per-call overhead).

## The same measurement with the gate work taken out of both sides (matrix products only, `-DNOELEM`)
At 100 steps: scalar loops 1.00x (0.98 to 1.02); vectorised, no reuse 1.01x; 4 rows 1.33x; 8 rows 1.38x (1.36 to 1.39); 16 rows 1.38x; **optimized multiply about 6.3x (6.2 to 6.6; recurrent 0.19 to 0.30 ms, parallel 0.03 to 0.047 ms)**. The sequence-length sweep was not run for this variant.
Build the variant with `-DNOELEM`; the gate functions then make up the missing difference: with equal gate work on both sides the optimized-multiply gap falls from about 6.3x to about 3.7x, because that work is the same on both sides and is about half of the recurrent step's time at this speed (0.362 ms with gates against 0.19 to 0.30 ms without).

## What this says
- Counting multiply-adds gives 1.0x in every row, so it cannot be the source of a gap.
- The gap appears as far as the kernel can **reuse each loaded weight across independent positions**: 1.0x, then 1.3x, then 3.7x (6.3x on the matrix products alone).
- With nothing to overlap the gap is about 1.0x: the slowdown belongs to **model and chip together**.
- The 3.7x also includes cache blocking and the matrix unit of this machine; we did not separate them from weight reuse.
- The most the corrected full-step measurement reaches is about 3.8x, at 400 steps. The matrix products alone reach about 6.3x. Neither is anywhere near eighty, and neither is a microcontroller.

## Superseded first run (`measurements_v1/`, unequal gate work: do not cite)
Scalar 6.91 vs 6.73 ms (1.03x); 4 rows 1.36x; 8 rows 1.40x; optimized multiply 0.484 vs 0.085 ms (5.7x; repeats of the same program gave 5.2x to 6.5x at 100 steps); band 4.8x to 5.7x. The 5.7x sat near the matrix-only figure by coincidence, not by design.

## Files
`measure_dependency.c`, `measure_scalar.c`, `measure_reuse.c` (build lines in each header; `-DRB=n` sets the rows per load; `-DNOELEM` removes the gate work); `measurements_v2.json` (the repeated runs); `measurements_v1/` (the superseded first run and its sources).
`lstm_check.py`, `cnn_fair.py` are the earlier rough Python pass, kept for the record.
