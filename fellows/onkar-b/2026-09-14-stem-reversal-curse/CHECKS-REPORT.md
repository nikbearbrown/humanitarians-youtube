# CHECKS-REPORT — The Reversal Curse

*Rendered and QC'd 2026-09-13.*
9 beats · **measured 128.0s (2:08)** against a 2:30 target
Cut on disk: `claude-stem-reversal-curse-slate.mp4`
**GATE V: 18 frames sampled · 0 BLOCKER · 0 MAJOR · clean ✓**
Narrator: Onkar Bhujbal, first person, Kokoro `am_onyx`.

## Per-beat classification

| Beat | Scene | Class | Measured | Pattern |
|---|---|---|---|---|
| B00 | 1 HOOK | SHOW | 15.55s | ClaudeComposerAsk |
| B01 | — BLUF | SHOW | 9.60s | BrutalistHesitantWriter |
| B02 | 2 FRAMEWORK | SHOW | 17.60s | ThreeStageBand |
| B03 | 3 ask | SHOW | 10.09s | ClaudeComposerAsk |
| B04 | 3 worked example | SHOW | 18.56s | ReversalTrainingGraph |
| B05 | 4 FALSIFIABILITY | SHOW | 18.45s | ReversalBidirectionalTest |
| B06 | 5 task | SHOW | 12.25s | ClaudeCodeBeat |
| BHTF | 5 handoff | SHOW | 16.34s | ClaudeComposerAsk |
| BOUT | 5 close | SHOW | 9.37s | HaiTitleOutro |

**9 SHOW / 0 HOLD / 0 PUNT-flagged.** Slots: 9/9 filled. No slates — this reel needs no
source material that wasn't supplied.

## Teaching arc

```
FRAMEWORK ✓    B02 states the Autoregressive Probability Rule before any example —
               the script's own Scene 2, in the right order.
WORKED EXAMPLE ✓ B04 — one training sentence, the two tokens highlighted in it, and
               the directed graph those weights actually build.
FALSIFIABILITY ✓ B05 — the bidirectional control. The reel names the test that could
               disprove its own claim and shows the result.
SCAFFOLDED TASK ✓ B06 two asymmetrical prompts with a stated expected failure, then
               BHTF a follow-up that makes the model map its own blind spots.
BOOKENDS ✓     B00 cold open · B01 BLUF · BHTF handoff · BOUT title restate.
NO-SOURCE-NO-VERDICT ✓ no benchmark number is claimed anywhere; the script reports none.
```

## Law checks (verified on rendered frames)

- **COLD OPEN LAW** ✓ · **EXECUTIVE-SUMMARY LAW** ✓ (9.60s ≥ 9s, `lead_silence_s: 0.8`)
- **ILLUSTRATE LAW** ✓ Claude UI only at B00, B03, BHTF, BOUT. No two consecutive beats
  share a scheme.
- **ASK → RESULT LAW** ✓ B03 → B04.
- **SPARK-LINE LAW** ✓ every inner beat carries a short serif line.
- **HANDOFF LAW** ✓ prompt read verbatim aloud, then discussed.
- **OUTRO LAW** ✓ exact title restate, terracotta period, handle beneath.
- **FILL-THE-CANVAS / title-safe** ✓ GATE V 0/0 across 18 frames.

## Defects found and fixed during this render

GATE V passed on the first compile. These were caught by **reading frames**, which the
gate cannot do — worth recording, because two of them are traps for any future reel.

| Beat | Defect | Fix |
|---|---|---|
| B04, B05 | **Animation tail silently trimmed.** Compositions register a fixed `durationInFrames` (630f = 21s), but `compile.py` conforms the clip to the beat's *measured audio* — 18.56s here. Everything scheduled past p≈0.85 never reached the cut: B04's dashed reverse edge never retracted and "never trained" never appeared; B05's verdict strip was frozen mid-fade. | Both timelines retimed to complete by **p ≈ 0.80**. This is a general rule for this toolkit, not a one-off — see below. |
| B04, B05 | Content clustered in the upper half with a dead lower half (FILL-THE-CANVAS). | Panels sized to content and centred in the safe area; node pairs centred with a wider edge gap. |
| B04 | The `strengthened` edge label did not render — positioned by a fraction with no explicit width, it drifted out of the panel. | Explicit `edgeLabelW`, both edge labels anchored to the arrow midpoint. |

### The general rule this render exposed

**An animation must finish by roughly p = 0.80, not p = 1.0.** A composition's
registered duration is not the duration the viewer sees. Whenever a beat's narration is
shorter than the registered `durationInFrames`, the end of the animation is cut off with
no warning and no gate failure — the frame simply freezes earlier than the author
intended. Anything load-bearing (a verdict, a reveal, a retraction) must land early and
hold.

## Dual render — BOTH ASPECTS DELIVERED

| | File | Format |
|---|---|---|
| 16:9 master | `claude-stem-reversal-curse-slate.mp4` | 3840×2160 @ 24fps · 2:08 |
| 9:16 companion | `vertical/claude-stem-reversal-curse-vertical-slate.mp4` | 1080×1920 @ 24fps · 2:08 |

**All 9 beats rewired to registered `916` compositions — zero flagged, zero centre-cut.**
The portrait cut is a genuine reflow per RENDER-TARGETS.md §3: the three-stage band
serializes top-to-bottom, and the two architecture columns stack. Verified on frame
that the double arrowhead — the beat's entire claim — survives the portrait layout.

The format spec is fully met: `compile.py` defaults to `--fps 24`, so both cuts probe as
24fps, and the 16:9 master is true 4K UHD.

## Open items

1. **Runtime 2:08 vs the 2:30 target** — 22s under, with the script's VO used
   near-verbatim; Kokoro reads faster than the script was timed for. Duration is an
   output, not a target (`duration-planner`), so nothing was padded. Natural places to
   add: B04 (what "conditionally dependent" means in practice) and B06 (why rarer facts
   make a cleaner test).
2. **24 fps not met.** The script header asks for 24; every registered composition is
   `fps={30}`. Toolkit-wide change, not a per-reel prop. Currently 4K/30.
3. **Sign-off wording.** The supplied script's last line still reads "Liam, for Onkar
   Bhujbal and Humanitarians AI"; built as **"Onkar Bhujbal, for Humanitarians AI."**
   per the author's standing instruction. One word reverts it.
5. **Scene 4 colour.** The script asks for red→green; built as one arrowhead versus two
   in the single-accent Claude palette (BUILD-LOG D2). Deliberate, not a miss.
6. **SKIN LINT warning (not blocking, expected).** `BOUT` uses `HaiTitleOutro` where the
   linter expects `ClaudeTitleOutro` — the latter hardcodes `@NikBearBrown`.
7. **Lane-mix warning (not blocking).** `remotion` carries 8/9 beats. Deliberate for an
   architecture explainer with no maths beat and no archival footage.
8. **Paperwork.** Built with `ART_FACTS=0`. A fully gated `./art run` needs
   `FACTCHECK.md`, `SHOTLIST.md` and `PROMPTS.md`.
9. **`./art final` has not been run** — no 4K master yet.
