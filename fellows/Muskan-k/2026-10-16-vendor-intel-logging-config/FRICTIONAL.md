# Frictional log — Vendor Intelligence update: Loud by Default

## 2026-10-16 — weekly project-update reel (changelog), 16:9 + 9:16
- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G
Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md`, `PROOF-REVIEW.md`
(8/12, gate PASS), `_qc/REPORT.md`, `vendor-intel-logging-config.mp4`,
`short/vendor-intel-logging-config-short.mp4`. Source: my change log (two tickets).
(YouTube / Drive: TBD.)

**What I was working on.** A changelog reel on two tickets: (1) replace `print` with
structured logging — 225 prints, zero logging; a silent print had hidden a broken
Langfuse handler; converted 76 across 9 files, kept 83 CLI report-prints; (2) a validated
`settings.py` — 36 scattered `os.getenv` calls → one module, blank = absent, `require()`
reports every missing key at once.

**What I tried, and what I expected.**
* I expected this to be a clean two-ticket update with no surprises in the build itself.

**Where it resisted, and what I did next.**
* Content-wise, the honest friction is in the work, not the render: this ticket
  *deletes* `collector/models.py` — the file I *created* only one reel ago (the 2026-10-09
  "Hardening" reel). I documented that reversal in the reel's verdict and pedagogy rather
  than quietly dropping it.
* Build-wise: the short pipeline (portrait cards + 9:16 bookend render + compile) ran
  past the 10-minute command window and finished in the background (exit 0, 166s, 4K) —
  no error, just long.

**What Claude contributed, and what I did with it.**
* Mine: the change log (exact counts; the verification — 12 modules import, 17 tests
  pass), the neutral framing.
* Claude's: built the reel under DOUBLE-CHECK; ran PROOF (8/12), which liked the real
  incident hook and the "kept 83 CLI prints" judgment, and flagged that I should show the
  *actual* log lines on screen rather than describe them.

**What I understand now, and what I still do not.**
* Understood: the reel series itself is now a record of config churn — `models.py`
  created, then deleted a week later — and the frictional log is where that stays honest.
* Not resolved: the `.git` video bloat (~600MB). A scoped `.gitignore` stops new videos;
  fully reclaiming it needs a history rewrite, which I'm deferring because it's a shared
  repo and would disrupt other fellows.
