# SOURCES — "Guardrails and Evals"

## Primary source

**`evals.py`** — authored for this video, shipped in this folder, runnable with no
dependencies and no API key.

Every figure the video puts on screen is printed by this file. Captured 2026-10-26:

```
$ python3 evals.py
WHAT REVIEWING EVERY RUN COSTS
 runs/day   human hours/day
       10               0.2
      100               2.5
     1000              25.0
    10000             250.0

SAMPLING 5% OF A 2% FAILURE RATE
 runs/day   failures   reviewed   unseen
      100          2        0.1      1.9
     1000         20        1.0     19.0
    10000        200       10.0    190.0

DOES A BIGGER SAMPLE FIX IT?  (1000 runs/day, 2% failing)
  sample   5%  ->   19.0 failures unseen,    1.2 human hours/day
  sample  25%  ->   15.0 failures unseen,    6.2 human hours/day
  sample  50%  ->   10.0 failures unseen,   12.5 human hours/day
  sample 100%  ->    0.0 failures unseen,   25.0 human hours/day
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
