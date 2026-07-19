# QC REPORT — claude-liam-math-explainer
# "Claude, Derived." | math-explainer skill teardown
# Auditor: Claude Sonnet 4.6 | 2026-07-18

## Probe
- Duration: 197.0s video / 197.03s audio
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
| 7 | IN-FOR-BEAR LAW: "Hallo, Liam" in B00 cold open | PASS |
| 8 | Self-demo shows real beat_sheet.json output (not faked) | PASS |
| 9 | Verbatim quotes cited with correct source (no prefix dupe) | PASS |

## Beat-by-Beat

- **B00** ClaudeComposerAsk: "MATH-EXPLAINER · SKILL TEARDOWN" / "Hallo, Liam" — correct. MINOR-COSMETIC: empty sparkLine (known issue all ClaudeComposerAsk beats)
- **B01** SkillTeardownAnatomy: "Three laws, one canvas." — file tree correct (SKILL.md/pedagogy.md/style.md/equations.md/scripts/), callout box renders. PASS
- **B02** SkillTeardownPipeline: "Mystery earns abstraction." — 6 phases render cleanly (MYSTERY OPEN → CONCRETE → TRANSFORM → ABSTRACTION → EQ TANGENT → CLEAN MASTER), footer note visible, sparkLine "Abstraction is the reward." PASS
- **B03** ClaudeComposerAsk: "MATH-EXPLAINER · SELF-DEMO · THE ASK" / "./art math-explainer 'Why is d/dx(x²) = 2x?'" — correct. MINOR-COSMETIC: empty sparkLine
- **B04** ClaudeCodeBeat: beat_sheet.json output shows MYSTERY→CONCRETE→TRANSFORM→ABSTRACTION→TANGENT arc. sparkLine "The sequence is the pedagogy." visible. PASS
- **B05** SkillTeardownMechanism: "The definition waits." — body/quote/cite correct, no double Source:. PASS
- **B06** SkillTeardownMechanism: "The algebra earns its name." — body/quote/cite correct, no double Source:. PASS
- **B07** SkillTeardownMechanism: "The equation gets its 45 seconds." — body/quote/cite correct, verdictLabel "EXPLANATION OVER PROOF" visible. PASS
- **BVDT** ClaudeVerdictArtifact: "Claude, Derived." / "What the skill actually does" — 4 items render correctly. PASS
- **BHTF** ClaudeComposerAsk: "Your turn." / "./art math-explainer '<your why-does question>'" — correct. MINOR-COSMETIC: empty sparkLine
- **BOUT** ClaudeTitleOutro: "Claude, Derived." / "@NikBearBrown" / "Liam, in for Bear." — PASS

## Defects

### BLOCKER: 0
### MAJOR: 0
### MINOR-COSMETIC: 3
- B00, B03, BHTF: ClaudeComposerAsk empty sparkLine — component renders bar at footer but text is absent. Known recurring issue (also in videos 1 and 2). No fix applied — not blocking.

## Verdict: QC PASS (0 BLOCKER / 0 MAJOR)
