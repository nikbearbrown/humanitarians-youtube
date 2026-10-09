# Frictional logs — market-sentiment pipeline

A frictional log is a short, dated, honest record of what was tried, where the
work resisted, what was done about it, and what was learned. It lives beside the
evidence it describes.

These cover the six steps of `market-sentiment-analysis-part-1` in
`nikbearbrown/mycroft`, written as each step was built.

| Date | Step | Merged in |
|---|---|---|
| 2026-08-27 | [Step 1 — verify provenance](./2026-08-27-step-1-verify-provenance.md) | [mycroft #23](https://github.com/nikbearbrown/mycroft/pull/23) |
| 2026-09-03 | [Step 2 — ingest declared inputs](./2026-09-03-step-2-ingest-declared-inputs.md) | [mycroft #37](https://github.com/nikbearbrown/mycroft/pull/37) |
| 2026-09-03 | [Step 3 — validate data shape](./2026-09-03-step-3-validate-data-shape.md) | [mycroft #37](https://github.com/nikbearbrown/mycroft/pull/37) |
| 2026-09-10 | [Step 4 — transform and quality check](./2026-09-10-step-4-transform-and-quality-check.md) | [mycroft #40](https://github.com/nikbearbrown/mycroft/pull/40) |
| 2026-09-10 | [Step 5 — run approved tools](./2026-09-10-step-5-run-approved-tools.md) | [mycroft #40](https://github.com/nikbearbrown/mycroft/pull/40) |
| 2026-09-17 | [Step 6 — produce human report](./2026-09-17-step-6-produce-human-report.md) | [mycroft #48](https://github.com/nikbearbrown/mycroft/pull/48) |
| 2026-09-25 | [Recipe promotion to RUNNABLE-SAMPLE, and the gate fixes](./2026-09-25-recipe-promotion-and-gate-fixes.md) | not yet merged upstream |
| 2026-10-02 | [Closing the DEFINE and APPROVE TODOs](./2026-10-02-closing-the-two-todos.md) | `8c13b87`, on the feature branch |
| 2026-10-09 | [Unhiding the step scripts from conformance](./2026-10-09-conformance-skip-list.md) | `fbd30b6`, on `fix/conformance-skip-list` |
| 2026-10-09 | [`.gitattributes` and manifest drift](./2026-10-09-gitattributes-and-manifest-drift.md) | same branch |

## Where the video work's logs are

The eight videos in this folder each carry their own equivalent record as
`BUILD-LOG.md`, inside that video's folder — what was attempted, which quality
gates failed and why, what was corrected, and what carried forward to the next
build.

## Relationship to `RUN_LOG.md`

These are deliberately not the RUN_LOG. The RUN_LOG is the durable record of
what a run *did* — the evidence chain an auditor follows. These record what it
cost to get there: dead ends, wrong diagnoses, tooling that mangled a file,
checks that reported green while not running at all.
