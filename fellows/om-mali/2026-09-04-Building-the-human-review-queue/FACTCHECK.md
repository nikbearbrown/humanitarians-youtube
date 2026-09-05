# Fact-check gate — building-the-human-review-queue (week 6)

Every number spoken or shown was checked against `figdata_week6.json`, which
`scripts/make_week6_figures.py` in the project repo queries from Postgres at build time and
dumps before anything is drawn. **Rows 6, 12, 18 and 19 are the ones to read before signing.**

Verdict types, as in weeks 1, 2, 4 and 5:

- `EXTERNALLY VERIFIABLE` — open the named filing on EDGAR and read the numbers.
- `REPRODUCIBLE` — re-run the committed query/script against the project database.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, run, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | 5,806 holdings, and every one has a decision | B00/B02/B09 | REPRODUCIBLE | `figdata.holdings` = `figdata.decided` = **5806**. Asserted at injection; the build fails if they diverge. |
| 2 | 4,537 resolved unaided — 78.1% | B00/B01/B02/B09 | REPRODUCIBLE | `figdata.auto_holdings` = **4537**; the percentage is derived at injection, never typed. |
| 3 | 1,269 stopped and waited for a person — 21.9% | B00/B01/B02/B09 | REPRODUCIBLE | `figdata.human_holdings` = **1269**. 4537 + 1269 = 5806, asserted. |
| 4 | Why they stopped: 925 split, 300 new company, 28 unresolved, 16 band | B02 | REPRODUCIBLE | `figdata.by_trigger` minus `auto`. The four sum to 1269, asserted. Narration says "most of those were suspected splits" — 925/1269 = 73%. |
| 5 | 42 cards, 8 actual questions | B00/B03/B04/B06/B09 | REPRODUCIBLE | `figdata.review_cards` = **42**, `len(figdata.review_groups)` = **8**. The 8 groups' cards sum to 42 and their holdings sum to 1269; both asserted. |
| 6 | **45 recorded decisions, each carrying a human name and a written reason — and the code rejects one missing either** | B01/B09 | AUTHOR-ASSERTED — **read this one** | `figdata.review_rows` = **45** and `figdata.reviewer` = "Om Mali" are in the data. That the code *rejects* a decision missing a name or a reason is a claim about the author's own implementation, not something the figure proves. It is also **the central claim of the whole project**, so it is the line most worth a reviewer's scepticism. |
| 7 | X.AI Corp arrives under 24 different spellings, 278 holdings | B03/B04/B09 | REPRODUCIBLE | `figdata.xai_spellings` — 24 entries summing to 278, matching the `review_groups` entry for X.AI Corp (24 cards, 278 holdings). Both asserted. Every string on screen is rendered verbatim as filed. |
| 8 | Some of those spellings share an issuer name and differ only in the security title | B03 | REPRODUCIBLE | Three rows share `X.AI HOLDINGS CORP` and differ only in title (`SER C PC PP`, `CLASS A P/P`, `SER B PC PP`). The README records that the figure showed three identical rows until the titles were added — which "reads as a data error rather than as the point". The injection asserts that duplicate names exist, so the titles cannot be dropped again. |
| 9 | 3 of the 8 questions are keyed at company level | B04 | REPRODUCIBLE | `figdata.company_level_keys` = **3**. The other five are single cards. Stated on screen so "one answer clears 24" is not over-generalised into "every question works this way". |
| 10 | `interrupt()` writes the entire graph state to Postgres | B05/B09 | AUTHOR-ASSERTED | A description of the author's own graph. No artifact in `figdata_week6.json` proves it; the evidence is the behaviour in rows 11 and 12. |
| 11 | Paused in one process, answered in a completely separate one | B05/B09 | AUTHOR-ASSERTED | The author's own test. Reproducible in principle by anyone with the repo; not captured in the figure data. |
| 12 | **The database server crashed, and all 42 questions were still there** | B06/B09 | AUTHOR-ASSERTED — **read this one** | The strongest beat in the reel and the weakest evidence in it: **n = 1, and it happened by accident.** The beat says so on screen. It is not a durability guarantee and the cut does not present it as one. |
| 13 | Perplexity: 6,081 shares → 60,810 shares | B07/B09 | EXTERNALLY VERIFIABLE | `figdata.perplexity`, two period ends (2025-12-31, 2026-03-31). The injection asserts the second balance is exactly ten times the first. |
| 14 | The filed value did not move: $4,228,993.75 at both period ends | B07/B08/B09 | EXTERNALLY VERIFIABLE | `figdata.perplexity[*].value_usd`, identical to the cent, asserted. The README records an earlier query rounding this to $4,228,994 before it reached a decision rationale — the unrounded figure is what makes the point. |
| 15 | Implied price 695.44 → 69.54, i.e. a naive −90% | B07 | REPRODUCIBLE | `figdata.perplexity[*].price`. The −90% is derived at injection from the two prices, not typed, and is shown struck through as the reading the queue prevented. |
| 16 | SpaceX's ten-times step is two share classes on the same day | B08/B09 | EXTERNALLY VERIFIABLE | `figdata.spacex_same_day`: 2023-10-31, asset category **EC** at $81 (16 holdings) and **EP** at $810 (15 holdings). The injection asserts both categories are present and the period ends match. |
| 17 | Anthropic's jump is an ordinary funding round, ×4.0 over one quarter — NOT a ten-times step | B08 | REPRODUCIBLE | `figdata.anthropic_step`: $12.18 on 2023-10-31 → $48.94 on 2024-01-31, sitting inside a 33-point `anthropic_series` with no offsetting share-count change. |
| 18 | **Three suspected-split questions, not four — so wrong two times out of three, not three out of four** | B08 | REPRODUCIBLE — **read this one** | `figdata.review_groups` filtered to `trigger == "split"`: **3 questions, 9 cards, 925 holdings**. The README records the prose saying four and "wrong three times out of four" until the figures were counted. The injection asserts the count, and the on-screen ratio is **derived from it** rather than typed, so the corrected number cannot drift back. |
| 19 | **28 holdings belonged to nothing at all — a deliberate canary** | B02/B09 | REPRODUCIBLE (data) + AUTHOR-ASSERTED (the canary) — **read this one** | `figdata.rejected`: two Cohere Technologies preferred series, 14 holdings each = **28**, matching the `unresolved` trigger and the `not_in_universe` review group. That it was **planted two months ago as a deliberate test** is the author's claim about their own repo history, and the reel states the finding without leaning on the plant. |
| 20 | How each holding was finally decided: alias 2,760 · LEI 1,681 · human 1,269 · fuzzy 57 · SPV 39 | B02 | REPRODUCIBLE | `figdata.by_method`, whose `questions` sum to `figdata.questions_total` = **231**. Rendered from the array; the human row is the only one in terracotta. |

## What this cut deliberately does NOT claim

- **The AI did not decide anything.** The README calls this "the one thing not to get wrong on
  camera". B01 makes it the whole beat: `route`, `group`, `present` land as chips, and
  `decide` lands and is struck through.
- **The matcher is not finished.** 78% is what it resolves unaided; the other 22% needed a
  person, and the cut frames that as the design working rather than a shortfall.
- **One crash is not a durability guarantee.** Row 12. B06 says it on screen: the only test of
  its kind, and it was run by accident.
- **No claim that every question collapses.** Row 9 — 3 of 8 are company-level keys; the rest
  are single cards, and the screen says so.
- **No valuation claim** anywhere, consistent with weeks 1, 2, 4 and 5.

## Wording changed from the script, and why

| Script | This cut | Why |
|---|---|---|
| "resolved four and a half thousand of them" | "four thousand five hundred and thirty-seven" | The exact figure is short enough to speak and it is the one on screen. Rounding it invites the viewer to check the round number against the precise one and find a mismatch. |
| The second opening paragraph (re-explaining the project) | trimmed to one sentence | The script's own note nominates this as the first cut: "the project gets re-explained every week and this one has plenty to say without it." Kept the one clause that frames the week — which company a filing is talking about. |
| "wrong three times out of four" *(earlier project prose)* | "wrong two times out of three" | Row 18. The corrected count, and the on-screen ratio is derived from the asserted question count rather than typed, so it cannot regress. |
| "the same fund reports common stock at eighty-one dollars and preferred at eight hundred and ten" | same, plus the period end on screen | Spoken, "on the same day" is a claim; on screen the shared `2023-10-31` is the evidence for it. |
| "Three price steps looked identical — a price falling by exactly ten" | "Three price steps tripped the same split detector" | **The three are not the same magnitude.** Perplexity and SpaceX are ×10; Anthropic's step is `12.18 → 48.94` = **×4.0**. The rendered beat labels each magnitude, so the original line contradicted its own frame. What the three actually share is the detector that flagged them, which is also the real point. Caught by reading the render, not by any gate. |

## Before publishing

Rows 6, 12, 18 and 19 are the four a reviewer is most likely to challenge, and two of them are
the author's own assertions about their repo rather than anything the figures prove — row 6
because it is the project's central claim, row 12 because it is the most memorable moment in
the reel and rests on a single accident. Everything else traces to `figdata_week6.json` under
an assertion. Publishing remains a separate, explicitly authorized step.
