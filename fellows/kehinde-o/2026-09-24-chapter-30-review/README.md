# Fact-Checking Chapter 30

**Volunteer:** Kehinde Obidele

Project update on the human fact-check of chapter 30 of the Medhavy cancer textbook,
future directions in cancer treatment research. The largest workbook in the project so far,
and the one that took four audit passes.

## Video Files

On the shared Google Drive under `Medhavy_Kehinde/Fact Check/Chapter 30/`:

**[Google Drive folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp)**

| File | Aspect | Spec |
|---|---|---|
| `chapter30.mp4` | 16:9 | 3840x2160, 30fps, 2m 44s |
| `chapter30-short.mp4` | 9:16 | 2160x3840, 30fps, native render |

## Chapter 30 by the numbers

1,654 sentences, more than five times Chapter 25. 55 flagged for verification, and those 55
assertions spread across **111 evidence rows**, because one sentence can lean on several
sources. 35 fell inside my scope, plus 6 editorial findings.

**24 need revision. 11 approved as written.** That produces 29 text edits across 6 files.

Every one of the 11 rows the verification pass had already marked FALSE turned out to be a
genuine error. Eleven out of eleven, no false alarms. That is the opposite of what I found
in Chapter 25.

## Two numbers standing in each other's place

The textbook says a screen of 15 compounds identified 10 anticancer agents. The study
screened a library of **2,427 drugs** and found **15 hits**, of which 10 were anticancer
agents. The 15 is the output, not the input. The sentence understates the work by two
orders of magnitude and makes the hit rate meaningless.

## An error the chapter inherited

The chapter names *Mycoplasma hominis* as the bacterium whose cytidine deaminase
inactivates gemcitabine. The documented species is *M. hyorhinis*.

The part worth knowing: a 2021 review says *hyorhinis* in its body text and *hominis* in a
figure caption **in the same paper**. The wrong name is already loose in the published
literature. The chapter probably inherited the error rather than inventing it.

## Four checks, and what each one caught

| Pass | What it asked | What it caught in my own work |
|---|---|---|
| 1 | Is the science right? | The review itself |
| 2 | Are links and quotes exact? | My document truncating links at 46 characters, four of them broken; 13 quotes not character-exact |
| 3 | Is there newer evidence? | A 2026 five-year update of a vaccine trial I had missed |
| 4 | Does the source support this row? | Three sources cited on rows they do not support, one range asserted with no source |

Pass 4 also caught one of my own corrections introducing a new problem: I had replaced an
unsourced figure with an unsourced word. I dropped the claim instead.

**The fourth pass was the one that stopped asking whether my sources were real and started
asking whether they said what I claimed.**

## Reported as unverified, not as wrong

Three figures could not be verified and are labelled that way rather than corrected:
organoid establishment rates of 60 to 90 percent, an approximately four-fold difference in
a drug-sensitivity measure, and that 60 percent of DNA vaccine trials use a combination
approach. Unverified is a verdict. It is not the same as wrong.

## Practical blocker for the next stage

The workbook recorded character-encoding damage in 4 files. It is actually in **7**,
including eight broken arrows nobody had logged. It has to be repaired and committed before
any text edit, or find-and-replace fails silently.

## Files in this repo

- `beat_sheet.json` — the script
- `PEDAGOGY.md` — narration gate, VERDICT: PASS
- `FACTCHECK.md` — every on-screen claim and its source
- `SHOTLIST.md` — typed work order
- `PROMPTS.md` — the on-screen prompts

Media files are not committed.
