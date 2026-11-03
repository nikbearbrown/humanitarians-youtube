# Frictional log — Chapter One, Reviewed

## 2026-09-04 — first chapter closed, and the first video about my own work

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/Fact Check/Chapter 1/`)
- **Report:** [REPORT.md](REPORT.md)
- **Project repository:** https://github.com/Medhavy/medhavi-cancer (private), branch `text-edits`
- **Paired explainer:** [What the Marks Weigh](../2026-09-04-what-the-marks-weigh/)

**What I was working on.** Closing out the Chapter 1 fact-check of the Medhavy
cancer textbook and reporting it: 136 flagged rows reviewed, 105 TRUE, 21 FALSE,
10 FLAGGED, with an evidence document recording the source chain for each.

**What I tried, and what I expected.**
- I expected the errors to be obvious inventions. Most were not.
- The video was originally going to be about AI hallucination in general, using
  fabricated citations as the hook.

**Where it resisted, and what I did next.**
- **The most common failure was not invention but misattribution.** The AI
  produced real, resolvable PMC identifiers and attached the wrong authors to
  them. "Otto and Bhatt, 2022" for PMC9583502 is a real paper with real authors,
  and neither of them is Otto or Bhatt. That is much harder to catch than a made-up
  reference, because every surface check passes.
- **Two other error shapes showed up alongside the misattributions.** Statistics
  that are near misses rather than inventions: the chapter says "10-30%" where the
  source says "25-30%", which is harder to catch than a wrong number because it
  sounds plausible. And figures that were right once and have been superseded: the
  chapter puts the human body at 10^14 cells where the modern estimate is
  3 x 10^13. Deciding which version of a number is current is its own piece of work.
- **I built the workflow while doing the chapter, then wrote it down.** Read the
  flagged sentence, find the cited source on PubMed or the FDA databases, confirm
  the citation is real and that it supports the specific claim, then record the
  decision and comments. I turned that into a step-by-step Workbook Update Guide so
  the next chapter would not start from nothing.
- **I changed the video.** The first draft was a general explainer on AI
  hallucination. It was more interesting as a plain progress report on what I had
  actually found and counted, so I dropped the framing and rebuilt it as a straight
  Chapter 1 report using the fellows format rather than the explainer one.
- **A correction in the video never appeared.** The overview beat is supposed to
  type a sentence and then correct a word in place. The trigger word had been
  written with its punctuation attached, and the component strips punctuation
  before matching, so the match never fired and the correction never played. This
  affected this reel and two others before it was found. All were rebuilt.

**What Claude contributed, and what I did with it.**
- Mine: the whole fact-check, the verdicts, the evidence document, and the
  decision to re-scope the video.
- Prof. Evin provided the workbook and the initial guidance on what the review
  columns should contain.
- Claude's: the beat sheet from my review record, and the diagnosis of the
  trigger-word bug.
- Accepted: reporting the counts plainly rather than dramatising the errors.
- Rejected/changed: the original hallucination framing, and an early draft that
  described the errors as dangerous without qualification. The errors are specific
  and mostly attribution or currency problems; overstating them would misrepresent
  the chapter.
- Evidence: `01_factcheck_review_REVIEWED.xlsx`, `Chapter_01_Evidence_Document.docx`
  and two step-by-step guides, held in the project working folder.

**What I understand now, and what I still do not.**
- Understood: a citation can be real and still be wrong. Checking that a PMCID
  resolves proves nothing about whether the authors, the year or the claim match.
- Understood: reporting my own numbers honestly is more useful than a narrative
  about AI risk. The counts are the finding.
- Open: the text corrections went up as part of PR #46 on
  https://github.com/Medhavy/medhavi-cancer; applying them to the chapter files is
  still outstanding.
