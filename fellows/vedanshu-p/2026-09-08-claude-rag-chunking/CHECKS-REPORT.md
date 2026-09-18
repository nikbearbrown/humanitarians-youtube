# CHECKS-REPORT — claude-rag-chunking

*Written before the first compile, per the ai-explainer PROOF GATE.*
*Reel: "Where You Cut The Page." · RAG Foundations, Chapter 4 — Chunking Documents*

---

## Beat classification

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Class | On-screen artifact (named in `shot.show` / `shot.visual_intent`) |
|---|---|---|
| B00 | SHOW | Composer types the ask; send arms; three output lines land (ASK→RESULT at the cold open) |
| B01 | SHOW | The hesitant writer types the BLUF and corrects `preprocessing` → `a design decision` on screen |
| B02 | SHOW | Five topic bands converge and collapse into one dot; the query's match meter fills part-way and stops |
| B03 | SHOW | Size axis with a failure card at each end; small chunks strand a fragment, one fat chunk dilutes its fact |
| B04 | SHOW | A fact severed at a hard seam, then rescued by an overlap window; the split verdict resolves into two equal panels |
| B05 | SHOW | Three page strips, cut three ways; the fixed-count rule visibly severs a line mid-word |
| B06 | SHOW | Three-rung separator ladder lighting top-down, fallback arrows drawing between rungs |
| B07 | SHOW | Predict card: the question types in, underline draws, commit nudge lands |
| B08 | SHOW | Question pinned; three outcome rows resolve in order and hold side by side |
| BVDT | SHOW | Verdict artifact page — five lines written into the artifact panel |
| BHTF | SHOW | Composer with the viewer's prompt typed in ("Your turn.") |
| BOUT | SHOW | Title restate, handle, author signature |

No beat is a bare CARD. Every beat whose narration makes a factual or structural
claim names its artifact and animates it.

## Legibility contract (every SHOW claim beat)

- [x] Names its on-screen artifact in `shot.show` or `shot.visual_intent`
- [x] ~15–35% negative space — `FigureFrame` reserves the spark/headline/caption bands; no figure exceeds 86% of canvas width
- [x] Un-highlighted elements never faded below ~40% opacity — inactive ladder rungs and non-winning rows stay at full ink/`INK_SOFT`, never ghosted out
- [x] Comparisons shown side-by-side and held — B03 (both failure modes), B04 (both verdict panels), B05 (three strips), B08 (three outcome rows) all resolve and then HOLD to the end of the beat

## Teaching arc

```
FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

- **FRAMEWORK before examples ✓** — B01 states the whole idea (chunking is a
  design decision), then B02–B06 build the framework (whole-doc dilution → the
  size tradeoff → overlap → structure-aware → the separator mechanism). The
  worked example does not arrive until B07/B08, after the framework is complete.
- **WORKED EXAMPLE ✓** — B07/B08 run the chapter's own example: one 40-page
  benefits manual, one question ("How many vacation days do I get in my second
  year?"), chunked three ways, three different retrieval outcomes. Predict-then-
  reveal, so the viewer commits before seeing the answer.
- **FALSIFIABILITY ✓** — B04 is built for it. Overlap is presented as a guard
  with a clear rationale whose payoff is **not settled**: the practitioner
  default and the 2026 controlled study get equal panels, equal weight, and
  neither is marked as the winner. The narration says "hold this one loosely"
  out loud. The verdict artifact repeats the word "Unsettled."
- **SCAFFOLDED TASK ✓** — BHTF hands the viewer a prompt that runs on a document
  they already work with, and requires the model to argue the opposite case and
  rank the two failure modes. The narration reads it aloud verbatim, then spends
  two lines on why the second half is the part that matters (HANDOFF LAW).
- **BOUNDS/BOOKENDS ✓** — cold open (B00) → hesitant-writer BLUF (B01) → body →
  verdict page (BVDT) → handoff (BHTF) → title-restate outro (BOUT). Typing
  appears in exactly three beats: B00 (the ask), B01 (the overview being thought
  through), BHTF (the viewer's prompt).
- **NO-SOURCE-NO-VERDICT ✓** — every claim on screen traces to
  `chapters/04-chunking-documents.md` (fact-checked 2026-08-13, GATE 4, 0
  discrepancies) or to a source that chapter itself cites. See SOURCES.md.

## Law checks

| Law | Status |
|---|---|
| COLD OPEN LAW | ✓ B00 is `ClaudeComposerAsk`, shown answered (3 output lines) |
| EXECUTIVE-SUMMARY LAW | ✓ B01 is `BrutalistHesitantWriter`, audio window 11.01s (≥9s), explicit `lead_silence_s: 0.8`, seed set per reel |
| ILLUSTRATE LAW | ✓ Claude UI appears only at B00, BVDT, BHTF. B02–B08 are concept illustrations. No two consecutive beats share a visual scheme |
| SPARK-LINE LAW | ✓ Every inner figure beat carries one short serif spark line (≤5 words) |
| REBUILD LAW | ✓ Fig. 01 rebuilt natively as B05; captioned "Redrawn (simplified) from the chapter's own Fig. 01". No source image embedded anywhere |
| DOODLE-BANNED LAW | ✓ No `DoodleScene` / `DoodleChart` |
| HANDOFF LAW | ✓ BHTF prompt is interesting, read aloud verbatim, then discussed |
| OUTRO LAW | ✓ BOUT restates the title exactly; `TitleOutroChannel` (not the claude-liam-locked card — OUTRO-LOCK.md §Scope) |
| VOX LAW | ✓ Zero pantry stills. This chapter's evidence is text and diagrams, so zero is the correct outcome, not a gap |
| GATE L | ✓ Six searches run before authoring; six genuine misses; six new components built, registered at both aspects, and indexed (`./art scene-index`) — not slated. (`TEMPLATE-MISSES.md` is not written: that auto-log needs `--reel`, and a punt discharged by building leaves nothing outstanding — see SOURCES.md §Components.) |
| NARRATION BUDGET | ✓ Body beats B02–B08 run 50–66 words. Bookends exempt |
| Free by default | ✓ Kokoro `am_onyx`, local. $0.00. No paid API touched |

## Rhythm

No two consecutive beats share a visual scheme:

```
B00 composer · B01 writer · B02 collapse · B03 axis · B04 seam+split
B05 strips   · B06 ladder · B07 card     · B08 rows · BVDT artifact
BHTF composer · BOUT title
```

## Open items

None blocking. Frame-level VISUAL QC LAW pass is logged separately in
`_qc/REPORT.md` after the render.
