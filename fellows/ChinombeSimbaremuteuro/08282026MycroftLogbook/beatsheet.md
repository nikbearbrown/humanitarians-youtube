# Mycroft Logbook — Beat Sheet

**Title:** The Logbook Before the Router
**Slug:** hai-mycroft-logbook
**Channel:** claude-hai · **Persona:** Simba · **Register:** Pragmatist · **Voice:** Kokoro `af_bella`
**Format:** ai-explainer (16:9 long cut) + 9:16 Shorts derivative (THE SHORTS LAW: single cycle, no revision, points back to the long cut)

Both cuts render from `beat_sheet.json` at true 4K (`ART_SCALE` scale=2). Durations below are Kokoro-measured (`actual_duration_s`), not estimates — audio is the master clock.

## 16:9 — long cut (13 beats, 3:44 / 223.6s, 3840×2160)

| # | Act | Start | Dur | Pattern | Motion | What's on screen |
|---|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 12.5s | ClaudeComposerAsk | type-on | Cold open — "Hi, Simba" greeting, the ask types into the composer, three output lines land answered |
| B01 | SUMMARY | 0:12 | 16.9s | ClaudeStatement | fade | BLUF sentence sets whole, terracotta underline settles |
| B02 | PROBLEM | 0:29 | 17.4s | BlindSpotFlow | illustrate | Request arrow flows into a box that resolves to "?"; cost/latency/retry/quality fields sit blank |
| B03 | REASONING | 0:47 | 24.6s | ReasonStack | stagger | Two numbered reasons land: the record outlives the decision |
| B04 | STRUCTURE | 1:11 | 17.3s | RecordCardFill | illustrate | Record card fills field by field (model→rule→cost→duration→retry→quality); 4 version stamps drop in |
| B05 | STRUCTURE | 1:29 | 18.3s | WriteOrderSafety | illustrate | Text-log-then-database write order; crash between them survives, reversed order loses the record |
| B06 | STRUCTURE | 1:47 | 13.8s | SummaryPanels | stagger | Three panels label in: cost/task type · retry rate/task type · slowest requests |
| B07 | PROOF | 2:01 | 23.7s | TwoWayCompare | illustrate | Two integrity tests: exact decimals vs. float drift; retry priced as one request vs. wrongly averaged |
| B08 | PROOF | 2:24 | 16.5s | GuardCards | illustrate | Retry record rejected without an escalation source; duplicate write recognized as one row |
| B09 | RESULTS | 2:41 | 24.0s | ResultsTable | illustrate | Real two-row trial table, ×260 cost-gap comparator, "TEST DATA" caveat stamp |
| B10 | SUMMARY | 3:05 | 21.2s | ClaudeVerdictArtifact | stagger | Verdict artifact: what shipped, what's proven, what's NOT yet proven |
| B11 | NEXT STEPS | 3:26 | 13.3s | ClaudeComposerAsk | type-on | Handoff — "Your turn." prompt types in |
| B12 | OUTRO | 3:39 | 4.3s | ClaudeTitleOutro | fade | Title restate, terracotta period, handle, subline |

## 9:16 — Shorts cut (5 beats, 0:51 / 51.4s, 2160×3840)

Per THE SHORTS LAW: single cycle, no revision pass — reuses/condenses a subset of the long cut and points back to it rather than retelling the whole thing.

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 9.7s | ClaudeComposerAsk916 | Condensed cold open |
| B01 | SUMMARY | 0:10 | 10.6s | ClaudeStatement916 | The point, stated |
| B02 | RESULTS | 0:20 | 14.3s | ResultsTable916 | The one real number — trial table + ×260 comparator + caveat |
| B03 | SUMMARY | 0:35 | 11.0s | ClaudeVerdictArtifact916 | Verdict, condensed |
| B04 | OUTRO | 0:46 | 5.7s | ClaudeTitleOutro916 | Title restate, "full build on the channel" |

`beat_sheet.json` in each reel's own folder (`hai-mycroft-logbook/` and `hai-mycroft-logbook-916/`) is the heart — this table is derived from it, not the other way around. Edit the sheet, not this file, if the reel changes.
