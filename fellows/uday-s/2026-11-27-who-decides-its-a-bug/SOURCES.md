# SOURCES — Who Decides It's A Bug?

Commissioned topic: **"Implications/Advantages of using AI as a Beta Tester for
games and other kinds of software"**, retitled under the standing permission to
make the title professional and correct.

Three primary sources, each read directly. No figure comes from secondary
coverage, a vendor page, or a summary.

## Primary

| # | Source | Access | Used for |
|---|---|---|---|
| 1 | **OSS-Fuzz README** — `https://github.com/google/oss-fuzz`, "Trophies" section | fetched, quoted verbatim | B03 — the scale figures |
| 2 | **OSS-Fuzz documentation index** — `https://google.github.io/oss-fuzz/`, "Trophies" section | fetched, quoted verbatim | B07 — the disagreement with #1 |
| 3 | **OSS-Fuzz-Gen README** — `https://github.com/google/oss-fuzz-gen` | fetched, quoted verbatim | B04 — the LLM's role, the reported count, the grading metrics |
| 4 | **Meta, "Automated Unit Test Improvement using Large Language Models at Meta"** — arXiv:2402.09171, FSE 2024 industry track, read via the ar5iv HTML render | fetched, full body read in two passes | B05, B06, B07 |

### Exactly what each one states

**#1 OSS-Fuzz README**, verbatim:

> "As of May 2025, OSS-Fuzz has helped identify and fix over 13,000
> vulnerabilities and 50,000 bugs across [1,000] projects."

The reel uses these three figures **with the "as of May 2025" qualifier on
screen**, and uses the project's own verb — *helped identify and fix*, not
"found".

**#2 OSS-Fuzz documentation index**, verbatim:

> "As of August 2023, OSS-Fuzz has helped identify and fix over [10,000]
> vulnerabilities and [36,000] bugs across [1,000] projects."

Used only in B07, to show that two official pages of the same project carry
different totals under different dates.

**#3 OSS-Fuzz-Gen README**, verbatim:

> "So far, we have reported 30 new bugs/vulnerabilities found by automatically
> generated targets built by this framework:"

> "This framework generates fuzz targets for real-world C/C++/Java/Python
> projects with various Large Language Models (LLM) and benchmarks them via the
> OSS-Fuzz platform."

Its four stated evaluation metrics for a generated target are **compilability,
runtime crashes, runtime coverage, and runtime line-coverage diff** against the
existing human-written targets. B04 uses exactly these.

**#4 TestGen-LLM paper.** The quoted sentence in B05, from Section 2:

> "Without an automatable test oracle [7], TestGen-LLM cannot automatically
> determine whether a failing test has found a bug, or whether it merely
> contains an incorrect test assertion."

Figures used in B06 — abstract and Section 4: 75% built correctly, 57% passed
reliably, 25% increased coverage; 196 of 1,979 test classes improved; 73% of
test improvements accepted.

## Deliberately NOT used

- **The Google Security Blog post of 20 November 2024** on LLM-generated fuzz
  targets. Its figure of 26 new vulnerabilities, the "hundreds of thousands of
  hours" of prior fuzzing, the 272-project and 370,000-line coverage numbers,
  and the CVE-2024-9143 claim are **all absent from this reel**. The page
  returned only its chrome — header, title, date, archive menu, footer — with
  none of the article body, so none of it could be read at the source. House
  rule: a source that cannot be read does not appear on screen. B04 uses the
  OSS-Fuzz-Gen README's own "30 reported" instead.
- Any claim that the crash is the *sole* bug oracle in OSS-Fuzz-Gen. The README
  lists a "Target oracle" column with undefined values and never states how a
  bug is adjudicated, so the reel says only what the README says: the LLM
  generates targets, and targets are graded on compiling, crashing and coverage.
- Any named game, studio, engine or commercial testing product. None was tested
  and no claim is made about any.
- Any figure for how many human beta testers a tool replaces. No source.

## Recorded caveats attached to the sources

- The OSS-Fuzz-Gen repository was **archived on 10 November 2026** and its
  README states "This repository is no longer being maintained."
- Of its 30 reported bugs, **2 rows are marked "(pending maintainer triage)"**,
  so "reported" is not the same as "confirmed".
- The project/coverage figures in that README come from a sample experiment
  dated **2024-01-31**.

All three are in FACTCHECK.md; the first two shape how B04 is worded.
