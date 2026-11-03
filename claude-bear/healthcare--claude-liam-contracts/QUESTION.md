# QUESTION.md

**Question:** Will Claude approve my contract before I sign it?

**Asked by:** N/A — no individual asker; this is the source reel's own framing,
carried over per the redo contract (the source is a skill-teardown of
Anthropic's `contracts` skill).

**Name usable:** N/A.

**Redo note:** this is a `mode: "redo"` build (SUBJECT.json). Source:
`anthropics/healthcare/youtube/claude-liam-contracts/beat_sheet.json` (7-beat
Teardown skill-teardown, register "Teardown", already fully built and
delivered — `AUDIT.md` shows GATE T PASS, GATE AUDIO PASS, no open defects).
Unlike some siblings in other families, this source carries **real, filled-in
facts** (no unfilled `>` placeholders): skill name `contracts`, job "Answer a
question across a corpus of contract documents with verified citations,"
scope ("use when the user asks what a contract says, which contracts have a
clause, what changed between amendments, or any question that needs reading
and citing across a set of contract files"), the corpus-must-be-local
constraint, and a real 3-file anatomy (README.md 12k, SKILL.md 40k, sweep.mjs
17k). Shape and beat count are locked from that source; this build
re-registers the narration to Plain, replaces the cold open with
BrutalistHesitantWriter, and reskins the close to Humanitarians AI.

**The newcomer's wrong guess:** that a "contracts" skill means Claude will
render a legal judgment on the contract — approve it, flag it as safe,
tell you whether to sign. What it actually does is closer to search: answer
a factual question across a set of contract files and cite exactly where
each answer comes from. It never renders a verdict on whether the contract
is good to sign.
