# 2026-11-20 - Reading the opening ledger instead of borrowing it

**Week covered:** 2026-11-16 - 2026-11-22

**Video:** [Mycroft_OmMali_20_11_2026.mp4](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The AI Debt Tracker is an AI agent, run entirely on a laptop, that reads companies' public
filings to keep an up to date record of every bond and loan owed by 25 AI-sector companies, and
is graded against the debt each company later reports officially.

Until this week, every quarter started from a ledger borrowed from the answer key. Now the
tracker reads that starting ledger itself, from the company's last report, and the cost is measured.

- **Last week's wrong additions are mostly gone.** Three fixes to the merge step (launch notices,
  bonds named with no amount, the banks' option) cut the bonds added that are not in the report
  from 26 to 3. Precision rose from 90.2% to 93.3%, level with carrying last quarter forward, and
  recall stayed 7 points above it.
- **The opening ledger, read from the report.** Code finds the debt table, the model points at
  the rows, code reads every number from the cell. On 94 reports it found 89.7% of the bonds, and
  98.8% of what it found was right (rules alone: 83.8%).
- **The week's check: a borrowed start against a read one.** Starting from its own reading costs
  7.9 points of recall (97.9% to 90.1%), most of it in a few companies; precision rose to 95.5%.
  Against carrying forward, the agent is level on recall and ahead on precision.
- **Does it know when it is wrong?** The self-checks flagged 17 of the 50 quarters that ended
  wrong. Investigators settled 21 of 67 open questions but changed no graded bond.
- **Checked again on unread reports.** The answer key agreed on 4 of 5 fresh reports.
- **The week's gate is recorded as delegated, not cleared.** The work was handed to Claude end
  to end and has not yet been reviewed by a person.

## Files

```
narration_script.md    the 2-3 minute script, with notes and where every number comes from
description.txt        the video description
adt-w6-merge.*         the merge fixes: wrong additions 26 -> 3, and what the merge step now does
adt-w6-opening.*       the opening-ledger reader on 94 reports, against rules alone
adt-w6-gap.*           the week's check: oracle start, agent start and carry-forward
adt-w6-catch.*         self-catch rate and the investigators
FRICTIONAL.md          the process log for the week
```
