# There's No REST API Here. — The Linear API Skill

Linear's API has exactly one endpoint: POST to api.linear.app/graphql. Reads
are queries, writes are mutations — everything goes through that same URL,
never a REST-style path. Two ID systems live side by side: a UUID, which the
API expects for every operation, and a human-readable identifier like
ENG-123, which only works for reading — pass an identifier where a mutation
expects a UUID and you get INVALID_INPUT back. The Authorization header
carries the key by itself, with no "Bearer" prefix, and an HTTP 200 doesn't
mean it worked: GraphQL returns 200 for most errors, with the real failure
sitting in the body under .errors. A few workflow patterns keep it
manageable — sanity-check with the viewer query, look up UUIDs before
mutating, Markdown for description and comment bodies, and check the
mutation's own success field too. The one that catches people coming from
REST: Linear's rate limit comes back as HTTP 400 with code RATELIMITED, not
the usual 429 — a retry loop built to watch for 429 never fires — and the
reset time is in epoch milliseconds, not seconds.

**Topic:** LINEAR API · GRAPHQL, NOT REST
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-linear-api

---

## Chapters

0:00 The naive framing: "how do I call the Linear REST API?"
0:12 One endpoint, two ID systems
0:51 Viewer first, then UUID
1:28 400, not 429
1:53 Carry-out
2:04 Your turn
2:24 Outro

---

## YOUR TURN

Paste this into Claude: show me the GraphQL query I'd send to list my open
issues in Linear, and the mutation to move one to "In Progress," using real
field names and IDs. For each one, tell me exactly what I'd check in the
response to know it actually worked — not just that the HTTP status came
back 200. Then tell me what changes about that check if I've been
rate-limited.

Run that today, on your own Linear workspace (or just to see the shape of
the calls), not the video's example.

---

## Deliberately not claimed

No claim about Linear API behavior outside what the linear-api skill's
source material specifies — the single endpoint, the two ID systems, the
auth header format, the HTTP-200-on-error behavior, and the rate-limit
status code are what this particular skill documents today. No claim that
the skill's documentation is poorly written; the gap named here (the
400-vs-429 distinction) is a fact about Linear's API, not a verdict on the
skill.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
