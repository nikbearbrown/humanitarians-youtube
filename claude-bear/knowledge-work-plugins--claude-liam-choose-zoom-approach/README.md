# How Does Claude Choose a Zoom Approach?

Ask "which Zoom API should I use?" and it's tempting to assume there's one
API to reach for. There isn't. Anthropic's `choose-zoom-approach` skill
reads a written SKILL.md and matches a use case's actual shape — an event
to be told about, a live meeting to embed, a voice call, an agent
tool-call — against a fixed list of surfaces: REST API, Webhooks,
WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP, Phone, Contact
Center, or a hybrid of two. Watch the anchor: "notify us the instant a
meeting ends" is an event, not a value to look up — ask the REST API for
that and you'd have to poll it repeatedly, arriving late every time. A
webhook fires the moment it happens, no polling at all. Matching the right
surface doesn't finish the build — you still write the endpoint — and a
use case that needs two things at once isn't a failure of the list: a
hybrid of two surfaces is one of the answers on it, not an exception.

**Topic:** CHOOSE-ZOOM-APPROACH · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-choose-zoom-approach

---

## Chapters

0:00 Which Zoom API should I use?
0:12 One API for everything, or matched surfaces?
0:32 One use case, nine surfaces
0:52 Match confirmed — now what?
1:14 Carry-out
1:23 Your turn
1:39 Outro

---

## YOUR TURN

"I have a Zoom use case: notify our support queue the moment a scheduled
call no-shows. Read the choose-zoom-approach skill and walk me through
which surface it picks, and why, before you touch any code."

Why it's worth running: naming the use case's shape out loud before the
tool call is what surfaces the real constraint logic — the same clause
the source skill's own handoff insisted on.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-choose-zoom-approach`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the
`choose-zoom-approach` skill picks the right Zoom architecture for a use
case among REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom
Apps SDK, Zoom MCP, Phone, Contact Center, or a hybrid approach — every
surface named here is stated verbatim from the source sheet's own
narration, not invented. The skill names the surface; it does not write
the integration code.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #AnthropicSkills #Zoom #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
