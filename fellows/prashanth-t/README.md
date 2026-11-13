# Prashanth Talwar — Humanitarians AI Fellow

**Role:** AI/ML Developer  
**Project:** Madison — Jungian Brand Archetype Detector  
**Repository:** _to be confirmed_  
**Branch:** not yet created — GitHub push access granted 28 Sep; code lands on a branch from the next sprint  
**Group / supervisor:** _to be filled in_  
**Agreement period:** 2 Sep — _to be filled in_  
**GitHub:** [@PrashanthTalwarr](https://github.com/PrashanthTalwarr)  
**Rendered videos:** [Google Drive folder](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) — all four cuts

## Research question

Can a brand's archetype be identified from the language and visuals it actually
publishes, scored so that a human can audit every number, rather than inferred from
a self-reported brief — and can that accuracy be tested before the output is trusted?

Most archetype tools take a short self-description and return one label with a
generic paragraph. They do not interrogate real evidence, they cannot express a
hybrid, and they stop at diagnosis. Madison is built around three commitments
instead: read what the brand actually ships, return a primary **and** a secondary
archetype with the inconsistency between them named, and end in application —
messaging pillars, tone guardrails, and the archetype's shadow. Scope is the Ruler
archetype for luxury branding first, to prove the pipeline end to end on one
archetype before scaling to twelve.

## Project work

| Week | Work | Result | Evidence | Log |
|---|---|---|---|---|
| 2–6 Sep | Onboarding | Madison project context, and the Brutalist reel pipeline — beat-sheet authoring, audio-first rendering, and the phase gates each build has to pass. | — | — |
| 14–18 Sep | Scoping with the team | Ruler archetype chosen as the first target, for luxury branding. Three design commitments fixed: evidence-based reads, hybrid/tension-aware output, output that ends in application. Progress update produced 16 Sep. | [`madison-archetype-progress/`](madison-archetype-progress) · [drive](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) · commit [`567602b`](https://github.com/nikbearbrown/humanitarians-youtube/commit/567602b88a8b005dda6b3c18f9c24eaab47753cb) | [log](madison-archetype-progress/FRICTIONAL.md) |
| 21–25 Sep | Technical design, from the section-five methodology | A concrete design across three parts: **inputs** — published brand copy, social captions, tagline, competitor copy, never a self-report questionnaire; **scoring** — every trait score carries the line of copy that earned it, so the output is auditable rather than a black box; **evaluation** — hand-labelled brands first, to prove it reads brand voice and not surface keywords. Progress update produced 24 Sep. | [`madison-archetype-progress-week2/`](madison-archetype-progress-week2) · [drive](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) · commit [`9fd2e15`](https://github.com/nikbearbrown/humanitarians-youtube/commit/9fd2e15229bbf878c37c91f07d8d58193ee1b639) | [log](madison-archetype-progress-week2/FRICTIONAL.md) |

**Status: design stage.** Nothing is built and no results exist. The blocker is
sample data — what format the samples arrive in, roughly how many brands are
needed, and who gathers them. Until that exists, evaluation cannot start and no
accuracy figure is quotable. Both progress reels state this on screen rather than
implying a working system: the one scored output shown is labelled a design target
carrying placeholder values, and the evaluation figure is labelled illustrative.

## STEM Topics

Topic selection and the content outline for each explainer are mine; narration
drafting, beat sheets and production by Claude from them.

| Week | Topic | Evidence | Log |
|---|---|---|---|
| 14–18 Sep | How LLM function calling works — the four-step loop, how a tool result returns as another message, the failure modes, and how the same loop is what an agent is built from | [`llm-function-calling/`](llm-function-calling) · [drive](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) · commit [`567602b`](https://github.com/nikbearbrown/humanitarians-youtube/commit/567602b88a8b005dda6b3c18f9c24eaab47753cb) | [log](llm-function-calling/FRICTIONAL.md) |
| 21–25 Sep | How memory works in an AI agent — stateless model calls, short-term memory as the running conversation and its context ceiling, long-term memory as an external store, and the retrieve-into-context pattern | [`agent-memory/`](agent-memory) · [drive](https://drive.google.com/drive/folders/1fJAA92dC6Rvwrlc5mhOTIM0Pl8g6m9sp?usp=drive_link) · commit [`9fd2e15`](https://github.com/nikbearbrown/humanitarians-youtube/commit/9fd2e15229bbf878c37c91f07d8d58193ee1b639) | [log](agent-memory/FRICTIONAL.md) |

Both explainers run ~200 seconds in the Plain register for @HumanitariansAI. Each
folder carries the `beat_sheet.json` the renderer consumes plus its build
documentation: the typed work order, a claim-by-claim factcheck, a provenance note
marking what is constructed or illustrative rather than measured, the pre-render
gate report, the on-screen prompts, and a paste-ready prompt that rebuilds the reel
end to end. `FnCalling.tsx` holds the reel-local Remotion components these cuts
share. Two folders also carry a `BUILD-LOG.md` recording defects found during the
build and how they were resolved.

## Next steps

- **Sample data** — settle format, approximate brand count, and ownership. This is
  the blocker; evaluation cannot begin without it.
- **Design review** — run the technical design through review and produce a proper
  SDD, which is what the build is written against.
- **Build and prove Ruler** — one archetype, end to end, against the hand-labelled
  set, before anything scales.
- **Then the other eleven** — scale is the last step, not the first. Not scheduled.

## Hours and renewal

Weekly hours: [HOURS.md](HOURS.md) — logged by week, project and STEM split out  
Renewal request: [RENEWAL.md](RENEWAL.md) — requesting 1 Oct – 31 Oct

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.
