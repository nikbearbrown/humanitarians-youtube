# GATE P — `data-contract-simulation`

**Reel:** "Prove The Number Changed."
**Skill:** `cli-explainer` (build reel — prompt → real code → moving output)
**Voice:** Kokoro `am_onyx` (Onyx) · Teardown register · first-person Hussain intro
**Source:** `mdhussainshariff/Mycroft` → `Data_Quality_Agent/` — the data contract
agent, and the metric-impact simulation added on branch
`feature/metric-impact-simulation` (commit `4469968`).

---

## What this reel teaches

One insight, stated once: **a schema change can compile, run, pass every test, and
still return a number that is wrong — and the only honest way to warn about it is to
rebuild the marts and measure.**

The reel earns that by walking the actual build: the agent could already prove *which*
models read a changed column (structural lineage), which is not the same as knowing
*what the number becomes*. The new layer closes that gap.

## Why the two-cycle structure is the pedagogy, not decoration

The REVISION LAW asks for a check-and-change cycle. Here the revision is not a
contrivance — it is the real design problem the feature had to solve:

- **Cycle 1** replays the migration and every model that reads the dropped column
  fails to compile. That is the *loud* half. It is also useless: the deterministic
  layer already proved it, and any CI run would have caught it.
- **Cycle 2** is the insight. Nobody merges a red pipeline. A reviewer mechanically
  renames the column in the staging model and moves on — and *that* is the state in
  which MRR is silently 100× low. So the simulation has to build twice to have
  anything to say.

A viewer who only sees cycle 1 learns the wrong lesson (that the tool finds compile
errors). Cycle 2 is where the reel's title is earned.

## Claim ledger (DOUBLE-CHECK / NO FABRICATION)

| On screen | Status | Source |
|---|---|---|
| `amount_cents → amount` with `/100.0` backfill | real | `fixtures/migrations/0003_subscriptions_amount.py` |
| staging keeps `amount_cents / 100.0 AS amount_usd` | real | `mock-analytics/models/staging/stg_subscriptions.sql` |
| 4 models fail to build as-is | real, measured | `as_is_failures` — stg_subscriptions, fct_mrr, fct_revenue, dim_users |
| post-fix: 0 failures, `fct_mrr` ×0.01 | real, measured | `test_scenario2_mrr_is_100x_low_after_the_mechanical_fix` |
| row count unchanged | real, measured | `test_scenario2_row_count_is_unchanged` |
| `108,176.33 → 1,081.76` | real | Phase-1 seeded ground truth, `Data_Quality_Agent/README.md` |
| patch scoped by lineage; `transactions.amount_cents` untouched | real | `test_scenario2_leaves_unrelated_marts_alone` |
| B03 / B06 code | real, trimmed | `contract_agent/simulate.py` (ACTUAL-CODE LAW) |

**Declared worked example:** the dollar figures come from the project's own
deterministic seed, not from a production system. The `×0.01` ratio — which is the
actual claim — is invariant to the data and is asserted in the test suite.

**Nothing dating the video:** no model version numbers on screen beyond the composer
chip, no drifting counts.

## Spine check (cli-explainer, 16:9)

| Beat | Act | Required by spine |
|---|---|---|
| B00 | INTRO | cold open, ask lands answered ✅ |
| B01 | PROBLEM | stakes before the build ✅ |
| B02–B04 | CLI → CODE → OUTPUT | cycle 1 ✅ |
| B05–B07 | CHANGE → CODE → OUTPUT | the revision ✅ (REVISION LAW) |
| B08 | SUMMARY | ✅ |
| B09 | NEXT STEPS | handoff prompt, read aloud ✅ (HANDOFF LAW) |
| B10 | OUTRO | title restate ✅ |

Output beats B01/B04/B07/B08 are bespoke Remotion motion, never stills
(SHOW-DON'T-TELL). No two share a visual scheme (ILLUSTRATE LAW).

## Narration, in full

- **B00 INTRO** — Hi, I am Hussain, and this video is about a data contract agent I built, and the feature I shipped into it today. It catches schema changes that compile, run, pass every test, and return a number that is simply wrong.
- **B01 PROBLEM** — Here is the shape of it. An engineer renames amount cents to amount, and divides by a hundred to match. Nothing crashes. But the staging layer was already dividing by a hundred. Monthly revenue is now a hundred times too low, and not one test fires.
- **B02 CLI** — My agent already proved which models read that column. That is not the same as knowing what breaks. So I asked for the layer that measures: build the warehouse before and after, and diff the marts.
- **B03 CODE** — This is the real code. Notice what it never does: call dbt. Every model's compiled S Q L already sits in the manifest, so it just runs it, in dependency order, against a throwaway database. A model that fails to build is the finding.
- **B04 OUTPUT** — And the first run failed. Usefully. Dropping the old column means every model that reads it stops compiling. Four go red. But that is the loud half — your build would have caught it. It tells me nothing new.
- **B05 CHANGE** — So here is the change. Nobody merges a red pipeline. A reviewer renames the column in staging and moves on, and that is exactly the state where the number is wrong. So build twice: once as it is, then again with the reviewer's fix.
- **B06 CODE** — Two things to verify. Pass one records what breaks. Pass two applies the rename and measures from there. And the patch is scoped by lineage, not by name — transactions has its own amount cents column, and a find and replace would have corrupted a second metric.
- **B07 OUTPUT** — Now the second run. Everything compiles. Nothing is red. And monthly recurring revenue reads one hundredth of what it read before. The warning is a number now, not a hunch.
- **B08 SUMMARY** — Three layers, each earning its place. The deterministic layer proves structure. The language model reads intent. The simulation measures damage. And the row count never moved — which is exactly why schema tests sail straight past this.
- **B09 NEXT STEPS** — Your turn. Paste this into Claude Code, pointed at your own warehouse. Replay a migration you already shipped, and ask which mart totals move. The interesting answer is the one you were not expecting.
- **B10 OUTRO** — Prove the number changed.

**402 words.** At the measured Kokoro `am_onyx` rate from the two previous reels
(3.2–3.4 w/s), that lands at **≈ 2:00–2:05** — inside the sub-2-minute cut preferred
for these reels. Real durations are measured at audio generation and become the clock.

---

## VERDICT: PASS

Signed: Hussain (delegated — build authorised in-session on 2026-08-31, "create a
brutalist video … give access to all the prompts it asks for"). Narration reviewed
against the claim ledger above before audio generation.
