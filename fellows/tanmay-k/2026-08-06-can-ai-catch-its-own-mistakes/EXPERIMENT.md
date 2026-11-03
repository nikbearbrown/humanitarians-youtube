# EXPERIMENT — Does a model miss its own mistakes?

The primary source for **"Can AI Catch Its Own Mistakes? I Ran the Experiment."** Every figure the film
puts on screen traces to this document and to the raw transcripts in
`experiment/`.

**Headline: 33 wrong expressions, 99 verdicts, zero missed. Gap 0.0 in all three
configurations.** The blind spot did not reproduce.

---

## 1. The question, and why it needed a new experiment

Published work reports that a language model asked to check its own work tends to
agree with itself:

| Source | Status | Finding |
|---|---|---|
| Huang et al., ICLR 2024 — [arXiv:2310.01798](https://arxiv.org/abs/2310.01798) | **Peer-reviewed** | Intrinsic self-correction — no external feedback — fails on reasoning and can *degrade* accuracy |
| Tsui, 2025 — [arXiv:2507.02778](https://arxiv.org/abs/2507.02778) | **Preprint, not peer-reviewed** | The *self-correction blind spot*: models fail to correct errors in their **own** output while correcting the **identical** error presented externally. **64.5%** average across 14 open **non-reasoning** models; appending **"Wait"** removes **89.3%** of it |

Neither is established for current Claude models. The source draft this film
rebuilds asserts a stronger claim than either — *"a system cannot reliably audit
its own output"* — with no measurement at all.

## 2. Design

**Task.** Make 24 from four numbers, each used exactly once. Ground truth is
decidable, so the model's opinion about correctness is never needed.

**One wrong expression per trial**, obtained one of two ways:

- **natural** — the model's own mistake, used as-is
- **injected** — its *correct* answer with exactly one binary operator corrupted;
  every corruption is verified to still use each number once and to not equal 24

Injection follows Tsui's own method (controlled error injection at three
complexity levels: **subtle** = closest to 24, **moderate** = median, **obvious**
= furthest). Waiting for natural errors alone does not work — see §5.

**That single expression then goes through four conditions:**

| Arm | Condition | Isolates |
|---|---|---|
| **A** self-verify | presented in the assistant turn, as the model's own | the blind spot |
| **B** external | **fresh conversation**, identical expression, presented as a third party's submission | **self-reference vs task difficulty** |
| **C** self + "Wait" | arm A with Tsui's one-token remedy | whether the remedy transfers |
| **D** evaluator | exact rational arithmetic in Python | ground truth |

**A vs B is the experiment.** A two-arm design — self-verify against an
evaluator, which is what the source draft uses — *cannot distinguish* "the model
is bad at this puzzle" from "the model won't contradict itself." Both produce an
identical result. Arm B separates them.

### Three model configurations

Thinking defaults differ, and that difference would otherwise be confounded with
generation:

| Config | Model | Thinking | Tests |
|---|---|---|---|
| `haiku-nothink` | `claude-haiku-4-5` | omitted → **off** | the non-reasoning class Tsui measured |
| `sonnet5-nothink` | `claude-sonnet-5` | **explicitly disabled** | newer generation, *same* reasoning mode → isolates generation |
| `sonnet5-think` | `claude-sonnet-5` | **adaptive** | does reasoning close the blind spot? |

`sonnet5-nothink` sets `thinking` explicitly because **Sonnet 5 runs adaptive
thinking by default** — omitting it would compare a reasoning model against a
non-reasoning one and call the difference "generation."

**No `temperature` / `top_p` / `top_k` anywhere.** Non-default sampling
parameters are rejected with a 400 on Sonnet 5, so they are omitted on both
models — removing a confound rather than adding one.

### Two correctness constraints in the harness

- **Exact rational arithmetic.** `8 / (3 - 8/3)` is exactly 24 but evaluates to
  `23.999999999999993` in floating point. A float grader marks the correct
  answer wrong and **inverts the entire finding**. Everything runs on
  `fractions.Fraction`.
- **No `eval()`.** Expressions go through an AST whitelist (`+ - * /` and unary
  sign on integer literals only), verified to reject `__import__`, `open`,
  attribute access, names, `**`, conditionals and lambdas. Model output is
  untrusted input.

All 12 puzzles were brute-force verified solvable, so no "wrong" answer is an
artifact of an impossible puzzle.

## 3. Results

Run 2026-08-12. 136 API calls. `results-20260812T014950Z.json`.

| Configuration | n | self | external | wait | **gap** |
|---|---:|---:|---:|---:|---:|
| `haiku-nothink` | 11 | 0% | 0% | 0% | **0.0** |
| `sonnet5-nothink` | 10 | 0% | 0% | 0% | **0.0** |
| `sonnet5-think` | 12 | 0% | 0% | 0% | **0.0** |

**33 wrong expressions. 99 verdicts. Zero missed. Zero unparseable.**

Validation on the result itself:

- All 33 tested expressions independently re-graded as **genuinely wrong**
- **0 of 99** verdicts unparseable — nothing silently dropped
- All three injection levels exercised: 10 subtle, 6 moderate, 8 obvious
- The model did the arithmetic rather than guessing. Verbatim, on a subtle
  corruption presented as its own:

  > "Let me verify: 8/3 = 2.666..., then 3 - 8/3 = 3 - 2.666... = 0.333...
  > Then 8 + (3 - 8/3) = 8 + 0.333... = 8.333...
  > This does not equal 24. The numbers used are correct (two 3s and two 8s),
  > but the arithmetic result is wrong."

## 4. What this licenses — and what it does not

| | |
|---|---|
| **Rejects 64.5%** | P(observing 0/33 if the true rate were 64.5%) = **1.4 × 10⁻¹⁵** |
| **Does NOT establish zero** | Exact binomial 95% upper bound = **8.7%** pooled (11.7% on injected-only). The claim is "below about nine percent," never "zero." |
| **Does NOT refute Tsui** | That paper measured 14 *open, non-reasoning* models. "Did not reproduce here" means **model-dependent**, not wrong. |
| **One task only** | Arithmetic with decidable ground truth is the easiest possible case for verification. Nothing here transfers to code review, factual claims, or judgment. |

## 5. Revision 1 — the run that failed, and why it is in the film

The first version waited for **natural** errors only. It produced the same null
but ran out of denominator: Sonnet 5 answered 9/10 and then 10/10 correctly, so
the `sonnet5-think` arm had **zero** wrong answers and therefore no data at all.

The control existed and never fired. The headline question was left *unanswered*
rather than answered. `results-20260811T065935Z.json` is kept as evidence, and
the film shows it — it is the reason the framework has a fourth question.

## 6. Reproducing it

```bash
cd experiment
python3 -m venv .venv && .venv/bin/pip install anthropic
python3 verify_bench.py --dry-run        # no key, no spend — inspect the pipeline
export ANTHROPIC_API_KEY=...             # supply your own
.venv/bin/python verify_bench.py         # ~144 short calls, well under a dollar
```

`--dry-run` output is labelled **NOT evidence** in both the console and the JSON,
because canned responses cannot support a finding.

Every prompt, reply, verdict and grade is in the results JSON. The summary is
derived from it and can be recomputed independently.
