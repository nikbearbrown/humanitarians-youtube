# Building the answer key, grader and baseline — narration script

**AI Debt Tracker, week 2**

**Target:** 3:00 · ~450 spoken words (448)
About 2:59 at 150 words per minute, 3:12 at 140. Steady, unhurried — let each number land.
Spoken forms are written out below where they differ from what's on screen.

The story of this week: before building the agent, build the thing that grades it — and check
the grader itself against real printed reports.

---

### 0:00 — Opening · on camera

> Hi I'm Om Mali. This video is about building the answer key and the grader for my AI debt
> tracker, and measuring the do-nothing baseline it has to beat. This is week 2 of the AI Debt
> Tracker.

*Shot: straight to camera.*

---

### 0:15 — The answer key · cut to `adt-w2-answerkey.png`

> The tracker is graded against each company's next quarterly report, so first that answer had to
> be written down. I built it for a hundred companies — the twenty-five AI companies and
> seventy-five others to compare against — from one thousand and ninety-three reports since
> January twenty twenty-four. That's nine thousand six hundred and fifty-three bonds. Most reports
> list their debt bond by bond; some only by deal, and some only as totals. The agent itself never
> gets to see any of this.

*Shot: the three big numbers, then the bar — red, ochre, dark — as each is named.*

---

### 0:48 — The grader · stay on `adt-w2-answerkey.png`, bottom lines

> The grader scores a debt list three ways. Bond by bond, the currency, interest rate and due year
> must agree, and the amount must be within one percent — and each true bond can be claimed by
> only one answer. Then deal by deal, and then the totals. Every score comes with a confidence
> range, so a small difference is never oversold.

*Shot: the two grey lines under the legend.*

---

### 1:13 — Checking the checker · cut to `adt-w2-handcheck.png`

> But who checks the answer key? I compared it with the debt tables printed in ten real reports.
> The first pass agreed on only eight. Every disagreement was my bug, not theirs: Oracle's repaid
> notes were still counted as owed, Broadcom's debt from buying VMware had been dropped entirely,
> and three more. After fixing all five, ten of ten.
>
> Because those ten reports found the fixes, I also graded three untouched reports, once. Two of
> three agree. The miss is one company's own data-entry errors — saved for next week, not tuned
> away.

*Shot: the three bars top to bottom; then the bug list during "and three more". Pause after
"ten of ten".*

---

### 1:50 — The floor · cut to `adt-w2-headroom.png`

> Then the floor. The simplest possible tracker just copies last quarter's debt forward. It still
> finds ninety point seven percent of bonds, because most debt doesn't change in three months. But
> it caught none of the thirty-six new bonds, and got only eighteen of forty-seven quarters exactly
> right.

*Shot: open on the empty top bar ("0 of 36"), then the two numbers along the bottom.*

---

### 2:09 — The headroom · stay on `adt-w2-headroom.png`, red bars

> And the changes can be found. Thirty of thirty-two new bonds were announced in a filing the agent
> could read in time, and so were five of six early repayments. That gap is exactly what the agent
> has to win.

*Shot: the two red bars.*

---

### 2:25 — One surprise · on camera

> One surprise: EDGAR quietly moved forty-three filing timestamps by four to five hours — most
> likely a time-zone change. So the server that stops the agent seeing the future now anchors each
> cut-off to the report itself, not to a clock.

---

### 2:42 — What's next · on camera

> Next week: fix that one company's data problems, check a fresh set of reports, and start building
> the agent's document reader — the part that turns a filing into sentences it can point to, so it
> never has to type a number itself.

*Shot: end card.*

---

## Notes

**"Week 2"** is the second video of this project; the first covered the feasibility check and model
choice. Don't say "week 1" anywhere else.

**"Every disagreement was my bug, not theirs"** is the honest centre of the video — the grader was
wrong in five ways the printed reports exposed. Don't soften it.

**"Ten of ten" is a calibration, not an accuracy score.** Those ten reports were used to find the
fixes. The three untouched reports are the honest check — that's why both are said.

**"Ninety point seven percent" is bond recall on the dev quarters graded bond by bond** (47 quarters,
95% interval 87.5–93.5%). It's high because most bonds simply carry over; the point is the zero.

**"Thirty of thirty-two", not thirty-six.** Four of the 36 new bonds have no tagged interest rate to
search for, so 32 could be searched. Say "thirty-two"; the figure's footnote explains it.

**"Five of six early repayments"**: of 16 bonds that disappeared, 9 simply reached their due date,
one had no rate to search for, and 5 of the other 6 were announced.

**"Most likely a time-zone change"** is an inference (the shift is 4 hours in summer dates and 5 in
winter, matching US Eastern to UTC). Keep "most likely".

**If you run long,** drop "and some only as totals" at 0:15 and "because most debt doesn't change in
three months" at 1:50 (about five seconds together).

## Where every number comes from

| Line | Number | Source |
|---|---|---|
| 0:15 | 100 companies (25 + 75), 1,093 reports, Jan 2024 – Sep 2026, 9,653 bonds; 900 / 41 / 152 by level | AI Debt Tracker `answer_key/index.json` ← `scripts/build_answer_key.py`; `docs/answer_key.md` |
| 0:48 | currency, coupon to 0.01 pt, due year, amount within 1%, one-to-one pairing; confidence range = 95% bootstrap interval | `src/ai_debt_tracker/eval/grader.py` |
| 1:13 | 8 of 10 first pass, 5 fixes, 10 of 10; held-out 2 of 3 | `docs/handcheck.md`; `manifests/handcheck/*.json`; DESIGN.md P30–P34, P35–P37 |
| 1:50 | 90.7% bond recall; 0 of 36 new bonds; 18 of 47 exact | `docs/baseline_b0.md` ← `scripts/score_baseline.py dev` |
| 2:09 | 30 of 32 new bonds, 5 of 6 early repayments announced | `docs/changes_dev.md` ← `scripts/explain_changes.py` |
| 2:25 | 43 of 495 timestamps moved 4–5 h | `logs/RUN_LOG.md` (2026-10-23); DESIGN.md P29 |
| 2:42 | next week's plan | DESIGN.md §17 |

## Figures (in this folder)

- `adt-w2-answerkey.png` — reports, companies and bonds in the answer key; how much detail each report
  gives; the bond-matching rule.
- `adt-w2-handcheck.png` — the grader against printed tables: first pass 8 of 10, after five fixes 10 of
  10, held out 2 of 3; the five bugs.
- `adt-w2-headroom.png` — new bonds caught by copying forward (0 of 36) vs announced (30 of 32); early
  repayments announced (5 of 6); 90.7% recall, 18 of 47 quarters exact.

Each has an `.svg` beside it. Every number is read from the project's saved results, and the figure
build fails if any differs from the recorded value.
