# Fact-check gate — measuring-a-local-llm-against-the-matcher (week 5)

Every number spoken or shown was checked against `figdata_week5.json` (generated from the
cached model replies by `scripts/make_week5_figures.py` in the project repo), `README.md`,
or `narration_script.md`. **Rows 3, 9, 13 and 18 are the ones to read before signing.**

Verdict types, as in weeks 1, 2 and 4:

- `EXTERNALLY VERIFIABLE` — open the named filing on EDGAR and read the numbers.
- `REPRODUCIBLE` — re-run the committed query/script against the cached artifacts.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | An eight-billion-parameter model, running locally | B00/B01/B02/B09 | REPRODUCIBLE | `figdata.run`: `llama3.1:8b`, `parameter_size` **8.0B**, `quantization` Q4_K_M, `host` http://localhost:11434, `machine` Windows AMD64. The injection asserts the parameter size. |
| 2 | The run is deterministic and schema-constrained | B02/B09 | REPRODUCIBLE | `figdata.run`: `temperature` **0**, `seed` **7**, `schema_constrained` **true**, `digest` 46e0c10c039e0191. Asserted at injection. Re-running should reproduce the same replies. |
| 3 | **The model was offered 11 candidate companies — 7 universe + 4 watchlist, not 7** | B02 | REPRODUCIBLE — **read this one** | `figdata.prompt_example.candidates` = **11**. `README.md` records this as a correction: the prose said 7 until the figures were generated. It matters because Scale AI and X.AI are both **watchlist** names, and the model's three worst answers all promote holdings to exactly those two. Asserted at injection. |
| 4 | 322 calls, zero failures, ~3.2 seconds each | B02/B09 | REPRODUCIBLE | `figdata.throughput`: `calls_measured` 322, `errors` **0**, `mean_seconds_per_call` 3.236, `median` 3.205, `slowest` 3.669. Asserted at injection. |
| 5 | About 17 minutes for the full golden set | B02 | REPRODUCIBLE | `figdata.throughput.seconds_for_full_golden_set_llm_only` = 1042.1s = 17.4 min, rendered as "17 min". Derived at injection, not typed. |
| 6 | Both systems see the same four fields | B02 | REPRODUCIBLE | `figdata.prompt_example` carries exactly `issuer_name`, `issuer_title`, `filer`, `candidates`. The on-screen row is a real one (HYPERSCALE DATA INC, Vanguard) — the same row B04 then dissects. |
| 7 | Price and the answer were withheld from both | B02 | AUTHOR-ASSERTED | `prompt_example` contains no price field and `truth` is not in the prompt payload (`system_chars` 1482, `prompt_tokens` 583). The claim that this parity was deliberate is the author's. |
| 8 | The rules: 0.9959 precision. The model: 0.9449 | B00/B01/B03/B09 | REPRODUCIBLE | `figdata.scoreboard.B_matcher_v1.macro.precision` and `.C_v2_band.macro.precision`. Spoken as "ninety-nine point six" and "ninety-four point five". Both asserted at injection. |
| 9 | **Five points, and one wrong record becomes 196** | B00/B01/B03/B09 | REPRODUCIBLE — **read this one** | Macro is per NAME; micro is per HOLDING. `B_matcher_v1.micro.fp` = **1**, `C_v2_band.micro.fp` = **196**. The 196 is not 196× the same error — it is 14 wrong names carrying 196 holdings between them. The beat says "a case is a name and a name can carry hundreds of holdings" on screen so the ratio cannot be misread as a multiplier. Both values asserted. |
| 10 | Recall did not move | B01/B03/B09 | REPRODUCIBLE | `macro.recall` = **1.0000** for both systems; `micro.recall` = 1.0000 for both. Nothing was lost; things were added. Asserted at injection. |
| 11 | The precision drop is −5.1 points | B01 | REPRODUCIBLE | `figdata.lift.C_v2_band.precision` = **−0.051**. Rendered as "−5.1 points", derived at injection. |
| 12 | Every error ran one way: 14 added, 1 removed | B01/B08/B09 | REPRODUCIBLE | `figdata.band_changes`: `promotions` 14, `broke` 14, `fixed` **1**, `changed` 15 of `consulted` 85. Asserted at injection — the direction is the entire basis for the veto policy in B08. |
| 13 | **"Hyperscale Data is the parent company of Scale AI" is the model's verbatim reason, and it is false** | B04/B09 | REPRODUCIBLE (quote) + AUTHOR-ASSERTED (rebuttal) — **read this one** | `figdata.failures[0].reason`, quoted verbatim on screen and struck. The *quotation* is reproducible; the claim that no such parent relationship exists is the author's own knowledge assertion and is the one line in the reel that no committed artifact proves. Reported at `confidence` **0.95**, `truth` NOT_IN_UNIVERSE, 1 holding. |
| 14 | Scaled Agile: also Scale AI, at confidence 1.000, 32 holdings | B05/B09 | REPRODUCIBLE | `figdata.failures[1]`: `SCALED AGILE INC. 2021 UNITRANCHE TERM LOAN`, said `Scale AI, Inc.`, reason "the issuer name and title match the name of Scale AI, Inc.", confidence **1.0**, holdings **32**. Asserted at injection. |
| 15 | XAI3-FT5O.AF: an internal security code, called X.AI at confidence 1.000, 8 holdings | B06/B09 | REPRODUCIBLE (data) + AUTHOR-ASSERTED (what the code IS) | `figdata.failures[2]`: name and title identical, said `X.AI Corp`, confidence **1.0**, holdings **8**, truth NOT_IN_UNIVERSE. That the string is an **internal Fidelity security code** rather than a ticker is the author's identification, per the script's own note; the *three matching characters* (X, A, I) are counted on screen. |
| 16 | The three shown failures are all rows where nothing should have matched | B04/B05/B06 | REPRODUCIBLE | All three carry `truth` = NOT_IN_UNIVERSE. Asserted at injection. This is why the flattering hardest-cases number is excluded — see below. |
| 17 | Confidence 1.000 on 315 of 322 answers | B00/B07/B09 | REPRODUCIBLE | `figdata.confidence.at_full` = **315**, and independently `figdata.dots` contains 322 entries of which 315 carry `confidence` 1.0. The injection asserts BOTH and that they agree. `README.md` records that the prose said 308 until the dot figure disagreed with it. |
| 18 | **12 of the 15 disagreements came back at 0.95 or higher** | B00/B07/B09 | REPRODUCIBLE — **read this one** | `figdata.confidence`: `disagrees` **15**, `disagrees_at_95_plus` **12**. From `dots`: 8 disagreements at 1.000, 4 at 0.95, 3 at 0.0. This is the finding that kills the stated plan for next week's review queue, and it is the reason to check it hardest. Asserted at injection. |
| 19 | The model only ever returned three confidence values | B07 | REPRODUCIBLE | `figdata.confidence.distinct_values` = [1.0, 0.95, 0.0] — three values across 322 different questions. Rendered from the array, not typed. |
| 20 | Veto-only scores 1.0000 — on 4 rows | B08/B09 | REPRODUCIBLE | `figdata.scoreboard.F_v2_veto.macro` precision **1.0**, fp **0**; `figdata.veto_rows` has exactly **4** entries, of which exactly **1** is vetoed (OPEN BAY AUTOS AI INC., claimed OpenAI, truth NOT_IN_UNIVERSE). Both asserted at injection. `figdata.lift.F_v2_veto.precision` = +0.0041. |

## What this cut deliberately does NOT claim

- **The flattering hardest-cases number is not on screen and not spoken.** The script's own
  note is explicit: on the hardest-cases subset every model policy scores a perfect 100%,
  *because that subset excludes the rows where nothing should match* — and those are the only
  rows the model damages. Quoting it would be true and misleading at once. It is recorded
  here instead.
- **No claim that AI cannot do this.** One model, one size, one quantization, one prompt.
  `figdata.run` documents exactly which. A larger model might clear the bar; none was tried,
  and B08's "decent sceptic, poor proposer" is scoped to this run. This is an open question
  and the reel says so rather than generalising.
- **No claim the veto policy is validated.** B08 puts the sample size at the same visual
  weight as the score and says a perfect result on four rows is not evidence.
- **No claim about latency being acceptable or unacceptable.** 3.2s per call and 17 minutes
  for the set are reported as measured facts, without a verdict attached.
- **No valuation claim** anywhere, consistent with weeks 1, 2 and 4.

## Wording changed from the script, and why

| Script | This cut | Why |
|---|---|---|
| "Same three hundred and twenty-two test cases I built last month" | "the same 322 labelled names" | DOUBLE-CHECK LAW: strip anything that dates the video. Week 4 shipped the same month, so "last month" is both datable and slightly wrong. Same referent (the week 4 golden set). |
| "a hundred and ninety-six" (records), unqualified | same, plus an on-screen line: "a case is a name and a name can carry hundreds of holdings" | Without the unit stated, 1 → 196 reads as a 196× multiplier on one error. It is 14 wrong names carrying 196 holdings. The spoken line is unchanged; the screen carries the qualifier. |
| "So a model allowed only to veto scores perfectly — on four rows. Four." | same, plus "A perfect score on four rows is not evidence" on screen | The spoken beat already carries the irony. The written caveat makes it unmissable to a viewer who screenshots the 1.0000. |
| Veto row names, in full (up to 138 characters) | shortened at the exposure clause, with the truncation disclosed in the on-screen source line | Rendered in full they cross the right title-safe edge and overprint the notes beneath — the exact BLOCKER week 4 hit at B08. The trailing-space distinction between rows 3 and 4 survives as a row note rather than being silently collapsed. |

## Before publishing

Rows 3, 9, 13 and 18 are the four a reviewer is most likely to challenge. Row 13 is the only
line in the reel whose rebuttal rests on the author's own knowledge rather than a committed
artifact — if the parent-company relationship were real, B04 would be wrong and the beat
would have to go. Everything else traces to `figdata_week5.json` under an assertion.
Publishing remains a separate, explicitly authorized step.
