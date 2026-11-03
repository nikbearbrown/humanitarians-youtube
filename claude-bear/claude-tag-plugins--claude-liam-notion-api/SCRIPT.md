# The Data Source, Not the Database — Narration Script (GATE P)

*Skill: `hai-simple` (redo of `claude-tag-plugins/claude-liam-notion-api`).*
*Register: **Plain**. 7 beats. Source was a 7-beat Teardown-register reel
covering B00 cold open, B01 anatomy (content model + two bundled scripts),
B02 design (sanity check, data-source extraction, schema-before-filter,
sharing-before-404), B05 teardown (gets right / bites), BVDT verdict, BHTF
your-turn, BOUT outro. Carry-out written first (CARRY-OUT.md, GATE C).*

**Cold open:** Brutalist Hesitant Writer (Remotion, no puppet, no
generation). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone assumes Claude just needs a database's ID to run a query. It doesn't — Notion splits every database into a separate data source, and queries need that ID instead. So what's the difference?" | Writer types "Claude just needs the database ID to run a query. How does that work?"; "database" hesitates and corrects to "data source" |
| NB01 | 3 mechanism | Notion doesn't let Claude query a database directly. Every database has its own data source underneath it, and that data source is where the real table lives — its schema, and every row in it. A row is just a page whose parent happens to be that data source. So schema reads, queries, and creating a new row all need the data source ID, not the database ID; get that wrong, and you'll be told the object doesn't exist. Two bundled scripts handle the common work: notion_search.sh searches your workspace and pages through every result; notion_read_page.sh reads a full page, block by block, in the order you'd read it. | "page = block" + "DB → source" + "2 scripts" chips |
| NB02 | 3 mechanism | Two details trip people up. First: every request needs a specific version header. Leave it off, and every single call fails immediately with a missing-version error, before Notion even looks at what you asked for. Second: when a search or a read comes back empty, or says the object wasn't found, that's almost never a bad ID. It almost always means the page or database hasn't been shared with Claude's connection yet. Check sharing before you start second-guessing the ID. | "version header" + "404 = sharing" + "not bad ID" chips |
| NB03 | 3 mechanism | A few things are easy to miss. The page-reading script lists a nested sub-page or sub-database when it finds one, but it doesn't open it — that needs its own separate read. Any file link inside a block, like an image, stops working after about an hour, so it's never something to save and reuse. When a result list has more pages, the code fetching them has to watch for an error coming back mid-stream, or the loop can run forever instead of stopping. And filtering a database isn't one-size-fits-all — the right condition depends on the property's type: select takes 'equals,' multi-select takes 'contains,' date takes 'before' or 'after.' Reading the schema first isn't optional; it's the only way to know which one applies. | "no recursion" / "links expire" / "guard loop" / "filter by type" chips |
| **BCRY** | **6 carry-out** | Claude doesn't query a Notion database directly — it queries the data source underneath it, and needs that ID, not the database's. And when something can't be found, that almost always means it hasn't been shared with Claude yet, not that the ID is wrong. | the sentence, alone, serif, large |
| BHTF | your turn | Your turn. Here's the prompt — read it with me. Search my Notion workspace for pages about onboarding, then read the most recently updated match and summarize it for me in your own words. If reaching that page means querying a database along the way, tell me out loud whether you're using the database's own ID or the data source ID underneath it. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | The Data Source, Not the Database. Liam, in for Bear. | OutroSeries — @HumanitariansAI |

## Redo audit — what changed from the source, what didn't

| | Source (`claude-tag-plugins`, Teardown-shaped) | This reel (`hai-simple`, Plain) |
|---|---|---|
| Question | "You are working with the notion-api skill... the key distinction: database IDs and data source IDs are not the same thing" (B00 cold-open framing) | reframed as a direct question: "Claude just needs the database ID, right?" — same subject, sharper hook |
| Facts | content model (page=block, DB→data source→schema, row=page with data_source parent); data source ID vs database ID; two bundled scripts; Notion-Version required; 404=sharing; file URL expiry; pagination error-envelope guard; filter conditions keyed by property type | unchanged, all carried — see QUESTION.md's full fact list |
| Beat count | 7 beats: B00 composer-ask + B01/B02 anatomy/design + B05 teardown analysis + BVDT verdict + BHTF your-turn + BOUT outro | kept the same 7-beat shape: B00 carries the wrong-guess pedagogy per WRITER LAW instead of a dedicated beat; B01→NB01, B02→NB02 kept as one beat each (B02's sanity-check-endpoint framing folded into NB02's version-header point, the schema-before-filter point moved to NB03 alongside the source's other documented gaps to avoid repeating "data source ID" content across three beats); B05's "gets right / bites" list reframed (not compressed away) into NB03's neutral "worth knowing" facts, dropping only the verdict framing itself; BVDT folded into BCRY; BHTF kept, with the source's five-point Claude-Code-session watch-list replaced by one paste-ready prompt any viewer can run without special workspace setup; BOUT kept |
| B00 | `ClaudeComposerAsk` cold open stating the routing model directly, no wrong-guess framing | `BrutalistHesitantWriter` (WRITER LAW) — "database" → "data source", the actual wrong guess the body corrects |
| Register | Teardown-shaped (`modifier: "skill-teardown"`, B05 rates what the skill "gets right" vs "where it bites") | Plain — explicit no-judgment audit below |
| Voice | am_onyx (unchanged) | am_onyx (unchanged) |
| Close | `ClaudeTitleOutro`, `@NikBearBrown` | `OutroSeries`, `@HumanitariansAI`, Liam sign-off |
| Handoff prompt | source's Claude-Code-session task ("find all In Progress items... watch five things") | reworked into one runnable, paste-ready prompt that exercises the same two behaviors (search, read) plus a direct check of the reel's central distinction (database ID vs data source ID), without requiring a specific database/workspace setup |

No source beat was `ai-video-prompt`, pantry, or a human-drop slot — the
source's final build was already entirely REMOTION (`ClaudeComposerAsk` for
B00/BHTF, `NotionApiAnatomy`/`NotionApiDesign`/`NotionApiTell` for the body,
`ClaudeVerdictArtifact` for BVDT, `ClaudeTitleOutro` for BOUT), so
NO-GENAI/NO-PANTRY LAW required no substitution beyond B00's mandated
cold-open swap. None of the source's custom body components
(`NotionApiAnatomy`/`NotionApiDesign`/`NotionApiTell`) were reused for
NB01–NB03 even though they are REMOTION: their on-screen headers are
hardcoded to the source's own section names and — in `NotionApiTell`'s
case — a "✓/✗ gets right / bites" rubric baked into the component itself,
the same defect class the `confluence-api` sibling documented. NB01–NB03
instead reuse the generic "chip row" Manim template (copied verbatim,
mechanism and GATE T exemption notes included, from the
`claude-tag-plugins--claude-liam-confluence-api` sibling), parametrized
entirely from neutral title/chip/caption strings.

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00 states the question; mechanism waits until NB01 |
| Wrong guess surfaced, falsified by a case | B00 states the guess (database ID is enough); NB01 states the actual data-source-ID requirement as the immediate correction |
| One anchor | N/A this reel — the wrong guess resolves immediately at NB01 rather than through a planted/paid-off scene; see `anchor_pair: "N/A"` in beat_sheet.json metadata |
| Both directions | NB02's two traps cover both practical failure directions of the same underlying cause (missing header → immediate hard failure; missing share → a 404 that looks like a bad ID) — both resolve to "check the setup before you doubt the identifier" |
| No design judgment | NB01–NB03 describe what the skill does and what to watch for; nothing rates whether the skill's documentation is well written |
| Carry-out survives retelling | BCRY — see CARRY-OUT.md secondhand test |

## Deliberately not claimed

- **Not that the database ID is useless.** It's exactly what you retrieve
  first, in order to read its `data_sources` list and find the ID that
  actually matters for schema, queries, and row creation.
- **Not a full four-format breakdown of block payloads.** The source
  documents a rich_text/type-keyed payload structure; this reel keeps only
  the practical traps a general viewer would actually hit (missing
  recursion, expiring file URLs), not the full payload shape.
- **Not a documentation-quality verdict.** NB03 states the same facts as
  the source's B05 "gets right/bites" teardown, but never frames them as a
  rating of the skill's own writing — see QUESTION.md's "Deliberately
  reframed, not new."

## Handoff prompt (BHTF, read aloud)

> "Search my Notion workspace for pages about onboarding, then read the
> most recently updated match and summarize it for me in your own words.
> If reaching that page means querying a database along the way, tell me
> out loud whether you're using the database's own ID or the data source
> ID underneath it."

Why it's worth running: it exercises the search-then-read path from NB01
and puts the NB01/NB02 distinction to a direct test — whether Claude
actually names which ID it used, out loud, before answering.

---
**GATE P — signed:** ______________________  (human)
