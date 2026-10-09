# CHECKS-REPORT — claude-liam-context-window (12-beat / 60s cut)

Rewritten for the rework to the Brutalist first-project spec (60s, 12 beats).
Supersedes the 9-beat/154.5s version's report. Reflects `nopunt/SKILL.md`'s
SHOW/HOLD/CARD classification and whole-sheet teaching-arc checklist.

## Per-beat classification

12 SHOW / 0 justified-HOLD / 0 PUNT-flagged

| Beat | Class | Component |
|---|---|---|
| B00 | SHOW | `ClaudeComposerAsk` — bookend |
| B01 | SHOW | `BrutalistHesitantWriter` — bookend; `qc.sparse_by_design` declared |
| B02 | SHOW | `ClaudeScienceLayerStack` (3 layers) |
| B03 | SHOW | `ClaudeScienceLayerStack` (2 layers) |
| B04 | SHOW | Manim `B04_TokenSplit` (`scenes.py`) |
| B05 | SHOW | `FormBCard` |
| B06 | SHOW | `AttritionChain` |
| B07 | SHOW | `FormBCard` |
| B08 | SHOW | `ScaleComparison` |
| B09 | SHOW | `ClaudeVerdictArtifact` — bookend |
| B10 | SHOW | `ClaudeComposerAsk` — bookend |
| B11 | SHOW | `OutroCTA` — bookend; `qc.sparse_by_design` declared |

## Teaching-arc checklist — honest result, not a rubber stamp

- [x] **FRAMEWORK** — B02/B03 state the shared-budget framework before any
      example.
- [~] **WORKED EXAMPLE** — **weakened.** B06 shows the ceiling climb, but at
      ~7s it no longer walks concrete turn-by-turn numbers on screen the way
      the long cut's dedicated beat did. Gestural, not a full worked example.
- [~] **FALSIFIABILITY** — **weakened.** B04/B05 gesture at "tokens aren't
      uniform" (a mild stress-test of the naive word=token assumption) but
      don't carry a dedicated counter-example beat.
- [x] **SCAFFOLDED viewer task** — B10 checks one concrete thing ("does it
      say what to drop first?") rather than the long cut's three-point
      rubric. Still clears the checklist's bar (a real criterion, not "ask
      Claude about X") but is thinner.
- [x] **Four bookends** — B00 cold open, B09 verdict/summary, B10 YOUR TURN,
      B11 title-restate outro.
- [x] **No source, no verdict** — every claim-bearing body beat (B00, B02,
      B03, B05, B06, B07, B08) carries on-screen evidence (composer output,
      layer cards, FormB lists, the room-remaining chart, the scale chart).

**Status: PASS with two disclosed weaknesses** (WORKED EXAMPLE,
FALSIFIABILITY) — an accepted, explicit cost of compressing to the 60s/12-beat
first-project spec, not an oversight. Full accounting of every cut/merge:
`SHOTLIST.md`. Fact-by-fact source table: `FACTCHECK.md` / `SOURCES.md`.
