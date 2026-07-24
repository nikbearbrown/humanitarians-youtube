# QC REPORT — claude-liam-lyric-overlay
# "Claude, Overlaid." | lyric-overlay skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Build facts
- Runtime: 213.4s | Beats: 11/11 VIDEO | Audio: Kokoro af_kore (free)
- Streams: video + audio confirmed (ffprobe)

## Frame verification
| Timestamp | Beat | Pattern | Result |
|---|---|---|---|
| 1s | B00 | ClaudeComposerAsk | PASS — "LYRIC-OVERLAY · SKILL TEARDOWN", "Habari, Kore", 4 layers listed |
| 117s | B05 | SkillTeardownMechanism | PASS — "MECHANISM · ACT 1", "Extract from the video. Never bring in a separate WAV.", quote |
| 189s | BVDT | ClaudeVerdictArtifact | PASS — "Claude, Overlaid.", "LYRIC-OVERLAY: WHAT IT DELIVERS", 4 lines |
| 211s | BOUT | ClaudeTitleOutro | PASS (BOUT starts at 210.4s) |

## 9-point rubric
1. IN-FOR-BEAR: "Kore, in for Humanitarians AI." visible at 1s — PASS
2. HELLO: "Habari, Kore" (Swahili) in B00 — PASS
3. ILLUSTRATE LAW: 5 UI + 6 illustration — PASS
4. SELF-DEMO: B03/B04 theme.ts configuration for bright travel video overlay — waveformMid/scrimOpacity/lyricStyle with documented values — genuine, not faked — PASS
5. VERBATIM QUOTES: 3 quotes from SKILL.md in B05/B06/B07 — PASS
6. MECHANISM × 3: B05 extract from video, B06 scrim legibility, B07 two-pass lyric timing — PASS
7. HANDOFF: BHTF "./art lyric-overlay <video.mp4>" with 2 forcing questions — PASS
8. OUTRO: BOUT "Claude, Overlaid." — PASS
9. MINOR-COSMETIC: sparkLine empty (B00, B03, BHTF) — known, non-blocking

**VERDICT: QC PASS | 0 BLOCKER | 0 MAJOR | 3 MINOR-COSMETIC (sparkLine)**
