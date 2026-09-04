# QUESTION — knowledge-work-plugins--claude-liam-digest

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-digest/beat_sheet.json`.
That source sheet's narration carries real, specific facts about the
Anthropic `digest` skill: generate a daily or weekly digest of activity
across all connected sources; use when catching up after time away, starting
the day and wanting a summary of mentions and action items, or reviewing a
week's decisions and document updates grouped by project. Claude reads
`SKILL.md` before acting and executes the steps linearly (source anatomy /
pipeline beats: one file, read → execute → return output; linear, no
branching unless a step says so). The source's design-tell beat names one
concrete constraint: "Default to --daily if no flag is specified." No
reconstruction was needed — the source's own narration states the skill's
function and its one interesting constraint in enough detail to redo
faithfully.

**What changes in this redo:** register Teardown → Plain (the source's BVDT
framed "makes Claude execute one task reliably... know the limit" as a
verdict; that judgment is removed, only the mechanism and its two failure
directions remain). The source's 7-beat shape (cold open / anatomy /
pipeline / design tell / verdict / handoff / outro) carried no WRONG-GUESS,
ANCHOR, or BOTH-DIRECTIONS beat — Teardown's shape does not require them.
This redo's Phase 1 structure does, so those are new: the wrong guess (a
newcomer assumes Claude has been quietly aware of everything happening
across their connected sources the whole time they were away, so asking for
"a digest" just taps into standing knowledge) falsified by what the skill
actually is (nothing runs until you ask, and the source's own design tell —
default to daily if no flag is specified — means that even then, asking
without saying "weekly" after a week away returns only the most recent day);
the anchor (it's Monday, you've been gone all week, you ask for a digest
without naming a window — the file's daily default fires and what comes back
covers only Friday, one day out of seven) planted at B02 and paid off at B03;
both directions at B03 (ask again with the window still unset and you get
the same one-day default, identically, every time — holds; say "weekly"
once and the same file runs the same steps across all seven days instead —
flips). B00 replaced the source's `ClaudeComposerAsk` cold open with
`BrutalistHesitantWriter` per WRITER LAW ("watching" → "waiting" — the naive
assumption that Claude keeps continuous watch, corrected to: it waits,
dormant, until asked). Close re-skinned to `OutroCTA` / @HumanitariansAI with
Liam's sign-off, per hai-simple's channel skin. No source beat was AI-VIDEO,
pantry, or a human-drop slot — every source beat was already REMOTION
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so
NO-GENAI/NO-PANTRY LAW required no beat replacement beyond B00 itself.

**Question this reel actually answers:** Has Claude been quietly keeping
track of everything across your connected sources while you were away — or
does the digest skill only run, and only cover what you told it to, the
moment you ask?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
