# QUESTION — knowledge-work-plugins--claude-liam-lead-triage

**Question:** Claude, Lead Triage.

**Who asked / where:** Redo-mode build. `SUBJECT.json` points at
`anthropics/knowledge-work-plugins/youtube/claude-liam-lead-triage/beat_sheet.json` as
the source — a Teardown-register skill-teardown of an Anthropic skill named
`lead-triage`, built in the same 2026-07-25 batch as this family's `crm-cleanup`,
`call-prep`, and `crm-maintenance` siblings (`PEDAGOGY.md`: "Batch build — skill
teardown format", verdict PASS).

**Source defect found on read — total, not partial.** The `crm-cleanup` and
`call-prep` siblings each had a batch template-truncation bug where a `>`-prefixed
skill-description placeholder got cut off mid-sentence in three of seven beats, but the
complete sentence survived intact in each source's own B00. `crm-maintenance` had the
same pattern empty everywhere. This source matches `crm-maintenance`'s case exactly: the
`>` placeholder is empty in B00, B03, BVDT, and BHTF alike — "The skill is lead-triage.
>. A SKILL.md tells Claude exactly how," "Claude's job: >. What it gets right: repeatable
results," "The SKILL.md is the spec — >. Same input, same output," and "Paste this into
Claude: 'I want to >. Read the lead-triage skill.'" No beat in the source's seven carries
the skill's actual domain-specific description of what "triage" means for a lead here —
there is nothing to recover, because nothing survived. The `source_skill` path the
source's own metadata points at
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/small-business/skills/lead-triage/SKILL.md`)
is Bear-machine-only and does not exist on this machine; a search of this repo's local
`knowledge-work-plugins` clone and the batch logs (`SKILL-EXPLAINERS-BATCH-LOG.md`,
`BUILD-SKILL-EXPLAINERS-LOG.md`) turned up only a build-status row
(`anthropics/knowledge-work-plugins/small-business/skills/lead-triage/SKILL.md — built`),
never the SKILL.md text itself. **This build does not invent what lead-triage
specifically scores, ranks, or routes a lead by** — that would be fabricating the exact
content the NO-INVENTION rule in this skill's redo contract forbids.

**What survives in the source's readable text, and is what this redo keeps:** a Skill is
a folder Claude reads before it works; this one, `lead-triage`, has two items —
`SKILL.md` (3k, the instruction set) and a `reference/` folder — this part is a genuine,
undamaged fact straight from the source's B01 props, not a gap; the SKILL.md is plain
language, no hidden logic ("the file is the program"); the pipeline lives in a Steps
section, read top to bottom, executed in order, no branching unless a step says so;
`lead-triage` "is a specification written as an instruction set" whose guarantee is
repeatable results — the same input produces the same output on every run — and whose
limit is "anything outside the spec": ask for something the file doesn't cover and the
skill has nothing to say about it. That is the entire readable fact set. Nothing more
specific than that (no scoring rubric, no routing destination, no field list) survives.

**The wrong guess this reel corrects:** "triage" is the word a newcomer over-reads. In
ordinary use — especially its medical origin — triage implies a judgment call: someone
(or something) deciding, on its own authority, which cases matter more and acting on
that call. The skill's actual, readable shape is the opposite of an autonomous judgment:
it is a bounded specification, invoked once per request, that reads a fixed set of steps
and produces the same output for the same input every time — not Claude exercising
independent judgment about which leads deserve attention. That reading is what the
cold-open writer beat states and then corrects (JUDGE → sort).

**Carry-out it's built to defeat:** the newcomer's guess that "Claude, lead triage"
means Claude decides, on its own judgment, which leads matter. The correction: it is one
spec-bound sort, the same steps every time, limited to exactly what the file says —
never an autonomous verdict on a lead's worth.
