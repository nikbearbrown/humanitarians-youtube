# QUESTION — knowledge-work-plugins--claude-liam-crm-maintenance

**Question:** Claude, Crm Maintenance.

**Who asked / where:** Redo-mode build. `SUBJECT.json` points at
`anthropics/knowledge-work-plugins/youtube/claude-liam-crm-maintenance/beat_sheet.json` as
the source — a Teardown-register skill-teardown of an Anthropic skill named
`crm-maintenance`, built in the same 2026-07-25 batch as this family's `crm-cleanup` and
`call-prep` siblings (`PEDAGOGY.md`: "Batch build — skill teardown format", verdict PASS).

**Source defect found on read — total, not partial, this time.** The `crm-cleanup` and
`call-prep` siblings each had a batch template-truncation bug where a `>`-prefixed
skill-description placeholder got cut off mid-sentence in three of seven beats, but the
*complete* sentence survived intact in each source's own B00. This source has the same
`>` placeholder pattern in B00, B03, BVDT, and BHTF — but here it is empty everywhere,
including B00: "The skill is crm-maintenance. >. A SKILL.md tells Claude exactly how,"
"Claude's job: >. What it gets right: repeatable results," "The SKILL.md is the spec —
>. Same input, same output," and "Paste this into Claude: 'I want to >. Read the
crm-maintenance skill.'" No beat in the source's seven carries the skill's actual
domain-specific description — there is nothing to recover, because nothing survived. The
`source_skill` path this source's own metadata points at
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/crm-maintenance/SKILL.md`)
is Bear-machine-only and does not exist on this machine; a search of this repo's local
`knowledge-work-plugins` clone and the batch logs
(`SKILL-EXPLAINERS-BATCH-LOG.md`, `BUILD-SKILL-EXPLAINERS-LOG.md`, `_audit/*.csv`) turned
up only build-status rows, never the SKILL.md text itself. **This build does not invent
what crm-maintenance specifically checks, updates, or touches inside a CRM** — that would
be fabricating the exact content the NO-INVENTION rule in this skill's redo contract
forbids.

**What survives in the source's readable text, and is what this redo keeps:** a Skill is
a folder Claude reads before it works; this one, `crm-maintenance`, has two items —
`SKILL.md` (the instruction set) and a `reference/` folder; the SKILL.md is plain
language, no hidden logic ("the file is the program"); the pipeline lives in a Steps
section, read top to bottom, executed in order, no branching unless a step says so;
`crm-maintenance` "is a specification written as an instruction set" whose guarantee is
repeatable results — the same input produces the same output on every run — and whose
limit is "anything outside the spec": ask for something the file doesn't cover and the
skill has nothing to say about it. That is the entire readable fact set. Nothing more
specific than that survives.

**The wrong guess this reel corrects:** "maintenance" is the word a newcomer over-reads.
In ordinary use, "CRM maintenance" suggests an ongoing job — something that runs in the
background, continuously keeping records tidy on its own initiative. The skill's actual,
readable shape is the opposite of continuous: it is a bounded specification, invoked once
per request, that reads a fixed set of steps and produces the same output for the same
input every time — not a standing autonomous process. That reading is what the cold-open
writer beat states and then corrects (MAINTAIN → CHECK).

**Carry-out it's built to defeat:** the newcomer's guess that "Claude, crm maintenance"
means an ongoing job Claude runs on the CRM by itself. The correction: it is one
spec-bound check, the same steps every time, limited to exactly what the file says —
never a standing background process.
