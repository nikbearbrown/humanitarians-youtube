# QUESTION — financial-services--claude-liam-fixed-income-portfolio

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-fixed-income-portfolio/beat_sheet.json`.
Like the `dcf-model` and `3-statement-model` siblings, this source sheet is
NOT a placeholder shell — its narration carries real, specific facts about
the Anthropic `fixed-income-portfolio` skill: it reviews fixed income
portfolios by pricing multiple bonds, retrieving reference data, analyzing
cashflows, and running scenario analysis; triggered when reviewing bond
portfolios, computing portfolio duration and DV01, analyzing cashflow
waterfalls, stress testing rate scenarios, or assessing portfolio
composition. The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/partner-built/lseg/skills/fixed-income-portfolio/SKILL.md`)
does not exist on this machine (different machine's home directory), but the
source *beat_sheet.json*'s own narration already states the skill's function
in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown -> Plain (the source's B03
framed "what it gets right / what it bites" as a design-tell verdict; that
judgment is removed, only the mechanism and its two failure directions
remain). The source's 7-beat shape (cold open / anatomy / pipeline / design
tell / verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer
assumes Claude decides how risky a bond portfolio is — the way an analyst
who has studied it forms an opinion) falsified by what the skill actually
is (it computes duration and DV01 — dollar-value-of-a-basis-point — from
the reference data it's given for each bond: coupon, maturity, current
price; feed it a different price and the numbers move without protest, it
never argues a bond is too risky); the anchor (DV01 summed across the
portfolio, then a rate shock in basis points driving a single P&L readout)
planted at B02 and paid off at B03 via the scenario/sensitivity analysis;
both directions at B03 (a portfolio that swings hard under one rate
scenario isn't necessarily poorly built — a large DV01 can be an
intentional, hedged position; a portfolio that holds steady under that one
scenario doesn't mean it's safe from rate risk generally — a bigger move,
or a shift that isn't parallel across the curve, can still hurt it). B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("judgment" -> "the numbers" — the
naive assumption that a portfolio's risk is Claude's judgment call,
corrected to: it is Claude computing duration and DV01 from the numbers it
was given). Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's
sign-off, per hai-simple's channel skin.

**Question this reel actually answers:** Does Claude decide how risky a
bond portfolio is — or is it computing duration and DV01, fixed
sensitivities to a rate move you specify?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
