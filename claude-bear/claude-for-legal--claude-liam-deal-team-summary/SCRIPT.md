# SCRIPT — Claude, Deal Team Summary.

Register: Plain. Voice: Liam (Kokoro am_onyx). Mode: redo of
`anthropics/claude-for-legal/youtube/claude-liam-deal-team-summary`
(source register: Teardown → re-registered here as Plain: same facts, no verdict).

## Source-fidelity note (read before treating this as a normal redo)

The source `beat_sheet.json` has a batch-templating defect: several narration
fields contain a literal, unfilled `>` where the task-specific fact should be
(`"Claude's job: >."`, `"The SKILL.md is the spec — >."`, `"Paste this into
Claude: 'I want to >.'"`). The `source_skill` SKILL.md the sheet points at
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/
corporate-legal/skills/deal-team-summary/SKILL.md`) does not exist on this
machine — it lives on Bear's, unreachable here. `PEDAGOGY.md` in the source
dir is a one-line stub ("VERDICT: PASS. Batch build — skill teardown
format.") with no additional content. There is no `SCRIPT.md` in the source.

What IS reliable from the source and kept verbatim in argument: the generic,
non-placeholder mechanism facts — a skill is a folder Claude reads before it
acts (B01), it contains one file (`SKILL.md`) with the full instruction set,
steps run in the order the file lists them with no branching unless the file
says so (B02), and the reliability property this buys is repeatable structure
from a fixed spec, not better judgment (BVDT, minus its `>` gap).

What is NOT in the source (the placeholder gaps) is the one task-specific
fact: exactly what "Claude's job" is for *this* skill. That is inferred
**directly and only from the skill's own name**, `deal-team-summary` — a
structured status update (parties, key terms, status, open issues, next
steps) for a deal team — which is the plain, industry-standard meaning of
that phrase in corporate/M&A practice, not an invented specific UI or
proprietary field list. No claim about the actual SKILL.md's exact steps,
prompts, or output format is made; the reel stays at the level the skill's
name safely supports.

## B00 — Hesitant writer (the question, typed and corrected)

On screen (typed, then corrected): "Claude writes a deal\nteam summary by\nmagic?" —
"magic" is typed, reconsidered, and replaced with "instructions."

Narration (Liam):
> You might think Claude writes a deal team summary by magic — like it just knows. It doesn't: it follows instructions, in a file called a skill. Here's what's inside it.

## S01 — Stakes

> A merger is underway. Lawyers, bankers, and executives all need the same picture: parties, key terms, status, open issues, next steps. Ask five people for that update and you get five different shapes.

## S02 — The wrong guess

> The natural assumption is that Claude already knows how to shape this — good judgment, no separate instructions required. It's read enough deal documents to just handle it.

## S03 — Breaking it

> Ask for the same deal's summary twice, with no skill installed, and the two answers don't match — different fields, different order, sometimes a missing item. Judgment alone isn't repeatable.

## S04 — The mechanism (anatomy)

> A skill fixes that. It's a folder Claude reads before it acts — this one called deal-team-summary. Inside is one file, SKILL.md, plain language, no hidden logic. The file is the instructions.

## S05 — The mechanism (pipeline)

> Inside SKILL.md is a list of steps. Claude reads them in order and runs each one — pull the parties, pull the terms, check status, flag open issues, list next steps. Linear, no shortcuts.

## S06 — Anchor, planted

> Take one illustrative deal: Aster Corp buying Vale Robotics. Feed the skill the term sheet, the disclosure schedule, and the latest redline. Same five fields come back — parties, terms, status, open issues, next steps.

## S07 — Anchor, payoff

> Run it again next week, after the redline changes. The five fields are still there, same order — only the contents update. That's what a skill buys: the shape holds, the deal moves.

## S08 — Both directions (A)

> A consistent shape doesn't prove the deal is healthy — the skill structures whatever the documents say, including a bad clause or a stale draft. Structure isn't a check on the underlying facts.

## S09 — Both directions (B)

> And two summaries that look different without the skill aren't necessarily wrong — they might both be reasonable readings, just organized differently. That's the exact inconsistency the skill removes.

## BCRY — Carry-out

> A skill doesn't make Claude better at judgment. It makes Claude follow the same steps, in the same order, every single time.

## BHTF — Your turn (Claude prompt, read aloud)

> Your turn. Here's the prompt — read it with me. I'm working a deal and have a term sheet and a signed NDA. Summarize this deal for the deal team — but tell me your structure first, before you fill it in. Then run it again from scratch, and tell me if the structure changed.

## BOUT — Outro (Humanitarians AI skin)

OutroSeries:
> Claude, Deal Team Summary. This is Claude Basics, from Humanitarians AI.

OutroCTA:
> Find more at humanitarians.ai. …Liam, in for Bear.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | S01–S03; mechanism waits until S04–S05 |
| Wrong guess surfaced and falsified by a case | S02 states the read; S03 breaks it with the same-deal-twice case |
| Anchor, planted early, paid off late | S06 → S07 (Aster Corp / Vale Robotics, same case) |
| Both failure directions | S08 (consistent ≠ healthy) and S09 (different ≠ wrong) |
| No design judgment | S04–S05 describe the mechanism, never rule on whether it was built well |
| Playlist | `claude-for-legal` has no entry in `loop/playlists.json`; resolves via `_default` → "Claude Across the Curriculum" (logged in BUILD-LOG.md) |
