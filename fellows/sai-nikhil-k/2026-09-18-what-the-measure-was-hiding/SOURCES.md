# SOURCES — What the Measure Was Hiding

Reel: `weekly_updates/09-18-2/` · slug `claude-sai-what-the-measure-was-hiding`
Week of 2026-09-18. Subject: **Prot2Vec**, v0.2.0 and v0.3.0.

## Raw-material provenance

The author (Sai) supplied the repository in place of dictated bullets and
explicitly authorised **the repository's own prose** — `README.md`,
`CHANGELOG.md` (0.2.0 and 0.3.0) and the commit subjects — as this week's raw
material. This mirrors the arrangement used for `09-11-2`.

Nothing in this reel was inferred from a diff alone. Every narrative claim
traces to one of those documents, or to a line of source read by hand, or to a
computation recorded in `evidence/`.

## External sources

| Source | Used for |
|---|---|
| `https://github.com/nikhil-kunapareddy/Prot2Vec` | The subject. Cloned at `2e38c9e` (merge of v0.3.0 into main). |
| `README.md` | B01's method list; the framing in B00 and B03; the `quick.yaml` run parameters (n=90, k=10) used in B02. |
| `CHANGELOG.md` §0.3.0 | B02 (confound group, LCMC), B04 (the coverage fix), B05 (per-pair failure isolation), B06. |
| `CHANGELOG.md` §0.2.0 | B06's first line: packaging, FASTA input, run manifest, chance baseline. |
| `src/prot2vec/evaluation/projection.py` | B02's algebra, read directly rather than taken from the changelog. |
| `src/prot2vec/evaluation/suite.py` | The 31-metric count, counted key by key. |
| `pyproject.toml` @ `405b00e` / `40ff686` | The before/after `exclude_lines` patterns quoted in B04. |
| coverage.py 7.8.2 | The measurement instrument in `evidence/coverage_exclusion.py`. |

## Week scope

Four commits, all dated 2026-09-16:

| Commit | Subject |
|---|---|
| `405b00e` | Rework into a distributable package: prot2vec, v0.2.0 |
| `40ff686` | Expand method coverage: 9 embedders, 13 reducers, 31 metrics, v0.3.0 |
| `1ec32de` | Fix CI: unpin mypy python_version, drop an ill-posed test, pin LLM dtype |
| `a114485` | Bump CI actions to v7 to clear the Node 20 deprecation |

`2e38c9e` merged the result into `main` via PR #1.

## Honesty log

- **No performance claim appears anywhere.** No runtime, no memory figure, no
  speedup against v0.2.0, no accuracy achieved by any embedder on any real
  dataset. None was supplied and none was measured.
- **No adoption figures.** No stars, downloads, installs or users.
- **The "84% coverage" figure from the changelog is deliberately NOT on screen.**
  Unlike the other counts it could not be reproduced without executing the full
  test suite, which needs the optional deep-learning extras. It is omitted
  rather than repeated on trust. See FACTCHECK.md.
- **The 117-pair figure is not on screen either.** 9 × 13 is arithmetic, but not
  every pair is valid — which is B05's entire subject — so B05 says "a full
  matrix" and "at this width" instead of naming a count that overstates it.
- **B03's two tracks are a constructed contrast**, not a recorded experiment on
  real families. They name the checks the confound group actually computes; they
  do not claim a specific family pair was caught this way.
- **The example numbers in B02 are labelled as what they are**: 0.1124 is the
  chance floor for the README's own quick-start shape (n=90, k=10), and the
  ±0.011 figure comes from 40 seeded random trials recorded in
  `evidence/lcmc_chance.out` — not from a protein benchmark.

## Attribution

Prot2Vec is the author's own project, so no third-party contributor is named in
narration or on screen. The reel names the project, never a person other than
the host.
