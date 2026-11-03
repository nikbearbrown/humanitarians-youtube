# CARRY-OUT.md — knowledge-work-plugins--claude-liam-build-zoom-meeting-sdk-app

**Carry-out sentence (written first, per CARRY-OUT LAW):**

> Build-zoom-meeting-sdk-app never decides to build a Zoom integration —
> it hands Claude the platform's exact join rules once that decision's
> already made.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it names the distinction (decide vs. supply-the-rules)
without naming the topic in detail, and it survives being repeated cold.

**The wrong guess it's built to defeat:** that a skill named
"build-zoom-meeting-sdk-app" designs the Zoom integration itself — picks
the platform, decides the feature, improvises the join flow. It's
deliberately narrower: it is a reference file, read only after a build
has already been routed to a meeting-embed workflow, and it supplies that
platform's specific rules — real meeting joins, auth and join flows,
waiting-room handling, meeting-bot patterns. Whether to embed a Zoom
meeting at all, and on which platform, is not this skill's job and isn't
in its file. That narrowness is stated as a design fact, not judged as a
strength or weakness (Plain register, no verdict).

**Sentence it defeats, made explicit:** "the skill builds the Zoom app" →
"the skill only supplies the platform's join rules once building it is
already the plan."
