# Chapter 14 Fact-Check — Methodology & Approach Report

**Book:** Cancer Biology and Oncology Textbook
**Chapter:** 14 (Tumor Microenvironment)
**Date:** 2026-09-03

This report documents the approach, data structure, and quality-control process used to fact-check Chapter 14. It is self-contained and links directly to the two source deliverables:

- **[Chapter 14 Fact-Check Review Workbook (Excel)](https://1drv.ms/x/c/b194bf3e40fce876/IQCS7wXjgyysRYilftCR4rL4AUigjCn6YkGawE0e4UxK6CQ?e=txDGN6)** — the human-review workbook (4 sheets: Summary, Chapter 14, AI-Only, Editorial), generated from the JSON
- **[Chapter 14 Fact-Check Data (JSON)](https://1drv.ms/u/c/b194bf3e40fce876/IQDT3aRvA5wBQ6760LmbwaowAaXuGcOcHScS7QTkfUeDEJ0?e=38Zkmz)** — the canonical data file (source of truth)

### Executive Summary

Chapter 14 (Tumor Microenvironment) was fact-checked sentence by sentence: all 138 sentences across its 6 source files were classified, 46 were flagged for external verification against a fixed list of authoritative websites, and 115 independent pieces of evidence were gathered across those 46 assertions. The results are stored in a JSON file structured as one assertion per fact-checked sentence, each holding a *list* of evidence entries — a design chosen specifically because a single sentence can require several independent sources, and a flat spreadsheet row cannot represent that relationship without either losing detail or duplicating data. The review workbook is generated entirely from this JSON, not maintained separately. Of the 46 flagged assertions, 25 were confirmed accurate, 9 were found false or misleadingly framed, and 12 remain genuinely unresolved and require a human judgment call. The full package was independently audited for structural integrity, source-domain compliance, and data fidelity before being finalized.

### Contents

1. Overall Approach — Four Steps
2. Sentence Classification
3. Site Verification — Approved Sources Only
4. The Problem With Rows, and How JSON Fixes It
5. Overall Verdict — A Judgment, Not a Vote
6. Expert Review Needed — A Separate, Stricter Rule
7. Report Package (Step 4 Output)
8. Quality Assurance Performed
9. Summary Statistics
10. Deliverables

---

## 1. Overall Approach — Four Steps

The fact-check follows a fixed four-step process, applied uniformly to every sentence in the chapter:

**Step 1 — Read the chapter.** All 6 `.mdx` files were read in order. JSX components, imports/exports, and frontmatter metadata were ignored; only the prose content was extracted for classification.

**Step 2 — Classify every sentence.** Each sentence was sorted into one of six flaggable categories, or marked AI-ONLY if it required no external verification (see Section 2).

**Step 3 — Verify flagged sentences using only approved sites.** For every flagged sentence, evidence was gathered *exclusively* from a fixed, category-specific list of authoritative websites (see Section 3). No other website was used to confirm or deny a claim, at any point.

**Step 4 — Generate the report package.** The results were compiled into the JSON data file first, and the review workbook was generated programmatically from that JSON (see Section 7). This methodology report explains that process and data structure.

---

## 2. Sentence Classification

Every sentence in the chapter fell into one of these categories:

| Category | Priority | What it captures |
|---|---|---|
| STAT | Low | Numeric statistics — incidence, percentages, physical measurements |
| GUIDELINE | Highest | Clinical practice recommendations from a medical body |
| APPROVAL | Highest | Drug/device regulatory approval status |
| EVIDENCE | High | Mechanistic or experimental research findings |
| SPECIALIST | High | Gene/protein/pathway-specific molecular claims |
| CURRENT | Medium | Present-day/ongoing status (active trials, current standard of care) |
| AI-ONLY | — | No verification needed (definitions, logical connectives, descriptive lists) |

**Chapter 14 results — 138 total sentences:**

| | Count |
|---|---|
| Flagged for verification | 46 |
| — STAT | 4 |
| — GUIDELINE | 0 |
| — APPROVAL | 0 |
| — EVIDENCE | 21 |
| — SPECIALIST | 13 |
| — CURRENT | 8 |
| AI-ONLY (no verification needed) | 92 |

This chapter covers tumor-microenvironment biology rather than clinical practice, which is why it has zero GUIDELINE/APPROVAL sentences — those categories are populated in other chapters that discuss treatment protocols or drug regulatory status.

---

## 3. Site Verification — Approved Sources Only

Each category is restricted to a fixed list of authoritative domains. No sentence was checked against any website outside its category's approved list:

| Category | Approved domains |
|---|---|
| STAT | seer.cancer.gov, cancer.org, gco.iarc.who.int, gco.iarc.fr |
| GUIDELINE | nccn.org, asco.org, who.int |
| APPROVAL | fda.gov, ema.europa.eu |
| EVIDENCE | pubmed.ncbi.nlm.nih.gov, nature.com, ncbi.nlm.nih.gov |
| SPECIALIST | pubmed.ncbi.nlm.nih.gov, ncbi.nlm.nih.gov, cancer.sanger.ac.uk (COSMIC) |
| CURRENT | clinicaltrials.gov, pubmed.ncbi.nlm.nih.gov, cancer.gov, ncbi.nlm.nih.gov |

**Verdict vocabulary per source checked:**
- **CONFIRMED** — the source supports the claim
- **CONTRADICTED** — the source explicitly states something different
- **OUTDATED** — the source confirms the claim was once true, but for something since superseded (e.g., a discontinued trial)
- **UNVERIFIED** — the approved sites simply have no content addressing this specific point (not evidence against the claim — an honest "not found within the approved list")

A deliberate methodology decision was made not to stop at a single source per claim: wherever multiple genuinely independent, on-domain sources existed, all of them were gathered rather than settling for the first confirming result. This is why most assertions carry 2–4 evidence entries rather than 1 — it surfaces disagreement between sources (see Section 5) that a single-source check would have missed entirely.

Each flagged assertion was checked against between 1 and 4 independent sources (median 2–3), not just one:

| Evidence entries per assertion | Number of assertions |
|---|---|
| 1 source | 4 |
| 2 sources | 18 |
| 3 sources | 21 |
| 4 sources | 3 |

**Total evidence entries across the chapter: 115**, breaking down as:

| Evidence verdict | Count |
|---|---|
| CONFIRMED | 78 |
| UNVERIFIED | 22 |
| CONTRADICTED | 9 |
| OUTDATED | 6 |

---

## 4. The Problem With Rows, and How JSON Fixes It

### The problem

The original workflow — read the chapter, verify each flagged sentence, and write the findings directly into a Markdown report and an Excel workbook — worked well when each assertion was checked against a single source. There was no separate structured data file; the workbook itself was the record, with one row per assertion, a single **"Sites Visited"** cell, and a single **"Finding Summary"** cell.

That format hits a real limit once the verification standard requires *multiple* independent sources per claim (see Section 3) rather than stopping at the first one. A spreadsheet row holds one value per column, so once an assertion had two to four sources — sometimes disagreeing — they all had to be typed into that one cell as flattened text, with no way to record which source produced which verdict. This is a limitation of the format, not a flaw in the original approach: it simply wasn't built to hold more than one source per claim, because it never needed to before. It surfaced directly during review, when an assertion's Overall Verdict would appear as one fixed value even though its underlying sources actually disagreed with each other.

### Why not just use the Markdown report?

The Markdown report can already list several sources under one sentence, and it reads fine to a person. The gap is that Markdown has no structure a program can rely on — a numbered list looks organized to a human eye, but to software it's just unlabeled text, with no guaranteed way to know where one entry ends and the next begins. That's why, in the original workflow, the Excel workbook was produced by someone reading the Markdown report and re-typing it into cells by hand — and that manual step is exactly where multiple sources got compressed into one "Sites Visited" cell. JSON removes that hand-off: it's read and written by scripts, not re-typed by a person, so nothing gets flattened in translation.

### The fix

JSON solves this because, unlike a spreadsheet, it supports **nested structures** — an object can contain a *list* of other objects. That lets the data model match the real relationship: **one assertion, many evidence entries.** The assertion-level fields (sentence, claim, Overall Verdict, Expert Review, Notes) are stored exactly **once**, and each evidence entry — with its own source URL, its own verdict, and its own explanation — lives as a distinct object inside that assertion's `evidence` list. Nothing gets collapsed, and nothing gets duplicated at the level of canonical storage:

The canonical data file ([JSON link above](https://1drv.ms/u/c/b194bf3e40fce876/IQDT3aRvA5wBQ6760LmbwaowAaXuGcOcHScS7QTkfUeDEJ0?e=38Zkmz)) uses this **assertion + evidence-list** schema — a one-to-many relationship, because a single sentence can require multiple independent sources, each with its own verdict:

```json
{
  "chapter": 14,
  "flagged": [
    {
      "id": 21,
      "file": "2_Components_of_the_Tumor_Microenvironment.mdx",
      "category": "EVIDENCE",
      "priority": "High",
      "sentence": "In the 1920s, Otto Warburg found that cancer cells...",
      "claim": "Historical attribution and description of the Warburg effect.",
      "overall_verdict": "TRUE",
      "overall_confirmation": "Confirmed via PubMed + Nature.com",
      "expert": "Yes",
      "notes": "Consider revising the stated rationale to reflect the modern biosynthetic-precursor model.",
      "evidence": [
        { "source": "https://pubmed.ncbi.nlm.nih.gov/21508971/", "verdict": "CONFIRMED", "detail": "..." },
        { "source": "https://www.nature.com/articles/nrc3038", "verdict": "CONFIRMED", "detail": "..." },
        { "source": "https://pubmed.ncbi.nlm.nih.gov/27911732/", "verdict": "CONFIRMED", "detail": "..." }
      ]
    }
  ],
  "ai_only": [ /* 92 sentences not requiring verification */ ],
  "editorial": [ /* 8 internal-consistency findings */ ]
}
```

**Why a list, not a single field:** this is the direct fix for the "Sites Visited" problem described above — instead of flattening every source into one text cell, each source's URL, verdict, and explanation is kept as its own object inside the assertion's `evidence` list, so nothing is collapsed or overwritten when multiple sources disagree.

**The JSON is the single source of truth — the row problem is solved by not treating rows as storage at all.** The Excel review workbook is generated programmatically *from* this JSON, and it does still show one row per evidence entry (so a human can filter/sort by individual source) — but that repetition only exists in the generated view. The canonical data underneath has each fact stored exactly once. If a sentence or verdict needs correcting, it's corrected in one place in the JSON, and the workbook is simply regenerated from it — there is never a question of which of several duplicated rows is the "real" one.

**Scope note:** this report documents Chapter 14 specifically, but the row problem and the JSON fix are not unique to this chapter — the same one-to-many need (multiple sources per claim) applies to every chapter of the book. Chapter 14 is the chapter where this schema was designed and adopted, and it is intended as the template other chapters will follow as their fact-check packages are built or revisited.

---

## 5. Overall Verdict — A Judgment, Not a Vote

Every assertion has one **Overall Verdict** (TRUE / FALSE / FLAGGED) sitting above its evidence list. This is *not* a mechanical count of how many evidence entries agree — it answers "is the textbook sentence, as written, correct?", which is a different question from "does source #1 agree with source #2?"

Two principles govern how Overall Verdict is set when evidence entries disagree:

**Principle 1 — Split sub-claims → FLAGGED.** If a sentence bundles more than one claim and the evidence supports one part while leaving another part unresolved, the Overall Verdict is FLAGGED rather than forcing a single TRUE/FALSE.
*Example — ID 129:* "FAK inhibitors... are under clinical evaluation in mesothelioma and pancreatic cancer." Evidence shows the pancreatic-cancer claim is current (CONFIRMED) while the mesothelioma claim is stale (OUTDATED, since a 2018 trial failure) → FLAGGED.

**Principle 2 — Accurate-but-outdated framing → FALSE, even if every source is CONFIRMED.** If a sentence presents a historical fact as still current, and that framing has since been superseded, the Overall Verdict is FALSE — because each evidence entry only confirms the narrow historical fact, not the sentence's present-tense claim.
*Example — ID 128:* All evidence entries confirm the CENTRIC trial happened and failed (a true historical fact) — but the sentence presents cilengitide as a live investigational strategy. Since that trial halted development over a decade ago, presenting it as current is false → FALSE, despite 100% of the evidence being individually accurate.

**Chapter 14 Overall Verdict distribution (46 flagged assertions):**

| Verdict | Count | Meaning |
|---|---|---|
| TRUE | 25 | Sentence is accurate as written |
| FALSE | 9 | Sentence is wrong or misleadingly framed — needs correction |
| FLAGGED | 12 | Genuinely unresolved or split — needs a human judgment call |

---

## 6. Expert Review Needed — A Separate, Stricter Rule

Expert Review Needed is a distinct field from Overall Verdict, but it follows one fixed rule applied consistently across the whole chapter:

> **Overall Verdict = FALSE or FLAGGED → Expert Review Needed = Yes, always, with no exceptions.**

This was tightened during review: FLAGGED assertions with only a "minor" unresolved detail were initially marked Expert=No, but that created a gap — a reviewer working strictly off the "Expert Review Needed = Yes" column would never see those rows, even though FLAGGED by definition means the sentence isn't fully resolved. The rule was corrected so that anything not cleanly TRUE always surfaces for review.

TRUE is the only verdict that can ever be Expert=No — and even a TRUE sentence can still be marked Expert=Yes if it sits next to a caveat worth a specialist's attention (e.g., ID 21: the sentence itself is accurate, but a nearby historical explanation is now considered scientifically outdated, so a note flags it for optional revision).

**Result: 24 of 46 flagged assertions require expert review** (all 9 FALSE + all 12 FLAGGED + 3 TRUE-with-caveat).

---

## 7. Report Package (Step 4 Output)

The JSON is rendered into a single review workbook ([link above](https://1drv.ms/x/c/b194bf3e40fce876/IQCS7wXjgyysRYilftCR4rL4AUigjCn6YkGawE0e4UxK6CQ?e=txDGN6)), which contains 4 sheets:

- **Summary** — totals table (counts by category, verdict, expert-review)
- **Chapter 14** — one row per evidence entry (115 rows), with Reviewer Decision / Reviewer Comments columns left blank for grading
- **Chapter 14 - AI-Only** — the 92 non-verified sentences, each with a rationale and a hallucination sanity-check result. Every AI-ONLY sentence was re-read a second time, knowledge-only (no web search), purely to catch anything that sounds fabricated or internally implausible: 87 of 92 passed ("sounds accurate"); 5 were flagged for human review (none confirmed as actual fabrications — they are knowledge-only suspicion flags, not web-verified findings).
- **Chapter 14 - Editorial** — 8 internal-consistency findings (contradictions within the chapter itself, independent of external verification)

---

## 8. Quality Assurance Performed

Before finalizing, the full package was audited programmatically against the spec, checking:

- **Structural integrity** — no duplicate/missing IDs across all 138 sentences
- **Site-domain compliance** — every evidence source's URL domain checked against the approved list for its category; 0 violations found
- **Data fidelity** — every one of the 115 Excel rows checked cell-by-cell against the JSON; 0 mismatches
- **Formatting correctness** — verdict color-coding, Expert-review red-bold font, and dropdown validation all verified programmatically against the intended styling rules
- **Cross-sheet consistency** — AI-Only (92) and Editorial (8) sheet row counts confirmed to match the JSON exactly; Summary-sheet totals confirmed to match values computed live from the JSON
- **Sentence provenance** — every stored sentence checked against the actual chapter text it was drawn from, to rule out fabricated or altered quotations

One category of finding surfaced by the provenance check is worth noting explicitly: **4 sentences (IDs 14, 57, 76, 91) initially appeared not to match the source text under a strict character-level comparison.** Direct inspection confirmed all 4 are genuinely, verbatim present in the chapter — the only difference is that the source `.mdx` files use Unicode Greek letters (e.g., "TGF-β", "α-SMA") while the JSON spells these out as English words ("TGF-beta", "alpha-SMA") for readability. This is a transcription-formatting difference, not a factual error or fabrication — the underlying sentences and claims are unchanged.

---

## 9. Summary Statistics

| Metric | Value |
|---|---|
| Total sentences read | 138 |
| Flagged for verification | 46 |
| AI-ONLY (no verification needed) | 92 |
| Editorial findings | 8 |
| Total independent evidence entries gathered | 115 |
| Overall Verdict: TRUE | 25 |
| Overall Verdict: FALSE (CRITICAL) | 9 |
| Overall Verdict: FLAGGED | 12 |
| Assertions requiring expert review | 24 / 46 |
| Hallucination sanity-check flags (AI-ONLY sentences) | 5 / 92 |

---

## 10. Deliverables

| Deliverable | Access |
|---|---|
| Fact-check data (JSON, source of truth) | [Open JSON](https://1drv.ms/u/c/b194bf3e40fce876/IQDT3aRvA5wBQ6760LmbwaowAaXuGcOcHScS7QTkfUeDEJ0?e=38Zkmz) |
| Review workbook (Excel — Summary / Chapter 14 / AI-Only / Editorial sheets) | [Open Workbook](https://1drv.ms/x/c/b194bf3e40fce876/IQCS7wXjgyysRYilftCR4rL4AUigjCn6YkGawE0e4UxK6CQ?e=txDGN6) |
| This methodology report | The document itself |
