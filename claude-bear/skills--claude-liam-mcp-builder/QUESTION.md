# QUESTION

**The question:** "MCP Builder" — when someone asks Claude to build an MCP
server for an external API, does the skill start writing code, or does it
do something else first? And once code starts, what actually separates a
server that merely runs from one that's proven to work? Answered using the
`mcp-builder` skill's own worked examples — a GitHub `create_issue` tool and
a GitHub `list_repos` tool — as the concrete case.

**Mode:** redo — source is
`anthropics/skills/youtube/claude-liam-mcp-builder/beat_sheet.json` (a
fully-filled, fully-narrated Teardown-register reel: metadata `register:
"Teardown"`, `brand: "claude-liam"`, `source_skill` pointing at
`anthropics/skills/skills/mcp-builder/SKILL.md`, modifier
`skill-teardown`). 7 beats — B00 cold open, B01 anatomy, B02 tool anatomy,
B05 teardown, BVDT verdict, BHTF handoff, BOUT outro; B00 was already
`ClaudeComposerAsk` REMOTION, not AI-video/pantry, so NO-GENAI/NO-PANTRY LAW
required no substitution beyond the WRITER LAW swap. This reel keeps the
question and the source's body facts, re-registers the narration to Plain,
replaces the cold open with the Brutalist Hesitant Writer, folds the
source's BVDT verdict recap into a proper carry-out beat, restates the
source's B05 "gets right / bites" as a both-directions mechanism fact
instead of a design judgment, and closes with the Humanitarians AI skin.

**Why it earns a reel:** mcp-builder runs four phases in fixed order —
research (study the MCP protocol, pick a language, plan the tool list
before writing anything), implement (project structure, an API client,
then each tool), review and test with the MCP Inspector, and evaluate (ten
questions). TypeScript with Zod is the recommended stack; streamable HTTP
for remote servers, stdio for local. Every tool needs four elements: a
typed input schema (Zod/Pydantic), an output schema, four annotations
(`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`), and
an actionable error message. Naming is a fixed pattern, prefix then action
— `github_create_issue`, `github_list_repos`. The evaluation gate requires
ten independent, read-only, complex, realistic, verifiable questions in
XML format — and that requirement itself has an asymmetry worth surfacing:
a read-only tool fits the proof directly; a tool that writes real state
cannot be checked the same way.

**Naive framing (B00, corrected on screen):** "How do I write an MCP
server for GitHub?" → corrects "write" to "research and build" (the skill
does not start with code; it starts with studying the protocol, choosing a
language, and planning the tool list).

**Body facts carried from source (unchanged):**
- Four phases, fixed order: research → implement → review/test → evaluate
- Research: read the MCP protocol spec, pick a language (TypeScript with
  Zod recommended; streamable HTTP for remote servers, stdio for local),
  plan the tool list before writing code
- Research relies on fetching the target API's own live documentation —
  if those docs are unavailable or stale, research has nothing solid to
  plan from
- Implement: project structure, an API client, then each tool
- Tool anatomy, four elements: Zod (or Pydantic) input schema, typed and
  constrained, with per-field descriptions; `outputSchema` for structured
  output; four annotations (`readOnlyHint`, `destructiveHint`,
  `idempotentHint`, `openWorldHint`); actionable error messages
- Naming convention: consistent prefix + action, e.g. `github_create_issue`,
  `github_list_repos`
- Review/test with the MCP Inspector
- Evaluate: ten evaluation questions — independent, read-only, complex,
  realistic, verifiable, in XML format
- The read-only requirement rules out naturally complex tasks built around
  a tool that writes state (e.g. `create_issue`) from being one of the ten
- TypeScript is the recommended language even when a team's expertise is
  in Python
- Source's Your Turn worked example: an MCP server for the
  OpenWeatherMap API, current weather + forecasts + historical data
