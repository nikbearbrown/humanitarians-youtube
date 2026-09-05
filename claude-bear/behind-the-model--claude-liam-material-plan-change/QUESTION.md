# QUESTION

**The question:** When an agent's plan has to change mid-task, should it tell
you what it did after the fact, or stop and ask before it does it?

**Mode:** redo — source is
`anthropics/youtube/behind-the-model/claude-liam-material-plan-change/beat_sheet.json`
("Material Plan Change: Stop Before the Scope Shifts," Teardown-register,
`brand: "claude-liam"`, cold open a `ClaudeComposerAsk` instruction card,
CARD/Manim body beats B01–B04, a short `B05` handoff line, `YOURTURN`,
`ClaudeTitleOutro`). The source's body narration (B01–B04) was fully written;
the facts carry forward compressed for the Plain register and the hai-simple
ten-beat shape.

**Why it earns a reel:** the natural assumption is that an agent adapting
mid-task is fine as long as it tells you afterward — a completion report that
lists what it had to do differently. But agents adapt constantly (a tool
fails, a file is missing, a format is unexpected — source B01), and by the
time a report exists, the adaptation has already happened: a library got
installed, a folder got read, a shared destination got used. None of that is
reversible by reading about it after the fact.

**Naive framing (B00, corrected on screen):** "My agent keeps adapting the
plan on its own. When should it tell me after it changes something?" →
corrects "after" to "before" (the real frame: material changes need
confirmation before they happen, not a report after).

**Body facts carried from source (unchanged):**
- agents adapt constantly, and adaptation itself is a normal feature of how
  they work, not a bug — the question is only whether the adaptation stays
  inside what was authorized (source B01)
- three concrete adaptations that feel small from inside — reading one extra
  file, sending output to a shared folder, installing a library — are each a
  real scope expansion: more data touched, more permissions used, a new
  dependency introduced (source B02)
- the material-plan-change rule has three triggers: a different tool than
  approved, data beyond what was named, or a higher risk level than the
  original plan; if any fires, the agent stops before proceeding, not after
  (source B03)
- reporting a scope change after the action is an audit log; asking before
  the action is supervision — only asking before can still change what
  happens (source B03/B04)
- the resulting design is one clause added to the task brief: on any of the
  three triggers, stop and report what you would do and why, before
  proceeding, and wait for a response (source B05 handoff line)

**Compression, per the constitution/IVP/IAG redo precedent:** ten beats —
B00 (writer) + B01–B06 (body) + BCRY + BHTF + BOUT. B01 plants the anchor (a
concrete multi-step plan the agent starts adapting) and states that
adaptation itself is normal. B02 states the wrong guess (a report afterward
is enough). B03 breaks it with the anchor's own case and states the three
triggers. B04 states the before/after mechanism (before = supervision, after
= audit). B05 covers direction A (stopping for every small in-scope
adaptation is its own failure — nobody keeps approving that). B06 covers
direction B (a report after the fact isn't worthless, it just can't undo
what already happened) and pays off the anchor.

**No inference flag.** Every claim here describes a design practice —
where a confirmation step sits in an agent's task brief, and what three
properties make a plan change worth stopping for — rather than an empirical
claim about model internals needing a hedge. Per `simple`'s ONE-FLAG LAW: "if
the source genuinely supports everything, there is no flag."
