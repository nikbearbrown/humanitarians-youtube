# Novia Dsilva

Fellow videos for the Medhavi cancer-textbook fact-check CLI series (Humanitarians AI).

## Voice choice

**Voice:** Bella (`af_bella`)
**Register:** Pragmatist — method first, then the counts.

This voice was selected for the reports below and will be kept across the series unless an explicit, documented re-voice decision is made.

Greeting on the Claude bookend: **Hello Novia**. Channel handle: **@Medhavy**.

## Reports

- `2026-08-25-chapter14-fact-check-generation/` — **Video 1.** Fact-Check Generation for cancer textbook Chapter 14 (TME). Four-move workbook: count, split, editorial, reread of the AI-only pile.
- `2026-08-26-chapter28-fact-check-generation/` — Fact-Check Generation for Chapter 28 (Nanotechnology in Cancer). Same workbook on a new chapter.
- `2026-09-06-chapter14-json-fix/` — **Video 2 (this week).** One Sentence, Many Sources. Does not replace video 1. After the fact-check, the record moved from a one-row Excel/Markdown workbook to nested JSON `evidence[]`.

## This week (2026-09-06)

The sentence-by-sentence fact-check was already done (138 sentences, 46 flagged, 115 evidence entries, approved sites only). This week is the **data-model change** after review with the professor.

The original workbook was the record: one row per assertion, one **Sites Visited** cell. That works for a single source. The standard became multiple independent sources per claim (usually 2–4, sometimes disagreeing). A spreadsheet row holds one value per column, so sources flattened into that one cell — you could not tell which source produced which verdict. This was not one bad row: **4 / 18 / 21 / 3** assertions had 1 / 2 / 3 / 4 sources. **42 of 46** flagged assertions hit the same wall.

**JSON is the record. The Excel workbook is generated from it.** Nested `evidence[]` keeps one assertion and many evidence entries: sentence and overall verdict stored once; each source keeps its own URL and verdict. Fix a verdict once, regenerate. Rows are a view, not storage. Overall verdict is a judgment, not a vote (assertion 21 Warburg: three CONFIRMED → TRUE; assertion 129: CONFIRMED + OUTDATED → FLAGGED).

- **Video (16:9 + 9:16):** [Google Drive folder](https://drive.google.com/drive/folders/1VKL-SXi5Zetkg1Os_A3Vd0qVJJQpcZ_C?usp=sharing)
- **Methodology report:** [OneDrive](https://1drv.ms/t/c/b194bf3e40fce876/IQDlgwNSfLCQS6huw3mgrwQLAasS39sJQ5Y8qIgUoq4bPGo?e=arpKMk)

Rebuild with the free local toolkit (`git clone https://github.com/nikbearbrown/brutalist.art.git`), then `./art run <episode>`. Masters and mp3s stay local; they are gitignored.
