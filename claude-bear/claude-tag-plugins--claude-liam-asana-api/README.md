# Claude, Asana API.

Claude doesn't manage your Asana tasks by clicking around inside the app —
it calls Asana's own REST API and reads back JSON. Every response, a read
or a write, arrives wrapped under a top-level `data` key, and every object
inside it is addressed by a `gid` (a string global ID), never a name. The
objects nest the same way every time: workspace holds projects, a project
holds sections and tasks, a task carries comments and subtasks. Ask for
every incomplete task assigned to you in one project, and Claude resolves
your name to a gid, then lists tasks under that project's gid, unwrapping
`data` at each step — and if the bundled script keeps requesting until the
pages run out, the list comes back complete. Skip either habit and the
request can look successful while it quietly returns the wrong task or
only the first page. One exception worth knowing: workspace search is
capped at 100 results and doesn't paginate at all — the one operation that
doesn't follow the other nine.

**Topic:** ASANA API · CLAUDE TAG PLUGIN
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-asana-api

---

## Chapters

0:00 Claude must open the Asana app and click around. Is that it?
0:12 Not a bare list — a data envelope
0:27 Workspace to task, then one request traced through
0:45 Complete — or quietly wrong
1:11 Carry-out
1:21 Your turn
1:42 Outro

---

## YOUR TURN

"List all incomplete tasks assigned to me across all my Asana workspaces,
and tell me which ones are due this week."

Why it's worth running: it forces three checks in one shot — does Claude
resolve `/users/me` before listing, does it project `.data` from every
response instead of assuming a bare array, and does it reach for the
bundled script's pagination instead of a single unpaginated request that
quietly misses tasks past the first page.

---

## Deliberately not claimed

Not a verdict on whether the Asana API skill is well designed — that's
Teardown territory; this reel states the mechanism and stops. Not a claim
that gid and the data envelope are the only rules that matter —
`opt_fields`, rate limits, and the search cap are real, but the carry-out
compresses the two habits that govern every single call, not the full
reference. Not a claim that every Asana request needs the bundled script —
only that a hand-rolled request still owes the same two habits.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeAPI #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
