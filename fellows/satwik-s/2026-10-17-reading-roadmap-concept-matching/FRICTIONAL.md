# FRICTIONAL.md - Match It, Prove It, Skip It

**Fellow:** Satwik Reddy Sripathi
**Folder:** `2026-10-17-reading-roadmap-concept-matching`
**Date:** Oct 17, 2026 (week ending October 17, 2026)
**Type:** Project update
**Project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)

> An append-only log of the process behind this week's work: what I set out to do, where it resisted, what
> I decided, and what Claude contributed as an assistant. Not a performance review; a record of the real work.

## What I set out to do and why

Made the concept-matching questions usable as an optional, formative knowledge-check that can advance a student.

## What I did (my contribution)

- Researched how matching items and concept maps should be scored and chose relational per-pair partial credit (the method validity studies rank highest), scoring each prompt-to-option link independently, with a pass bar of 0.75 set above the roughly 4% chance of a lucky four-by-four match.
- Set and implemented the three constraints: the check is opt-in (a student gets the roadmap without it), a pass can advance a student (prune-after-evaluate), but it is recorded as a knowledge-check and never as a grade.
- Made the question type usable everywhere: a scorer behind 12 passing tests, an importer that preserves the full matching structure, the gate branch, and an opt-in self-check in the demo app, so 178 matching items are now live and 0 are dropped (was 186).
- Diagnosed the 8 malformed items as a question-bank defect (not a textbook issue, so re-cloning could not fix it), recovered all 8 into a separate review file for faculty (2 high, 6 medium confidence), and confirmed the textbook and question bank were both current.
- Wrote the week's research report and directed the Brutalist weekly video end to end: the premise and beat sheet, the narration script, the visual plan, the 4K render review, and the PROOF production-gate check before I accepted it.

## Where it resisted, and what I decided

- The matching answers are mappings, not single letters, so the gate was dropping all of them; I chose a principled scoring method rather than discard a whole question type.
- I had to decide how a formative check can still advance a student without being a grade, and settled on the opt-in, knowledge-check framing.

## What Claude contributed (assistant)

- Implemented the scorer, the importer, the gate branch, and the app self-check to my design, with the test suite.
- Rendered the demo screenshots and drafted the report.
- Rendered the video scenes and the narration audio, and drafted figures, from my beat sheet and visual plan.

Claude acted as an implementation assistant under my direction. The research questions, the framing, the
design decisions, the interpretation of results, the faculty collaboration, and the final acceptance of
every output were mine.

## Accepted / changed / rejected

I accepted relational partial credit with a formative, opt-in framing; I rejected all-or-nothing scoring and any 'graded test' framing; I kept the 8 recovered items separate pending faculty confirmation.
