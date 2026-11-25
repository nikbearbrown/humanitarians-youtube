# What Does a P-Value Actually Mean? — Gomathy S.

*What Does a P-Value Actually Mean?* Bella, in for Gomathy · Humanitarians AI · built 2026-10-15

A p-value is how likely data this extreme would be if there were no real effect. It is not the chance you're
right, not the size or importance of the effect, and p under 0.05 alone proves nothing.

Text and code only. **The masters live in the shared Google Drive**, not in this repository. See the link below.

**Type:** STEM.

**Opening line.** This video does not use the required opening line ("Hi, I am [name] and this video is about [summary]"). The rule was already in `FELLOWS-SUBMISSION.md` when it was built; it opens "Hi — Bella, in for Gomathy. A study says p is zero point zero three. Meaning?" instead, naming the Kokoro narrator but not saying it is an AI voice. Not re-rendered.

## This week's contribution

- **Question:** A study reports p = 0.03. What does that number mean, and what doesn't it mean?
- **Prediction:** Reviewing the narration and on-screen text once before any build would move corrections into the script instead of the renders.
- **What I built/tried:** Research, script, both cuts and both 4K masters (2026-10-15), my first explainer outside Claude's own behaviour, sourced to the ASA Statement on p-Values (2016).
- **Observed result:** A p-value is how likely data this extreme would be if there were no real effect; it is not the chance you're right or the size of an effect. The video is 63.7 s, not 60. Both masters passed GATE T and GATE V, but checking portrait frames by eye still found overlaps the gates missed.
- **Next experiment:** Not recorded at the time.

## Human and AI work

- **My decisions, implementation and verification:** Approved the script with edits (the greeting, the definition line, "If the null is true…", "p under zero point zero five", "its uncertainty", the summary); rewrote B06 on review; sized the "≈" symbol instead of changing the checker; checked portrait frames by eye; approved the pedagogy gate with five known weaknesses accepted.
- **AI tools/voices used and what they generated:** Claude found the ASA release and a published quote of the definition, confirmed the citation, computed every example number in code, drafted the script and both cuts, and trimmed lines I hadn't edited (194 → 179 words). Kokoro `af_bella` at speed 1.08 generated the narration; the brutalist.art toolkit rendered the beats.
- **What I rejected or corrected:** Rejected "how surprising your data would be if nothing were going on" (read literally, it runs backwards) for the ASA's framing; logged that the coin's 11/1024 is one-sided (two-sided is about 2%); fixed the "ILLUSTRATIVE" overlap and a box touching its line, found by eye.
- **What remains unverified or failed:** The journal page was blocked, so the definition is confirmed through the ASA's release and a published quote. The "no real effect" paraphrase and the confidence-interval row are marked as inference in `SOURCES.md`. Five known weaknesses accepted at the pedagogy gate.

Full record: [`FRICTIONAL.md`](FRICTIONAL.md).

## Reproduce

- **Brutalist version/commit and date checked:** brutalist.art [`ad329089`](https://github.com/nikbearbrown/brutalist.art/commit/ad329089aa2a9cde41a1c8927361187b8da8fb7c) (`main`, 2026-09-28), the only commit of the local checkout used for every build: cloned 2026-09-28, HEAD never moved (checked from its reflog on 2026-11-20). The checkout also has uncommitted local edits to 6 runtime files (20 lines added, 13 removed), last modified 2026-09-28/29, before this build, so the commit alone does not reproduce it exactly. The weekly version check the submission guide asks for was not recorded at build time.
- **Source commit used for this export:** the beat sheets and `scenes.py` files in this folder were committed in [`c5d2730e`](https://github.com/nikbearbrown/humanitarians-youtube/commit/c5d2730e7fc9b00f6ea4151eb5b1acc207d7a284) ([PR #251](https://github.com/nikbearbrown/humanitarians-youtube/pull/251)), after the export. They are byte-identical (SHA-256 compared 2026-11-20) to the copies the masters were built from.
- **Beat sheet and custom scene files:** `beat_sheet.json`, `scenes.py`, `vertical/beat_sheet.json`, `vertical/scenes.py`.
- **Commands or browser steps, dependencies, input/source links:** Built with the [`brutalist.art`](https://github.com/nikbearbrown/brutalist.art) toolkit (`ai-explainer`, `claude-hai` channel). Kokoro narration is generated from `beat_sheet.json` at speed 1.08 and its measured durations are the clock. Masters built with `./art final` (see `BUILD-LOG.md`). Sources are listed below and in `SOURCES.md`.
- **Approvals and checks:** [`CHECKS-REPORT.md`](CHECKS-REPORT.md), [`BUILD-LOG.md`](BUILD-LOG.md), [`PEDAGOGY.md`](PEDAGOGY.md) and the sign-off in [`FRICTIONAL.md`](FRICTIONAL.md) (pedagogy gate approved by me). No PM or professor approval is recorded.

## Watch and review

- **Landscape:** [Drive](https://drive.google.com/drive/folders/1Qv08qMadpEt0HqUofMmGLkYbmBDq5knF?usp=drive_link) — 3840×2160 — 63.7 s — SHA-256 `41879301d41abb6583ce7e41fad1752c46e02b2b6bdff28a9a4e9eb3cc32ceb4` (`p-value.mp4`, built 2026-10-15). Hashed from the local master `brutalist.art/renders/p-value.mp4` on 2026-11-20; it matches the build record. The Drive copy was not hashed.
- **Vertical:** [Drive](https://drive.google.com/drive/folders/1Qv08qMadpEt0HqUofMmGLkYbmBDq5knF?usp=drive_link) — 2160×3840 — 63.7 s — SHA-256 `75164daab2da12ad2f9e1db86ed35542c150494c153b9bcb7646b76c251d3a33` (`p-value-vertical.mp4`, built 2026-10-15). Hashed from the local master `brutalist.art/renders/p-value-vertical.mp4` on 2026-11-20; it matches the build record. The Drive copy was not hashed.
- **Sources/large assets Drive link:** none recorded; the sources cited are listed in `SOURCES.md`.
- **PM review status:** in review (`RENEWAL.md`); no recorded outcome.
- **YouTube 4K processing check:** pending upload.
- **Professors' publication decision:** pending.

## What's in this folder

- **16:9:** `beat_sheet.json` (source of truth), `scenes.py` (Manim beats), `SOURCES.md`, `FACTCHECK.md`,
  `PEDAGOGY.md`, `SHOTLIST.md`, `PROMPTS.md`, `CHECKS-REPORT.md`, `BUILD-LOG.md`.
- **`vertical/` (9:16):** its own `beat_sheet.json` and `scenes.py` (not a crop of the 16:9), plus `BUILD-LOG.md`,
  `SOURCES.md`, `FACTCHECK.md`, `PEDAGOGY.md`, `SHOTLIST.md`, `PROMPTS.md`.

## Sources

The primary source is the American Statistical Association's 2016 statement (`SOURCES.md`, `FACTCHECK.md`):

- Wasserstein, R. L., & Lazar, N. A. (2016). The ASA Statement on p-Values: Context, Process, and Purpose.
  *The American Statistician*, 70(2), 129–133. [doi:10.1080/00031305.2016.1154108](https://doi.org/10.1080/00031305.2016.1154108)
- ASA, [statement release with the six principles](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf)
- J. Utts, [Understanding p-values](https://ics.uci.edu/~jutts/UnderstandingP-Values) (quotes the statement's
  informal definition)

The ASA principle numbers are on the cards that cite them. Every example number (the coin, the two studies) is
computed in `scenes.py` and labelled `ILLUSTRATIVE` on screen; the coin's 11/1024 is a one-sided p-value
(two-sided is about 2%). The plain-language "no real effect" paraphrase and the confidence-interval row are marked
as inference in `SOURCES.md`.
