# CHECKS-REPORT — claude-cli-rag-vector-databases

*Written before the first compile, per the cli-explainer PROOF GATE.*
*"Watch Exact Search Hit A Wall." · RAG Foundations, Chapter 5.*

---

## Beat classification

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Spine role | Class | On-screen artifact |
|---|---|---|---|
| B00 | INTRO | SHOW | Composer types the ask; send arms; three output lines land |
| B01 | PROBLEM | SHOW | Headline + subline resolve: exact search doesn't scale |
| B02 | CLI | SHOW | The prompt for the brute-force benchmark types in |
| B03 | CODE | SHOW | `brute_force_search.py` — the real search function |
| B04 | OUTPUT | SHOW | Real captured transcript: 0.08 / 1.16 / 10.87 ms, verdict line |
| B05 | CLI (revision) | SHOW | The revised prompt — note the recall requirement |
| B06 | CODE (revision) | SHOW | `ann_search.py` — `n_cells`, `build_lists`, `ivf_search` |
| B07 | OUTPUT (revision) | SHOW | Two plotted series drawing across collection size |
| B08 | OUTPUT (dial) | SHOW | Recall plotted against share of collection compared |
| B09 | SUMMARY | SHOW | Headline + subline resolve: approximate is a setting |
| B10 | NEXT STEPS | SHOW | Composer with the viewer's prompt typed in |
| B11 | OUTRO | SHOW | Title restate, handle, author signature |

**Every OUTPUT beat is motion, never a still** (spine requirement): B04 is a
staggered transcript, B07 draws two polylines progressively, B08 sweeps a curve
through four measured points. No output slot is a static png, and none is a slate.

## The mandatory CLI spine

| Requirement | Status |
|---|---|
| INTRO on the interface, ask shown answered (COLD OPEN LAW) | ✓ B00 |
| PROBLEM beat after intro, before the CLI loop | ✓ B01 — stakes stated with no prompt yet |
| Cycle 1: CLI → CODE → OUTPUT | ✓ B02 → B03 → B04 |
| **≥1 revision cycle (THE REVISION LAW)** | ✓ B05 → B06 → B07 (+B08, a second output from the same run) |
| SUMMARY | ✓ B09 |
| NEXT STEPS (HANDOFF LAW) | ✓ B10 — read aloud verbatim, then discussed |
| OUTRO, title restate, last beat | ✓ B11 |

## Legibility contract (every SHOW claim beat)

- [x] Names its on-screen artifact in `shot.show` or `shot.visual_intent`
- [x] ~15–35% negative space — `FigureFrame` reserves the spark/headline/caption bands; plots sit at ≤86% canvas width
- [x] Un-highlighted elements never below ~40% opacity — the non-accented series and non-final dial points are full-strength ink, never ghosted
- [x] Comparisons shown side-by-side and held — B07's two series both remain plotted to the end of the beat; B08's four points all persist once drawn

## Teaching arc

```
FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

- **FRAMEWORK before examples ✓** — B01 states why exact search fails before any
  code exists; the build then tests that claim.
- **WORKED EXAMPLE ✓** — the whole body IS the worked example, and it is executed
  rather than described: 100,000 vectors, 20 queries, top-10, measured twice.
- **FALSIFIABILITY ✓** — B08 is built for it. The reel does not claim the index is
  free: it measures recall against the exact answer at four settings and shows
  that at the cheapest setting you recover only 33% of the true neighbours. The
  method is shown failing before it is shown succeeding.
- **SCAFFOLDED TASK ✓** — B10 asks the viewer to sweep the setting on their own
  data and, critically, to surface *the query where it first breaks* rather than
  an average.
- **BOOKENDS ✓** — cold open → problem → build → summary → handoff → outro.
  Typing appears only in the composer beats (B00, B02, B05, B10), each for a
  different reason.
- **NO-SOURCE-NO-VERDICT ✓** — every on-screen number traces to a captured run
  (`_run-brute.txt`, `_run-ann.txt`); every conceptual claim traces to the
  chapter or a source it cites. See SOURCES.md.

## Law checks

| Law | Status |
|---|---|
| ACTUAL-CODE LAW | ✓ Both CODE beats quote `code/*.py` verbatim. The scripts run; the reel's numbers are their real stdout. Prompt → code → output is one honest receipt |
| REVISION LAW | ✓ One full revision cycle in the 16:9 cut |
| SPARK-LINE LAW | ✓ B02 `"The ask,"`, B05 `"The change,"`, B10 `"Your turn."`; B00 carries the hello. No empty greeting on any composer beat |
| ASK → RESULT LAW | ✓ Every composer beat is followed by what it produced |
| REBUILD LAW | ✓ Fig. 01 rebuilt natively as B07, from measured data. No source image embedded. Fig. 02 deliberately not used — see SOURCES.md |
| DOODLE-BANNED LAW | ✓ No `DoodleScene` / `DoodleChart` |
| HANDOFF LAW | ✓ Interesting prompt, read verbatim, then two lines on why the last clause matters |
| OUTRO LAW | ✓ Exact title restate; `TitleOutroChannel` per OUTRO-LOCK.md §Scope |
| GATE L | ✓ Four searches before authoring; the one close lead (`BarChart`) rejected on palette grounds, documented; two components built, registered at both aspects, indexed |
| Free by default | ✓ Kokoro `am_onyx`, local. **$0.00**. No paid API touched |
| NARRATION BUDGET | ✓ Body beats 50–66 words. Bookends exempt |

## Rhythm

No two consecutive beats share a visual scheme:

```
B00 composer · B01 summary card · B02 composer · B03 code · B04 transcript
B05 composer · B06 code · B07 line chart · B08 curve · B09 summary card
B10 composer · B11 title
```

The composer recurs, but only where the interface IS the subject (the asks and
the handoff) — ILLUSTRATE LAW. Code and output beats carry the middle.

## Open items

None blocking. Frame-level VISUAL QC LAW pass logged separately in `_qc/REPORT.md`
after the render.
