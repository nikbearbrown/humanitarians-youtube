# Fact-Checking Chapter 23

**Volunteer:** Kehinde Obidele

Project update on the human fact-check of chapter 23 of the Medhavy cancer
textbook, the chemotherapy chapter. The densest chapter so far, and the one
where I started auditing my own review as well as the text.

## Video Files

On the shared Google Drive under `Medhavy_Kehinde/Fact Check/Chapter 23/`:

**[Google Drive folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp)**

| File | Aspect | Spec |
|---|---|---|
| `chapter23.mp4` | 16:9 | 3840x2160, 30fps, 2m 47s |
| `chapter23-short.mp4` | 9:16 | 2160x3840, 30fps, native render |

## Chapter 23 by the numbers

474 sentences in the chapter, 136 flagged for verification, 86 rows reviewed:
all 21 FALSE verdicts, all 10 FLAGGED, 8 TRUE rows marked for expert review,
15 spot-checked TRUE rows, all 10 editorial findings, 22 spot-checked AI-only
sentences.

**52 need revision. 34 approved as written.**

## The finding that matters most

The textbook presents **venetoclax for multiple myeloma** as established
practice. It is not an FDA-approved use, the label carries a mortality warning
against that combination, and the CANOVA phase III trial (January 2026) missed
its primary endpoint with more treatment-emergent deaths in the venetoclax arm.

Most errors cost accuracy. This one could reach a patient.

## Errors reaching back a century

| The textbook says | The record says |
|---|---|
| Arsenicals in cancer treatment from the 1900s | Lissauer treated leukemia with arsenic in 1865 |
| Nitrogen mustard research from WWI | It came from WWII |
| Methotrexate half-life | Stated backwards against the FDA label; rescue timing depends on it |

## Auditing the audit

Three full passes: the science, then every source re-fetched and the quoted text
confirmed present on the page rather than in a search summary, then the
deliverables against the master instructions.

Those caught **five errors in my own work**, including two quotations attributed
to the wrong papers, three wrong identifiers, two dead FDA links, and one verdict
I reversed myself on **dexrazoxane** after reading the 2025 evidence.

The evidence document carries **100 unique source URLs**, all machine-verified.

## Practical blocker for the next stage

Files 2-5 carry a character-encoding defect that corrupts Greek letters. It has
to be fixed before any text edits, or find-and-replace will silently fail.

## Files in this repo

- `beat_sheet.json` — the script
- `PEDAGOGY.md` — narration gate, VERDICT: PASS
- `FACTCHECK.md` — every on-screen claim and its source
- `SHOTLIST.md` — typed work order
- `PROMPTS.md` — the on-screen prompts

Media files are not committed.
