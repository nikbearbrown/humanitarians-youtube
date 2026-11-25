# Most Insider Trades Aren't Buys — Gomathy S.

*Most Insider Trades Aren't Buys* Bella, in for Gomathy · Humanitarians AI · built 2026-11-10

A Form 4 reports any change in an insider's holdings, not only buys. Of 999,542 Form 4 transactions filed
Q2 2023 – Q3 2026, about 8% are purchases (code P). After parse checks and four filters fixed before any return
was computed (private deals, employee plans, late filings, stocks under $1), 65,106 buys are left to test, 6.5% of
all transactions. A spot-check of 25 random buys against the original filings found no errors beyond rounding.
Whether these buys predict anything **has not been tested**; the reel makes no claim about returns.

Text and code only. **The masters live in the shared Google Drive**, not in this repository. See the link below.

**Type:** project update.

**Opening line.** This video does not use the required opening line ("Hi, I am [name] and this video is about [summary]"). The rule was already in `FELLOWS-SUBMISSION.md` when it was built; it opens "Hi — Bella, in for Gomathy. An insider buys stock. Is that a signal?" instead, naming the Kokoro narrator but not saying it is an AI voice. Not re-rendered.

## This week's contribution

- **Question:** An insider buys stock. Is that a signal? First: how much of what insiders report on Form 4 is actually a buy?
- **Prediction:** The working title, "Most Insider Buying Is Noise". The audit said otherwise: 65,106 of the 78,495 qualifying buys (83%) pass the filters. What the data supports is that most Form 4 transactions aren't buys (purchases are 8.2% of rows), so the title changed.
- **What I built/tried:** A reel built only from the committed audit files of my Mycroft `insider-signals/` module at commit [`fed487c`](https://github.com/GomathySelvamuthiah/mycroft/commit/fed487c28b47daaf3330a4fa2890e3fce6362d54) ([PR #86](https://github.com/nikbearbrown/mycroft/pull/86)), with every number cited by file and line in `SOURCES.md`.
- **Observed result:** Of 999,542 Form 4 transactions filed Q2 2023 – Q3 2026, about 8% are purchases, and 65,106 buys are left to test after parse checks and four pre-registered filters. Whether they predict anything has not been tested; the reel makes no claim about returns. Both masters (about 64.7 s) passed GATE T and strict GATE V.
- **Next experiment:** The returns analysis, in Mycroft (PR #86). Since this reel: price enrichment ran and its gate (G3) was cleared on 2026-11-20; scoring signals comes next. No returns have been reported.

## Human and AI work

- **My decisions, implementation and verification:** Approved the new title; edited B04, B05, B06 and B08 in first review; chose line trims over a faster voice (80.8 s → 64.7 s); chose four pre-final line fixes after re-reading the full narration; did not use uncommitted Mycroft work; approved the pedagogy gate with eight known weaknesses accepted.
- **AI tools/voices used and what they generated:** Claude read the committed audit files, traced every number to a file and line, checked the Form 4 facts against SEC's pages, flagged that the working title didn't match the data, and drafted the script and both cuts. Kokoro `af_bella` at speed 1.08 generated the narration; the brutalist.art toolkit rendered the beats.
- **What I rejected or corrected:** Rejected the working title; rejected speeding the voice to 1.12 in favour of cuts; reworded B04, B06, B07 and B08 for clarity; moved B03's Purchases row 0.1 units inward after the first 4K vertical final was refused.
- **What remains unverified or failed:** Whether these buys predict returns is untested. A 9:16 review-cut edge flag is a documented false positive from the toolkit compiler's padding, left unfixed in the shared toolkit. "Every filter" in B08 is labelled inference (scope). Eight known weaknesses accepted.

Full record: [`FRICTIONAL.md`](FRICTIONAL.md).

## Reproduce

- **Brutalist version/commit and date checked:** brutalist.art [`ad329089`](https://github.com/nikbearbrown/brutalist.art/commit/ad329089aa2a9cde41a1c8927361187b8da8fb7c) (`main`, 2026-09-28), the only commit of the local checkout used for every build: cloned 2026-09-28, HEAD never moved (checked from its reflog on 2026-11-20). The checkout also has uncommitted local edits to 6 runtime files (20 lines added, 13 removed), last modified 2026-09-28/29, before this build, so the commit alone does not reproduce it exactly. The weekly version check the submission guide asks for was not recorded at build time.
- **Source commit used for this export:** the beat sheets and `scenes.py` files in this folder were committed in [`75f168ea`](https://github.com/nikbearbrown/humanitarians-youtube/commit/75f168ea75e22efa619b16d9e2743f6c674d33f6) ([PR #386](https://github.com/nikbearbrown/humanitarians-youtube/pull/386)), after the export. They are byte-identical (SHA-256 compared 2026-11-20) to the copies the masters were built from.
- **Beat sheet and custom scene files:** `beat_sheet.json`, `scenes.py`, `vertical/beat_sheet.json`, `vertical/scenes.py`.
- **Commands or browser steps, dependencies, input/source links:** Built with the [`brutalist.art`](https://github.com/nikbearbrown/brutalist.art) toolkit (`ai-explainer`, `claude-hai` channel). Kokoro narration is generated from `beat_sheet.json` at speed 1.08 and its measured durations are the clock. Masters built with `./art final` (see `BUILD-LOG.md`). Sources are listed below and in `SOURCES.md`.
- **Approvals and checks:** [`CHECKS-REPORT.md`](CHECKS-REPORT.md), [`BUILD-LOG.md`](BUILD-LOG.md), [`PEDAGOGY.md`](PEDAGOGY.md) and the sign-off in [`FRICTIONAL.md`](FRICTIONAL.md) (pedagogy gate approved by me). No PM or professor approval is recorded.

## Watch and review

- **Landscape:** [Drive](https://drive.google.com/drive/folders/1ycNcATgR7NhZOC9Qd7e0tp6oIDXTWJZ6) — 3840×2160 — 64.7 s — SHA-256 `eb625ed4888705189ce9ef78bde60b3e9902adef85401a32bdaf42bb942e3d42` (`insider-buying-noise.mp4`, built 2026-11-11 (UTC)). Hashed from the local master `my-videos/youtube/insider-buying-noise/insider-buying-noise.mp4` on 2026-11-20; it matches the build record. The Drive copy was not hashed.
- **Vertical:** [Drive](https://drive.google.com/drive/folders/1ycNcATgR7NhZOC9Qd7e0tp6oIDXTWJZ6) — 2160×3840 — 64.6 s — SHA-256 `e8a97b8ed4eb853294200b7f88d72d367d35ed317b2f1b69595e677d07a43040` (`insider-buying-noise-vertical.mp4`, built 2026-11-11 (UTC)). Hashed from the local master `my-videos/youtube/insider-buying-noise/vertical/insider-buying-noise-vertical.mp4` on 2026-11-20; it matches the build record. The Drive copy was not hashed.
- **Sources/large assets Drive link:** none recorded; the sources cited are listed in `SOURCES.md`.
- **PM review status:** pending; no recorded outcome.
- **YouTube 4K processing check:** pending upload.
- **Professors' publication decision:** pending.

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
