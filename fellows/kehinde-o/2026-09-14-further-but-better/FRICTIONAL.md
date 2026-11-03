# Frictional log — Explainer: Further, But Better

## 2026-09-14 — a result that sounds wrong until you measure the right thing

- **Video:** not yet published
- **Drive:** https://drive.google.com/drive/folders/1V-BZnGQ8a2soQqO7zD2N_atkRd7OYYPp (`Medhavy_Kehinde/STEM Topic/further-but-better/`)
- **Report:** [REPORT.md](REPORT.md)
- **Source project:** https://github.com/Kenny0bi/quantlab
- **Paired report:** [Fact-Checking Chapter 23](../2026-09-14-chapter-23-review/)

**What I was working on.** An explainer on post-training quantization, built on my
own `quantlab` repo: three methods implemented from their papers and measured
across 34 configurations on GPT-2.

**What I tried, and what I expected.**
- I expected the best method to be the one that keeps the compressed weights
  closest to the originals. That is the intuition the whole topic seems to rest on.

**Where it resisted, and what I did next.**
- **The winning method moves the weights further away.** GPTQ ends about 2.5x
  further from the original weights than naive rounding, and its outputs are about
  twice as accurate. Stated plainly that sounds like a mistake, which is exactly
  why it makes a good explainer: distance in weight space is not damage in loss
  space.
- **The video needed my own animation, and re-rendering it was not optional.** The
  repo ships a 1080p mp4. Upscaling it would have failed the 4K-at-source
  requirement, so the Manim scene was re-rendered at 3840x2160 from source.
- **The toolkit had changed under me.** A required paperwork set (fact-check,
  shotlist, prompts) had been added upstream and blocked every master until it
  existed. Writing those properly was the right outcome but it was not planned work.
- **The vertical cut exposed a layout fault** that had been latent in the earlier
  weeks: components laid out for a wide frame bled past the safe area in portrait.
  A first attempt at fixing it by scaling the type up overcorrected and bled
  further. The fix that worked was authoring shorter lines in the portrait beat
  sheet rather than resizing.

**What Claude contributed, and what I did with it.**
- Mine: the implementations, the 34-configuration sweep, the Manim scene and the
  argument the video makes.
- Claude's: the beat sheet, the 4K re-render of my animation, and the portrait
  layout fixes.
- Accepted: keeping my own dark violet palette in the animation rather than
  retinting it to match the video's cream styling. The palette is part of the work.
- Rejected/changed: two attempts at the portrait fix that made it worse before the
  line-length approach was tried.
- Evidence: the repository above; the measured perplexity figures quoted in the
  beat sheet.

**What I understand now, and what I still do not.**
- Understood: the quantity you optimise has to be the quantity you care about.
  Rounding to the nearest value optimises weight distance, which is not what the
  model is judged on.
- Understood: a deadline-driven toolkit upgrade mid-build costs more than doing the
  paperwork up front.
- Not resolved: I measured GPT-2 only. Whether the same ordering holds at larger
  scale is not something this project shows.
