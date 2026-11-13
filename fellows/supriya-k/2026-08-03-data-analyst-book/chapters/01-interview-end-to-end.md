# Chapter 1 — The Data Analyst Interview, End to End

Most people prepare for a data analyst interview by collecting questions. They bookmark a SQL practice site, download a statistics cheat sheet, and skim a list of "top 50 behavioral questions." Then they walk into the process and discover that the interview is not a pile of questions — it is a **sequence of distinct stages, and each stage is testing something different.** The recruiter screen is not a smaller version of the technical round. The case round is not graded like the SQL round. Candidates who don't know this ace the SQL screen, then freeze when the case interviewer asks what metric they'd even look at.

This chapter gives you the map. By the end of it you'll be able to name every stage of a real data analyst interview and say what each one is actually evaluating. You'll also build a prep plan that spends your time where your gaps are — not where the internet's questions happen to pile up.

## The process, start to finish

A typical entry-level data analyst interview runs as roughly five blocks, in this order:

1. **Recruiter screen** — a 15-to-30-minute call covering your résumé, your motivation, salary expectations, and logistics. No coding.
2. **Hiring-manager chat** — a conversation about your direct experience and why you want this role and team.
3. **Technical screen** — SQL and often Python, delivered as a live shared editor or a take-home with a messy dataset.
4. **Statistics / experimentation round** — reasoning about distributions, hypothesis tests, and A/B tests.
5. **Case / business round** — an open business or metrics problem, increasingly a take-home you then present.
6. **Behavioral round** — how you collaborate, handle ambiguity, and recover from setbacks.

(That's "roughly five blocks" because the hiring-manager chat and the statistics round are sometimes folded into neighbors.) Most processes run **three to five rounds over two to six weeks**; startups compress to two or three, while larger and FAANG-adjacent companies can run longer.[^trends1]

![The interview stage by stage: each stage's focus and typical duration, left to right.](images/01-interview-end-to-end-fig-01.png)

## What's tested where

One thing separates candidates who prep well from candidates who just prep hard: **each stage scores a different thing.** Learn this matrix before anything else.

| Stage | What the interviewer is really scoring |
|---|---|
| Recruiter screen | Basic fit, communication, do the logistics/salary line up |
| Hiring-manager chat | Relevant experience, genuine motivation, team fit |
| Technical screen | Correct SQL/Python **and** how clearly you explain your logic |
| Statistics round | Sound reasoning under uncertainty; stating assumptions |
| Case / business round | Framing, assumptions, insight, and a defensible recommendation — over raw correctness |
| Behavioral round | Collaboration, ownership, handling ambiguity, influence |

In the technical screen, a query that runs but that you can't explain is a weak answer: interviewers grade logic and communication, not just whether the code executes.[^trends1] In the case round, the "right number" matters less than whether you framed the problem well. Preparing without this matrix is how strong candidates give technically-correct answers that still don't land.

## What changed by 2026

Three things changed how these interviews run, and scattered older resources haven't caught up:[^trends1]

- **AI-tool fluency is now assessed.** You may be asked how you use tools like ChatGPT or Cursor responsibly. They want to see *judgment*: when to lean on the tool, and when to read the generated query line by line — because AI output can pass a surface smell test and still be subtly wrong. (Chapter 7 has a full section on this.)
- **Take-home case studies are common.** Mid-to-large companies increasingly send a real-feeling business question built on intentionally messy data, with a time cap and a presentation. (Chapter 8 rehearses the format.)
- **Communication and business framing are weighted heavily.** The later rounds reward stakeholder translation and judgment about *which question is worth answering* — not just the ability to compute.

## How to use this book

The chapters follow the order you'll actually experience the interview: orientation (this chapter), the recruiter screen, the technical rounds (SQL, statistics, spreadsheets, Python), the case round, the behavioral round, and finally a full mock loop. Each stage chapter opens with a **"What's tested here"** box — the same idea as the matrix above, zoomed in — and then drills that skill with practice questions.

Two things about those practice questions. First, they are **leveled**: warm-up, then representative, then stretch, so you always know how hard the rep is. Second, **every question in this book is original** — invented companies, invented datasets, invented metrics — written to exercise the same skills real interviews test. Nothing here is copied from a question bank. That means you can trust the practice to build skill rather than memorized answers.

## Worked example: a three-week prep plan

Meet Maya. She graduated eight months ago with an economics degree (two statistics courses, one intro-to-databases course), finished a three-month analytics bootcamp, and has interviews starting in three weeks. She can write a `SELECT ... JOIN` and build a pivot table. She has never done a take-home case or told a behavioral story that landed.

A plan that spends time by *stage weight and personal gap* — rather than evenly — might look like this:

- **Week 1 — shore up the technical floor.** SQL is the most-tested skill and Maya is slow, so: SQL I and II (Chapters 3–4), 90 minutes a day, plus the statistics round (Chapter 5) she half-remembers.
- **Week 2 — the parts she's never done.** Spreadsheets and pandas (Chapters 6–7) for maintenance, but the real investment goes to the case round (Chapter 8) — the format she's never seen — including one full take-home.
- **Week 3 — integrate and rehearse.** Behavioral stories (Chapter 9), then the full mock loop (Chapter 10) twice, self-scoring each stage and re-drilling her two weakest.

Notice the plan is *lopsided on purpose.* Maya isn't spending equal time on each stage; she's spending most on the stages she's weakest at and that count most.

![Maya's three-week plan, with time blocks sized by weakness and stage weight.](images/01-interview-end-to-end-fig-02.png)

## Exercises

**1. (Warm-up.)** Match each prompt to the stage it belongs to:
(a) "Walk me through your résumé and what you're looking for." (b) "Write a query to find the top 3 products by revenue." (c) "How would you measure whether a new feature succeeded?" (d) "Tell me about a time you disagreed with a teammate." (e) "Is this A/B test result trustworthy?" (f) "Why do you want to work here specifically?"

**2. (Representative.)** Read this short profile: *"Confident on SQL and Excel from a data internship; has never done a case study or a structured behavioral round; interviews in four weeks."* Name the **two stages** this person should invest the most in, and explain why in one sentence each.

**3. (Stretch.)** Using the three-week template above, write your **own** prep plan: self-assess each stage as strong / okay / weak, then allocate your available hours so the most time goes to high-weight, low-confidence stages.

---

*Next:* before any code, the interview starts with a human on the phone. Chapter 2 takes apart the recruiter and hiring-manager screen — what those early calls are really checking, and how to pass them without over-sharing or freezing on the salary question.

[^trends1]: Interview-structure and 2026-trend claims in this chapter are drawn from current data-analyst interview guides (DataCamp, Exponent, BrainStation, KORE1, Interview Query), recorded in `blueprint-trends-notes.md`. These describe the hiring *process*; they are not used as authorities for technical facts.
