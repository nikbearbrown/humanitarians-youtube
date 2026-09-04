# QUESTION — financial-services--claude-liam-audit-xls

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-audit-xls/beat_sheet.json`.
This source sheet is NOT a placeholder shell — its narration carries real,
specific facts about the Anthropic `audit-xls` skill: it audits a
spreadsheet for formula accuracy, errors, and common mistakes; it scopes to
a selected range, a single sheet, or the entire model, including
financial-model integrity checks like BS balance, cash tie-out, and logic
sanity; it triggers on phrases like "audit this sheet", "check my
formulas", "find formula errors", "QA this spreadsheet", "sanity check
this", "debug model", "model won't balance", "something's off in my
model". Claude reads `SKILL.md` before acting and executes the steps
linearly (source anatomy/pipeline beats: one file, read → execute →
return). The design tell the source states: BS balance is checked first —
if it doesn't balance, everything downstream is suspect. The
`source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/financial-services/plugins/agent-plugins/earnings-reviewer/skills/audit-xls/SKILL.md`)
does not exist on this machine (different machine's home directory), but
the source *beat_sheet.json*'s own narration already states the skill's
function in enough detail to redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown → Plain (the source's B03
framed the BS-balance-first ordering as "the interesting constraint... a
deliberate trade-off" — Teardown design judgment; that judgment is
removed, only the mechanism and its two failure directions remain). The
source's 7-beat shape (cold open / anatomy / pipeline / design tell /
verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer
assumes "audit" means Claude will find AND repair the errors it turns up)
falsified by what the skill actually is (it reports what it finds — cites
the cell, describes the mistake — and does not rewrite the formula itself;
the sheet is unchanged when you check it afterward); the anchor (a balance
sheet that's off by a fixed amount — checked first, before anything else,
because if it doesn't balance everything downstream is suspect) planted at
B02 and paid off at B03; both directions at B03 (a clean BS-balance pass
does not mean the whole model in scope is error-free — it only clears that
one check, formula errors elsewhere are checked separately; a BS-imbalance
flag does not mean every downstream number is individually wrong — it
means they're unverified until the imbalance is resolved, not confirmed
incorrect). B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("fix" → "audit" — the naive
assumption that asking Claude to look at a broken spreadsheet means asking
it to repair it, corrected to: it audits and reports, it doesn't rewrite).
Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off, per
hai-simple's channel skin. No source beat was AI-VIDEO, pantry, or a
human-drop slot — every source beat was already REMOTION
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so
NO-GENAI/NO-PANTRY LAW required no beat replacement beyond B00 itself.

**Question this reel actually answers:** When Claude "audits" a
spreadsheet, does it find AND fix the errors — or is it doing something
narrower?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
