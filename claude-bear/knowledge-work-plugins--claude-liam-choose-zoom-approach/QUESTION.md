# QUESTION — knowledge-work-plugins--claude-liam-choose-zoom-approach

**Source note (redo mode, read before anything else):** `SUBJECT.json` points
`source_sheet` at
`/Users/nik/Documents/books/anthropics/knowledge-work-plugins/youtube/claude-liam-choose-zoom-approach/beat_sheet.json`.
That source sheet's narration carries real, specific facts about the
Anthropic `choose-zoom-approach` skill: it chooses the right Zoom
architecture for a use case, deciding between REST API, Webhooks,
WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP, Phone, Contact
Center, or a hybrid approach. Claude reads its `SKILL.md` before acting and
executes the Steps section linearly, no branching unless a step says so.
The `source_skill` path it names
(`/Users/bear/Documents/CoWork/bear-textbooks/.../zoom-plugin/skills/choose-zoom-approach/SKILL.md`)
does not exist on this machine (different machine's home directory), but
the source *beat_sheet.json*'s own narration already states the skill's
scope (the nine-plus named surfaces) in enough detail to redo faithfully —
no reconstruction needed.

**What changes in this redo:** register Teardown → Plain. The source's B03
framed "what it gets right / what it bites" as a design-tell verdict on
the skill's construction — Plain keeps only the mechanism and its two
failure directions, no verdict on whether the skill was built well. The
source's 7-beat shape (cold open / anatomy / pipeline / design tell /
verdict / handoff / outro) carried no WRONG-GUESS, ANCHOR, or
BOTH-DIRECTIONS beat — Teardown's shape doesn't require them. This redo's
Phase 1 structure does, so those are new: the wrong guess (a newcomer
assumes "which Zoom API should I use" means Zoom has one integration
surface to reach for) falsified by a concrete case (asking the REST API to
tell you the instant a meeting ends means polling it over and over,
arriving late every time — a webhook fires the moment it happens, no
polling at all); the anchor is a single concrete use case — "notify us the
instant a meeting ends" — resolved to Webhooks by shape (an event to be
told about, not a value to look up), planted at B02 and paid off at B03;
both directions at B03 (matching the right surface doesn't finish the
build — you still write the endpoint and handle the request; and a use
case that needs two things at once isn't a failure of the list — a hybrid
of two surfaces is one of the answers on it, not an exception to it). B00
replaced the source's `ClaudeComposerAsk` cold open (itself already
Remotion, not a puppet — no NO-GENAI violation in the source) with
`BrutalistHesitantWriter` per WRITER LAW ("API" → "approach" — the naive
assumption that there's one Zoom API to call, corrected to: it's a choice
of approach among several). Close re-skinned to `OutroCTA` /
@HumanitariansAI with Liam's sign-off, per hai-simple's channel skin. Kept
the source's 7-beat count (B00, B01, B02, B03, BCRY, BHTF, BOUT).

**Question this reel actually answers:** Is choosing how Claude integrates
with Zoom a matter of picking one API — or matching what the use case
actually needs to one of several different Zoom surfaces?

**Who asked, where:** nobody — this is a factory redo of a published
skill-teardown reel into the hai-simple format; see SUBJECT.json.
**Name usable:** n/a.
