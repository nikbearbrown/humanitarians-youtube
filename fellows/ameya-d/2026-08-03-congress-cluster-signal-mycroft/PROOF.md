# PROOF.md — self-assessment · congress-cluster-signal

**Reel:** Congress Doesn't Beat the Market. The Cluster Does.
**Volunteer:** Ameya Deshmukh · **Project:** Mycroft (congressional signal analysis)
**Persona:** Liam, in for Ameya (Kokoro `am_onyx`) · **Channel:** @HumanitariansAI
**Deliverable:** `Mycroft_AmeyaDeshmukh_2026-08-03.mp4` · **Resolution:** 3840×2160 (4K) · **Runtime:** ~3:54

Self-assessment before submission. Each item is checked against the actual
rendered master, not the plan.

## Reviewer feedback (Sanjana Rao) — resolution status

| # | Requirement | Status | Evidence |
|---|-------------|--------|----------|
| 1 | Handle is `@[Your Name]` or `@HumanitariansAI` **throughout** — no `@NikBearBrown` | ✅ FIXED | `folderLabel: @HumanitariansAI` on every composer beat (B00, B02, B05, B09); `handle: @HumanitariansAI` on the outro (B10); no `@NikBearBrown` remains in `beat_sheet.json` |
| 2 | Code for the film uploaded to GitHub; share link | ✅ DONE | Reel source (beat_sheet.json, scenes.py, gate paperwork) pushed — link in the submission note |
| 3 | Resolution at 4K (3840×2160) | ✅ DONE | Manim scenes re-rendered at `-r 3840,2160`; Remotion beats at `--scale=2` (native 4K); compiled `--height 2160` |
| 4 | Self-assess using PROOF.md | ✅ this file | — |

## Content integrity (DOUBLE-CHECK LAW)
- Every on-screen number traces to `RESEARCH_REPORT.md` and the real
  `market_adjusted.py` / `backtest.py`. Full claim-by-claim table in
  [FACTCHECK.md](FACTCHECK.md); source map in [SOURCES.md](SOURCES.md).
- The two CODE beats (B03, B06) show real, trimmed source — not pseudocode
  (ACTUAL-CODE LAW).
- No model-version numbers or drift-prone live counts on screen; the
  108-member / 13,877-trade figures are stated as the study's fixed sample.
- Not financial advice — stated on screen (B08) and in the source paper.

## Toolkit gates
- **GATE P (pedagogy):** signed — [PEDAGOGY.md](PEDAGOGY.md), VERDICT: PASS.
- **GATE V (visual QC):** frame-level pass — 0 BLOCKER. Remaining advisory is the
  outro title card's negative space, inherent to the `ClaudeTitleOutro` template.
  Contact sheet: `qc-sheet.png`.
- **Audio-first:** all 11 narration beats measured (Kokoro); each visual conforms
  to its measured beat length (no extreme slow-motion; Manim scenes auto-fill to
  the audio clock).

## Spine (cli-explainer, 11 beats)
B00 INTRO · B01 PROBLEM · B02 ASK · B03 CODE · B04 OUTPUT · B05 CHANGE · B06 CODE
· B07 OUTPUT · B08 SUMMARY · B09 NEXT STEPS · B10 OUTRO. Required revision cycle
present (B05→B06→B07).

## Weekly-report content (what / done / next)
- **Worked on:** an event-study backtest of congressional cluster buy signals
  under strict per-trade market adjustment (Mycroft module).
- **Completed:** the finding that congressional buying doesn't beat the market in
  aggregate (+0.13% alpha), while cluster buys carry a small, consistent edge
  (~50% vs ~45% win rate); packaged as this explainer.
- **Next:** significance testing (t-tests / bootstrap CIs) on the tier
  differences, and expanding coverage beyond 108 members.

## Known limitations of this cut
- All beat motion is `fade` (toolkit advisory: >40% single-transition); acceptable
  for a report cut, could diversify transitions in a future pass.
- Outro card is intentionally sparse (template).

**Self-verdict: PASS** — meets all four reviewer requirements and the toolkit
gates. Ready for re-upload.
