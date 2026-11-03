# Sprint 4 — Retry system and the first full run

**Week:** 14–18 Sep 2026 · logged 2026-09-17
**Project:** Mycroft — Adaptive Model Routing & Inference Gateway
**Evidence of commit:** https://github.com/nikbearbrown/mycroft/commit/d2355422cf45a7951881cc4547a2b90a5e266678

- **Video:** https://www.youtube.com/watch?v=VndHWZ2dPFI
- **Drive:** https://drive.google.com/drive/folders/1OopER7YqxoKf_w_qwXM98Jh9C2Yxwm6l?usp=sharing
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **This week's explainer:** [Prefill vs decode](../09172026prefill-decode/)

## What this sprint was for

Everything before this could record a call, make a call, and choose a tier. This
sprint closes the loop: check the answer for free, and if the check fails, try
once on a stronger model. Then run the entire frozen fixture set live and find
out what the gateway actually does.

## What was built

| File | What it does |
|---|---|
| `validators.py` | Five free checks — one per task type — that decide whether an answer is *usable*, never whether it is *correct*. Truncation and emptiness are checked first. |
| `prompts.py` | One prompt per task type. Three of its rules exist solely so the checks are fair to the model. |
| `gateway.py` | Route, call, check, retry once. The retry is written with no loop anywhere, so a retry chain is structurally impossible rather than merely discouraged. |
| `bench/run.py` | The full sweep: dry run with a cost ceiling, a typed confirmation before spending, one timestamped log per run, and grading against the answer key. |
| 50 new tests | 146 passing in total. |

**The retry rule, in full:** one retry, on a failed check or a provider error the
adapter marked retryable, never a second. A terminal error — bad credential,
unknown model, request too large — is never retried, because every tier shares
one credential and would fail identically. A request already on the top tier has
nowhere to go and stops.

## Results — final sweep, `2026-09-17T015116`

| Measure | Value |
|---|---|
| Requests | 24 |
| Attempts | 26 |
| Escalation rate | 8% |
| Failure rate | 0% |
| Total cost | $0.00250 |
| Cost per request | $0.000104 |
| Latency p50 / p95 | 393 ms / 734 ms |
| Graded | 16 of 24 |
| Correct | 14 of 16 |

**Both escalations behaved exactly as designed.** `rag-001` and `rag-004` failed
the citation check on the mid tier and then answered correctly on strong.

**There were zero wrong-but-valid answers.** This reversed the sprint's main
expectation. Every model answer that completed was correct; the two graded wrong
are errors in my own answer key, not model errors. A retry recovers a malformed
answer or a flaky provider — it cannot fix a wrong answer, because a wrong answer
passes every free check.

**Escalation is a cost decision, not just a reliability one.** Escalated requests
were 8% of requests and **23% of the spend** — roughly 3.2x the cost of a normal
request.

**The cost ladder is not monotonic.** On a trivial prompt the strong model
answered for 20% *less* than the cheap one, because cost follows how much a model
says. The crossover is around five output tokens.

## Four failures found by running it

1. **A check that punished correct answers.** `verdict_with_quote` demanded one
   contiguous quoted span; models quoted both conflicting statements joined
   together. All three escalations in the earlier sweep were false alarms caused
   by the check, not the models. The prompt now asks for one continuous span from
   a single statement, and all four contradiction fixtures then passed.
2. **The strong model disappeared.** `qwen/qwen3.6-27b` returned 404 a week after
   two successful calls; the provider's deprecation page still recommended it as
   a migration target. Replaced with `qwen/qwen3.8-27b`.
3. **A configuration number made a whole tier look broken.** A 1024-token budget
   exceeded the account's cap of 1000 output tokens per minute, so every strong
   call was refused before the model ran. Lowered to 896 and re-gated live. A 429
   meaning "request too large" is now classified terminal — waiting cannot fix it.
4. **A summary counted another run's requests.** Log files were named by day, so a
   3-request smoke test and the 24-fixture sweep shared one file and the summary
   reported 27 requests for 24 fixtures. Log files are now stamped to the second
   and each summary counts only its own run's request ids.

## Evidence

- `logs/gateway/runs/2026-09-17T015116-sprint4-run.jsonl` — every attempt, with
  cost, latency, tier and validator result
- `scripts/gateway/bench/results/2026-09-17T015116-sprint4-run.json` — the graded
  rows and summary
- `scripts/gateway/FINDINGS.md` section 7 — what the first full run showed
- `logs/RUN_LOG.md`, entry dated 2026-09-17
- Commit [`d235542`](https://github.com/nikbearbrown/mycroft/commit/d2355422cf45a7951881cc4547a2b90a5e266678)

## Limits and open items

- **No progress video was recorded for this week.**
- 8 of 24 fixtures could not be graded at all — extraction and open prose, where
  no deterministic check can judge correctness. That became Sprint 5.
- The two answer-key errors from Sprint 3 are still unfixed and account for both
  "wrong" gradings above.
-