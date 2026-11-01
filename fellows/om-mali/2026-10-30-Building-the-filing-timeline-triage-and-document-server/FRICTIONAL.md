# Frictional log - 2026-10-30

**AI Debt Tracker, week 3 · triage · Building the filing timeline, triage and document server**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to `docs/triage.md`,
`docs/triage_labels.md`, `docs/handcheck.md`, `docs/worklog.md`, `manifests/week3_gate.json` or
`logs/RUN_LOG.md` in the project.

---

## What I was working on

Week 2 built the judge. Week 3 was the agent's first real job: finding the debt news. In a
quarter, a company files dozens of announcements, and most of them are about earnings, dividends
or board changes. The agent has to find the few about bonds and loans without missing any, and
then read them in a way it can cite. That meant four pieces:

1. **Last week's leftovers.** Three answer key defects (P35 to P37) from Digital Realty's own
   tagging, and a new held-out check, because last week's held-out reports had now been read.
2. **A filing timeline** that gathers, for each quarter, the announcements (8-K), prospectuses
   (424B) and term sheets (FWP) filed before the report the quarter is graded on.
3. **Triage**, which decides which of those filings are about debt.
4. **A document server** that turns a filing into numbered pieces the agent can cite.

This week was different in one way that matters for this log. I handed the whole week to Claude
before it started, with the instruction: "Do all the work for week 3. I dont want to be involved
in it so complete everything end to end." Everything below was done under that instruction.

## What I tried, and what I expected

The pass line for triage was written into the design in week 1, before any of this existed:
triage must find at least 95% of the debt-relevant filings on a labelled set. Missing debt news is
the expensive mistake, because a bond the agent never reads is a bond it can never record. Keeping
a few extra filings only costs reading time. So the check is on recall, and precision is reported
beside it rather than used as the pass line.

The check was set up so that it could not be fitted to the result. 50 filings were drawn by a
fixed seed, 30 at random and 20 from filings containing any debt word, and labelled against a
written definition **before** triage ran. The labels file has the same hash before and after the
run.

For the answer key, the same rule as last week applied. Week 2's three held-out reports found the
three defects, so after fixing them they became calibration. Five fresh reports were drawn by seed
before reading and graded once.

## Where it resisted, and what I did next

**The fresh held-out check did not pass cleanly.** Last week's three reports now agree 3 of 3, but
that is a calibration. Of the five fresh reports, Cipher Mining and TeraWulf had no debt at those
dates, so there was nothing to grade and they are not counted. Of the three that remained, **1
agreed** (Dell, totals exactly). Super Micro's key counted the banks' over-allotment option on a
convertible as a second bond (P38). Core Scientific's small notes have no due date anywhere in the
XBRL (P39). Both were diagnosed and left open on purpose. Fixing them against the reports that
found them would turn next week's check into another calibration. The check also caught a mistake
by the checker: a Super Micro coupon was transcribed from the notes' original terms, which were
amended in 2025. It does not change the verdict.

**A company's debt is often not filed by the company.** Equinix's euro notes, for example, are
issued through a financing subsidiary with its own SEC number. The timeline gathers filings for
the company and its issuing subsidiaries, and removes co-filings that would otherwise be counted
twice. Across the development quarters that came to **593 filings: 469 8-Ks, 94 prospectuses and
30 term sheets.**

**Most filings never needed a model.** Five plain rules decide **394 of 593**: a new-obligation
item on an 8-K, a prospectus cover selling notes rather than shares, a term sheet, a debt headline,
and no debt words at all. Only the doubtful **199 (34%)** go to the local `qwen3:4b`, at a median
of 3.1 seconds each. **184 are kept**, 163 by rule and 21 by the model.

**The first full run crashed.** One model answer ran past its token limit and came back as broken
JSON. Dropping that filing would have been the expensive kind of mistake, so an unreadable answer
now keeps the filing and flags it for the reader. The whole pool was rerun from the start, and
nothing from the crashed run was scored. In the final run, 1 answer did not parse and was kept.

**The check found a bug in last week's work.** The first version of the report showed 21 of 22 of
Week 2's announced bond changes kept by triage. The missing one was not a triage miss. Week 2's
search had matched "0%" inside "escalates 20%" and credited a 0% 2031 convertible to an earnings
release. That is now P40, fixed, and the result is **22 of 22**.

**The result.** On the 50 labelled filings:

- debt filings found: **24 of 24** (recall; the pass line was 95%)
- kept filings that are about debt: **24 of 26** (an Alphabet share mini-tender, not notes, and a
  TeraWulf acquisition)
- event type right: **20 of 24**

**Some of the model's evidence is not word for word.** For 8 of the 21 filings the model kept, the
quote it gave as evidence was not found in the text it was given. The check compares the first 80
characters, so a paraphrase fails it as well as an invention. The filings are still kept, and the
event reader built next will have to re-check every fact against the document.

**Two rule weaknesses were left in place.** While labelling, two cases showed up that the rules
handle badly: `Item1.01` written without a space, and a prospectus cover with the coupon and year
left blank. Fixing them against the labelled set would flatter the next check, so they are carried
to a fresh triage check on filings outside these 50.

## What Claude contributed, and what I did with it

Claude Code did the week end to end, at my request. It fixed P35 to P37, drew and transcribed the
five fresh held-out reports, built the timeline, the document parser and store, the document
server and triage, labelled the 50 filings, ran triage, wrote the reports, the design document
updates and the worklog, and made the figures and narration script for the video. The test suite
stands at 123 offline tests, all passing.

The labels and the held-out transcriptions are a model judgment, and each file says so. The labels
came from Claude, a different model from the one being tested, but not from a person.

What I did with it:

- **I delegated the week before it started**, and did not review the labels, the transcriptions
  or the results while the work was done.
- **The safeguards I had set in earlier weeks still applied.** The pass line was fixed in the
  design in week 1. The held-out sets are drawn before reading. The frozen test files refuse to be
  overwritten. The gate needs a named human.
- **I did not clear the gate.** `manifests/week3_gate.json` records the week as **DELEGATED, not
  CLEARED**, because no person has reviewed it. Clearing it means reading `docs/triage.md` and
  `docs/triage_labels.md`, then logging the decision with a name and a date.

Nothing in this week has yet been accepted, changed or rejected by me. That review is the open
step.

## What I understand now, and what I still do not

**Understood.** The protections from earlier weeks are what made it possible to hand this week
off. A pass line fixed in advance, held-out reports drawn before reading, labels written before
the run and frozen files enforced in code all held without anyone watching. They do not replace
the human gate, though. A model labelled the check set and a model did the work, so the result is
a measurement, not a review. A 100% recall is also easy to over-read. It is 24 of 24 positives in a
50-filing sample, and it sits beside a lower precision and a lower event-type score. And a check
can find bugs upstream as well as in the thing it checks: the triage check found one in last
week's search.

**What I still do not know.**

- **Whether the 50 labels are right.** No person has read them yet.
- **Whether triage holds outside the labelled set.** 24 positives is a small check, and the two
  rule weaknesses are still in place. Week 4 runs a fresh triage check.
- **Whether the 8 unmatched quotes are paraphrases or inventions.** The event reader has to answer
  that by re-checking every fact against the document.
- **Whether the answer key is right beyond the reports checked.** The fresh check agreed on 1 of 3,
  and P38 and P39 are still open.
- **Whether the agent can read the filings it is given.** It still cannot turn a filing into
  structured debt events. That reader is Week 4.
