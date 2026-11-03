# CHECKS-REPORT — The Geometry of Meaning

Reel: `claude-stem-geometry-of-meaning` · 9 beats · **measured 124.7s (2:05)** vs 2:30 target
**GATE V (16:9): 18 frames · 0 BLOCKER · 0 MAJOR ✓**

## Deliverables

| | File | Format |
|---|---|---|
| 16:9 master | `claude-stem-geometry-of-meaning-slate.mp4` | 3840×2160 @ 24fps |
| 9:16 companion | `vertical/claude-stem-geometry-of-meaning-vertical-slate.mp4` | 1080×1920 @ 24fps |

## Per-beat classification

| Beat | Class | Measured | Pattern |
|---|---|---|---|
| B00 | SHOW | 14.53s | ClaudeComposerAsk |
| B01 | SHOW | 10.35s | BrutalistHesitantWriter — ≥9s ✓ |
| B02 | SHOW | 17.24s | ThreeStageBand |
| B03 | SHOW | 9.15s | ClaudeComposerAsk (ask half of ASK→RESULT) |
| B04 | SHOW | 18.41s | **EmbeddingScatter2D** (new) |
| B05 | SHOW | 17.54s | SimilarityBlindspot |
| B06 | SHOW | 11.86s | ClaudeCodeBeat |
| BHTF | SHOW | 16.19s | ClaudeComposerAsk |
| BOUT | SHOW | 9.28s | HaiTitleOutro |

**9 SHOW / 0 HOLD / 0 PUNT.** Slots 9/9 filled. **No slate in this reel** — unlike the
Gatekeeper build, nothing here was blocked on unsupplied material.

## Dual render — both aspects delivered

**All 9 beats rewired to registered `916` compositions. Zero flagged, zero centre-cut.**

The script asked to "keep core visual artifacts center-framed for 9:16 safe zones."
`EmbeddingScatter2D` satisfies that structurally rather than by luck: the plot is a
**centred square sized to the smaller safe dimension**, so the artifact is already
centred and portrait needs no separate layout. `SimilarityBlindspot` stacks its two
cards; `ThreeStageBand` serializes top-to-bottom.

## Defects found and fixed — all by reading frames, none caught by a gate

GATE V passed this reel 0/0 on its first compile. Every defect below was still present
at that point. The mp4 probe and the gate are not QC.

| Beat | Defect | Fix |
|---|---|---|
| B04 | The measured DOG↔WOLF link **struck through both labels** — labels sat beside their dots, directly in the line's path. | Labels centred above/below the dot instead of beside it. |
| B04 | The link caption was anchored above the line, which put it **off the top of the canvas**. Invisible. | Caption flips to whichever side of the link has room. |
| B04 | Point labels near `y = ±0.9` **crossed the plot border**. | Clamped inside the plot rect. |
| B04 | `CANINE` / `FELINE` captions sat on the same side as the centred point labels and **collided with DOG**. | Moved left of the y-axis. |
| B04 | Plot undersized, leaving dead margin (FILL-THE-CANVAS). | Enlarged to the available safe square. |
| B03 | Audio was 5.7s — **the composer prompt could not finish typing**. | Narration lengthened to 9.15s. Third reel running into this; the rule is ~7s minimum for any beat that types a long command. |

## Teaching arc

```
FRAMEWORK ✓     B01 BLUF + B02 the three stages, both before the plot.
WORKED EXAMPLE ✓ B04 — DOG/WOLF/CAT with one distance actually measured on screen.
FALSIFIABILITY ✓ B05 — the antonym flaw; the framework's own breaking point.
SCAFFOLDED TASK ✓ B06 runnable Python; BHTF extends it to the viewer's own probing.
BOOKENDS ✓      B00 cold open · B01 BLUF · BHTF handoff · BOUT restate.
NO-SOURCE-NO-VERDICT ✓ every figure traces to the script or to arithmetic.
```

## Law checks (verified on rendered frames)

- **COLD OPEN LAW** ✓ · **EXECUTIVE-SUMMARY LAW** ✓ (10.35s ≥ 9s, `lead_silence_s: 0.8`)
- **ILLUSTRATE LAW** ✓ UI only at B00, B03, BHTF, BOUT. No two consecutive beats share a
  visual scheme.
- **ASK → RESULT LAW** ✓ B03 → B04.
- **HANDOFF LAW** ✓ prompt read verbatim aloud, then discussed.
- **OUTRO LAW** ✓ title restate, terracotta period, handle beneath.
- **DOUBLE-CHECK LAW** ✓ see SOURCES.md — axis direction corrected against the script's
  own coordinates, `0.82` labelled as the author's illustrative figure, plot captioned
  on screen as a simplified teaching model.

## Open items

1. **`0.82` is illustrative, not measured.** The script states it; this build ran no
   embedding model. To make it real: run the model, then set `simValue` and `simFillTo`
   on B05 to the measured cosine.
2. **X-axis labels were flipped** relative to the script's caption to match the script's
   own coordinates and VO. See SOURCES.md §1 — confirm this is what was intended.
3. **Lane-mix warning (not blocking).** `remotion` carries 9/9 beats against MOTION.md's
   ~40% guidance. Deliberate: every beat is a generated diagram; there is no archival
   footage or maths beat in this topic. B04 is the natural Manim candidate if variety
   matters.
4. **SKIN LINT warning (not blocking, expected).** `BOUT` uses `HaiTitleOutro` where the
   linter wants `ClaudeTitleOutro`; the latter hardcodes `@NikBearBrown` and is scoped by
   OUTRO-LOCK.md to claude-liam reels.
5. **Runtime 2:05 against a 2:30 target.** Not padded — duration is an output, not a
   target (`duration-planner`). If the target is firm, B02 and B04 have room for one more
   sentence each.
6. **Paperwork.** Built with `ART_FACTS=0`. A fully gated `./art run` needs
   `FACTCHECK.md`, `SHOTLIST.md`, `PROMPTS.md`.
7. **`./art final` not yet run** — no clean master without the review label.
