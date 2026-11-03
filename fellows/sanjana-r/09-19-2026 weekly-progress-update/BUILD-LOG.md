# BUILD-LOG — Two-Week Progress Review

Reel: `sept-progress-review` · channel @HumanitariansAI · narrator Sanjana Rao
Skill: cli-explainer (Claude skin) · voice af_bella (Bella, female) · built 2026-09-19.

## Decisions
- A stakeholder-facing PROGRESS REPORT (film 3), not a concept explainer. Data
  source: Sanjana's own tracker "Humanitarians AI Video Reviews.xlsx" (sheet
  "September Videos"), window Sep 6–19 ("past two weeks" from today, 2026-09-19).
- SAME Claude intro (B00) and outro (B11) as the prior reels (explicit request);
  the MIDDLE uses a new dashboard visual language (counters, waffle, flow diagram,
  KPI cards, funnel, week bars, donut, gauge) — graphics deliberately different
  from the histograms/range-bands of the earlier reels.
- Breakdown presented by WEEK (Week 1 = 87, Week 2 = 85), not per-review dates
  (creator instruction mid-build).
- Two deliverables: 16:9 4K (3840×2160) + 9:16 Short.
- Output local under "Humanitarians AI Brutalist files"; NOT pushed to GitHub.

## Pipeline (Windows — bash wrappers bypassed; scripts called directly)
1. Read the xlsx with openpyxl; computed + reconciled all figures (see SOURCES.md).
2. `generate_audio_kokoro.py` → 12 mp3s (af_bella). Master clock = 290.0s.
3. `remotion_scenes.py --now <iso>` → 7 Claude beats at 4K (--scale=2).
4. `manim -qk -r 3840,2160` → 5 dashboard scenes → manim/<BID>.mp4.
5. `compile.py --height 2160` → final 16:9.
6. `add_transitions.py` → cream cross-dissolves → *-fx.mp4.
7. Frame-level QC + PROOF self-review → fixes → recompile.
8. 9:16 Short authored + compiled at 2160×3840.

## Fixes during QC
- B01: waffle sat too low → caption clipped. Raised waffle, tightened cells.
- B05: tiny "blocked" (3) segment label collided with "changes" → moved to the
  right of the segment. No overlaps remain (creator requirement).
- B02 (2.47x) and B09 (3.2x "extreme" slow-mo) scenes lengthened with paced holds
  and re-rendered; recompiled → B09 now 1.42x, B02 1.62x. (B05 2.13x / B08 2.34x
  left as-is — mostly fades/holds, within the prior reels' accepted range.)

## Honesty / DOUBLE-CHECK
- Every on-screen number computed from the tracker; generating pandas shown (B04/B07).
- 172 = 119 + 50 + 3; 172 = 87 + 85; 172 = 77 + 95 — all reconciled.
- No individual fellow named/ranked; aggregates only. Honest caveat on screen (B09).

## GATE N (Professor Bear's notes)
- N/A — self-authored cli-explainer progress report; no Bear-notes beat to sign.
