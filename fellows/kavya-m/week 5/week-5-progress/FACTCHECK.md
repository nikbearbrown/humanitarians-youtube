# FACTCHECK — CabStream — Week 2 Progress (Kavya)

Every claim mapped to its evidence, with an honest status on each.

## What kind of reel this is

A real progress recap of `C:\Users\kavya\OneDrive\Desktop\CabStream`,
grounded in that repo's actual git log. This reel covers **week 2 only**
(commits 2026-06-16 through 2026-06-22) — a direct sequel to
`kavya-cabstream-week1-progress`.

## B00 — Cold open

- **"6 Terraform files added: Event Hubs, Databricks, Storage, Key Vault"**
  — real, commit `56c17b9` (2026-06-19 18:38): `databricks.tf`,
  `eventhubs.tf`, `main.tf`, `outputs.tf`, `storage.tf`, `variables.tf`,
  262 insertions.
- **"managed Kafka defined to replace the local Docker setup"** — real;
  `eventhubs.tf`'s own header comment states this explicitly ("Azure Event
  Hubs — managed Kafka on Azure... Zero infrastructure: no Docker").
- **"1 access-policy gap found and closed, the next day"** — real, commit
  `7d1eef4` (2026-06-20 12:12): "fix(infra): add personal user read access
  policy to Key Vault."

## B01 — BLUF

- No new factual claim beyond B00/B02.

## B02 — What happened

- **Event Hubs defined** — real, `56c17b9`.
- **Databricks workspace defined** — real, `56c17b9`, `databricks.tf`.
- **Storage + Key Vault added** — real; `storage.tf` same commit,
  `keyvault.tf` added in `7d1eef4` the next day.
- **Access gap closed, next day** — real, `7d1eef4`.

## B03 — The real log

- **06-19 18:38: Terraform config — Event Hubs, Databricks, Storage, Key
  Vault** — real, `56c17b9`.
- **06-19 23:00: main.tf + variables.tf expanded** — real, `d3e8959`
  (+23 lines).
- **06-20 12:12: fix — personal read-only access added to Key Vault** —
  real, `7d1eef4`.
- All timestamps confirmed via `git log --all --format="%ad %H:%M %s"`
  against the CabStream repo.

## B04 — The honest caveat

- **"No confirmed terraform apply — plan committed, not run"** — defensible:
  this window's git log contains only `.tf` file commits; there is no
  commit evidence (state file, deployment log, or application-code change)
  that `terraform apply` was executed or that any Azure resource is
  actually live. State/tfvars files are explicitly gitignored (`6436b64`),
  so this reel cannot and does not claim to verify deployment status from
  the commit history alone.
- **"Pipeline still reads local Docker Kafka, not Event Hubs"** — defensible:
  no producer/application code changed in this date window; only
  `terraform/*.tf` files were touched.
- **"The plan exists. It hasn't been run yet."** — an honest scope
  statement, not an overclaim.

## B05 — Verdict

- Restates B02/B03/B04's claims; no new facts introduced.

## B06 — Handoff

- No factual claim; a prompt for the viewer to audit their own
  infrastructure-as-code claims the same way.

## B07 — Outro

- No factual claim; "Built by — Kavya Mehta" credit card.

## Corrections & caveats applied during this build

- The "defined vs. deployed" distinction in B04/B05 is the reel's central
  honesty check, directly modeled on week 1's "shape vs. scale" caveat —
  consistent register across the series.
- GATE T: PASS, 8/8, on first run. The `ClaudeScienceLayerStack` false
  positive that affected the three Brutalist week reels and
  `kavya-cabstream-week1-progress` was already fixed at the root
  (`type_check.py`'s `HAND_DRAWN_PATTERNS` allowlist) before this reel was
  built, so no new occurrence or workaround was needed here.
