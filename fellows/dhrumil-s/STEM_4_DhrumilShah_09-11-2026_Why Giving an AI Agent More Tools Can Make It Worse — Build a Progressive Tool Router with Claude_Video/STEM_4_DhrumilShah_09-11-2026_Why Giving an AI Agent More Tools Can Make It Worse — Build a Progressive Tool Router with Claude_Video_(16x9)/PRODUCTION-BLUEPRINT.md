# PRODUCTION BLUEPRINT
## "Why Giving an AI Agent More Tools Can Make It Worse — Build a Progressive Tool Router with Claude"

*Alternative title: "1,000 AI Tools vs. 3 — Why More Context Can Make an Agent Worse"*

| Spec | Value |
|---|---|
| Aspect ratio | 9:16 vertical (native, not cropped) |
| Master resolution | 2160 × 3840 (4K UHD vertical) |
| Frame rate | 30 fps · constant |
| Container / codec | MP4 · H.264 (CRF 16–18) master; H.265 optional archive |
| Audio | 48 kHz stereo AAC, −14 LUFS integrated, −1.5 dBTP |
| Target runtime | 118 s (range 90–120 s) |
| Design canvas | 1080 × 1920, rendered at `--scale=2` for the 4K master |
| Presenter | Dhrumil Shah |
| Series | AI · STEM · Computer Science explainers |
| Folder | `progressive-tool-router` |

**Timing rule for this series: audio is the clock.** The times below are design targets. Generate
narration first, measure each line, then re-time scene boundaries from the measured durations.
Never stretch or speed up speech to hit a target — rewrite the line instead.

---

## Scene table

| Scene | Time | Narration | On-Screen Text | Visuals / Animation | Technical Notes |
|---|---|---|---|---|---|
| **S1 — Presenter open** | 0:00–0:07 | "Hi, I am Dhrumil Shah, and this video is about why giving an AI agent more tools can actually make it worse — and how we can build a smarter progressive tool router with Claude." | `DHRUMIL SHAH` / `PROGRESSIVE TOOL ROUTER` / kicker `AI · AGENTS · CONTEXT ENGINEERING` | Dark grid fades up. Name types in behind a terminal caret; thin terracotta underline sweeps left→right. Five ghosted pipeline chips (DISCOVER · FILTER · RANK · LOAD · EXECUTE) preview at 20% opacity. | No hook before this line — hard requirement. Type stays inside x 96–984, y 380–1340. Caret blink 1.2 s. |
| **S2 — The question** | 0:07–0:14 | "If an AI agent has access to a thousand tools, does it really need all thousand in its context just to analyze one CSV file?" | `1,000 tools` → `1 CSV file` / `?` | Left: dense 1,000-dot tool cloud (25 × 40) pulsing. Right: single CSV glyph. Large terracotta `?` snaps in on "really". | Dot grid is generated, not an image. Exactly 1,000 dots so the on-screen number is literally true. |
| **S3 — What one tool costs** | 0:14–0:23 | "Every tool costs context before the work even starts — a name, a description, an input schema, parameters, permissions." | `ONE TOOL DEFINITION` · `name` · `description` · `inputSchema` · `parameters` · `annotations / permissions` | One tool card expands into five metadata rows; each row highlights on its spoken word. Context bar on the right starts filling in the "definitions" colour before any task text exists. | Field names must match the MCP tool definition (`name`, `title`, `description`, `inputSchema`, `outputSchema`, `annotations`). No invented fields. |
| **S4 — The cascade** | 0:23–0:32 | "Multiply that by a thousand and the context fills with menu instead of meal — bigger search space, more latency, more cost, more chances to pick the wrong tool." | `1,000 TOOLS ↓ HUGE CATALOG ↓ MORE CONTEXT TOKENS ↓ LARGER SEARCH SPACE ↓ HIGHER LATENCY ↓ HIGHER COST ↓ POSSIBLE WRONG TOOL` | Chain builds top-to-bottom, one link per beat, short down-arrows. Final link flashes amber with a ⚠ glyph. | **Claim discipline:** "can" and "more chances", never "the model gets dumber". Amber always paired with the ⚠ glyph (colour-blind safe). |
| **S5 — Concrete request** | 0:32–0:43 | "Take a real request: analyze this CSV and create a chart. The agent loads a thousand definitions, searches them all, and ends up using three." | `USER: "Analyze this CSV and create a chart."` → `LOADS 1,000` → `SEARCHES 1,000` → `USES 3` / `CSV Reader · Data Analyzer · Chart Generator` | Dot cloud flows into the agent node; a magnifier sweeps it; exactly three dots light teal and rise as named chips. The other 997 stay grey. | The three chips keep identity, colour and order in S8 and S9 — the film's visual through-line. |
| **S6 — Progressive discovery** | 0:43–0:52 | "Progressive discovery flips it. Read the intent first, search a tool registry, and load only what the task needs." | `INTENT ROUTER ↓ TOOL SEARCH / RETRIEVAL ↓ TOP RELEVANT TOOLS ↓ AI AGENT` | Four-stage vertical flow lights in order. The 997 irrelevant dots dissolve downward out of frame; only the three chips continue into the agent. | Reuse the S5 chip components so the "3" visibly survives the transition. |
| **S7 — Router architecture** | 0:52–1:02 | "Claude can help you build each piece: intent classification, a tool registry, semantic search, ranking, top-K selection, then execution." | `USER QUERY ↓ INTENT CLASSIFICATION ↓ TOOL REGISTRY ↓ SEMANTIC SEARCH ↓ RANKING ↓ TOP-K SELECTION ↓ AGENT CONTEXT ↓ TOOL EXECUTION` | Eight-stage stack builds in sync with narration; a data pulse travels the finished chain. Each stage carries a one-word gloss (what · catalog · compare · score · choose · load · call). | Eight rows is the legibility ceiling at 1080 wide: 44 px mono, 96 px rows, 16 px gaps. |
| **S8 — The code** | 1:02–1:12 | "The code stays small: search the registry, rank against the query, keep the top three, and hand those to Claude." | Python block (see §D) + `TOP-K = 3` | Code reveals line by line (not character by character). As `[:3]` lands, three chips snap in beside the code and a counter ticks `1,000 → 3`. | Code card: mono 40 px, line height 1.45, ≤ 34 chars/line, `#0E1117` background, syntax highlighted. |
| **S9 — A/B comparison** | 1:12–1:22 | "Same thousand tools. Method A exposes a thousand. Method B exposes three. Same job, far less overhead." | `ILLUSTRATIVE EXAMPLE` · `METHOD A — load entire catalog: exposed 1,000 · relevant 3 · context overhead HIGH · routing complexity HIGH` · `METHOD B — progressive discovery: exposed 3 · relevant 3 · context overhead LOW · routing complexity LOWER` | Two stacked cards, matching rows vertically aligned for direct comparison. The `ILLUSTRATIVE EXAMPLE` plate stays on screen for the whole scene. | **No invented numbers.** Only counts literally true of the demo (1,000 / 3) plus qualitative HIGH/LOW. Token, latency and cost figures only after §E is run. |
| **S10 — The STEM stack** | 1:22–1:29 | "This is information retrieval, ranking algorithms, software architecture, distributed systems and context engineering, in one build." | `INFORMATION RETRIEVAL` · `ALGORITHMS` · `SOFTWARE ENGINEERING` · `DISTRIBUTED SYSTEMS` · `CONTEXT ENGINEERING` · `LLM AGENTS` | Six chips land in a 2 × 3 grid, each with a small glyph (index, sort bars, module blocks, network nodes, window frame, agent dot). | One line of type per chip, no sub-captions. |
| **S11 — MCP and the ecosystem** | 1:29–1:41 | "This matters as ecosystems grow. Anthropic's tool search tool already defers loading until Claude needs a tool, and the MCP roadmap calls progressive discovery a priority — check the official docs before you quote any specifics." | `MCP · MODEL CONTEXT PROTOCOL` · `tools/list → paginated catalog` · `defer_loading: true` · plate `CURRENT-DEVELOPMENT INFO — VERIFY AGAINST OFFICIAL DOCS` | Three MCP server nodes connect to one client, each exposing a stack of tool chips. Only matched chips travel the wire into the agent; the rest stay parked at the server. | Every product claim must survive §F. Verify plate stays up the whole scene. Say "tool search tool" and `defer_loading` exactly as documented, or cut the specifics and keep the concept. |
| **S12 — The loop** | 1:41–1:47 | "Discover, filter, rank, load, execute." | `DISCOVER ↓ FILTER ↓ RANK ↓ LOAD ↓ EXECUTE` | Five words light one per spoken word, then compress into a ring that rotates once. | Cue each highlight to the measured word boundary, not an even split. |
| **S13 — Takeaway** | 1:47–1:55 | "The goal isn't to give an AI agent every tool at once. The goal is to give it the right tools at the right time." | `NOT every tool at once` / `THE RIGHT TOOLS AT THE RIGHT TIME` | First line greys and strikes through on "isn't"; second line scales up in terracotta. Background dims to isolate the type. | Largest type in the film (110–120 px). This is the screenshot frame — design it to stand alone. |
| **S14 — Close** | 1:55–2:02 | "Progressive tool discovery can make agent systems more focused, efficient and easier to scale. I'm Dhrumil Shah, and this is how smarter tool routing helps us build better AI agents." | `DISCOVER → FILTER → RANK → LOAD → EXECUTE` · `DHRUMIL SHAH` · `progressive-tool-router` | Pipeline redraws once as a ribbon, then the end card settles: title, presenter, repo folder. | Hold the end card ≥ 2 s after narration so a paused scroll can read it. |

---

## A. Full narration script

> ~290 words ≈ 115–120 s at this series' measured rate (~146 wpm with Kokoro `af_kore`).
> Re-measure after generating audio. If it runs past 120 s, cut from S10 and S11 first — never
> speed the voice up.

**S1.** Hi, I am Dhrumil Shah, and this video is about why giving an AI agent more tools can actually make it worse — and how we can build a smarter progressive tool router with Claude.

**S2.** If an AI agent has access to a thousand tools, does it really need all thousand in its context just to analyze one CSV file?

**S3.** Every tool costs context before the work even starts — a name, a description, an input schema, parameters, permissions.

**S4.** Multiply that by a thousand and the context fills with menu instead of meal — bigger search space, more latency, more cost, more chances to pick the wrong tool.

**S5.** Take a real request: analyze this CSV and create a chart. The agent loads a thousand definitions, searches them all, and ends up using three.

**S6.** Progressive discovery flips it. Read the intent first, search a tool registry, and load only what the task needs.

**S7.** Claude can help you build each piece: intent classification, a tool registry, semantic search, ranking, top-K selection, then execution.

**S8.** The code stays small: search the registry, rank against the query, keep the top three, and hand those to Claude.

**S9.** Same thousand tools. Method A exposes a thousand. Method B exposes three. Same job, far less overhead.

**S10.** This is information retrieval, ranking algorithms, software architecture, distributed systems and context engineering, in one build.

**S11.** This matters as ecosystems grow. Anthropic's tool search tool already defers loading until Claude needs a tool, and the MCP roadmap calls progressive discovery a priority — check the official docs before you quote any specifics.

**S12.** Discover, filter, rank, load, execute.

**S13.** The goal isn't to give an AI agent every tool at once. The goal is to give it the right tools at the right time.

**S14.** Progressive tool discovery can make agent systems more focused, efficient and easier to scale. I'm Dhrumil Shah, and this is how smarter tool routing helps us build better AI agents.

---

## B. Visual asset list

All assets are code-generated (React/SVG in Remotion, Manim, matplotlib). No stock imagery, no
third-party icon packs, no imitation of any existing channel's branding.

**Components**
1. `ToolDot` — one tool in the cloud; grey / teal / amber states.
2. `ToolCloud` — deterministic 25 × 40 grid (1,000 dots), staggered entrance, dissolve-out path.
3. `ToolChip` — named tool pill (CSV Reader, Data Analyzer, Chart Generator); reused in S5, S6, S8, S9.
4. `AgentNode` — agent core with input port and pulse ring.
5. `ContextWindowBar` — vertical bar split "tool definitions" vs "actual task".
6. `TokenMeter` — numeric ticker; label-only unless fed measured data.
7. `ToolDefinitionCard` — expandable card: `name`, `description`, `inputSchema`, `parameters`, `annotations`.
8. `CascadeChain` — S4 seven-link vertical chain with down-arrows and the ⚠ terminal state.
9. `RouterStack` — S7 eight-stage architecture stack with per-stage gloss.
10. `CodePanel` — syntax-highlighted Python card, 34-char line budget, line-by-line reveal.
11. `ComparisonCard` — Method A / Method B with aligned rows and the `ILLUSTRATIVE EXAMPLE` plate.
12. `STEMChipGrid` — 2 × 3 discipline chips with glyphs.
13. `MCPTopology` — three servers, one client, animated wire, travelling chips.
14. `LoopRing` — Discover → Filter → Rank → Load → Execute ring.
15. `EndCard` — title, presenter, folder name.
16. `CaptionBand` — burned-in captions with keyword highlighting.

**Charts / diagrams**
17. Retrieval-similarity visual: query vector vs tool vectors, cosine-similarity bars sorted
    descending — values from the real demo run, not invented.
18. Top-K cut line animating across the ranked bars.
19. Optional post-benchmark charts in `assets/charts/` once §E has been run.

**Sound design** — `tick` (chip select), `swish` (routing), `warn` (amber cascade link), `search`
(magnifier sweep), `rank` (bars sorting), `whoosh` (transition), `chime` (takeaway, end card).
One cue per beat maximum; music bed ≥ 18 dB under narration.

---

## C. Architecture diagram

```text
                    ┌──────────────────────────────┐
                    │        USER QUERY            │
                    │ "Analyze this CSV and make   │
                    │  a chart"                    │
                    └──────────────┬───────────────┘
                                   ↓
                    ┌──────────────────────────────┐
                    │   INTENT CLASSIFICATION      │  what is being asked?
                    │   → intent: data_analysis    │
                    │   → entities: csv, chart     │
                    └──────────────┬───────────────┘
                                   ↓
   ┌───────────────────────────────────────────────────────────┐
   │                      TOOL REGISTRY                        │
   │  1,000 tool records: name · description · inputSchema ·   │
   │  tags · server · permissions · embedding                  │
   └──────────────┬────────────────────────────────────────────┘
                  ↓
   ┌──────────────────────────────┐        ┌────────────────────────┐
   │      SEMANTIC SEARCH         │ ←──────│  QUERY EMBEDDING /     │
   │  (embeddings, BM25, hybrid)  │        │  keyword expansion     │
   └──────────────┬───────────────┘        └────────────────────────┘
                  ↓
   ┌──────────────────────────────┐
   │          RANKING             │  score = similarity
   │                              │        + tag/intent match
   │                              │        + success-rate prior
   │                              │        − cost/permission penalty
   └──────────────┬───────────────┘
                  ↓
   ┌──────────────────────────────┐
   │      TOP-K SELECTION         │  K = 3 (+ always-on essentials)
   └──────────────┬───────────────┘
                  ↓
   ┌──────────────────────────────┐
   │        AGENT CONTEXT         │  only K tool definitions enter
   │   CSV Reader · Data Analyzer · Chart Generator            │
   └──────────────┬───────────────┘
                  ↓
   ┌──────────────────────────────┐
   │       CLAUDE (AGENT)         │
   └──────────────┬───────────────┘
                  ↓
   ┌──────────────────────────────┐
   │       TOOL EXECUTION         │  → MCP servers / local tools
   └──────────────┬───────────────┘
                  ↓
   ┌──────────────────────────────┐
   │   RESULT + TELEMETRY LOG     │  chosen tool, rank, latency, tokens
   └──────────────────────────────┘
                     ↑
                     └── feedback: success/failure updates the prior
```

Escalation path (one extra line if you extend the cut): if the top-K set fails, widen K or
re-search using the failure as extra query context — never fall back to dumping the whole catalog.

---

## D. Claude build demo

**On-screen pseudocode (S8) — keep this exact shape, ≤ 34 characters per line:**

```python
query = "Analyze this CSV and create a chart"

tools = search_tool_registry(query)

selected_tools = rank_tools(
    query,
    tools
)[:3]

response = claude.run(
    prompt=query,
    tools=selected_tools
)
```

**Runnable demo** — `src/progressive_tool_router.py` implements the same flow for real: a synthetic
1,000-tool registry, TF-IDF retrieval (swappable for embeddings), a transparent scoring function,
top-K selection, and an optional Claude call. It prints the routing decision and the tool-definition
overhead of Method A vs Method B, so the comparison in S9 is reproducible rather than asserted.

**Two ways to ship this**
1. **Client-side router (this demo).** You own retrieval, ranking and K, and you can log everything
   for §E. Works with any model or runtime.
2. **Anthropic's tool search tool.** Documented server-side feature: send all definitions but mark
   rarely-used ones `defer_loading: true`, keep the search tool itself non-deferred, and Claude
   discovers tools on demand; discovered tools arrive as `tool_reference` blocks that the API
   expands. A custom client-side search can also return `tool_reference` blocks (for example from an
   embedding index). Verify parameter names, variants and limits against current docs before putting
   them on screen — see §F.

---

## E. Benchmark plan

Run this before publishing any number. Keep measured and illustrative values in separate files and
label them differently on screen.

**Fixed conditions:** one model version, one registry snapshot, one machine, the same 50–100 task
prompts, N ≥ 5 repeats per condition, median and p95 reported, warm-up run discarded.

| Metric | How to measure | Tooling |
|---|---|---|
| Tools exposed | Count definitions actually placed in context per request | Router log; for deferred setups count non-deferred + expanded references |
| Context / token overhead | Token count of the tool block alone, Method A vs Method B | Anthropic token-counting endpoint (authoritative) or `usage.input_tokens` |
| Tool-selection accuracy | Label each task with its correct tool(s); score top-1 and top-K recall | `bench/tasks.jsonl`; report per-category accuracy |
| Routing latency | Query → selected-tool list (retrieval + ranking only) | `time.perf_counter()` around the router |
| Total agent latency | Query → final answer, including model and tool execution | Wall clock per run; median + p95 |
| Estimated inference cost | Tokens × published per-token price for that exact model | Computed from measured tokens; record the price date |
| Failure modes | Tasks where the right tool fell outside top-K | Miss log — this is what sets K and the escalation policy |

**Reporting rules**
- Every on-screen number is either **MEASURED** (model, date, task count, repeats stated) or
  **ILLUSTRATIVE** (plate visible for its full on-screen life). Never mix them in one card.
- Do not present published vendor figures as your own measurements; attribute them.
- Ship the task set and registry snapshot with the repo so anyone can reproduce the result.

`src/benchmark_router.py` is the harness: it runs the router over a task file, records every metric
above, marks whether token counts are measured or estimated, and writes `bench/results.csv`.

---

## F. Fact-check checklist

Verify each row against **official Anthropic docs** and the **official MCP specification/roadmap**
immediately before publication; both move fast. Record the date checked.

| # | Statement in the video | Where | Verify against | Status (checked 2026-09-28) |
|---|---|---|---|---|
| F1 | A tool definition carries name, description, input schema, parameters, permissions/annotations | S3 | MCP spec *Tools*: `name`, `title`, `description`, `icons`, `inputSchema`, `outputSchema`, `annotations` | ✅ verified — say "annotations/permissions", not an invented field |
| F2 | Tool definitions consume context before the user's task | S3, S4 | Anthropic *Tool search tool*: "Loading every tool definition up front causes … Context bloat" | ✅ verified |
| F3 | Selection accuracy can degrade as tool count grows | S4 | Anthropic docs: accuracy "degrades once you exceed 30–50 available tools" | ✅ verified — keep narration qualitative |
| F4 | Claude can defer tool loading until needed | S11 | Anthropic *Tool search tool*: `defer_loading: true`, regex + BM25 variants, `tool_reference` expansion | ✅ verified — re-check variant names and dates before publish |
| F5 | Custom/embedding-based tool search is supported | §D | Anthropic docs: custom client-side search returns `tool_reference` blocks | ✅ verified |
| F6 | MCP roadmap prioritises progressive discovery | S11, S12 | MCP roadmap 2026-08-22: "a server can offer a small entry point and reveal more of its catalog as the conversation narrows" | ✅ verified — roadmap ≠ shipped spec; label as current-development |
| F7 | `tools/list` is paginated and cacheable | S11 visual | MCP spec: cursor pagination, `nextCursor`, `ttlMs`, deterministic ordering | ✅ verified |
| F8 | Any token / latency / cost figure | S9, any chart | Your own §E run, or an attributed vendor figure | ⛔ **not yet measured** — keep S9 qualitative until §E runs |
| F9 | "1,000 tools" and "3 tools" | S2, S5, S9 | True of the demo registry in `src/` | ✅ true by construction — keep the registry at exactly 1,000 |
| F10 | Any named model version | any | Current Anthropic model list | ⚠ avoid naming a model version on screen; it dates the video |
| F11 | "More tools make a model less intelligent" | — | — | ⛔ **never state this.** Supported framing is context, routing and selection overhead |

---

## G. 9:16 editing instructions

**Safe zones (design px on 1080 × 1920; ×2 for the 4K master)**
- Left/right margins 72 px; nothing readable beyond x 1008.
- Right interaction rail: keep x > 940 clear of essential content.
- Top: nothing essential above y 150.
- Content band: y 260 → 1330 (all diagrams, code, cards).
- Source/disclaimer line: y ≈ 1340.
- Caption band: y 1372–1540, centred. **Nothing essential below y 1540.**

**Code sizing** — mono 40–44 px, line height 1.45, ≤ 34 chars/line, ≤ 12 visible lines, 32 px card
padding, `#0E1117` background, comments `#6B7280`. Reveal a line every ~0.25 s.

**Diagram sizing** — vertical stacks; node height ≥ 96 px; labels ≥ 32 px; arrow gap 24 px; never
more than 8 stacked nodes; strokes ≥ 3 px to survive platform compression.

**Subtitles** — 1–2 lines, ≤ 34 chars/line, 44–48 px bold sans, centred on a 92%-opacity plate.
Highlight in accent: *AI Agent, Tool Calling, MCP, Context Window, Progressive Discovery, Tool
Registry, Semantic Search, Ranking, Top-K, Latency, Token Usage, Context Engineering*. Cue from
measured audio, never even division.

**Transitions and pacing** — hard cut on every question and every number reveal; 6–8 frame
cross-dissolve elsewhere; no spins or 3D flips. Minimum shot 1.5 s; maximum single-idea hold 12 s
(S11 is longest — break it with the topology animation). Target one visual event per 1.5–2 s.

**Motion** — spring entrances (damping ≈ 20, stiffness ≈ 140), 8–12 frame ramps, ease-out. Motion
must carry meaning: dots *travel* into the agent, irrelevant tools *fall away*, the top-K line
*cuts* the ranked list.

**Colour** — background `#0B0D11`, surface `#141821`, ink `#E8E6E1`, muted `#9BA1AC`, accent
terracotta `#D97757`, positive teal `#3E7C74`, caution amber `#B8912F`. Never encode state by colour
alone: colour + shape/glyph + label.

---

## H. Final video metadata

- **Video title:** Why Giving an AI Agent More Tools Can Make It Worse — Build a Progressive Tool Router with Claude
- **Alternative YouTube title:** 1,000 AI Tools vs. 3 — Why More Context Can Make an Agent Worse
- **Short description (≤ 150 chars):** An AI agent with 1,000 tools doesn't need all 1,000 to read one CSV. Here's how a progressive tool router fixes that — built with Claude.
- **YouTube description:**

```text
If an AI agent has access to 1,000 tools, should all 1,000 sit in its context just to analyze one CSV file?

Every tool definition costs context before the work starts — name, description, input schema,
parameters, permissions. Scale that to a large catalog and you add context overhead, a bigger
search space, more routing complexity, more latency and cost, and more chances to select the
wrong tool.

This short builds the alternative: a Progressive Tool Router.

USER QUERY → INTENT CLASSIFICATION → TOOL REGISTRY → SEMANTIC SEARCH → RANKING → TOP-K → AGENT CONTEXT → EXECUTION

Covered:
- Why tool definitions are a context cost, not a free option
- A worked example: "analyze this CSV and create a chart" needs 3 tools, not 1,000
- Building the router with Claude: intent, registry, retrieval, ranking, top-K
- Why this matters for MCP as tool ecosystems grow
- How to benchmark it honestly: tools exposed, token overhead, selection accuracy, latency, cost

STEM areas: LLM agents, information retrieval, ranking algorithms, software engineering,
distributed systems, context engineering.

Numbers shown as "ILLUSTRATIVE EXAMPLE" are examples, not measurements. Real values depend on your
tool schemas, model, architecture and implementation — measure your own with the benchmark plan in
the repo. Product capabilities described here are current-development information: verify against
official Anthropic and Model Context Protocol documentation.

Code and full production notes: progressive-tool-router

— Dhrumil Shah
```

- **Hashtags:** `#AIAgents` `#Claude` `#MCP` `#ContextEngineering` `#MachineLearning` `#InformationRetrieval` `#SoftwareEngineering` `#LLM` `#ComputerScience` `#STEM`
- **Thumbnail text:** `1,000 TOOLS → 3` with sub-line `Why more context can make an agent worse` — silhouetted agent node, 997 dots dimmed, 3 chips lit.
- **GitHub project/folder name:** `progressive-tool-router` (series-prefixed alternative: `claude-liam-progressive-tool-router`).

---

## I. Final quality-control checklist

| # | Check | Pass when |
|---|---|---|
| 1 | Opens with "Hi, I am Dhrumil Shah…" | It is the first spoken line; no hook precedes it |
| 2 | Resolution 2160 × 3840, aspect 9:16 | `ffprobe` reports exactly this on the master |
| 3 | 30 fps constant, MP4 H.264/H.265, AAC 48 kHz stereo | `ffprobe` streams confirm |
| 4 | Runtime 90–120 s | Measured master duration |
| 5 | Narration matches captions word-for-word | Diff the script against the SRT |
| 6 | Captions cued from measured audio | Validation report shows no overlaps, no single-word cues |
| 7 | Diagrams readable on a phone | Reviewed at 1080-logical width; every label ≥ 32 px |
| 8 | Code readable on a phone | ≤ 34 chars/line, ≥ 40 px, no clipping |
| 9 | Hypothetical metrics labelled | Every non-measured number carries `ILLUSTRATIVE EXAMPLE` for its full on-screen life |
| 10 | Technical claims sourced | Every §F row marked ✅ with a date |
| 11 | No unsupported performance claims | No token/latency/cost/accuracy figure without §E data or attribution |
| 12 | MCP terminology accurate | Terms match the current spec; roadmap items labelled as roadmap |
| 13 | No "more tools = dumber model" framing | Narration and on-screen text both audited |
| 14 | Audio clear, music subordinate | −14 LUFS integrated, −1.5 dBTP, bed ≥ 18 dB under voice |
| 15 | Structure problem → solution → implementation → takeaway | S2–S5 problem, S6–S7 solution, S8–S9 implementation, S13–S14 takeaway |
| 16 | Safe areas respected | Nothing essential above y 150, below y 1540, or right of x 940 |
| 17 | Original visuals only | No third-party branding, icon packs, or imitation of another creator's style |
