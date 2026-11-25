# SHOTLIST — Quantization: Big AI on a Laptop

Native 16:9 (3840×2160) and 9:16 (2160×3840, `vertical/`). 12 beats · Kokoro `am_onyx` (speed 1.2) · @HumanitariansAI · 60.000 s.

| # | Act | Pattern (→ 916 twin) | Show |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | "Namaskaram, Likhith" (9:16 "Hey, Likhith") · ask · 4 lines, first = "narrated by an AI voice" |
| B01 | BLUF | BrutalistHesitantWriter | "To shrink a model, cut its weights." → "round" |
| B02 | HOOK | QzHook | 70,000,000,000 × 2 bytes counter · 140 GB bar vs a 16 GB laptop · "8.75× too big" |
| B03 | FRAMEWORK | QzWeights | 24 real toy weights · +0.0172 → its 16 bits (± / exponent / mantissa) · = 14 GB |
| B04 | MECHANISM | QzGrid | 8 weights on a number line snap to the 4-bit grid · stored levels + one scale |
| B05 | MECHANISM | QzLevels | 256-tick vs 16-tick rulers · ŵ = s · q · 43.3 % vs 13.1 % error |
| B06 | EVIDENCE | QzPayoff | 14 / 7 / 3.5 GB bars · tokens/s bound 7.1 / 14.3 / 28.6 |
| B07 | EVIDENCE | QzCancel | error histogram · 6.62 vs 0.134 (49×) · outlier crushes 27 of 31 neighbours · GPTQ / AWQ |
| B08 | TRADEOFF | QzLimit | weight-error curve 8 → 2 bits, shaded below 4 · small models · maths · code |
| B09 | VERDICT | QzLocal | llama.cpp + Ollama logos · 4-bit by default (GGUF Q4_K_M) · 3 verdict lines |
| B10 | YOUR TURN | ClaudeComposerAsk | prompt read aloud |
| B11 | OUTRO | HaiOutro | HAI mark · title · Subscribe · "Narrated by an AI voice." |
