# One Door In — Beat Sheet

**Title:** One Door In
**Slug:** hai-mycroft-gateway
**Channel:** claude-hai · **Persona:** Simba · **Register:** Pragmatist · **Voice:** Kokoro `af_bella`
**Format:** ai-explainer (16:9 long cut) + 9:16 Shorts derivative (THE SHORTS LAW: single cycle, no revision, points back to the long cut)

Both cuts render from `beat_sheet.json` at true 4K (`ART_SCALE` scale=2). Durations below are Kokoro-measured (`actual_duration_s`), not estimates — audio is the master clock.

## 16:9 — long cut (16 beats, 5:58 / 357.8s, 3840×2160)

| # | Act | Start | Dur | Pattern | Motion | What's on screen |
|---|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 21.8s | ClaudeComposerAsk | type-on | Cold open — the ask ("guarantee nobody can call a model without it being logged, or priced") types in, answered |
| B01 | SUMMARY | 0:21 | 14.4s | ClaudeStatement | fade | BLUF: "a caller must not be able to make an unlogged call" |
| B02 | STRUCTURE | 0:36 | 16.0s | GatewayDoor | illustrate | `GatewayClient.call()` as the one labeled door wrapping adapter + logbook; success and failure both write a row |
| B03 | STRUCTURE | 0:52 | 26.0s | LayerStack | illustrate | Three layers stack: Adapter → Client → Router (dashed, "coming next"), each with a does/does-not line |
| B04 | PROOF | 1:18 | 22.3s | DataTable | illustrate | File table lands: 5 modules shown, 1,015 lines total, 377 of them tests |
| B05 | PROOF | 1:40 | 41.8s | TestSuiteProof | stagger | 56 passing / 32 new this sprint; 3 rule-encoding tests surface; closes on the test that failed on purpose |
| B06 | REASONING | 2:22 | 26.1s | EvidenceTrail | illustrate | "No PM/billing access" → one evidenced provider (Groq), others only configured, never evidenced |
| B07 | REASONING | 2:48 | 25.1s | DataTable | illustrate | Three priced models on one Groq key: cheap / mid / strong, in/out price and context per tier |
| B08 | REASONING | 3:13 | 24.4s | BreakEvenThresholds | illustrate | Break-even math: cheap needs >50% vs. mid, >11% vs. strong; old free-tier setup had no floor |
| B09 | RESULTS | 3:37 | 19.1s | DataTable | illustrate | 3 live-call rows; hand-recomputed cost lands on MATCHES |
| B10 | FINDINGS | 3:57 | 32.8s | FindingPair | illustrate | Finding 1–2: reasoning-token overhead on a 1-word answer (80% of cost); 3× cold start |
| B11 | FINDINGS | 4:29 | 31.3s | FindingPair | illustrate | Finding 3–4: shared-key escalation trap; "ok" that landed exactly on max_tokens — succeeded but worth nothing |
| B12 | RISK | 5:01 | 17.1s | ConvergenceRisk | illustrate | All 3 tiers converge on one provider/key — already blocked a production batch once |
| B13 | SUMMARY | 5:18 | 20.9s | ClaudeVerdictArtifact | stagger | Verdict: delivered / proven / NOT yet done (mid+strong live-gate, task corpus) |
| B14 | NEXT STEPS | 5:39 | 14.3s | ClaudeComposerAsk | type-on | Handoff — "Your turn." prompt types in |
| B15 | OUTRO | 5:53 | 4.3s | ClaudeTitleOutro | fade | Title restate, terracotta period, handle, subline |

## 9:16 — Shorts cut (5 beats, 0:56 / 56.1s, 2160×3840)

Per THE SHORTS LAW: single cycle, no revision pass — reuses the long cut's live-calls table (same tested `DataTable916` props as B09) and condenses the rest, pointing back to the long cut.

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 14.0s | ClaudeComposerAsk916 | Condensed cold open |
| B01 | SUMMARY | 0:14 | 9.4s | ClaudeStatement916 | The rule, stated |
| B02 | RESULTS | 0:23 | 15.2s | DataTable916 | The one live-call table + hand-recomputed-cost footnote |
| B03 | SUMMARY | 0:38 | 11.5s | ClaudeVerdictArtifact916 | Verdict, condensed |
| B04 | OUTRO | 0:50 | 6.0s | ClaudeTitleOutro916 | Title restate, "full build on the channel" |

`beat_sheet.json` in each reel's own folder (`hai-mycroft-gateway/` and `hai-mycroft-gateway-916/`) is the heart — this table is derived from it, not the other way around. Edit the sheet, not this file, if the reel changes.
