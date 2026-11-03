# QUESTION — financial-services--claude-liam-kyc-doc-parse

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-kyc-doc-parse/beat_sheet.json`.
This source sheet's narration already carries real, specific facts about the
Anthropic `kyc-doc-parse` skill: it parses an investor or client onboarding
packet into **structured KYC fields** — identity, ownership, control, source
of funds, and document inventory — and is used as the **first step** of KYC
screening; its output feeds a downstream rules engine. The skill is a
SKILL.md instruction set Claude reads before acting; execution is linear
(read the file, execute each step in order, return output). Same input
produces the same output every run; the skill is limited to only what the
SKILL.md specifies. The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/kyc-screener/skills/kyc-doc-parse/SKILL.md`)
does not exist on this machine (different machine's home directory, same
situation as the `initiating-coverage` and `clean-data-xls` sibling redos),
but the source *beat_sheet.json*'s own narration already states the skill's
function in enough detail to redo faithfully. No reconstruction needed.

**What changes in this redo:** register Teardown → Plain. The source's B03
"design tell" framed the skill as "what it gets right: repeatable results /
what it bites: anything outside the spec" — Teardown judgment on the design
choice itself. Plain keeps only the mechanism (parse into five structured
field categories, feed the rules engine) and its two failure directions, no
verdict on whether the skill was built well. The source's 7-beat shape (cold
open / anatomy / pipeline / design tell / verdict / handoff / outro) carried
no WRONG-GUESS, ANCHOR, or BOTH-DIRECTIONS beat — Teardown's shape does not
require them. This redo's Phase 1 structure does, so those are new: the
wrong guess (a newcomer assumes "parse KYC fields" means the skill also
judges or clears the client — decides whether they pass screening) falsified
by what the skill actually is (it only extracts what's already on the page
into the five field categories; feed it a packet with the beneficial-owner
section left blank and it doesn't raise an alarm — it records that field as
missing and returns the rest of the packet, parsed, exactly as instructed);
the anchor (one onboarding packet's data landing in all five field
buckets — identity, ownership, control, source of funds, document
inventory — planted at B02 and paid off at B03); both directions at B03 (a
complete set of fields is captured data, not a cleared client — the rules
engine downstream still has to screen it; a field marked missing isn't
proof of fraud either — the document may simply not have been submitted
yet). B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("approve" → "parse it into
fields" — the naive assumption that the skill approves or clears a client,
corrected to: it only parses the packet into structured fields). Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off, per
hai-simple's channel skin. No source beat was AI-VIDEO, pantry, or a
human-drop slot — every source beat was already REMOTION
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so
NO-GENAI/NO-PANTRY LAW required no beat replacement beyond B00 itself.

**Question this reel actually answers:** When Claude "parses" a client's
KYC onboarding packet, does it decide whether the client passes screening —
or is it doing something narrower?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
