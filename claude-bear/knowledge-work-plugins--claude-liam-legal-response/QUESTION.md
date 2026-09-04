# QUESTION — knowledge-work-plugins--claude-liam-legal-response

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-legal-response/beat_sheet.json`.
This source sheet's narration already carries real, specific facts about the
Anthropic `legal-response` skill: it generates a response to a common legal
inquiry using **configured templates**, with **built-in escalation checks**
for situations that shouldn't use a templated reply — used when responding
to data subject requests, litigation hold notices, vendor legal questions,
NDA requests from business teams, or subpoenas. The skill's stated design
constraint: **always present the draft response for user review before
suggesting it be sent.** The skill is a SKILL.md instruction set Claude reads
before acting; execution is linear (read the file, execute each step in
order, return output). Same input produces the same output every run; the
skill is limited to only what the SKILL.md specifies. The `source_skill`
path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/knowledge-work-plugins/legal/skills/legal-response/SKILL.md`)
does not exist on this machine (different machine's home directory, same
situation as the `financial-services` sibling redos — e.g.
`claude-liam-kyc-doc-parse`), but the source *beat_sheet.json*'s own
narration already states the skill's function in enough detail to redo
faithfully. No reconstruction needed.

**What changes in this redo:** register Teardown → Plain. The source's BVDT
verdict framed the skill's reliability and its limit ("know the limit: only
what the file says") as a Teardown recap; Plain keeps only the mechanism
(match to a template, draft, escalation check, hold for review) and its two
failure directions, no verdict on whether the skill was built well. The
source's 7-beat shape (cold open / anatomy / pipeline / design tell /
verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape does not require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer
assumes "respond to a legal inquiry" means the skill reads the request,
drafts a reply, and sends it — handling the matter start to finish),
falsified by the skill's actual escalation check (send it a request that
doesn't fit any configured template — a subpoena with unusual terms, say —
and it doesn't force a templated reply anyway; it flags the situation for
escalation and stops, because a bespoke legal answer isn't a job a template
can do); the anchor (one data-subject request walked through the pipeline —
inquiry, template match, draft assembled, escalation check, held for
review — planted at B02 and paid off at B03); both directions at B03 (a
drafted reply that's ready to review isn't a reply that's been sent — a
human still has to read it and decide; and a flagged escalation isn't a
legal opinion either — it just means the skill declined to guess, so a
person still has to write the actual response). B00 replaced the source's
`ClaudeComposerAsk` cold open with `BrutalistHesitantWriter` per WRITER LAW
("send" → "draft it for review" — the naive assumption that the
skill sends its own answer, corrected to: it drafts, then waits). Close
re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off, per
hai-simple's channel skin. No source beat was AI-VIDEO, pantry, or a
human-drop slot — every source beat was already REMOTION
(`ClaudeComposerAsk`, `SkillTeardownAnatomy`, `SkillTeardownPipeline`,
`SkillTeardownMechanism`, `ClaudeVerdictArtifact`, `ClaudeTitleOutro`), so
NO-GENAI/NO-PANTRY LAW required no beat replacement beyond B00 itself.

**Question this reel actually answers:** When Claude "responds" to a legal
inquiry — a subpoena, a data subject request, a litigation hold notice —
does it decide how to answer and send that reply, or is it doing something
narrower?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
