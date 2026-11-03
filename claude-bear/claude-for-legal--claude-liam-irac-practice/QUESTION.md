# QUESTION.md

**Question:** When you practice IRAC (Issue, Rule, Application, Conclusion)
with Claude on a law hypo, does Claude hand you the finished answer — or
does it drill you through the four steps one at a time?

**Who asked / where:** Redo-mode reel. Source question carried over from the
locked source script (`claude-liam-irac-practice`), a Teardown reel under
`anthropics/claude-for-legal/youtube/claude-liam-irac-practice/` that walks
the `irac-practice` Anthropic Skill. Not a live viewer submission.

**Name usable:** N/A (no submitter).

**Source note:** the source `beat_sheet.json` was a batch build whose
narration for the specific-check beat (source B03/BVDT) carries literal
unfilled template placeholders (the `>` marks) — the `irac-practice`
skill's own SKILL.md (in a law-student skills collection not reachable from
this machine: `/Users/bear/Documents/CoWork/bear-textbooks/books/
anthropics/claude-for-legal/law-student/skills/irac-practice/SKILL.md`
does not exist on this machine) was never actually filled in for this
build. The question, mechanism claims (a Skill is a folder; SKILL.md holds
the instruction set; Claude reads it and executes its Steps linearly), and
verdict shape (reliable, repeatable execution, limited to what the file
says) carry over unchanged. The one concrete "specific check" beat (source
B03/BVDT) is filled in here with a generic, well-established, true fact
about IRAC itself rather than an invented one: stating the right Conclusion
without showing the Application earns no credit — the Application (the
Rule applied to the specific facts, one fact at a time) is where the actual
legal reasoning lives, and is the part IRAC exists to force. That
distinction is the actual reason "IRAC practice" is a task worth having a
Skill for, and it needs no invented Claude feature or fabricated checklist
item.
