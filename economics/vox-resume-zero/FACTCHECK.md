# FACTCHECK — vox-resume-zero

Source chapter: the-reallocation-engine/chapters/13-resumes-that-survive-the-filter.md

---

## Claims audit

| Claim | Beat | Verdict | Source / Note |
|-------|------|---------|---------------|
| Candidate spends a weekend, submits to forty companies, most reject before a human opens it | B01 | minor | Chapter 13 para 1: "A candidate spends a weekend on a résumé… submits it to forty companies. Most reject it before a human opens it." Direct from chapter. |
| ~82% of companies screen resumes with software | B02 | minor | Chapter 13: "roughly 82% of companies screened résumés with software" with footnote [^13-screening] tagged **[verify]** against primary source. Used as stated in chapter; labeled illustrative pending verification. |
| ~1 in 5 candidates auto-rejected before human review | B02 | minor | Chapter 13: "about one in five candidates were auto-rejected with no human review." Footnote tagged **[verify]**. Used as stated in chapter. |
| A visually impressive resume should reach human reviewers | B03 | checkmark | Naive expectation, correctly framed as the gap-formula setup. Not a factual claim. |
| Parsers read text in document order, left to right across full page width | B05 | checkmark | Chapter 13: "A parser reads text in document order, which in a two-column PDF is typically left-to-right across the full page width, not column by column." Direct from chapter. |
| Two-column layout causes columns to interleave line by line into incoherent text | B05 | checkmark | Chapter 13: "the left column's first line and the right column's first line appear interleaved. This is not a subtle degradation — it makes the extracted text incoherent." Direct from chapter. |
| Parser cannot do OCR; reads only embedded text | B06 | checkmark | Chapter 13: "A name set in a header graphic is invisible to the parser. Literally absent. The parser cannot do OCR; it reads embedded text." Direct from chapter. |
| Skill bars and graphic elements produce no text | B06 | checkmark | Chapter 13: "Skill bars and graphic elements produce no text at all. They exist visually. To the parser, they are a gap." Direct from chapter. |
| Safe structures: single-column, real text characters, standard headings, dates adjacent to roles | B07 | checkmark | Chapter 13: "The safe structures are their opposites: a single-column flow, real text characters for every piece of content that needs to be extracted, standard headings as plain words, dates in a consistent parseable format next to the roles they describe." Direct from chapter. |
| Ayesha's two-column PDF: "Data Analyst, 2023-2024" mid-sentence between unrelated bullets | B08 | illustrative | Invented example. Character name "Ayesha" is made up. The behavior described (title-date mid-sentence between unrelated bullets) is consistent with the chapter's mechanism. Labeled illustrative. |
| Ayesha's name set in header banner graphic: absent in parser output | B08 | illustrative | Invented example consistent with chapter mechanism. Labeled illustrative. |
| Skills sidebar with labeled bars: zero text in parser output | B08 | illustrative | Invented example consistent with chapter mechanism. Labeled illustrative. |
| Single-column: name on line one, title adjacent to date, skills as plain list | B08 | illustrative | Invented example illustrating the correct outcome. Consistent with chapter's worked trace. Labeled illustrative. |
| Paste test: copy all text from the PDF, paste into plain text editor — what you see is what the parser sees | B10 | checkmark | Chapter 13: "copy all text from the PDF — Ctrl/Cmd-A, Ctrl/Cmd-C — and paste it into a plain text editor. What you see pasted is roughly what the parser sees." Direct from chapter. Qualifier "roughly" honored in narration framing. |

---

## Terms table

| Term | Debut beat | Prior beat that created the need |
|------|-----------|----------------------------------|
| ATS (applicant-tracking system) | B02 (implicit: "software") | B01 (auto-rejection before human opens it) |
| Parser | B04 | B02 (software screens first) |
| Document order | B05 | B04 (parser reads first — viewer now wants to know HOW) |
| OCR (optical character recognition) | B06 | B06 (parser is described as NOT doing OCR — used negatively, no prior explanation needed) |
| Paste test | B10 | B05-B06 (mechanism explained — viewer now wants the practical check) |

---

## Exclusion confirmations

- **No ATS vendor comparisons:** confirmed. No vendor names appear anywhere.
- **No discussion of bullet content quality:** B11 says "say something true" in one line only — not developed.
- **No Playwright/Chromium details:** confirmed absent.
- **No invented numbers presented as facts:** the 82% and 1-in-5 statistics are from the chapter and tagged **[verify]**; Ayesha example is labeled illustrative.

---

## Illustrative numbers

- Ayesha example: all details (name, specific column behavior, outcome) are **illustrative** — invented to demonstrate the mechanism described in the chapter.
