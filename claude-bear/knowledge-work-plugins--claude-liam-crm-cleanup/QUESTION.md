# QUESTION — knowledge-work-plugins--claude-liam-crm-cleanup

**Question:** Claude, Crm Cleanup.

**Who asked / where:** Redo-mode build. `SUBJECT.json` points at
`anthropics/knowledge-work-plugins/youtube/claude-liam-crm-cleanup/beat_sheet.json` as the
source — a Teardown-register skill-teardown of an Anthropic skill named `crm-cleanup`, built
in a 2026-08-03 batch (all 7 source beats `build.status: "VIDEO"`, `cut: "master"`).

**Source defect found on read:** the source's narration truncates its own skill-description
sentence mid-quote in three of its seven beats. B00 carries the complete, untruncated
version — "Scans HubSpot for stale deals, duplicate contacts, and missing fields, then fixes
what the owner approves. Accepts optional scope argument for deals, contacts, or all." — but
B03 cuts it to "...then fixes what the owner app.", `BVDT` cuts it to "...then fixe.", and
`BHTF` cuts it to "...missing fields,." right before the clause finishes. This is the same
batch template-truncation bug already logged on this family's `call-prep` sibling. Nothing
had to be invented; the complete sentence was recovered directly from B00 and used wherever
the truncated copies appear.

**What this redo keeps, and what it does not invent:** every fact the source's readable text
establishes is kept and generalized — a Skill is a folder Claude reads before it works; the
`SKILL.md` file is the full instruction set in plain language, not hidden logic ("the file is
the program"); the pipeline lives in a Steps section, read top to bottom, executed in order,
no branching unless a step says so; `crm-cleanup` specifically scans HubSpot for three named
things — stale deals, duplicate contacts, and missing fields — and only fixes what the owner
approves; it accepts an optional scope argument narrowing the run to deals, contacts, or all;
run the same request through it twice and the same steps produce the same result; the
guarantee holds only for what the file specifies, nothing outside it. This reel never invents
what "stale," "duplicate," or "missing" thresholds the skill actually applies inside HubSpot —
the source names the three categories and the approval gate, and nothing more specific than
that survives in its readable text.

**The wrong guess this reel corrects:** "crm cleanup" sounds like Claude will use its own
judgment to tidy up whatever it finds messy in the CRM, and just fix it. It doesn't — it scans
for exactly the three things the file specifies, and it fixes only what the owner approves. That
reading is what the cold-open writer beat states and then corrects.

**Carry-out it's built to defeat:** the newcomer's guess that Claude, crm cleanup means Claude
decides on its own how to clean up the CRM. The correction: it scans for exactly what the file
specifies, and fixes only what the owner approves — the same way every time.
