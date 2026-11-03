# FACTCHECK-SHORT: Take Away Days (the Short)

Status: checked against the final, Gate P signed `short/SHORT-SCRIPT.md` (all 7 lines, 142 words) and the compiled master, 2026-10-17. Sources are the long film's result files in this folder (`RESULTS.md`,
`match-rates.json`, `cluster-rates.json`, `sqrt-rule.json`, all from our own code, seed 2701) plus arithmetic re-run on 2026-10-17. Every figure is
the long film's, so the long film's `FACTCHECK.md` rows apply too.

Verdicts: **OK**, **OK-ROUNDED** (after the rounding stated), **FRAMING** (a characterisation to keep honest).

| Line | Spoken | Source value | Verdict |
|---|---|---|---|
| S01 | twenty three people; two share a birthday | n = 23 | OK |
| S02 | "about half the time" (on screen: 50.7%) | even days, exact P(23) = 0.5073; 400,000 simulated groups agree | OK-ROUNDED |
| S03 | "keep the group at twenty three" | the group *size* is held; the probabilities are for random groups of 23, not for the dots shown | OK. The dots are an illustration and are labelled "Not data" |
| S03 | ninety days, "ninety five percent" (on screen: 95.4%) | even days within a 90-day window P(23) = 0.9540; real weights 0.9544 | OK-ROUNDED |
| S03 | one month, "almost certain" (on screen: above 99.99%) | 30-day window: P(23) = 0.99999441 (28 to 31 days all above 99.999%) | OK. "Almost certain" is a characterisation of 99.9994% |
| S04 | "not the people, we kept them" | group size held at 23 | OK |
| S04 | uneven birthdays "move it a tenth of a point" | real calendar 50.79–50.84% vs even days 50.73%: 0.06–0.11 point; inside windows 0.01–0.09 point | OK. "A tenth of a point at most" is the long film's wording; here "a tenth of a point" is rounded up from 0.06–0.11, so the on-screen row says "+0.1 point at most" |
| S04 | "it's how many days there are" | 12% to 99% (people), 50.7% to 50.8% (evenness), 50.8% to 95.4% (days) in the long film | FRAMING from those numbers |
| S05 | "square root of the days, times one point two, add a half" | rule: round(1.2 √d + ½), round halves up; `sqrt-rule.json` | defined here |
| S05 | (on screen) "checked for every day count from 2 to 2,000" | exact for 1,161 of 1,999, one off for the other 838, never more | OK; do not say "always exact" |
| S06 | "a year needs twenty three people" | rule 23, exact 23 (365 days, even odds = at least 50%) | OK |
| S06 | "one month needs seven" | rule 7, exact 7 (30 days) | OK |
| S07 | "That's why it's twenty three" | the rule gives 23 for 365 days | OK |
| S07 | "The full video shows three things you could change, and the one that decides it" | describes the long film's structure (people, evenness, days) | OK |

## Claims that need care

1. **The same dots.** The scene moves one set of 23 dots as the calendar narrows. That is a device, not a result: each probability is for a random group of
   that size. The on-screen source line says so.
2. **"One month"** is a 30-day window with equally likely days (28 to 31 days all give above 99.999%). It is a calculation, not a claim about a real group.
3. **Equal days** are assumed in S03, S05 and S06. The real-calendar difference is the S04 row.
4. **The rule** is an approximation; the Short states it as a rule and shows its check range, not as a law.

## Sources and licences

Our own simulations and calculations; the one external input is the US federal births-by-day counts (NCHS 1994 to 2003; SSA 2000 to 2014) via the
`fivethirtyeight/data` repository, repository licence CC BY 4.0, credited on the S04 source line and in the description. No third-party images, text, footage or music; fonts are EB Garamond and Inter (open licence).
