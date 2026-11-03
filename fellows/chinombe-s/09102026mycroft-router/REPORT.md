# Sprint 3 — Task policy, router, and a frozen test set

- **Week:** 7–11 Sep 2026 · logged 2026-09-10
- **Project:** Mycroft — Adaptive Model Routing & Inference Gateway
- **Evidence of commit:** https://github.com/nikbearbrown/mycroft/commit/68bbeb5d1ee5b7e53bd283d17dc516024a2b5589

- **Video:** https://www.youtube.com/watch?v=MiWZyDMCR50
- **Drive:** https://drive.google.com/drive/folders/1xOoXuHBwvOA8mb8O3YAUd3hiCSPezVJB
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **This week's explainer:** [Paged Attention](../09102026paged-attention/)

## What this sprint was for

The first two sprints could record a request and make one. This sprint decides
**which tier a request should start on**  and builds the hand-labelled test set
that any such decision will eventually be judged against. The labels were set
before a single model had been run on the fixtures, on purpose: a test set
labelled after you have seen the results is labelled to fit them.

No live calls, no API key.

## What was built

| File | What it does |
|---|---|
| `policy.json` v0.1.0 + `policy.py` | Six task types, locked. Each names its output kind, its validator, the tier it starts on, the tier it may escalate to, and the per-tier token budget. |
| `router.py` | A pure function of task type and input length. Returns a tier and a one-sentence explanation of why. |
| `bench/fixtures.py` | Loads and validates the fixture set; refuses to freeze while any label is unreviewed. |
| `bench/label.py` | Interactive labelling, one fixture at a time. Deliberately never shows the router's choice. |
| `bench/audit.py` | Coverage report and the freeze command (SHA-256 per file). |
| 24 fixtures + `manifest.json` | Frozen 2026-09-10. |

96 tests passing.

## Results

**Six task types, each tied to evidence already in the repository:** sentiment
classification, topic classification, structured extraction, contradiction
detection, summarization, and RAG answering. Every type cites the files it was
derived from, and a test fails if any of those paths stops existing.

**The router is deliberately simple.** Input length is measured in **characters,
not tokens**, because token counts depend on the model and the router must not
need a model to make its decision. An unknown or pinned task type raises rather
than falling back to a default  a silent default is how a request ends up on
the wrong model permanently.

**The break-even rule was left out on purpose.** Routing cheap only when the
cheap model's expected quality justifies it is the actual idea behind this
project, and it needs measured pass rates. It is reserved for Sprint 8, so that
the simple router exists first as a baseline for the clever one to beat.

**24 fixtures, 4 per type, 2 easy and 2 hard, fictional companies.** Labeller
tiers: cheap 6, mid 11, strong 7. The router chose cheap 8, mid 16, strong 0.

**The router agreed with the labels on 9 of 24**  and the router was not
adjusted to close that gap. The labels are predictions, not measurements; tuning
the router to agree with a guess would make Sprint 7 measure nothing.

## Decisions taken, and why

**The fixtures are synthetic, not real, which the sprint plan did not intend.**
There is no real request corpus in this repository: 203 of 217 sample payloads
are generic placeholders, the market-sentiment sample declares itself synthetic,
and the mock transactions file holds zero records. Rather than pretend
otherwise, every claim this project makes is scoped to *how models handle these
task types*  not to Mycroft's real traffic mix.

**`expected_tier` means the cheapest tier the labeller expects to get it right.**
A judgment, explicitly not the router's rule applied by hand.

**Task types and routing rules live in one file** so they cannot drift apart.

## Evidence

- `scripts/gateway/bench/manifest.json`  24 fixtures, SHA-256 per file, frozen
  2026-09-10
- `scripts/gateway/FINDINGS.md` section 6  what the first fixture set showed
- `logs/RUN_LOG.md`, entry dated 2026-09-10
- Commands: `bench/label.py --by "Simba"`, `bench/audit.py --freeze`,
  `python -m pytest scripts/gateway/tests -q` (96 passed)

## Limits and open items


- One labeller, no agreement measure  the first real check on these labels is
  Sprint 6.

