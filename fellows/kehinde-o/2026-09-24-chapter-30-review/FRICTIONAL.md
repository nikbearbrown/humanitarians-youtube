# Fact-Checking Chapter 30 — frictional log

## 2026-09-24 — building the week 5 project update

This was the largest workbook in the project so far: 1,654 sentences, more than five times
Chapter 25, with 55 flagged assertions spread across 111 evidence rows because one sentence
can lean on several sources.

The thing I did not expect is that every single row the verification pass had already
marked FALSE turned out to be a genuine error. Eleven out of eleven, no false alarms. That
is the opposite of what I found in Chapter 25, where re-checking reversed six calls. I do
not have a clean explanation for the difference yet.

The error I keep describing to people is the drug screen. The chapter says a screen of 15
compounds identified 10 anticancer agents. The study screened 2,427 drugs and found 15
hits, of which 10 were anticancer. The 15 is the output, not the input. Both numbers are
real; they are standing in each other's place, and the sentence understates the work by two
orders of magnitude.

The one I liked most is the wrong species, because I found where it came from. The chapter
names Mycoplasma hominis where the documented species is M. hyorhinis. Then I opened a 2021
review and its body text says hyorhinis while a figure caption in the same paper says
hominis. The wrong name is already loose in the published literature. That changed how I
describe these errors: this one was inherited, not invented.

### Four passes, and what the fourth one was for

Pass 1 checked the science. Pass 2 found my own document truncating links at 46 characters
and shipping four broken ones, plus thirteen quotes that were accurate in substance but not
character-exact. Pass 3 found newer evidence I had missed, a 2026 five-year update. Pass 4
found three sources cited on rows they do not actually support.

Pass 4 is the one worth keeping. The first three passes were asking whether my sources were
real. The fourth asked whether they said what I claimed. It also caught one of my own
corrections introducing a new problem: I had replaced an unsourced figure with an unsourced
word, so I dropped the claim entirely.

Three figures stayed unverified and are reported that way rather than corrected. Unverified
is a verdict. It is not the same as wrong, and collapsing the two would have been the easy
thing to do.

### Still open

The encoding damage is worse than recorded: 7 files, not the 4 in the workbook, including
eight broken arrows nobody had logged. That has to be repaired and committed before any
text edit, or find-and-replace fails silently. That is the blocker for the next stage.
