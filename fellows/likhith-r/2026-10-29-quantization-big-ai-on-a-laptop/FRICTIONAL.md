# Frictional Log — Quantization: Big AI on a Laptop

> Append dated entries as you go; never rewrite an earlier one.

## 2026-10-29 — Build a 60-second explainer on Quantization, in 16:9 and 9:16

*Drafted with Claude Code from the build record and reviewed by me.*

- **What I tried, and what I expected:**
  I gave eight points, from the 140 GB problem to 4-bit becoming the local default, and expected the story to be that quantization trades quality for size. I wanted every number on screen to come from code, so a small seeded numpy run produced the sizes, levels and errors.

- **Where it resisted, and what I did next:**
  The fact-check corrected my point on GPTQ and AWQ: they don't do the same thing. The first draft ran 66.5 s, so the narration was trimmed three times without dropping a point. The one-word correction in the opening line never finished on time until it was a single mid-sentence trigger. When I watched it, "Your turn" wasn't pronounced properly, so it got a pronunciation fix, along with my name and llama.cpp. The type check then flagged the bright accent colour and some small lowercase headings, which were darkened and set on filled chips.

- **What Claude or another person contributed — and what I accepted, changed, or rejected:**
  Claude Code drafted the beat sheet, wrote the scenes and the evidence script, checked the claims against the GPTQ and AWQ papers and the llama.cpp / Ollama docs, and fixed the layout and type-check issues. I accepted the GPTQ/AWQ correction and the "about 3.5 GB" wording.

- **What I understand now, and what I still do not:**
  I understand why fewer bits means less memory and often more speed, and why rounding errors mostly cancel. I haven't yet measured what 4-bit costs on a real model on my own machine.

- **Evidence:** [beat sheet](beat_sheet.json) · [vertical beat sheet](vertical/beat_sheet.json) · [build log](BUILD-LOG.md) · [fact-check](FACTCHECK.md) · [evidence](evidence/)
