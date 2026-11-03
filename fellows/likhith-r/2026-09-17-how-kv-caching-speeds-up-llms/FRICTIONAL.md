# Frictional Log — How KV Caching Speeds Up LLMs

> Append dated entries as you go; never rewrite an earlier one.

## 2026-09-17 — Build a 60-second explainer on KV caching, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I gave seven points, including the idea that LLMs get faster per token as a response goes on. I expected the main job to be showing the cache clearly, with real counts behind the "quadratic to linear" claim.

- **Where it resisted, and what I did next:**
  Fact-checking pushed back on my own brief: after the first token the cost is roughly steady, not accelerating, so that point was corrected. The memory numbers needed a real published model shape, and the equation had to be simplified to stay readable. The portrait version needed merged labels to clear the text-size floor.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the scenes, and wrote a small script that decodes the same text with and without a cache and confirms the outputs match, which is where the counts on screen come from. I accepted the correction to my brief. It also fixed layout issues found in frame checks.

- **What I understand now, and what I still do not:**
  I understand the pause is prefill filling the cache, and that the cache trades memory for compute. I only touch on how batch size and grouped-query attention change the memory cost; that's worth a deeper look.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
