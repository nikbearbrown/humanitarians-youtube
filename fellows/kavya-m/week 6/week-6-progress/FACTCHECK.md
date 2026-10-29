# FACTCHECK — CabStream — Week 3 Progress (Kavya)

Every claim mapped to its evidence, with an honest status on each.

## What kind of reel this is

A real progress recap of `C:\Users\kavya\OneDrive\Desktop\CabStream`,
grounded in that repo's actual git log. This reel covers **week 3 only**
(commits 2026-06-23 through 2026-06-29) — third in the series, and the
week where the scale verification that weeks 1 and 2 both flagged as
"not yet here" finally lands.

## B00 — Cold open

- **"Databricks cluster stood up, Key Vault secret scope added"** — real,
  commit `4e93378`, 2026-06-29 18:55.
- **"2 real infra bugs fixed the same night"** — real, see B03/B04.
- **"Bronze + Silver ingestion ran — described as 1.57B + 252.3M rows"**
  — this is explicitly framed as what the commit *describes*, not an
  independently verified measurement — see the caveat below.

## B01 — BLUF

- Restates B00's framing; no new claim.

## B02 — What happened

- **Databricks cluster added, auto-terminate + Key Vault secret scope** —
  real, `4e93378`.
- **Two real bugs fixed** — real, see B03.
- **Bronze ingestion ran — NYC taxi data, 2019 to 2026, resume-safe** —
  real; `databricks/01_bronze_ingestion.py` (committed in `df47dac`)
  literally implements a resume-safe ingestion loop over `YEARS =
  range(2019, 2027)`.
- **Silver processing ran, described as 252.3M rows** — same commit
  message framing as the Bronze figure; see caveat below.

## B03 — The real log

- **18:55: Databricks cluster + Key Vault secret scope** — real, `4e93378`.
- **19:19: fix — provider bootstrapping error** — real, `89566e0`,
  "fix(infra): remove dynamic data sources causing provider bootstrapping
  error."
- **20:16: fix — prevent_destroy added to storage** — real, `a99d715`.
  `storage.tf`'s own new comment explains why: "Bronze/Silver/Gold Delta
  tables are written once, read forever... Storage must survive terraform
  destroy between sessions."
- **22:44: Bronze + Silver ingestion land** — real, `df47dac`.
- All four timestamps confirmed via `git log --all --format="%ad %H:%M
  %s"` against the CabStream repo.

## B04 — The honest caveat (this reel's central honesty check)

- **"1.57 billion rows is what my commit message says, not a number I
  re-ran and watched land myself"** — accurate and important: this reel
  (built by Claude, directed by Kavya) did not execute the Databricks
  notebook. The 1.57B/252.3M figures come entirely from Kavya's own commit
  message text (`df47dac`: "add Bronze ingestion (1.57B rows) and Silver
  yellow taxi processing (252.3M rows)"), not from a run log, a
  `.verified.json` receipt, or any artifact this reel inspected.
- **"The ingestion script tests one known month first, January 2023,
  against a locally verified count, before it ever scales up"** — real and
  directly verifiable: `databricks/01_bronze_ingestion.py`'s own first
  code cell reads "Test with Jan 2023 — known good, matches local verified
  count of 3,066,766" before the loop over all years/months.
- **"The discipline is visible. The total isn't independently checked
  here."** — this is the reel's own falsifiability statement, matching the
  series' established honesty pattern (week 1's "shape vs. scale", week
  2's "defined vs. deployed").

## B05 — Verdict

- Restates B02/B03/B04's claims; no new facts introduced.

## B06 — Handoff

- No factual claim; a prompt for the viewer to apply the same scrutiny to
  their own commit-message claims.

## B07 — Outro

- No factual claim; "Built by — Kavya Mehta" credit card.

## Corrections & caveats applied during this build

- This is the first CabStream reel in the series built with the correct
  compile resolution (`--height 2160`/`--height 3840`) from the start —
  see BUILD-LOG.md for why that mattered.
- GATE T: PASS, 8/8, on first run.
