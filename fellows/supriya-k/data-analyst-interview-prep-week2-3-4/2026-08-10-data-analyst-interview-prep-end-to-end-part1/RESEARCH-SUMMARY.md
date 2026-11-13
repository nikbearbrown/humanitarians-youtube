# Research Summary — "The Data Analyst Interview, End to End"

**Skill:** deep-explainer (5–7 min) · **Persona:** HAI / Bella · **Primary source:**
`books/data-analyst-interview-prep/chapters/01-interview-end-to-end.md` (Chapter 1,
"The Data Analyst Interview, End to End"), cross-referenced against the
"What's tested here" boxes opening Chapters 2–9 and the book's
`factchecks/MASTER_REPORT.md`.

This is the book's broadest claim: the interview is not a pile of questions,
it's a sequence of stages that each test something different, and 2026 added
three shifts that older prep resources haven't caught up to. Organized here
into the four acts the video will use.

## Act I — The process, start to finish (six stages)

1. Recruiter screen — 15–30 min, résumé/motivation/salary/logistics, no coding.
2. Hiring-manager chat — experience + genuine motivation + team fit.
3. Technical screen — SQL and often Python, live or take-home.
4. Statistics/experimentation round — distributions, hypothesis tests, A/B tests.
5. Case/business round — open business problem, increasingly a take-home + presentation.
6. Behavioral round — collaboration, ambiguity, recovering from setbacks.

Timing: "roughly five blocks" (HM chat and stats round sometimes folded into
neighbors) — most processes run **3–5 rounds over 2–6 weeks**; startups
compress to 2–3 rounds, larger/FAANG-adjacent companies run longer.
Source: Ch.1 body text, footnote `[^trends1]` → `blueprint-trends-notes.md`
(DataCamp, Exponent, BrainStation, KORE1, Interview Query) — explicitly labeled
in the book as a *process* description, not a technical-fact citation.

## Act II — What's tested where (the matrix)

| Stage | What's really scored |
|---|---|
| Recruiter screen | Basic fit, communication, logistics/salary alignment |
| Hiring-manager chat | Relevant experience, genuine motivation, team fit |
| Technical screen | Correct SQL/Python **and** how clearly you explain your logic |
| Statistics round | Sound reasoning under uncertainty; stating assumptions |
| Case/business round | Framing, assumptions, insight, a defensible recommendation — over raw correctness |
| Behavioral round | Collaboration, ownership, handling ambiguity, influence |

Key line (Ch.1, echoed as each chapter's own "what's tested here" box —
verified present in Ch.2, 3, 5, 8, 9): "In the technical screen, a query that
runs but that you can't explain is a weak answer: interviewers grade logic and
communication, not just whether the code executes." Preparing without this
matrix is how strong candidates give technically-correct answers that don't land.

## Act III — What changed by 2026 (three shifts)

All three sourced to Ch.1 footnote `[^trends1]` (same career-guide research
note as Act I's timing claim):

1. **AI-tool fluency is now assessed** — candidates may be asked how they use
   tools like ChatGPT or Cursor responsibly; interviewers want *judgment*
   (when to lean on the tool vs. read the generated query line by line,
   because AI output can pass a surface smell test and still be subtly
   wrong). Full treatment lives in Ch.7 (not repeated here — just the shift).
2. **Take-home case studies are common** — mid-to-large companies increasingly
   send a real-feeling business question on intentionally messy data, with a
   time cap and a presentation. Full treatment in Ch.8.
3. **Communication and business framing are weighted heavily** — later rounds
   reward stakeholder translation and judgment about *which question is worth
   answering*, not just the ability to compute.

## Act IV — Worked example: Maya's three-week plan (the payoff)

Maya: economics degree (8 months out), two stats courses, one intro-databases
course, a 3-month analytics bootcamp, interviews in 3 weeks. Can write a
`SELECT…JOIN` and build a pivot table; has never done a take-home case or told
a behavioral story that landed.

- **Week 1 — shore up the technical floor.** SQL is the most-tested skill and
  she's slow, so: SQL I/II + the statistics round, 90 min/day.
- **Week 2 — the parts she's never done.** Spreadsheets/pandas for
  maintenance; the real investment goes to the case round, including one full
  take-home.
- **Week 3 — integrate and rehearse.** Behavioral stories, then the full mock
  loop twice, self-scoring and re-drilling the two weakest stages.

The point stated explicitly in the book: the plan is **lopsided on purpose** —
most time on the stages that are both high-weight and low-confidence, not
spread evenly.

## Cross-reference (for continuity — not explained in this video)

| Act I stage | Full treatment lives in |
|---|---|
| Recruiter & HM screen | Ch. 2 |
| Technical (SQL) | Ch. 3–4 |
| Statistics/experimentation | Ch. 5 |
| Spreadsheets | Ch. 6 |
| Python/pandas + AI tools | Ch. 7 |
| Case/business | Ch. 8 |
| Behavioral | Ch. 9 (this book's video #1, the STAR-method explainer) |
| Full mock loop | Ch. 10 |

## Fact-check status

All claims in this video are process/trend descriptions traced to Ch.1's own
footnote (career-guide research, not re-verified as technical fact — the book
itself makes this distinction, see `factchecks/MASTER_REPORT.md` §"Definitional
claims" row for Ch.1/2/8/10). No statistics, code, or claims are invented for
this video. See `SOURCES-FACTCHECK.md` in this folder for the full trace.
