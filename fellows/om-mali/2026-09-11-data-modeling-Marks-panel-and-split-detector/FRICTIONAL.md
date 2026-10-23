# Frictional log — 2026-09-11

**Week 6 · data modeling · The marks panel, and a detector that missed its own test case**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to
`docs/marks_panel.md`, `src/marks/` or `docs/worklog.md`.

---

## What I was working on

Turning 5,806 resolved holdings into the actual deliverable: **5,479 marks**, one row per
(security, fund, period end), each carrying `value_usd / balance` as a per-share price.

The arithmetic is one line. The week is everything that stops that line from lying — and the
spine of it is a bug I wrote myself.

## What I tried, and what I expected

Build the panel, reconcile it against the filed holdings, and detect stock splits so a 10:1
split does not enter a price series as a 90% crash.

I expected the split detector to be the easy half. Week 5 had already built a trigger with an
absolute ±0.02 window around an integer ratio, and it worked — it correctly flagged SpaceX and
Perplexity at exactly 10.0000.

## Where it resisted, and what I did next

**The split rule missed the plan's own verification case, and it looked correct while doing
it.**

Perplexity's ARK holding went 695 → 58 shares. That is a ratio of **11.93**, and a ±0.02 window
misses it by a factor of three hundred. The rule looked right only because the *other*
Perplexity step lands on exactly 10.000 — so the detector caught Perplexity, reported
Perplexity, and I believed it was working.

I found it by checking the detector against the case the plan names, rather than against the
cases the detector had already flagged. The rule is now a **relative 1% window under the same
cap of 20**, defined once in `src/marks/splits.py` and imported by the week 5 queue trigger so
the two can never disagree. It still excludes X.AI's 2.064x repricing (44 occurrences) and
still excludes the 348x `$1.00` placeholder artifact — by the cap, which was always the part
that mattered.

**And the 11.93 case is a composite, which is the better finding.** ARK's Perplexity common
went 6,081 → 60,810 shares (×10) while the value fell $4,226,522.43 → $3,542,758.43. So
**11.93 = a 10:1 split AND a 16% markdown in one period.** Week 7 divides by 10. Adjusting by
11.93 would erase a real price move — which is the mirror image of the mistake the detector
exists to prevent.

That distinction is now visible in one row of `docs/marks_panel.md`: ratio **11.9300**, factor
**10.0000**. A reader can see that the number to divide by is not the number the detector
measured.

**I adjudicated all three suspected splits myself, and the share counts settled them:**

- **Perplexity — a real 10:1 split.** Five T. Rowe Price funds show the share count multiplied
  by exactly ten with the dollar value **unchanged to the cent**: 19,395 → 193,950 at
  $13,488,132.50; 40,949 → 409,490 at $28,477,728.17; 10,496 → 104,960; 6,081 → 60,810;
  1,346 → 13,460; 98 → 980.
- **Anthropic — not a split.** ARK holds **89,078 shares in every one of thirteen periods**;
  only the value moves. The 4.02 rise to $48.94 **reverses to $30.00** the next quarter, and a
  split never reverses.
- **SpaceX — not a split.** Neuberger Berman's share counts are constant at 22,368 and 3,428
  while value doubles exactly ($4,742,016 → $9,484,032). A 2x repricing that continues to
  $526.59 the following quarter.

**Three things the data forced, each logged as a deviation from the plan:**

- **Amendments supersede.** All 16 `NPORT-P/A` filings restate a (fund, period) that already
  had an original. The panel's uniqueness constraint would otherwise have rejected the second,
  and the survivor would have been an accident of insert order. The amendment wins; 72 original
  holdings never become marks.
- **One security arrives on several lines, and sometimes those lines are not one security.**
  189 line groups inside a single filing share an issuer name and title — 464 rows. Summing is
  right for 151 of them. For the rest the lines disagree on price (SpaceX common and preferred
  filed under an identical title, ten times apart), so the mark is recorded **blended with no
  price**, keeping what the lines said rather than averaging two different things.
- **`asset_category` is part of a security's identity**, not decoration — it is the only thing
  separating SpaceX common from preferred inside one filing. But three Databricks titles say
  "Series I" and are filed `EC` by one manager and `EP` by another, so the category lives in
  `security_map` rather than in the security's key.

**A rule I wrote too strong, then narrowed.** My first detector blocked every mark of a
security whose series broke anywhere. That cost 90 further marks, including all of ARK's
Anthropic series, for a break that a change between two *other* periods never crosses. The
plan's invariant is per mark. Now the series is *flagged* and only the step is *blocked* —
different claims, different columns.

## What Claude contributed, and what I did with it

Claude wrote `src/marks/{build,splits,verify}.py`, the CLI and 19 tests, one synthetic hazard
per real defect.

**The defect that cost the reviewer a repeat was mine, and I want it on the record.**
`--factor` was accepted on the command line and **never written to the database**. Two edits I
believed were saved were lost when a patch script asserted and exited before its write, so the
`split_factor = %(factor)s` assignment and the guard requiring a factor both went missing.
psycopg2 ignores an unused named parameter without complaint — so the command succeeded,
printed a confirmation, and recorded a null factor. The verdicts, reviewers and rationales all
landed; only the factor was missing.

I fixed it **at the cause, not the symptom**: the logic moved out of the CLI into
`src/marks/splits.py::adjudicate()`, with two tests that would both have failed on the broken
version. A guard that only exists in a script is a guard nothing tests.

**Four corrections the figures forced**, all of them substance rather than layout:

- **A verification check failed because a human answered it.** `perplexity_split_blocked`
  required `NOT split_adjudicated`, so my own adjudication made it fail — it was asserting the
  pre-review state rather than the rule the plan states. And the figure's title hardcoded
  "0 fail" while its own table showed one.
- **The evidence figure quoted a different fund than the RUN_LOG.** It ordered by position size
  ascending and picked the smallest SpaceX holding; the log cites the largest. Now
  deterministic and largest-first, so figure and written record quote the same row.
- **A rounding was doing part of an argument.** $4,228,993.75 rendered as $4,228,994 beside the
  words "the same dollars". Values now carry two decimals.
- **Red was used as a warning colour**, which the project's `DESIGN.md` forbids — red is the
  primary series, never danger. The two wrong choices in the factor figure are now secondary,
  and red marks the answer the figure is about.

## What I understand now, and what I still do not

**Understood.** A detector that flags the right company can still be using the wrong rule — a
correct output is not evidence of a correct mechanism, and testing against cases it already
catches proves nothing. A ratio is a measurement; a factor is a judgment; they are different
columns because they are different claims. And coverage reconciles exactly: 5,806 holdings =
28 rejected in week 5 + 72 superseded by amendments + 5,706 aggregated into marks, with a test
asserting it.

**Not understood, and left open.** Non-USD currency is guarded but unexercised — all 5,806
holdings are USD, so the guard has never fired and I cannot claim it works. The plan's ~$589
check remains unreachable from bulk data and says so rather than passing quietly. The
`$1.00` OpenAI placeholder is identified but still priced in the panel.

**Carried:** the live EDGAR path, 314 of 322 golden-set labels unattested, the 28
`%COHERE%` holdings still inside the shipped universe layer, milestone PR 1 still not opened.
