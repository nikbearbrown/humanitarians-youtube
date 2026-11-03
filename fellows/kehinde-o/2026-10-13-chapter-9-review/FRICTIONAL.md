# Frictional log — Fact-Checking Chapter 9

## 2026-09-24 — The audit, and the finding that turned out to be mine

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1QAjFH3y4w_j7DfTFjUmGsy05ZVqJIv0r?usp=drive_link (`Medhavy_Kehinde/Fact Check/Chapter 9/`)
- **Report:** [REPORT.md](REPORT.md)
- **Project repository:** `Medhavy/medhavi-cancer` (private), branch `text-edits`
- **Paired explainer:** [Every Reading Said Fine](../2026-10-13-every-reading-said-fine/)

**What I was working on.**

Chapter 9, cell cycle control. 292 sentences, 145 flagged by the pipeline. I worked
the main tab, the AI-only tab and the editorial tab, and produced a filled workbook,
`Chapter_9_Evidence_Document.docx` and `Chapter_9_MDX_TextEdit_Guide.md`. The
corrections went into PR #46 alongside Chapter 6.

**What I tried, and what I expected.**

I expected the usual distribution: a few fabricated citations, a few stale numbers,
a long tail of editorial noise. The stale numbers showed up where I expected. The
"100,000 genes" line is a textbook case of a figure that was reasonable when it was
written and has been wrong since roughly 2003.

**Where it resisted, and what I did next.**

Two places.

The first was deciding what counted as in scope. 145 flagged sentences became 30
assertions. The other 115 are definitional, or hedged to the point where there is no
claim to check, or a restatement of something I had already ruled on. I was
uncomfortable with that ratio until I went back through them and wrote down why each
one was out of scope. If I had quietly dropped them the number would look better and
mean less.

The second was trilaciclib, and it was my own mistake. I had an earlier note recording
its approval wrongly. Checking the chapter against FDA NDA 214200 showed February 2021,
small cell lung cancer, bone marrow protection during chemotherapy. The chapter was
right. I was wrong. I corrected my record and put it in the video, because an audit
that only ever finds other people's errors is not being run honestly.

The dinaciclib row is still open. The workbook says the trial was terminated for
futility; ClinicalTrials.gov says COMPLETED. I have not worked out which is right, so
the reel reports the discrepancy and does not resolve it.

**What Claude contributed, and what I did with it.**
- Mine: the review itself, every verdict, the scope decisions, the evidence document,
  the MDX edit guide, and catching my own trilaciclib error.
- Claude's: drafting the beat sheet from my review record, the visual treatment, and
  checking the arithmetic on screen against the workbook.
- Accepted: the structure that puts my own corrected finding in its own act near the
  end, rather than burying it.
- Rejected/changed: an early draft led with the gene count because it is the most
  quotable error. I moved it back. The chapter's real problem is the wrong-agent
  error on UV damage, which a student could carry into an exam; the gene count is
  obviously stale to anyone who looks.
- Evidence: PMC6549324 for the gene count, PMC8514742 for UV photoproducts, FDA NDA
  214200 for trilaciclib, ClinicalTrials.gov for dinaciclib.

**What I understand now, and what I still do not.**
- Understood: stale numbers and wrong-agent errors fail differently. A stale number is
  caught by anyone who checks the date. A wrong agent reads as fluent and correct unless
  you know the specific mechanism, which makes it the more dangerous of the two.
- Not understood: why the pipeline flagged 145 sentences when 30 carried checkable
  assertions. The flagging appears to fire on surface features rather than on whether a
  sentence asserts anything.
- Open: the dinaciclib trial status.

## 2026-10-12 — The video build

- **Paired explainer:** [Every Reading Said Fine](../2026-10-13-every-reading-said-fine/)

**What I was working on.**

Both week 7 videos, 16:9 and 9:16 native renders each. This reel came in at 2m35s
across 10 beats and cleared Gate V with zero blockers and zero majors on the first
compile.

**Where it resisted, and what I did next.**

The attrition beat, B02, crashed the renderer on the first attempt. The component
draws one DOM node per unit of the total it is given, and I had handed it the full
sentence count. That is a real constraint of the component, not a bug in my numbers,
so I kept the figures and let the chain draw the three stages 292, 145, 30 at a scale
it can actually render.

The paperwork went first this time. On the previous batch the compile was refused at
Gate F because `FACTCHECK.md` was missing, which is a gate I had written into my own
checklist and then walked straight into. Writing all five documents before building
meant this reel cleared on the first pass.

**What Claude contributed, and what I did with it.**
- Mine: every figure, the review behind them, and the call on what each beat argues.
- Claude's: the beat sheet draft, the component choices, the render pipeline work.
- Accepted: the attrition chain as the scope visual.
- Rejected/changed: nothing substantive on this reel.
- Evidence: `FACTCHECK.md` lists all 15 on-screen claims with sources.

**What I understand now, and what I still do not.**
- Understood: the gate order in this toolkit is not advisory. Writing the documents
  first is faster than writing them after a refusal.
- Open: nothing on this reel.
