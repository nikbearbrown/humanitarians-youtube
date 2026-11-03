# QUESTION.md

**Question:** When Claude reviews an IP clause in a contract, is it judging
whether the clause is "good" — or is it checking the clause against a fixed
list of things that go wrong?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-ip-clause-review`), a Teardown reel under
`anthropics/claude-for-legal/youtube/claude-liam-ip-clause-review/` that
walks the `ip-clause-review` Anthropic Skill. Not a live viewer submission.

**Name usable:** N/A (no submitter).

**Source note:** the source `beat_sheet.json` was a batch build whose
narration carries literal unfilled template placeholders (the `>` marks in
B00/B03/BVDT/BHTF) — the specific contract clause the skill checks was never
written in. The question, mechanism claims (a Skill is a folder; SKILL.md
holds the instruction set; Claude reads it and executes steps linearly), and
verdict shape (reliable execution, limited to what the file says) carry over
unchanged. The one concrete "specific rule" beat (source B03/BVDT) is filled
in here with a generic, true-by-definition fact about IP clauses rather than
an invented one: a clause that only *licenses* rights does not transfer
ownership — only a clause that *assigns* rights does. That distinction is
the actual reason an "IP clause review" is a task worth having a Skill for,
and it needs no invented Claude feature or fabricated UI to state.
