# Ask For It, Or It Isn't There. — The HubSpot API Skill (Claude Plugins)

HubSpot's five record types — contacts, companies, deals, tickets, and
custom objects — all live under the same path:
/crm/v3/objects/{objectType}. But a plain get or list call returns only a
handful of default fields — every other property is opt-in, so you have to
name exactly what you want or the record comes back looking almost empty.
Each type has its own dedup rule (contacts on email, companies on domain),
and links between records are typed associations, discovered through their
own endpoint. And here's the catch: HubSpot's search endpoint is eventually
consistent — create a record, search for it immediately, and it might not
show up yet, because the write and the search index aren't on the same
clock.

**Topic:** HUBSPOT API · CLAUDE PLUGINS
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-hubspot-api

---

## Chapters

0:00 The naive framing: "do I get back everything?"
0:11 One path, opt-in fields
0:49 Dedup keys, typed links
1:19 The catch: search lags
1:46 Carry-out
1:57 Your turn
2:25 Outro

---

## YOUR TURN

Paste this into Claude: Use the hubspot-api skill to find all contacts in
the lead lifecycle stage created in the last 30 days, and return their email
and phone number. Then check what Claude does: does it pass
properties=email,phone, or does it come back with near-empty records? Does
it follow the pagination cursor through every page of results, or stop at
the first one? And does it mention that a contact created moments ago might
not show up in search yet, because the index takes a moment to catch up?

Run that today, on your own HubSpot workspace or a sandbox account.

---

## Deliberately not claimed

No claim about how long HubSpot's search index actually takes to catch up
after a write — the source Skill documents the eventual-consistency
behavior but gives no wait/retry guidance, and this video doesn't invent a
number. No claim that every HubSpot object type works identically end to
end; the uniform path and opt-in-properties contract are shared across all
five, but dedup keys, and which fields ship free by default, differ per
type.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeCode #ClaudeSkills #ClaudePlugins #HubSpot #LLM #HumanitariansAI #ProfessorBear

---
