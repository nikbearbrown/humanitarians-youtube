# QUESTION.md

**Question:** Does the comp-analysis Skill decide what to pay someone on its own, like an
app would — or does Claude need to be told how, step by step?

**Asked by:** N/A — no individual asker; this is the source reel's own framing, carried
over per the redo contract (the source is a skill-teardown of Anthropic's `comp-analysis`
skill for HR compensation work).

**Name usable:** N/A.

**Source check:** SUBJECT.json's `source_sheet` metadata records `source_skill` as
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/human-resources/skills/comp-analysis/SKILL.md`
— confirmed absent on this machine (scoped `find` under
`anthropics/knowledge-work-plugins` for `comp-analysis` and `human-resources`
generally, not a full-filesystem scan). The source sheet itself is **not** a placeholder
shell — every beat's `narration_text` carries a real, specific fact: the exact skill
description ("Analyze compensation — benchmarking, band placement, and equity modeling.
Trigger with 'what should we pay a [role]', 'is this offer competitive', 'model this
equity grant', or when uploading comp data to find outliers and retention risks."), the
`3k` SKILL.md file size, and the verdict recap. Several of the source's later beats
(B03, BVDT, BHTF) carry a **truncated/garbled copy** of that same description (cut off
mid-word, e.g. "...Trigger with \"what should" / "...only what the SKILL.md specifies.
Trigge"), a known templating defect already seen and logged in this family's other
skill-teardown redos. This build reuses the one **untruncated** copy (from the source's
B00) everywhere the description is needed, rather than propagating the truncation.

**Redo note:** this is a `mode: "redo"` build (SUBJECT.json). Source:
`anthropics/knowledge-work-plugins/youtube/claude-liam-comp-analysis/beat_sheet.json`
(7-beat Teardown skill-teardown: B00 cold open, B01 anatomy, B02 pipeline, B03 design
tell, BVDT verdict, BHTF handoff, BOUT outro — register "Teardown"). Shape and beat count
are locked from that source (7 beats kept: B00, B01, B02, B03, BCRY [was BVDT], BHTF,
BOUT). This build re-registers the narration to Plain (drops the "Teardown moment" /
"what it gets right, what it bites" verdict framing while keeping the same underlying
facts), replaces the cold open with `BrutalistHesitantWriter` (WRITER LAW), and reskins
the close to Humanitarians AI (`OutroSeries`, handle `@HumanitariansAI`).

**Wrong guess (WRITER LAW):** the newcomer's naive framing is that `comp-analysis` is an
autonomous app that decides what to pay someone by itself. The corrected word on screen
("app" → "skill") ties directly to B01's anatomy beat (a skill is a folder Claude reads
before it works) and to the carry-out (a Skill doesn't give Claude judgment about pay, it
makes Claude run fixed steps) — matching the same convention already used across this
family's other skill-teardown redos (e.g.
`financial-services--claude-liam-investment-proposal`,
`financial-services--claude-liam-ic-memo`).
