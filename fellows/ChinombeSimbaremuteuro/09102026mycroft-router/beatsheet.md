# One File, No Contradictions — Beat Sheet

**Title:** One File, No Contradictions
**Slug:** hai-mycroft-router
**Sprint:** Mycroft Sprint 3
**Channel:** claude-hai · **Persona:** Simba · **Register:** Pragmatist · **Voice:** Kokoro `af_bella`
**Format:** ai-explainer (16:9 long cut) + 9:16 Shorts derivative (THE SHORTS LAW: single cycle, no revision, points back to the long cut)

Source: the Mycroft Sprint 3 router/policy report pasted directly into this session — task-type routing rules locked into a single `policy.json`, a pure `router.py` that reads it, 24 frozen fixtures, blind agreement against a human labeler, structural and design-risk findings. Both cuts render from `beat_sheet.json` at true 4K (`ART_SCALE` scale=2). Durations below are Kokoro-measured (`actual_duration_s`), not estimates — audio is the master clock.

## 16:9 — long cut (15 beats, 6:12 / 372.45s, 3840×2160)

| # | Act | Start | Dur | Pattern | Motion | What's on screen |
|---|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 22.3s | ClaudeComposerAsk | type-on | Cold open — the ask types in (six task types, three cost tiers, how do you route without one quietly contradicting another), answered: one locked file, one pure router, tested blind at 9/24 |
| B01 | SUMMARY | 0:22 | 14.8s | ClaudeStatement | fade | BLUF: task types and their routing rules live in exactly one file, so two rules can never quietly disagree |
| B02 | STRUCTURE | 0:37 | 31.3s | PolicyGrid | illustrate | `policy.json`'s six task-type cards (sentiment, topic, structured extraction, contradiction detection, summarization, RAG answer), each locked to the same five fields — generic per-card note, no invented per-type values; footnote on the file-pointer test |
| B03 | STRUCTURE | 1:08 | 41.5s | RouterFlow | illustrate | The router's pure-function main path down to a tier decision, one dashed branch off to a refused/unrecognized-type box, a struck-through note for the break-even rule left out on purpose |
| B04 | WHAT WAS BUILT | 1:49 | 30.7s | TestSuiteProof | stagger | The bench folder's three tools (fixtures.py, audit.py, label.py), 24 fixtures / 4 per type / 2 easy·2 hard, capstone: frozen and fingerprinted 2026-09-10 |
| B05 | DECISIONS | 2:20 | 29.0s | FactStack | illustrate | Synthetic, not real — 203/217 placeholder script samples, a self-declared-fake dataset, an empty Klarna mock file; closing line on what the results can and can't support |
| B06 | DECISIONS | 2:49 | 20.3s | FactStack | illustrate | Labeling without anchoring — expected tier labeled before any model ran, the labeling tool never shows the router's pick |
| B07 | RESULTS | 3:09 | 23.1s | DataTable | illustrate | Your labels vs. the router — 6/11/7 by tier vs. 8/16/0 by tier, footnote: 9 of 24 agree, not yet a measurement |
| B08 | FINDINGS | 3:33 | 32.7s | FindingPair | illustrate | The tier the router can't reach — path one (long input) vs. path two (escalation), sparkline: no path from a short input straight to strong, and all 7 strong-labeled fixtures are short |
| B09 | FINDINGS | 4:05 | 23.2s | FactStack | illustrate | What the free checks actually catch — format, not correctness; a misread-sarcasm answer can still pass; main design risk heading into Sprints 4–5 |
| B10 | FINDINGS | 4:28 | 22.3s | DataTable | illustrate | Fixtures built to break the checks — summ-004 (correct answer) FAIL, extract-004 (made-up answer) PASS |
| B11 | PROBLEMS | 4:51 | 38.8s | FindingPair | illustrate | Labeling tool and first labeling pass, both FIXED; sparkline flags two problems found but not fixed here (dropped run-log entries, Windows Python detection) |
| B12 | SUMMARY | 5:29 | 25.0s | ClaudeVerdictArtifact | stagger | Verdict: delivered / proven — 9 of 24, a starting point not a benchmark / NOT yet done — length-only escalation, format-only checks, synthetic fixtures |
| B13 | NEXT STEPS | 5:54 | 12.9s | ClaudeComposerAsk | type-on | Handoff — "Your turn." prompt types in |
| B14 | OUTRO | 6:07 | 4.6s | ClaudeTitleOutro | fade | Title restate, terracotta period, handle, subline "one policy · no disagreement · Mycroft" |

## 9:16 — Shorts cut (5 beats, 0:58 / 58.07s, 2160×3840)

Per THE SHORTS LAW: single cycle, no revision pass — condenses the cold open and verdict, reuses the one "wait, what" comparison-table moment (`DataTable916`, same props as the long cut's B07), and points back to the long cut for the design risks.

| # | Act | Start | Dur | Pattern | What's on screen |
|---|---|---|---|---|---|
| B00 | INTRO | 0:00 | 13.9s | ClaudeComposerAsk916 | Condensed cold open |
| B01 | SUMMARY | 0:13 | 7.5s | ClaudeStatement916 | The rule, stated |
| B02 | RESULTS | 0:21 | 15.0s | DataTable916 | Your labels vs. the router, 9 of 24 agree |
| B03 | SUMMARY | 0:36 | 16.0s | ClaudeVerdictArtifact916 | Verdict, condensed |
| B04 | OUTRO | 0:52 | 5.6s | ClaudeTitleOutro916 | Title restate, "full build on the channel" |

`beat_sheet.json` in each reel's own folder (`hai-mycroft-router/` and `hai-mycroft-router-916/`) is the heart — this table is derived from it, not the other way around. Edit the sheet, not this file, if the reel changes.
