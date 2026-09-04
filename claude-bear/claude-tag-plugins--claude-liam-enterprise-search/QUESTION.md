# QUESTION

**The question:** "enterprise-search" — when Claude searches a company's own
knowledge (chat, drives, tickets, wikis) instead of the open web, is one
search enough to get an answer? Answered using the `enterprise-search`
Claude skill (Glean Client REST API) as the concrete case.

**Mode:** redo — source is
`anthropics/claude-tag-plugins/youtube/claude-liam-enterprise-search/beat_sheet.json`
(a fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at the
`enterprise-search` Anthropic skill. 7 beats — B00 cold open, B01 anatomy,
B02 design, B05 teardown scorecard, BVDT verdict, BHTF handoff, BOUT outro —
all already REMOTION patterns, no puppet/AI-video/pantry beat to replace
beyond the WRITER LAW swap at B00).

**Why B05/BVDT could not be reused as-is:** unlike the source's B00/B01/B02
narration (which is pure mechanism/fact — the three-step loop, the
index-first rule — and ports to Plain unchanged), the source's B05 beat
(`EnterpriseSearchTell`) bakes Teardown judgment directly into the pixels:
on-screen headers read "ENTERPRISE SEARCH · TEARDOWN" and "What it gets
right / where it bites", with columns literally labelled "GETS RIGHT" and
"WHERE IT BITES" — a scorecard verdict, not a fact. Reusing that component
in a Plain redo would put visible Teardown judgment on screen even with
re-registered narration. Per CARRY-OUT LAW precedent (the `action-creator`
and `build-mcpb` redos in this family), the verdict/scorecard beat is
dropped and its load-bearing facts are redistributed into an anchor
payoff and a dedicated both-directions beat, stated as mechanism, not score.

**Why B01 (anatomy) and B02 (design) reuse their source REMOTION components
unchanged:** their on-screen headers ("THREE-STEP LOOP + SCRIPTS", "DESIGN
RULES") and their narration are already mechanism-only, no verdict language.
Confirmed by reading the components directly: `EnterpriseSearchAnatomy` and
`EnterpriseSearchDesign` schemas take only a `sparkLine` prop (body content
is fixed), so the fix was in the surrounding beats and the narration
compression, not the components.

**Body facts carried from source (unchanged):**
- backend: Glean Client REST API, works against any Glean-compatible index
- 3-step loop: `/search` (ranked snippets, ~35-word preview, per-result
  `trackingToken` + document ID) → `/getdocuments` (full text, up to 50 IDs
  per call) → feedback (`UPVOTE`/`DOWNVOTE`, raw curl, no bundled script)
- 2 bundled scripts: `es_search.sh` (cursor pagination, `--datasource`
  filter, `--json` for tracking tokens), `es_read.sh` (batch doc fetch)
- index-first rule: search the shared index (cross-source ranking, dedup,
  access control already applied) before falling back to one connector
- cursor pagination: pass the cursor back verbatim, never construct one,
  stop when `hasMoreResults` is false or the cursor is absent
- empty-results ambiguity: could mean not-indexed (broaden the query) or a
  permissions gap (the identity can't see it) — the API doesn't distinguish
- feedback trains the ranker; `DOWNVOTE` (what you rejected) matters as much
  as `UPVOTE`, and is the first thing skipped when a task is finishing

**Naive framing (B00, corrected on screen):** "Does Claude just search our
docs and answer from the results?" → corrects "results" to "documents" (the
misconception that a search *result* — a short snippet — already contains
the answer, corrected to: the answer comes from reading the *document*
itself).

**Anchor (planted B01, paid off B05):** "What's our policy on contractor
onboarding, and is there a prior decision on file?" — the concrete question
the loop is built to answer.

**Your Turn:** paste a real search-then-read-then-report prompt using the
same onboarding-policy question, watching whether the assistant reads the
full document (not just the snippet) and reports what it used.
