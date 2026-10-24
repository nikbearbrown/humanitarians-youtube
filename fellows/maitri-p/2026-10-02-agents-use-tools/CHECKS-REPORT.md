# CHECKS-REPORT — agents-use-tools

Written before the first slate compile, per PROOF GATE (ai-explainer SKILL.md).
Beat sheet validated: `build_safety.validate_project` → PASS (2026-10-02).

## Beat classification

**7 SHOW / 3 bookend-UI / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Class | Named on-screen artifact |
|---|---|---|
| B00 | BOOKEND-UI | `ClaudeComposerAsk` — ask lands answered (COLD OPEN LAW) |
| B01 | SHOW | hesitant writer types, mis-states, corrects on screen |
| B02 | SHOW | model box → runtime frame draws around it, ports appear |
| B03 | SHOW | four loop stages light in narration order, loop arc closes |
| B04 | SHOW | five real size rows print; winner fills terracotta + bar |
| B05 | SHOW | direct path struck through; legal path animates; model dims |
| B06 | SHOW | gate passes a read, closes on a destructive command |
| B07 | SHOW | structured `P(clean)=pⁿ`, values substitute, decay curve draws |
| B08 | BOOKEND-UI | `ClaudeComposerAsk`, greeting "Your turn.", prompt typed |
| B09 | BOOKEND-UI | `ClaudeTitleOutro` — title restate |

No beat is a bare CARD. Every claim beat names its artifact in `shot.show`.

## Teaching arc

```
FRAMEWORK            ✓  B02 + B03 precede the worked example
WORKED EXAMPLE       ✓  B04 — real execution, verbatim output
FALSIFIABILITY       ✓  B04 command is reproducible verbatim; B07's
                        0.96^74 ≈ 0.05 is checkable arithmetic over a
                        stated n and p. Both can be shown wrong.
SCAFFOLDED TASK      ✓  B08 — a runnable prompt, read aloud and discussed
BOOKENDS             ✓  B00 cold open / B01 BLUF / B08 handoff / B09 outro
NO-SOURCE-NO-VERDICT ✓  B07's verdict rests on B04's real run and the
                        session's own 74-call record, not on assertion
```

## Law compliance

- **COLD OPEN LAW** — B00 is `ClaudeComposerAsk` with RESULT output lines.
- **EXECUTIVE-SUMMARY LAW** — B01 is `BrutalistHesitantWriter`, `lead_silence_s: 0.8`, 26 words (≥9s window). Correction is the reel's actual misconception: *a smarter model* → *a model wrapped in a runtime*. The corrected sentence stands alone as the reel's claim.
- **ILLUSTRATE LAW** — Claude UI appears at B00, B08, B09 only. B02–B07 all illustrate. No two consecutive beats share a visual scheme (B02 and B05 share `AgentRuntimeFrame` but are separated by B03 and B04, and use different `phase` props).
- **HANDOFF LAW** — prompt is read verbatim in narration, then discussed ("watch where expectation and result disagree").
- **OUTRO LAW** — title restated exactly.
- **TYPING RULE** — typing in exactly three beats: B00, B01, B08.
- **MATH** — structured MathText SVG via `typeset_math.py`, real superscript. No LaTeX required (MATH-TYPESETTING.md:6-7). Algebra verified: `0.96^74 = e^(74·ln0.96) = e^(−3.021) = 0.0488`.
- **EXECUTABLE EVIDENCE** — B04 is a real run, not a constructed example; command and cwd recorded in the beat's `evidence` block.

## Open items before `./art run`

1. **FOUR components must be built** (GATE L punts, logged to `TEMPLATE-MISSES.md`):
   `AgentRuntimeFrame` (B02, B05), `AgentToolLoop` (B03), `PermissionGate` (B06),
   plus the `CompoundingReliability` Manim scene (B07).
   Per GATE L a miss is a design card, never a licence to slate.
2. **`./art scene-index`** after adding them, or no future reel can find them.
3. **9:16 native beat sheet** — `shorts.py` writes `short/`; every beat needs a
   registered `<Pattern>916` or it is flagged, never centre-cut.
4. **FACTCHECK.md** — recompute p and n at build time and record.
5. **Visual QC** — frame-level pass after compile, per VISUAL QC LAW.
