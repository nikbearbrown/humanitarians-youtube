# SOURCES — "Grounding and Retrieval"

## Primary source

**`grounding.py`** — authored for this video, shipped in this folder, runnable with no
dependencies and no API key.

Every figure the video puts on screen is printed by this file. Captured 2026-10-26:

```
$ python3 grounding.py
FOUR ANSWERS, EACH WITH A CITATION

claim                                      automatic check      actually true?
Expenses over $500 need manager approval.  CITATION_CHECKS_OUT  yes
Travel is reimbursed within 14 days.       CITATION_CHECKS_OUT  NO
Remote employees get a $2,000 stipend.     QUOTE_NOT_IN_SOURCE  NO
Contractors get the same stipend.          MISSING_SOURCE       NO

  citations that check out automatically : 2 of 4
  of those, claims that are still FALSE  : 1

  The check cannot catch this one:
    claim  Travel is reimbursed within 14 days.
    quote  Travel is reimbursed within 30 days of submission.
    both the source and the quote are real. The claim still is not.
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
