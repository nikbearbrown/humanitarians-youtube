# FRICTIONAL — Trust, Then Verify

The frictional log for this piece of work: short, dated, honest entries about what was
tried, where it resisted, what was done about it and what was learned — appended as the
work goes, never rewritten. <https://www.humanitarians.ai/fellows#frictional-logs>.

## 2026-10-29 — Build, QC and fixes

> Drafted with Claude on 2026-11-02 from this folder's beat sheet, QC report and the
> series build log, which were kept during the build.

**Working on.** Decide which claims in a script need a source before the final cut, and who signs for them. Research and scripting ran Weeks 7–8; the film was
narrated, rendered and checked on 2026-10-29.

**Tried, and expected.** Show GATE F as a design choice: the final cut refuses to compile until a person has signed a fact-check. I expected this to be the simplest film, since its example was the very first failure of the series.

**Where it resisted, and what I did next.**

- B01 underfilled at its midpoint and the correction landed late — same fix as films 2 and 3.
- The fact-check card was labelled PYTHON.
- Its own fact-check is still a draft. The film argues for signing before the final cut, so it ships as a review cut until I sign.

**What Claude contributed — accepted, changed, rejected.**

- Claude drafted every film's fact-check and deliberately named it `FACTCHECK-DRAFT.md`, so the gate cannot be satisfied without me.
- Accepted: compiling review cuts with `ART_FACTS=0` rather than writing a file that would let `./art final` through.

**Understand now / still don't.**

- Now: A gate that a machine can satisfy on its own is not a human sign-off.
- Still open: Sign the six fact-checks — the open item this film is literally about.

**Evidence:** [`QC-REPORT.md`](./QC-REPORT.md) · [`FACTCHECK-DRAFT.md`](./FACTCHECK-DRAFT.md) · [`beat_sheet.json`](./beat_sheet.json)
