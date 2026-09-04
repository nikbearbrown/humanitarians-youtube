# The Data Source, Not the Database. — The Notion API Skill

Notion's content model has a twist that trips up anyone who assumes "the
database" is one flat thing with one ID. A database is a container; the
data it actually holds — the schema, and every row — lives in a separate
object called a data source, with its own ID. Schema reads, queries, and
creating a new row all need that data source ID, not the database's. Two
smaller traps sit right alongside it: every request needs a specific
version header or it fails outright, and a 404 almost never means a bad
ID — it almost always means the page or database was never shared with
Claude's connection.

**Topic:** NOTION API · CLAUDE TAG PLUGIN
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-notion-api

---

## Chapters

0:00 The naive framing: "Claude just needs the database ID"
0:12 One database, two IDs
0:46 Missing version, missing share
1:10 Listed, not opened
1:47 Carry-out
2:01 Your turn
2:21 Outro

---

## YOUR TURN

Search my Notion workspace for pages about onboarding, then read the most
recently updated match and summarize it for me in your own words. If
reaching that page means querying a database along the way, tell me out
loud whether you're using the database's own ID or the data source ID
underneath it.

Run that today, on your own Notion workspace, not the video's example.

---

## Deliberately not claimed

No claim that the database ID is useless — it's exactly what you retrieve
first, in order to read its `data_sources` list and find the ID that
actually matters. No claim that this reel rates the Notion API skill's
documentation as good or bad — the facts it surfaces (missing recursion
into sub-pages, expiring file URLs, an unguarded pagination loop,
property-typed filters) are things to know, not a verdict on how well the
skill's own docs are written.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeSkills #ClaudePlugins #ClaudeCode #LLM #HumanitariansAI #ProfessorBear

---
