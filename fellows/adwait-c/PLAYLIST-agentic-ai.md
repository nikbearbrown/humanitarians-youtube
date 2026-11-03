# Playlist — Agentic AI: From the Loop to MCP

**Fellow:** Adwait Changan · **Channel:** @HumanitariansAI · **Voice:** Kokoro `am_onyx` ("Onyx, in for Humanitarians AI")
**Cadence:** one episode every Friday, starting 2026-08-07.
**Audience:** students and mid-career learners getting started with AI — the HAI spine question (*when to use AI, and when not to*) is carried in every verdict.

## The arc

The playlist is a single argument delivered in ten parts. Episode 1 defines an agent
as *a model inside a loop*. Episodes 2–8 add one capability per week and charge for it
honestly. Episodes 9–10 land on MCP, which is only interesting once you have felt the
integration pain it removes — so it comes last, not first.

| # | Friday | Topic slug | Episode title | Skill | The one idea it lands |
|---|---|---|---|---|---|
| 1 | 2026-08-07 | `WhatMakesAIAgentic` | What Makes an AI "Agentic" | ai-explainer | An agent is not a smarter model — it is the same model placed inside a loop that can act. |
| 2 | 2026-08-14 | `TheAgentLoop` | The Agent Loop | ai-explainer | The loop only works because the observation is real; remove it and you get a confident guess repeated. |
| 3 | 2026-08-21 | `ToolsAndFunctionCalling` | Tools: Giving a Model Hands | ai-explainer | A tool is a contract, not a function — the description is the part the model actually reads. |
| 4 | 2026-08-28 | `AgentMemory` | Memory and Context | ai-explainer | Agents don't forget, they overflow — context is a budget you spend, not a place you store things. |
| 5 | 2026-09-04 | `PlanningAndDecomposition` | Planning and Decomposition | ai-explainer | Planning helps when steps are expensive and helps nothing when they're cheap. |
| 6 | 2026-09-11 | `GroundingAndRetrieval` | Grounding and Retrieval | ai-explainer | Retrieval doesn't make an agent truthful; citation you can check does. |
| 7 | 2026-09-18 | `GuardrailsAndEvals` | Guardrails and Evals | ai-explainer | You cannot review every run, so you must be able to score one — evals are the stopping rule for the builder. |
| 8 | 2026-09-25 | `MultiAgentSystems` | Multi-Agent Systems | ai-explainer | More agents buys parallelism and costs coherence; most "multi-agent" wins are one agent with better tools. |
| 9 | 2026-10-02 | `WhatIsMCP` | MCP — the Model Context Protocol | ai-explainer | MCP turns an M×N integration problem into M+N by standardising the seam, not the model. |
| 10 | 2026-10-09 | `BuildingAnMCPServer` | Building an MCP Server | cli-explainer | Build one end to end, connect a client, and watch the agent discover the tools it was never told about. |

## Continuity rules across the playlist

1. **Each episode ends by naming the next one** in the outro subline (`Episode N of 10`)
   and the last narration line. The playlist reads as a course, not ten uploads.
2. **One running artifact.** `agent_loop.py` is authored in Episode 1 as a real,
   runnable file and is extended — never rewritten from scratch — in later episodes.
   ACTUAL-CODE LAW: every code beat shows real file contents that run.
3. **No forward-references that don't pay off.** An episode may name a later topic
   once, as a promise; it may not lean on it.
4. **Register:** Teardown (Onyx). Narrate the mechanism, then judge it — what the
   design gets right, where it bites.
5. **HAI honesty clause.** Every verdict card carries at least one line naming the
   limit or the cost, never only the capability.

## Output naming

Every master ships as:

```
TopicName_AdwaitChangan_YYYY-MM-DD.mp4
```

set as `metadata.slug` in each `beat_sheet.json`, so `compile.py` emits it directly
(`<slug>.mp4` for the master, `<slug>-slate.mp4` for the review cut). Build folders keep
the repo's fellows convention, `fellows/adwait-changan/<YYYY-MM-DD>-<kebab-slug>/`.

## Build contract (per episode)

```bash
source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate
cd /Users/adwaitchangan/Study/Brutalist/brutalist.art
python3 runtime/scripts/generate_audio_kokoro.py <REEL>   # audio is the clock
python3 runtime/scripts/remotion_scenes.py <REEL>         # render every beat
python3 runtime/scripts/compile.py <REEL> --review        # slate/review cut
# frame-level VISUAL QC → _qc/REPORT.md → fix → re-render
./art final <REEL>                                        # 4K clean master
```

GATE P (`PEDAGOGY.md`, signed "VERDICT: PASS") binds before audio. Nothing publishes
from this repo — the master stays in the reel folder.
