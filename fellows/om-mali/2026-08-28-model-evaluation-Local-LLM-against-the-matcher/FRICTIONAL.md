# Frictional log — 2026-08-28

**Week 4 · model evaluation · A local 8B model measured against the matcher, and declined**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to
`docs/entity_resolution.md` §9, `docs/_adjudication_metrics.json` or
`docs/_adjudication_results.json` — which contains every raw model reply.

---

## What I was working on

Testing whether a language model does entity resolution better than the deterministic matcher
I built the week before.

This is the week the project was most likely to fool itself. The honest version of the question
requires committing to the answer *before* running it, so the plan carried the instruction in
advance: **"if there is no lift, keep the deterministic matcher and say so."** That sentence is
the only reason the result is worth anything.

## What I tried, and what I expected

Ollama 0.33.1 with `llama3.1:8b` — 8.0B parameters, Q4_K_M, 5.3 GB, running entirely on an
RTX 4070 Laptop. **322 calls, temperature 0, fixed seed, JSON-Schema-constrained decoding,
zero failures.**

The model saw issuer name, title, filer and the candidate list — **exactly what the
deterministic matcher gets, and deliberately no price**, since the matcher does not get price
either. There is a test asserting the label never reaches the prompt.

I expected modest lift on the hard cases. Language models are supposed to be good at exactly
this: messy names, abbreviations, human spelling variation.

## Where it resisted, and what I did next

**It lost 5.1 points of precision.**

| System | Precision | Recall | F1 | Lift |
|---|---|---|---|---|
| Deterministic matcher v1 | 0.9959 | 1.0000 | 0.9979 | — |
| + LLM in the review band | 0.9449 | 1.0000 | 0.9717 | **−0.0262** |
| + LLM overruling everything | 0.9447 | 0.9958 | 0.9696 | −0.0283 |

Per holding, that is **1 wrongly-included holding becoming 196**.

**The failure mode is specific and worth naming: it promotes resemblances.** Of the 85 strings
it saw, it fixed 1 and broke 14 — and all fourteen are the same move. The matcher had resolved
nothing, and the model named a company anyway:

- `HYPERSCALE DATA INC` → Scale AI, on the invented ground that it *"is the parent company of
  Scale AI"*.
- A `SCALED AGILE` term loan → Scale AI.
- `COHERE TECHNOLOGIES` → Cerebras.
- **`XAI3-FT5O.AF`, which is a Fidelity internal security code**, → X.AI.

Two replies contradict themselves outright: the reason field says *"do not match any of the
candidate companies"* while the company field names Scale AI.

**Confidence is unusable for triage, which constrains the next week.** The model returned
**1.000 on 315 of 322 answers**, and only three distinct values in the entire run. Twelve of
the fifteen answers that disagree with their label came back at 0.95 or higher. A review queue
sorted by model confidence would put the wrong rows at the bottom. There is a test pinning
that.

**The hard subset lied, and that is a methodology finding rather than a result.** Every LLM
policy scores **1.0000 precision on the 144-string hard subset**. That number is true and
completely misleading: the subset was defined in week 3 to exclude labels decided by the name,
which excludes the `E0` negatives — which is the only place the model does damage. *A subset
built to test one system is not automatically the right lens for the next one.* I put that in
the narration script's guardrails explicitly, as a number not to quote.

**I built a fourth policy and then argued against it.** Every break was a *promotion*; the
single fix was a *demotion* — the matcher had claimed OpenAI for `OPEN BAY AUTOS AI INC.`, the
used-car marketplace, and the model withdrew it. So `POLICY_VETO` lets the model only withdraw
a weak claim, never create one. It scores **1.0000 / 1.0000**.

That number should not be believed, and I wrote down why: it is consulted on 4 of 322 strings,
vetoes one, and is right about the other three by declining to act. It was designed *after*
reading the failures, so this golden set motivated it and cannot validate it. And decisively —
those four strings are **the same four the matcher already routes to a human**, so it saves no
human effort at all. Retained, measured, **off by default**.

## What Claude contributed, and what I did with it

Claude wrote the adjudication harness, the schema-constrained prompt, the scoring script and
the stub-backed tests (the whole suite runs with no GPU and no 5 GB model).

**The figures caught two factual errors in my own prose, and that is the useful part.** Because
every number in a figure is queried at render time rather than typed, the chart disagreed with
the paragraph:

- **"Confidence 1.000 on 308 of 322" was wrong; it is 315.** And "nine of the fourteen wrong
  answers at 0.95 or above" was wrong twice over — it is 12 of the **15** answers that disagree
  with their label, or 11 of the 14 band-policy breaks if that is the intended denominator.
  Both original numbers were typed by hand. `run_adjudication.py` now emits a `confidence`
  block into the metrics artifact and a test recomputes it from the cache, so the prose cannot
  drift from the data again.
- **The model was offered 11 candidate companies, not 7.** The figure's count came from
  `user.count("\n- ")`, which matches nothing — the block is indented, not bulleted — and fell
  through to a hand-typed `or 7`. Seven is the universe; the list also carries four watchlist
  companies, and **Scale AI and X.AI, the two names the model most often promotes to, are both
  watchlist**. A fallback that hides a failed measurement is worse than no fallback.

**The judgment Claude could not make was the scoping one.** A model that produces
`HYPERSCALE DATA INC → Scale AI` with a confident invented justification reads, in isolation,
like a plausible answer. Deciding it is wrong requires knowing the corpus. And deciding that
the correct response is *decline the model* rather than *tune the prompt* is a project
decision, not a technical one — the plan pre-committed to it, and I held to it.

I also wrote three guardrails into the narration against overclaiming in the opposite
direction: don't call the model useless (it is mis-scoped, not incapable), don't imply a larger
model would also fail (none was tried), and don't quote the hard-subset score.

**One dependency deviation, decided deliberately.** The plan pins `ollama==0.4.5`;
`src/resolve/llm.py` uses `requests` against the same HTTP API. One POST to one endpoint does
not need a wrapper package, and `OLLAMA_HOST` can now point anywhere.

## What I understand now, and what I still do not

**Understood.** The failure is not randomness — it is a systematic bias toward producing an
answer when the correct output is "nothing". Self-reported confidence carries no usable signal
here. And an evaluation subset inherits the assumptions of whatever it was built to test; the
hard subset was fit for week 3 and actively misleading for week 4.

**Throughput, since cost is the usual counter-argument.** 3.236 s mean per call, 196.9 tokens/s,
2.4 s cold load. Against the shipped universe layer that is 12.5 minutes for LLM-alone and 16
seconds for the band policy. Note the band policy consults 26.4% of the golden set but only
**2.2% of the corpus** — the golden set over-samples near-miss negatives by design, so quoting
its consult rate as an operating cost would overstate the bill tenfold. **Cost is not why this
was declined. Negative accuracy is.**

**Not understood.** Whether a 70B model fails the same way — I did not try one, and I will not
claim it would. Whether the promotion bias is a property of the model, the prompt, or the task
framing. And `Inter` does not resolve in the renderer and falls back to monospace, so every
non-title figure label renders mono against what `DESIGN.md` specifies; week 3's figures do the
same, so it is consistent rather than new, but it is still not right.
