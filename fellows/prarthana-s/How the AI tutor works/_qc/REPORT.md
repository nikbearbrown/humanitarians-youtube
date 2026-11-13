# Visual QC — How the Tutor Stays Grounded in Your Textbook

**Build 2** · 2026-09-09 · 3840×2160 · 181.87s · 10/10 slots
**Method:** frames sampled per beat into `_qc/frames/` and read. The mp4 probe alone is
not QC (rule 4). Build 1's findings and their fixes are kept below.

**Verdict: both blockers cleared, all three majors addressed. Ships.**

---

## Build 1 defects — resolved

| # | Defect | Fix | Verified |
|---|---|---|---|
| BLOCKER 1 | B00/B08 command text clipped off the right edge | `MedhavyTerminalAsk` uses `whiteSpace:'pre'` — never wraps, but honours `\n`. Both commands broken into short lines. | `B00_late.png`, `B08_late.png` — all lines in frame; B08's third question complete |
| BLOCKER 2 | B05 language chip read PYTHON over JSON | Added a `language` prop to `MedhavyCodeBlock` (was the literal string `python` at line 125), defaulting to `python`. B05 passes `json`. | rebuilt |
| MAJOR 1 | Cards floating in a third of the frame | New full-frame scenes in `MedhavyGroundedScenes.tsx`, laid out from the `SAFE` box | `B02_late.png`, `B03_late.png` |
| MAJOR 2 | B03 evidence note at 14px | Footnote is now 32px in `MedhavyStepFlow` | `B03_late.png` — readable |
| MAJOR 3 | Card beats were static slides | Every ramp is now a fraction of the beat via `useP()`; length is a prop (`durationS`) resolved by `calculateMetadata` | motion histogram below |

### Root cause of MAJOR 3

The old `MedhavyConceptCard` / `MedhavyTwoColumnCard` key every ramp to raw frame
numbers (`spring({frame: frame - 28, ...})`), so all motion completes by frame ~40 —
1.3s — and the remaining 15–20s is a freeze-hold added by `extend_clip_to_duration`.
They also import the **CLAUDE** palette, not MEDHAVY, which is why the "Medhavy" cards
rendered terracotta instead of teal, and they fix the card at 820px in a 1920 frame.

The four replacements normalize progress over the composition's own duration, so a 16s
beat and a 21s beat both animate end to end.

### Motion histogram

```
before:  illustrate:7  type-on:2  fade:1        → WARNING: illustrate 70%, over the ~40% cap
after:   type-on:2  compare:2  sequence:2  reveal:1  hold:1  illustrate:1  fade:1   → no warning
```

---

## Found and fixed during build 2

**Accents arriving too late to read.** Sampling at 88% of each beat caught the B06
warning and the B02/B07 accent labels still half-faded — their ramps completed at 0.97,
giving roughly 0.5s of full-strength time on a 21s beat. Pulled earlier:

| Element | was | now |
|---|---|---|
| `MedhavyCompareColumns` accent shift | 0.74 → 0.93 | 0.68 → 0.85 |
| `MedhavyCompareColumns` accent label | 0.86 → 0.97 | 0.76 → 0.87 |
| `MedhavyStepFlow` footnote | 0.78 → 0.90 | 0.60 → 0.72 |
| `MedhavyStepFlow` warning | 0.86 → 0.97 | 0.74 → 0.86 |

Verified in `B06_fix.png` and `B07_fix.png` — both now full strength with seconds of
settled frame after.

---

## Per-beat state

| Beat | Scene | Reading |
|---|---|---|
| B00 | `MedhavyTerminalAsk` | three lines, nothing clipped |
| B01 | `MedhavyStatementStack` | full-frame serif, last line takes teal, rule draws under |
| B02 | `MedhavyCompareColumns` | both columns full width; left stays full-strength ink |
| B03 | `MedhavyStepFlow` | four boxes, connectors, teal on step 3, visible gap before "The AI" |
| B04 | `MedhavyQuestionHold` | question at 104px, teal rule drawing the whole beat |
| B05 | `MedhavyCodeBlock` | JSON large and readable, chip reads `json` |
| B06 | `MedhavyStepFlow` | three stages, labelled crimson caution at full strength |
| B07 | `MedhavyCompareColumns` | benefit and cost equally weighted, neither dimmed |
| B08 | `MedhavyTerminalAsk` | all four lines in frame, third question complete |
| B09 | `MedhavyOutro` | unchanged from build 1 |

## Remaining, minor — not blocking

- **Bottom-third space on B02, B03, B06.** Content now occupies roughly the top two
  thirds rather than a middle band. Much improved, still not edge-to-edge under
  FILL-THE-CANVAS. Would need taller boxes or a lower baseline.
- **B07 crowding.** The third caution item wraps to two lines, so "The cost, named
  plainly." sits tight beneath it. No overlap; `accentLabel` is positioned from a fixed
  row count and does not account for wrapped rows.
- **B04 lower third** is deliberately empty — it is the pause beat.

## Toolkit changes made to get here

Four fixes in `brutalist.art`, all cross-platform, all written up in
`../BRUTALIST-WINDOWS-BUGS.md`: `run.sh:27` (POSIX path to Windows Python),
`remotion_scenes.py:85` (`npx` → `npx.cmd`), `compile.py:613` (ffmpeg font-path
escaping), and the `MedhavyCodeBlock` `language` prop. Plus one new file,
`scenes/MedhavyGroundedScenes.tsx`, and four `<Composition>` registrations.

Nothing pushed.
