# Frictional log — Step 2: Ingest declared inputs

**Date:** 2026-09-03 · **Script:** `scripts/ingest/market-sentiment-analysis-part-1-ingest-inputs.py` · **Recipe:** `recipes/market-sentiment-analysis-part-1.md`

> A frictional log is a short, dated, honest record of what was tried, where the work
> resisted, what was done about it, and what was learned. It lives beside the evidence
> it describes.

## What was tried

Move the declared source payloads into the raw layer so the validation steps have something to read.

## Where the work resisted

- The pull to be helpful. The defective news envelope declares 7 records while holding 8, and the obvious instinct is to recount and write the right number.
- One source file does not parse at all. Skipping it is the natural thing to do, and reads as robustness.

## What was done about it

- Made the step transport-only: no recount, no dedupe, no dropped rows, no coercion. The declared 7 is preserved verbatim alongside the payload.
- Copied the unparseable file through byte-for-byte and recorded a reject, instead of skipping it or raising, so the next step can attempt the parse itself.

## What was learned

An ingest step that cleans data destroys the evidence that cleaning was needed. Both of these defects only survive to be caught later because this step refused to help.

Restraint is a feature here, and it needed to be written down — the code looks under-built until you know why.
