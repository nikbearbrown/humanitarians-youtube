# PLAN — Claude, Unstuck (Ch.14: Troubleshooting and Staying Current)

**Slug:** `claude-liam-troubleshooting` · **Channel:** claude-liam (Kore, Kokoro `af_kore`, free) · **Register:** Teardown
**Source:** `chapters/ch14-troubleshooting.txt` (short chapter, ~520 words) · **One idea:** *When something breaks or doesn't match the screen, don't chase the surface — return to the durable concept (what the plugin is for, what it can and can't do) and check the official docs for the current specifics; the interface dates, the mental model doesn't.*

> **Episode thesis = the datable-strip doctrine.** This chapter is literally about things changing. The reel leans INTO that: you troubleshoot by returning to durable concepts and verifying current specifics against the official docs. The DOUBLE-CHECK LAW isn't just applied here — it is the subject.

## Act map (spine)

```
B00  COLD OPEN  ClaudeComposerAsk — "My plugin isn't working and the fixes don't match my screen." → ask lands answered ("concept, not screen; then the docs"), Kore signs in "Salaam — this is Kore, in for Humanitarians AI."
ACT I    When It Breaks        frustration→abandonment; drop to the durable layer   (B01 C3 illustration, B02 Manim layers surface-vs-bedrock)
ACT II   The Common Failures   five recurring shapes → durable causes/fixes         (B03 ChipGrid, B04 reopen-reload, B05 VOX auth, B06 Manim threshold, B07 Manim scope, B08 Onda code-block)
ACT III  The Four Steps        quick diagnostics + the diagnostic loop              (B09 /plugins toggle, B10 Manim four-step accumulate, B11 VOX isolate-by-shrinking)
ACT IV   Staying Current       interface dates / concept persists / check the docs  (B12 VOX evolve, B13 Manim timeline, B14 SourceFlow, B15→B16 VOX run R1)
V01  VERDICT   ClaudeVerdictArtifact — "Let's recap with Claude." (0.5s lead)
H01  YOUR TURN ClaudeComposerAsk "Your turn." — diagnostic prompt read aloud + discussed
O01  OUTRO     ClaudeTitleOutro — title re-read + sign-off "Claude, Unstuck. Kore, in for Humanitarians AI."
```

## Lane histogram (body beats only; bookends B00/V01/H01/O01 exempt)

| Lane | Count | Share | Target | Verdict |
|---|---|---|---|---|
| VOX | 5 | 25% | 20–25% | ✓ top of band; one 2-beat run |
| MANIM | 5 | 25% | 25–40% | ✓ bottom of band (moving data every time) |
| REMOTION | 6 | 30% | 30–45% | ✓ bottom of band |
| CARD | 4 | 20% | remainder | 4 segment cards (one per act) |

Body beats: **20** · Est. runtime ≈ **4:00** (short chapter, short reel — not padded; measured audio is the only clock).

**Lane semantics honored.** MANIM = moving data only: B02 surface/bedrock layers, B06 threshold meter, B07 scope-shrinks-latency-falls, B10 four-step accumulate with resolved counter, B13 interface-versions-churn/concept-line-flat. REMOTION = ChipGrid (B03), illustrations (B01, B04, B09), Onda code-block (B08), SourceFlow (B14). VOX = pantry stills + pantry_note, all Tier 1. CARD = segment cards only.

## Vox runs
- **R1 (B15→B16):** "monthly reminder / changelog" → "the model persists." One continuous downward camera move off the fluttering changelog pages onto the solid foundation block (the durable layer from B02, returning). `vox_run` id + handoff blocks authored in the sheet (single run, ≤3 beats, does not cross an act boundary). All other vox beats (B05, B11, B12) are standalone hard cuts.

## Datable facts STRIPPED / handled (DOUBLE-CHECK LAW — the episode's own subject)
- **No plugin counts, no prices, no platform lists** anywhere on screen or in narration. (Source chapter introduced none; none added.)
- **No named third-party vendors.** "CRM query, database lookup, web research" kept as generic operation *types*, never product names.
- **Official channels kept, not pinned to versions.** "The Anthropic blog and Claude's release notes," "the plugin directory," "each plugin's GitHub docs" — named as durable institutions (they ARE the thesis: where to check current specifics), never as a dated URL or version string.
- **Transcription fixes** ("Cloud"→"Claude", "Co-Work"→"Cowork", "Andthropic"→"Anthropic", "Global work"→"Cowork", "Pressure slow"→"operations run slow", "trades revoked"→"access revoked") logged in SOURCES.md.
- Source header mislabels this "Chapter 12"; it is Ch.14 per book order — corrected in metadata/derived_from.

## Gates
1. Plan (this doc) — **approve**.
2. Factcheck — inherits whole-book FACTCHECK.md; per-reel corrections + datable log in SOURCES.md.
3. **GATE P** — full narration (B00→O01) reviewed on an animated slate before any audio spend. Kokoro `af_kore`, free. No ElevenLabs.
4. Audio lock (Kokoro) → align (word clock) → **Gate D2 SHOPPING.md** (5 vox stills: B05, B11, B12, B15, B16 — all Tier 1; tier-0 `pantry_search.py` pass first) → **Gate D1 SLATE PREVIZ** (`./art run`, slates in vox slots) → pantry fill → review cut → VISUAL QC LAW → `./art final`.
