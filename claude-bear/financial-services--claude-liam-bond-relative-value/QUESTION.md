# QUESTION — financial-services--claude-liam-bond-relative-value

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-bond-relative-value/beat_sheet.json`.
This source sheet is NOT a placeholder shell — its narration carries real,
specific facts about the Anthropic `bond-relative-value` skill: it performs
relative value analysis on bonds by combining pricing, yield curve context,
credit spreads, and scenario stress testing; it is used for analyzing bond
richness/cheapness, computing spread decomposition, comparing bonds,
assessing bond value versus curves, and running rate-shock scenarios.
Claude reads `SKILL.md` before acting and executes the steps linearly
(source anatomy/pipeline beats: one file, read → execute → return; "same
input → same output, every run"; "know the limit: only what the file
says"). The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/partner-built/lseg/skills/bond-relative-value/SKILL.md`)
does not exist on this machine (different machine's home directory), but
the source *beat_sheet.json*'s own narration already states the skill's
function in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown → Plain (the source's B03
framed "what it gets right / where it bites" as a design-tell verdict; that
judgment is removed, only the mechanism and its two failure directions
remain). The source's 7-beat shape (cold open / anatomy / pipeline / design
tell / verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer
assumes Claude judges whether a bond is rich or cheap using its own market
feel, the way an experienced trader might) falsified by what the skill
actually is (it computes a relative-value read from four fixed inputs —
price, yield curve context, credit spread, and a stress-tested rate shock;
give it a bond with no yield curve to compare against and it has nothing to
spread it against, so it has nothing to read); the anchor (a ten-year
corporate bond trading forty basis points over the curve — priced, curve
read, spread decomposed, stress-tested, then it stops with a single
computed read, waiting) planted at B02 and paid off at B03; both
directions at B03 (a bond that comes back cheap by the read is not the
same as a bond worth buying — the read only reflects the curve you gave
it, and a stale curve makes a wrong read look just as confident; a bond
that comes back rich by the read does not mean avoid it — the stress
scenario can still favor holding it). B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per WRITER LAW
("feel" → "a curve" — the naive assumption that telling a bond's
richness or cheapness takes a trader's feel, corrected to: a read computed
against a yield curve). The first B00 render's narration (30 words,
9.30s) never let the writer finish typing the replacement before the
clip ended — frame-verified still mid-typing "by the s" at t=9.25s of a
9.3s clip — fixed by lengthening the narration to 35 words (10.41s,
clearing the TIMING LAW's ≥9s floor with real margin) and shortening the
replacement word from "the spread" to "a curve"; re-rendered,
re-verified the correction ("feel" → "a curve") fully lands by t=9.8s
with margin before the 10.43s clip ends. Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off, per hai-simple's channel skin.
No source beat was
AI-VIDEO, pantry, or a human-drop slot — every source beat was already
REMOTION (`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so
NO-GENAI/NO-PANTRY LAW required no beat replacement beyond B00 itself.

**Question this reel actually answers:** Does Claude tell whether a bond is
rich or cheap using its own trading feel — or is it running a fixed,
computed comparison?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
