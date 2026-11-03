# Frictional Log — Mixture of Experts

> Append dated entries as you go; never rewrite an earlier one.

## 2026-09-18 — Build a 60-second explainer on Mixture of Experts, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I expected the story to be "a model made of specialist sub-models" and wanted real parameter counts to show the saving. I also wanted the router step to be the visual centrepiece.

- **Where it resisted, and what I did next:**
  The sources corrected my framing: experts are feed-forward blocks inside each layer, not whole specialist models, and the active share isn't simply two-eighths because shared weights always run. The opening hesitant-writer correction didn't fire at first because it only swaps single words, so it was rewritten. The type check also flagged contrast on a few bars, which were darkened.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the scenes, checked the numbers against the Mixtral and DeepSeek-V3 papers, and fixed the issues the checks found. I accepted using the published 13B figure instead of a neat ratio. It also avoided having the voice say "MoE" because of pronunciation risk.

- **What I understand now, and what I still do not:**
  I understand the trade: more capacity without every token paying full compute, but with every expert held in memory. I didn't cover how routers are trained to balance load across experts, which would be a good follow-up.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md)
