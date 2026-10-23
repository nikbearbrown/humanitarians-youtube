# Frictional log — 2026-10-09

**Week 10 · documentation · Auditing my own project against its plan, and losing**

A frictional log is not a status report. It records where the work pushed back, what I did
about it, and what I still do not know. Every number here is traceable to `proposal.md`,
`system_architecture.md`, `data_architecture.md` or `docs/worklog.md`.

---

## What I was working on

The final week. The code was finished; what was missing was everything that lets another
person understand it without me sitting next to them — a proposal, an architecture, a data
model, a demo.

## What I tried, and what I expected

The plan names six documents for this week. My expectation was that most of them existed in
some form and needed tidying, because I had been writing documentation continuously for ten
weeks.

So rather than assume, I checked each one against the last commit with `git show HEAD:<path>`.

## Where it resisted, and what I did next

**Three of the six did not exist at all.** Not thin, not stale — absent. `proposal.md`,
`system_architecture.md` and `data_architecture.md` had never been written. **The audit found
them; the plan did not predict them.**

I wrote all three from the project's own measured figures and the decisions already recorded in
the worklog, rather than from the plan's prose — 126, 155 and 163 lines. The architecture
document is the one I would keep if I could keep one: it states where the graph framework earns
its place and where it is ceremony (most of this project is batch ETL, and batch ETL should not
be a state machine), and it names the exactly two places a language model sits, neither of
which touches a number.

**Then the one that actually stung.** The plan says the published documents must cite the
prior-art literature honestly. It is emphatic about it — this data source is "commercially
exploited" and "academically mature", and claiming novelty "would not survive a literature
review".

I grepped `docs/findings.md` and `docs/entity_resolution.md` for Caplight, Gornall,
Strebulaev, Agarwal, Chernenko and Kwon.

**Zero. Not thin coverage — zero matches, in both files.** A requirement stated plainly in my
own plan, met zero times across ten weeks, and I had not noticed because I never checked.

It is in three places now (9, 8 and 5 mentions), and in one of them it is **load-bearing rather
than decorative**. Gornall & Strebulaev (JFE 2020) established that funds write up *every*
share class to the latest round price. That is reproduced on this cohort, and it is the reason
dispersion is measured at company level with the share class recorded rather than within-class
only — it overturned an earlier draft's rule. The other citations frame the contribution as
open infrastructure rather than discovery, which is the honest framing.

**`docs/findings.md` had stopped at week 7**, and I extended it **through its generator rather
than by hand**. It is a generated artifact, so editing it directly would make the document and
the data disagree on the next run. `scripts/analyze.py` gained a section 6 (the Form D × N-CSR
corroboration, with its denominator caveat) and a section 7 (the literature). Regenerating
reproduces them.

**`DATABASE_SETUP.md` was stale in a way that read as complete** — its schema block listed only
the four week 2 core tables while the database held fifteen. I had found that a week earlier
and deliberately deferred the consolidated listing to this week rather than half-doing it. Now
all fifteen with row counts, verified against `information_schema`, plus the four LangGraph
checkpoint tables named as **not** belonging to this project's schema.

**The plan says to put the catalogue entry in `n8n_Workflows/README.md`. No such directory
exists in this repository** — the path refers to a sibling repo. Rather than invent a top-level
directory to satisfy a path, I wrote it as `n8n/README.md` beside the workflow it documents,
carrying a paste-ready catalogue row, and stated the deviation in the file itself so it is
visible rather than silently resolved.

## What Claude contributed, and what I did with it

Claude drafted all three architecture documents and `scripts/demo.py`.

**The demo is where I overruled the plan, and I think correctly.** The plan says "record a
demo". I wrote a script instead — five acts, every figure queried live, so a transcript that
disagrees with the database is a bug rather than an old file. A recording is true on the day it
was made; this re-runs.

**Act II is read-only on purpose, and that was the real decision.** The obvious demo makes a
review-queue decision on camera, because it is the most visually interesting thing the system
does. It also clears a human gate for the sake of a screenshot, which is precisely the failure
the gate exists to prevent. So Act II *displays* a decision a named human already recorded and
makes no new one. Act I likewise shows the ingest reconciliation rather than re-downloading 6
GB — what is worth seeing is that nothing was dropped for being awkward, not the download.

**One defect in the figures, caught by reading the rendered PNGs rather than the code.** The
layout audit passed all four. But the demo figure's caption read "15 tables read" when the demo
reads a subset — reworded to "15 project tables, by layer". And the provenance figure's closing
lines sat 10 pixels from the source line, which the geometric audit does not flag because both
elements are inside the canvas.

**One thing the reel got narrower than its own source figure, and I let the correction stand.**
`w12-priorart.png` tabulates three documents at BEFORE 0; the reel says two. `proposal.md`
carries `existed: false` — its zero is an **absent file**, not a document that failed the
requirement. The figure's own caption already agrees ("in either published document"); its
table does not. That is a real distinction and the narrower claim is the right one.

## What I understand now, and what I still do not

**Understood.** The documents I had not written were the ones that explain *why*, not *what* —
ten weeks of worklog entries record every decision and none of them constitutes an
architecture. An audit against the last commit finds things that memory does not, which is why
I ran `git show HEAD` instead of trusting my own recollection of what existed. And a
requirement can sit at zero for the entire life of a project if nobody ever runs the check.

**What I still do not know, and the project ends with this open.** The plan's Phase 1 exit
criteria are six; five pass. The sixth — reproducing the Anthropic move to ~$589 — **cannot be
met with the current archive**, because the 5/29 and 5/31 period ends sit in 2026Q3 and the SEC
has not published it. That is the same blocker as the Cerebras event study. Both harnesses are
built and tested against injected data and both complete themselves when `2026q3_nport.zip`
lands, roughly November 2026.

The accurate claim is not "complete". It is: **the eleven-week build is delivered, with two
verification items blocked on an SEC publication rather than on the work.** That is a weaker
headline and a checkable one.

**Also still open:** 314 of 322 golden-set labels unattested; the 28 `%COHERE%` canary holdings
still inside the shipped universe layer; the commentary running on a substitute model because
Groq retired the one the plan named; the live EDGAR path never built; and **milestone PRs
1, 2 and 3 not opened** — git is mine and I have not run it.
