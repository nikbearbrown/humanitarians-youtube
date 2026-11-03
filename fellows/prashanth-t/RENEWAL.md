# Renewal request — Prashanth Talwar

**Current agreement:** 2 Sep — 30 Sep

**Requested period:** 1 Oct — 31 Oct

**Project:** Madison — Jungian Brand Archetype Detector

**Repository:** _to be confirmed_

**Branch:** not yet created. GitHub push access was granted on 28 Sep, which is
when the first files went up. Code changes will land on a branch from the next
sprint onward; the work to date is design and documentation, which is why it
appears as beat sheets and build records rather than application code.

## What the current period produced

Four weeks from a standing start: onboarding, a scoped project, a technical
design, and four produced explainers. **Nothing is built and no accuracy figure
exists** — that is stated on screen in both project videos and is the honest
position going into the renewal.

* **A scoped project.** Ruler archetype chosen as the first target, for luxury
  branding, with the deliberate constraint of proving the pipeline end to end on
  one archetype before touching the other eleven.
* **Three design commitments fixed**, and they are what separate this from the
  existing archetype tools: read what a brand actually publishes rather than a
  self-reported brief; return a primary **and** a secondary archetype with the
  inconsistency between them named; end in application — messaging pillars, tone
  guardrails, and the archetype's shadow.
* **A concrete technical design** across three parts. Inputs: published website
  copy, social captions, tagline, and competitor copy for contrast, never a
  questionnaire. Scoring: every trait score carries the quoted line of copy that
  earned it, so a reviewer can audit any number rather than trusting a total.
  Evaluation: a small hand-labelled brand set scored first, so that reading brand
  voice can be told apart from matching surface keywords.
* **The blocker named precisely** rather than left vague — sample data: what
  format the samples arrive in, roughly how many brands are needed, and who
  gathers them. Evaluation cannot start without it, and no quality figure is
  quotable until it does.
* **Four explainers produced** on the Brutalist pipeline, two on the project and
  two on STEM topics, each shipping with its beat sheet, a claim-by-claim
  factcheck, a provenance note marking what is constructed or illustrative rather
  than measured, and a dated frictional log.

## Evidence

| Work | Commit | Drive | Video | Log |
|---|---|---|---|---|
| Madison — scoping update | [`567602b`](https://github.com/nikbearbrown/humanitarians-youtube/commit/567602b88a8b005dda6b3c18f9c24eaab47753cb) | [folder](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) | [watch](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) | [log](madison-archetype-progress/FRICTIONAL.md) |
| Madison — technical design | [`9fd2e15`](https://github.com/nikbearbrown/humanitarians-youtube/commit/9fd2e15229bbf878c37c91f07d8d58193ee1b639) | [folder](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) | [watch](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) | [log](madison-archetype-progress-week2/FRICTIONAL.md) |

Beat sheets, shotlists, factchecks, sources, gate reports and rebuild prompts for
each piece of work are in that work's folder under
[`fellows/prashanth-t/`](.).

## STEM Topics

| Week | Topic | Video | Drive | Log |
|---|---|---|---|---|
| 14–18 Sep | How LLM function calling works | [video](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) | [drive](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) | [log](llm-function-calling/FRICTIONAL.md) |
| 21–25 Sep | How memory works in an AI agent | [video](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) | [drive](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) | [log](agent-memory/FRICTIONAL.md) |

Weekly hours: [HOURS.md](HOURS.md). Weekly frictional logs: one per work folder,
listed in [README.md](README.md).

## Plan for the requested period

Five sprints across October, in order, each gating the next. The sequence is
deliberate: the sample data has to exist before evaluation means anything, and
evaluation has to run before any scoring claim is worth making. The period is
scoped to proving one archetype, not to breadth.

1. **Unblock the sample data (1–3 Oct).** Settle format, approximate brand count,
   and who assembles it. Begin the hand-labelled set — brands scored by a human
   first, before the detector is pointed at them, so the labels cannot be
   influenced by its output.
2. **Design review into an SDD (6–10 Oct).** Run the technical design through
   review and produce a proper software design document. That is what the build
   is written against, rather than building straight from a video script.
3. **Build the Ruler scorer (13–17 Oct).** Implement inputs and scoring against
   the SDD, on a branch in the project repository. Every trait score must carry
   its evidence quote from the first commit — auditability is a build requirement
   here, not a later feature.
4. **Evaluate against the hand-labelled set (20–24 Oct).** Report agreement per
   brand, and separately for the hard cases — brands that read Ruler without
   using the obvious vocabulary. **If it only agrees where the obvious keywords
   appear, that is the finding and it will be reported as such**, rather than
   tuning the scorer until it agrees with the labels.
5. **Decision, and the application layer (27–31 Oct).** Decide whether the Ruler
   scorer is good enough to extend, against criteria fixed before the evaluation
   runs. **"Not yet" is an acceptable outcome and will be published as one.** On a
   pass, begin the application layer the design promises — messaging pillars, tone
   guardrails and the shadow — since a score without those is a diagnosis the
   project explicitly set out not to stop at. On a fail, the sprint is spent on the
   specific failure the evaluation named instead.

**Deliverable by 31 Oct:** one archetype proven or honestly failed, end to end,
with an evaluation result that can be shown. The adjacent luxury archetypes and
the remaining nine are **out of scope for this period** and stay unscheduled —
extending before Ruler is proven is the mistake this plan exists to avoid.

Reporting continues as it has: a dated frictional log per work folder, weekly
hours, and a STEM explainer alongside the project work each week.

## Open items I am carrying

* **No branch yet.** GitHub push access arrived 28 Sep. Code lands on a branch
  from Sprint 3; until then the repository field above needs confirming.
* **Sample data is the blocker.** Format, count and ownership are unresolved, and
  nothing downstream of it can start.
* **No quality figure is quotable.** Nothing is built, so there is no accuracy
  number to report, and the scored output shown in the week-two video is a design
  target with placeholder values rather than a result.
* **Uploads.** The four cuts are in the Drive folder; per-video links are not yet
  split out, and nothing is on YouTube.
