# QUESTION.md

**Question:** Does the ic-memo Skill write the investment committee memo on its own, like
an app would — or does Claude need to be told how, step by step?

**Asked by:** N/A — no individual asker; this is the source reel's own framing, carried
over per the redo contract (the source is a skill-teardown of Anthropic's `ic-memo`
skill for PE deal-approval work).

**Name usable:** N/A.

**Source check:** SUBJECT.json's `source_skill` field (recorded in the original sheet's
metadata) points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/valuation-reviewer/skills/ic-memo/SKILL.md`
— confirmed absent on this machine. Unlike some siblings in this family (e.g.
`claude-for-legal--claude-liam-clearance`), **the source sheet itself is NOT a
placeholder shell** — every beat's `narration_text` and REMOTION props carry real,
specific facts (file size `2k`, the exact skill description "Draft a structured
investment committee memo for PE deal approval. Synthesizes due diligence findings,
financial analysis, and deal terms...", the verdict recap). No `>` placeholders anywhere
in the source. So this redo carries those facts forward directly rather than
reconstructing them generically.

**Redo note:** this is a `mode: "redo"` build (SUBJECT.json). Source:
`anthropics/financial-services/youtube/claude-liam-ic-memo/beat_sheet.json` (7-beat
Teardown skill-teardown: B00 cold open, B01 anatomy, B02 pipeline, B03 design tell, BVDT
verdict, BHTF handoff, BOUT outro — register "Teardown"). Shape and beat count are
locked from that source (7 beats kept: B00, B01, B02, B03, BCRY [was BVDT], BHTF, BOUT).
This build re-registers the narration to Plain (drops the "Teardown moment" / "what it
gets right, what it bites" verdict framing while keeping the same underlying facts),
replaces the cold open with `BrutalistHesitantWriter` (WRITER LAW), and reskins the
close to Humanitarians AI (`OutroSeries`, handle `@HumanitariansAI`).

**Wrong guess (WRITER LAW):** the newcomer's naive framing is that `ic-memo` is an
autonomous app that writes the memo by itself. The corrected word on screen ("app" →
"skill") ties directly to B01's anatomy beat (a skill is a folder Claude reads before it
works) and to the carry-out (a Skill doesn't make Claude smarter, it makes Claude follow
fixed steps) — matching the same convention already used across this family's other
skill-teardown redos (e.g. `financial-services--claude-liam-buyer-list`, built the same
day as the structural precedent for this reel).
