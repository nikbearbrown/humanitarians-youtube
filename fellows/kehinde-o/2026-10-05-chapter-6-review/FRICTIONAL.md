# Frictional log — Fact-Checking Chapter 6

## 2026-10-05 — the chapter where the worst defect was mine

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/Fact Check/Chapter 6/`)
- **Report:** [REPORT.md](REPORT.md)
- **Project repository:** https://github.com/Medhavy/medhavi-cancer (private), branch `text-edits`
- **Paired explainer:** [Nothing Errored](../2026-10-05-nothing-errored/)

**What I was working on.** The Chapter 6 fact-check, on tumor suppressor genes:
212 sentences, 134 flagged, 16 inside scope, plus 13 editorial findings. 8 need
revision and 8 are approved, which is the first even split in this project.

**What I tried, and what I expected.**
- I expected to audit the textbook. By now I expected my own method to be settled.
- I expected copied text to be a presentation problem, an attribution gap rather
  than an accuracy one.

**Where it resisted, and what I did next.**
- **A copied error, not an invented one.** The chapter calls the BRCA and PARP
  relationship "synergistic lethality" where the field says synthetic lethality,
  and the two mean different things. It did not make that up. It reproduces 43
  consecutive words from an NCBI GeneReviews page, and that page uses the wrong
  term too. That changed my view of copying: an inherited error outlives the
  source it came from, and no sentence-level check finds it.
- **A sentence that reverses its own epidemiology.** Non-inherited retinoblastoma
  is called rare. Non-heritable disease is 60 to 70 percent of cases. What is rare
  is the event being described, two independent hits in one cell. The mechanism is
  right and the word attached to it is the opposite of true.
- **The worst defect in the review was in my own evidence document.** Pass two
  found that most of the narrative sections had been carried over from a template
  and still described Chapter 30's findings: organoid rates, a species mix-up, a
  melanoma vaccine. My summary table said zero TRUE rows in scope when there were
  six, and six editorial findings when there were thirteen. Every section was
  rewritten and every count recomputed from the workbook.
- **Three of my citations resolved and still failed.** Two gene records and one
  sequence record are now served behind a bot challenge. The link returns fine; a
  reader following it sees a captcha instead of the fact. A status check cannot see
  that. Replaced with PMC sources. 120 links checked: 115 resolve, 5 error.
- **I had recorded five plagiarism claims as confirmed without testing them.**
  Measured properly on a later pass: 440, 352, 278 and 202 characters for four of
  them. One could not be tested at all and is reported as unverifiable.

**What Claude contributed, and what I did with it.**
- Mine: the review, the verdicts, the four passes, the evidence document and the
  TextEdit guide.
- Claude's: the beat sheet from my review record, and the link re-testing that
  distinguished "resolves" from "readable".
- Accepted: building the video around my own defect rather than the chapter's.
  It is the more useful lesson and it is what actually happened.
- Rejected/changed: an early draft said the chapter invented the wrong term. It
  copied it. That distinction is the whole point and the draft lost it.
- Evidence: `Chapter_6_Evidence_Document.docx`, `Chapter_6_MDX_TextEdit_Guide.md`,
  the reviewed workbook, and the corrections in PR #46.

**What I understand now, and what I still do not.**
- Understood: a template saves time until it quietly answers for the wrong chapter.
  Mine did, for two passes, and nothing flagged it.
- Understood: checking that a link resolves is checking the wrong thing. The
  question is whether a reader can see the fact.
- Open: the text edits for this chapter are written and verified but not applied.
