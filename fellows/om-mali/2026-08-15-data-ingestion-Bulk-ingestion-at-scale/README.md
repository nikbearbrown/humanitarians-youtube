# 2026-08-15 - Bulk ingestion at scale

**Week covered:** 2026-08-10 - 2026-08-16

**Video:** [Mycroft_OmMali_15_08_2026.mp4](https://drive.google.com/drive/folders/1ueu5Fy9flEOYmzNXVpHvwfMPR76A4LKv)

**Process log:** [FRICTIONAL.md](./FRICTIONAL.md)

## Result

The Private AI Valuation Agent works out a per-share price for private companies such as Anthropic, OpenAI, SpaceX and Databricks, using the quarterly reports that US mutual funds are required to file with the SEC: a fund must disclose what a holding is worth in dollars and how many shares it owns, and dividing one by the other gives a price for a company that has no share price.

This week turned that idea into a dataset: fourteen quarters of filings,
downloaded, filtered and checked.

- **80.5 million filed rows were narrowed to 5,806 holdings** in the companies
  being tracked, across 14 quarters and 5.9 GB of SEC data. Every row is
  accounted for in a table showing where it went, so nothing is quietly
  dropped.
- **The SEC publishes this data about two months late**, and that has a
  consequence worth stating plainly: a striking price found by hand earlier is
  **not in the bulk data at all and cannot be**, because the filings carrying
  it had not been published yet. A test now records this limit so a later
  version cannot quietly paper over it.
- **Two date bugs were found that would have reversed the project's main
  result.** Dates were stored as text, so they sorted alphabetically — putting
  30 April before 31 March. And the obvious-looking date column is the fund's
  financial year end, not the date the holdings are valued: one fund reports a
  year end of 31 May while its holdings are valued at 27 February.
- **Fidelity was being counted as four separate fund managers**, which would
  have inflated exactly the figure that measures how many managers agree.
- **The holder base is far wider than expected** — 31 fund groups hold these
  companies that an earlier search had missed entirely.
- **Scope was deliberately reduced** from 27 quarters to 14, because the
  earlier quarters contain almost none of these companies. The missing range
  is recorded as a known gap rather than left unmentioned.

---

## The episode

The unglamorous week, and the one that decides whether anything later is true. Eighty million
filed rows come in; 5,806 come out; the deliverable is a table showing where every single one
went.

The turn in the episode is that the $589 repricing, verified by hand the week before, is
provably absent from the route this week built. That is a structural property of the SEC's
publication lag, not a bug, and it is pinned by a test so a future version cannot quietly
"fix" it.

| Document | What it is |
|---|---|
| `narration_script.md` | the spoken script, with timings measured rather than estimated |
| `figdata_week2.json` | the measured data every figure was drawn from |
| `BUILD-PROMPT.md` | the single paste-ready prompt that rebuilds this reel end to end |
| `BUILD-LOG.md` | decisions taken, and every defect found by reading frames |
| `CHECKS-REPORT.md` | the PROOF GATE — per-beat SHOW/HOLD classification, written before the first compile |
| `FACTCHECK.md` | 20 rows traced to source (row 16 is derived, not quoted, and says so) |
| `PEDAGOGY.md` | GATE P — what the author is being asked to sign off on |
| `description.txt` | the written version of the episode |

## The built reel

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`) — free and local
throughout: Kokoro TTS, Remotion, ffmpeg. **$0.00 spent, no API key used.**

Eleven beats, 3:00, 3840×2160. **GATE P signed, GATE L and GATE V clean, 20 FACTCHECK rows
traced.**

The rendered media and the figure `pantry/` have since been cleared from this folder to keep
the repository small; `figdata_week2.json` and `beat_sheet.json` remain, which is what the
reel is actually rebuilt from.

Nothing here is published. The masters stay in this folder.
