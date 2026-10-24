# Work report — Week 1 — How Pi Works and Where Memory Could Fit

**Fellow:** Maitri P. · **Period:** Week 1 (Sep 21 – Sep 27, 2026) · **Track:** Weekly update (catch-up report)

## Hours

| Category | Hours | What it covered |
|---|---:|---|
| Progress / workflow | 15 | Onboarding, company policies, installing arkenOS, studying the Pi agent loop |
| Brutalist videos | 4 | Beat sheet and render of this catch-up video (produced 2026-10-23) |
| Meetings | 0 | — |
| Documentation | 1 | Notes on Pi's request → model → tool → output cycle |
| **Total** | **20** | |

> Hours are **reconstructed estimates** made on 2026-10-23 from my recollection and the dated work in this folder; contemporaneous time logs were not kept for this week. They are not Git-derived or independently verified.

## What I did

- Completed onboarding and read the company policies.
- Installed arkenOS and set up the Brutalist toolkit locally.
- Chose the Pi agent harness for the assigned memory-types research.
- Traced how Pi sends a request with instructions and tools, executes requested tool calls, and returns real output or errors to the model.

## How I approached it

Understand the system before changing it: I studied the existing loop end to end so that any memory added later would sit at a clear point in that loop.

## Outcome

Identified the key distinction for the project: seeing an error within one run is not the same as remembering a lesson for a later run. No measurements were taken in week 1.

## Evidence

- [Project README and videos](README.md#watch-and-review)
- [Frictional log](FRICTIONAL.md)
- [Fact-check](FACTCHECK.md)
- Beat sheets: [landscape](beat_sheet.json) · [portrait](vertical/beat_sheet.json)

## Next

Run Pi on small tasks and inspect its tool calls, errors and results.
