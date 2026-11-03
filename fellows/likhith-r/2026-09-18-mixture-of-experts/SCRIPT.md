# SCRIPT — Mixture of Experts

Narration as generated. **AI voice** (Kokoro `am_onyx`), not a recording of Likhith.

**B00 · ASK** — Hi, I am Likhith, and this video is about Mixture of Experts.

**B01 · BLUF** — Here's the idea. A huge model doesn't need all of itself for every single word. It calls on just a few experts, so it gets huge capacity at a small price.

**B02 · HOOK** — Models hold hundreds of billions of parameters. How are they still fast?

**B03 · FRAMEWORK** — A dense model runs every parameter for every token. Double the size, double the cost.

**B04 · MECHANISM** — Mixture of Experts splits each layer into many smaller experts.

**B05 · MECHANISM** — A small router scores the experts for each token, and picks two of eight.

**B06 · WORKED EXAMPLE** — Only those run. The rest sit idle, so each token pays for a slice.

**B07 · CONTRAST** — Mixtral holds forty-seven billion parameters, but uses about thirteen billion per token.

**B08 · FALSIFIABILITY** — The catch: memory. Every expert stays loaded, even if only two run.

**B09 · VERDICT** — Verdict: more capacity, without every token paying full price.

**B10 · YOUR_TURN** — Your turn. Ask Claude: walk me through how a Mixture of Experts router would route my sentence. Then ask what that leaves out.

**B11 · OUTRO** — Mixture of Experts. At Humanitarians A I.
