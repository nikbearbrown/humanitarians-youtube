# CHECKS-REPORT — Labels Are Not Decoration.

PROOF GATE, written before the first render (nopunt SKILL.md §"SHOW / HOLD / CARD").

```
10 SHOW / 1 justified-HOLD / 0 PUNT-flagged

Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per-beat classification

| Beat | Pattern | Class | Why |
|---|---|---|---|
| B00 | ClaudeComposerAsk | SHOW | the ask types, send arms, output lines land — COLD OPEN LAW |
| B01 | BrutalistHesitantWriter | SHOW | the misconception is typed, caught and corrected on screen |
| B02 | PromptTwoLayouts | SHOW | the left wall fills, then labelled sections land one at a time beside it |
| B03 | LostMiddleCurve | SHOW | the same passage is placed at three positions; the marker dims in the middle; the U draws |
| B04 | EvidenceTiers | SHOW | two claims fill, then their evidence bars resolve visibly unequal |
| B05 | GroundingDrift | SHOW | two sentences land; one draws an anchor to its source, one has none to draw |
| B06 | ProblemPredictCard | **justified HOLD** | the predict beat exists to open a gap and hold it. Resolving it here would destroy the beat's function; B07 is the reveal |
| B07 | AnnotatedPrompt | SHOW | sections fill, callouts draw in, the relevant chunk lights and the near-miss recedes, the answer lands cited |
| BVDT | ClaudeVerdictArtifact | SHOW | verdict lines land in sequence; the honest last line holds alone |
| BHTF | ClaudeComposerAsk | SHOW | the handoff prompt types; held on screen while the voice discusses it |
| BOUT | TitleOutroChannel | SHOW | title restates poster-style; handle and signature settle |

No beat is a bare CARD. No PUNTs — every bespoke visual need was searched
(GATE L), missed, and discharged by **building** the component.

## Teaching arc detail

- **FRAMEWORK before examples ✓** — B01 states the whole idea in one breath and
  B02 lays out the three-part anatomy before any worked case appears. The
  resignation example does not arrive until B06.
- **WORKED EXAMPLE ✓** — the chapter's own: "How much notice do I need to give
  before resigning?", with the resignation-policy chunk and the HR-contacts
  chunk that merely contains the word *notice*. Predicted at B06, resolved at B07.
- **FALSIFIABILITY ✓** — B04 is built around it. The chapter explicitly declines
  to promote the top-of-prompt ordering rule to a law because it rests on one
  vendor's internal testing; the beat draws that as two visibly unequal evidence
  tiers rather than flattening both into a "best practices" list.
- **SCAFFOLDED VIEWER TASK ✓** — BHTF asks the viewer to print the prompt their
  own system actually sends and mark its boundaries. Concrete, runnable, and
  aimed at the exact thing the chapter says goes unexamined.
- **FOUR BOOKENDS ✓** — cold open (B00), BLUF (B01), verdict (BVDT), handoff +
  outro (BHTF, BOUT).
- **NO-SOURCE-NO-VERDICT ✓** — every on-screen claim carries its citation:
  Anthropic Claude Platform Docs for the structure/tagging/grounding guidance,
  Liu et al. (TACL 2024) for the position effect, and the chapter itself for the
  worked example. Full record in SOURCES.md.

## Legibility contract (per SHOW/HOLD claim beat)

| Requirement | Status |
|---|---|
| Names its on-screen artifact in `shot.show` / `shot.visual_intent` | ✓ all body beats |
| ~15–35% negative space | designed for; confirmed at QC |
| Un-highlighted elements never below ~40% opacity | ✓ — B07's dimmed near-miss chunk bottoms out at 45%, deliberately readable |
| Comparisons shown side-by-side, held ≥2s | ✓ B02 (two layouts), B04 (two tiers), B05 (two sentences) |

## Honesty notes carried into the build

1. **B03 draws no numbers.** The chapter reports the *direction* of the
   Lost-in-the-Middle effect and publishes no per-position figures. REBUILD LAW
   allows exact data only when the source gives it, and orderings/anchors
   otherwise — so the accuracy axis is deliberately unlabelled. Inventing
   plausible percentages would convert a real finding into a fabricated one.
2. **B04 exists because the chapter refused to simplify.** Reporting both tiers
   as equally settled would be the easiest and most misleading edit available.
3. **B05 keeps both sentences equally confident.** Greying out the ungrounded
   sentence would destroy the point — in a real answer the drift is invisible,
   which is why it survives review.
