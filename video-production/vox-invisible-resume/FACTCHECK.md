# FACTCHECK — vox-invisible-resume

Source of truth: `books/the-reallocation-engine/chapters/13-resumes-that-survive-the-filter.md`.
Every narration line, viz element, and card string checked. ✓ holds · minor
(editorial/simplification, defended) · WRONG (must fix). FLAGGED = sourced but the
chapter itself marks it for verification.

This film deliberately excludes: ATS vendor comparisons, an OCR tangent,
résumé-content/keyword advice, an 82%-stat deep-dive, and the Markdown/Playwright
pipeline. The paste test appears only as the closing payoff (B11).

| # | Claim (beat) | Verdict | Source / derivation | Note |
|---|---|---|---|---|
| 1 | The first reader is a **parser**, not a human; a beautiful doc can be unreadable to it (B01, B04) | ✓ | §4, §6: "The first reader of your résumé is a parser." "A résumé a human would admire and a machine cannot read is a résumé no human will ever see." | The film's thesis, stated in the chapter. |
| 2 | Designed résumé = two columns, skill-bar sidebar, name in a header graphic (B02) | ✓ | §4: "Two columns, a sidebar with tasteful skill bars … the name set large in a header graphic." | Matches the chapter's opening example exactly. |
| 3 | The parser's job is to **extract structured text** — it doesn't care about looks (B03) | ✓ | §6: "It cares whether it can extract structured text." | Quote-card is a compression of this line. |
| 4 | The parser reads the page in **document order, top to bottom / left to right** (B04, B05) | ✓ | §58: "A parser reads text in document order, which in a two-column PDF is typically left-to-right across the full page width, not column by column." | Exact. |
| 5 | Two columns **interleave line by line into nonsense** (B05) | ✓ | §4, §45, §58: "the left column's first line and the right column's first line appear interleaved … it makes the extracted text incoherent." | Break mode 1. Strip shows L1 R1 L2 R2. |
| 6 | A **name in a header image is absent** — parser reads embedded text, can't read pictures (B06) | ✓ | §60: "A name set in a header graphic is invisible to the parser. Literally absent. The parser cannot do OCR; it reads embedded text." | Break mode 2. Film says "can't read pictures — only embedded text" and moves on — NO OCR tangent (card exclusion). |
| 7 | **Skill bars produce no text at all — a gap** (B07) | ✓ | §64: "Skill bars and graphic elements produce no text at all. They exist visually. To the parser, they are a gap." | Break mode 3. Near-verbatim. |
| 8 | The parser then **can't find a job title** and scores the candidate **unqualified for everything** (B08) | ✓ | §4: "The parser could not find a job title. So it scored the candidate as unqualified for everything." | Exact. "dates drifting" ← §32/§62 (tables/columns drift dates). |
| 9 | It happens **before a human opens it**; **~1 in 5** auto-rejected with no human review (B09) | ✓ | §6: "about one in five candidates were auto-rejected with no human review." §4/§11: the fork happens before any human judgment. | "one in five" is stated plainly in the chapter (not flagged). |
| 10 | **~82% / "around eight in ten"** companies screen résumés with software by 2025 (B09) | ✓ (FLAGGED) | §6 + footnote [^13-screening]: "roughly 82% of companies screened résumés with software" — the footnote appends "**[verify]** against primary source." | Chapter commits to 82% but flags it for verification. Film softens to "around eight in ten" (does not stake a precise 82%). Provenance surfaced; safe. |
| 11 | The **fix**: single column, real text, plain headings ⇒ clean ordered extraction (B10) | ✓ | §66: "a single-column flow, real text characters … standard headings as plain words, dates in a consistent parseable format next to the roles." §43: single-column paste test passes. | No keyword/content advice (excluded). |
| 12 | The **paste test**: select all, copy, paste; what you see is what the parser sees (B11) | ✓ | §25: "copy all text from the PDF — Ctrl/Cmd-A, Ctrl/Cmd-C — and paste it into a plain text editor. What you see pasted is roughly what the parser sees." | Appears ONLY as the closing payoff, per the card exclusion. |
| 13 | Card title "Why your beautiful résumé is invisible"; endcard "chapter 13" (B01, B11) | ✓ | Candidate 06 card title; source chapter is `13-resumes-that-survive-the-filter.md`. | — |

## Simplifications, labeled (defended)

- **"around eight in ten"** (B09) for the chapter's "roughly 82%": deliberately softened
  because the chapter's own footnote flags 82% `[verify]`. "Eight in ten" is a faithful,
  less-precise rendering that does not assert a figure the source hasn't confirmed.
  Defended (and this is the safer direction).
- **"can't read pictures — only embedded text"** (B06): plain-language rendering of
  "cannot do OCR; it reads embedded text." Chosen specifically to avoid the OCR tangent
  the card excludes while staying accurate. Defended.
- **"dates drifting"** (B08): the chapter attributes date/title drift to tables and
  columns used for layout (§32, §62). Used here as one symptom in the scramble summary,
  not a separate break-mode lecture. Defended.

## Numbers / text appearing on screen (viz)

- B05 strip: **L1 R1 L2 R2** interleave (3 navy + 3 crimson) — §58. ✓
- B06 / B07: empty crimson slots for name and skills — §60, §64. ✓
- B08: **UNQUALIFIED** stamp — §4. ✓
- B09: the two paths + "~8 in 10 / 1 in 5" context — §6 (82% FLAGGED per footnote). ✓
- No ATS vendor name, no OCR explanation, no keyword advice, no pipeline command appears
  anywhere (confirmed against beat_sheet.json).

**Verdict: all claims hold.** One FLAGGED stat (82%), surfaced and softened to "eight in
ten"; three labeled simplifications, each defended. No WRONG claims. Cleared to render.
