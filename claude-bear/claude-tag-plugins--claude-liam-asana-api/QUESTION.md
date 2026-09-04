# QUESTION

**The question:** "Claude, Asana API." — when Claude manages your Asana
tasks, is it clicking around inside the Asana app, or calling Asana's own
API? Answered using the Asana API skill's own worked facts as the concrete
case.

**Mode:** redo — source is
`anthropics/claude-tag-plugins/asana/skills/asana-api/../../youtube/claude-liam-asana-api/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register "skill-teardown" sheet:
metadata `register: "Teardown"`, `brand: "claude-liam"`, 7 beats — B00 cold
open, B01 anatomy, B02 ten operations, B05 teardown tell, BVDT verdict,
BHTF handoff, BOUT outro — all already REMOTION, no puppet/AI-video/pantry
beat to replace beyond the WRITER LAW swap). This reel keeps the question
and the source's body facts, re-registers the narration to Plain, replaces
the cold open with the Brutalist Hesitant Writer, folds the source's BVDT
verdict recap into a proper carry-out beat, and closes with the
Humanitarians AI skin.

**Why it earns a reel:** the Asana API skill covers Asana's REST API
(`app.asana.com/api/1.0`) plus a bundled `asana_tasks.sh` script for the
most common workflow. Every resource — workspace, project, section, task,
story — is identified by a string `gid`, never a name. Every response,
read or write, wraps its payload under a top-level `data` key. Compact
records return only `gid`/`name`/`resource_type`; anything else has to be
requested explicitly with `opt_fields`. Ten core operations cover list,
get, create, update/complete, comment, search, projects/sections, move,
gid-lookup, and subtasks/tags/attachments — the bundled script handles the
pagination that a hand-rolled loop tends to miss. One documented gotcha
worth carrying: workspace search is premium-only, capped at 100 unstable
results, with no real pagination — easy to miss in the middle of an
otherwise generous API.

**Naive framing (B00, corrected on screen):** "Claude must open the Asana
app and click around to manage my tasks. Is that it?" → corrects "app" to
"API" (Claude isn't operating the visual app — it's calling Asana's REST
API directly and reading the JSON that comes back).

**Body facts carried from source (unchanged):**
- resource hierarchy: workspace → project → section → task → story, gid
  all the way down
- three universal rules: gid not name (resolve names to gids first); the
  data envelope (reads return `{"data": …}`, writes send `{"data": {…}}`,
  errors replace `data` with `errors`); `opt_fields` (compact records carry
  only gid/name/resource_type — request more explicitly, dot notation for
  relations like `assignee.name`)
- ten operations, one bundled script (`asana_tasks.sh`) that handles
  pagination and TSV/JSONL output for the single most common request:
  listing tasks
- documented gap: workspace search is premium-only, capped at 100 unstable
  results, no real pagination — a rule that looks like the other nine, but
  isn't
- Your Turn: paste a real multi-workspace task-listing request and watch
  whether Claude resolves `/users/me` first, projects `.data` from every
  response, and reaches for the bundled script instead of a bare `curl`
  loop
