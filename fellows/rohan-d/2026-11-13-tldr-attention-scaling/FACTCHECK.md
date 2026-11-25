# FACTCHECK — tldr-attention-scaling

Verdicts: PASS · CORRECTED · EXEMPT. "Run" = recomputed by `experiment.py` / `naive_fixed_divisor.py` / `bhtf_check.py` (seed 7; outputs saved beside them).

| # | Beat | Claim | Verdict | Source | Fix |
|---|---|---|---|---|---|
| 1 | B00, B01 | The scores are divided by √d_k in the Transformer's attention | PASS | Paper §3.2.1, Eq. 1 | — |
| 2 | B01 | Every attention layer uses it | PASS | §3.2.3: all three uses of multi-head attention go through scaled dot-product attention | Narration says "every attention layer" in the Transformer; keep |
| 3 | B00, B12, B16 | For independent q, k components with mean 0 and variance 1, q·k has mean 0 and variance d_k | PASS | Paper footnote 4; run: var 3.99, 15.98, 63.99, 512.65, 2052.58 for d_k = 4, 16, 64, 512, 2048 | Film states the assumption on screen |
| 4 | B16 | Var(q_i k_i) = 1 for each product | PASS | derived: E[q²]E[k²] − (E[q]E[k])² = 1·1 − 0 | — |
| 5 | B16 | Variances of independent terms add; Var(X/c) = Var(X)/c² | PASS | standard; confirmed by run (std 1.00 after dividing) | — |
| 6 | B10 | At length 512 one key takes 99.6% | PASS | run, single instance: raw softmax [0, 0.996, 0.004, 0, 0, 0] | Label "one example, seed 7" on screen |
| 7 | B11 | On average the largest weight climbs from 57% to 96% (lengths 4 → 512) | PASS | run: 0.574 → 0.961 over 20 000 trials, 6 keys | "on average" in narration; "6 keys" on screen |
| 8 | B11 | At length 512 scores span dozens of units | PASS | run instance: −17.2 … 41.1 | — |
| 9 | B12 | Saturated softmax passes back almost no gradient | CORRECTED | Paper says only "extremely small gradients" and that it suspects this ("We suspect…") | Narration frames the slope readout as "our rough measure" (largest p(1−p): 0.203 → 0.0276, run); on-screen label "our measure" |
| 10 | B13 | Divide-by-10 gives largest weight 0.209 (d=4), 0.368 (d=64), 0.809 (d=2048) | PASS | run (`naive_output.txt`); uniform over 6 keys is 0.167 | — |
| 11 | B13 | √d_k divisor holds ≈ 0.40–0.42 at every length | PASS | run: 0.400 … 0.422 | not narrated as a number, shown in B15 |
| 12 | B14 | Score-cloud std is 2, 4, 8, 16, 22.6, 45.3 at d = 4, 16, 64, 256, 512, 2048 | PASS | run | — |
| 13 | B14 | "Every time the length quadruples, the width doubles" | PASS | follows from std = √d_k; run values 2→4→8→16 | — |
| 14 | B15 | After dividing at d=512, softmax = [0.027 0.356 0.278 0.085 0.103 0.151] | PASS | run (same instance as claim 6) | — |
| 15 | B17 | Measured variance at 512 is 512.65 → "about five hundred and thirteen"; divided, 1 | PASS | run: 512.65; std/√512 = 1.00 | — |
| 16 | BHTF | Variance 4 entries, d=64: var(q·k)=1024; dividing by √64 leaves 16; divisor 4·√64 gives 1 | PASS | `bhtf_check.py`: 1021.0, 16.0, 0.997 (200 000 draws) | answer is not revealed in the film; viewer's own check |
| 17 | all | Scope: results hold for the paper's idealised assumption; trained vectors are not claimed to behave this way | EXEMPT (scope statement) | Paper: "We suspect" | B12 and BVDT carry "for random vectors"; boundary named in BHTF |

Datable material stripped: no model names, version numbers, benchmark scores, or dates in narration or on-screen text.
Source inconsistency noted, not used: the paper's abstract/Table 2 give 41.8 BLEU for English→French while §6.1 text says 41.0 (irrelevant to this film).
Algebra check separate from typography: items 4, 5, 16 verified numerically; equation frames to be inspected at revealed states and 15/50/85% before the final.
