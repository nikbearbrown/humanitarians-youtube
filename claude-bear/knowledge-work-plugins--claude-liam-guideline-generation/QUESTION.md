# QUESTION — knowledge-work-plugins--claude-liam-guideline-generation

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-guideline-generation/beat_sheet.json`.
This source sheet's narration carries an unfilled template gap: several
narration strings and one Remotion prop (`B03.body`) contain a literal `>`
where a per-skill description sentence should have interpolated (a batch
build defect, not a design choice — confirmed by diffing against sibling
sheets in the same batch, e.g. `claude-liam-accessibility-review` and
`claude-liam-analyze`, where the equivalent slot is filled with the skill's
one-line description). The description sentence itself IS present, intact,
in two other fields of this same source sheet that did interpolate
correctly: `B00.shot.remotion.props.output[1]` and
`BVDT.shot.remotion.props.artifactLines[1]`, both reading verbatim
**"Generates brand voice guidelines from source materials."** This redo
uses that intact, source-confirmed sentence to fill every `>` gap — no
external file was read or invented; the fact was already in the document,
just not in the one field that broke. The `source_skill` path the source
names (`/Users/bear/Documents/CoWork/bear-textbooks/.../guideline-generation/SKILL.md`)
does not exist on this machine (different machine's home directory) and
was not needed for this reason.

Facts preserved from the source, confirmed by its *own* intact fields (not
reconstructed): the skill is `guideline-generation`; it generates brand
voice guidelines from source materials; it is a folder Claude reads before
it works, containing `SKILL.md` (6k) plus a `references/` folder (source
B01, "2 files total"); Claude reads the Steps section and executes each
step in order, linearly, with no branching unless a step says so (source
B02); same input produces the same output every run, and the skill's
coverage is bounded by what `SKILL.md` specifies (source BVDT, both fields
intact in that beat).

**What changes in this redo:** register Teardown → Plain. The source's B03
framed "what it gets right / what it bites" as a design-tell verdict —
removed; Plain keeps only the mechanism (read source material, extract the
patterns the file defines, structure them, return the guideline) and its
two failure directions, no verdict on the design. The source's 7-beat shape
(cold open / anatomy / pipeline / design tell / verdict / handoff / outro)
carried no WRONG-GUESS, ANCHOR, or BOTH-DIRECTIONS beat — this redo's
Phase 1 structure requires them, so they are new: the wrong guess (a
newcomer assumes a brand voice guideline comes from Claude's own literary
taste — an editor's ear for what the writing should sound like) falsified
by what the skill actually is (a written specification that pulls the same
kind of patterns from source material every time, regardless of whose
writing it is; ask it to judge whether a voice is any good and there is no
step written for that); an anchor (ten of a company's own blog posts,
handed over for a brand voice guideline: read → extract → structure →
return, landing on one guideline document built from patterns already
sitting in those ten posts) planted at B02 and paid off at B03; both
directions at B03 (feed the same ten posts through twice and the guideline
comes back identical — holds; ask whether the voice in those posts is
actually a *good* one and there is nothing tailored to reach for — flips).
B00 replaces the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("taste" → "your samples" — the
naive assumption that the guideline comes from Claude's own taste,
corrected to: it's built from the material you hand it). Close re-skinned
to `OutroCTA` / @HumanitariansAI with Liam's sign-off. No source beat was
AI-VIDEO, pantry, or a human-drop slot — every source beat was already
REMOTION (`ClaudeComposerAsk`, `SkillTeardownAnatomy`,
`SkillTeardownPipeline`, `SkillTeardownMechanism`, `ClaudeVerdictArtifact`,
`ClaudeTitleOutro`), so NO-GENAI/NO-PANTRY LAW required no beat replacement
beyond B00 itself.

**Question this reel actually answers:** Does a Claude brand voice
guideline come from Claude's own taste in good writing — or is it
something narrower?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
