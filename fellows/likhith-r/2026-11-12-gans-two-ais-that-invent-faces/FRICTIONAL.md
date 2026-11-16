# Frictional Log — GANs: Two AIs That Invent Faces

> Append dated entries as you go; never rewrite an earlier one.

## 2026-11-12 — Build a 60-second explainer on GANs, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I asked for a GAN video that also explains the dangers and the cautions we should take. I expected a tiny numpy GAN to reach 50 % detective accuracy without trouble, and the danger section to be the hardest part to keep accurate in a few seconds.

- **Where it resisted, and what I did next:**
  The first training setup failed: the detective never learned, so a 50 % reading would have been meaningless. It was rejected and kept in the logs, and the second setup, with five detective steps per forger step, was run once. No free local model makes photoreal faces, so the faces are labelled drawings. The voice kept swallowing "-ed" endings in the danger line, so it was reworded. The type check read the drawn face's features as tiny text, so they were recoloured.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the GAN script and the scenes, checked the claims against the 2014 paper, the StyleGAN paper, the Hong Kong police reporting, Arup's confirmation and the C2PA standard, and fixed the layout and type-check issues. I accepted the rejected first run, the drawn stand-ins and the diffusion footnote.

- **What I understand now, and what I still do not:**
  I understand why the game ends at a coin flip and why that makes fakes hard to spot by eye. I'm less sure how well content credentials survive in practice once images are re-shared.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
