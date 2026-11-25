# SCRIPT — Quantization: Big AI on a Laptop

Narration as generated. **AI voice** (Kokoro `am_onyx`), not a recording of Likhith.

**B00 · ASK** — Hi, I am Likhith, and this video is about quantization, and how big AI models fit on a laptop.

**B01 · BLUF** — The idea: to shrink a model, you don't cut its weights. You round them.

**B02 · HOOK** — A 70 billion weight model needs 140 gigabytes. Yet laptops run big models. How?

**B03 · FRAMEWORK** — Every weight is a number, two bytes each. Seven billion: 14 gigabytes.

**B04 · MECHANISM** — Quantization stores each weight in fewer bits, eight or four, by rounding it onto a small grid.

**B05 · MECHANISM** — Eight bits gives 256 levels; four, just 16. A scale per group maps them back.

**B06 · EVIDENCE** — So 14 gigabytes becomes 7, then three and a half, and often faster: memory is the bottleneck.

**B07 · EVIDENCE** — Rounding errors mostly cancel. GPTQ corrects them; AWQ guards the key weights.

**B08 · TRADEOFF** — The limit: below four bits, quality drops. Small models, maths and code suffer first.

**B09 · VERDICT** — llama.cpp and Ollama made 4-bit the local default. Same model, fewer bits.

**B10 · YOUR_TURN** — Your turn. Ask Claude: which 4-bit model fits my laptop, and what do I lose? Then test it.

**B11 · OUTRO** — Quantization: big AI on a laptop. At Humanitarians AI.
