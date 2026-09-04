# QUESTION

**The question:** "Claude, Jira API." — when Claude moves a ticket to Done,
is it setting a status field directly, or something else? Answered using
the jira-api skill's own worked facts as the concrete case.

**Mode:** redo — source is
`anthropics/claude-tag-plugins/youtube/claude-liam-jira-api/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet:
metadata `register: "Teardown"`, `brand: "claude-liam"`, 7 beats — B00 cold
open, B01 anatomy, B02 design/patterns, B05 teardown tell, BVDT verdict,
BHTF handoff, BOUT outro — all already REMOTION, no puppet/AI-video/pantry
beat to replace beyond the WRITER LAW swap). This reel keeps the question
and the source's body facts, re-registers the narration to Plain, replaces
the cold open with the Brutalist Hesitant Writer, folds the source's BVDT
verdict recap into a proper carry-out beat, and closes with the
Humanitarians AI skin.

**Why it earns a reel:** the jira-api skill covers Jira Cloud's two REST
families — Platform REST v3 (issues, projects, JQL search, comments,
transitions — the default) and Agile REST v1 (boards, sprints, backlog,
epics — only for concepts the core issue model lacks). Two structural
facts shape every write: description and comment bodies are Atlassian
Document Format, a JSON tree (`type: doc`, `version: 1`, a `content`
array) — a plain string returns a 400 whose message never mentions ADF —
and status can't be set directly; it moves through a transition, listed
first and posted by ID, and that ID is per-workflow, so a hardcoded ID
from one issue often fails on another. Pagination comes in three flavors:
JQL search's `nextPageToken` (no total — stop when it's absent), most
lists' `startAt`/`total`/`isLast`, and comments' offset pagination nested
under a named key. Documented gaps worth carrying: the no-total workaround
(`/search/approximate-count`) is mentioned once with no example; three
pagination schemes have no single detection rule; `maxResults` is silently
clamped per endpoint; the watcher endpoint takes a bare JSON string, not an
object; and 404 — not 403 — is what an issue you can't browse returns,
so a "not found" loop can silently skip unauthorized issues.

**Naive framing (B00, corrected on screen):** "Claude must just set the
ticket's status to Done to close it out." → corrects "set" to
"transition" (there is no direct status write — only a workflow
transition, looked up first and posted by ID).

**Body facts carried from source (unchanged):**
- two API families: Platform REST v3 default (issues/projects/JQL/
  comments/transitions); Agile REST v1 only for boards/sprints/epics
- transitions: list first, POST by ID; IDs are per-workflow and
  per-current-status, not portable across issues
- ADF: description and comment bodies are a JSON tree (`type: doc`,
  `version: 1`, `content` array); a plain string draws a 400 that never
  names ADF as the fix
- JQL search must be bounded (at least one filter clause) and returns no
  total — paginate on `nextPageToken`'s presence, not a count
- accountId, not email, for assignee/watcher/reporter (Jira stopped
  accepting email lookups after the GDPR change)
- documented gaps: no-total workaround under-documented; three pagination
  schemes, no detection rule; `maxResults` silently clamped; 404 (not 403)
  masks access control on issues you can't browse
- Your Turn: paste a real bounded-search-plus-transition-plus-comment
  request and watch whether Claude looks up the transition ID instead of
  writing status directly, sends the comment as ADF, and paginates by
  token instead of expecting a total
