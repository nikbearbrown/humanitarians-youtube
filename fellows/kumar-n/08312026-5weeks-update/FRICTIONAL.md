# Frictional log — ML for SERS Review Paper (Paper 2 of 3), Weeks 1–4

## 2026-08-31 — rewriting Sections 2.4–2.6 and 3.3–3.5

- **Period:** 3–31 Aug 2026 (agreement weeks 1–4)
- **Video (progress):** https://drive.google.com/file/d/19nsmO86GMq5KFVTzu0dVtudDOF0Gy6Nx/view?usp=share_link — *Machine Learning for SERS: From a Draft to a Real Paper*
- **Evidence folder:** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/08312026-5weeks-update
- **Evidence:** paper draft, with the original and current versions of
  Sections 2.4–2.6 and 3.3–3.5 (https://docs.google.com/document/d/1yMAE0CghIcEXnI67sW6jCQ1tVSY3qqnLF1kgoWTtlKo/edit);
  reference mapping `References_SERS_Review_Paper_Mapping_4Aug2026.docx`;
  video source `beat_sheet.json` and `scenes.py` in this folder
- **Backfilled:** written in October 2026 from the video materials and drafts,
  not during the weeks it describes. See process friction below.

**What I was working on.** Turning the AI-generated first draft of Paper 2 in
the RAMAN Effect series into a review with real citations and an actual
argument. The introduction went to the project manager first, because it
needed chemistry background neither writer had; we then added the machine
learning framing. After that the sections were split at random
between my teammate Kunal and me. Kunal took 2.1–2.3 and 3.1–3.2. I took 2.4 (spectral alignment),
2.5 (dimensionality reduction), 2.6 (SERS-specific preprocessing), 3.3
(ensembles), 3.4 (the validation framework) and 3.5 (the summary table).

**What I tried, and what I expected.**
- I expected the first draft to need polishing, not rebuilding. It covered
  every method, from cosmic ray removal to baseline correction, and it looked
  finished.
- I expected the references to be usable as given, so the work would mostly
  be wording.
- I expected that a claim stated as a specific number, like a 10–30
  percentage point performance gap, had a source somewhere.
- I expected ensembling to be a safe recommendation, since combining models
  sounds like a free improvement.

**Where it resisted, and what I did next.**
- **Every section only defined its topic.** None said why the method mattered
  or what to do with it. The team wrote a guidelines document that forced
  every section to answer three questions: what has actually been done, why
  it works or fails, and what we recommend based on the evidence. A section
  that only defined a term was not finished.
- **Several references either did not exist or did not say what the draft
  claimed.** That changed how the work was scheduled. Each section ran on the
  same two-week cycle: a research week checking every citation against its
  source, then a rewrite week using what the research turned up. The cycle
  ran once for my Section 2 block and once for my Section 3 block, with
  research and rewrite weeks alternating: 3–7 Aug researching Section 2,
  10–14 Aug rewriting it, 17–21 Aug researching Section 3 and 24–28 Aug
  rewriting it. Each research or rewrite week took around 20–25 hours.
- **2.4 had to be written from scratch.** I added real citations for both
  alignment methods and a caveat that alignment can itself introduce error
  if the reference spectrum is chosen badly.
- **2.5 needed a stronger warning:** PCA must be fit on training data only,
  never on the full dataset before splitting, or the test set leaks into
  training. I also added a forward link to the deep learning section:
  automatic feature learning needs far more data than hand-built features
  before it pays off.
- **2.6 had claims with no evidence behind them.** I found two studies to
  support them. Zhao et al. (2025) trained on deliberately varied hot-spot
  conditions instead of identical ones and cut prediction error by 84.8%, so
  hot-spot variability can be a training signal rather than only noise to
  average away. Guo et al. (2020) measured the same samples on 35
  instruments across 15 institutes and found systematic differences caused by
  the hardware, not the chemistry.
- **Ensembling turned out to be conditional.** One study combined four
  classifiers and beat each of them, reaching 97.9%. Another combined SVM and
  XGBoost and scored 76.1%, below XGBoost alone at 97.4%, because the two
  models disagreed over noisy data instead of complementing each other. That
  second case is a preprint, and I labelled it as one. Decision trees and
  logistic regression lost their standalone treatment, because in this
  literature they only appear as parts of someone else's ensemble.
- **Nobody could find a source for the 10–30 percentage point gap** in 3.4. I
  removed it and replaced it with the honest statement: the gap between
  reported and deployment accuracy has never been measured. The claim that no
  study has reached Tier 1 validation got the same treatment, scoped to the
  databases and years actually searched rather than stated as a fact about
  the whole field.
- **The summary table had a citation that did not belong.** The Rothemund et
  al. random forest study sat in the table as SERS evidence, but it was fecal
  source testing that never used Raman spectroscopy; it had been included
  only because it used the same algorithm. I removed it. I closed the
  long-open PLSR citation gap with Hou et al. (2016), a real SERS
  quantification study. I split the ensemble row into two rows,
  heterogeneous and voting ensembles, because it had mixed two different
  approaches.
- **Process friction:** I gave bi-weekly progress updates to my supervisor,
  Edward Olano, but I did not write them up as documentation or commit them
  to GitHub, which my agreement requires. This log is backfilled from my
  video materials and drafts, and labelled as such.

**What Claude contributed, and what I did with it.**
- The first draft of the paper was generated by AI.
- During research: I used AI mostly to find links to relevant papers.
  I read those papers myself, asked AI whether my reading of them made
  sense, and then rewrote my sections against the guidelines we had set
  for every section.
- Accepted: links to candidate papers, but only as leads. Nothing went
  into the paper until I had read the source.
- Rejected or changed: much of the AI-generated first draft. Several of its
  references did not exist or did not say what the draft claimed, and its
  10–30 percentage point figure had no source at all.
- Video: I gave Claude the information about the rewrite and asked it to
  write the beat sheet and the Manim scene files. I reviewed them.
- This log was drafted with Claude from my beat sheet and scenes. I reviewed
  and corrected it.

**What I understand now, and what I still do not.**
- Understood: a draft can be complete and still hollow. Defining a method is
  not the same as explaining why it matters or what to do about it.
- Understood: a specific-sounding number is not evidence. "This has never
  been measured" is a real research gap, and it is more useful than a figure
  nobody can trace.
- Understood: a mismatched citation reads as false evidence. A study that
  shares an algorithm is not evidence for a different measurement technique.
- Understood: data leakage happens in the order of operations, not in the
  model. Any transformation fit on the full dataset before the split inflates
  the result.
- Understood: ensembling helps only when the models fail in different ways.
  It should not be the default.
- Not understood: [FILL: an honest open question, for example whether Zhao
  et al.'s varied-hot-spot result transfers to other substrates and analytes]
- Still open: check that U-23 (Li et al., 2015) is described with the method
  it actually used, since its title names SVM and the draft says PCA-LDA;
  check that U-21 supports the claim about portable instruments; check that
  the citations shown under the PCA leakage diagram in the video belong to
  that claim.
