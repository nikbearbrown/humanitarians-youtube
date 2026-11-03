# QUESTION

**The question:** "Claude just queries the Notion database, right?" — and
specifically: is the database's own ID enough, or does Claude need something
else, and what happens if it gets that choice wrong?

**Mode:** redo — source is
`anthropics/claude-tag-plugins/youtube/claude-liam-notion-api/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel, 7 beats: `register`
implied Teardown via `modifier: "skill-teardown"`, `brand: "claude-liam"`,
cold open a `ClaudeComposerAsk` typed ask, B01/B02 Remotion anatomy+design
beats, B05 a "gets it right / where it bites" teardown beat, `BVDT` a verdict
artifact, `BHTF` your-turn, `BOUT` `ClaudeTitleOutro`). This reel keeps the
question and the source's body facts, replaces the cold open with the
Brutalist Hesitant Writer, and closes with the Humanitarians AI skin.

**Why it earns a reel:** Notion's content model has a twist that trips up
anyone who assumes "the database" is one flat thing with one ID. A database
is a container; the data it actually holds — the schema, and every row —
lives in a separate object called a data source, with its own ID. Schema
reads, queries, and creating a new row all need that data source ID, not the
database's. Two smaller traps sit right alongside it: every request needs a
specific version header or it fails outright, and a 404 almost never means a
bad ID — it almost always means the page or database was never shared with
Claude's connection.

**Naive framing (B00, corrected on screen):** "Claude just needs the
database ID to run a query." → corrects "database" to "data source" (Claude
doesn't query the database directly — it queries the data source
underneath it).

**Body facts carried from source (unchanged):**
- content model: a page is a block, sharing one ID space; a database's real
  table is a separate data source object owning the schema and the rows; a
  row is a page whose parent is that data source
- schema reads, queries, and row creation all take the data source ID —
  retrieved from the database object's `data_sources` list — not the
  database ID; sending the database ID to those calls returns "object not
  found"
- two bundled scripts cover the everyday work: `notion_search.sh` (search,
  follows pagination, type-aware title extraction, newest-edited first) and
  `notion_read_page.sh` (reads a full page body depth-first, decodes blocks
  to plain text, but does not recurse into `child_page`/`child_database`
  blocks — those need a separate invocation)
- `Notion-Version` is required on every request; missing it returns a
  `400 missing_version` before anything else is checked
- a 404 `object_not_found` almost always means the page or database has not
  been shared with the integration via Connections — check sharing before
  suspecting the ID
- smaller documented gaps worth knowing: file URLs inside block payloads
  expire after about an hour, so they should never be cached and reused;
  a pagination loop must guard against an error envelope, or a naive cursor
  loop can run forever; filter conditions are keyed by property type (a
  `select` field takes `equals`, `multi_select` takes `contains`, `date`
  takes `on_or_before`/`after`) — reading the schema before writing a filter
  is mandatory, not optional

**Deliberately reframed, not new:** the source's B05 "gets it right / where
it bites" list is a documentation-quality verdict — Teardown judgment on the
skill's own writing. Plain register keeps every fact in that list (folded
into NB03) but drops the verdict framing: this reel never rates the skill's
documentation, it only states what's true and what's easy to miss.
