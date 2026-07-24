# QC REPORT — claude-liam-audience-preset
# "Claude, Branded." | audience-preset skill teardown

**VERDICT: PASS**
**Date**: 2026-07-18
**Duration**: 211.5s | **Beats**: 11/11

## Frame checks

| Beat | Timestamp | Check | Result |
|------|-----------|-------|--------|
| B00 | 1s | ClaudeComposerAsk — "Hei, Kore" greeting, command visible, folder label | PASS |
| B01 | 30s | SkillTeardownAnatomy — title "One reel. N brand variants." + file card | PASS |
| B02 | 60s | SkillTeardownPipeline — fork→register→tangent→outro→build phases | PASS |
| B04 | 107s | ClaudeCodeBeat — 3-way comparison (source/HAI/Medhavy) visible | PASS |
| B05 | 134s | SkillTeardownMechanism — quote box "One skill, one flow, N brands." present | PASS |
| B06 | 155s | SkillTeardownMechanism — quote "The canonical beat_sheet.json is NEVER modified." | PASS |
| B07 | 176s | SkillTeardownMechanism — quote "No code changes — brand_variant.py takes the brand name as an argument." | PASS |
| BVDT | 187s | ClaudeVerdictArtifact — "Claude, Branded." + 4 delivery lines | PASS |
| BOUT | 209s | ClaudeTitleOutro — "Claude, Branded." / @HumanitariansAI / "Kore, in for Humanitarians AI." | PASS |

## 9-point rubric

1. **IN-FOR-BEAR LAW** — "Kore, in for Humanitarians AI." in B00: PASS
2. **ILLUSTRATE LAW** — 5 UI beats (B00/B03/BVDT/BHTF/BOUT) + 6 illustration beats: PASS
3. **VERBATIM QUOTE LAW** — 3 quotes exact, cited once per figure: PASS
4. **SELF-DEMO** — Phase 2 register rewrite; canonical + HAI Pragmatist + Medhavy Wonder shown in B04; free, no brand_variant.py: PASS
5. **NO SLATES** — 11/11 filled: PASS
6. **AUDIO FIRST** — all beats have measured actual_duration_s: PASS
7. **FREE PIPELINE** — Kokoro af_kore, $0.00: PASS
8. **PALETTE** — cream/terracotta Claude palette throughout: PASS
9. **BOUT** — "Claude, Branded." / @HumanitariansAI / "Kore, in for Humanitarians AI.": PASS

## Issues

| Severity | Beat | Description |
|----------|------|-------------|
| MINOR-COSMETIC | B04 | ClaudeCodeBeat 3.6× slow-mo (10s Remotion clip stretched to 36.39s narration) — known, non-blocking |
| MINOR-COSMETIC | B00 | sparkLine empty — known, non-blocking |
| MINOR-COSMETIC | B03 | sparkLine empty — known, non-blocking |
| MINOR-COSMETIC | BHTF | sparkLine empty — known, non-blocking |

**0 BLOCKER | 0 MAJOR | 4 MINOR-COSMETIC**
