# Frictional log - 2026-11-13

**AI Debt Tracker, week 5 · orchestration · Running full episodes from filings to ledger**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to `docs/episodes.md`,
`docs/triage.md`, `docs/reader.md`, `docs/handcheck.md`, `docs/worklog.md`,
`manifests/week5_gate.json` or `logs/RUN_LOG.md` in the project.

---

## What I was working on

Weeks 1 to 4 built the pieces one at a time: an answer key, a do-nothing baseline (B0), triage,
and an event reader. Week 5 was about running them together. For one company and one quarter, the
agent should go from the filings in the window to a ledger of the company's bonds: list the
filings, keep the ones about debt, read each one, merge what was found, retire bonds that have
matured, apply the rest to the opening ledger, and check the result. The design's check for the
week: full episodes run end to end on the development quarters, and the first bond-level recall
and precision.

Before that came last week's leftovers: four answer-key defects (P41 to P44) and a fresh
hand-check; two triage weaknesses (P45, P46) and a third fresh triage check; three reader defects
and a fresh check of the reader.

As in weeks 3 and 4, I handed the whole week to Claude before it started: "Do all the work for
next week. I dont want to be involved in it so complete everything end to end." Everything below
was done under that instruction, and I have not reviewed it yet.

## What I tried, and what I expected

The graph is built with LangGraph: a timeline node, triage, one reader branch per relevant filing
(a `Send` fan-out, so they run at the same time), then the ledger engine and the self-checks, with
every step checkpointed. The ledger engine is plain code: it merges events that describe the same
bond, sweeps matured bonds by the same rule B0 uses, and applies new issues, add-ons and
redemptions. Anything it cannot place (a repayment of a bond it does not hold, a new bond with no
maturity) becomes an open question rather than a guess.

The opening ledger is borrowed from the answer key, exactly the one B0 carries forward. That was
deliberate: with the same starting point, any difference from B0 is what reading the filings
added. Reading the opening ledger itself is next week.

I expected recall to rise, because reading is the only way to see a new bond, and precision to
hold.

## Where it resisted, and what I did next

**Recall rose; precision did not hold.** On the 45 quarters graded bond by bond, recall went from
90.9% to 97.8%, and the tracker caught 30 of the 34 new bonds that carrying forward cannot see.
But precision fell from 92.8% to 90.2%. Every bond it added in those quarters was checked against
the report: 40 are real, 26 are not. The 26 are three kinds: existing notes read from a prospectus
as if new (10), launch announcements that state no coupon yet and so cannot be merged with the
priced bond that follows (10), and the banks' option to buy more read as a bond of its own (4).
Two more were misreads. They are logged as P56 to P58, not fixed against this run.

**The first run had a timing bug.** The window runs up to the day the target report is filed,
weeks after the quarter ends, and the engine applied everything in it, so bonds sold after the
quarter end landed in that quarter's ledger. The design keeps the ledger by settlement date. I
fixed it on development data (only events filed by the quarter end are applied) and re-ran from
the saved readings. Both runs are reported; the first had precision 89.2%. Filing date stands in
for settlement until settlement dates are parsed, so a bond priced in the last days of a quarter
can still land on the wrong side.

**The laptop ran out of memory.** Midway through, the model server and the episode run were
stopped because the machine was low on memory. I said "resume it", and they were restarted one job
at a time with the model server limited to one model and one slot. The checkpoints and saved
readings meant nothing was redone.

**A setup slip.** Installing LangGraph first went into a mistyped folder outside the repo (the
shell dropped the backslashes in the path). It was reinstalled in the right place; the two stray
folders are mine to delete.

**The fresh checks mostly held.** Triage, after the two fixes, found 15 of 15 debt filings on a
third set labelled before the run (last week 8 of 9). Fifteen positives is still small: one miss
would have been below the line. Two of its three false alarms are new rule weaknesses (a tender
for shares read as a debt tender, a share term sheet that mentions notes), logged as P53 and P54.
The reader read 91% of fields on fresh filings against 74% for regex; asking the model directly
read 96% but reported 15 instruments that are not in the filings, and none of its numbers has a
sentence behind it. The answer key agreed on 3 of 4 gradable reports; TeraWulf's total is tagged
in a way the key does not read (P47).

**Running out of companies.** Only 2 of the 25 companies had never been hand-checked, so the
held-out draw had to be extended before drawing: three of the five fresh reports are from companies
checked before, in other quarters.

## What Claude contributed, and what I did with it

Claude Code did the week end to end, at my request: the fixes, the fresh draws and labels, the
transcriptions, the ledger engine, the self-checks, the ledger MCP server, the LangGraph graph, the
runs, the reports, the design document and worklog updates, and the figures and script for this
video. The test suite stands at 166 offline tests, all passing.

The triage labels, the reader truth, the transcriptions and the diagnosis of the 26 wrong
additions are a model judgment, and each file says so. They came from Claude, a different model
from the one being tested, but not from a person.

What I did with it:

- **I delegated the week before it started**, and did not review the labels, the truth or the
  results. My one decision during the week was to resume the runs after the memory stop.
- **The safeguards from earlier weeks still applied.** Sets were drawn by seed before reading,
  labels and truth were written and hashed before the runs, and defects found by a fresh check were
  logged rather than fixed against it. The one fix made after seeing results (the timing bug) was
  made on development data, and both runs are reported.
- **I did not clear the gate.** `manifests/week5_gate.json` records the week as DELEGATED, not
  CLEARED.

Nothing this week has yet been accepted, changed or rejected by me. That review is the open step,
for weeks 3, 4 and 5.

## What I understand now, and what I still do not

**Understood.** Reading the filings pays off exactly where the design said it would: new bonds.
But a system that adds things will add some wrong things, and precision is where that shows. The
wrong additions are not random; they fall into three kinds that the merge step can recognise. And
a pipeline is only as good as its sense of time: the first run's mistake was not a misread but a
bond put in the wrong quarter.

**What I still do not know.**

- **Whether the labels, the truth and the diagnosis are right.** No person has read them.
- **How much of the gain survives a real opening ledger.** Every quarter started from the answer
  key's ledger; reading it from the filings is next week, and it will add its own errors.
- **Whether the merge fixes for P56 to P58 cost recall.** A rule that drops launch notices could
  also drop a real bond announced only once.
- **What happens to repayments.** The tracker caught 3 of 14 removed bonds; 24 repayments matched
  nothing in the ledger and are open questions for the investigators.
- **Whether any of this holds on the test split**, which has not been touched.
