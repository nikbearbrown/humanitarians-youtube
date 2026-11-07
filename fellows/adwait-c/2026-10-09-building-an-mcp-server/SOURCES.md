# SOURCES — "Building a Tool Server"

## Primary source

**`server.py`** — authored for this video, shipped in this folder, runnable with no
dependencies and no API key.

Every figure the video puts on screen is printed by this file. Captured 2026-10-26:

```
$ python3 server.py
1. CLIENT CONNECTS AND ASKS WHAT EXISTS
   column_names  List the column headers of a CSV file, in order.
   row_count     Count data rows in a CSV file, excluding the header.

2. CLIENT ASKS FOR ONE CONTRACT IN FULL
{
  "name": "row_count",
  "description": "Count data rows in a CSV file, excluding the header.\n\nUse this when you need the size of a file. Do NOT use it to read values.",
  "input_schema": {
    "type": "object",
    "properties": {
      "path": {
        "type": "string"
      }
    },
    "required": [
      "path"
    ]
  }
}

3. CLIENT CALLS IT
   row_count(path='sales.csv')  ->  3

4. CLIENT CALLS SOMETHING THAT DOES NOT EXIST
   'no such tool: delete_everything'
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
