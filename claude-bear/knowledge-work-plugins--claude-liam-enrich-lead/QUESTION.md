# QUESTION — knowledge-work-plugins--claude-liam-enrich-lead

**Question:** Claude, Enrich Lead.

**Who asked / where:** Redo-mode build. `SUBJECT.json` points at
`anthropics/knowledge-work-plugins/youtube/claude-liam-enrich-lead/beat_sheet.json` as the
source — a Teardown-register skill-teardown of an Anthropic skill named `enrich-lead`
(brand `claude-liam`, audience `Claude`, 7 beats: B00 cold open, B01 anatomy, B02 pipeline,
B03 design tell, BVDT verdict, BHTF handoff, BOUT outro — all already REMOTION).

**Source is intact — unlike this batch's `crm-maintenance`/`crm-cleanup` siblings, whose
`>`-prefixed skill-description placeholder was truncated or empty.** Every beat here
carries the full sentence: "Instant lead enrichment. Drop a name, company, LinkedIn URL,
or email and get the full contact card with email, phone, title, company intel, and next
actions." Nothing to recover — the domain-specific fact set survives completely and is
what this redo keeps.

**What survives in the source, and is what this redo keeps:** a Skill is a folder Claude
reads before it works; this one, `enrich-lead`, is one file, `SKILL.md` — plain language,
no hidden logic ("the file is the program"); the pipeline lives in a Steps section, read
top to bottom, executed in order, no branching unless a step says so; the job is instant
lead enrichment — drop **any one** of a name, a company, a LinkedIn URL, or an email, and
get back a full contact card (email, phone, title, company intel, next actions); the
guarantee is repeatable results (same input, same output, every run); the limit is
"anything outside the spec" — ask for something the file doesn't cover and the skill has
nothing to say about it.

**The wrong guess this reel corrects:** a newcomer hears "lead enrichment" and assumes it
means turning a *complete* profile — name, company, and a LinkedIn link, all already in
hand — into something more complete still. The source's own line reads the opposite way:
"Drop a name, company, LinkedIn URL, **or** email" — any single one of those four is
enough to start from; the skill fills in the rest. The cold-open writer beat states the
over-read (needing a full LinkedIn profile already) and corrects it (needing just a name).

**Carry-out it's built to defeat:** the newcomer's guess that enrich-lead needs a
near-complete profile to begin. The correction: it needs exactly one identifying detail —
a name, a company, a LinkedIn URL, or an email — and turns that alone into the same full
contact card, every time, never inventing anything the file doesn't say to produce.
