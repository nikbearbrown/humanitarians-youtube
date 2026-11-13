# Frictional log — ML for SERS Review Paper (Paper 2 of 3), Weeks 7–8

## 2026-09-27 — revising Section 4.4, Hybrid and Multi-Task Architectures

- **Period:** 14–27 Sep 2026 (agreement weeks 7–8)
- **Video (progress):** https://drive.google.com/file/d/1PrcdTqEzoUHAYqTdwhzb7Wx5dqrQTFne/view?usp=share_link — *What Changed in Section 4.4?*
- **Evidence folder:** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/kumar-n/09272026_ProjectUpdate
- **Evidence:** paper draft, with the original and current versions of
  Section 4.4 (https://docs.google.com/document/d/1yMAE0CghIcEXnI67sW6jCQ1tVSY3qqnLF1kgoWTtlKo/edit);
  video source `beat_sheet.json`, `scenes.py`, `FACTCHECK.md` and
  `PROMPTS.md` in this folder
- **Backfilled:** written in October 2026 from the video materials and drafts,
  not during the weeks it describes.
- **Supervisor updates:** bi-weekly progress updates given to Edward Olano
  during this period; not written up or committed to GitHub at the time.

**What I was working on.** Section 4.4 of the review, on hybrid and
multi-task architectures: models that combine network types, or that
classify and quantify from one measurement. Section 4 was split at random between Kunal and
me, and 4.4 was one of mine. The original section was two short paragraphs that described
ResFusionNet-TSMT and a physics-constrained autoencoder study without
judging either. The goal, under the same guidelines document as before, was
a section that tells readers when these models are worth their complexity.

**What I tried, and what I expected.**
- I expected the claim that joint training "often" improves both tasks to
  be well established, so it would only need a citation added.
- I expected reference U-55 to be correct as listed, since it had a real
  title and DOI.
- I expected that once I found a controlled comparison, describing it
  accurately would be the easy part.

**Where it resisted, and what I did next.**
- **The "often helps" claim had no source behind it.** The draft said joint
  training often improves performance on both tasks relative to separately
  trained models, with no citation. Instead of finding something to support
  it, I looked for a controlled test. Shamim et al. (2026, arXiv:2607.16493)
  compared an attention-enhanced multi-task model (AMTLNet) against the
  strongest single-task baseline on a leakage-audited split. The multi-task
  model scored 84.12%; the single-task CNN-LSTM scored 84.20%, and the
  difference was not significant (Tukey p = 1.0). "Often" became
  "sometimes, under specific conditions."
- **The counter-evidence comes from outside SERS, and it is a preprint.** It
  is fault diagnosis on engine and bearing data, not spectroscopy. I kept
  both caveats next to the result, in the paper and on screen, so it reads as
  a controlled counterpoint rather than proof about SERS.
- **The same study showed the evaluation protocol mattering as much as the
  architecture.** With the same model on the same bearing data, a naive
  window-level split gave 99.9%, a degenerate coarse split collapsed toward
  0%, and a leakage-free split gave about 30% (±15). Based on this, the
  revision sets a default: when two tasks are not naturally coupled, train a
  separate classifier and regressor, which are easier to debug and
  interpret.
- **The autoencoder paragraph reported a result without a mechanism.** I
  added the missing explanation: a model trained only to reconstruct a
  spectrum can hit that target with physically impossible outputs, such as
  negative concentrations, and building non-negativity into the model
  removes that failure. This matters for wastewater, where every spectrum is
  a mixture of contaminants.
- **Reference U-55 had the wrong authors.** It was listed as Shao et al. The
  paper with that title and DOI is by Georgiev, Fernández-Galiana, Vilms
  Pedersen, Papadopoulos, Xie, Stevens and Barahona (*PNAS*, 2024). I
  corrected the attribution.
- **I described the Shamim comparison wrongly, and the video fact-check
  caught it.** I had called it an "identical-backbone" test, but the 84.12%
  versus 84.20% result compares two *different* encoders. The study has a
  separate identical-backbone section whose figures I had not used. The
  video was corrected before release; the paper still says
  "identical-backbone" and needs the same fix.
- **One ResFusionNet claim could not be confirmed.** The paper says it
  includes a class-attention mechanism for low-concentration samples, but I
  could only verify dual-stream inputs and attention pooling from the
  abstract. The video states only the verified features; the paper's claim
  is still open until I read the full Tan et al. text.

**What Claude contributed, and what I did with it.**
- During research: I used AI mostly to find links to relevant papers.
  I read those papers myself, asked AI whether my reading of them made
  sense, and then rewrote Section 4.4 against the guidelines we had set
  for every section.
- Video: the beat sheet, Manim scenes and fact-check were written with
  Claude from my original Section 4.4, my revision and my change log. I
  approved the beat structure before any files were written and reviewed
  the results.
- Accepted: the fact-check's three corrections to the video: dropping
  "identical-backbone", replacing the 84.12% figure on the audited-split
  track with the ≈30% bearing result so "same data, same model" held, and
  narrowing the ResFusionNet description to verified features.
- Rejected or changed: the draft's uncited claim that multi-task learning
  "often" helps, which the Shamim et al. comparison did not support, and
  the U-55 author list, which did not match the paper with that title and
  DOI.
- This log was drafted with Claude from my beat sheet, scenes and fact-check.
  I reviewed and corrected it.

**What I understand now, and what I still do not.**
- Understood: a frequent claim is not an established one. The honest fix for
  "often helps" was a controlled test, not a supporting citation.
- Understood: how the data is split can change accuracy more than the choice
  of model. A reported number means little until I know whether the split
  was by sample or by spectrum.
- Understood: a physical constraint is a good reason for architectural
  complexity. A reconstruction score can look good while the outputs are
  impossible.
- Understood: fact-checking the video found errors in the paper, not only in
  the video. Explaining a revision in public is itself a check on it.
- Not understood: [FILL: an honest open question, for example whether the
  multi-task result would hold on SERS data, where the classification and
  quantification tasks may be more tightly coupled than fault diagnosis and
  remaining-life estimation]
- Still open: remove "identical-backbone" from Section 4.4; confirm the
  class-attention claim against the full Tan et al. paper; apply the
  Georgiev attribution everywhere U-55 appears, including the reference
  mapping document.
