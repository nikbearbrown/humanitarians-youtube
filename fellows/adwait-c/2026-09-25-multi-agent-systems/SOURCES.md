# SOURCES — "Multi-Agent Systems"

## Primary source

**`agents.py`** — authored for this video, shipped in this folder, runnable with no
dependencies and no API key.

Every figure the video puts on screen is printed by this file. Captured 2026-10-26:

```
$ python3 agents.py
COORDINATION LINKS
 agents   supervisor   mesh
      1            0      0
      2            2      1
      3            4      3
      5            8     10
      8           14     28

EVERY STEP MUST SUCCEED  (95% each)
 agents   end to end   failures/100 runs
      1       95.0%                   5
      2       90.2%                  10
      3       85.7%                  14
      5       77.4%                  23
      8       66.3%                  34

HOW GOOD MUST EACH AGENT BE FOR 95% END TO END?
  2 agents  ->  each must be 97.47%
  3 agents  ->  each must be 98.30%
  5 agents  ->  each must be 98.98%
  8 agents  ->  each must be 99.36%
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
