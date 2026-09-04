# Does Claude Send Your Legal Replies, or Just Draft Them?

Ask whether Claude's `legal-response` skill handles a legal matter start to
finish — reads a subpoena, drafts a reply, and sends it — and that's a
reasonable first guess. It's not what's happening. Anthropic's
`legal-response` skill reads a written SKILL.md and only matches the
inquiry to one of its configured templates, assembles a draft, and runs an
escalation check before anything moves further. Watch the anchor: one
data-subject request walked through inquiry, template match, draft
assembled, escalation check, held for review — never sent. Send it a
request that doesn't fit any template — a subpoena with unusual terms, say
— and it doesn't force a reply anyway: it flags the situation for
escalation and stops. A draft that's ready isn't a reply that's sent — a
human still has to read it and decide. And a flagged escalation isn't a
legal opinion either — it just means the skill declined to guess, so
someone still has to write the actual response. legal-response doesn't
decide how to handle a legal matter or send anything on its own — a
finished draft means the words are ready, not that anyone approved sending
it.

**Topic:** LEGAL-RESPONSE · ANTHROPIC SKILL
**Playlist:** Extending Claude — Skills, Plugins & Connectors
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/knowledge-work-plugins--claude-liam-legal-response

---

## Chapters

0:00 What does the skill do with a subpoena — just send?
0:10 Handles it, or drafts it?
0:31 One request, five stages
0:47 Held, with a catch
1:05 Carry-out
1:21 Your turn
1:40 Outro

---

## YOUR TURN

"Take a routine written request you get often — a scheduling ask, a data
question, a standard vendor email. Ask Claude to draft a reply from a
fixed template you give it, and to flag rather than answer if the request
doesn't fit. Then send it something that clearly doesn't fit the
template, and see whether it flags instead of guessing."

Watching the drafter refuse to force a reply onto a request that doesn't
fit is the fastest way to see that assembling a templated answer and
deciding what to say about something unusual are two different jobs.

---

## Deliberately not claimed

This reel redoes a published Teardown-register skill-showcase reel
(`claude-liam-legal-response`) in the Plain register for a general
audience. The underlying facts are unchanged from the source: the skill
generates a response to a common legal inquiry using configured templates,
with built-in escalation checks for situations that shouldn't use a
templated reply, and always presents the draft for user review before
suggesting it be sent — it does not itself decide how to handle a legal
matter or send anything. This script makes no claim about any specific
client, law firm, or document format — only the general mechanism
(template-and-escalation) and its two failure directions.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #LegalTech #Compliance #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics
