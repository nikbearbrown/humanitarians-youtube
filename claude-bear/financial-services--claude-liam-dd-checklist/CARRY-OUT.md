# CARRY-OUT — financial-services--claude-liam-dd-checklist

**The line (written first, GATE C):**

> A Claude due diligence checklist isn't independent judgment about a deal's
> risks — it's a written procedure that tailors known workstreams to the
> deal's sector and type, and it only flags what it's already tracking.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land (a
tailored, written procedure vs. an analyst's independent judgment call about
what risks matter for this deal), not the topic (due diligence generally).

**The wrong guess it defeats:** that asking Claude to "build the DD
checklist" means it sizes up this specific deal and decides, from its own
judgment, which risks are worth chasing. It doesn't. The `dd-checklist`
skill reads the target's sector, deal type, and complexity, then builds the
checklist from workstreams the file already defines — request lists, status
tracking, red-flag escalation. Hand it a sector the file never lists and it
has no independent research to reach for; it will not invent a bespoke
workstream from general deal-making knowledge.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope; this line compresses it into the reel's
carry-out.
