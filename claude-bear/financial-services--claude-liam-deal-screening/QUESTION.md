# QUESTION — financial-services--claude-liam-deal-screening

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-deal-screening/beat_sheet.json`.
That source sheet's narration carries real, specific facts about the
Anthropic `deal-screening` skill: it quickly screens inbound deal flow —
CIMs, teasers, and broker materials — against a fund's investment criteria;
it extracts key deal metrics, runs a pass/fail framework, and outputs a
one-page screening memo; it is used when reviewing new deal flow, triaging
inbound materials, or deciding whether to take a first call; and it
triggers on "screen this deal," "review this CIM," "should we look at
this," "triage this teaser," or "deal screening." Claude reads SKILL.md
before acting (source B01, anatomy: "a skill is a folder... the file is
the program") and executes the Steps section in order, linearly, with no
branching unless a step says so (source B02, pipeline). Source B03 (design
tell) and BVDT (verdict) both state the same limit twice, once as "design
tell" and once as "verdict": deal-screening's job is specifically to screen
deal flow against stated criteria and produce a memo; it gets repeatable
results (same input, same output, every run); and its limit is that it
only does what the SKILL.md's steps say — nothing outside the spec. The
`source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/vertical-plugins/private-equity/skills/deal-screening/SKILL.md`)
does not exist on this machine (different machine's home directory), but
the source *beat_sheet.json*'s own narration already states the skill's
scope in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown → Plain. The source's B03
framed the skill's scope as a "design tell" verdict — "what it gets right"
/ "what it bites" — Teardown judgment language; that framing is removed,
leaving only the mechanism (a fixed spec, executed the same way every run)
and its plain consequence (nothing outside the spec is in scope). The
source's 7-beat shape (cold open / anatomy / pipeline / design tell /
verdict / handoff / outro) carries no dedicated WRONG-GUESS or ANCHOR
beat — Teardown's shape does not require them, and, as with the
`cim-builder` and `claude-plugins-official--claude-liam-agent-development`
siblings (same shape: thin Teardown body, no separate wrong-guess/anchor
material to redistribute), the source's single running example — the
deal-screening skill itself, named at B00 and never dropped through the
body — already fills the anchor's job: there is nothing separate to plant
and pay off, because it never leaves the frame. So the wrong guess is
carried entirely by B00's WRITER LAW correction, and no beat is invented to
hold a case that does not exist in the source. B00 replaces the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per WRITER
LAW: trigger word "decide" → "screen" — the naive assumption that the
skill decides whether the fund should pursue the deal, corrected to: it
screens the deal against stated criteria and hands back a memo; a person
still decides. BVDT's verdict facts are folded into the single BCRY
carry-out sentence, per CARRY-OUT LAW, rather than kept as a separate
bulleted artifact card. Close re-skinned to `OutroSeries` /
@HumanitariansAI with Liam's sign-off.

No source beat was AI-VIDEO, pantry, or a human-drop slot — the source's
final build was already entirely REMOTION (`ClaudeComposerAsk`,
`SkillTeardownAnatomy`, `SkillTeardownPipeline`, `SkillTeardownMechanism`,
`ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW
required no beat replacement beyond B00's mandated cold-open swap.

**Question this reel actually answers:** Does the deal-screening skill
decide whether the fund should do the deal — or does it just screen the
materials against your criteria and hand you a memo?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
