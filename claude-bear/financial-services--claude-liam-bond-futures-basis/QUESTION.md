# QUESTION — financial-services--claude-liam-bond-futures-basis

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-bond-futures-basis/beat_sheet.json`.
Like its sibling redo `financial-services--claude-liam-3-statement-model`,
this source sheet is NOT a placeholder shell — its narration carries real,
specific facts about the Anthropic `bond-futures-basis` skill: it prices
bond futures, identifies the cheapest-to-deliver (CTD) bond, and compares
against yield curves to assess delivery-option value and basis-trading
opportunities; it is triggered when analyzing bond futures, computing the
basis, identifying CTD bonds, calculating implied repo rates, or evaluating
basis trades. Claude reads its `SKILL.md` before acting and executes the
steps linearly. The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/partner-built/lseg/skills/bond-futures-basis/SKILL.md`)
does not exist on this machine (different machine's home directory), but
the source *beat_sheet.json*'s own narration already states the skill's
function in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown -> Plain (the source's B03
framed "what it gets right / where it bites" as a design-tell verdict; that
judgment is removed, only the mechanism and its two failure directions
remain). The source's 7-beat shape (cold open / anatomy / pipeline / design
tell / verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer
assumes finding the cheapest bond to deliver takes a trader's feel for
which bond will perform best) falsified by what the skill actually is (it
prices every eligible bond against the futures contract by its conversion
factor and ranks them by computed delivery cost — ask it to favor a bond
because you like its prospects and it won't); the anchor (one bond's price
and conversion factor combine into a delivery cost, which becomes its
implied repo rate) planted at B02 and paid off at B03; both directions at
B03 (finding the cheapest bond to deliver is not the same as finding a
profitable trade — the implied repo rate can sit below the market's actual
financing cost; and a bond ranked expensive today is not permanently
excluded — yields move, so the ranking gets rerun, not assumed fixed). B00
replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("feel" -> "the math" — the naive
assumption that finding the cheapest bond takes trading feel, corrected to:
it takes a computed comparison). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off, per hai-simple's channel skin.

**Question this reel actually answers:** Does Claude find the cheapest bond
to deliver into a futures contract by trading feel — a sense for which
bond will perform best — or is it running a fixed, computed comparison?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
