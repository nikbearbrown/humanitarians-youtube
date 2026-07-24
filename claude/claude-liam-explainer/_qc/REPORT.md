# QC REPORT — claude-liam-explainer
# "Claude, Mixed." | explainer skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Probe
- Duration: 193.7s video / 193.72s audio
- Streams: video h264 + audio aac — BOTH PRESENT
- Beat count: 11 (B00–B07, BVDT, BHTF, BOUT)

## 9-Point Rubric

| # | Check | Result |
|---|---|---|
| 1 | Brand palette (cream bg, terracotta accent, warm ink) | PASS |
| 2 | Correct prop names / no default fallback content | PASS |
| 3 | No double "Source:" in cite fields | PASS |
| 4 | Audio present and synced | PASS |
| 5 | All 11 beats render (no black frames, no slates) | PASS |
| 6 | ILLUSTRATE LAW: 5 UI beats, 6 illustration beats | PASS |
| 7 | IN-FOR-BEAR LAW: "Hej, Kore" in B00 cold open | PASS |
| 8 | Self-demo shows real SHOTLIST.md output (not faked) | PASS |
| 9 | Verbatim quotes cited with correct source (no prefix dupe) | PASS |

## Beat-by-Beat

- **B00** ClaudeComposerAsk: "EXPLAINER · SKILL TEARDOWN" / "Hej, Kore" — correct. MINOR-COSMETIC: empty sparkLine
- **B01** SkillTeardownAnatomy: "One treatment. Every source." — file tree correct, callout box renders. PASS
- **B02** SkillTeardownPipeline: "Slots fill last, not first." — 6 phases, footer note, sparkLine "Cheap before expensive." PASS
- **B03** ClaudeComposerAsk: self-demo command correct, output lines render. MINOR-COSMETIC: empty sparkLine
- **B04** ClaudeCodeBeat: SHOTLIST.md output with GRAPHIC/STILL/DOCUMENT shot types, realistic Manim scene names. PASS
- **B05** SkillTeardownMechanism: "Every source lands the same." — laundering function body/quote/cite correct. PASS
- **B06** SkillTeardownMechanism: "Type is locked. Source is late." — two-axis system correct. PASS
- **B07** SkillTeardownMechanism: "The slate is a standard, not a shame." — always-watchable law, verdictLabel "SLATE IS A FEATURE". PASS
- **BVDT** ClaudeVerdictArtifact: "Claude, Mixed." / 4 items render correctly. PASS
- **BHTF** ClaudeComposerAsk: "Your turn." / correct command. MINOR-COSMETIC: empty sparkLine
- **BOUT** ClaudeTitleOutro: "Claude, Mixed." / "@HumanitariansAI" / "Kore, in for Humanitarians AI." — PASS

## Defects

### BLOCKER: 0
### MAJOR: 0
### MINOR-COSMETIC: 3
- B00, B03, BHTF: ClaudeComposerAsk empty sparkLine — known recurring issue. Not blocking.

## Verdict: QC PASS (0 BLOCKER / 0 MAJOR)
