# Frictional log — ML for SERS Review Paper (Paper 2 of 3), Weeks 11–12

## 2026-10-18 — revising Section 4.6, Practical Deployment Considerations

- **Period:** 11–24 Oct 2026 (agreement weeks 11–12)
- **Video (progress):** https://drive.google.com/file/d/1Y8sDrNScZtMCfVsPoFP1K1vd1Iab8vYz/view?usp=share_link — *What Changed in Section 4.6?*
- **Evidence folder:** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/10182026_ProjectUpdate
- **Evidence:** paper draft, with the original and current versions of
  Section 4.6 (https://docs.google.com/document/d/1yMAE0CghIcEXnI67sW6jCQ1tVSY3qqnLF1kgoWTtlKo/edit);
  video source `beat_sheet.json`, `scenes.py`, `FACTCHECK.md` and
  `PROMPTS.md` in this folder
- **Supervisor updates:** bi-weekly progress updates given to Edward Olano
  during this period; not written up or committed to GitHub at the time.

**What I was working on.** Section 4.6 of the review, on what happens when a
model leaves the lab. Section 4 was split at random between Kunal and me. It has three
parts: computational requirements, interpretability and generalization
across conditions. Unlike the earlier sections, my approach here was to
check each part before deciding whether it needed rewriting at all.

**What I tried, and what I expected.**
- I expected all three subsections to need the same kind of rewrite as
  Sections 4.4 and 4.5.
- I expected the claim that compression cuts inference costs by "one to two
  orders of magnitude" to be standard and easy to source.
- I expected interpretability to still be an open problem, as the draft
  said.
- I expected my literature search to have settled the generalization
  question: that there was no SERS-specific proof-of-concept.

**Where it resisted, and what I did next.**
- **The three subsections needed three different fixes.** Compute needed
  reframing, interpretability needed updating, and generalization needed
  qualifying. Treating them alike would have meant rewriting parts that
  only needed checking.
- **Compute: the evidence is real, but it is not SERS evidence.** Pruning,
  quantization and distillation can shrink models dramatically, so the
  revision makes compression the default path to field deployment. But that
  evidence comes from general deep learning. I found no published result
  showing a compressed SERS model holding its accuracy under real substrate
  and hot-spot variability. The section now recommends compression with an
  expected accuracy cost, rather than as a free step.
- **The "one to two orders of magnitude" figure is uncited in both
  drafts.** It was kept out of the video and still needs a source in the
  paper.
- **Interpretability had moved on since the draft.** The draft called
  mechanistically grounded explanation an open problem. Dedicated methods now
  exist: Zaki et al.'s CRIME (2025, *ACS Sensors*), built for explaining SERS
  mixture quantification, and Yang et al.'s GRASS (2026, *Spectrochimica
  Acta A*), which segments a Raman spectrum into continuous regions before
  scoring them with SHAP, instead of scoring each wavenumber alone. The
  recommendation is now to use a dedicated spectral method rather than
  unmodified GradCAM.
- **My generalization claim was wrong, and the fact-check caught it.** The
  revision said a literature search had not surfaced a SERS-specific
  application, and that this was the one area in Section 4 without even an
  initial proof-of-concept. Checking for the video turned up Mahmud et al.,
  a SERS study that translates spectra from four portable instruments to a
  lab-grade reference on silver nanorod substrates. I agreed to revise the
  claim: early SERS cross-device work exists, but it covers devices on one
  substrate type. Cross-site and cross-substrate generalization are still
  open.
- **One reference in my revision could not be located.** Kalatzis and Nega
  (2026) was left out of the video because it could not be found during
  checking. [FILL: whether you have located it. If not, remove it from the
  paper. After the U-55 author error, an unlocatable reference should be
  treated as possibly invented until proven otherwise.]
- **The draft's core generalization claim still rests on [U-29].** That
  reference is still marked CITATION NEEDED in the paper's reference list.
  [Note for the author: your reference mapping assigns U-29 to Pérez-Jiménez
  et al., 2020, *Chem. Sci.* Check whether that paper supports the claim.]
- **Video production:** the scene files carried forward the build lessons
  from 4.4 and 4.5, and added two more: captions that change in place are built by a helper
  because the build gate reads literal coordinates, and translucent fills
  stay at or above 0.4 opacity to pass the contrast gate.

**What Claude contributed, and what I did with it.**
- During research: I used AI mostly to find links to relevant papers.
  I read those papers myself, asked AI whether my reading of them made
  sense, and then rewrote Section 4.6 against the guidelines we had set
  for every section.
- Video: the beat sheet, Manim scenes and fact-check were written with
  Claude from my original Section 4.6, my revision and my change log. I
  approved the beat structure before any files were written.
- The fact-check surfaced Mahmud et al., which contradicted my revision's
  claim that no SERS proof-of-concept existed. I verified it and approved
  changing the generalization framing in both the video and the paper.
- Accepted: dropping the uncited compression figure from screen; omitting
  the reference that could not be located; labelling the spectrum and
  attribution bars as illustrative.
- Rejected or changed: the draft's claim that mechanistic interpretability
  was an open problem, which was out of date once I read the CRIME and
  GRASS papers.
- This log was drafted with Claude from my beat sheet, scenes and fact-check.
  I reviewed and corrected it.

**What I understand now, and what I still do not.**
- Understood: revising does not always mean rewriting. Checking each claim
  first showed that one part needed a new framing, one needed new sources
  and one needed narrowing.
- Understood: "no study exists" is only as strong as the search behind it.
  My search missed a relevant SERS paper, so absence claims should name the
  databases and dates searched, as Section 3.4 already does for Tier 1.
- Understood: a field can move during a review. Interpretability went from
  open problem to dedicated methods within the paper's own timeline.
- Understood: generalization is three problems, not one. Device, site and
  substrate batch shift need separate evidence, and only the first has any
  SERS work so far.
- Not understood: [FILL: an honest open question, for example whether a
  cross-device translation model like Mahmud et al.'s would itself need
  retraining for each new substrate batch]
- Still open: cite Mahmud et al. and remove "not yet produced even an
  initial proof-of-concept"; source the compression figure; resolve [U-29];
  locate or remove Kalatzis and Nega (2026); confirm GRASS's comparison
  against GradCAM and LIME from the full text.
