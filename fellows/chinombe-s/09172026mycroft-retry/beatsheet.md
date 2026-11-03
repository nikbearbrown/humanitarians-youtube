# One Retry, Never a Chain — Beat Sheet

**Title:** One Retry, Never a Chain
**Slug:** hai-mycroft-retry
**Sprint:** Mycroft Sprint 4 — Handle Failures
**Channel:** claude-hai · **Persona:** Simba · **Register:** Pragmatist · **Voice:** Kokoro `af_bella`
**Format:** ai-explainer (16:9 long cut) + 9:16 Shorts derivative (THE SHORTS LAW: single cycle, no revision, points back to the long cut)

Source: the Mycroft Sprint 4 report ("Handle Failures") pasted directly by the user. Both cuts render from `beat_sheet.json` at true 4K (`ART_SCALE` scale=2). Durations below are Kokoro-measured (`actual_duration_s`), not estimates — audio is the master clock. Unlike the last two builds in this series (PagedAttention, mycroft-router), this one needed **zero new Remotion components** — every beat mapped to a shape already built and QC'd: `FactStack` (×2), `RouterFlow` (×1), `TestSuiteProof` (×1), `DataTable` (×2), `FindingPair` (×3), plus the four house components.

## 16:9 — long cut (14 beats, 5:31 / 330.8s, 3840×2160)

| # | Act | Start | Dur | Pattern | Motion | What's on screen |
|---|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 18.9s | ClaudeComposerAsk | type-on | Cold open — the ask types in (can a wrong answer in the right shape slip through, uncaught, unhelped by retry?), answered: one retry ever, never a chain; 24 fixtures, 0% failure |
| B01 | SUMMARY | 0:19 | 13.4s | ClaudeStatement | fade | BLUF: retry happens exactly once, on the escalation tier, triggered by a free check failing |
| B02 | STRUCTURE | 0:32 | 23.2s | FactStack | illustrate | validators.py — five per-task-type checks (allowed label, JSON keys, contradiction quotes input, summary numbers in input, RAG cites a passage), plus two universal checks |
| B03 | STRUCTURE | 0:55 | 32.1s | RouterFlow | illustrate | gateway.py — route → call → check → retry once (tier above); terminal failures (bad key/unknown model/too large) never retried; no second retry, no loop exists |
| B04 | WHAT WAS BUILT | 1:27 | 14.5s | TestSuiteProof | stagger | Tests 96 → 146; validators.py / prompts.py / bench/run.py; first full graded run across all 24 fixtures |
| B05 | RESULTS | 1:42 | 25.9s | DataTable | illustrate | The final sweep, 24 fixtures — 24/26 requests/attempts, 0% failure, 8% escalation, $0.00250 total cost, p50 393ms / p95 734ms, 16/24 graded (14 correct) |
| B06 | FINDINGS | 2:07 | 38.4s | FindingPair | illustrate | The failure that didn't happen (0%) + the two flags were the answer key (sent-001/sent-004 keyed negative, models correctly said positive) |
| B07 | PROBLEMS | 2:46 | 38.2s | FindingPair | illustrate | Quote check too strict (11% → 8% escalation, fixed) + the vanished qwen3.6-27b model (404s, replaced with qwen3.8-27b) |
| B08 | PROBLEMS | 3:24 | 34.3s | FindingPair | illustrate | Token budget exceeded the rate cap (1024 → 896, fixed) + one log file, two runs (27 vs 24, fixed) — sparkLine notes the hardcoded-1024 test breaking correctly |
| B09 | FINDINGS | 3:58 | 24.1s | DataTable | illustrate | Escalation's real price — normal $0.000088 vs. escalated $0.000282 (3.2×); 2 of 24 requests = 23% of total spend |
| B10 | FINDINGS | 4:22 | 26.9s | FactStack | illustrate | The cost ladder isn't monotonic — strong tier 20% cheaper than cheap tier on the gate prompt despite 13× higher sticker price; cheap=77 thinking tokens, strong=2; crossover ~5 output tokens |
| B11 | SUMMARY | 4:49 | 26.9s | ClaudeVerdictArtifact | stagger | Verdict: Delivered (one retry, validators, adapters, graded bench run) / Proven (0% failure, both flags were the answer key) / Worth watching (3.2× escalation premium, sticker price ≠ real cost) |
| B12 | NEXT STEPS | 5:16 | 9.7s | ClaudeComposerAsk | type-on | Handoff — "Your turn." — have you checked where your own cost ladder crosses over? |
| B13 | OUTRO | 5:26 | 4.5s | ClaudeTitleOutro | fade | Title restate, terracotta period, handle, subline "one retry · zero failures · Mycroft" |

## 9:16 — Shorts cut (5 beats, 0:49 / 49.3s, 2160×3840)

Per THE SHORTS LAW: single cycle, no revision pass — condenses the cold open and verdict, reuses the one "wait, what" comparison moment (`DataTable916`, same content as the long cut's B05 — the final sweep numbers), and points back to the long cut for the full cost findings.

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 10.7s | ClaudeComposerAsk916 | Condensed cold open |
| B01 | SUMMARY | 0:10 | 7.5s | ClaudeStatement916 | The rule, stated |
| B02 | RESULTS | 0:18 | 12.1s | DataTable916 | The final sweep — 24 fixtures, 0% failure, 8% escalation; footnote: both flags were the answer key |
| B03 | SUMMARY | 0:30 | 13.3s | ClaudeVerdictArtifact916 | Verdict, condensed |
| B04 | OUTRO | 0:43 | 5.6s | ClaudeTitleOutro916 | Title restate, "full build on the channel" |

`beat_sheet.json` in each reel's own folder (`hai-mycroft-retry/` and `hai-mycroft-retry-916/`) is the heart — this table is derived from it, not the other way around. Edit the sheet, not this file, if the reel changes.
