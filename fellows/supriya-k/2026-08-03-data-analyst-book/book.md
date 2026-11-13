# book.md — Data Analyst Interview Prep

*The one-page pitch. Everything in Blueprint (vision → architecture → chapter spec → risk → outline) flows from this. Filled during Phase 0. Informed by `blueprint-trends-notes.md` (2026 interview-structure research).*

---

## One-sentence pitch

A practice-first guide that walks an entry-level candidate through the **entire** data analyst interview — recruiter screen, technical rounds, case/business round, and behavioral — teaching the *pattern of what each stage tests* and drilling it with original, real-style practice questions.

## Central argument (one sentence)

Entry-level candidates rarely fail data analyst interviews for lack of talent; they fail because **no one taught them what each stage is actually testing** — so a book organized around the real end-to-end process, with original practice questions calibrated to each stage, prepares a candidate better than any pile of scattered resources.

## The gap this book fills

Most prep resources drill *one slice* (a SQL practice site, a stats PDF, a list of behavioral questions) and leave the candidate to assemble the whole interview themselves. Others are aimed at data scientists / ML engineers. Few give an *entry-level data analyst* a single, stage-by-stage map of the real hiring process — what the recruiter screen is really checking, why the case round grades business framing over correctness, what a behavioral panel is listening for — paired with **original** practice questions written in the style of real interviews (not scraped from a question bank).

## The one specific reader

A recent graduate or bootcamp finisher, a few weeks out from data analyst interviews, with **foundational exposure** to SQL, spreadsheets, and intro statistics but no clear picture of how the full interview process works or what each round rewards. Can write a simple query; has never done a take-home case study or a structured behavioral round.

**Capability at the end (that they lack now):** navigate every stage of a real data analyst interview loop — hold a strong recruiter screen, clear the SQL/stats/spreadsheet/Python technical rounds, structure and present a business case, and answer behavioral questions with evidence — while understanding *what each interviewer is evaluating* and adapting accordingly.

## What makes this book distinct

- **Organized around the real process, end to end** — recruiter screen → technical → case/business → behavioral — not around a topic taxonomy.
- **"What's tested here" is explicit in every chapter** — each stage chapter names the evaluation pattern (what the interviewer is really scoring) before any practice.
- **All practice questions are original.** Written in the *style* of real interview questions, calibrated to each stage — never copied from any question bank, site, or company. This is a hard editorial rule (see below).
- **Current for 2026** — reflects observed shifts: responsible AI-tool use (knowing when to trust vs. read a generated query), take-home case studies on intentionally messy data, and the heavier weighting of communication and business framing.

## Scope

**In scope (this version):** the full standard process for an entry-level data analyst role — recruiter/HM screen, the four technical areas (SQL, statistics & experimentation, spreadsheets, Python/pandas), the case/business round, and the behavioral round — plus an orientation chapter and a capstone mock-loop. ~10 chapters (comprehensive).

**Deliberately out of scope (for now):** deep machine-learning / modeling interviews, data-engineering / pipeline-design loops, BI-tool tutorials (Tableau/Power BI product training), and company-specific guides. Candidates for a later edition.

## High-level outline (draft — refined in outline.md)

1. **The Data Analyst Interview, End to End** — the full process, every stage, what each one tests, timeline, and the 2026 shifts (AI-tool fluency, take-homes, communication weighting). *(Orientation / establish.)*
2. **The Recruiter & Hiring-Manager Screen** — what these early calls actually check (fit, motivation, resume, logistics, salary), how to prepare, red flags to avoid.
3. **SQL I — Querying, Filtering, and Joins** — the core query skills every technical round assumes.
4. **SQL II — Aggregation, Window Functions, and Problem Patterns** — the harder SQL that separates candidates.
5. **Statistics, Probability & Experimentation** — distributions, hypothesis testing, A/B tests, and the probability questions that recur.
6. **Spreadsheets for Analysts** — formulas, lookups, pivot tables, and data cleaning under time pressure.
7. **Python & pandas for Analysts** — loading, transforming, and summarizing data; the coding-round basics; **plus a dedicated section on working with AI tools responsibly** (when to trust vs. read a generated query).
8. **The Case / Business Round** — product sense, metrics, business framing (e.g. a Plan→Analyze→Construct→Execute structure), and the take-home case study on messy data.
9. **The Behavioral Round** — the STAR method, collaboration, decisions under ambiguity, handling setbacks, and influence without authority.
10. **Putting It Together — The Full Loop & Mock Interviews** — assembling every stage into realistic mock loops, thinking out loud, and self-scoring. *(Capstone / apply.)*

*(10 chapters. SQL gets two chapters because it is the largest technical component. AI-tool fluency is introduced in Chapter 1 and treated in a dedicated section of Chapter 7.)*

## The original-questions rule (hard editorial constraint)

Every practice question in this book is **written from scratch** in the style of a real interview question for the relevant stage. **No question is copied, paraphrased-to-evade, or lifted from any question bank, interview-prep site, company, or Glassdoor-style leak.** Questions are original scenarios (invented companies, invented datasets, invented metrics) designed to *exercise the same skill* real questions test. This is enforced in drafting and re-checked in Fact Check (Phase 4): any question that resembles a known source item is rewritten.

## Source strategy

**Primary source: Wikipedia** (per author's choice) — for the conceptual/definitional backbone of the technical content (e.g. *SQL*, *Join (SQL)*, *Window function*, *Statistical hypothesis testing*, *A/B testing*, *Probability*, *Pivot table*, *pandas (software)*).

**Interview-structure content** (stages, what each tests, 2026 trends) is grounded in the career-guide research recorded in `blueprint-trends-notes.md`, treated as editorial/secondary sourcing — appropriate for describing process, not for asserting technical facts.

**Source-tier note:** Wikipedia is a *tertiary* source, used for stable definitions and concept framing. Interview craft — question patterns, "what interviewers look for," difficulty calibration, and all practice questions — is **original editorial content the author supplies**, labeled as guidance, not fact. Phase 1 (Research) records sources per chapter; Phase 4 (Fact Check) verifies factual claims and audits the original-questions rule.

## Decisions (resolved with author, 2026-07-15)

- **Title:** *Data Analyst Interview Preparation.*
- **SQL dialect:** **MySQL** — all SQL examples and practice questions use MySQL syntax (e.g. `LIMIT`, backtick identifiers, MySQL date functions, MySQL 8.0 window-function support).
- **AI-tool fluency:** gets a **dedicated section in Chapter 7** (Python & pandas for Analysts) — using AI tools responsibly, when to trust vs. read a generated query — and is still introduced briefly in Chapter 1.

*No open `[NEEDS HUMAN INPUT]` items remain at the book.md level.*
