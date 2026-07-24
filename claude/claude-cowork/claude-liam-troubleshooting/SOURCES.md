# SOURCES — Claude, Unstuck (Ch.14)

## Source document
- `books/anthropics/books/claude-cowork-plugins/chapters/ch14-troubleshooting.txt`
  (from `claude-cowork-plugins.md`, Chapter 14 — *Claude Cowork Plugins*, rev. Spring 2026, "John Collins")
  Short chapter (~520 words). Reel is scaled to it: 20 body beats, ~4:00. Not padded.

## Corrections applied (DOUBLE-CHECK LAW; see book-level FACTCHECK.md)
| In source | On screen / in narration | Why |
|---|---|---|
| "Chapter 12. Troubleshooting…" | Ch.14 (per book order) | Source .txt header is mis-numbered; corrected in metadata + derived_from. |
| "Cloud" / "Co-Work" (STT throughout) | "Claude" / "Cowork" | Speech-to-text artifacts (per FACTCHECK §3). |
| "Andthropic" | "Anthropic" | STT artifact. |
| "Global work handles most updates automatically" | "Cowork handles most updates automatically" | STT garble ("Global work" → "Cowork"). |
| "Pressure slow. Plugin operations…" | "operations run slow" | STT garble; header for the slow-operations issue. |
| "Trades get revoked" | "access gets revoked" | STT garble ("trades" → tokens/access). |
| "cloud.com slash plugins" | "the plugin directory" (kept generic) | STT ("cloud"→"claude") + we do NOT pin an exact URL on screen. |

## Datable material — stripped or held generic (this reel's THESIS)
- **No plugin counts, no prices, no platform lists** anywhere. The chapter introduced none; none added.
- **No named third-party vendors.** "CRM query, database lookup, web research" kept as generic operation *types*.
- **Official channels named as durable institutions, not versions:** "the Anthropic blog and Claude's release notes," "the plugin directory," "each plugin's GitHub docs." Naming *where to check current specifics* is the point of Act IV — but no URL, version, or "as of [month]" is spoken or shown.
- The whole of Act IV is the DOUBLE-CHECK LAW made explicit: the interface dates, the concept persists, verify specifics against the live docs.

## Claims carried (verified true / durable mechanisms)
- Plugins load at startup; a full Cowork restart reloads them; reinstall from the sidebar as fallback. ✓ (durable mechanism)
- Credentials go stale — tokens expire, passwords change, access is revoked; disconnect/reconnect; IT gating may require approval. ✓
- Out-of-box defaults are intentionally broad; customization with your context sharpens results. ✓ (consistent with Ch.1)
- Operations reaching external services are slower than local; reduce scope (one date range, one folder). ✓
- `/plugins` shows installed/active plugins; disable + re-enable reloads a plugin's config. ✓ (durable command)
- The four-step loop (active → authorized → simpler request → restart) resolves most problems. ✓
- Anthropic's official channels (blog + Claude release notes) are the most reliable sources for Cowork/plugin updates. ✓ (per FACTCHECK sources list)

## Seeds / determinism
- Manim + Remotion scenes are pure functions of the audio clock; log any RNG seed here at render time.
- No AI-generated real people in this reel; all 5 vox stills (B05, B11, B12, B15, B16) are Tier 1 illustrative — no rights escalation.

## Credits
- Narration: Liam (in for Bear), Kokoro `am_onyx`. Channel: @NikBearBrown.
