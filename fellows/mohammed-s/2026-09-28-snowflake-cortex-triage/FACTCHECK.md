# FACTCHECK — Cortex, In The Warehouse.

Reel: `hussain-snowflake-cortex-triage`
Checked: 2026-09-20

**Verification basis, stated plainly.** This reel was scripted from working
knowledge of Snowflake Cortex, not from a live documentation fetch in the build
session. Every claim below is deliberately restricted to *version-stable
mechanism* — what the functions are and how the execution model works — and no
claim depends on a model name, a price, a benchmark, a region list, or a
capability that ships and un-ships. Anything that would date the video was cut
before scripting (DOUBLE-CHECK LAW).

**Before publishing, re-check the four ✅ rows against `docs.snowflake.com`.**
They are stable, but they are the only load-bearing factual claims in the reel.

| # | Claim on screen / in narration | Verdict | Rests on | Fix applied |
|---|---|---|---|---|
| 1 | `SNOWFLAKE.CORTEX.SENTIMENT`, `SUMMARIZE`, and `CLASSIFY_TEXT` are SQL-callable functions | ✅ stable | Documented Cortex LLM function surface | Used the fully-qualified `SNOWFLAKE.CORTEX.*` form rather than newer unqualified aliases, which are the names most likely to churn |
| 2 | `SENTIMENT` returns a score in the range −1 to +1 | ✅ stable | Documented return contract | Narration says "minus one to plus one" and the B06 bars are drawn on that scale |
| 3 | `CLASSIFY_TEXT` selects from a caller-supplied label set | ✅ stable | Documented signature takes the categories as an argument | B05 shows the label array inline so the viewer sees the set is theirs |
| 4 | Inference runs inside the Snowflake boundary; text is not exported to an external API by the caller, and existing RBAC/grants apply | ✅ stable | Core architectural premise of Cortex | Phrased as "the text never leaves the boundary" — a statement about the execution model, not a compliance or certification claim |
| 5 | Cortex LLM functions are billed by token consumption | ✅ stable | Documented credit-consumption model | **No rate, no dollar figure, and no credit number is stated anywhere** — only the directional claim that a full-table scan costs more than a filtered one |
| 6 | LLM classification is not deterministic across runs | ✅ stable | General property of LLM inference | Stated as "can classify differently", not as a measured rate |
| 7 | "40,000 support tickets" | ⚠️ illustrative | Invented scenario | Framed as *my* hypothetical table throughout ("I have 40,000…"), never as an industry statistic |
| 8 | B06's result rows (T-48119 etc., categories, sentiment values, summaries) | ⚠️ illustrative | Invented scenario | These are authored example rows for a fictional `support_tickets` table, **not** a captured query result. Noted in the component's own header comment. No real figure is asserted |

## Deliberately excluded (would date the video)

- Model names and versions available to `COMPLETE` / `CLASSIFY_TEXT`.
- Any price, credit rate, or cost-per-million-rows figure. The B09 handoff
  prompt asks the *viewer* to get that number from Claude for their own account
  and region — which is the correct place for a figure that moves.
- Region/cloud availability of specific functions.
- Cortex Analyst, Cortex Search, and Cortex Agents. Out of scope: this reel is
  deliberately "one starter use case", and naming the whole product family would
  both bloat the reel and age it.
- Any accuracy or benchmark number for LLM classification.

## Honesty notes

- The reel's judgment beat (B07) is not decoration. The three failure modes —
  per-token billing, non-determinism, unmeasured accuracy — are real and are
  stated without a counterweight, per the Teardown register.
- The B05 `WHERE` clause is load-bearing pedagogy, not filler: B07 calls back to
  it as the cost control. The query shown is the query discussed.
