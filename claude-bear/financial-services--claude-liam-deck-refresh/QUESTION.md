# QUESTION — financial-services--claude-liam-deck-refresh

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/financial-services/youtube/claude-liam-deck-refresh/beat_sheet.json`.
That source sheet is NOT a placeholder shell — its narration carries real,
specific facts about the Anthropic `deck-refresh` skill: it updates a
presentation with new numbers (quarterly refreshes, earnings updates, comp
rolls, rebased market data); it triggers on requests like "update the deck
with Q4 numbers", "refresh the comps", "roll this forward", "swap in the
new earnings", or literally "change all the $485M to $512M" — any request
to swap figures across an existing deck without rebuilding it. Claude reads
its `SKILL.md` before acting and executes the Steps section linearly, no
branching unless a step says so. The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/.../pitch-agent/skills/deck-refresh/SKILL.md`)
does not exist on this machine (different machine's home directory), but
the source *beat_sheet.json*'s own narration already states the skill's
function and its own worked example ($485M → $512M) in enough detail to
redo faithfully — no reconstruction needed.

**What changes in this redo:** register Teardown → Plain. The source's B03
framed "what it gets right / what it bites" as a design-tell verdict on
the skill's construction — Plain keeps only the mechanism and its two
failure directions, no verdict on whether the skill was built well. The
source's 7-beat shape (cold open / anatomy / pipeline / design tell /
verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape doesn't require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer
assumes "refresh the deck" means Claude reconsiders the numbers —
rewriting the commentary and trend language along with the figure)
falsified by what the skill actually is (a fixed find-and-replace: it
swaps the figure and leaves the surrounding sentence untouched, even when
that sentence was built on the old number); the anchor is the source's own
worked example, literalized — $485M appearing in three places across the
deck (executive summary, comps table, footnote), each independently found
and swapped to $512M in slide order; both directions at B03 (every figure
changing is not the same as every sentence built on those figures still
being true; a leftover instance of the old figure is not always a miss —
it may never have been the target). B00 replaced the source's
`ClaudeComposerAsk` cold open (itself already Remotion, not a puppet — no
NO-GENAI violation in the source) with `BrutalistHesitantWriter` per
WRITER LAW ("story" → "numbers" — the naive assumption that a "refresh"
touches the deck's narrative, corrected to: it touches the numbers only).
Close re-skinned to `OutroCTA` / @HumanitariansAI with Liam's sign-off, per
hai-simple's channel skin. Kept the source's 7-beat count (B00, B01, B02,
B03, BCRY, BHTF, BOUT).

**Question this reel actually answers:** Does "refreshing a deck" mean
Claude reconsiders the story the numbers tell — or is it a narrower,
mechanical swap of one figure for another?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
