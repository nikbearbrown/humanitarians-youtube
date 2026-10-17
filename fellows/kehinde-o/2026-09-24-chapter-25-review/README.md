# Fact-Checking Chapter 25

**Volunteer:** Kehinde Obidele

Project update on the human fact-check of chapter 25 of the Medhavy cancer textbook, the
targeted therapies chapter. This is the chapter where I learned that a correction can be
wrong in the other direction.

## Video Files

On the shared Google Drive under `Medhavy_Kehinde/Fact Check/Chapter 25/`:

**[Google Drive folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp)**

| File | Aspect | Spec |
|---|---|---|
| `chapter25.mp4` | 16:9 | 3840x2160, 30fps, 2m 43s |
| `chapter25-short.mp4` | 9:16 | 2160x3840, 30fps, native render |

## Chapter 25 by the numbers

288 sentences in the chapter, 45 flagged for verification, 22 inside my review scope (the
FALSE verdicts, the FLAGGED ones, and the rows sent up for expert review), plus 12
editorial findings.

**14 need revision. 8 approved as written.** That produces 15 text edits across 7 files.

## The error type that runs through the chapter

Almost nothing here was invented. Things were filed in the wrong place.

The clearest case: the textbook lists **cetuximab** among drugs that cause tyrosine kinase
inhibitor keratitis. Cetuximab is a chimeric monoclonal antibody that binds the receptor
from the outside. It is not a small-molecule kinase inhibitor, and the sentence sits inside
a section about kinase inhibitors. A real drug, in the wrong class, inside a sentence that
survives a confident read.

## The row that went false after it was written

The chapter lists pancreatic ductal adenocarcinoma among cancers with no actionable
targets. On **26 August 2026** the FDA approved **daraxonrasib** for metastatic pancreatic
adenocarcinoma, with median overall survival of 13.2 months against 6.7.

That row was true when the chapter was written and true when the workbook was built. It
went false about a month before I checked it. Accuracy and currency are two different
questions.

## The part I did not expect

Chapter 25 already had a completed workbook from an earlier pass. Re-checking it against
the sources changed six of its calls, and twice the earlier plan was going to correct a
textbook that was already right:

| Row | Earlier plan | What the sources show |
|---|---|---|
| EMA ctDNA authorisation, 2014 | Could not verify, revise it | The EMA committee did approve ctDNA testing for EGFR status in September 2014. Chapter approved as written. |
| NCI 30-point omics checklist | Could not verify, revise it | McShane 2013 describes an NCI checklist and lists 30 criteria. Chapter approved as written. |

Flagging something true as false is also an error. Nobody audits the corrections.

## Auditing the audit

Three full passes. The second caught five wrong first authors and a quote I had linked to a
page that words it differently. The third caught nine quotations ending in a full stop the
source did not have, five shortened article titles, and four statements I could not tie
back to a source I had actually read.

Final state: **44 sources**, every quoted fragment located in the page its link opens.

## Files in this repo

- `beat_sheet.json` — the script
- `PEDAGOGY.md` — narration gate, VERDICT: PASS
- `FACTCHECK.md` — every on-screen claim and its source
- `SHOTLIST.md` — typed work order
- `PROMPTS.md` — the on-screen prompts

Media files are not committed.
