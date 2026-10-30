# SOURCES — "What Is MCP?"

## Primary source

**`integrations.py`** — authored for this video, shipped in this folder, runnable with no
dependencies and no API key.

Every figure the video puts on screen is printed by this file. Captured 2026-10-26:

```
$ python3 integrations.py
CONNECTORS TO BUILD
 apps  tools   direct   protocol
    2      3        6          5
    3      5       15          8
    5     10       50         15
   10     20      200         30

ADDING ONE MORE TOOL
 existing apps   direct   protocol
             3        3          1
             5        5          1
            10       10          1
            50       50          1

WHERE THE PROTOCOL LOSES
  1 app(s), 1 tool(s):  direct 1, protocol 2  ->  DIRECT wins
  1 app(s), 3 tool(s):  direct 3, protocol 4  ->  DIRECT wins
  2 app(s), 2 tool(s):  direct 4, protocol 4  ->  tie
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
