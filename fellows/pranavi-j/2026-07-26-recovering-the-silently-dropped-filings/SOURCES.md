# SOURCES — The Pipeline That Was Lying to Me

Primary source for every measured claim in `beat_sheet.json`:

- `/Users/pranavijs/mycroft/scripts/regulatory-intel/FINDINGS.md` (dated 2026-07-24)
  — "Regulatory Intelligence — Hardening Verification & Output Findings."
  Method: the `Normalize Data` and `Keyword Analysis` code nodes from
  `workflow.dev.json` were extracted and run against the 5 live RSS feeds;
  the parameterized insert was exercised against the local `mycroft_intelligence`
  DB (`localhost:5431`) in a rolled-back transaction. Aggregate counts were
  cross-checked against the authoritative n8n-produced rows in `regulatory_feeds`.
- `/Users/pranavijs/mycroft/scripts/regulatory-intel/workflow.dev.json` — the
  hardened n8n workflow copy itself (original left untouched/quarantined).

## Claim → source mapping

| Number / claim | Value used in video | FINDINGS.md line |
|---|---|---|
| Old vs. new pass count | 297 → 370 (+73 recovered) | line 19, row "B1 recover empty-content" |
| Recovered item examples | Cboe Clear U.S., MEMX LLC, Nasdaq GEMX SRO notices, US v. Edwards LifeSciences (DOJ antitrust) | line 24 |
| Parameterized insert stress test | 370 items, 46 new / 324 dedup-skip / 0 errors | line 14, row "A2 parameterized insert" |

## Citation status (open)

- The four recovered-item names (Cboe Clear U.S., MEMX LLC, Nasdaq GEMX,
  US v. Edwards LifeSciences) are named in FINDINGS.md as representative
  examples but **no exact filing URL/citation is recorded there**. This
  toolkit never publishes, so this is not a blocking gate — but if this reel
  is ever shown outside the fellows program, pull the exact filing links
  from the `regulatory_feeds` table before showing the names on screen.
- No claim in this beat sheet is sourced from anything other than FINDINGS.md
  and the workflow file above — there is no external web citation to verify.
