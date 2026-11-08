# 2026-11-06 - Reading debt announcements into cited facts

**Week covered:** 2026-11-02 - 2026-11-08

**Video:** [Mycroft_OmMali_06_11_2026.mp4](https://drive.google.com/drive/u/1/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The AI Debt Tracker is an AI agent, run entirely on a laptop, that reads companies' public
filings to keep an up to date record of every bond and loan owed by 25 AI-sector companies, and
is graded against the debt each company later reports officially.

This week the agent learned to read a debt filing into structured facts: each bond or loan, with
its amount, interest rate and due year, every value pointing back to the sentence it came from.

- **An event reader that never types a number.** Code picks the passages that state debt terms;
  a small local model lists each instrument and copies the exact words for every value, naming the
  passage; code checks the words are really there and parses the number itself.
- **It passes the week's check, and the honest comparison is less flattering.** On 24 filings
  whose 66 instruments were labelled before anything ran, the reader got 94% of fields right
  against 84% for plain pattern matching. Asking the same model to type the numbers itself got
  100%. What the reader adds is a cited sentence behind every value, not accuracy.
- **The copy check caught real mistakes.** For euro bonds the model "copied" amounts in dollars
  the filing never states. Those values were refused rather than used: missing, not wrong.
- **A fresh triage check did not pass.** On 50 newly labelled filings, triage found 8 of the 9
  about debt, below the 95% line. The miss is logged, not tuned away.
- **A fresh check of the answer key agreed on 1 of 5 reports** and found four new tagging
  defects, each in a different company's data. Last week's two defects are fixed.
- **The week's gate is recorded as delegated, not cleared.** The work was handed to Claude end
  to end and has not yet been reviewed by a person.

## Files

```
narration_script.md    the 2-3 minute script, with notes and where every number comes from
description.txt        the video description
adt-w4-reader.*        B1, the event reader and B2: fields read right, and extras
adt-w4-grounding.*     the copy check: the Alphabet euro example, and what was refused
adt-w4-triage.*        the fresh triage check, 8 of 9, below the pass line
adt-w4-holdout.*       the answer key on five fresh reports, 1 of 5
FRICTIONAL.md          the process log for the week
```
