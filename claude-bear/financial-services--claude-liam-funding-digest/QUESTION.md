# QUESTION — financial-services--claude-liam-funding-digest

**Mode:** redo (`SUBJECT.json.mode == "redo"`).
**Source:** `anthropics/financial-services/youtube/claude-liam-funding-digest/beat_sheet.json`
(Teardown register, 7 beats, `source_skill` field points at
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/partner-built/spglobal/skills/funding-digest/SKILL.md`).

## Source-file check

That `source_skill` path does **not** exist on this machine (checked directly
and via `find` across the whole `anthropics/financial-services` tree and the
rest of `anthropics/` — no `plugins/partner-built/spglobal` directory is
present locally; only the YouTube build folder for this reel exists). As with
the `claude-tag-plugins--claude-liam-datadog-api` precedent, this is **not** a
missing-content problem: the source `beat_sheet.json`'s own `narration_text`
fields already quote the skill's full frontmatter description verbatim in
B00 — a complete, specific sentence about what the skill produces, when it
triggers, and what it outputs. This build reuses that quoted text as the
factual record, per the redo contract ("keep its facts").

**The skill's stated description (quoted verbatim from the source sheet):**

> Generate a polished one-page PowerPoint slide summarizing key takeaways from
> recent funding rounds and notable capital markets activity across a user's
> watched sectors or companies. Use this skill when the user asks for a deal
> flow summary, weekly recap, funding digest, transaction roundup, or capital
> markets briefing. Triggers on: 'deal flow digest', 'weekly funding recap',
> 'deal roundup', 'transaction summary this week', 'what happened in [sector]
> this week', 'capital markets update', or any request to compile recent
> funding activity into a briefing slide. Produces a professional single-slide
> PPTX with key takeaways, valuation data, and Capital IQ deal links.

**The skill's file anatomy (from source B01, unchanged):** 3 files —
`LICENSE` (11k), `SKILL.md` (29k, the instruction set), `references/` (folder).

**The skill's pipeline (from source B02, unchanged):** read `SKILL.md` → execute
each step in order, linear, no branching unless a step says so → return the
result.

## The question, translated for a newcomer

The source is written for an audience that already knows what a Claude Skill
is and wants a teardown of one specific partner-built skill. `hai-simple`'s
audience is a newcomer to Claude. The redo contract requires keeping the
source's question, facts, and body argument — so the question is generalized
to what a newcomer is actually asking when they see Claude produce a polished,
on-brand funding digest slide on request:

> **Does Claude already know what belongs in a good funding digest, or does
> something have to tell it?**

The wrong guess a newcomer makes: that Claude is exercising its own judgment
about what counts as market-relevant news — reading the room the way an
analyst would. The correction: Claude is *told* — it reads a Skill (a file)
before acting, and that file is what fixes the exact trigger phrases, the
exact output format, and the exact fields (valuation data, Capital IQ deal
links) that training alone would not reliably standardize run to run.

## What carries over from the source (facts, unchanged)

- The skill's full stated description, quoted above verbatim.
- 3-file anatomy: `LICENSE` (11k), `SKILL.md` (29k), `references/`.
- Linear pipeline: read the file, execute steps in order, return the result.
- Output is a single PPTX slide, not a report or a deck.

## What changes (register, per the redo contract)

- **Teardown → Plain.** The source's B03 (`SkillTeardownMechanism`, narration:
  "What it gets right: repeatable results. What it bites: anything outside the
  spec.") and `BVDT` (`ClaudeVerdictArtifact`, a card literally titled
  "Verdict") are both a design-quality judgment on the skill. Plain drops that
  frame. `B01` (`SkillTeardownAnatomy`) and `B02` (`SkillTeardownPipeline`) are
  reused verbatim — their narration and their components' props were already
  descriptive, not evaluative, in the source. The B03/BVDT pair is replaced by
  one **both-directions** beat (`MedhavyTwoColumnCard`, prop-driven, no
  baked-in verdict framing) stating the identical underlying facts — named
  triggers get the same fixed output; anything the file never names has
  nothing backing it — as two directions rather than a grade, followed by a
  plain carry-out sentence (`WantQuote`) instead of a verdict card.
- **Cold open:** source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`
  (WRITER LAW).
- **Outro:** source's single `ClaudeTitleOutro` → the fixed hai-simple
  `OutroSeries` + `OutroCTA` split, Humanitarians AI skin.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
