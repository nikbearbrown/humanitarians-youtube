# QUESTION — claude-for-legal--claude-liam-infringement-triage

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/claude-for-legal/youtube/claude-liam-infringement-triage/beat_sheet.json`.
That sheet exists and is fully "built" (7 beats, all marked VIDEO/filled), but
its narration text carries **literal, never-filled template placeholders**
(`>`) at every point where the actual skill-specific fact should be —
`"The skill is infringement-triage. >."`, `"Claude's job: >."`, `"The
SKILL.md is the spec — >."`, `"I want to >."` The `source_skill` field it
names,
`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/ip-legal/skills/infringement-triage/SKILL.md`,
does not exist anywhere on this machine (`/Users/bear/Documents/CoWork` does
not exist at all; searched the whole `books/` tree for any `ip-legal` folder
or `infringement-triage` SKILL.md — no match). Same defect class already
logged and worked around on sibling `claude-for-legal--*` redos in this
factory (`-ai-inventory`, `-ai-tool-handoff`, `-amendment-history`,
`-board-minutes`, `-dsar-response`).

**The call (logged, not asked):** rather than block on a missing human
answer, this build reconstructs the evident subject from the title
("INFRINGEMENT-TRIAGE") and the family (`claude-for-legal`, an IP-legal
practice skill) into a generic, defensible account of what triaging an
incoming infringement claim/letter means and why sorting comes before
responding — the same kind of intake practice the skill's name unambiguously
points at, described generically per the fresh-script Phase 1 rule ("when in
doubt, describe behavior generically") rather than inventing specific tool
names, UI, or product claims. No fact here is Claude-specific or
unverifiable; it is the general shape of an infringement-triage practice (who
is asserting the claim, what specific right they claim, what evidence is
attached, what deadline is demanded) as used in IP-legal intake broadly.

**Question this reel actually answers:** An infringement letter — a
cease-and-desist, a takedown notice, an accusation that your product copies
someone else's — lands in the inbox. What's the first move: respond to it,
or triage it first?

**Who asked, where:** nobody — reconstructed per the note above.
**Name usable:** n/a.
