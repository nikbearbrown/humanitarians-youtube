# Frictional log - 2026-11-20

**AI Debt Tracker, week 6 · agent start · Reading the opening ledger instead of borrowing it**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to `docs/agent_start.md`,
`docs/opening_reader.md`, `docs/handcheck.md`, `docs/triage.md`, `docs/worklog.md`,
`manifests/week6_gate.json` or `logs/RUN_LOG.md` in the project.

---

## What I was working on

Week 5 ran whole quarters end to end, but with two crutches. Every quarter started from an opening
ledger borrowed from the answer key (oracle start), and the merge step added 26 bonds that were not
in the report. Week 6 was about removing the first crutch and fixing the second. The design's check
for the week: measure the gap between a borrowed start and a read one (ablation A4), and measure how
often the self-checks notice when an episode ends wrong (the self-catch rate).

Last week's leftovers came first: the three merge fixes (P56 to P58), two triage false alarms (P53,
P54), two answer-key findings (P47, P49), and loans, where the size of a new facility is not debt
until it is drawn.

As in weeks 3 to 5, I handed the whole week to Claude before it started: "Do all the work for next
week. I dont want to be involved in it so complete everything end to end." Everything below was done
under that instruction, and I have not reviewed it yet.

## What I tried, and what I expected

The merge fixes are code: a launch notice with no coupon folds into the priced bond that follows it,
a bond named with no amount becomes a question instead of an addition, and the banks' option is
recorded but not added. I expected precision to recover without costing recall.

The opening-ledger reader follows the same rule as the event reader: the model points, code reads.
Code finds the tables that look like a debt note; `qwen3:4b` names the rows that are one bond or loan;
code reads every value from the cited cell and the row's own label. I expected it to be close to the
answer key on companies with clean debt tables, and to struggle on the messy ones.

Investigators were meant to answer the questions the engine raises: a bond with no amount, a bond
with no maturity, a repayment of a bond the ledger does not hold. I expected them to close a good
share of the 53 questions from last week.

## Where it resisted, and what I did next

**The merge fixes worked.** On the same readings, the wrong additions fell from 26 to 3 and precision
rose from 90.2% to 93.3%, level with carrying forward, with recall unchanged at 97.9%. The three
additions left are not yet diagnosed.

**The opening reader had two code defects on its first pass.** Salesforce prints a header with one
cell per column, and the reader took the last number in each row, the coupon, as the amount. Super
Micro's caption was cut by the parser before "(in thousands)", and a total came out in billions.
Both were fixed on development data, every report was re-read, and both passes are reported. After
the fix: recall 89.7%, precision 98.8% on 94 reports; without the model, 83.8%.

**The model does not answer the same way twice.** The first pass had stored only the first 3,000
characters of each model answer, so nine long answers could not be reused and were asked again.
Broadcom's January 2025 report gave 36 matching bonds the first time and 22 the second. That
variance is part of what the reader is, and it is now reported rather than averaged away.

**Reading the start costs recall.** Agent start against oracle start, the same 45 quarters: recall
90.1% against 97.9%, 7.9 points lower; precision 95.5% against 93.3%, higher, because fewer bonds
held means fewer held wrongly. Most of the gap is a few companies. The total debt is the weakest
number: within 2% on 26 of 79 quarters at agent start, against 44 at oracle start.

**The point-in-time rule said no.** Four opening reports, Core Scientific's amendments and two late
Super Micro reports, were filed so close to the report being predicted that the agent may not read
them (P60). That is the rule doing its job, and it is counted in the gap rather than worked around.

**The investigators did less than I hoped.** They settled 21 of 67 questions. Nineteen were bonds named with
no amount that the merge step had already kept out of the ledger: dropping one confirms the ledger
rather than changing it. Two were repayments matched to a held bond on a looser key. No graded bond
changed. All 24 maturity questions stayed open, because the passages the
model pointed at gave no due date. The real answers are in older filings, which the investigators do
not search yet.

**The laptop ran out of memory again.** Midway through, the model server and the opening-ledger run
were stopped. I said "resume it", and they were restarted one job at a time with one model and one
slot. The 73 readings saved before the stop were reused.

**The fresh hand-check mostly held.** Five reports drawn by seed before reading: 4 of 5 agree.
Alphabet's euro notes are keyed at their dollar carrying amount, logged as P59 and not fixed against
the set that found it. Last week's TeraWulf disagreement now agrees after the P47 fix.

**No fresh triage set this week.** The two triage fixes only remove false alarms, and the re-run kept
every labelled set at full recall. But all three sets are now calibrations, and that is stated.

## What Claude contributed, and what I did with it

Claude Code did the week end to end, at my request: the fixes, the fresh draw and transcriptions, the
opening-ledger reader, the investigators, the three episode runs, the reports, the design document and
worklog updates, and the figures and script for this video. The test suite stands at 182 offline tests,
all passing.

The hand-check transcriptions are a model judgment, and each file says so. Which table rows are
instruments, and which passage states a missing value, are `qwen3:4b`'s judgments, flagged in every
record. Every number in a ledger was parsed by code.

What I did with it:

- **I delegated the week before it started**, and did not review the transcriptions or the results. My
  one decision during the week was to resume the runs after the memory stop.
- **The safeguards from earlier weeks still applied.** The held-out set was drawn by seed before
  reading and graded once; the defect it found was logged, not fixed against it. The fixes made after
  seeing results (P61) were made on development data, and both passes are reported.
- **I did not clear the gate.** `manifests/week6_gate.json` records the week as DELEGATED, not
  CLEARED.

Nothing this week has yet been accepted, changed or rejected by me. That review is the open step, for
weeks 3 to 6.

## What I understand now, and what I still do not

**Understood.** The borrowed start was hiding a real cost, and now it has a number: about eight points
of recall. The cost is concentrated, not spread evenly. A few hard debt tables account for most of it,
so it can be worked on. And a check that cannot see a missing bond cannot flag it: a third of the wrong
episodes were flagged, and I do not yet know how many of the rest any check could have caught.

**What I still do not know.**

- **Whether the transcriptions and results are right.** No person has read them.
- **How much of the reader's variance is noise.** One re-ask moved Broadcom by 14 bonds. One run per
  report cannot say how often that happens.
- **Whether investigators that search older filings would close the 15 unknown repayments**, or whether
  those bonds were simply missed by the opening reader.
- **Why total debt is so often off at agent start**, even where the bonds are right.
- **Whether any of this holds on the test split**, which has not been touched.
