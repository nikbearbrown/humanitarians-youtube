# SCRIPT — Monorepos vs. Polyrepos

Narration as generated. **AI voice** (Kokoro `am_onyx`), not a recording of Likhith.

**B00 · ASK** — Hi, I am Likhith, and this video is about monorepos versus polyrepos.

**B01 · BLUF** — Here's the idea. One repo or many sounds like housekeeping. It's really a choice about how tightly your teams need to coordinate, and what that costs you at scale.

**B02 · HOOK** — Why does Google keep billions of lines of code, from thousands of engineers, in one repo?

**B03 · FRAMEWORK** — Poly-repo: one repo per project or service. Teams move independently, with clear owners.

**B04 · FRAMEWORK** — Mono-repo: everything in one giant repo, sharing one history and one toolset.

**B05 · MECHANISM** — The payoff: one commit updates a library and all its users. Dependencies stay in sync.

**B06 · TRADEOFF** — The catch: at huge scale, plain git checkouts and builds crawl without special tooling.

**B07 · EVIDENCE** — Fix one: sparse checkout. Download only the folders you actually need.

**B08 · EVIDENCE** — Fix two: remote build caching. Reuse earlier builds, so only what changed rebuilds.

**B09 · VERDICT** — No universal winner. Independent teams? Many repos. Tight coordination? One.

**B10 · YOUR_TURN** — Your turn. Ask Claude: here's how my teams ship code. One repo or many, and what breaks first? Then challenge its reasons.

**B11 · OUTRO** — Mono-repos versus poly-repos. At Humanitarians AI.
