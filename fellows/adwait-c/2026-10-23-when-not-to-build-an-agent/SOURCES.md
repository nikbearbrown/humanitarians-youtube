# SOURCES — "When Not to Build an Agent"

## Primary source

**`decide.py`** — authored for this video, shipped in this folder, runnable with no
dependencies and no API key.

Every figure the video puts on screen is printed by this file. Captured 2026-10-26:

```
$ python3 decide.py
task                                   verdict  missing
Reformat a folder of CSVs              AGENT    -
Draft a reply for me to send           NOT YET  doing
Triage and close support tickets       NOT YET  undoable, checkable
Research and summarise a topic         NOT YET  doing, checkable
Run the test suite and fix failures    AGENT    -
Email the quarterly numbers to board   NOT YET  undoable

2 of 6 pass all three.

WHICH CONDITION FAILS MOST OFTEN?
  doing      fails 2 of 6
  undoable   fails 2 of 6
  checkable  fails 2 of 6
```

The beats were built from this output rather than transcribed from it, and the code beat
shows the shipped function verbatim, so the screen cannot drift from the file.

## Nothing else is cited, deliberately

No model, vendor, product, benchmark or price is named. See `FACTCHECK.md` for the
claim-by-claim audit, including which lines are arithmetic and which are the author's
judgement.

## Toolkit provenance

- Built with `brutalist.art`, skill `ai-explainer`.
- Voice: Kokoro `am_onyx` ("Onyx"), generated locally. Cost: $0.00.
- 16:9 master and 9:16 derivative cut both rendered from the same beat sheet.
