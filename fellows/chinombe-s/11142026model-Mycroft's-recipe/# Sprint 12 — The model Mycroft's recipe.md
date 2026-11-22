# Sprint 12 — The model Mycroft's recipes name cannot be bought

**Week:**  9-14Nov 2026 · 
**Project:** Mycroft — Adaptive Model Routing & Inference Gateway
**Repository:**(https://github.com/nikbearbrown/mycroft/commit/f7981c7922dc83a51a6042dd381f2614b965e2e4)

- **Video:** TO FILL
- **Drive:** (https://drive.google.com/drive/u/1/folders/18Qh0yaNu-Y_naWIw3ht5mMRL_ECXiovd)
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Commit:**(https://github.com/nikbearbrown/mycroft/commit/f7981c7922dc83a51a6042dd381f2614b965e2e4)

## What this sprint was for

Sprint 11 replayed Mycroft's only real model requests — 16 of them, prepared by
the contradiction-detection agent and never sent — and found two reasons the
gateway could not serve them. They name a model with no rate in the price
table, and each asks for 2,000 output tokens against a budget of 512. This
sprint was meant to clear both.

## What was found

**The missing price is not missing. It does not exist.**

| model | published price | max completion tokens |
|---|---|---|
| **llama-3.3-70b-versatile** | **Contact Sales** (Enterprise tier) | 32,768 |
| openai/gpt-oss-20b (cheap) | $0.075 / $0.30 per 1M | 65,536 |
| openai/gpt-oss-120b (mid) | $0.15 / $0.60 per 1M | 65,536 |
| qwen/qwen3.8-27b (strong) | $0.80 / $4.00 per 1M | 16,384 |

Checked against Groq's own model documentation on 17 November. The model every
one of those requests names is sold on an Enterprise tier, with "Contact Sales"
where a per-token rate would be. There is no number to add to the table.

**The recipe may not be able to run at all.** An Enterprise-only model on a
developer-plan key is likely to be refused outright — independently of the
gateway, and before any routing decision is reached. The owner of
`contradiction-detection-agent` does not know this yet, and it matters more
before their approval gate clears than after.

**2,000 output tokens is not a model limit.** The cheap tier's model permits
65,536 completion tokens. The 512 that would truncate all 16 requests is a
policy budget I set, not a capability ceiling. What the work actually needs is
still unmeasured.

**A limit blamed on the model belongs to the account.** Sprint 4 recorded a cap
of 1,000 output tokens per minute and set the strong tier's budget to 896
because of it. The published developer-plan limit is 250,000 tokens per minute.
The cap is real but it is a property of this account's plan. The budget stands;
the reason given for it was wrong and has been corrected in the record.

**All three tier prices were unchanged** after two months. Re-stamped with
today's reading date rather than re-derived.

## What was built

| Change | Why |
|---|---|
| `prices.json` version 2026-11-17 | Re-read prices; `llama-3.3-70b-versatile` recorded as `unpriced` with its reason, max completion tokens added for every model |
| `prices.py` — `unpriced` entries | The refusal now quotes the reason. It previously told callers to "add it to prices.json with a source URL", which sends them after a figure that cannot be obtained |
| `prices.py` — stricter validation | An entry with neither rates nor a reason is now rejected. That silent middle state is exactly how a missing price becomes a zero |
| `prices.py` — `entry()` | Lets a caller read the note without triggering an exception, so a tool can report *why* rather than just *failed* |
| `tests/test_prices.py` | Six new cases, including that the shipped table refuses the model Mycroft's recipes name, and explains itself |

**238 tests passing.** No calls made, nothing spent.

## What this sprint did not settle

- **What a contradiction review actually emits.** One live call with a generous
  budget decides whether 2,000 tokens was measured or inherited. Deliberately
  deferred to Sprint 13 rather than rushed to close this one.
- **Whether an Enterprise model is callable on this key.** One request to the
  provider's model-list endpoint would answer it.
- **A priced equivalent.** If the recipe must move off Llama, the nearest
  priced model is the mid tier's `gpt-oss-120b`. Nothing has tested whether it
  does that job as well.

## Evidence

- `scripts/gateway/FINDINGS.md` section 16
- `logs/RUN_LOG.md`, entry dated 2026-11-17
- Source: https://console.groq.com/docs/models, read 2026-11-17

## Next

Sprint 13 measures what the work needs, and offers the contradiction-detection
agent a gateway-backed path for when its gate clears —
[the following work folder](../11232026mycroft-recipe-adoption/).
