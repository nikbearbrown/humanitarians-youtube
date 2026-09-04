# Claude, Jira API.

Claude doesn't set a Jira ticket's status directly — there is no status field
to write. It lists the issue's available transitions, matches the one it
wants by name, and posts that transition's ID, and that ID isn't universal:
the same-looking transition on a different ticket, in a different workflow,
often carries a different ID entirely. Two API families split the work —
Platform REST v3 for issues, projects, and search (the default), Agile REST
v1 only for boards and sprints. Search a bounded JQL filter for every open
bug assigned to you and the results page by a next-page token, not a total
count — the loop stops when the token disappears, no total needed. Comment
on the top result, and that comment can't be a plain string: it has to be a
JSON tree, a typed doc with a content array, or Jira sends back a 400 that
never mentions ADF. Skip either habit and the request fails quietly — a
loop expecting a total spins forever, or the comment 400s with no clue why.
One more habit worth carrying: assignees and watchers take an account ID,
never an email — Jira stopped accepting email lookups years ago.

**Topic:** JIRA API · CLAUDE TAG PLUGIN
**Playlist:** Claude Basics
**Code (no media):** https://github.com/nikbearbrown/humanitarians-youtube/tree/main/claude-bear/claude-tag-plugins--claude-liam-jira-api

---

## Chapters

0:00 Claude must just set the ticket's status to Done. Is that it?
0:11 Not a status field
0:29 Two families, then one request traced through
1:02 Complete — or quietly wrong
1:32 Carry-out
1:45 Your turn
2:09 Outro

---

## YOUR TURN

"Find all open bugs in PROJ assigned to me, then move the highest-priority
one to In Progress and add a comment explaining why."

Why it's worth running: it forces three checks in one shot — does Claude
look up the transition ID instead of trying to set status directly, does it
send the comment as a JSON tree instead of a plain string, and does it keep
paging by token instead of expecting a total that JQL search never sends.

---

## Deliberately not claimed

Not a verdict on whether the jira-api skill is well designed — that's
Teardown territory; this reel states the mechanism and stops. Not a claim
that transitions and ADF are the only rules that matter — `createmeta`, the
sanity-check call, the 404-vs-403 access-control quirk, and `maxResults`
clamping are real parts of the skill; the reel picks the two habits that
govern every write as the carry-out, not a full reference. Not a claim that
all three pagination schemes are equally risky — JQL search's missing total
is the one flagged, because it's the one most likely to make a hand-rolled
loop spin forever.

---

**@HumanitariansAI**

Narrated by Liam, in for Bear. Voice: Kokoro `am_onyx` — free, local, no account.

*AI-generated narration. Visual scenes built with Manim (Graphic) and Remotion
(motion graphics). No human-performed audio or video in this production.*

#AI #ClaudeAI #ClaudeAPI #AIagents #AgenticAI #HumanitariansAI #ProfessorBear #ClaudeBasics

---
