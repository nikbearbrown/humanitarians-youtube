# Most Insider Trades Aren't Buys

*Most Insider Trades Aren't Buys* Bella, in for Gomathy · Humanitarians AI · built 2026-11-10

A Form 4 reports any change in an insider's holdings, not only buys. Of 999,542 Form 4 transactions filed
Q2 2023 – Q3 2026, about 8% are purchases (code P). After parse checks and four filters fixed before any return
was computed (private deals, employee plans, late filings, stocks under $1), 65,106 buys are left to test, 6.5% of
all transactions. A spot-check of 25 random buys against the original filings found no errors beyond rounding.
Whether these buys predict anything **has not been tested**; the reel makes no claim about returns.

Text and code only. **The masters live in the shared Google Drive**, not in this repository. See the link below.

## The files

| | File | |
|---|---|---|
| **16:9** | `insider-buying-noise.mp4` | 3840×2160 · 1:05 (64.7 s) |
| **9:16** | `insider-buying-noise-vertical.mp4` | 2160×3840 · 1:05 (64.6 s) |

12 beats, Plain register, Kokoro `af_bella` ("Bella").

## What's in this folder

- **16:9:** `beat_sheet.json` (source of truth), `scenes.py` (Manim beats), `SOURCES.md`, `FACTCHECK.md`,
  `PEDAGOGY.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `BUILD-LOG.md`, `FRICTIONAL.md`.
- **`vertical/` (9:16):** its own `beat_sheet.json` and `scenes.py` (not a crop of the 16:9), plus `BUILD-LOG.md`,
  `SOURCES.md`, `FACTCHECK.md`, `PEDAGOGY.md`, `SHOTLIST.md`, `PROMPTS.md`.

## Sources

Every number comes from the committed audit files of my Mycroft `insider-signals/` module at commit `fed487c`
([GomathySelvamuthiah/mycroft](https://github.com/GomathySelvamuthiah/mycroft), branch
`feature/insider-trading-signals`), built from SEC's
[Insider Transactions Data Sets](https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets).
`SOURCES.md` gives each number's file and line. Form 4 rules are checked against SEC's own pages:

- SEC, [Form 4 and its General Instructions](https://www.sec.gov/files/form4.pdf) (filing deadline, transaction codes,
  Rule 10b5-1 checkbox)
- SEC, [Ownership Form Codes](https://www.sec.gov/edgar/searchedgar/ownershipformcodes.html)
- SEC Investor Bulletin, [Insider Transactions and Forms 3, 4, and 5](https://www.sec.gov/files/forms-3-4-5.pdf)

Spoken roundings, the "employee plans" simplification and other plain-language glosses are marked as inference in
`SOURCES.md`.

## Links

| | Drive | YouTube |
|---|---|---|
| 16:9 and 9:16 masters | <!-- DRIVE_LINK --> [Drive](https://drive.google.com/drive/folders/1ycNcATgR7NhZOC9Qd7e0tp6oIDXTWJZ6) | <!-- YOUTUBE_LINK --> *(to add)* |

## Rebuilding

Built with the [`brutalist.art`](https://github.com/nikbearbrown/brutalist.art) toolkit (`ai-explainer`, `claude-hai`
channel). Kokoro narration is generated from `beat_sheet.json` at speed 1.08 and its measured durations are the clock.
