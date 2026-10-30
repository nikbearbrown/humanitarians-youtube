# Week 1: Groundwork, Memory Types, and Experimental Design (Pi Memory)


**Group:** RL Environment · **Reporting week:** 2026-09-21 through 2026-09-27

## Executive Summary

The week established the project foundation: onboarding on Discord, reviewing past discussions, securing ArkenOS access, studying six distinct memory types (procedural, semantic, episodic, causal, prospective, and metacognitive), mapping Pi's internal architectural seams (initialization, tool runs, hooks, session storage, context compaction), and formulating a 5-step experimental plan. The plan establishes baselines (with and without memory), pins the Pi version, evaluates architectures on public benchmarks (SWE-bench, LongMemEval), and enforces token budget constraints across storage, writes, retrieval, and context.

## Evidence — Open Directly

- [Adapted beat sheet (12 beats)](beat_sheet.json).
- [Frictional log](Frictional.md).
- [Weekly hours](weekly_hours.md).
- [Explainer video](https://drive.google.com/file/d/12p9n-g-WytTNod9JqK-EiRpuE2CRawxR/view?usp=drive_link)
- [Progress video](https://drive.google.com/file/d/1mQ6zEhl8dr_QLyXH6MfGbJpPkcwBrtQS/view?usp=drive_link)

## Attribution and Contribution

Work by Kriti S.: narrative adapted to a 12-beat update structure, custom Remotion scene components created (`WeekUpdate.tsx`), ArkenOS referenced as a named boundary without displaying private UI, and narration script written, then voiced via Kokoro am_onyx speaking as Kriti. Research and review by Kriti S.: weekly onboarding, literature study of six memory architectures, defining experimental controls and budgets, and reviewing render cuts.

## Folder Contents

- README.md: result, evidence status, and attribution.
- report.md: comprehensive technical report, architecture manifest, and execution guide.
- beat_sheet.json: 12-beat weekly update production plan and cues.
- Frictional.md: illustrative process reflection and build friction log.
- weekly_hours.md: 20-hour weekly task breakdown and evidence index.
- Initial_Memory_Scoping.docx: initial 5-phase memory scoping document.
