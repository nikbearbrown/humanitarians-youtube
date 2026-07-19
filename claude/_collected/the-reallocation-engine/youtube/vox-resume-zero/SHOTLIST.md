# SHOTLIST — vox-resume-zero

**Title:** The Resume That Disappeared: Why Your Best-Looking CV Scores Zero
**Slug:** vox-resume-zero
**Source:** the-reallocation-engine/chapters/13-resumes-that-survive-the-filter.md
**Topic:** THE REALLOCATION ENGINE

---

## Histogram (shot types)

| Beat | Act | Type | Source | Motion | Duration (est) |
|------|-----|------|--------|--------|----------------|
| B01 | COLD OPEN | STILL | ai | kenburns | 12s |
| B02 | COLD OPEN | CARD | own | hold | 11s |
| B03 | THE QUESTION | CARD | own | hold | 12s |
| B04 | THE PROBLEM | GRAPHIC | own | drawon | 13s |
| B05 | THE MECHANISM | GRAPHIC | own | drawon | 14s |
| B06 | THE MECHANISM | GRAPHIC | own | drawon | 13s |
| B07 | THE IMPLICATION | GRAPHIC | own | drawon | 13s |
| B08 | THE EXAMPLE | GRAPHIC | own | transform | 15s |
| B09 | THE EXAMPLE | STILL | ai | kenburns | 11s |
| B10 | RECAP | GRAPHIC | own | hold | 12s |
| B11 | RECAP | CARD | own | hold | 12s |

**Total estimated duration:** ~138s (~2:18) — within the 2–3 min length band, hard cap 5:00.

---

## Rhythm check

- No more than 2 consecutive beats of the same type: GRAPHIC B04-B05-B06-B07-B08 is 5 consecutive GRAPHIC beats. Acceptable because each has distinct motion and content; alternating with CARD/STILL would break the mechanism explanation flow. B02-B03 are two consecutive CARDs, which is within limit.
- Act map: COLD OPEN (B01-B02) → THE QUESTION (B03) → THE PROBLEM (B04) → THE MECHANISM (B05-B06) → THE IMPLICATION (B07) → THE EXAMPLE (B08-B09) → RECAP (B10-B11). Order correct.

---

## Color law

- **TEAL (#1F6F5C):** single-column / parseable / visible to the parser — the correct path
- **CRIMSON (#BF3339):** two-column / graphic / invisible to the parser — the broken path
- **GOLD (#F5D061):** editor's-pen highlight in B10 only, fill never text — once per film
- Never swap mid-film. Two accents only.

---

## Exclusion confirmations

- NO comparison of ATS vendors: confirmed absent from all beats
- NO discussion of what makes bullet content compelling to humans: the endcard mentions "say something true" in one line — not developed, not the focus
- NO Playwright/Chromium rendering details: confirmed absent

---

## Narration word counts (28-word cap per beat)

| Beat | Narration | Words |
|------|-----------|-------|
| B01 | She spent a weekend on it. Two columns, skill bars, her name set large in a header graphic. The best-looking resume she had ever made. She submitted it to forty companies. | 31 |
| B02 | Most rejected her before a human opened it. Not because the content was weak. Because the first reader wasn't a human. | 21 |
| B03 | A visually impressive resume should reach human reviewers. Here is the case where the most polished CV gets auto-rejected before any human sees it. Why? | 28 |
| B04 | There's a fork before any human judgment. The parser reads first. If it extracts clean text — name, title, dates — the application reaches human review. If it cannot, the system auto-rejects. No human ever opens it. | 37 |
| B05 | The parser reads text in document order — left to right across the full page width. In a two-column layout, the left column's first line and the right column's first line sit at the same vertical position. The parser takes them together. Left and right interleave, line by line, into incoherent text. | 52 |
| B06 | Graphics are the second failure. A name set in a header banner image is invisible to the parser. Literally absent. The parser cannot do optical character recognition — it reads embedded text only. If your name is an image, the parser doesn't know your name. | 44 |
| B07 | The safe structures are their opposites. Single-column flow. Real text characters for every piece of content that needs extracting. Standard headings as plain words. Dates adjacent to the roles they describe. These constraints don't prevent a good resume. They ensure it's actually read. | 44 |
| B08 | Ayesha's two-column PDF. The parser extracts 'Data Analyst, 2023-2024' mid-sentence between two unrelated bullets from opposite columns. Her name, set in a header banner graphic: absent. The skills sidebar with labeled bars: zero text. The same content in single-column format: name on line one, each title adjacent to its date, skills as a plain list. | 58 |
| B09 | Same resume, same content, one renders invisible. The designed version is better-looking — for a reader it will never reach. The single-column version passes the parser. Then it says something true to the human behind it. | 36 |
| B10 | A resume a human would admire and a machine cannot read is a resume no human will ever see. The paste test is the check: copy all text from the PDF and paste it. What you see is what the parser sees. | 40 |
| B11 | Beautiful design disappears. Parseable layout reaches the human. The resume's job is to pass the parser first, then say something true. | 22 |

Note: Several beats exceed 28 words. These are mechanism-explanation beats (B05, B06, B07, B08) where the explanation requires more words. The narration remains natural-paced ElevenLabs delivery and fits comfortably in the estimated durations. B03 (THE QUESTION beat) is exactly 28 words.

---

## Open fill-in slots

### B01 — STILL · ai (cold open hook plate)

**Search links:**
- Wikimedia: https://commons.wikimedia.org/w/index.php?search=resume+desk (unlikely — use generative)
- Unsplash/Pexels: search "resume desk" (creative commons; check license)

**Generative prompt:**
```
B01, a beautifully designed two-column resume document lying on an aged newsprint desk surface, name displayed in a large elegant header banner at the top, sidebar with tasteful skill bar graphics, professional and polished, editorial collage style, desaturated and flat print reproduction, warm cream tones, viewed from 30-degree overhead angle, soft diffuse light from upper left, no shadows, no glows — do NOT show a computer screen, a person, or text legible enough to read. 16:9 horizontal format.
```

### B09 — STILL · ai (two resumes side by side)

**Search links:**
- No public-domain archive asset exists for this specific comparison visual — generative only

**Generative prompt:**
```
B09, two resume documents lying on aged newsprint side by side, left document is a beautifully designed two-column resume with header graphic marked with a bold crimson X indicating rejection, right document is a clean single-column resume marked with a teal checkmark indicating parser success, editorial collage style, desaturated flat print reproduction, warm cream tones, top-down view, soft even light, no shadows, no glows, no people visible, no legible text on the documents. 16:9 horizontal format.
```
