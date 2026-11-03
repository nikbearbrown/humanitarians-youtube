# Frictional log — Adaptive Model Routing Gateway, Sprint 4

## 2026-09-17 — one retry, and the first full run

- **Video (progress):** https://www.youtube.com/watch?v=VndHWZ2dPFI&t=10s
- **Drive:** https://drive.google.com/drive/folders/1OopER7YqxoKf_w_qwXM98Jh9C2Yxwm6l?usp=drive_link
- **Evidence of commit:** https://github.com/nikbearbrown/mycroft/commit/d2355422cf45a7951881cc4547a2b90a5e266678


**What I was working on.** The retry rule  when a free check fails, try once on
a stronger model  and then the first live sweep of all 24 fixtures through the
whole gateway.

**What I tried, and what I expected.**
- I expected retries to be the feature that earns the project its keep:
  cheap model answers badly, strong model rescues it.
- I expected a meaningful number of answers that **pass the check and are still
  wrong**, since that is the failure the checks can't see.
- I expected the cost ladder to be monotonic  cheap always cheapest.

**Where it resisted, and what I did next.**
- The first sweep showed three escalations, and **all three were false alarms
  caused by my own check.** `verdict_with_quote` demanded one contiguous quoted
  span; the models had quoted both conflicting statements joined together, which
  is a reasonable thing to do and not what the check allowed. I was paying for
  strong-tier retries to fix a formatting rule. Narrowed the prompt to ask for
  one continuous span from a single statement; all four contradiction fixtures
  then passed and graded correct.
- **The strong model disappeared.** `qwen/qwen3.6-27b` returned 404 "does not
  exist or you do not have access" a week after two successful calls. The
  provider's own deprecation page still recommended it as a migration target,
  so their documentation contradicted their API. Replaced with 3.8.
- Then **every** strong call was refused before the model even ran: my 1024
  token budget exceeded the account's cap of 1000 output tokens per minute. A
  configuration number, not a model problem, and it made a whole tier look
  broken. Lowered to 896, then gate-called it live to prove it.
- Related: a 429 saying "request too large" is nothing like a 429 saying "slow
  down". Waiting fixes the second and can never fix the first, so the first is
  now classified terminal and never retried.
- My run summary **counted a different run's requests**: log files were named by
  day, so a 3-request smoke test and the 24-fixture sweep shared one file and the
  summary reported 27 requests for 24 fixtures. Log files are now stamped to the
  second and the summary only counts the request ids from that run. I nearly
  reported that 27 as a result.
- A test hardcoded 1024 as the strong budget and broke when the budget changed 
  it was asserting a literal instead of the configuration.

**What Claude contributed, and what I did with it.**
- I wrote `validators.py`, `prompts.py`, `gateway.py` and `bench/run.py`.
  Claude ran the three sweeps and read the raw answers and helped in debugging
- Accepted: **one** retry, expressed with no loop anywhere in the code, so a
  retry chain is structurally impossible rather than merely discouraged.
- Accepted: a terminal provider error is never retried, because every tier
  shares one credential and would fail identically.
- **Rejected, and this one mattered:** Claude ran a `git merge` to main and wrote
  a commit with its own attribution trailer. I stopped it and had it undone. From
  that point the working rule is that Claude gives me commands and I run them 
  no commits, merges or pushes on my behalf. It is my name on this work and my
  repository history.
- Evidence: `logs/gateway/runs/2026-09-17T015116-sprint4-run.jsonl` and the
  matching results file; `FINDINGS.md` section 7.

**What I understand now, and what I still do not.**
- Understood, and it reversed my expectation: **there were zero wrong-but-valid
  answers** across 24 fixtures. The two graded wrong are errors in my own answer
  key. Retries recover malformed answers and flaky providers; they do not fix
  wrong answers, because a wrong answer looks fine to every free check.
- Understood: escalations were 8% of requests and **23% of the spend**  an
  escalated request costs about 3.2x a normal one, so the retry rule is a
  cost decision, not just a reliability one.
- Understood: the cost ladder is not monotonic. On a trivial prompt the strong
  model answered for 20% *less* than the cheap one, because cost follows how
  much a model says, and the crossover is around five output tokens.
- Not understood at the time: whether zero wrong-but-valid survives more
  fixtures, and how to grade the 8 open-ended ones at all. That became Sprint 5.
- Not verified: the provider's usage console against my logged costs.