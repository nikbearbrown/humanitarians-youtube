# Frictional log - 2026-11-06

**AI Debt Tracker, week 4 · extraction · Reading debt announcements into cited facts**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to `docs/reader.md`,
`docs/reader_truth.md`, `docs/triage.md`, `docs/handcheck.md`, `docs/worklog.md`,
`manifests/week4_gate.json` or `logs/RUN_LOG.md` in the project.

---

## What I was working on

Week 3 found the debt news. Week 4 was about reading it: turning a filing into structured
instruments (amount, currency, coupon, due year, and whether it is a new issue, an amendment or a
repayment), with every value traceable to the words it came from. The design's rule from week 1 is
that the model never types a number. It points; code parses.

Three things came first, carried from week 3: two answer-key defects (P38, P39) and a fresh
held-out check; two triage rule weaknesses and a fresh triage check; then the event reader and the
two baselines it is measured against, B1 (regex rules) and B2 (one model call per document, the
model typing each value).

As in week 3, I handed the whole week to Claude before it started: "Do all the work for next week.
I dont want to be involved in it so complete everything end to end." Everything below was done
under that instruction, and I have not reviewed it yet.

## What I tried, and what I expected

The week 4 check was set in the design in week 1: the reader must beat B1 on field accuracy on the
labelled documents. The labelled documents are the 24 debt-relevant filings from week 3's triage
set. Their 66 instruments were labelled before any of the three methods ran, and the label file has
the same hash before and after the runs. As a machine check on that reading, all 51 labelled new
bonds with a coupon and a year appear in the next quarterly report's XBRL with the same coupon and
year, and the labelled principal agrees on 19 of 19 where the key states one in the same currency.

The reader was developed only on the week 1 bake-off documents that are not in the evaluation set:
three rounds, then frozen, then run once on the 24.

The expectation built into the design was that pointing would be more accurate than letting the
model type numbers, because it removes made-up figures.

## Where it resisted, and what I did next

**The reader passed, and the baseline did better.** The reader got 157 of 167 fields right (94%),
B1 got 84%, so the check passes. But B2, the model simply typing the numbers, got 160 of 160. On
these documents (mostly pricing term sheets and prospectus covers from large issuers) a 4B model
reads numbers reliably. So the expectation was wrong for this set: the reader's gain is not
accuracy. It is that every number it reports has a sentence behind it, and B2's numbers do not.

**The copy check caught something real.** For Alphabet's euro notes the model "copied"
$1,500,000,000 where the filing says €1,500,000,000. It rewrote the currency sign while claiming to
copy. Because those words are not in the passage, the values were refused. Eight of the 24 refused
copies were currency signs like that; the other 16 were the word "null" written as text, a
bookkeeping bug with no effect on any score, fixed in code afterwards. A refused value is missing
rather than wrong, which is the trade the design asked for.

**Three reader defects were left in place.** The currency sign problem; a "$500 million term loan
facility" sentence that scored below the passage threshold, so one filing had no passages at all;
and a blank preliminary prospectus where the model listed the company's table of existing notes as
if they were new. Fixing them against the 24 filings would turn the evaluation set into a
calibration set, so they go to week 5.

**The fresh triage check failed.** The two week 3 weaknesses were fixed, and 50 new filings were
labelled before triage ran. It found 8 of 9 debt filings, below the 95% line. The miss is an IBM
euro prospectus whose cover is blank even where the year's "20" should be, so the week 3 fix for
blank covers did not fire, and the rule then read "Preferred Stock" in its contents as a share
sale. Logged as P46, not tuned away. Nine positives is a small check. One of the four false alarms is
probably a labelling error: an Applied Digital earnings release does announce a $150 m financing,
and the label missed it. Labels are not changed after a run. One document also turned out to be in
both labelled sets, filed twice under two co-issuers (P45).

**The answer key failed its fresh check again.** After the P38 and P39 fixes, week 3's set agrees 3
of 3, but that is now a calibration. Five fresh reports, drawn by seed: 1 of 5 agree. Four new
defects, each in a different company's tagging (P41 to P44). One slip in the process: the key's
totals for those five reports were printed once before the transcriptions were written. It is
disclosed beside the result.

## What Claude contributed, and what I did with it

Claude Code did the week end to end, at my request: the fixes, the held-out draw and the five
transcriptions, the fresh triage labels, the reader truth, the event reader, both baselines, the
runs, the reports, the design document and worklog updates, and the figures and script for this
video. The test suite stands at 146 offline tests, all passing.

The triage labels, the reader truth and the transcriptions are a model judgment, and each file says
so. They came from Claude, a different model from the one being tested, but not from a person.

What I did with it:

- **I delegated the week before it started**, and did not review the labels, the truth or the
  results.
- **The safeguards from earlier weeks still applied.** The pass lines were fixed in the design
  before any of this ran, sets were drawn by seed before reading, labels and truth were written
  before the runs, and defects found by a fresh check were logged rather than fixed against it.
- **I did not clear the gate.** `manifests/week4_gate.json` records the week as DELEGATED, not
  CLEARED, and records that the fresh triage check failed. Whether that failure blocks week 5 is a
  decision for whoever reviews it.

Nothing this week has yet been accepted, changed or rejected by me. That review is the open step,
for week 3 as well as week 4.

## What I understand now, and what I still do not

**Understood.** Pointing at the source is not automatically more accurate; on easy documents it is
slightly less. Its value is that it fails safe: when the model writes a number that is not in the
filing, the number is refused instead of used. A fresh check keeps finding things the previous one
did not (four answer-key defects, a blank-cover variant the last fix missed), which is what a fresh
check is for. And passing the check a week was set is not the same as being the best option measured
that week.

**What I still do not know.**

- **Whether the labels and the truth are right.** No person has read them.
- **Whether the reader holds on harder documents.** 62 of the 66 instruments were new notes in
  pricing documents; loans, amendments and redemptions were 4.
- **Whether triage can reach 95% on a fresh set** once P46 is fixed. That needs a third fresh check.
- **Whether the answer key is right beyond the reports checked.** 1 of 5 on the fresh set, with
  P41 to P44 open.
- **Whether the pieces work together.** The reader is not yet connected to a ledger; whole
  quarters running end to end is week 5.
