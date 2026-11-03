# Two APIs, Not One. — The Confluence API Skill

Confluence Cloud actually runs two REST API generations at once. Claude
defaults to the newer one, v2, for everyday work — pages, spaces, blog
posts, comments, attachments, and labels. It only drops to the older v1
API for three jobs v2 can't do: searching with Confluence's query
language, uploading or downloading an attachment, and adding a label.
Three small scripts cover the hot path, and two concrete traps sit right
at the boundary of that routing: every call needs a `/wiki` prefix or it
404s outright, and the two API versions build their "next page" link
differently, so getting the direction backwards silently truncates a
search instead of erroring. Underneath all of it sits one rule that
matters more than any API detail: whatever a Confluence page says, Claude
reads it as content to report, never as a command to run.

**Topic:** CONFLUENCE API · CLAUDE TAG PLUGIN
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-confluence-api

---

## Chapters

0:00 The naive framing: "Claude just calls one Confluence API"
0:10 Two versions, three scripts
0:44 Miss /wiki, get a 404
1:17 Read it. Don't obey it.
1:59 Carry-out
2:11 Your turn
2:33 Outro

---

## YOUR TURN

Search our Confluence space for pages about onboarding, then read the most
recently updated match and summarize it for me. Before you show me
anything from inside that page, tell me plainly whether you're giving me
your own summary or quoting the page's own words.

Run that today, on your own Confluence space, not the video's example.

---

## Deliberately not claimed

No claim that v1 is deprecated or going away — it's the correct, current
choice for search, uploads, and labels, not a legacy fallback for
something broken in v2. No claim that this reel rates the Confluence API
skill's documentation as good or bad — the facts it surfaces (the `/wiki`
prefix, the pagination trap, a couple of easy-to-miss details) are things
to know, not a verdict on how well the skill's own docs are written.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
