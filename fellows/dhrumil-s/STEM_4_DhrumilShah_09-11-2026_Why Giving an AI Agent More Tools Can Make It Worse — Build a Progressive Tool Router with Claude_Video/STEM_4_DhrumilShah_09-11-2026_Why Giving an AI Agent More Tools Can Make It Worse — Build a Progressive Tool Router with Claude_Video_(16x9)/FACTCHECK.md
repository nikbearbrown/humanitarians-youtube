# FACTCHECK — Progressive Tool Router

Research date: **2026-09-28** · Researcher: Claude (automated) · **Human sign-off: pending**

Re-verify every row on the publish date. Anthropic's tool APIs and the MCP specification both move
quickly, and two rows below are explicitly roadmap (not shipped spec) or version-sensitive.

Verdicts: SUPPORTED · QUALIFY · VERIFY (human confirmation required) · DO-NOT-CLAIM

---

## General ML / systems claims

| ID | Narration / on-screen | Claim | Source | Evidence | Verdict |
|---|---|---|---|---|---|
| F1 | "a name, a description, an input schema, parameters, permissions" (S3) | A tool definition carries this metadata | MCP specification — *Tools*, Data Types | Fields are `name`, `title` (optional), `description`, `icons` (optional), `inputSchema`, `outputSchema` (optional), `annotations` (optional) | SUPPORTED — say "annotations/permissions" on screen; do not invent a `permissions` field |
| F2 | "Every tool costs context before the work even starts" (S3, S4) | Tool definitions consume context ahead of the task | Anthropic — *Tool search tool* | "Loading every tool definition up front causes two problems as a tool library grows: **Context bloat** …" | SUPPORTED |
| F3 | "more chances to pick the wrong tool" (S4) | Selection quality can degrade as the catalog grows | Anthropic — *Tool search tool* | Documents that selection accuracy "degrades once you exceed 30–50 available tools" | SUPPORTED — narration stays qualitative on purpose; if you cite the 30–50 range on screen, attribute it to Anthropic's docs |
| F7 | `tools/list → paginated catalog` (S11 visual) | MCP tool listing is paginated and cacheable | MCP specification — *Tools*, *Pagination* | `tools/list` takes an opaque `cursor`, returns `nextCursor`; responses carry `ttlMs`/`cacheScope`; servers SHOULD return a deterministic order to help prompt caching | SUPPORTED |
| F9 | "1,000 tools" / "3 tools" (S2, S5, S9) | Literal counts | `src/progressive_tool_router.py` | Registry is built at exactly 1,000 tools; `TOP_K = 3` | SUPPORTED — true by construction; keep the registry size at 1,000 if the number stays on screen |
| F11 | — | "More tools make the model less intelligent" | — | No source supports this framing | **DO-NOT-CLAIM** — use context, routing and selection overhead instead |

## Claude / Anthropic product claims

| ID | Narration / on-screen | Claim | Source | Evidence | Verdict |
|---|---|---|---|---|---|
| F4 | "Anthropic's tool search tool already defers loading until Claude needs a tool" (S11); `defer_loading: true` on screen | The capability exists and works by deferring definitions | Anthropic — *Tool search tool* | Two variants (`tool_search_tool_regex_20251119`, `tool_search_tool_bm25_20251119`); tools marked `defer_loading: true` load only when discovered; at least one tool must stay non-deferred; discovered tools arrive as `tool_reference` blocks the API expands | **VERIFY** — supported as of the research date; re-check variant names, versions and model support before publishing |
| F5 | §D "custom client-side search" | You can supply your own retrieval and still use the same mechanism | Anthropic — *Tool search tool*, Custom tool search implementation | A custom tool may return `tool_reference` blocks in a standard `tool_result`; every referenced tool must have a definition in `tools`, normally with `defer_loading: true` | **VERIFY** |
| F10 | any model name | Model version named on screen | Anthropic model list | Model lineups change | **QUALIFY** — avoid naming a model version on screen; it dates the video. Keep versions in the repo, not the film |
| — | Vendor figures (≈55k tokens for a five-server setup; "over 85 percent" reduction; 3–5 tools loaded) | Published example figures | Anthropic — *Tool search tool* | These are Anthropic's documented figures, not measurements of this project | **QUALIFY** — if used, attribute on screen ("Anthropic docs"), and never present them as this project's benchmark |

## MCP roadmap claims

| ID | Narration / on-screen | Claim | Source | Evidence | Verdict |
|---|---|---|---|---|---|
| F6 | "the MCP roadmap calls progressive discovery a priority" (S11); DISCOVER→FILTER→RANK→LOAD→EXECUTE (S12) | Progressive discovery is a stated roadmap priority | MCP roadmap, published 2026-08-22 (`modelcontextprotocol/modelcontextprotocol`, `blog/content/posts/2026-08-22-mcp-roadmap.md`) | "Connecting to a server with a hundred tools means the model pays for that entire surface before the user has asked a single question"; the aim is that "a server can offer a small entry point and reveal more of its catalog as the conversation narrows", under the *Improved primitives* priority | **VERIFY** — roadmap ≠ shipped specification. Keep the on-screen plate `CURRENT-DEVELOPMENT INFO — VERIFY AGAINST OFFICIAL DOCS`, and check whether a later spec release has shipped it |

## Measurements

| ID | Claim | Status |
|---|---|---|
| F8 | Any token, latency, cost or accuracy number attributed to this project | **NOT YET MEASURED.** Run `src/benchmark_router.py`, then label each number with model, date, task count and repeats. Until then S9 stays qualitative (HIGH/LOW) with the `ILLUSTRATIVE EXAMPLE` plate |

## Sources

- Model Context Protocol — *Tools* specification (tool definition fields, `tools/list`, pagination, `listChanged`, deterministic ordering)
- Model Context Protocol — roadmap, 2026-08-22 (progressive discovery)
- Anthropic — *Tool search tool* documentation (`defer_loading`, regex/BM25 variants, `tool_reference`, custom client-side search, limits, when to use)
- Anthropic — *Effective context engineering for AI agents* and *Advanced tool use* (background for the just-in-time retrieval framing)

## Claims deliberately not made

- No statement that any model "gets worse" or "less intelligent" with more tools.
- No token, latency, cost or accuracy figure presented as measured before the benchmark is run.
- No claim that MCP has shipped progressive discovery in a released specification.
- No named model version on screen.
