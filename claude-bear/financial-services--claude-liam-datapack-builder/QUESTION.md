# QUESTION — financial-services--claude-liam-datapack-builder

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-datapack-builder/beat_sheet.json`.
That source sheet's narration carries real, specific facts about the
Anthropic `datapack-builder` skill: it builds professional financial
services data packs from various sources — CIMs, offering memorandums, SEC
filings, web search, or MCP servers — extracting, normalizing, and
standardizing the financial data into investment-committee-ready Excel
workbooks with consistent structure, proper formatting, and documented
assumptions. It's for M&A due diligence, private equity analysis,
investment committee materials, and standardizing financial reporting
across portfolio companies. It explicitly is NOT for simple financial
calculations or for working with a data pack that's already completed.
Claude reads `SKILL.md` before acting (source B01, anatomy: "a skill is a
folder... the file is the program") and executes the Steps section in
order, linearly, with no branching unless a step says so (source B02,
pipeline). Source B03 (design tell) and BVDT (verdict) both state the same
limit twice, once as "design tell" and once as "verdict": datapack-builder's
job is specifically to extract and standardize the data pack; it gets
repeatable results (same input, same output, every run); and its limit is
that it only does what the SKILL.md's steps say — nothing outside the spec,
including the numeric analysis itself. The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/vertical-plugins/investment-banking/skills/datapack-builder/SKILL.md`)
does not exist on this machine (different machine's home directory), but
the source *beat_sheet.json*'s own narration already states the skill's
scope in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown → Plain. The source's B03
framed the skill's scope as a "design tell" verdict — "what it gets right"
/ "what it bites" — Teardown judgment language; that framing is removed,
leaving only the mechanism (a fixed spec, executed the same way every run)
and its plain consequence (nothing outside the spec is in scope, including
the calculations). The source's 7-beat shape (cold open / anatomy /
pipeline / design tell / verdict / handoff / outro) carries no dedicated
WRONG-GUESS or ANCHOR beat — Teardown's shape does not require them, and
this source's single running example — the datapack-builder skill itself,
named at B00 and never dropped through the body — already fills the
anchor's job: there is nothing separate to plant and pay off, because it
never leaves the frame. So per the `cim-builder` sibling's resolution (same
shape: thin Teardown body, no separate wrong-guess/anchor material to
redistribute), the wrong guess is carried entirely by B00's WRITER LAW
correction, and no beat is invented to hold a case that does not exist in
the source. B00 replaces the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW: trigger word "calculate" →
"extract" — the naive assumption that the skill does the financial analysis
itself, the way an analyst would, corrected to: it extracts and
standardizes data from your sources into a workbook; the source's own line
("do not use for simple financial calculations") is the direct textual
basis for this correction. BVDT's verdict facts are folded into the single
BCRY carry-out sentence, per CARRY-OUT LAW, rather than kept as a separate
bulleted artifact card. Close re-skinned to `OutroSeries` / @HumanitariansAI
with Liam's sign-off, kept as one beat (not split into OutroSeries +
OutroCTA) to hold the source's exact 7-beat count, same disposition as the
`cim-builder` sibling.

No source beat was AI-VIDEO, pantry, or a human-drop slot — the source's
final build was already entirely REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW
required no beat replacement beyond B00's mandated cold-open swap.

**Question this reel actually answers:** Does the datapack-builder skill
calculate your financials the way an analyst would — or does it extract and
standardize the data you give it into one workbook?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
