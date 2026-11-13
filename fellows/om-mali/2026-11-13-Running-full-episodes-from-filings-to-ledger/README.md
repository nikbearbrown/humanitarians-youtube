# 2026-11-13 - Running full episodes from filings to ledger

**Week covered:** 2026-11-09 - 2026-11-15

**Video:** [Mycroft_OmMali_13_11_2026.mp4](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The AI Debt Tracker is an AI agent, run entirely on a laptop, that reads companies' public
filings to keep an up to date record of every bond and loan owed by 25 AI-sector companies, and
is graded against the debt each company later reports officially.

This week the pieces built so far run as one system: for each company and quarter, the agent goes
from the filings in the window to a ledger of the company's bonds, and checks its own result.

- **A graph that runs a whole quarter.** Code lists the filings, triage keeps the ones about debt,
  a reader runs on each of those in parallel, and code merges what they found, retires matured
  bonds and updates the ledger, then runs self-checks. All 95 development quarters ran end to end.
- **It finds the new bonds.** Against carrying last quarter's debt forward, bond recall rose from
  91% to 98%, and the tracker caught 30 of the 34 bonds issued in those quarters; carrying forward
  catches none.
- **And it adds some that are not there.** Precision fell from 93% to 90%. Every wrongly added bond
  was traced: existing notes read as new, launch notices with no interest rate yet, and the banks'
  option to buy more. All three are fixes for next week.
- **One bug found and fixed on development data**, with both runs reported: bonds sold after a
  quarter ended had been put into it.
- **Last week's pieces, checked again on unread filings.** Triage found 15 of 15 debt filings
  (it failed last week, 8 of 9); the reader beat pattern matching again, 91% to 74%; the answer
  key agreed on 3 of 4 reports.
- **The week's gate is recorded as delegated, not cleared.** The work was handed to Claude end
  to end and has not yet been reviewed by a person.

## Files

```
narration_script.md    the 2-3 minute script, with notes and where every number comes from
description.txt        the video description
adt-w5-graph.*         the episode graph, with this week's counts
adt-w5-episodes.*      the tracker against carrying forward: recall, precision, new bonds caught
adt-w5-additions.*     every bond the tracker added, checked: 40 real, 26 not, and why
adt-w5-fresh.*         three checks on unread filings: triage, reader, answer key
FRICTIONAL.md          the process log for the week
```
