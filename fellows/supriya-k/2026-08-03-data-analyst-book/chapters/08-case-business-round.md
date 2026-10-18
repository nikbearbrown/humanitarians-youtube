# Chapter 8 — The Case / Business Round

Here the "right answer" matters less than how you **frame the problem, state assumptions, and land a recommendation.** This round asks whether you can think like a business partner, not just run a query.[^trends8]

> **What's tested here**
> Framing, assumptions, insight, and a defensible recommendation — **over raw correctness.**[^trends8] Evaluation spans ~7 dimensions: problem understanding, approach, reasoning, rigor, insight, storytelling, and communication.[^trends8]

## A structure to lean on

When a case opens, don't jump straight to the numbers. Use a visible framework — one common one is **PACE**:[^trends8]

- **Plan** — clarify the objective and success metric.
- **Analyze** — what data would you pull, what would you check.
- **Construct** — turn findings into an answer.
- **Execute** — the recommendation and next step.

PACE comes from Google's Advanced Data Analytics program; it's one common structure, not the only one — use it as scaffolding, not a script.[^pace]

## "How would you measure the success of X?"

A recurring question type. Answer with structure:
1. **Goal** — what "success" means for feature X.
2. **Primary metric** — the one number that captures it.
3. **Guardrails** — metrics that must *not* get worse.
4. **Segments & time frame** — for whom, over how long.

## The take-home case study

A 2026 norm at many companies: a real-feeling business question on **intentionally messy data** (usually 3–4 seeded quality issues), with a time cap (~3 hours) and a **presentation** afterward.[^trends8]

Budget it:
- **First 20 min:** read the prompt, define the question, scan the data for the seeded issues.
- **Middle:** clean, analyze, find the one insight worth presenting.
- **Last 30 min:** build the one-slide story — don't run out of time before you can *tell* it.

## Presenting findings

Lead with the **insight and recommendation**, then support it. One clear slide beats five busy ones. Expect pushback — defend with your assumptions, and concede what you didn't have time to check.

## Worked example

An invented ride-share company: *"Weekend rides have been flat for two months. What's going on?"*

- **Weak:** immediately querying random tables.
- **Strong:** "First, what's 'flat' — flat rides, or flat *relative to* growth elsewhere? I'd check whether it's demand (fewer riders opening the app) or supply (fewer drivers online), segment by city, and compare against weekday trend. My hypothesis is a supply shortage in two growth cities; I'd confirm with driver-online-hours before recommending driver incentives."

![PACE (Plan, Analyze, Construct, Execute) applied to the "weekend rides are flat" prompt.](images/08-case-business-round-fig-01.png)

## Exercises

1. **(Warm-up.)** List, in priority order, what an interviewer scores in a case round.
2. **(Representative.)** "How would you measure the success of a new in-app messaging feature?" Give a structured answer with a primary metric and two guardrails.
3. **(Stretch.)** Given an original messy-data take-home prompt, outline your 3-hour plan and the one-slide finding you'd aim for.

---

*Next:* the round that often decides a tie — behavioral.

[^trends8]: Case-round expectations, take-home norms, and evaluation dimensions from 2026 guides recorded in `blueprint-trends-notes.md`.
[^pace]: The PACE framework (Plan, Analyze, Construct, Execute) originates in Google's Advanced Data Analytics program (offered via Coursera). Verified 2026-07-15.
