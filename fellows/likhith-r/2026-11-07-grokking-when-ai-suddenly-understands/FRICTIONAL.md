# Frictional Log — Grokking: When AI Suddenly Understands

> Append dated entries as you go; never rewrite an earlier one.

## 2026-11-07 — Build a 60-second explainer on Grokking, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I gave eight points, from the hook to Heinlein's word, and wanted every curve on screen to come from a real run. I expected the small numpy run might never show the jump and would need a smaller modulus.

- **Where it resisted, and what I did next:**
  It grokked on the first full run at mod 97, about 17 minutes for both runs, so nothing had to be changed. The harder part was timing: in the first render the opening beat was too short and the AI-narration line never appeared, so the beats were re-timed. At the faster voice speed, "weight decay" was heard as "Wait the K", so that beat stayed slower. The type check flagged arrow glyphs, fused grid cells and axis ticks, which were redrawn.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the training script and the scenes, checked the claims against Power et al. 2022, Nanda et al. 2023, Varma et al. 2023 and Heinlein, and fixed the timing and type-check issues. I accepted that the explanation is the field's account, shown next to our own control.

- **What I understand now, and what I still do not:**
  I understand why weight decay makes the rule cheaper than the lookup table, and I saw the delayed jump in my own run. I don't yet know how the delay depends on how much of the table the model sees.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
