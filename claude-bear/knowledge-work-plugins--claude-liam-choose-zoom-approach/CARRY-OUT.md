# CARRY-OUT — knowledge-work-plugins--claude-liam-choose-zoom-approach

**The line (written first, GATE C):**

> Picking a Zoom integration isn't picking one API — it's matching what
> the use case needs to one of several surfaces, and combining two of them
> when one isn't enough.

**Test:** if someone repeats only this in a meeting next week, is it still
true? Yes — it compresses the one distinction the reel is built to land
(matching need-to-surface vs. reaching for a single default API), not the
topic (Zoom integration generally).

**The wrong guess it defeats:** that "which Zoom API should I use" is the
right question — as if Zoom offered one integration surface and the only
decision was whether to use it. It doesn't work that way. The
`choose-zoom-approach` skill reads a written SKILL.md and matches a use
case's actual shape — an event to be told about, a live meeting to embed,
a voice call, an agent tool-call — against a fixed list of surfaces: REST
API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP,
Phone, Contact Center, or a hybrid of two. Ask the REST API to tell you the
instant a meeting ends and it won't — you'd have to poll it repeatedly,
arriving late every time. A webhook fires the moment it happens, no
polling at all.

**GATE C — signed:** derived directly from the source sheet's own stated
facts (see QUESTION.md) — the source beat_sheet.json's narration already
states the skill's scope (the nine-plus named surfaces and the hybrid
option); this line compresses it into the reel's carry-out.
