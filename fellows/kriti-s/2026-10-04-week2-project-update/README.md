# Week 2: Pinned Baseline, Persistent Logging, and Scoping Six Memory Designs (Pi Memory)

**Group:** RL Environment · **Reporting week:** 2026-09-28 through 2026-10-04

## Executive Summary

The week delivered foundational engineering rigor: pinning Pi to a single fixed repository version to guarantee reproducible test harnesses, inspecting the Optimus-generated model configuration and `arm0_runner.py` execution files, and upgrading the experimental runner to persist all logs into permanent directories rather than ephemeral temporary paths so that every run remains auditable. Additionally, following a progress check-in with the team and project lead, six concrete memory architectures were scoped: three episodic designs (contrastive trajectories, milestone subtask DAGs, closed-loop utility retrieval) and three causal designs (causal dependency graphs, intervention/counterfactual memory, failure-repair graphs).

## Evidence — Open Directly

- [Adapted beat sheet (11 beats)](beat_sheet.json).
- [Frictional log](Frictional.md).
- [Weekly hours](weekly_hours.md).
- [Explainer video](https://drive.google.com/file/d/1cgrPLyHPYWT5n3w6fxOis5dKi2yYOx8j/view?usp=drive_link)
- [Progress video](https://drive.google.com/file/d/1SgdIIJpmpgKTf5gCDyWiZwosWo2TYzNb/view?usp=drive_link)


## Attribution and Contribution

Work by Kriti S.: narrative condensed into an 11-beat structure (B08 timeline removed per author request), custom Remotion scene components created (`UpdPin`, `UpdFlow`, `UpdKeep` in `WeekUpdate.tsx`), code and runner changes visually abstracted without exposing private credentials or verbose code snippets, and narration script written, then voiced via Kokoro `am_onyx`. Research and review by Kriti S.: version pinning, modifying runner logging destinations, team coordination, scoping the six memory paradigms, and approving the video review cut.

## Folder Contents

- README.md: result, evidence status, and attribution.
- report.md: comprehensive technical report, architecture manifest, and execution guide.
- beat_sheet.json: 11-beat weekly update production plan and cues.
- Frictional.md: illustrative process reflection and build friction log.
- weekly_hours.md: 20-hour weekly task breakdown and evidence index.
- Episodic and Causal Memory Architectures.docx: canonical master architecture document.
