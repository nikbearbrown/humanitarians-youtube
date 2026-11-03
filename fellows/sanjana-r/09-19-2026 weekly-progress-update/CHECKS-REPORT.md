# CHECKS-REPORT — Two-Week Progress Review

Written per the cli-explainer PROOF GATE.

## Beat classification
11 SHOW / 1 HOLD / 0 PUNT   (12 beats)

| Beat | Act | Class | On-screen artifact |
|---|---|---|---|
| B00 | INTRO | HOLD (bookend) | Claude composer, ask answered (SAME as prior reels) |
| B01 | PROBLEM | SHOW | scale counters (2 / 38 / 172) + 172-video waffle |
| B02 | FRAMEWORK | SHOW | weekly-cadence toggle + review pipeline diagram |
| B03 | ASK | SHOW | the analysis prompt (Claude composer) |
| B04 | CODE | SHOW | real pandas review_report.py v1 (ClaudeCodeBeat) |
| B05 | OUTPUT | SHOW | 4 KPI cards + status funnel (172 -> 119 / 50 / 3) |
| B06 | CHANGE | SHOW | the revision prompt (Claude composer) |
| B07 | CODE | SHOW | real pandas v2 — map + groupby by week/project |
| B08 | OUTPUT | SHOW | Week 1 (87) vs Week 2 (85) bars + project donut (77/95) |
| B09 | SUMMARY | SHOW | scorecard tiles + GitHub gauge (85%) + honest caveat |
| B10 | NEXT STEPS | SHOW | scaffolded stakeholder prompt (Claude composer) |
| B11 | OUTRO | HOLD (bookend) | title restate, @HumanitariansAI (SAME as prior reels) |

No CARD-only claim beats. No unresolved PUNTs. Every OUTPUT beat is a moving
dashboard, never a still.

## Teaching-arc checklist
- FRAMEWORK ✓ — B02 shows the cadence + pipeline system before the numbers.
- WORKED EXAMPLE ✓ — B03→B08 read the real tracker, compute totals, revise to a
  week/project split; every number reproduced by the shown pandas.
- FALSIFIABILITY / HONESTY ✓ — B09 states the method's limits on screen (counts
  videos not hours; "changes requested" is the gate working and keeps converting
  to "changes made"), so the report is held to its own standard.
- SCAFFOLDED TASK ✓ — B10 hands PMs a copyable prompt (tracker → totals, week/
  project split, GitHub rate, three stakeholder sentences), not "ask Claude".
- BOOKENDS ✓ — Claude cold-open (B00), framework (B02), handoff (B10), title
  outro (B11) — intro/outro identical to the prior reels, as requested.
- NO-SOURCE-NO-VERDICT ✓ — every number computed from the tracker; the generating
  pandas is shown (B04, B07); scenes.py constants == the code's outputs.

## Legibility contract (verified in frame-level QC)
- Each SHOW beat names its artifact; ~15–35% negative space held.
- NO overlapping text/graphics (explicit creator requirement): every dashboard
  scene was frame-checked; two overlaps caught and fixed pre-final —
  B01 waffle caption position, B05 "blocked" label collision.
- Comparisons (B05 funnel; B08 Week1/Week2 + donut) shown together, held ≥2s.
- Motion smoothness: B02/B09 lengthened after first compile flagged slow-mo;
  final slow factors all ≤ ~2.3x (B09 fixed 3.2x → 1.4x).

## Graphics differ from prior reels (creator requirement)
Prior reels used histograms / range bands. This reel uses a DIFFERENT visual
language — counters, waffle, flow diagram, KPI cards, funnel, week bars, donut,
gauge — while keeping the Claude fidelity palette and the identical Claude
intro/outro.

Status: authoring PASS. Frame-level QC done → see _qc/ and PROOF-REVIEW.md.
