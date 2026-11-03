# Frictional log — ML for SERS Review Paper (Paper 2 of 3), Weeks 9–10

## 2026-10-10 — revising Section 4.5, Training Strategies for Limited Data

- **Period:** 28 Sep – 10 Oct 2026 (agreement weeks 9–10)
- **Video (progress):** https://drive.google.com/file/d/1IC8uWNKcDZ4Jg6oQ6XFIkkvC-ZqOvPHy/view?usp=share_link — *What Changed in Section 4.5?*
- **Evidence folder:** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/10102026_ProjectUpdate
- **Evidence:** paper draft, with the original and current versions of
  Section 4.5 (https://docs.google.com/document/d/1yMAE0CghIcEXnI67sW6jCQ1tVSY3qqnLF1kgoWTtlKo/edit);
  video source `beat_sheet.json`, `scenes.py`, `FACTCHECK.md` and
  `PROMPTS.md` in this folder
- **Backfilled:** written in October 2026 from the video materials and drafts.
- **Supervisor updates:** bi-weekly progress updates given to Edward Olano
  during this period; not written up or committed to GitHub at the time.

**What I was working on.** Section 4.5 of the review, on training models
when data is limited. Section 4 was split at random between Kunal and me. The original
section listed two strategies, data augmentation and self-supervised or
contrastive learning, and called SERS applications of self-supervised
learning "limited" without citing anything. The goal was a section that
tells readers which strategy to use when, and how far the evidence for each
actually goes.

**What I tried, and what I expected.**
- I expected the two strategies to be alternatives competing for the same
  problem, so the section would end by ranking them.
- I expected "peer-reviewed SERS applications are limited" to be a fair
  summary that only needed a citation or two.
- I expected that finding strong self-supervised results on Raman data would
  let me say the approach works for SERS.

**Where it resisted, and what I did next.**
- **The strategies solve different shortages.** Ranking them was the wrong
  question. The revision opens with one the draft never asked: what is
  actually scarce? Too few spectra overall points to augmentation first. Plenty
  of spectra but too few labels points to self-supervised pretraining.
- **Augmentation needed a rule, not just a warning.** The draft said
  excessive noise degrades performance. I turned that into a usable rule:
  set augmentation parameters from measured instrument and substrate noise.
  Augmentation is recommended first because it needs no new data collection.
- **Self-supervised learning needed a reason tied to SERS.** I tied it to the
  economics of the field: collecting raw spectra is cheap, but confirming what
  is in each one usually needs an independent reference method, which is
  expensive. So pretrain on the large unlabeled pool and fine-tune on the few
  spectra you can afford to label.
- **The uncited gap claim was replaced with evidence.** Ren et al.'s masked
  autoencoder, SMAE (2025), reached 83.90% after fine-tuning on limited
  labels, level with a fully supervised ResNet at 83.40%. Sun and Wang's
  SemiRaman (2026, *Spectrochimica Acta A*) reached 89.2% and 92.0% using
  only 5% and 10% labeled data. Those SemiRaman figures are not in the
  abstract, so I checked them against the full paper.
- **Both studies used conventional Raman spectra of bacteria, not SERS.**
  This was the main friction of the period. The results are strong, and it
  would have been easy to let them stand in for SERS evidence. Instead, the
  section now says plainly that self-supervised pretraining is promising and
  low-risk to test on SERS, but not validated there until someone
  demonstrates it on SERS data.
- **The fact-check found the revision still overclaims in one place.**
  Paragraph 4 opens by saying the approach "moved considerably faster from
  concept to practice" than the earlier framing suggested. The earlier claim
  was about SERS, and paragraph 4's own caveat confirms there is still no
  SERS demonstration. That sentence needs scoping to conventional Raman.
- **Video production:** the scene files carried lessons from the Section
  4.4 build. They included passing font weights as strings because the
  build gate's stub lacked the constants, adding a footer caption from the
  first second to keep frame fill above the gate threshold, and sizing scene
  lengths to the narration voice's real pace of about 3.25 words per second.

**What Claude contributed, and what I did with it.**
- During research: I used AI mostly to find links to relevant papers.
  I read those papers myself, asked AI whether my reading of them made
  sense, and then rewrote Section 4.5 against the guidelines we had set
  for every section.
- Video: the beat sheet, Manim scenes and fact-check were written with
  Claude from my original Section 4.5, my revision and my change log. I
  approved the beat structure before any files were written, and I checked
  the SemiRaman 5% and 10% figures against the full paper myself.
- Accepted: framing the video's opening as a "tempting conclusion" (proven →
  untested), so it does not attribute an overclaim to either draft; labelling
  the spectrum, noise bands and dot counts as illustrative or schematic.
- Rejected or changed: treating the SMAE and SemiRaman results as SERS
  evidence. Reading both papers showed they used conventional Raman spectra
  of bacteria, so I scoped the claim to Raman.
- This log was drafted with Claude from my beat sheet, scenes and fact-check.
  I reviewed and corrected it.

**What I understand now, and what I still do not.**
- Understood: "limited data" is two different problems. Too few spectra and
  too few labels call for different first moves.
- Understood: augmentation only helps if it is realistic. Noise far beyond
  what the instrument produces trains the model for conditions it will never
  see.
- Understood: the cost asymmetry in SERS, cheap spectra and expensive
  labels, is the actual argument for self-supervised learning, more than any
  benchmark score.
- Understood: evidence from conventional Raman can motivate a SERS
  experiment, but it cannot validate one. This is the third section in a row
  where the honest answer was to state the scope next to the result.
- Not understood: [FILL: an honest open question, for example whether
  representations pretrained on SERS spectra would transfer across
  substrates, given how much hot-spot variability changes the spectra]
- Still open: rescope the opening of paragraph 4 to conventional Raman; add a
  citation for the excessive-noise claim or present it as reasoning; confirm
  that the *Expert Systems with Applications* version of Ren et al. reports
  the same figures as the arXiv preprint.
