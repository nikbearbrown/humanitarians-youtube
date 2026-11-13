# What Does a P-Value Actually Mean?

*What Does a P-Value Actually Mean?* Bella, in for Gomathy · Humanitarians AI · built 2026-10-15

A p-value is how likely data this extreme would be if there were no real effect. It is not the chance you're
right, not the size or importance of the effect, and p under 0.05 alone proves nothing.

Text and code only. **The masters live in the shared Google Drive**, not in this repository. See the link below.

## The files

| | File | |
|---|---|---|
| **16:9** | `p-value.mp4` | 3840×2160 · 1:04 (63.7 s) |
| **9:16** | `p-value-vertical.mp4` | 2160×3840 · 1:04 (63.7 s) |

12 beats, Plain register, Kokoro `af_bella` ("Bella").

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

## Links

| | Drive | YouTube |
|---|---|---|
| 16:9 and 9:16 masters | <!-- DRIVE_LINK --> [Drive](https://drive.google.com/drive/folders/1Qv08qMadpEt0HqUofMmGLkYbmBDq5knF?usp=drive_link) | <!-- YOUTUBE_LINK --> *(to add)* |

## Rebuilding

Built with the [`brutalist.art`](https://github.com/nikbearbrown/brutalist.art) toolkit (`ai-explainer`, `claude-hai`
channel). Kokoro narration is generated from `beat_sheet.json` at speed 1.08 and its measured durations are the clock.
