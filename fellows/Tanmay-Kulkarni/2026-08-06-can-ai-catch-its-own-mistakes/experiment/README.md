# Self-Verification Blind Spot — Measurement Harness

Measures how often a current Claude model **confirms its own wrong answer**, and
whether that changes when the identical wrong answer is presented as someone
else's.

Built for the Week 18 video, which rebuilds
`claude-for-artificial-intelligence/nbb-cli-agent-self-verification-failure`
from the `humanitarians-youtube` repo. That draft asserts a conclusion it cannot
support; this harness produces the evidence instead.

## The question

Published work says an LLM asked to check its own reasoning tends to agree with
itself:

- **Huang et al., ICLR 2024** — [arXiv:2310.01798](https://arxiv.org/abs/2310.01798).
  *Peer-reviewed.* Intrinsic self-correction — no external feedback — fails on
  reasoning tasks and can *degrade* accuracy.
- **Tsui, 2025** — [arXiv:2507.02778](https://arxiv.org/abs/2507.02778).
  **Preprint, not peer-reviewed.** Names the *self-correction blind spot*:
  models fail to correct errors in their **own** output while correcting the
  **identical** error presented externally. Reports **64.5%** average across 14
  open **non-reasoning** models, and that appending **"Wait"** removes **89.3%**
  of it.

Neither is established for current Claude models. That's what this measures.

## Why four arms

The task is make-24: given four numbers, write an expression using each exactly
once that equals 24. Ground truth is decidable, so the model's opinion about
correctness is never needed.

Each trial takes the model's **first** answer, then runs three verification
conditions **on that same answer** — so framing is the only thing that varies:

| Arm | Condition | Isolates |
|---|---|---|
| **A** self-verify | asked in the same conversation, answer visibly its own | the blind spot |
| **B** external | **fresh conversation**, identical expression presented as a third party's | **self-reference vs task difficulty** |
| **C** self + "Wait" | arm A with Tsui's one-token remedy | whether the remedy transfers |
| **D** evaluator | exact rational arithmetic in Python | ground truth |

**A vs B is the experiment.** A two-arm design — self-verify against an
evaluator, which is the obvious one and the one the source draft uses — *cannot
distinguish* "the model is bad at this puzzle" from "the model won't contradict
itself." Both produce an identical result. Arm B is what separates them.

It's also a genuine falsifiability test: **if B fails as often as A, the
self-reference thesis is dead** and the video reports that instead.

## Why three model configurations

Thinking defaults differ between these models, and that difference would
otherwise be silently confounded with generation:

| Config | Model | Thinking | Tests |
|---|---|---|---|
| `haiku-nothink` | `claude-haiku-4-5` | omitted → **off** | the non-reasoning class Tsui measured |
| `sonnet5-nothink` | `claude-sonnet-5` | **explicitly disabled** | newer generation, *same* reasoning mode → isolates generation |
| `sonnet5-think` | `claude-sonnet-5` | **adaptive** | does reasoning close the blind spot? |

`sonnet5-nothink` must set `thinking` explicitly: **Sonnet 5 runs adaptive
thinking by default**, so omitting the parameter would compare a reasoning model
against a non-reasoning one and call the difference "generation."

`sonnet5-think` tests Tsui's own hypothesis — that models trained with outcome
feedback learn error correction — on models the paper never covered.

**No `temperature` / `top_p` / `top_k` anywhere.** Non-default sampling
parameters are rejected with a 400 on Sonnet 5, so they're omitted on both
models. That removes a confound rather than adding one.

## Exact arithmetic is not optional

`8 / (3 - 8/3)` is exactly **24**, but evaluates to **23.999999999999993** in
floating point. A float grader marks the correct answer wrong and **inverts the
entire finding**. Everything here runs on `fractions.Fraction`.

Expressions are evaluated through an AST whitelist (`+ - * /` and unary sign on
integer literals only) — never `eval()`. Verified to reject `__import__`,
`open`, attribute access, names, `**`, conditionals, and lambdas.

## Running it

Inspect the pipeline first, with no key and no spend:

```bash
python3 verify_bench.py --dry-run
```

Then the real run:

```bash
python3 verify_bench.py
```

Credentials: the SDK reads `ANTHROPIC_API_KEY`, or an `ant auth login` profile —
**an unset env var does not mean there are no credentials.** Needs
`pip install anthropic`.

Useful flags:

```bash
python3 verify_bench.py --models haiku-nothink sonnet5-nothink   # skip the thinking arm
python3 verify_bench.py --trials 6                              # shorter run
python3 verify_bench.py --max-retries 8                         # flaky network
```

**Cost:** 4 calls per trial × 12 puzzles × 3 configs = **144 short calls**, well
under a dollar at current Haiku 4.5 and Sonnet 5 rates.

## Reading the output

`results-<timestamp>.json` holds **every prompt, every reply, every verdict, and
every grade**. The transcript is the evidence; the summary is derived from it and
can be recomputed independently.

The **blind-spot rate** denominator is *only* the trials whose first answer was
actually wrong — a trial that was right has no error to miss. Unparseable
verdicts are excluded from their arm's denominator and **reported separately**,
never coerced to either side, because silently dropping them would bias the rate.

The number that matters is **`gap` = self − external**:

- **large positive gap** → the blind spot reproduces; provenance is the variable
- **gap near zero** → no blind spot here; the task was just hard. The
  self-reference thesis fails and the video says so.

## Honesty constraints this harness enforces

- `--dry-run` numbers are labeled **not evidence** in the console output and in
  the JSON `meta.dry_run` field. Canned responses cannot support a finding.
- Refusals and `max_tokens` truncation are recorded as errors, never as verdicts.
- Nothing is inferred where a call failed; failed trials are excluded from
  denominators and counted in `errors`.
