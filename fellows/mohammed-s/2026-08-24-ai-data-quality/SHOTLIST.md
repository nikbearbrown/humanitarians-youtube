# SHOTLIST — `ai-data-quality` · "The Rule, Not The Report."

Typed work order. Every slot is machine-fillable — there is **no human media
owed on this reel**, and `pantry/` is empty by design. Durations are the
measured Kokoro mp3s (ground truth), not estimates.

| Beat | Act | Lane | Composition | 16:9 | 9:16 | Dur | Owner |
|---|---|---|---|---|---|---|---|
| B00 | ASK | ask | `ClaudeComposerAsk` | 1920×1080 | `…916` @1080×1920 | 18.11s | machine |
| B01 | PROBLEM | remotion | `DqScoreVsField` | ✅ | `DqScoreVsField916` | 16.21s | machine |
| B02 | SCALE | remotion | `DqRuleScale` | ✅ | `DqRuleScale916` | 17.32s | machine |
| B03 | DEFINITION | remotion | `DqRuleCard` | ✅ | `DqRuleCard916` | 15.36s | machine |
| B04 | ASK | ask | `ClaudeComposerAsk` | ✅ | `…916` | 11.52s | machine |
| B05 | RESULT | remotion | `DqProposal` | ✅ | `DqProposal916` | 15.19s | machine |
| B06 | GATE | remotion | `DqRatifyGate` | ✅ | `DqRatifyGate916` | 17.47s | machine |
| B07 | RUNTIME | remotion | `DqPipelineGate` | ✅ | `DqPipelineGate916` | 15.19s | machine |
| B08 | TEARDOWN | remotion | `DqWhereItBites` | ✅ | `DqWhereItBites916` | 15.85s | machine |
| B09 | VERDICT | bookend | `ClaudeVerdictArtifact` | ✅ | `…916` | 17.90s | machine |
| B10 | HANDOFF | bookend | `ClaudeComposerAsk` | ✅ | `…916` | 19.80s | machine |
| B11 | OUTRO | bookend | `ClaudeTitleOutro` | ✅ | `…916` | 7.57s | machine |

**Total 187.5s — 3:07.**

## Lane histogram

- UI beats (ILLUSTRATE LAW allows these five and no others): B00 cold open ·
  B04 ask micro-beat · B09 verdict artifact · B10 handoff · B11 outro — **5**
- Concept illustrations (C3), one bespoke component each: B01 B02 B03 B05 B06
  B07 B08 — **7**
- Manim: **0** (see `scenes.py` — a declared choice, not an omission)
- Human/pantry media: **0**

No two adjacent beats share a visual scheme. The longest UI run is one beat.

## The two ASK → RESULT pairs

1. **B00 → the whole reel.** The cold open's composer shows its result lines
   (`318 candidate checks`, `41 flagged`), so the ask lands answered and the
   numbers it prints are the ones B06 later sorts.
2. **B04 → B05.** The single-column ask, then exactly what came back. B05 is
   the only beat where the model's output is the subject, and it is shown as
   evidence-then-rule-then-cost, in that order, because that is the order the
   narration interrogates it in.

## Terracotta ledger (one accent moment per beat)

| Beat | The one terracotta thing |
|---|---|
| B01 | the strike through 98.7% |
| B02 | the "stale in 90 days" wipe |
| B03 | the `block` severity token |
| B05 | the 1,284 counter |
| B06 | the review gate bar + its chip |
| B07 | the quarantine box and the rows that divert into it |
| B08 | the underline on card 03 |

Nothing else in the body is coloured. Cream ground `#F2F0E9`, warm ink
`#3D3929`, terracotta `#D97757` / `#C6613F`.

## Geometry contract

Both cuts render from **one component per beat**, branching on `portrait`
internally — so the vertical cut can never drift from the horizontal one in
content, only in arrangement:

| Scene | 16:9 arrangement | 9:16 arrangement |
|---|---|---|
| DqScoreVsField | score left, field right | score on top, field below |
| DqRuleScale | 80×50 cell field, stats below | 40×100 cell field, stats below |
| DqRuleCard | clause + annotation on one row | annotation wraps under its clause |
| DqProposal | bars, card, counter stacked | same, taller bars |
| DqRatifyGate | flow left→right, lanes stack right | flow top→bottom, lanes stack below |
| DqPipelineGate | source→gate→warehouse across; quarantine below | source→gate→warehouse down; quarantine beside |
| DqWhereItBites | 3 columns | 3 rows |

Type is sized as a fraction of the safe box, and the safe box is a uniform 5%
inset in both aspects — so the same authored size renders **proportionally
larger in portrait**, which is what phone viewing needs.
