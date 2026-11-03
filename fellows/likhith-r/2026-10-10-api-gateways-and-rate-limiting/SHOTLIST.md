# SHOTLIST — API Gateways and Rate Limiting

Native 16:9 (3840×2160) and 9:16 (2160×3840, `vertical/`). 12 beats · Kokoro `am_onyx` (speed 1.14) · @HumanitariansAI · 60.0 s.

| # | Act | Pattern (→ 916 twin) | Show |
|---|---|---|---|
| B00 | ASK | ClaudeComposerAsk | "Namaskaram, Likhith" · ask · 3 lines · AI-narration disclosure line |
| B01 | BLUF | BrutalistHesitantWriter | "Protection belongs in every service" → "in one gateway" |
| B02 | HOOK | GwHook | 10 service cards stamp auth / log / limit · counter → 30 |
| B03 | FRAMEWORK | GwFrontDoor | clients → API gateway → services · copies fly into the gateway · 30 copies → 3, shared |
| B04 | MECHANISM | GwPipeline | GET /orders walks Authenticate ✓ → Route (/orders highlighted) → Log line types |
| B05 | MECHANISM | GwRateLimit | 10 requests at a 5/s gate · 5 pass to backend · 5 bounce as 429 chips |
| B06 | MECHANISM | GwTokenBucket | 5-token bucket · burst of 4 passes · refill drips · flood runs dry (11 / 4) |
| B07 | COMPARISON | GwSlidingWindow | fixed lane: 5 + 5 across the 1:00 reset all pass · sliding bracket rejects the second 5 |
| B08 | APPLICATION | GwAiQuota | 24 shared slots: A22/B1/C1 with no limits vs 8/8/8 per-user · requests + tokens/min caption |
| B09 | VERDICT | ClaudeVerdictArtifact | 6 lines |
| B10 | YOUR TURN | ClaudeComposerAsk | prompt read aloud |
| B11 | OUTRO | HaiOutro | HAI mark · title · Subscribe · "Narrated by an AI voice." note |
