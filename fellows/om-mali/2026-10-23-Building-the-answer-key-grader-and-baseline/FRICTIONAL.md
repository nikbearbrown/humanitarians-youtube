# Frictional log - 2026-10-23

**AI Debt Tracker, week 2 · evaluation · Building the answer key, grader and baseline**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to `docs/answer_key.md`,
`docs/baseline_b0.md`, `docs/handcheck.md`, `docs/changes_dev.md`, `docs/worklog.md` or
`manifests/week2_gate.json` in the project.

---

## What I was working on

Week 1 proved the project was worth building. Week 2 was about the judge. The agent can only be
trusted as far as its scoring can, so I built the scoring first, before writing a line of agent
code. That meant three pieces:

1. **An answer key** covering every quarterly and annual report of all 100 companies, the 25 AI
   companies plus the 75 in the generalisation set.
2. **A grader** that compares any ledger against that key at the level of detail each company
   actually reports.
3. **Baseline B0**, the do-nothing strategy of carrying last quarter's debt forward and dropping
   bonds that matured. This is the floor the agent has to beat.

I also started the week with housekeeping. I committed weeks 0 and 1, appended their run log
entries to the shared `logs/RUN_LOG.md`, and archived the superseded draft universe instead of
deleting it.

## What I tried, and what I expected

The design's Week 2 check was that the grader must agree with a hand check of 10 company
quarters, using the debt tables printed in the reports. I expected that to pass on the first
try, because the grader is plain code following written rules. The rules are: same currency,
coupon within 0.01 points, same maturity year, and principal within 1% of face or 2% of carrying
value, with each bond paired once through an optimal assignment.

I set the check up so it could not flatter itself. Those 10 reports were the calibration set. If
they found bugs, I would hold out a second set, choose its reports **before** reading them, and
grade that set once.

For B0 I expected a mediocre score. I assumed doing nothing would look bad, which would make the
headroom obvious.

## Where it resisted, and what I did next

**The grader was wrong, not the companies.** The first pass agreed on 8 of 10, and every
disagreement traced back to my side:

- **Oracle:** repaid notes came back to life through their face-value tags (P30).
- **AMD:** a member covering two bonds was read as a duplicate (P31).
- **Broadcom:** the VMware notes it took on in the acquisition were dropped along with their
  acquisition axis (P32). Others were named only by due date, or misspelt as `SeniorNots` (P33).
- **Equinix:** a Swiss franc note was tagged in dollars in the XBRL (P34).
- **Microsoft:** offerings were measured on their original deal size instead of what was still
  outstanding.

I fixed each one and logged it in the design's problem list. After that the grader agreed on
10 of 10. **Because those ten were the reports that found the fixes, I did not count 10 of 10 as
the score.** On the three held-out reports it agreed on 2 of 3. The miss is Digital Realty's own
tagging: a repaid note tagged only at face value, a dollar note tagged as euros, and translated
face amounts (P35 to P37). I left those open on purpose rather than tuning against the held-out
set. They come first in Week 3, along with a new held-out check.

**B0 first looked worse than it really is, and then better.** Two problems pulled it down. The
bulk data started after Intel's and Oracle's previous annual reports, and B0 refused Intel's
FY2023 report because it itemised 79% of its debt against an 80% bar. I added the earlier data
and let B0 fall back to the best-itemised recent report. The honest result: **90.7% bond recall,
90.3% precision, 99.2% principal accuracy, and 0 of 36 new bonds caught.** It caught 3 of 16
removals, and 18 of 47 bond-by-bond episodes came out exactly right. The per-offering recall
first came out at 91.7%. That figure compared original deal sizes and flattered B0. Measured
properly, it is 76.2%.

**A re-run quietly changed a frozen file.** Re-running the selection scripts with the fixed
parser swapped Molson Coors for Post Holdings in the generalisation set, which was supposed to be
frozen. I restored the frozen files from the commit and changed the three scripts so they refuse
to overwrite a frozen artifact unless `--refreeze` is passed. I also listed the 5 of 495 episodes
that today's rules would grade at a different level. They stay frozen until a gate decides
otherwise.

**The SEC's clock moved.** The same re-run showed that 43 of the 495 episode cutoffs had shifted
by 4 to 5 hours in EDGAR's own index since 18 October. Nine filers had switched from Eastern time
to UTC. A cutoff that can move is a leak waiting to happen, so the point in time server now pins
the cutoff to the target report itself and keeps a 5-hour safety margin on the cutoff day.

**The first count of announced changes was too low.** The search used rounded coupons, for
example 3.62% instead of 3.625%, and missed four bonds. After the fix, **30 of 32 searchable new
bonds and 5 of 6 early removals were announced before the report.** Four more new bonds carry no
tagged interest rate, so there is nothing to search for. I report 30 of 32, not 30 of 36, and say
why.

## What Claude contributed, and what I did with it

Claude Code implemented most of the code to the rules in my design: the answer key builder, the
grader, the bootstrap intervals, B0, and the change-explaining script. It also ran them against
the data. The test suite grew from 65 to 95 tests.

It also transcribed the ten printed debt tables for the hand check. Those transcriptions are a
model judgment, and each one is labelled that way in `manifests/handcheck/`.

What I did with it:

- **I designed the check so it could not pass by construction.** Calibration and held-out sets
  were kept separate, the held-out reports were chosen before reading, and they were graded once.
  That is why the real number is 2 of 3 and not 10 of 10.
- **I treated every disagreement as our bug until it was proven otherwise**, and had each one
  traced to a cause before anything was fixed.
- **I refused the flattering numbers.** I asked for the 91.7% per-offering figure to be
  recomputed on outstanding amounts, and for the announced-change count to be stated against the
  bonds that can actually be searched for.
- **I protected the frozen test set.** When the re-run changed it, it was restored, not
  re-frozen to fit.
- **I cleared the Week 2 gate myself.** I reviewed the hand check and accepted it on the basis
  recorded in `manifests/week2_gate.json`, with P35 to P37 carried forward instead of being
  waved through.

## What I understand now, and what I still do not

**Understood.** A grader needs its own grader. Plain code with written rules still had five bugs,
and only comparison with the printed reports found them. A check that found the fixes cannot also
be the score, so held-out data matters even for a tool and not only for a model. A high baseline
is not a failure. Doing nothing scores 90.7% because debt mostly does not move. The number that
matters is the zero, the new bonds it cannot catch. And "frozen" has to be enforced in code,
because a well-meaning re-run will silently change it.

**What I still do not know.**

- **Whether the grader is right beyond the reports I checked.** 2 of 3 on the held-out set is a
  small check, and Digital Realty's tagging is still open.
- **Whether the agent can close the gap.** It does not exist yet. Week 3 builds the document
  tools and triage, and the agent's reader comes after that.
- **How the 5 of 495 episodes should be graded** under the improved rules. That is a gate
  decision I have deferred, not made.
- **How much of the hand check I could do without help.** Reading a printed debt note line by
  line, with currency, carrying versus face, and assumed debt from acquisitions, is still slower
  for me than for the model. Reviewing its transcriptions is how I am learning it.
