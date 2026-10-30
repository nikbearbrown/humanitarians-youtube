# Frictional Log — pi-memory-week-one

## 2026-10-03 —  Week 1 Entry

**Record provenance:** Reflecting on the Week 1 memory architecture planning reel 

- **Work and expectation:** In the scenario, I review and verify the Week 1 progress explainer and expect the transition from onboarding to a concrete experimental design—incorporating baselines, budgets, and six memory types—to be clear and verifiable within ~103 seconds.
- **What I try:** Communicate the onboarding milestones (Discord, team threads, ArkenOS access), summarize six distinct memory taxonomies, identify Pi's architectural hook seams, and present the 5-phase plan without over-claiming completed benchmarks before code is implemented.
- **Where it resists:** 
  - *Scope Separation:* Clarifying that week one represents groundwork and experimental planning rather than completed empirical benchmark runs.
  - *Visual Constraints:* Honoring project boundaries by presenting ArkenOS as a labeled entity rather than exposing private workspace UI.
  - *Audio Timing:* Kokoro audio takes required lead-silence and hold buffers baked into `mp3/beat-*.mp3` to align with the Remotion compiler's strict duration thresholds ($\pm 0.15$s).
- **What I do next:** Set up the isolated evaluation repository, pin the Pi core package versions, implement the baseline harness (no-memory vs. baseline memory), and configure the token budget controller.
- **AI and other contributions:** Claude Code generated the 12-beat sheet, authored custom Remotion components (`WeekUpdate.tsx`), verified factcheck claims, and ran the Brutalist video build pipeline. Audio voiced via Kokoro `am_onyx`. Human fellow authored the weekly progress message, outlined experimental parameters, and approved the review cut.
- **What I understand:** Establishing baselines, resource budgets, and evaluation metrics before writing memory code prevents confusing retrieval volume with genuine reasoning improvement.
- **Evidence:** [beat_sheet.json](beat_sheet.json), [report.md](report.md), [weekly_hours.md](weekly_hours.md)
