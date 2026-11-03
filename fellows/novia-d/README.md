# Novia D.

**Role:** Data Scientist  
**Project:** Medhavi cancer-textbook fact-check  
**GitHub:** [@Novia-Dsilva](https://github.com/Novia-Dsilva)

Fellow videos for the Medhavi cancer-textbook fact-check CLI series (Humanitarians AI).

## Voice choice

**Voice:** Bella (`af_bella`)
**Register:** Pragmatist — method first, then the counts.

This voice was selected for the reports below and will be kept across the series unless an explicit, documented re-voice decision is made.

Greeting on the Claude bookend: **Hello Novia**. Channel handle: **@Medhavy**.

## Reports

- `2026-08-25-chapter14-fact-check-generation/` — **Video 1.** Fact-Check Generation for cancer textbook Chapter 14 (TME). Four-move workbook: count, split, editorial, reread of the AI-only pile.
- `2026-08-26-chapter28-fact-check-generation/` — Fact-Check Generation for Chapter 28 (Nanotechnology in Cancer). Same workbook on a new chapter.
- `2026-09-06-chapter14-json-fix/` — **Video 2.** One Sentence, Many Sources. Does not replace video 1. After the fact-check, the record moved from a one-row Excel/Markdown workbook to nested JSON `evidence[]`.
- `2026-10-12-factcheck-handoff/` — **The Handoff.** What was added on top of the original prompt, so the next person can run the pipeline. Does not replace videos 1 or 2.

## Status (as of 2026-10-12)

**36 packages done, all current format:** 14, 23, 25, 30, 1, 6, 9, 10, 13, 19, 27, 31, 32, 2, 4, 5, 7, 12, 16, 28, 29, 33, 3, 11, 15, 26, 8, 20, 21, 22, 24, 34, 35, 36, 37, 38

This week is the **handoff reel**: the eight additions on top of Prof. Evin Gultepe's original prompt (one chapter at a time, bullet = sentence, approved sites only, JSON as the record, one sentence / many sources, four-file package, required AI-Only second read, completeness + classification-bypass), how one sentence moves, and the 36-done count above.

JSON is still the record. The Excel workbook is generated from it. Nested `evidence[]` keeps one assertion and many evidence entries. Overall verdict is a judgment, not a vote. FALSE or FLAGGED always means expert review.

- **Handoff video (16:9 4K + 9:16 4K):** masters stay local (gitignored). Source in `2026-10-12-factcheck-handoff/`.
- **Earlier videos (16:9 + 9:16):** [Google Drive folder](https://drive.google.com/drive/folders/1VKL-SXi5Zetkg1Os_A3Vd0qVJJQpcZ_C?usp=sharing)
- **Methodology report:** [OneDrive](https://1drv.ms/t/c/b194bf3e40fce876/IQDlgwNSfLCQS6huw3mgrwQLAasS39sJQ5Y8qIgUoq4bPGo?e=arpKMk)

Rebuild with the free local toolkit (`git clone https://github.com/nikbearbrown/brutalist.art.git`), then `./art run <episode>`. Masters and mp3s stay local; they are gitignored.

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.
