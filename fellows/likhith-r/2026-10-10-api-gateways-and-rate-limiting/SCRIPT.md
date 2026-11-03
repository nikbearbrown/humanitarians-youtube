# SCRIPT — API Gateways and Rate Limiting

Narration as generated. **AI voice** (Kokoro `am_onyx`), not a recording of Likhith.

**B00 · ASK** — Hi, I am Likhith, and this video is about API gateways and rate limiting.

**B01 · BLUF** — The idea: one gateway checks, routes, logs, and limits every request, instead of every service guarding itself.

**B02 · HOOK** — Ten services each need logins, logs, and overload protection. Ten copies?

**B03 · FRAMEWORK** — A gateway is one entry point for them all. Shared work, done once.

**B04 · MECHANISM** — It checks who you are, routes to the right backend, and logs it.

**B05 · MECHANISM** — Rate limiting caps each client's requests per window. Floods never reach the backend.

**B06 · MECHANISM** — A token bucket refills steadily. Bursts spend saved tokens; floods run dry.

**B07 · COMPARISON** — Fixed windows reset on the clock, so edge bursts double. Sliding windows count the last minute.

**B08 · APPLICATION** — AI calls are expensive. Per-user limits stop one client draining shared capacity.

**B09 · VERDICT** — Verdict: scattered protection becomes one consistent layer every request passes through.

**B10 · YOUR_TURN** — Your turn. Ask Claude: design rate limits for my API and pick an algorithm for my traffic. Then test it on bursts.

**B11 · OUTRO** — API gateways and rate limiting. Humanitarians AI.
