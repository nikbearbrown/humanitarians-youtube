# CHECKS-REPORT — claude-cli-rag-pipeline

*Written before the first compile, per the cli-explainer PROOF GATE.*
*"Watch A Bug Name Its Own Stage." · RAG Foundations, Chapter 7.*

---

## Beat classification

**12 SHOW / 0 justified-HOLD / 0 PUNT-flagged**

| Beat | Spine role | Class | On-screen artifact |
|---|---|---|---|
| B00 | INTRO | SHOW | Composer types the ask; three output lines land |
| B01 | PROBLEM | SHOW | Headline + subline: one symptom, four suspects |
| B02 | CLI | SHOW | The prompt for the five-stage pipeline |
| B03 | CODE | SHOW | `pipeline.py` — the five function signatures as a chain |
| B04 | OUTPUT | SHOW | Five stage boxes lighting in order with measured artifacts; answer strip |
| B05 | CLI (revision) | SHOW | The fault-injection prompt — one stage at a time, three signals |
| B06 | CODE (revision) | SHOW | `diagnose.py` — `retrieve_wrong` and `trace` |
| B07 | OUTPUT (revision) | SHOW | 4×4 fault/signal table resolving row by row, verdict beneath |
| B08 | OUTPUT | SHOW | The four returned answers as a transcript |
| B09 | SUMMARY | SHOW | Headline + subline resolve |
| B10 | NEXT STEPS | SHOW | Composer with the viewer's prompt typed in |
| B11 | OUTRO | SHOW | Title restate, handle, author signature |

**Every OUTPUT beat is motion, never a still:** B04 lights five stages in
sequence then lands the answer, B07 resolves four rows then the verdict, B08 is
a staggered transcript. No output slot is static or slated.

## The mandatory CLI spine

| Requirement | Status |
|---|---|
| INTRO on the interface, ask shown answered (COLD OPEN LAW) | ✓ B00 |
| PROBLEM beat after intro, before the CLI loop | ✓ B01 — stakes stated, no prompt yet |
| Cycle 1: CLI → CODE → OUTPUT | ✓ B02 → B03 → B04 |
| **≥1 revision cycle (THE REVISION LAW)** | ✓ B05 → B06 → B07 (+B08, a second output from the same run) |
| SUMMARY | ✓ B09 |
| NEXT STEPS (HANDOFF LAW) | ✓ B10 — read aloud verbatim, then discussed |
| OUTRO, title restate, last beat | ✓ B11 |

## Legibility contract (every SHOW claim beat)

- [x] Names its on-screen artifact in `shot.show` / `shot.visual_intent`
- [x] ~15–35% negative space — figures sit at ≤98% of the figure width inside `FigureFrame`'s reserved bands
- [x] Un-highlighted elements never below ~40% opacity — the healthy control row renders at 0.72 opacity, still well above the floor, and is the only dimmed element
- [x] Comparisons shown side-by-side and held — B07's four rows and B08's four answers all persist to the end of their beats

## Teaching arc

```
FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

- **FRAMEWORK before examples ✓** — B00/B01 establish the five stages and why
  their separation matters before any code exists.
- **WORKED EXAMPLE ✓** — the chapter's own question ("How many vacation days do
  I get in my first year?") traced stage by stage, executed rather than
  described.
- **FALSIFIABILITY ✓** — this reel's structure *is* a falsification test. B05
  states the condition out loud before the result: if any two faults produce the
  same signature, the pipeline is not a diagnostic map. B07 then reports the
  measured signatures. The claim could have failed and the reel would have said
  so.
- **SCAFFOLDED TASK ✓** — B10 asks the viewer to log three signals per answer on
  their own system and surface the rows where those signals disagree.
- **BOUNDS/BOOKENDS ✓** — intro → problem → build → summary → handoff → outro.
  Typing appears only in composer beats (B00, B02, B05, B10).
- **NO-SOURCE-NO-VERDICT ✓** — every on-screen number is captured stdout
  (`_run-pipeline.txt`, `_run-diagnose.txt`); every conceptual claim traces to
  the chapter or a source it cites. See SOURCES.md.

## Law checks

| Law | Status |
|---|---|
| ACTUAL-CODE LAW | ✓ Both CODE beats quote `code/*.py` verbatim; the scripts run; output beats are their real stdout |
| Generator honesty | ✓ The generate stage is NOT an LLM, and the reel says so in the code beat, in B09's narration, and in the docstring. Declared as a control, with its limitation named |
| Retrieval is REAL | ✓ Genuine `all-MiniLM-L6-v2` weights via the carried-over `encoder.py` |
| REVISION LAW | ✓ One full revision cycle in the 16:9 cut |
| SPARK-LINE LAW | ✓ B02 `"The ask,"`, B05 `"The change,"`, B10 `"Your turn."`; B00 carries the hello |
| ASK → RESULT LAW | ✓ Every composer beat is followed by what it produced |
| REBUILD LAW | ✓ Fig. 01 rebuilt as B04 with measured artifacts. No source image embedded |
| DOODLE-BANNED LAW | ✓ No `DoodleScene` / `DoodleChart` |
| HANDOFF LAW | ✓ Interesting prompt, read verbatim, then discussed |
| OUTRO LAW | ✓ Exact title restate; `TitleOutroChannel` per OUTRO-LOCK.md §Scope |
| GATE L | ✓ Four searches before authoring; closest lead read and rejected (hardcoded stage list, `sparkLine` only); two components built, registered both aspects, indexed |
| Free by default | ✓ Kokoro `am_onyx` + local numpy/model cache. **$0.00**. No paid API, no network call |
| NARRATION BUDGET | ✓ Body beats 50–70 words. Bookends exempt |

## Rhythm

No two consecutive beats share a visual scheme:

```
B00 composer · B01 summary card · B02 composer · B03 code · B04 pipeline rail
B05 composer · B06 code · B07 fault table · B08 transcript · B09 summary card
B10 composer · B11 title
```

## Open items

None blocking. Frame-level VISUAL QC LAW pass logged separately in
`_qc/REPORT.md` after the render.
