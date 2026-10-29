# SOURCES — CabStream — Week 3 Progress (Kavya)

## Primary source

`C:\Users\kavya\OneDrive\Desktop\CabStream` — the user's own repository.
Every claim traces to `git log --all --format="%ad %H:%M %s" --date=short`
run directly against that repo.

| Claim | Commit |
|---|---|
| Databricks cluster (auto-terminate) + Key Vault secret scope | `4e93378`, 2026-06-29 18:55 |
| fix: provider bootstrapping error | `89566e0`, 2026-06-29 19:19 |
| fix: prevent_destroy added to storage account/containers | `a99d715`, 2026-06-29 20:16 |
| Bronze ingestion (1.57B rows) + Silver processing (252.3M rows), per commit message | `df47dac`, 2026-06-29 22:44 |

Silent days in the week-3 window: 06-23 through 06-28.

## Content provenance for the B04 caveat

`databricks/01_bronze_ingestion.py` (committed in `df47dac`) read directly
to confirm: the script's first cell tests a single known-good month
(January 2023) against a stated local verified count of 3,066,766 rows
before looping over the full `range(2019, 2027)`. This is the only figure
in this reel independently confirmed from the committed code itself,
rather than taken from the commit message's own description.

## Generative media

None. Zero generative image/video model calls — every beat is a Remotion
scene composed from authored props.

## Brutalist toolkit version

- Repo HEAD at build time: `b21f6253a336098f3f55847a9525ae6868ccbdb7`
  (2026-10-10), branch `main`.
