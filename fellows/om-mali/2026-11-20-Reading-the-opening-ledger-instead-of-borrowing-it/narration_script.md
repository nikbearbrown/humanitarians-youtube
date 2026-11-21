# Reading the opening ledger instead of borrowing it — narration script

**AI Debt Tracker, week 6**

**Target:** 2:00–2:15 · 305 spoken words
About 2:02 at 150 words per minute, 2:11 at 140. Steady, unhurried — let each number land. Spoken forms are written out below where they differ from what's on screen.

The story of this week: last week the tracker started every quarter from a ledger borrowed from the answer key. This
week it reads that ledger itself, and the cost of doing so is measured. First, the wrong bonds it added last week are
mostly gone.

---

### 0:00 — Opening · on camera

> Hi I'm Om Mali. This video is about my AI debt tracker reading its own starting ledger from a company's last report,
> instead of borrowing it from the answer key, and measuring what that costs. This is week 6 of the AI Debt Tracker.

*Shot: straight to camera.*

---

### 0:15 — The merge fixes · cut to `adt-w6-merge.png`

> Last week the tracker added twenty-six bonds that weren't there. Three kinds of mistake: old notes read as new,
> launch notices with no interest rate yet, and the banks' option to buy more. I fixed all three in the merge step.
> On the same filings, the wrong additions fell from twenty-six to three. Precision went from ninety to ninety-three
> percent, level with the baseline, and recall stayed seven points above it.

*Shot: the two bars, then the three lines below.*

---

### 0:45 — Reading the opening ledger · cut to `adt-w6-opening.png`

> Until now every quarter started from a ledger taken from the answer key. That's cheating a little. So I built a
> reader for it. Code finds the debt table in the last report, the model points at the rows, and code reads every
> number from the cell. On ninety-four reports it found ninety percent of the bonds, and ninety-nine percent of what
> it found was right. The model's pointing also changes from run to run.

*Shot: the red recall bar, then the precision bars.*

---

### 1:20 — The week 6 check · cut to `adt-w6-gap.png`

> Then the real test: the same quarters, starting from what the tracker read. Recall fell from ninety-eight percent to
> ninety, a cost of about eight points. Most of that is a few companies: Broadcom, where it found twenty-three of about
> forty bonds in two quarters, and convertible notes it didn't find. Starting from its own reading, it is level with
> the baseline on recall, and ahead on precision.

*Shot: the recall bars, then the red line at the bottom.*

---

### 1:55 — Does it know when it is wrong? · cut to `adt-w6-catch.png`

> The last measurement: when an episode ends wrong, do the checks notice? Seventeen of fifty times. I also added
> investigators for the open questions. They settled twenty-one of sixty-seven, but changed no graded bond.

*Shot: the red bar, then "21 of 67".*

---

### 2:15 — What's next · on camera

> Next week: fixing the opening reader's misses, and investigators that search older filings.

*Shot: end card.*

---

## Notes

**"Twenty-six to three"**: the bonds added in L1 episodes that the target report does not hold. Week 5: 66 added, 40
real. Week 6, same readings, B0's opening ledger: 44 added, 41 real, 3 not. The three left are not yet diagnosed.

**"Ninety to ninety-three"**: 90.2% → 93.3%. B0 92.8%; the paired difference against B0 is +0.5 points (−0.2 to
+1.4), so say "level", not "better". Recall 97.9%, +7.0 points over B0.

**"That's cheating a little"**: the design calls it *oracle start* (ablation A4). Keep it light; it was deliberate.

**"Ninety percent … ninety-nine percent"**: the reader on 94 opening reports, L1 (43 reports): recall 89.7%, precision
98.8%. Rules alone: 83.8%, 97.9%. Two code defects were found on the first pass and fixed on dev data (P61); both
passes are in `docs/opening_reader.md`. "Changes from run to run": Broadcom's January 2025 10-Q, 36 bonds matched on one
run and 22 on the next.

**"Ninety-eight to ninety, about eight points"**: 97.9% → 90.1%, paired −7.9 points (−2.0 to −15.3). Precision went
the other way: 93.3% → 95.5%. Against B0, which still borrows its start: recall −0.9 points (−9.4 to +6.0), precision
+2.6. Total debt within 2% is the weak spot: 26 of 79 at agent start against 44 at oracle start — not said aloud.

**"Broadcom … twenty-three of about forty"**: two episodes, the opening reader found 23 instruments where the report
holds 39 and 40. Also Snowflake and Super Micro (convertible tables not found), and Core Scientific, whose opening
reports the point-in-time rule refuses (P60).

**"Seventeen of fifty"**: self-catch rate, agent start: 17 of 50 episodes that ended wrong were flagged (34%); 11 of
36 that ended right were flagged anyway. Oracle start: 16 of 39 (41%).

**"Twenty-one of sixty-seven"**: oracle start; 17 were bonds the opening ledger already held, 2 the model judged not
offered, 2 repayments matched on a looser key. All 24 maturity questions stayed open. Ablation A1: no L1 grade
changed.

**Not reviewed by a person.** The week was delegated end to end; the gate record says DELEGATED, not CLEARED. The
fresh hand-check (4 of 5) is not in the script; it is in the description.

**If you run long,** drop "That's cheating a little" at 0:45 and "The model's pointing also changes from run to run."

## Where every number comes from

| Line | Number | Source |
|---|---|---|
| 0:15 | 26 → 3 wrong additions; precision 90.2% → 93.3%; recall +7.0 over B0 | AI Debt Tracker `docs/agent_start.md` |
| 0:45 | 94 reports; recall 89.7%, precision 98.8% | `docs/opening_reader.md` |
| 1:20 | recall 97.9% → 90.1% (−7.9 points); Broadcom 23 of ~40 | `docs/agent_start.md` |
| 1:55 | self-catch 17 of 50; questions 21 of 67 settled; A1 no change | `docs/agent_start.md` |

## Figures (in this folder)

- `adt-w6-merge.png` — wrong additions 26 → 3; 21 launches folded, 25 amount-less bonds held as questions, 4 options recorded; precision 90.2% → 93.3%.
- `adt-w6-opening.png` — the opening-ledger reader on 94 reports: model + code 89.7% / 98.8%, rules only 83.8% / 97.9%.
- `adt-w6-gap.png` — oracle start, agent start and B0 on recall and precision; the −7.9-point gap.
- `adt-w6-catch.png` — self-catch 17 of 50, false flags 11 of 36, questions settled 21 of 67.

Each has an `.svg` beside it. Every number is read from the project's generated reports, and the figure build fails
if any differs from the recorded value.
