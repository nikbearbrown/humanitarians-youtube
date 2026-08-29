# FACTCHECK.md — Claude, Judged.

## Method note (read first)

Unlike the three prior builds this session (each grounded entirely in one
already-read book chapter), this reel has no single source document — the
topic ("LLM-as-a-judge" evaluation systems) is a well-established software
engineering pattern, not a text being explained. Per the DOUBLE-CHECK LAW,
every claim below is checked against ONE of two categories:

- **(General)** — a widely-documented engineering pattern with no single
  citable origin (e.g. "cache identical judge calls," "separate what from
  how"), stated at the level of the mechanism, never with an invented
  statistic, tool name, or specific implementation claimed to behave a
  particular way without direct knowledge of its source.
- **(Cited)** — a specific, attributable finding, cited by name. Exactly
  one citation appears in this reel: Zheng, L. et al. (2023), *"Judging
  LLM-as-a-Judge with MT-Bench and Chatbot Arena,"* the paper that
  originated the position-bias / verbosity-bias / self-enhancement-bias
  framing and validated LLM-judge agreement against human preference —
  both used in beats A2-3, A2-4, A2-5, and A4-6.

No claim in this reel states a specific percentage, benchmark score, or
named commercial tool's exact internal behavior — all of those would need
a live source check this build doesn't have, so they were deliberately
kept out of the script.

## Claim-by-claim

| Beat | Claim | Category | Note |
|---|---|---|---|
| A1-2 | A test case = input + candidate + reference + rubric | General | The four fields recur across essentially every published LLM-eval harness design; not attributed to one source |
| A1-4 | A judge prompt needs role framing, rubric, candidate output, and a fixed answer format | General | Standard structure; the "impartial judge" framing phrase specifically echoes Zheng et al. 2023's own prompt template |
| A1-5 | Reference-based vs. reference-free judging is a real, named distinction | General | Widely used distinction in eval literature |
| A1-6 | Asking for reasoning before the score improves judge reliability | General | A documented chain-of-thought-style technique; not attributed to one paper here |
| A2-2 | Free-text regex parsing vs. constrained/JSON-mode output | General | Standard software-engineering distinction, not eval-specific |
| A2-3 / A2-4 | Position bias, verbosity bias, self-enhancement bias, named and defined | **Cited** | Zheng et al., 2023 — the paper that named and measured all three |
| A2-5 | Swapping answer order and requiring agreement mitigates position bias | **Cited** | The mitigation technique described in the same paper |
| A3-2 through A3-6 | Metric abstraction, caching, retries, concurrency, partial-failure handling | General | Standard batch-systems engineering, applied to eval; not eval-specific research claims |
| A4-2 through A4-5 | Aggregation (mean/pass-rate/win-rate/category breakdown), baseline comparison, CI gating, artifact publishing | General | Standard CI/CD and metrics-reporting practice |
| A4-6 | Zheng et al. validated their judge against human preference agreement | **Cited** | Stated as the paper's own methodology, not a specific agreement percentage (no number is claimed on screen) |

## Corrections applied

None — this is a first draft, not a revision of an existing script.

## What was deliberately left out

- No specific commercial eval framework (OpenAI Evals, DeepEval, promptfoo,
  RAGAS, etc.) is named or described, since none of their specific internal
  behavior was verified for this build — the reel describes the general
  pattern all of them implement some version of, not any one tool.
- No benchmark numbers, latency figures, or cost figures are stated, since
  none were sourced or verified.
