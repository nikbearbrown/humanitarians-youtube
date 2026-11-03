# Frictional log — Vendor Intelligence update: Hardening

## 2026-10-09 — weekly project-update reel (changelog), 16:9 + 9:16
- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G
Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `PROOF-REVIEW.md`
(8/12, gate PASS), `_qc/REPORT.md`, `vendor-intel-hardening.mp4`,
`short/vendor-intel-hardening-short.mp4`. Source: my change log (three reliability
fixes). (YouTube / Drive: TBD.)

**What I was working on.** A changelog reel on three reliability fixes: (1) the model ID
consolidated into a new `collector/models.py` (after Groq retired a model and broke both
collectors at once), (2) the 10-K/A bug, (3) timeouts on Postgres/Neo4j/Bedrock.

**What I tried, and what I expected.**
* I expected the three fixes to read as three unrelated chores.

**Where it resisted, and what I did next.**
* They turned out to share one spine: *failing silently.* The 10-K/A bug is the
  sharpest — `get_filings("10-K")` is a prefix match, so it also returns 10-K/A
  amendments; `.latest()` grabbed one with no Item 1, extraction returned nothing, and
  the row was stored as a failure (AMD `extraction_ok: false`). A plausible result and
  no error — the same class of bug the whole project keeps teaching me to fear. Framed
  the reel around "fail loud, not silent." B02 (the bug, verified AMD FAILED → OK) is
  the standout.

**What Claude contributed, and what I did with it.**
* Mine: the change log (figures + verification), the neutral framing.
* Claude's: built the reel under DOUBLE-CHECK; ran PROOF (8/12 changelog floor), calling
  out B02 as the strongest, verified beat.

**What I understand now, and what I still do not.**
* Understood: silent failures — success-with-empty-data, infinite hangs — are the
  dangerous class; this update is three of them, caught.
* Flag for the record: this reel *creates* `collector/models.py`, which the next week's
  reel (`2026-10-16-vendor-intel-logging-config`) *deletes*. The log is where that
  churn stays honest.
* Not resolved: the repo's `.git` is bloating (~600MB) from committed reel videos — the
  root `.gitignore` doesn't match our `<slug>.mp4` / `-short.mp4` names. Added a scoped
  `fellows/Muskan-k/.gitignore`; the already-committed videos still need untracking.
