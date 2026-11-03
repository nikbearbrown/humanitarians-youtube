# FRICTIONAL — The Workflow Is the Lesson

The frictional log for this piece of work: short, dated, honest entries about what was
tried, where it resisted, what was done about it and what was learned — appended as the
work goes, never rewritten. <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-10-30 — Build, QC and fixes

> Drafted with Claude on 2026-11-02 from this folder's beat sheet, QC report and the
> series build log, which were kept during the build.

**Working on.** Map an AI-assisted workflow as steps and mark which the machine runs and where a person must check. Research and scripting ran Weeks 11–12; the film was
narrated, rendered and checked on 2026-10-30.

**Tried, and expected.** Show the loop itself — author → audio → render → check → sign — and which steps the machine runs versus where a person stands. The worked example is the real generator script that wrote films 2–6.

**Where it resisted, and what I did next.**

- B01 ran 8.7 s, under the skill's 9 s minimum, and GATE V passed it. Added "The machine runs the steps. You stand at the checks." and regenerated B01 (12.0 s).
- The docstring on the code card had to be trimmed and re-wrapped to fit; logged as such in the fact-check.

**What Claude contributed — accepted, changed, rejected.**

- Claude wrote `build_films.py` and `build_films_5_6.py`; I chose the film order and the topics.
- Accepted: keeping post-render QC patches in the script's `__main__` so a rerun doesn't silently undo them.

**Understand now / still don't.**

- Now: Rounds of fixes fell 4 → 3 → 2 → 2 across films once the generator held the lessons. The workflow got better, not just the films.
- Still open: Re-running `build_films.py` still overwrites post-render patches for films 2–4.

**Evidence:** [`QC-REPORT.md`](./QC-REPORT.md) · [`FACTCHECK-DRAFT.md`](./FACTCHECK-DRAFT.md) · [`beat_sheet.json`](./beat_sheet.json)
