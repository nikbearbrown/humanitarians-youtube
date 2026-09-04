# MCP Builder. — Narration Script (GATE P)

*Skill: `hai-simple` (redo of a `skill-teardown` Teardown sheet). Register:
**Plain**. 7 beats ≈ 1:55.*
*Carry-out written first (CARRY-OUT.md, GATE C). Every beat lands it.*

**Cold open:** Brutalist Hesitant Writer (Remotion, free, no human/paid step).
**Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "Someone asks how to write an MCP server for GitHub. But mcp-builder starts with research, not code — study the protocol, pick a language, plan the tool list first. What does that cover?" | BrutalistHesitantWriter — types "How do I write an MCP server for GitHub?", corrects "write" → "research and build" |
| B01 | 1 stakes / 2 wrong guess, falsified | Research means three things before any code: read the actual MCP protocol spec, pick a language — TypeScript with Zod is recommended — and plan the tool list against the target API's own documentation. When those docs are live, that plan is grounded in the API's real shape. When they're offline or stale, the research phase has nothing solid to plan from, and stalls. | a code editor icon jumping straight at "implement", crossed out; the real order — RESEARCH → IMPLEMENT → REVIEW → EVALUATE — with RESEARCH expanding into protocol / language / tool list; docs live vs docs stale, branching |
| B02 | 3 mechanism / **4 anchor planted** | Every tool carries four things: an input schema — Zod in TypeScript, Pydantic in Python — typed and constrained, with a description on each field; an output schema, so the client knows the shape of what comes back; four annotations — read-only, destructive, idempotent, open-world; and an error message that names the problem and suggests the fix. Names follow one pattern, prefix then action: `github`, underscore, `create`, underscore, `issue` — a write. `github`, underscore, `list`, underscore, `repos` — read-only. | four tool-anatomy cards; THE ANCHOR — `github_create_issue` and `github_list_repos` built segment by segment, side by side, one tagged WRITE, one tagged READ-ONLY |
| B03 | **4 anchor payoff / 5 both directions** | Here's the both-directions of the evaluation rule. `github_list_repos` is read-only — call it, check the answer against the real list, done. It fits the ten-question proof directly. `github_create_issue` writes real state, an actual issue gets created. Since the standard requires read-only, verifiable questions, a task built around `create_issue` can't be one of the ten — even though it's exactly the call an agent gets asked to make. Same asymmetry in the stack: TypeScript with Zod is recommended, even for a team that knows Python better. | THE ANCHOR RETURNS — `list_repos` fires into a lit "checked ✓" card; `create_issue` fires into a card marked "writes state — outside the ten"; a small TypeScript/Python asymmetry note beneath |
| **BCRY** | **6 carry-out** | A good MCP server isn't judged by how many endpoints it covers — it's judged by real tasks it can prove it completes. And that proof only reaches as far as read-only calls, checked directly against the real answer. | the sentence, alone, serif, large |
| BHTF | handoff | Your turn. Here's the prompt — read it with me: Build an MCP server for the OpenWeatherMap API. Use TypeScript and Zod. Cover current weather, forecasts, and historical data. Follow the mcp-builder skill. Watch whether Claude starts with research — the protocol, the API's docs — before writing any code. Then check each tool for a Zod input schema, an output schema, and the four annotations: read-only, destructive, idempotent, open-world. Liam, in for Bear. | ClaudeComposerAsk, "Your turn." |
| BOUT | outro | MCP Builder. Liam, in for Bear. | OutroCTA, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B01 states research-comes-first; the tool-anatomy/naming mechanism waits until B02 |
| Wrong guess surfaced *and falsified by a case* | B00 states the naive read (just write it); B01 falsifies it with a case — research grounded in live docs produces a real plan; research with no reachable docs has nothing to plan from and stalls |
| Exactly one inference flag | none needed — every claim is read directly off the source's own documentation of the skill, no inference beyond it |
| One anchor, planted early, paid off late | B02 → B03 (`github_create_issue` / `github_list_repos`, the same naming pattern, one a write and one read-only) |
| Both directions | B03 — a read-only tool fits the ten-question proof directly; a tool that writes state can't be verified the same way, even though it's a normal call an agent makes |
| No design judgment | B03 states the read-only/write asymmetry as a fact about what the evaluation standard can check, never a verdict on whether that standard should exist or whether TypeScript-over-Python is the right call |

## Deliberately not claimed

- **Not a verdict on the design.** The source's B05 framed the live-docs
  dependency, the read-only eval constraint, and the TypeScript
  recommendation as "what it gets right" / "where it bites" — Teardown
  language. Plain keeps the same underlying facts but states them as
  mechanism and asymmetry, not a critique of the skill file.
- **Not a claim that write-tools go untested.** The source only says the
  *ten-question, read-only* standard can't verify them the same direct
  way — this reel doesn't invent a claim about how (or whether) they get
  proven some other way.
- **Not a full recitation of all four phases at equal depth.** The source
  also covers project structure, the API client, and the MCP Inspector
  review step; this 7-beat Plain cut compresses to the research-first
  mechanism and the tool-anatomy/eval anchor, logged here rather than
  invented on screen.

## Handoff prompt (BHTF, read aloud)

> "Build an MCP server for the OpenWeatherMap API. Use TypeScript and Zod.
> Cover current weather, forecasts, and historical data. Follow the
> mcp-builder skill."

Why it's worth running: watching whether Claude opens with research (the
MCP protocol, OpenWeatherMap's own docs) before any implementation code,
and whether each resulting tool carries a Zod schema, an output schema,
and all four annotations, surfaces whether the research-first order and
the tool-anatomy rules from B01/B02 actually land in a live session.

---
**GATE P — signed:** ______________________  (human)
