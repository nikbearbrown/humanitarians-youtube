# CHECKS-REPORT — "BLIP: Noisier Data, Better Model?"

The PROOF GATE authoring exit condition, written **before** the first render (per the
ai-explainer skill: "write before the slate, not after"). Classification rules are
`skills/make/nopunt/SKILL.md` § "SHOW / HOLD / CARD".

```
11 SHOW / 0 justified-HOLD / 0 PUNT-flagged
Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

## Per beat

| Beat | Act | Class | The on-screen artifact, and how it stays legible |
|---|---|---|---|
| B00 | ASK | **SHOW** | The composer types the three-part ask and answers it with four output lines. Lines hand-broken to ≤ 46 chars so the mono block wraps at an authored point on the 972px short axis, in both cuts. |
| B01 | SUMMARY | **SHOW** | Title, one-breath thesis, three numbered roadmap cards that rise in spoken order. Thesis renders as ONE paragraph wrapped by its box — authored line breaks double-wrap at 972px, which is how the sibling reel broke a clause in half. |
| B02 | FRAMEWORK | **SHOW** | Four numbered axes, each with the table that proves it in mono at the right. The rubric lands **before** any BLIP specific. Terracotta rule draws under the four. |
| B03 | MECHANISM | **SHOW** | Three cards, each holding an SA/CA/FFN chip stack and the loss it activates. CA renders dashed on the unimodal card — the absence is drawn, not just unstated. |
| B04 | WORKED-EXAMPLE | **SHOW** | A drawn web image, its two candidate captions, and the filter's verdict struck through one of them as it lands. Twenty tiles carry the published 25% rate. The two strings are labelled illustrative in frame. |
| B05 | EDGE-CASE | **SHOW** | Two rejection rates counting to 8% and 25%, then four downstream rows with render-computed deltas. Both columns are held together for the whole beat — the side-by-side requirement, not a voiced comparison. |
| B06 | FRICTION | **SHOW** | A butterfly around one spine: noise grows left, accuracy grows right, both wings longer as you go down. Both axis floors declared before the bars draw. |
| B07 | ABLATION | **SHOW** | Five bars on a declared truncated axis with a break glyph, a dashed reference line at 80.6 composed from the rows, and the published exception rendered beside the claim. |
| B08 | VERDICT | **SHOW** | The Claude artifact page — the UI is the subject here. Four verdict lines, each carrying its own number, and the source note under a hairline. |
| B09 | HANDOFF | **SHOW** | The composer with the audit prompt typed in, read aloud verbatim, plus PASS/FAIL/WATCH output lines showing what a good answer looks like. |
| B10 | OUTRO | **SHOW** | Title restate, poster-style serif with the terracotta period, handle beneath. |

No beat is a bare CARD and none is a PUNT. Every beat that makes a factual claim names its
artifact in `shot.show` and renders its citation in the same frame.

## Legibility contract

| Requirement | Status |
|---|---|
| Artifact named in `shot.show` | ✓ all 11 beats, 3–7 ordered events each |
| ~15–35% negative space | ✓ enforced by GATE V's canvas-fill floor (55% ink bbox) from the other side |
| Un-highlighted elements ≥ ~40% opacity | ✓ nothing fades below the `INK_SOFT`/`GHOST` tokens; rejected items are struck, not ghosted out |
| Comparisons side-by-side, held ≥ 2s | ✓ B05 (two columns, whole beat), B06 (two wings, whole beat), B07 (five bars + reference line, ~5s) |
| Sources on screen | ✓ `ReelKit.Stage` renders `source` under every illustration; the two UI evidence beats carry `sourceNote` |

## Teaching arc

| Item | Beat | Note |
|---|---|---|
| FRAMEWORK before examples | B02 | The four-axis audit is beat 3 of 11, ~19s in, ahead of every BLIP number except the cold open's preview |
| WORKED EXAMPLE | B04 | CapFilt run on one image, then on a cohort at the published rate |
| FALSIFIABILITY | B05, B07 | B05 is the paper's own stress test of axis 2; B07 names where the thesis fails (captioning CIDEr) |
| SCAFFOLDED TASK | B09 | Quote-and-grade all four axes, then name the unproven one |
| BOOKENDS | B00, B01, B09, B10 | Cold open → BLUF → … → verdict → handoff → title restate |
| NO SOURCE, NO VERDICT | all | Every published figure carries its table in the same frame; the one illustrative element says so |

## Motion mix (MOTION.md ~40% per-language cap)

`reveal:4 (36%)` · `drawon:3 (27%)` · `type-on:2 (18%)` · `annotate:1 (9%)` · `count-up:1 (9%)`

Max 36%, under the cap. The labels are chosen against what each beat actually does:
B04 annotates an artifact (a strike drawing through a caption — MOTION.md §7), B05 is
counters resolving, B06/B07 are chart draw-on, B02's rule draws.
