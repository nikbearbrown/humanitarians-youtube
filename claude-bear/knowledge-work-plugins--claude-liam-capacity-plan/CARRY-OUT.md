# CARRY-OUT — knowledge-work-plugins--claude-liam-capacity-plan

**The line (written first, GATE C):**

> Capacity-plan isn't Claude sensing that your team is stretched thin — it's
> a written two-step procedure, workload analysis then utilization
> forecasting, run on the numbers you give it, and it only answers what
> those two steps compute.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land (a
numbers-driven, two-step written procedure vs. a manager's private instinct
for who's stretched thin), not the topic (capacity planning generally).

**The wrong guess it defeats:** that asking Claude to plan capacity means it
senses overload the way an experienced manager would — reading strain into
how a request is phrased. It doesn't. The `capacity-plan` skill runs two
fixed steps on the numbers you supply: workload analysis (each person's
committed hours against their available capacity), then utilization
forecasting (projecting that load forward). Ask it something with no
workload or capacity numbers attached, and neither step has anything to run
on; it will not infer overload from tone or manager instinct.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope; this line compresses it into the reel's
carry-out.
