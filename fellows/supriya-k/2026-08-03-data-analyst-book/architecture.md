# architecture.md — Data Analyst Interview Preparation

*Blueprint Phase 2 of 4: learning outcomes, sequencing model, three-act arc, assessment plan. Derived from `book.md` and `vision.md`.*

---

## Sequencing model: **the candidate's real timeline**

Chapters follow the order a candidate *actually experiences the interview loop* — orientation, then recruiter screen, then the technical rounds (in the order they typically appear and build on each other), then the case/business round, then behavioral, then a capstone that reassembles the whole loop.

**Why this model over a difficulty ramp or topic taxonomy:** the book's central argument is that candidates fail because they don't understand the *process*. Sequencing by the process itself teaches the mental model structurally — by the time the reader finishes, they have walked the loop once, in order. Within the technical block, SQL precedes stats/spreadsheets/Python because SQL is the most-tested and most-assumed skill; each technical chapter is self-contained so a reader can also jump to a weak spot.

## Three-act arc

- **Act I — Establish (Ch. 1–2):** the map. What the whole process is, what each stage tests, and the first live stage (recruiter/HM screen). Reader leaves with the mental model the rest hangs on.
- **Act II — Build (Ch. 3–7):** the technical toolkit, one round at a time — SQL I, SQL II, statistics/experimentation, spreadsheets, Python/pandas (+ AI tools). Each chapter = one testable skill, its evaluation pattern, and original reps.
- **Act III — Apply (Ch. 8–10):** the judgment rounds and integration — the case/business round, the behavioral round, and a capstone full-loop mock. Reader assembles everything under realistic conditions.

## Per-chapter learning outcomes (measurable, with Bloom's level)

Each outcome is phrased "the reader can …" and tagged with a Bloom's level: *Remember / Understand / Apply / Analyze / Evaluate / Create.*

**Ch. 1 — The Data Analyst Interview, End to End**
- Describe the standard end-to-end interview process and name what each stage evaluates. *(Understand)*
- Explain the 2026 shifts (AI-tool fluency, take-home case studies, communication weighting) and why they change how to prepare. *(Understand)*
- Build a personal prep plan that allocates effort across stages by their weight and the reader's gaps. *(Create)*

**Ch. 2 — The Recruiter & Hiring-Manager Screen**
- Identify what a recruiter screen and a hiring-manager chat each check. *(Understand)*
- Apply a structure to answer "tell me about yourself," motivation, and logistics/salary questions. *(Apply)*
- Evaluate a sample screen answer and diagnose why it helps or hurts. *(Evaluate)*

**Ch. 3 — SQL I: Querying, Filtering, and Joins**
- Write MySQL queries using `SELECT`, `WHERE`, `GROUP BY`, and the join types. *(Apply)*
- Choose the correct join for a described relationship and predict its row output. *(Analyze)*
- Explain query logic aloud the way a technical screen expects. *(Understand)*

**Ch. 4 — SQL II: Aggregation, Window Functions, and Problem Patterns**
- Write MySQL queries using aggregation, subqueries/CTEs, and window functions (`ROW_NUMBER`, `RANK`, running totals). *(Apply)*
- Recognize the recurring SQL problem patterns (top-N-per-group, running totals, gaps/islands, deduplication) and map a new question to one. *(Analyze)*
- Critique a query for correctness and efficiency. *(Evaluate)*

**Ch. 5 — Statistics, Probability & Experimentation**
- Define and apply core concepts: distributions, sampling, hypothesis testing, p-values, confidence intervals. *(Apply)*
- Reason through a probability question and an A/B-test design out loud, stating assumptions. *(Analyze)*
- Evaluate a flawed experiment or a misused statistic and explain the error. *(Evaluate)*

**Ch. 6 — Spreadsheets for Analysts**
- Apply core spreadsheet skills: formulas, lookups (`VLOOKUP`/`INDEX-MATCH`/`XLOOKUP`), pivot tables, conditional aggregation. *(Apply)*
- Clean a small messy dataset under time pressure, naming the quality issues found. *(Analyze)*
- Choose spreadsheet vs. SQL/Python for a given task and justify it. *(Evaluate)*

**Ch. 7 — Python & pandas for Analysts (+ AI tools)**
- Apply pandas to load, filter, group, join, and summarize a dataset. *(Apply)*
- Solve a small data problem end-to-end in pandas and explain the approach. *(Apply)*
- Evaluate AI-generated analysis code — decide when to trust it and when to read it line by line — and articulate a responsible-use stance for an interviewer. *(Evaluate)*

**Ch. 8 — The Case / Business Round**
- Explain what a case/business round grades (framing, assumptions, insight, recommendation) over mere correctness. *(Understand)*
- Apply a structure (Plan → Analyze → Construct → Execute) to a business/metrics case and a take-home on messy data. *(Apply)*
- Create a concise findings presentation with a defensible recommendation. *(Create)*

**Ch. 9 — The Behavioral Round**
- Explain what behavioral panels evaluate (collaboration, ambiguity, ownership, influence). *(Understand)*
- Construct evidence-backed STAR stories mapped to the competencies being scored. *(Create)*
- Evaluate a behavioral answer against the competency it targets. *(Evaluate)*

**Ch. 10 — Putting It Together: The Full Loop & Mock Interviews**
- Assemble the stage skills into a simulated end-to-end loop. *(Create)*
- Self-score a mock performance against each stage's evaluation pattern. *(Evaluate)*
- Design a final-week prep plan from the self-scoring. *(Create)*

## Assessment plan

Assessments are decided here and generated later as editions (`conductor/editions/`). Because this is a *prep* book, practice is the spine, not an add-on.

| Assessment | Status | Applies to | Notes |
|---|---|---|---|
| **Original practice questions (in-chapter)** | **Needed** | Every chapter (2–10) | The core of the book. Real-interview *style*, all original. Each stage chapter carries a graduated set (warm-up → representative → stretch). |
| **Worked solutions / model answers** | **Needed** | Every chapter (2–10) | Each practice question has a worked solution or model answer that also shows *how it would be evaluated*. |
| **"What's tested here" callouts** | **Needed** | Every stage chapter | Not an exercise, but a required structural block naming the evaluation pattern before practice. |
| **Full mock-interview loop** | **Needed** | Ch. 10 (capstone) | An end-to-end simulated loop with self-scoring rubrics per stage. |
| **Chapter quizzes (checks for understanding)** | **Desired** | Ch. 1, 3–7 | Short recall/understanding checks for the conceptual chapters. Generated as an edition post-spine. |
| **Flashcards / Anki deck** | **Desired** | Whole book | For definitions and recurring patterns (SQL patterns, stat terms). Generated as an edition post-spine. |
| **Take-home case pack** | **Desired** | Ch. 8 | One or two original messy-data take-home prompts with a grading rubric. |
| **Exam bank** | **Out of scope** | — | Not needed for a prep workbook. |
| **Canvas / LMS modules** | **Out of scope** (this version) | — | Possible later if used in a course. |

**Difficulty calibration:** every practice set is leveled *warm-up → representative → stretch*, and each question is tagged with the stage it belongs to and the skill/pattern it exercises, so the reader always knows what they're rehearsing.
