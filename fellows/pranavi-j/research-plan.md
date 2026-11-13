# Research plan — requested period (1 Nov 2026 – 20 Feb 2027)

Continuing the established cadence: two Brutalist videos a week (one real Project 29 engineering
fix, one general AI/STEM explainer), each in 4K 16:9 + native 4K 9:16, with `FACTCHECK.md`,
`SOURCES.md`, a `BUILD-LOG.md`, and — starting this period — a contemporaneous `FRICTIONAL.md` per
work folder, written as the work happens rather than reconstructed afterward.

## Project 29 (`mycroft`) — specific next items

The original hardening plan was 4 layers: (1) harden the existing n8n workflow, (2) a formal eval
benchmark, (3) an LLM second-pass re-scoring layer, (4) spaCy NER entity disambiguation. Layer 1 is
substantially complete (A1–A7, B1–B6, source classification improvements). Layer 2's LLM
re-scoring/fallback-classification pieces are shipped (C1/C2, B2 addendum). Three concrete items
remain:

1. **`Regulatory_QA`'s `SourceFeed` enum rejects valid dynamic classifier output** — identified and
   reproduced live this week (`SourceFeed('Federal Register - Department of Labor')` raises
   `ValueError`), not yet fixed. The route parameter (`routers/feeds.py:103`) is typed against a
   fixed 5-value enum, but `identifySource()` can now emit open-ended `Federal Register - {creator}`
   labels; `crud.py` already treats `source_feed` as a plain string, so the fix is a narrow type
   change, not a rewrite. Planned for the first week of the requested period.
2. **Layer 2 formal eval benchmark** — planned since the original `FINDINGS.md` roadmap
   ("freeze the baseline on the post-B1 pipeline"), never actually built. The two named C1
   false-positive patterns (Medicare "Emergency Medical Treatment", Nasdaq "Immediate
   Effectiveness") are ready-made labeled cases; needs a real labeled set beyond those two to be a
   genuine benchmark rather than a confirmation of what's already known.
3. **Layer 3 — spaCy NER entity disambiguation** — the fourth and final layer of the original plan.
   Zero scaffolding exists in the repository. Scoping this is a requested-period goal, not
   necessarily a completed deliverable within it; the engineering fixes above take priority.

## STEM explainer series

Continuing the same framework-first format (a reusable rubric, a worked example, a falsifiability
stress-test, a scaffolded audit task), fully generic with no real model/vendor named or
benchmarked, matching the house style established across the first 9 weeks (hallucination,
tokenization, lost-in-the-middle, chain-of-thought faithfulness, and others). Topic selection
continues week to week, generally following whatever mechanism underlies that week's real
engineering work when there's a natural connection, and otherwise covering adjacent reliability/
epistemics topics in AI systems (e.g. calibration, in-context learning limits) that haven't yet
been covered.

## Process changes for this period

- `FRICTIONAL.md` written contemporaneously in every new work folder from day one — closing the
  gap flagged in this renewal request, where none of the prior 18 folders had one until
  reconstructed retrospectively as part of this submission.
