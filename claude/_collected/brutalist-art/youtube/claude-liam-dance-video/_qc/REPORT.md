# QC REPORT — claude-liam-dance-video
# "Claude, Dancing." | dance-video skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Build facts
- Runtime: 190.4s | Beats: 11/11 VIDEO | Audio: Kokoro am_onyx (free)
- Streams: video + audio confirmed (compile.py)

## Frame verification
| Timestamp | Beat | Pattern | Result |
|---|---|---|---|
| 1s | B00 | ClaudeComposerAsk | PASS — "DANCE-VIDEO · SKILL TEARDOWN", "Liam, in for Bear.", "Talofa, Liam", 4 output lines |
| 103s | B05 | SkillTeardownMechanism | PASS — "MECHANISM · ACT 1", "The downbeat grid is the cut grid.", verbatim quote |
| 162s | BVDT | ClaudeVerdictArtifact | PASS — "Claude, Dancing.", "DANCE-VIDEO: WHAT IT DELIVERS", 4 lines |
| 188s | BOUT | ClaudeTitleOutro | PASS — "Claude, Dancing." / @NikBearBrown / "Liam, in for Bear." |

## 9-point rubric
1. IN-FOR-BEAR: "Liam, in for Bear." visible at 1s — PASS
2. HELLO: "Talofa, Liam" (Samoan) in B00 — PASS
3. ILLUSTRATE LAW: 5 UI (B00, B03, BVDT, BHTF, BOUT) + 6 illustration (B01, B02, B04, B05, B06, B07) — PASS
4. SELF-DEMO: B03/B04 Phase 2 dance beats for rubber-hose Calloway character, 120 BPM swing — 4-part prompt formula (CHARACTER + DANCE + CAMERA + BACKGROUND + STYLE) for 3 beats — genuine Phase 2, no Higgsfield, no audio — PASS
5. VERBATIM QUOTES: "Audio is the master clock." (B05), "Describe the actual space and what's in it." (B06), "Beat-match is the thing to verify, not assume." (B07) — all from SKILL.md — PASS
6. MECHANISM × 3: B05 downbeat grid as master clock, B06 explicit background requirement, B07 beat-match gate verification — PASS
7. HANDOFF: BHTF "./art dance-video <reel>" with 2 forcing questions (character look? background space?) — PASS
8. OUTRO: BOUT "Claude, Dancing." — PASS
9. MINOR-COSMETIC: B04 ClaudeCodeBeat slow-mo 3× (10s Remotion clip stretched to 30.4s audio) — known, non-blocking; sparkLine empty (B00, B03, BHTF) — known, non-blocking

**VERDICT: QC PASS | 0 BLOCKER | 0 MAJOR | 4 MINOR-COSMETIC (B04 slow-mo + sparkLine)**
