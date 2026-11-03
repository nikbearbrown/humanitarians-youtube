# CHECKS-REPORT — stale-ecg

PROOF GATE, per `skills/make/nopunt/SKILL.md`. Governs authoring, not rendering.

```
11 SHOW / 0 justified-HOLD / 1 CARD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification

| Beat | Class | On-screen artifact |
|---|---|---|
| B00 | SHOW | `ClaudeComposerAsk` — ask lands answered with real cohort counts |
| B01 | SHOW | `EcgAverageTrap` — aggregate bar splits into four signed components |
| B02 | SHOW | `ClaudeComposerAsk` — the binning ask |
| B03 | SHOW | `ClaudeCodeBeat` — real `cluster_bootstrap()` source |
| B04 | SHOW | `EcgStalenessBars` — four bins, CIs, hatched underpowered pair |
| B05 | SHOW | `ClaudeComposerAsk` — the revision ask |
| B06 | SHOW | `ClaudeCodeBeat` — real `oof_cross_lag()` source |
| B07 | SHOW | `EcgWithinPatientDecay` — log-age series crossing zero |
| B08 | SHOW | `EcgVerdictPanel(mechanism)` — two age distributions + falsifier |
| B08B | SHOW | `EcgVerdictPanel(mitigation)` — both remedies straddling zero |
| B09 | SHOW | `ClaudeComposerAsk` — handoff prompt, read aloud |
| B10 | CARD | `OutroSeries` — title restate. A card by definition; not a punt. |

Every beat that makes a factual or structural claim is SHOW. No beat naming a
visual ("the split", "the line", "the intervals") resolves to a bare card.

## Teaching-arc detail

- **FRAMEWORK before examples** — B01 establishes *the average is a mixture*
  before any binned result is shown. The viewer has the lens before the data.
- **WORKED EXAMPLE** — two, and the second tests the first: B02→B04 (binned)
  and B05→B07 (within-patient, removing the confound the first one carries).
- **FALSIFIABILITY** — B08 carries the reverse-training check: train on stale
  ECGs and the harm disappears, which is what makes "unearned trust" a claim
  that could have failed. B08B reports two remedies that did not work.
- **SCAFFOLDED TASK** — B09 hands over a runnable prompt shaped to the
  viewer's own model, not a restatement of this one.
- **BOOKENDS** — B00 intro, B08/B08B verdict, B09 handoff, B10 outro.
- **NO-SOURCE-NO-VERDICT** — every on-screen number resolves to a row in
  `results/results.json` or `results/within_patient.json`; see `SOURCES.md`.

## GATE L — library-first

Searched before authoring:

| Query | Outcome |
|---|---|
| "bar chart with confidence intervals by category" | LEAD `BarChart` — rejected: unsigned, no interval marks, no underpowered state |
| "line declining over time with error bars" | miss — all hits reel-specific figures |
| "sign change positive to negative effect" | miss |
| "before after metric comparison big number delta" | miss |
| "average hides variation aggregate trap" | miss |

Four genuine PUNTs → four design cards built and registered:
`EcgAverageTrap`, `EcgStalenessBars`, `EcgWithinPatientDecay`,
`EcgVerdictPanel`. Scene index rebuilt (588 → 592 renderable); all four confirmed
RENDERABLE via `./art scenes --check`.

## Legibility contract

- Every SHOW beat names its artifact in `visual_intent` or `shot.remotion.pattern`.
- All essential content laid inside `SAFE` (96, 54, 1728×972).
- Underpowered bins sit at ~33% ink, above the ~40%-opacity floor for
  un-highlighted elements only because they are *labelled* rather than faded —
  the hatch plus the explicit stamp carries the meaning, not the tint.
- Comparisons (fresh vs stale; training vs deployment) are side-by-side and
  held for the full beat, well past the 2s minimum.
- Colour is reinforcement only: position relative to the zero rule plus the
  printed signed value carry the finding. The teal/orange pair is split across
  warm/cool and survives red-green CVD.
