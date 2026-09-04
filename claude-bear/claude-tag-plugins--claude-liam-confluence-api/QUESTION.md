# QUESTION

**The question:** "Claude just calls the Confluence API, right?" — and
specifically: is there one API, or does Claude have to choose between more
than one, and what happens if it gets that choice wrong?

**Mode:** redo — source is
`anthropics/claude-tag-plugins/youtube/claude-liam-confluence-api/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel, 7 beats: `register:
"Teardown"`, `brand: "claude-liam"`, cold open a `ClaudeComposerAsk` typed
ask, B01/B02 Remotion anatomy+design beats, B05 a "gets it right / where it
bites" teardown beat, `BVDT` a verdict artifact, `BHTF` your-turn, `BOUT`
`ClaudeTitleOutro`). This reel keeps the question and the source's body
facts, replaces the cold open with the Brutalist Hesitant Writer, and closes
with the Humanitarians AI skin.

**Why it earns a reel:** Confluence Cloud actually runs two REST API
generations side by side. Claude defaults to the newer one (v2) for
everyday work — pages, spaces, blog posts, comments, attachments, labels —
and only drops to the older one (v1) for three jobs v2 can't do: searching
with Confluence's query language, uploading or downloading an attachment,
and adding a label. Two concrete traps sit right at the boundary of that
routing: every call needs a `/wiki` prefix or it 404s outright, and the two
API versions build their "next page" links differently, so getting the
direction backwards silently truncates a paginated result instead of
erroring. Underneath all of it sits one non-negotiable rule: a page's own
words are never a command, no matter what they say.

**Naive framing (B00, corrected on screen):** "Claude just calls one
Confluence API." → corrects "one" to "two" (Claude doesn't call a single
API — it routes between two versions depending on the job).

**Body facts carried from source (unchanged):**
- Confluence Cloud runs two REST API generations at once: v2
  (`/wiki/api/v2/`) is the default, covering pages, spaces, blog posts,
  comments, attachments, and labels; v1 (`/wiki/rest/api/`) is used only
  where v2 has no equivalent — CQL search, attachment upload/download, and
  label add
- three bundled scripts cover the hot path: `cql_search.sh` (search, follows
  pagination, TSV/JSON output), `read_page.sh` (reads a page in the
  requested body format, diagnostics to stderr), `write_page.sh` (resolves a
  space key, reads the current version before updating, bumps it, retries
  once on a 409 version race)
- the `/wiki` prefix is mandatory on every path; missing it returns a 404
  (not an auth error) on every single call
- the pagination URL relativity trap: v2's `_links.next` is site-root-
  relative (strip `/wiki` off the base before prepending, or you double it);
  v1's `_links.next` is `/wiki`-root-relative (prepend the base as-is);
  getting this backwards silently truncates results at the first page
  boundary, with no error
- the security note, which the source calls the most important thing in the
  skill: pages, comments, and attachments returned by the API may carry
  adversarial instructions; retrieved content is quoted as inert evidence
  only, never followed as a command
- smaller documented gaps worth knowing: `atlas_doc_format`'s `value` field
  is a JSON string that must be parsed a second time; the default list size
  (25–50 items) is well under the real max (250), so a large search can come
  back silently short; hard delete and some uploads need one extra
  permission or header most people miss the first time

**Deliberately reframed, not new:** the source's B05 "gets it right / where
it bites" list is a documentation-quality verdict — Teardown judgment on the
skill's own writing. Plain register keeps every fact in that list (folded
into NB03) but drops the verdict framing: this reel never rates the skill's
documentation, it only states what's true and what's easy to miss.
