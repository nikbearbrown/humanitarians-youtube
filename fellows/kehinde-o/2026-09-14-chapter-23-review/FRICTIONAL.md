# Frictional log — Fact-Checking Chapter 23

## 2026-09-14 — the chapter where I started auditing myself

- **Video:** https://www.youtube.com/watch?v=GBjkrRlyDSE
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/Fact Check/Chapter 23/`)
- **Report:** [REPORT.md](REPORT.md)
- **Project repository:** https://github.com/Medhavy/medhavi-cancer (private), branch `text-edits`
- **Paired explainer:** [Further, But Better](../2026-09-14-further-but-better/)

**What I was working on.** The chemotherapy chapter, the densest so far: 474
sentences, 136 flagged, 86 rows reviewed across three tabs. 52 need revision, 34
approved as written.

**What I tried, and what I expected.**
- I expected this to be Chapter 2 at larger scale.
- I expected one audit pass over my own work to be enough.

**Where it resisted, and what I did next.**
- **One finding was a patient-safety risk rather than an accuracy problem.** The
  chapter presents venetoclax for multiple myeloma as established practice. It is
  not an FDA-approved use, the label carries a mortality warning against that
  combination, and the CANOVA phase III trial missed its primary endpoint with more
  treatment-emergent deaths in the venetoclax arm. Most errors in this project cost
  accuracy. This one could reach a patient, and it changed how I prioritise.
- **The methotrexate half-life was stated backwards** relative to the FDA label.
  Rescue timing depends on that number, so the direction of the error matters more
  than its size.
- **Errors reached back a century.** Arsenicals in cancer treatment were dated to
  the 1900s; Lissauer treated leukaemia with arsenic in 1865. Nitrogen mustard
  research was attributed to the First World War when it came from the Second.
- **One audit pass was not enough, and I found that out the hard way.** I ran
  three. The second re-fetched every source and confirmed the exact quoted text was
  on the page rather than in a search-engine summary; it caught two quotations I
  had attributed to the wrong papers, three wrong identifiers and two dead FDA
  links. The third checked my deliverables against the master instructions and
  found 37 rows missing required elements. Five errors in my own work, found by me,
  which is the part I would rather not have needed.
- **I reversed one of my own verdicts.** On dexrazoxane, 2025 literature had shifted
  the consensus after I had already ruled. Reversed and documented.
- **The editorial tab needed a different kind of work.** Garbled text and broken
  characters from generation are quick to spot but are not factual verification,
  and they cannot be fixed in the same pass. The rule I settled on is that encoding
  repairs go in as their own commit before any content edit, because a content edit
  made against corrupted text cannot be trusted.
- **The AI-only tab had errors again**, as in Chapter 2, which settles it: a tab
  marked as not needing human review still needs human review.
- **A defect blocks the next stage.** Files 2 to 5 carry a character-encoding fault
  that corrupts Greek letters. Until it is repaired and committed, find-and-replace
  on those files fails silently, so no text edit can be trusted.

**What Claude contributed, and what I did with it.**
- Mine: the review, all verdicts, the three audit passes, the evidence document and
  its 100 source URLs.
- Claude's: the beat sheet, and machine-verification that every URL in the evidence
  document resolves.
- Accepted: making the self-audit the spine of the video rather than a footnote.
  The honest lesson of this chapter is that the reviewer can make the same mistake
  as the text.
- Rejected/changed: an early beat described the venetoclax finding in stronger
  language. Since the video is public and the subject is a real drug, I had it cut
  back to what the label and the trial actually say, with no advice attached.
- Evidence: `Chapter_23_Evidence_Document.docx` (100 unique source URLs),
  `Chapter_23_Evidence_AIOnly.docx`, `Chapter_23_MDX_TextEdit_Guide.md`,
  `Chapter_23_StepByStep_WorkbookUpdate.docx`.

**What I understand now, and what I still do not.**
- Understood: auditing the text is not enough. The failure mode I am looking for in
  the textbook, citing a source that does not say what you claim, is available to
  me too.
- Understood: a search-engine summary is not the source. Opening the page is the
  only check that counts.
- Open: the encoding repair, and the text edits that depend on it. The corrections
  went up as part of PR #46 on https://github.com/Medhavy/medhavi-cancer.
- Open: a step-by-step Workbook Update Guide was written for this chapter, as for
  Chapter 1, so the process stays repeatable.
