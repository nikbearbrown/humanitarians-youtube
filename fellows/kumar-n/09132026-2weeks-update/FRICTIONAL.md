# Frictional log — ML for SERS Review Paper (Paper 2 of 3), Weeks 5–6

## 2026-09-13 — revising Section 4.2, Transformer Architectures

- **Period:** 1–13 Sep 2026 (agreement weeks 5–6)
- **Video (progress):** https://drive.google.com/file/d/1kEl2exl4Ir8VLZ_uphFgBxbwqUb0xIfP/view?usp=share_link — *Transformers in SERS-ML: What the Rewrite Actually Fixed*
- **Evidence folder:** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/09132026-2weeks-update
- **Evidence:** paper draft, with the original and current versions of
  Section 4.2 (https://docs.google.com/document/d/1yMAE0CghIcEXnI67sW6jCQ1tVSY3qqnLF1kgoWTtlKo/edit);
  video source `beat_sheet.json`, `scenes.py`, `FACTCHECK.md` and
  `PROMPTS.md` in this folder
- **Backfilled:** written in October 2026 from the video materials and drafts,
  not during the weeks it describes.
- **Supervisor updates:** bi-weekly progress updates given to Edward Olano
  during this period; not written up or committed to GitHub at the time.

**What I was working on.** Section 4.2 of the review, on transformer
architectures for SERS. Section 4 was split at random between Kunal and me,
as Sections 2 and 3 were in August. The first draft summarized
three transformer studies: Wang et al.'s Raman Spectral Translation network,
Zhang et al.'s TMNet and Hajikhani et al.'s SERSFormer-2.0. The job was to
turn that summary into an argument, using the same guidelines document as
in August: what has been done, why it works or fails, and what we
recommend.

**What I tried, and what I expected.**
- I expected 4.2 to need a polish pass. It covered three studies in full
  detail, including methods, results and deployment concerns, and it read
  as complete.
- I expected a reported 100% identification rate to be a strong result
  that could stand on its own.
- I expected that a section citing three transformer papers would already
  show whether transformers beat CNNs on SERS data.

**Where it resisted, and what I did next.**
- **The section described evidence but never judged it.** It summarized the
  three studies and then stopped, with no verdict on when a transformer is
  worth choosing. This is exactly what the paper's guidelines are meant to
  catch. I added a closing recommendation: default to a CNN for most SERS
  classification work, and use a transformer only when the problem needs
  multi-task output or long-range spectral dependencies.
- **"100% positive identification rate in the tested conditions" had no
  context.** I went back to the Wang et al. paper. The figure came from a
  validation set of 75 spectra, collected under two laser power levels and
  a narrow range of integration times. I added those conditions. A perfect
  score on a small, narrow test is a strong result on a controlled trial,
  not evidence that the method generalizes, and the section now says so.
- **None of the three cited studies benchmarked a transformer against a CNN
  on the same data.** Without that comparison, there was no way to tell
  whether the architecture was doing the work or a well-tuned CNN would do
  as well. Flagging the gap was not enough, so I looked for a direct
  comparison.
- **The answer only turned up on the second revision pass.** Sineesh and
  Kamsali (2026, *Digital Discovery*, DOI 10.1039/D6DD00044D) compared five
  Raman deep learning architectures, a transformer among them, under one
  unified training and tuning protocol. The transformer finished last, more
  than five percentage points behind the best model. [CONFIRM: on which of
  the paper's datasets, or whether this is an average across them.]
- **The benchmark uses general Raman data, not SERS.** I kept that caveat in
  the text and on screen in the video rather than letting the result stand
  in for SERS evidence it does not provide. The new recommendation rests on
  it as independent evidence that a transformer does not automatically win,
  not as proof that CNNs are better for SERS.
- **Video production:** the video's `FACTCHECK.md` separates what could
  be checked directly (the three differences between the two drafts) from
  what rests on my own source-checking (the Wang et al. conditions and the
  benchmark result), instead of presenting everything as equally verified.
  The Manim scenes were adjusted so every reveal finishes in the first
  ~30% of each scene, because the build gate samples frames at 50% and 85%
  and was catching animations mid-reveal.

**What Claude contributed, and what I did with it.**
- During research: I used AI mostly to find links to relevant papers.
  I read those papers myself, asked AI whether my reading of them made
  sense, and then rewrote Section 4.2 against the guidelines we had set
  for every section.
- Accepted: links to candidate papers, but only as leads. Nothing went
  into the section until I had read the source.
- Rejected or changed: the draft's unqualified 100% figure for Wang et al.
  Reading the paper showed it held only on 75 spectra under narrow
  acquisition conditions, so I added those conditions.
- Video: I gave Claude the information about the revision and asked it to
  write the beat sheet, the Manim scene files and the fact-check. I
  reviewed them.
- This log was drafted with Claude from my beat sheet, scenes and fact-check.
  I reviewed and corrected it.

**What I understand now, and what I still do not.**
- Understood: summarizing studies is not the same as recommending from
  them. A section can describe every paper accurately and still not be
  finished.
- Understood: a perfect accuracy figure means little without its test
  conditions. Sample size and acquisition range decide what the number can
  support.
- Understood: noticing an evidence gap is only half the job. The section
  improved when I went looking for the missing comparison instead of only
  naming it.
- Understood: evidence from a neighbouring field can support a
  recommendation, but only if its scope is stated next to it.
- Not understood: [FILL: an honest open question, for example whether the
  benchmark ranking would hold on SERS data, where hot-spot variability
  adds noise that general Raman data does not have]
- Still open: B04's on-screen title in the video, "No Study Ever Tested Them
  Together", is broader than the claim, which is that none of the three
  *cited* studies did; B05 then shows a study that did. The B05 bars are
  schematic heights with no figures, but the video does not label them as
  schematic.
