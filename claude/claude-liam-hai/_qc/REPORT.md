# QC REPORT — claude-liam-hai
# "Claude, Pragmatic." | hai skill teardown

**VERDICT: PASS**
**Date**: 2026-07-18
**Duration**: 240.0s | **Beats**: 11/11

## Frame checks

| Beat | Timestamp | Check | Result |
|------|-----------|-------|--------|
| B00 | 1s | ClaudeComposerAsk — "Bonjour, Liam" + "Liam, in for Bear." + command + output | PASS |
| B01 | 35s | SkillTeardownAnatomy — "Pragmatist register. Busy practitioners." + files | PASS |
| B04 | 126s | ClaudeCodeBeat — SOURCE + PRAGMATIST REWRITE (method/when-to/when-NOT-to) | PASS |
| B05 | 153s | SkillTeardownMechanism — quote "Required: when NOT to and where it fails" present | PASS |
| B06 | 175s | SkillTeardownMechanism — "This the AI does well. This is the human's." | PASS |
| BVDT | 218s | ClaudeVerdictArtifact — "Claude, Pragmatic." + 4 delivery lines | PASS |
| BOUT | 238s | ClaudeTitleOutro — "Claude, Pragmatic." / @NikBearBrown / "Liam, in for Bear." | PASS |

## 9-point rubric

1. **IN-FOR-BEAR LAW** — "Liam, in for Bear." in B00: PASS
2. **ILLUSTRATE LAW** — 5 UI beats (B00/B03/BVDT/BHTF/BOUT) + 6 illustration beats: PASS
3. **VERBATIM QUOTE LAW** — 3 quotes exact, cited once per figure: PASS
4. **SELF-DEMO** — Phase 2 register rewrite; canonical + Pragmatist rewrite (method/when-to/when-NOT-to) shown in B04; free, no ElevenLabs: PASS
5. **NO SLATES** — 11/11 filled: PASS
6. **AUDIO FIRST** — all beats have measured actual_duration_s: PASS
7. **FREE PIPELINE** — Kokoro am_onyx, $0.00: PASS
8. **PALETTE** — cream/terracotta Claude palette throughout: PASS
9. **BOUT** — "Claude, Pragmatic." / @NikBearBrown / "Liam, in for Bear.": PASS

## Issues

| Severity | Beat | Description |
|----------|------|-------------|
| MINOR-COSMETIC | B04 | ClaudeCodeBeat 3.8× slow-mo (10s Remotion clip stretched to 38.23s narration) — known, non-blocking |
| MINOR-COSMETIC | B00 | sparkLine empty — known, non-blocking |
| MINOR-COSMETIC | B03 | sparkLine empty — known, non-blocking |
| MINOR-COSMETIC | BHTF | sparkLine empty — known, non-blocking |

**0 BLOCKER | 0 MAJOR | 4 MINOR-COSMETIC**
