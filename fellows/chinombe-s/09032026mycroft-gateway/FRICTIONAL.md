# Frictional log — Adaptive Model Routing Gateway, Sprint 2

## 2026-09-10 — connecting the three model tiers

- **Video (progress):** 
- **Drive:** https://drive.google.com/drive/folders/1pHXg01GKXl1-iEPKqCr3O4BUJwsPSCBk?usp=drive_link

- **Evidence of commit:** https://github.com/nikbearbrown/mycroft/commit/f8c80ee081c0cf1411b0dcc0592a06ec4d79a384



**What I was working on.** One piece of code that talks to all three model
sizes the same way, so cost and latency get recorded without the caller having
to remember to. Plus the first real API calls this repository has ever made 
one per tier, watched.

**What I tried, and what I expected.**
- I expected wiring up an SDK to be the routine part of the sprint, and the
  interesting part to be choosing which models go in which tier.
- I expected a successful HTTP response to mean a usable answer.
- I expected the published prices to predict what the tiers actually cost
  relative to each other: cheap = mid is 2x on paper, cheap = strong 10x.

**Where it resisted, and what I did next.**
- My first live call returned **empty text and cost money**. `max_tokens=16`,
  and `gpt-oss` spent the entire budget on internal reasoning before writing a
  single word of answer. Raised to 256.
- The strong model returned its reasoning *inline*, wrapped in `<think>` tags,
  ahead of the answer and the call **passed every check in my gate script**.
  That was the moment I stopped trusting `outcome: ok` to mean anything about
  the answer. Fixed with `strip_reasoning()` in the adapter plus a real answer
  check, and verified on a second live call.
- Worse: the gate script printed the problems it found and then **exited 0**. A
  script that reports failure with a success code is worse than no script. Now
  exits 1.
- The observed cost ratios were nothing like the sticker ratios: 1.4x where the
  price list said 2x, and 19–26x where it said 10x. The reason is that these
  models decide how much to say the strong model's reasoning length varied
  **35% run to run on an identical prompt**, and it used 245 of its 256 tokens,
  eleven from being truncated without me knowing.
- The provider publishes no per-token rate for the Llama models this repo had
  evidence of using. I could not put a number in `prices.json` that I could not
  cite, so the tiers moved to models with published prices instead. Choosing
  worse models to keep the accounting honest felt wrong at the time; it is the
  right call.
- A test still asserted the old Ollama tier after the ladder changed  it
  passed against configuration that no longer existed.
- Process: `f8c80ee` committed live calls with **no RUN_LOG entry again**, and
  also committed a `.lock` runtime sidecar that should be ignored.

**What Claude contributed, and what I did with it.**
- I wrote `adapters/`, `client.py`, `tiers.py` and the tests and claude helped
  me to debug them.I ran all six live calls myself and watched each one.
- Accepted: the client writes a logbook row *before* returning, including for
  failures, so there is no code path that answers without being recorded.
- Accepted: the provider SDK is imported lazily, so the test suite needs no
  network library installed.
- Accepted: a real 401 should produce a logged row and no crash  we tested
  that deliberately rather than hoping.
- Changed on my own reading of the output: the token budget, after seeing an
  empty answer I had paid for.
- Evidence: `logs/gateway/first-live-call.jsonl` (6 rows, $0.00138 total);
  `FINDINGS.md` section 5.

**What I understand now, and what I still do not.**
- Understood: "the call succeeded" and "the answer is usable" are different
  claims, and only the first one is free to check.
- Understood: a price list is not a cost model. What a tier costs depends on how
  much the model chooses to say, which I cannot know in advance.
- Understood: all three tiers sit behind one provider and one credential, so a
  rate limit or an auth failure takes out the whole ladder rather than
  degrading it. That shaped Sprint 4's retry rules.
- Not understood: why the same prompt produces reasoning of such different
  lengths, or how to budget tokens for that.
- Not verified: the provider's own usage console against my logged costs  the
  one check my code cannot perform on itself.
- Process lesson: a credential used in this sprint was exposed outside the
  terminal and needs rotating. Details are in the internal run log, not here.