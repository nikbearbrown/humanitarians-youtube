# FACTCHECK.md — Further, But Better

Every claim the narration or the screen makes. All figures are measured in
github.com/Kenny0bi/quantlab across 34 evaluations on one fixed wikitext-2
protocol, and are reported as measured rather than rounded.

| # | Claim on screen or spoken | Verdict | Source |
|---|---|---|---|
| 1 | Three quantization methods implemented from their papers (RTN, GPTQ, AWQ) | TRUE | quantlab README and source |
| 2 | 34 configurations measured on one fixed protocol | TRUE | quantlab results table |
| 3 | fp32 baseline perplexity 26.2 | TRUE | quantlab results table |
| 4 | 4-bit GPTQ group-128 perplexity 28.5 | TRUE | quantlab results table |
| 5 | 8x memory reduction at 4 bits | TRUE | 32 bits to 4 bits per weight |
| 6 | Roughly a 9% quality tax | TRUE | 28.5 vs 26.2 = +8.8% |
| 7 | At 3 bits GPTQ 112 against naive per-channel RTN 2,482 | TRUE | quantlab results table |
| 8 | At 2 bits every method collapses | TRUE | quantlab results table |
| 9 | GPTQ weights end 2.5x further from originals than RTN | TRUE | quantlab test suite |
| 10 | GPTQ outputs 2x more accurate than RTN at 4 bits | TRUE | quantlab test suite |
| 11 | The first benchmark confounded algorithm with scale granularity | TRUE | README, author's own account |
| 12 | Granularity alone: 2,482 to 183. Compensation alone: 2,482 to 504. Both: 112 | TRUE | quantlab ladder figure |
| 13 | AWQ at the paper's fixed alpha performed worse than grouped rounding (245 vs 183) | TRUE | quantlab results |
| 14 | Per-layer alpha search improved AWQ to 143 | TRUE | quantlab results |

## Not claimed
- No claim that these results transfer to models other than GPT-2.
- No claim of state of the art; the video compares only what was run here.
- The failed configurations are acknowledged on screen rather than omitted.

## Terminology deliberately avoided
Hessian, perplexity internals, group size and Bellman-style notation are not
named. The benchmark is introduced only as "lower is better", because the
audience is not assumed to have a quantization background.
