# SCRIPT — How KV Caching Speeds Up LLMs

Narration as generated. **AI voice** (Kokoro `am_onyx`), not a recording of Likhith.

**B00 · ASK** — Hi, I am Likhith, and this video is about K V caching.

**B01 · BLUF** — Here's the idea. Each new word a model writes looks back at every word before it. Instead of redoing that work each time, it saves the results, and reuses them.

**B02 · HOOK** — Why does a chatbot pause first, then stream the rest so fast?

**B03 · PROBLEM** — Without a cache, each new token recomputes attention over every earlier token.

**B04 · FRAMEWORK** — Each token makes a query, key, and value. Past keys and values never change.

**B05 · MECHANISM** — So the model stores them: the K V cache. Filling it from your prompt is the pause.

**B06 · MECHANISM** — Then each new token brings just its query, against the cached keys and values.

**B07 · EVIDENCE** — Per new token, work drops from quadratic to roughly linear.

**B08 · TRADEOFF** — The price: memory. It grows with every token, so long contexts need memory, not just compute.

**B09 · VERDICT** — Verdict: text streams fast after the first word, and long contexts eat memory.

**B10 · YOUR_TURN** — Your turn. Ask Claude: estimate the K V cache for a model and context I pick, and what to shrink first. Check its math.

**B11 · OUTRO** — How K V caching speeds up L L Ms. At Humanitarians A I.
