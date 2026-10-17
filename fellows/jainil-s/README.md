# Jainil S.

**Role:** Data Analytics Engineer  
**Project:** _to be filled in_  
**GitHub:** [@jainil112](https://github.com/jainil112)

## What's in this folder

Each piece of work gets its own dated, lowercase-kebab subfolder —
`YYYY-MM-DD-short-slug/` — holding its `beat_sheet.json`, README, sources and
build assets.

| Folder | Track | Thesis |
|---|---|---|
| [`2026-09-18-ai-accuracy-is-lying-to-you`](2026-09-18-ai-accuracy-is-lying-to-you) | educational (STEM / AI) | A 95%-accurate model on a rare event can be worthless — accuracy rewards the majority answer |
| [`2026-09-18-dae-the-numbers-arent-final-yet`](2026-09-18-dae-the-numbers-arent-final-yet) | independent research (data analytics engineering) | A metric is a draft that keeps being revised; comparing a fresh number to a settled one measures the settling, not performance |
| [`2026-09-25-ai-why-it-cant-count-letters`](2026-09-25-ai-why-it-cant-count-letters) | educational (STEM / AI) | It cannot count the letters in a word because it never receives letters — text is split into tokens first |
| [`2026-09-25-dae-your-test-set-saw-the-future`](2026-09-25-dae-your-test-set-saw-the-future) | independent research (ML evaluation) | A random split on time-ordered data trains on the future and tests on the past — silently |
| [`2026-10-02-ai-lost-in-the-middle`](2026-10-02-ai-lost-in-the-middle) | educational (STEM / AI) | Where a fact sits in a long context changes how reliably it is used — the middle is the weakest position |
| [`2026-10-02-dae-your-feature-importance-is-lying`](2026-10-02-dae-your-feature-importance-is-lying) | independent research (ML interpretability) | Importance measures what a model would miss, not what matters — duplicate a signal and you hide it |
| [`2026-10-09-ai-only-half-the-curve`](2026-10-09-ai-only-half-the-curve) | educational (STEM / AI) | The overfitting curve you were taught is the left half — past the interpolation threshold, test error spikes and then falls below the classical best |
| [`2026-10-16-ai-the-tails-go-first`](2026-10-16-ai-the-tails-go-first) | educational (STEM / AI) | Train a model on its own output and the average stays fine while the rare cases vanish — permanently |
| [`2026-10-16-ai-same-prompt-different-answer`](2026-10-16-ai-same-prompt-different-answer) | educational (STEM / AI) | The model draws rather than picks; temperature reshapes the distribution, and even temperature 0 is only as stable as the arithmetic |

**Video files are not in this repo.** They are delivered separately. Everything
here is the record of how they were built and why each claim in them holds.

Each work subfolder contains:

- `beat_sheet.json` — the master cut (16:9). Source of truth: narration,
  scenes, props and measured durations.
- `beat_sheet.short.json` — the derived 9:16 cut.
- `README.md` — what the video argues, its beats, and how to reproduce it.
- `SCRIPT.md` — narration as delivered.
- `FACTCHECK.md` · `SOURCES.md` — every claim with its verdict and source,
  including what was deliberately cut as unsourceable.
- `SHOTLIST.md` · `PROMPTS.md` — the typed work order.
- `INTAKE.md` — weekly-work folders only: the assignment and what was
  actually done that week, recorded before the video was authored. It is
  the primary source the factcheck rows point at.
- `STATUS.md` · `ToDo.md` — build ledger.
- `qc/` — GATE V reports plus frame evidence from the finished files.

Shared documents are stored **once** per piece of work rather than duplicated
per cut. Only the beat sheet and the QC artifacts differ between a master and
its Short.

### Conventions

- Every factual claim traces to a row in `FACTCHECK.md`. A claim that cannot be
  sourced is cut, not softened into something vaguer.
- A Short is a derived cut, never a centre-crop — beats are re-laid-out through
  dedicated portrait compositions.
- Audio is generated first and its measured durations are the master clock;
  visuals conform to the audio, never the reverse.

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.
