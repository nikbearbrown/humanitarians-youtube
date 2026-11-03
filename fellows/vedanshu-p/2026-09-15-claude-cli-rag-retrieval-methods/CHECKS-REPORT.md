# CHECKS-REPORT — claude-cli-rag-retrieval-methods

*Written before the first compile, per the cli-explainer PROOF GATE.*
*"Watch The Right Answer Get Outvoted." · RAG Foundations, Chapter 6.*

---

## Beat classification

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Spine role | Class | On-screen artifact |
|---|---|---|---|
| B00 | INTRO | SHOW | Composer types the ask; three output lines land |
| B01 | PROBLEM | SHOW | Two query cards converging on the one gold passage |
| B02 | CLI | SHOW | The BM25 prompt, incl. the tokenisation requirement |
| B03 | CODE | SHOW | `bm25_search.py` — the TOKEN regex, `idf()`, `score()` |
| B04 | OUTPUT | SHOW | Real transcript: HIT on the code, MISS on the paraphrase |
| B05 | CLI (revision) | SHOW | The revised prompt — dense + RRF, report all three |
| B06 | CODE (revision) | SHOW | `hybrid_search.py` — `rrf()` and the dense dot product |
| B07 | OUTPUT (revision) | SHOW | 3×2 method/query matrix resolving row by row |
| B08 | OUTPUT | SHOW | The fusion arithmetic and the 0.00025 margin |
| B09 | SUMMARY | SHOW | Headline/subline resolve |
| B10 | NEXT STEPS | SHOW | Composer with the viewer's prompt typed in |
| B11 | OUTRO | SHOW | Title restate, handle, author signature |

**Every OUTPUT beat is motion, never a still** (spine requirement): B04 is a
staggered transcript, B07 resolves three rows in narration order, B08 writes out
two reciprocal sums then settles the margin. No output slot is static or slated.

## The mandatory CLI spine

| Requirement | Status |
|---|---|
| INTRO on the interface, ask shown answered (COLD OPEN LAW) | ✓ B00 |
| PROBLEM beat after intro, before the CLI loop | ✓ B01 — the two employees, no prompt yet |
| Cycle 1: CLI → CODE → OUTPUT | ✓ B02 → B03 → B04 |
| **≥1 revision cycle (THE REVISION LAW)** | ✓ B05 → B06 → B07 (+B08, a second output from the same run) |
| SUMMARY | ✓ B09 |
| NEXT STEPS (HANDOFF LAW) | ✓ B10 — read aloud verbatim, then discussed |
| OUTRO, title restate, last beat | ✓ B11 |

## Legibility contract (every SHOW claim beat)

- [x] Names its on-screen artifact in `shot.show` / `shot.visual_intent`
- [x] ~15–35% negative space — `FigureFrame` reserves the chrome bands; tables and rows sit at ≤96% of the figure width
- [x] Un-highlighted elements never below ~40% opacity — non-accented matrix cells render in full `INK`/`INK_SOFT`, never ghosted
- [x] Comparisons shown side-by-side and held — B01's two queries, B07's three rows and B08's two candidates all persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

- **FRAMEWORK before examples ✓** — B00/B01 establish that there are two kinds
  of match and that one query suits each, before any code exists.
- **WORKED EXAMPLE ✓** — the chapter's own example, executed rather than
  described: the same gold passage, two queries, three retrievers, measured.
- **FALSIFIABILITY ✓** — this reel is unusually strong here, because the run
  contradicted the expected result and the reel reports that:
  (a) the fused hybrid **lost** the paraphrase, with the rank arithmetic shown
  in B08; (b) dense retrieval did **not** fail the exact-code query, contrary to
  the weakness the chapter warns about — and B09 names the reason (12 passages
  is far too small to reproduce an effect documented over rare entities at
  scale). Neither finding was engineered away.
- **SCAFFOLDED TASK ✓** — B10 asks the viewer to find the queries where their
  own hybrid is *worse* than its best single retriever, and to show the
  arithmetic.
- **BOUNDS/BOOKENDS ✓** — intro → problem → build → summary → handoff → outro.
  Typing appears only in composer beats (B00, B02, B05, B10).
- **NO-SOURCE-NO-VERDICT ✓** — every on-screen number is captured stdout
  (`_run-bm25.txt`, `_run-hybrid.txt`); every conceptual claim traces to the
  chapter or a source it cites. See SOURCES.md.

## Law checks

| Law | Status |
|---|---|
| ACTUAL-CODE LAW | ✓ Both CODE beats quote `code/*.py` verbatim; the scripts run; the output beats are their real stdout |
| Dense retrieval is REAL | ✓ Genuine `all-MiniLM-L6-v2` weights, forward pass in numpy, validated 1.000 / 0.555 / 0.100. No similarity score is hand-set |
| REVISION LAW | ✓ One full revision cycle in the 16:9 cut |
| SPARK-LINE LAW | ✓ B02 `"The ask,"`, B05 `"The change,"`, B10 `"Your turn."`; B00 carries the hello. No empty greeting on a composer beat |
| ASK → RESULT LAW | ✓ Every composer beat is followed by what it produced |
| REBUILD LAW | ✓ Fig. 02 rebuilt inside B08 with measured ranks; Fig. 01 deliberately unused (documented). No source image embedded |
| DOODLE-BANNED LAW | ✓ No `DoodleScene` / `DoodleChart` |
| HANDOFF LAW | ✓ Interesting prompt, read verbatim, then discussed |
| OUTRO LAW | ✓ Exact title restate; `TitleOutroChannel` per OUTRO-LOCK.md §Scope |
| GATE L | ✓ Four searches before authoring; every close lead read and rejected on props (content hardcoded elsewhere); three components built, registered both aspects, indexed |
| Free by default | ✓ Kokoro `am_onyx` + local numpy/model cache. **$0.00**. No paid API, no network call |
| NARRATION BUDGET | ✓ Body beats 55–70 words. Bookends exempt |

## Rhythm

No two consecutive beats share a visual scheme:

```
B00 composer · B01 two-query cards · B02 composer · B03 code · B04 transcript
B05 composer · B06 code · B07 matrix · B08 fusion rows · B09 summary card
B10 composer · B11 title
```

The composer recurs only where the interface IS the subject — the asks and the
handoff (ILLUSTRATE LAW). Code and output beats carry the middle.

## Open items

None blocking. Frame-level VISUAL QC LAW pass logged separately in
`_qc/REPORT.md` after the render.
