# The Routing Key, Not the Token. — The PagerDuty API Skill

PagerDuty isn't one API with one credential — it's two, on two different
hosts, with two unrelated auth schemes. The REST API (`api.pagerduty.com`)
reads and manages everything — schedules, services, escalation policies,
incidents, users — with a Token header. Events v2 (`events.pagerduty.com`)
triggers, acknowledges, and resolves alerts with a routing key in the request
body and no Authorization header at all. Mix the two up and the failure
mode isn't a clear error — it's a 401 with an empty body.

**Topic:** PAGERDUTY API · CLAUDE TAG PLUGIN
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-pagerduty-api

---

## Chapters

0:00 The naive framing: "Can Claude trigger an alert with my API TOKEN?"
0:13 Two APIs, two auth schemes
0:57 Sanity check, then From:
1:26 Needs -g, id+type, rate limits differ
2:02 Carry-out
2:17 Your turn
2:34 Outro

---

## YOUR TURN

I want to connect Claude to PagerDuty. For three tasks — checking who's on
call, triggering a test alert, and looking up why an incident paged
someone — tell me which API you'd call, which host, and exactly how you'd
authenticate for each one, before you write any code.

Run that today — no live PagerDuty account required to check the reasoning.

---

## Deliberately not claimed

No claim that the API token is useless outside Events v2 — it's exactly what
the REST API needs to look up who's on call or trace an incident's log
entries. No claim that this reel rates the PagerDuty API skill's
documentation as good or bad — the facts it surfaces (bracket-URL encoding,
the `From:` header, reference-object `type` fields, plain-text Events v2
errors, mismatched rate limits) are things to know, not a verdict on how
well the skill's own docs are written.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
