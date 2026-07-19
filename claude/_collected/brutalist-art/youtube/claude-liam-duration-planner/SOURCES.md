# SOURCES — claude-liam-duration-planner
# "Claude, Timed." | duration-planner skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "Duration is an output, never a target."
- Source: skills/make/duration-planner/SKILL.md line 19
- Role: core principle — why clock targets have no learning basis; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "Cutting a beat below the time working memory needs to register and begin integrating the new element does not make learning faster — it makes it fail."
- Source: skills/make/duration-planner/SKILL.md line 74-75
- Role: consolidation floor rationale — working-memory constraint, not aesthetic preference; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Optimize for the structural completeness of each beat, not completion rate."
- Source: skills/make/duration-planner/SKILL.md line 113-114
- Role: anti-padding rule — ceiling is idea-complete, not clock-complete; stated once, in B07

## Self-demo source
- Video: claude-liam-sim-scout (built in this batch, video 12)
- B03 beat: actual_duration_s = 6.04s; content_type = title/definitional; floor = 3-5s; result = ABOVE FLOOR; action = +1s inter-beat hold recommended
- B04 beat: actual_duration_s = 20.12s; content_type = mechanism; floor = 6-10s; ceiling ~20s; result = ABOVE FLOOR / at-ceiling; action = none (genuinely single idea)
- Total runtime: 149.3s — content derives this; no clock consulted
- Not faked: actual_duration_s values read from sim-scout beat_sheet.json
