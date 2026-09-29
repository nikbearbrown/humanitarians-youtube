# Renewal request — Kehinde Obidele

- **Current agreement:** 21 Aug — 30 Sep 2026
- **Requested period:** 1 Oct — 30 Nov 2026

- **Role:** Research Analyst (AI Textbook Auditor)
- **Project:** Medhavy — cancer textbook fact-checking
- **Repository:** https://github.com/Medhavy/medhavi-cancer (private), branch `text-edits`
- **Supervisor:** Prof. Evin

## What the current period produced

Seven chapters of the Medhavy cancer textbook audited against primary sources,
and ten videos produced. Every figure below comes from a reviewed workbook or an
evidence document rather than an estimate.

- **Seven chapters audited:** 1, 2, 6, 9, 23, 25 and 30. Each produced a reviewed
  workbook, an evidence document recording the source chain claim by claim, and an
  MDX TextEdit guide for applying the corrections.
- **325 rows formally reviewed and ruled on** across the five reported chapters,
  drawn from 418 flagged assertions. In the three chapters where the full sentence
  count was recorded (23, 25 and 30) those assertions were screened out of 2,416
  sentences. Chapters 6 and 9 are complete but not yet counted here.
- **A patient-safety finding in Chapter 23.** The chapter presents venetoclax for
  multiple myeloma as established practice. It is not an FDA-approved use, the
  label carries a mortality warning against that combination, and the CANOVA phase
  III trial missed its primary endpoint with more treatment-emergent deaths in the
  venetoclax arm.
- **A method that audits itself.** Chapter 23 was checked three times, Chapter 30
  four. Those passes found errors in my own review, not only in the textbook: two
  quotations attributed to the wrong papers, five wrong first authors, links
  truncated at 46 characters, and three sources cited on rows they do not support.
  One of my own verdicts was reversed on newer evidence.
- **Ten videos, 4K in both aspect ratios**, five project updates and five STEM
  explainers, each built on measured work rather than description. Two are
  published; eight are delivered and awaiting the review pipeline.

### Evidence

| Chapter | Scope | Result | Drive | Video | Log |
|---|---|---|---|---|---|
| 1 | 136 rows | 105 TRUE, 21 FALSE, 10 FLAGGED | [folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp) | not yet published | [log](./2026-09-04-chapter-1-review/FRICTIONAL.md) |
| 2 | 46 main claims, 134 AI-only | 25 TRUE, 18 FALSE, 3 FLAGGED; approved by Prof. Evin with 3 changes | [folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp) | [watch](https://www.youtube.com/watch?v=mVGxJ4ssHQ4) | [log](./2026-09-08-chapter-2-review/FRICTIONAL.md) |
| 23 | 474 sentences, 136 flagged, 86 reviewed | 52 revise, 34 approved; 100 source URLs; triple-audited | [folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp) | [watch](https://www.youtube.com/watch?v=GBjkrRlyDSE) | [log](./2026-09-14-chapter-23-review/FRICTIONAL.md) |
| 25 | 288 sentences, 45 flagged, 22 in scope | 14 revise, 8 approved; 44 sources; six earlier calls reversed | [folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp) | not yet published | [log](./2026-09-24-chapter-25-review/FRICTIONAL.md) |
| 30 | 1,654 sentences, 55 flagged over 111 rows, 35 in scope | 24 revise, 11 approved; all 11 prior FALSE rows confirmed; four audit passes | [folder](https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp) | not yet published | [log](./2026-09-24-chapter-30-review/FRICTIONAL.md) |
| 6 | reviewed workbook, evidence document, TextEdit guide | complete, not yet reported | — | — | — |
| 9 | reviewed workbook, evidence document, TextEdit guide | complete, not yet reported | — | — | — |

### STEM explainers

| Week | Topic | Built on | Video | Log |
|---|---|---|---|---|
| [1–4 Sep](./2026-09-04-what-the-marks-weigh/) | What the Marks Weigh | [ami](https://github.com/Kenny0bi/ami) | not yet published | [log](./2026-09-04-what-the-marks-weigh/FRICTIONAL.md) |
| [7–11 Sep](./2026-09-08-the-target-that-moved/) | The Target That Moved | [Deep-Q-learning-lunarlander](https://github.com/Kenny0bi/Deep-Q-learning-lunarlander) | not yet published | [log](./2026-09-08-the-target-that-moved/FRICTIONAL.md) |
| [14–18 Sep](./2026-09-14-further-but-better/) | Further, But Better | [quantlab](https://github.com/Kenny0bi/quantlab) | not yet published | [log](./2026-09-14-further-but-better/FRICTIONAL.md) |
| [21–25 Sep](./2026-09-24-the-number-that-shrank/) | The Number That Shrank | [adverse-event-pipeline](https://github.com/Kenny0bi/adverse-event-pipeline) | not yet published | [log](./2026-09-24-the-number-that-shrank/FRICTIONAL.md) |
| [21–25 Sep](./2026-09-24-backwards-along-the-tape/) | Backwards Along the Tape | [ember](https://github.com/Kenny0bi/ember) | not yet published | [log](./2026-09-24-backwards-along-the-tape/FRICTIONAL.md) |

Weekly hours: [HOURS.md](HOURS.md) — 134 hours to date, 83 audit and 51 video.
Weekly frictional logs: one per work folder, listed in [README.md](README.md).

## Plan for the requested period

In order, each gating the next:

1. **Clear the backlog of applied edits** (1–10 Oct). Five chapters have TextEdit
   guides written and none applied. Repair and commit the character-encoding fault
   first, because until it is fixed find-and-replace fails silently on Chapters 23,
   25 and 30 and any edit made before then cannot be trusted.
2. **Report Chapters 6 and 9** (13–17 Oct). Both are audited and neither is
   recorded anywhere. Undocumented work cannot be recognised, so this comes before
   new chapters.
3. **Measure my own error rate** (20–24 Oct). Across seven chapters the audit
   passes have found a consistent set of mistakes in my own review. I want to count
   them by type rather than describe them: how often a quotation is not
   character-exact, how often a source does not support the row it sits on. If the
   rate is high for a category, the honest outcome is reporting that my review is
   unreliable for that category rather than quietly tightening up.
4. **Audit the remaining assigned chapters** (from 27 Oct), at the pace the
   measured error rate justifies rather than the pace that produces the most
   chapters.
5. **Two videos per week throughout**, one project update and one STEM explainer,
   continuing the current standard: 4K in both aspect ratios, every figure traced
   to a source in a committed FACTCHECK.md.

## Open items I am carrying

- The character-encoding repair, and every text edit blocked behind it.
- Chapters 6 and 9 unreported.
- Eight of ten videos delivered but not published, so there is no engagement data
  yet to act on.
- Weekly engagement (commenting on my own and other HAI videos) cannot start in
  earnest until the videos are live.
