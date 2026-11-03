# QUESTION.md

**Question:** Does the investment-proposal Skill write the client pitch on its own, like
an app would — or does Claude need to be told how, step by step?

**Asked by:** N/A — no individual asker; this is the source reel's own framing, carried
over per the redo contract (the source is a skill-teardown of Anthropic's
`investment-proposal` skill for pitching prospective wealth-management clients).

**Name usable:** N/A.

**Source check:** SUBJECT.json's `source_sheet` metadata records `source_skill` as
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/meeting-prep-agent/skills/investment-proposal/SKILL.md`
— confirmed absent on this machine (scoped `find` under `anthropics/financial-services`
and for `meeting-prep-agent` generally, not a full-filesystem scan). The source sheet
itself is **not** a placeholder shell — every beat's `narration_text` and REMOTION props
carry real, specific facts (file size `3k`, the exact skill description "Create
professional investment proposals for prospective clients. Covers the firm's approach,
proposed allocation, expected outcomes, and fee structure. Use when pitching new clients
or presenting a new investment strategy.", the trigger phrases, the verdict recap). No
unfilled `>` placeholders anywhere. This redo carries those facts forward directly rather
than reconstructing them generically.

**Redo note:** this is a `mode: "redo"` build (SUBJECT.json). Source:
`anthropics/financial-services/youtube/claude-liam-investment-proposal/beat_sheet.json`
(7-beat Teardown skill-teardown: B00 cold open, B01 anatomy, B02 pipeline, B03 design
tell, BVDT verdict, BHTF handoff, BOUT outro — register "Teardown"). Shape and beat count
are locked from that source (7 beats kept: B00, B01, B02, B03, BCRY [was BVDT], BHTF,
BOUT). This build re-registers the narration to Plain (drops the "Teardown moment" /
"what it gets right, what it bites" verdict framing while keeping the same underlying
facts), replaces the cold open with `BrutalistHesitantWriter` (WRITER LAW), and reskins
the close to Humanitarians AI (`OutroSeries`, handle `@HumanitariansAI`).

**Wrong guess (WRITER LAW):** the newcomer's naive framing is that `investment-proposal`
is an autonomous app that picks the client pitch — or even the investments — by itself.
The corrected word on screen ("app" → "skill") ties directly to B01's anatomy beat (a
skill is a folder Claude reads before it works) and to the carry-out (a Skill doesn't
make Claude smarter, it makes Claude follow fixed steps) — matching the same convention
already used across this family's other skill-teardown redos (e.g.
`financial-services--claude-liam-ic-memo`, `financial-services--claude-liam-buyer-list`).
