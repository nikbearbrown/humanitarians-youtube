# Fact-check gate — building-the-answer-key-grader-and-baseline (AI Debt Tracker, week 2)

Every number spoken or shown is a prop injected from `figdata.json` by `build_beat_sheet.py`
under assertions. Nothing is typed into a scene. `figdata.json` transcribes the author's own
saved results as published in `pantry/*.svg` and in `narration_script.md`'s source table; each
bar's geometry in those SVGs was recomputed as a ratio and had to agree with its printed
fraction before the value was accepted.
**Rows 5, 8, 9, 12, 14 and 17 are the ones to read before signing.**

Verdict types, as in every earlier episode:

- `REPRODUCIBLE` — re-run the committed query/script against the AI Debt Tracker repository.
- `EXTERNALLY VERIFIABLE` — open the named filing or report and read it.
- `AUTHOR-ASSERTED` — a fact about the author's own plan, repo, run, or decision.

| # | Claim | Beat | Verdict | Source |
|---|---|---|---|---|
| 1 | An answer key over 1,093 reports from 100 companies — 25 AI, 75 others | B00/B01/B09 | REPRODUCIBLE | `answer_key/index.json` ← `scripts/build_answer_key.py`; `docs/answer_key.md`. The injection asserts 25 + 75 = 100. |
| 2 | 9,653 bonds, every quarterly and annual report Jan 2024 – Sep 2026 | B00/B01/B09 | REPRODUCIBLE | Same source. The date range is a property of what was downloaded, not a claim about completeness of EDGAR. |
| 3 | 900 reports list debt bond by bond, 41 by deal, 152 totals only | B01/B09 | REPRODUCIBLE | `answer_key/index.json`. The injection asserts 900 + 41 + 152 = 1,093, so **B01 can draw them as one partitioned bar the width of the whole key** rather than three bars that would invite 900 to be compared with 41. It also asserts 900 is a majority, because the narration says "most". |
| 4 | The agent never sees the answer key | B01 | AUTHOR-ASSERTED (design) | `DESIGN.md`. A property of how grading is defined, not a measurement. B01 carries it on the frame. |
| 5 | **The agent does not exist** | B00/B02/B08/B09 | AUTHOR-ASSERTED — **read this one** | Week 2 built the answer key, the grader and the baseline. The reader-and-ledger agent is unwritten. A reel full of scores reads as a reel about a working system unless it says otherwise, so this is said in B00, written on B02's subtitle, and is B08's last row. |
| 6 | A bond matches only if currency, interest rate (to 0.01 pt), due year and amount (within 1%) all agree | B02/B09 | REPRODUCIBLE | `src/ai_debt_tracker/eval/grader.py`. Four fields, asserted at injection. |
| 7 | Each true bond can be claimed by at most one answer | B02/B09 | REPRODUCIBLE | Same file. The constraint that stops one correct answer being counted against several bonds; B02 gives it its own block because a viewer would not guess it. |
| 8 | **Every score carries a 95% bootstrap interval** | B02/B05/B08 | REPRODUCIBLE — **read this one** | Same file. This is why 90.7% is reported as 87.5–93.5% in B05 and B08 rather than as a point. A single number from 47 quarters would be read as precise. |
| 9 | **The grader agreed with only 8 of 10 printed tables on the first pass, and all 5 disagreements were bugs in the grader** | B00/B03/B09 | EXTERNALLY VERIFIABLE (the tables) / AUTHOR-ASSERTED (the attribution) — **read this one** | `docs/handcheck.md`, `manifests/handcheck/*.json`. The tables are printed in real 10-Qs and 10-Ks and can be opened. **That every disagreement was the grader's fault is the author's own finding**, and it is the honest centre of the reel. The five are named on camera with the company that exposed each. |
| 10 | The five bugs: repaid notes counted (Oracle), two bonds in one entry (AMD), acquired debt dropped (Broadcom), due dates read as issue dates, currency never stated (Equinix) | B03/B09 | REPRODUCIBLE | `docs/handcheck.md`, DESIGN.md P30–P34. The injection asserts there are exactly five, and B03's own label counts them rather than stating a literal. |
| 11 | 10 of 10 after the five fixes | B04/B09 | REPRODUCIBLE | Same source. See row 12 — this number on its own is not evidence. |
| 12 | **10 of 10 is a CALIBRATION; 2 of 3 on untouched reports is the measurement** | B04/B08/B09 | REPRODUCIBLE — **read this one** | The same ten reports found the bugs, so the grader cannot help but agree with them afterwards. The three held-out reports were picked before reading and graded once. **This is the reel's framing assertion**: the build fails if the held-out score ever catches up with the calibrated one, because the distinction B04 draws would then be empty. DESIGN.md P35–P37. |
| 13 | The one held-out miss is that company's own tagging errors, kept for next week | B04/B08 | AUTHOR-ASSERTED | `docs/handcheck.md`. The claim is that the miss was diagnosed and recorded, not that it was fixed — explicitly "rather than tuned away", which is the point. Three reports is a small check and B04 says so on the frame. |
| 14 | **The do-nothing baseline caught 0 of 36 new bonds** | B00/B05/B06/B09 | REPRODUCIBLE — **read this one** | `docs/baseline_b0.md` ← `scripts/score_baseline.py dev`. Copying last quarter forward cannot, by construction, produce a bond that was not there before; the zero is the measurement confirming it over 47 real quarters. **B05 draws it as an outlined, labelled EMPTY track** — an absent bar reads as a rendering fault, which this series has shipped before. |
| 15 | 90.7% bond recall (87.5–93.5%), 18 of 47 quarters exact | B05/B08/B09 | REPRODUCIBLE | Same source. 90.7% is high for the same reason the zero is zero: most debt does not move in a quarter. The reel never presents it as a target to beat, and B05 places it **beneath** the zero at smaller size. |
| 16 | 30 of 32 new bonds were announced in a filing the agent could read in time | B06/B08/B09 | REPRODUCIBLE | `docs/changes_dev.md` ← `scripts/explain_changes.py`. "Could read in time" means published before the report being graded on — the point-in-time rule from week 1. |
| 17 | **30 of 32, not 30 of 36** | B06/B08 | REPRODUCIBLE — **read this one** | Four of the 36 new bonds carry no tagged interest rate, so there is nothing to search a filing for. 32 is the searchable denominator and the injection asserts 36 − 4 = 32. Saying "thirty of thirty-six" would overstate the miss rate; saying "thirty of thirty-two" without the footnote would hide four bonds. Both numbers are on the frame. |
| 18 | 5 of 6 early repayments announced | B06/B09 | REPRODUCIBLE | Same source. Of 16 bonds that disappeared, 9 reached their due date and 1 had no rate to search for, leaving 6. The injection asserts 16 − 9 − 1 = 6. |
| 19 | EDGAR moved 43 of 495 filing timestamps by 4–5 hours | B07/B08 | REPRODUCIBLE | `logs/RUN_LOG.md` (2026-10-23), DESIGN.md P29. Two reads of the same filings returned different publication times. 43 of 495, not all of them. |
| 20 | "Most likely a time-zone change" | B07/B08 | AUTHOR-ASSERTED (inference) | The shift is 4 hours on summer dates and 5 in winter, matching US Eastern to UTC. **EDGAR published no note**, so this is an inference and B07 says the word on the frame. The consequence — anchoring each cut-off to the report rather than to a clock — holds whatever the cause was. |

## What this cut deliberately does NOT claim

- **No claim that the agent exists.** Row 5. Week 2 built its judge.
- **No claim that 10 of 10 is an accuracy score.** Row 12 — it is a calibration on the reports
  that found the bugs, and the measured figure beneath it is 2 of 3.
- **No claim that the held-out check is large.** Three reports. Said on camera and on the frame.
- **No claim that 90.7% is good.** Row 15 — it is what doing nothing scores, and it hides a zero.
- **No claim that the baseline is a straw man.** It is the floor every tracker must clear, and
  it clears most of the task because most of the task is unchanged debt.
- **No claim that 30 of 32 means the agent will find 30.** Those bonds were announced in a
  readable filing; reading them is the work that has not been done.
- **No claim about why EDGAR's timestamps moved.** Row 20 — an inference, labelled as one.
- **No company valuation, and no view on whether any company's debt is too much.** This project
  records what was borrowed, not whether it was wise.

## Wording changed from the script, and why

| Script | This cut | Why |
|---|---|---|
| "It still finds ninety point seven percent of bonds … but it caught none of the thirty-six new bonds" | the zero **first**, then 90.7% | Row 14. Said in the script's order, a listener hears a 90% system with a caveat. B05 draws the empty track before either flattering number appears. |
| "After fixing all five, ten of ten." then "I also graded three untouched reports" | the same two numbers, with "**so ten of ten is a calibration, not a score**" between them | Row 12. The script's Notes make exactly this point; this cut puts it in the voice and draws a rule between the two groups on the frame. |
| "thirty of thirty-two new bonds" | kept, with 36 and the 4 untagged bonds on the frame | Row 17. The script's Notes require the explanation; the figure's footnote carries it so the voice does not have to. |
| "most likely a time-zone change" | kept verbatim, plus "EDGAR published no note" on the frame | Row 20. "Most likely" in the voice is easy to miss; the frame names it an inference. |
| — (the script's closing section is on camera) | B08, a limits beat, with the three next steps inside it | Every episode in this series ends on its own limits. The content is from the script's Notes and its closing section. |

## Before signing

Rows 4, 5, 9 (the attribution half), 13 and 20 are the claims this reel makes that
`figdata.json`'s measured block does not contain. Each is passed as a named constant or stated
as a design property, and each beat that uses one says on the frame where it came from.
