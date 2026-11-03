# Satwik Reddy Sripathi

**Role:** Research Data Scientist<br>
**Project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)<br>
**Group:** Medhavy team<br>
**GitHub:** [@SatwikReddySripathi](https://github.com/SatwikReddySripathi)<br>
**Supervision:** Prof. Nik Bear Brown and Dr. Evin Gultepe<br>
**Last updated:** October 26, 2026

> This folder contains my work as an HAI fellow. I am building a personalized, project-driven reading-roadmap
> system for cancer-nanomedicine trainees and producing a weekly Brutalist video documenting each step.

## Executive Summary

I am building an end-to-end system that turns a student's research-project description into an ordered,
dependency-sequenced reading roadmap over a 38-chapter cancer-biology textbook. The governing idea is that
this is a reordering problem, not a retrieval problem: sections are selected by relevance and then sequenced
by learning dependency under a graph constraint, so the system can say "read A before B," which a similarity
ranker cannot. Over this period I designed the four-stage pipeline (section extraction, metadata tagging,
a prerequisite dependency graph, and personalized sequencing), added a test-to-advance assessment gate that
evaluates a prerequisite before trusting it, reworked the prerequisites into three tiers on faculty feedback,
attached the collaborators' question bank, and made the concept-matching questions usable as an optional,
formative knowledge-check. The work is a research prototype supporting a methods paper, built for
reproducibility and faculty review. Claude assisted with implementation under my direction; the research
direction, design decisions, interpretation, and faculty collaboration were mine.

## Quick Review

- [Renewal request (November 2026)](renewal-requests/2026-10-25-november-renewal.md)
- [Weekly hours and evidence](weekly-hours/)
- [Research plan](research-plan.md)
- [Sources used](sources.md)
- Video evidence: [Google Drive folder](https://drive.google.com/drive/folders/1-1lr-yszPd0xFqds04MtVUlilBkt0wtK)
- System repository: https://github.com/SatwikReddySripathi/personalized-roadmap (private)
- Supervision: Prof. Nik Bear Brown and Dr. Evin Gultepe

## Folder Guide and Evidence

| Folder | Date | Type | Description |
|---|---|---|---|
| [2026-07-28-personalized-reading-roadmap-introduction](2026-07-28-personalized-reading-roadmap-introduction/) | Jul 28, 2026 | Project update | Personalized, Project-Driven Reading Roadmaps (Introduction): Introduced the project and the framing that governs every design decision: this is a reordering problem, not a retrieval problem. |
| [2026-08-09-personalized-roadmap-ablationstudy1](2026-08-09-personalized-roadmap-ablationstudy1/) | Aug 9, 2026 | Project update | Does the Fancy Part Earn It? A Tagging Ablation: Tested whether the LLM metadata tagging earns its place against a deterministic baseline. |
| [2026-08-17-reading-roadmap-ablation-aug17](2026-08-17-reading-roadmap-ablation-aug17/) | Aug 17, 2026 | Project update | What an Ablation Can (and Can't) Decide - Full-Book Tagging: Scaled the tagging ablation to the whole book and stated honestly what it decides. |
| [2026-08-23-personalized-roadmap-goldenset](2026-08-23-personalized-roadmap-goldenset/) | Aug 23, 2026 | Project update | Which One Is Right? Scoring Taggers Against a Gold Set: Built a gold standard so tagger quality could be judged against truth, not just against another tagger. |
| [2026-08-29-reading-roadmap-reason-or-retreive](2026-08-29-reading-roadmap-reason-or-retreive/) | Aug 29, 2026 | Project update | Does It Reason, or Just Retrieve?: Showed that the graph constraint, not similarity, is what makes this reasoning rather than retrieval. |
| [2026-09-05-reading-roadmap-ober-is-it-any-good](2026-09-05-reading-roadmap-ober-is-it-any-good/) | Sep 5, 2026 | Project update | How Would We Know It's Any Good?: Turned the vague question of quality into concrete, measurable evaluation criteria. |
| [2026-09-11-reading-roadmap-test-before-building](2026-09-11-reading-roadmap-test-before-building/) | Sep 11, 2026 | Project update | Test Before You Advance: Designed the test-to-advance gate: never assume prior knowledge, evaluate first, prune on pass, descend on fail. |
| [2026-09-18-reading-roadmap-prereqs-creation](2026-09-18-reading-roadmap-prereqs-creation/) | Sep 18, 2026 | Project update | Read the Book, Draft the Graph: Built the prerequisite dependency graph from the textbook as a reviewable draft for faculty. |
| [2026-09-25-reading-roadmap-evaluate-then-advance](2026-09-25-reading-roadmap-evaluate-then-advance/) | Sep 25, 2026 | Project update | Evaluate, Then Advance: Ran the full evaluation pipeline: the MCQ gate with item pools and prune-after-evaluate. |
| [2026-10-02-reading-roadmap-mcq-generation](2026-10-02-reading-roadmap-mcq-generation/) | Oct 2, 2026 | Project update | A Question for Every Step: Produced a reviewable question for every step so the gate always has something real to ask. |
| [2026-10-10-reading-roadmap-threetier-plan](2026-10-10-reading-roadmap-threetier-plan/) | Oct 10, 2026 | Project update | Three Tiers, One Plan: Rebuilt the prerequisites into three tiers on faculty feedback, and attached the question bank. |
| [2026-10-17-reading-roadmap-concept-matching](2026-10-17-reading-roadmap-concept-matching/) | Oct 17, 2026 | Project update | Match It, Prove It, Skip It: Made the concept-matching questions usable as an optional, formative knowledge-check that can advance a student. |
| [2026-10-25-prereq-recall-gap](2026-10-25-prereq-recall-gap/) | Oct 25, 2026 | Project update | The Links That Weren't There: Diagnosed why the later, applied chapters came out with almost no required prerequisites, and built a content-grounded fix. |

## Voice Choice

**Voice:** Kokoro af_bella ("Bella")
**Channel:** @HumanitariansAI
**Series kicker:** Brutalist weekly research report
**Register:** Pragmatist / skeptical-explainer

## Completed Results

- A working four-stage roadmap pipeline (section extraction -> metadata -> prerequisite graph -> personalized
  sequencing) on the full 38-chapter textbook, built for reproducibility and faculty review.
- A test-to-advance assessment gate (prune-after-evaluate, descend-on-fail; hard vs soft prerequisites).
- A three-tier prerequisite graph (required / recommended / curious), acyclic, with a plain-language
  reading-order for faculty and an audit of a tier-aware transitive reduction that removed inherited redundancy.
- The collaborators' question bank mapped to sections, and concept-matching made usable as an optional,
  formative knowledge-check (relational partial-credit scoring, opt-in, never a graded test).
- 13 Brutalist weekly research videos documenting the work; masters on [Google Drive](https://drive.google.com/drive/folders/1-1lr-yszPd0xFqds04MtVUlilBkt0wtK).
- Reproducibility throughout: pinned models, saved intermediate artifacts, confidence/provenance/needs_review,
  and prompts kept in-repo.

## Next Steps

- Strengthen the later-chapter prerequisites (faculty feedback: therapy/disease chapters under-connected to
  core biology) and bring a corrected required-prerequisite proposal to faculty.
- Complete the faculty review loop on the three-tier prerequisites and the recovered concept-matching items.
- Wire the verified tiers and questions into the gate so it runs on the approved structure.
- Continue generating one Brutalist weekly research video per week.
- Publish a research paper

## Frictional Log Policy

Every work subfolder has its own `FRICTIONAL.md` beside the work it describes. Each log records what I tried
and expected, where it resisted, what I did next, what Claude or another person contributed, and what was
accepted, changed, or rejected. Each folder also carries a `REPORT.md` stating what the video covers, why
that topic that week, and its limits. The logs are not graded and are not performance reviews.

---
