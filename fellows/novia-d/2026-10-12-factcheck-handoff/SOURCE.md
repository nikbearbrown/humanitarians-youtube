# Fact-Check Project — Handoff Document

**Project:** Cancer Biology and Oncology Textbook fact-check
**Prepared by:** Novia Dsilva

---
## ACCESS TO THE RESOURCES

Chapter 14 — Methodology & Approach Report (explains the JSON fix, see point 4 below): **[link](https://1drv.ms/t/c/b194bf3e40fce876/IQDlgwNSfLCQS6huw3mgrwQLAasS39sJQ5Y8qIgUoq4bPGo?e=MVJ4HW)**

Videos: **[Google Drive folder](https://drive.google.com/drive/folders/1pA-SERJ8Pyl_3xoiSZJcOTTVZ2KtRZlA?usp=sharing)**

GitHub — brutalist video: **[link](https://github.com/nikbearbrown/humanitarians-youtube/tree/main/fellows/novia-d)**

---

## Part A — Original Prompt

This is the starting spec from Prof. Evin Gultepe: **[link — add here]**

Everything in Part B is what we added on top of it.

---

## Part B — What we added on top of the prompt

**1. One chapter at a time**
- The prompt says: read the whole book, write one report.
- We don't do that. We do one chapter at a time.
- Some chapters have 1,200+ sentences — too much for one pass.
- Each chapter gets its own folder: `content/docs/ChapterN/`.
- Inside a chapter, we split the files into 3–4 batches, run them at the same time, then merge the results.

**2. Rules for bullet points and headers**
- The prompt doesn't say how to handle bullet points or headers.
- We added two rules:
  - Every bullet or numbered item is its own sentence, including sub-bullets.
  - A bold-only header line (like `**Mechanisms:**`) is skipped — it's not a sentence.

**3. Verification sites — never change these**
- The prompt gives 6 categories. Each has its own approved list of websites.
- Rule: only use the approved sites for that category. Never a different one, even a well-known site.
- If none of the approved sites confirm a claim, the answer is "unverified." Don't look elsewhere.
- Two small changes we made:
  - The prompt names exact pages (like one specific FDA page). Pages move over time, so we approve the whole domain instead (e.g. `fda.gov`).
  - We added a couple of extra domains for sources that publish in more than one place: `gco.iarc.who.int` alongside `gco.iarc.fr` for STAT, and `ncbi.nlm.nih.gov` for EVIDENCE and CURRENT. (For SPECIALIST this isn't a new domain — the prompt already names `ncbi.nlm.nih.gov/gene/`; we just widened it to the whole domain.)

**4. A real data structure: JSON (not in the prompt at all)**
- The prompt only asks for one Markdown file.
- Prof. wanted more than that: a complete, correct data structure — not an Excel sheet as the main record.
- So every chapter's result is saved first as a JSON file. The Excel workbook and both Markdown reports are generated *from* that JSON.
- If something needs fixing, we fix it once in the JSON, then regenerate the rest.
- Why JSON and not a bigger spreadsheet: one Excel cell holds one value. A single sentence can need several sources. JSON can hold a list — Excel can't.
- Full example with real data: see the Chapter 14 report link above.

**5. One sentence, many evidence sources**
- The prompt checks a sentence against one site and gives one verdict.
- In practice, a claim often needs more than one source — e.g. a drug's mechanism (PubMed) and its FDA status (FDA) are two separate checks.
- Sometimes sources disagree.
- Fix: each sentence's evidence is a list. Each source gets its own entry (link + verdict + detail).
- The four verdict words from the prompt don't change: CONFIRMED / OUTDATED / UNVERIFIED / CONTRADICTED. Each one now belongs to a single source, not the whole sentence.
- On top of that list, we added one more thing: one overall verdict for the whole sentence — **TRUE / FALSE / FLAGGED**.
  - Sources disagree on different parts of the sentence → `FLAGGED`.
  - The sentence was true once, but isn't anymore (e.g. an approval later withdrawn) → `FALSE`, even if every source says CONFIRMED.
  - Rule: FALSE or FLAGGED always means `Expert Review Needed = Yes`.

**6. Four files instead of one**
The prompt asks for one Markdown file. We produce four per chapter:
- **JSON** — the real data (point 4).
- **Excel workbook, 4 sheets** — Summary, flagged sentences (one row per evidence source), AI-Only sentences, Editorial notes. Every sheet has a spot for a reviewer's decision and comment — the prompt doesnt include this.
- **Two Markdown reports** — one for flagged/verified sentences, one for AI-Only + Editorial + the hallucination check (next point).

Two small side-effects:
- The prompt's separate "Unverified Sentences" table is gone. UNVERIFIED is just one possible value on a single evidence entry now.
- "CRITICAL" used to mean "verdict OUTDATED or CONTRADICTED." Now it means "Overall Verdict = FALSE," since those two words moved down to the individual source level.

**7. Checking AI-Only sentences for mistakes**
- The prompt says: note anything odd "if you notice it." That's optional.
- We made it required. Every AI-Only sentence gets a second read — no web search, just checking if it sounds right.
- Warning: a "0 issues found" result is not automatically safe to trust. This has already gone wrong once — a chapter reported 0 issues out of 1,599 sentences, then a real re-check found 26 genuine problems. Always double-check a zero.

**8. Two extra safety checks**
- **Completeness check** — makes sure every sentence in the source file was actually captured. (A batch once said "done" and passed every check, but had secretly skipped most of a file.)
- **Classification-bypass check** — makes sure no AI-Only sentence was secretly "decided true" from memory instead of being properly checked. (Warning sign: a category name like "EVIDENCE" showing up inside an AI-Only tag — that should never happen.)
- Run both on every chapter, every time.


---

## Part C — How one sentence moves through the process

**The flow, start to finish:**

```
Sentence from the .mdx file
        |
        v
Does it match one of the 6 categories?
(STAT / GUIDELINE / APPROVAL / EVIDENCE / SPECIALIST / CURRENT)
        |
   NO --+-- YES
   |         |
   v         (see the FLAGGED path below)
AI-ONLY path
```

**If NO — AI-ONLY path:**
```
AI-ONLY sentence
        |
        v
Hallucination Sanity Check
(re-read using own knowledge only, no website)
        |
        v
Sounds right (OK)  or  sounds wrong (flagged)?
        |
        v
Goes into the "AI-Only" sheet either way, with that result recorded
```

**If YES — FLAGGED path:**
```
FLAGGED sentence
        |
        v
Search ONLY the approved sites for that category
        |
        v
Record one evidence entry per source checked:
source link + verdict (CONFIRMED / OUTDATED / UNVERIFIED / CONTRADICTED) + detail
        |
        v
Decide ONE Overall Verdict for the whole sentence: TRUE / FALSE / FLAGGED
        |
        v
FALSE or FLAGGED? -> Expert Review = Yes        Otherwise -> Expert Review = No
        |
        v
Goes into the "Chapter N" sheet (one row per evidence entry)
```

### The Hallucination Sanity Check, explained

This only applies to AI-Only sentences — the ones that skipped Step 3. It means reading the sentence again. No website. Just one question: *does this sound wrong?*

This is a judgment call the AI makes, not a mechanical check. For every AI-Only sentence, the AI writes two things: a verdict (accurate, or flagged) and its own written reason for that verdict.

The AI-Only sheet has its own columns for this:

| Column | What it means |
|---|---|
| Sentence | Exact text from the book |
| Source Verified | Always "N/A (AI-ONLY)" — never went through Step 3 |
| Spec Sub-Type Match | A short label for *why* it didn't need verification (e.g. "definition," "general mechanism," "logical connector") |
| Hallucination Sanity Check Result | ✓ if it sounds correct, ✗ if something seems off |
| Hallucination Sanity Check | The explanation — what was checked, and why it passed or failed |

Source Verified and Spec Sub-Type Match are also things we added, not things the prompt asked for. The prompt only names five kinds of sentences that count as AI-Only — it never asks for a column tracking which kind applies, or a column marking that a sentence skipped verification.

---

## Part D — How to build a chapter (checklist)

1. Check `content/docs/ChapterN/` first. Don't assume a chapter's status.
2. Read the `.mdx` files. Split into 3–4 batches. Run them at the same time.
3. Merge all batches into one JSON. `flagged` and `ai_only` share one ID list. `editorial` has its own.
4. Run these scripts in order: `validate_chapter.py` → `completeness_check.py` + `classification_bypass_check.py` (check any hits by hand) → `build_chapter_workbook.py` + `generate_chapter_reports.py` → `final_audit_chapter.py`.
5. Copy the 4 files into `content/docs/ChapterN/`. Never overwrite an existing package (Part B, point 9).

Scripts and setup instructions: `scripts/factcheck/README.md`.

---

## Part E — Status (as of 2026-10-12)

**36 chapters done, current format:** 14, 23, 25, 30, 1, 6, 9, 10, 13, 19, 27, 31, 32, 2, 4, 5, 7, 12, 16, 28, 29, 33, 3, 11, 15, 26, 8, 20, 21, 22, 24, 34, 35, 36, 37, 38

