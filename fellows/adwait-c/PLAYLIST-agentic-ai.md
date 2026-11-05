# Playlist — Agentic AI: From the Loop to MCP

**Fellow:** Adwait Changan · **Channel:** @HumanitariansAI · **Voice:** Kokoro `am_onyx`
**Cadence:** one episode every Friday, starting 2026-08-07.
**Audience:** students and mid-career learners getting started with AI — the HAI spine
question (*when to use AI, and when not*) is carried in every verdict.

## The arc

A single argument delivered in parts. The first defines an agent as *a model inside a
loop*. The middle adds one capability per week and charges for it honestly. MCP lands
late, not early, because it is only interesting once you have felt the integration pain it
removes. The last two go past MCP on purpose: once you can build one, the useful questions
are what it must not be trusted with, and when not to build one at all.

| # | Friday | Topic slug | Title | The one idea it lands |
|---|---|---|---|---|
| 1 | 2026-08-07 | `WhatMakesAIAgentic` | What Makes an AI "Agentic" | An agent is not a smarter model. It is the same model placed inside a loop that can act. |
| 2 | 2026-08-14 | `TheAgentLoop` | The Agent Loop | The loop works only because the observation is real. Remove it and you get a confident guess, repeated. |
| 3 | 2026-08-21 | `ToolsAndFunctionCalling` | Tools: Giving a Model Hands | A tool is a contract, not a function. The description is the part the model actually reads. |
| 4 | 2026-08-28 | `AgentMemory` | Memory and Context | Agents do not forget, they overflow. Context is a budget you re-pay every turn. |
| 5 | 2026-09-04 | `PlanningAndDecomposition` | Planning and Decomposition | Planning helps when steps are expensive and helps nothing when they are cheap. |
| 6 | 2026-09-11 | `GroundingAndRetrieval` | Grounding and Retrieval | Retrieval does not make an agent truthful. A citation you can check does. |
| 7 | 2026-09-18 | `GuardrailsAndEvals` | Guardrails and Evals | You cannot read every run, so you must be able to score one. |
| 8 | 2026-09-25 | `MultiAgentSystems` | Multi-Agent Systems | More agents buys parallelism and costs coherence. Most wins are one agent with better tools. |
| 9 | 2026-10-02 | `WhatIsMCP` | What Is MCP? | It turns an M×N integration problem into M+N by standardising the seam, not the model. |
| 10 | 2026-10-09 | `BuildingAnMCPServer` | Building a Tool Server | Three calls are the whole shape, and your docstring is what the machine reads. |
| 11 | 2026-10-16 | `TheConfusedDeputy` | The Confused Deputy | The text has no permissions. The agent has yours. |
| 12 | 2026-10-23 | `WhenNotToBuildAnAgent` | When Not to Build an Agent | A failed condition is a specification for what to build instead, not a rejection. |

Every episode ships in **both** aspect ratios: a 16:9 master at 3840×2160 and a 9:16
derivative cut at 2160×3840.

## Continuity rules

1. **No episode or week numbers on screen or in narration**, and no back-references to a
   previous video. Each one stands alone; the playlist supplies the order.
2. **One running artifact.** Each episode ships a real, runnable file, extended rather than
   rewritten. ACTUAL-CODE LAW: every code beat shows real file contents that run, and the
   props are generated from the file at authoring time rather than transcribed.
3. **Every number on screen is printed by a real run**, captured in `SOURCES.md`. A figure
   that is a judgement or an assumption is labelled as one in `FACTCHECK.md`.
4. **Register:** Teardown. Narrate the mechanism, then judge it — what the design gets
   right, and where it bites.
5. **HAI honesty clause.** Every verdict card carries at least one line naming the limit or
   the cost, never only the capability.
6. **The 9:16 cut drops the code beat.** Portrait is 1080 wide and these functions run 70
   to 86 characters per line. Code cannot reflow, so type sized to the longest line is not
   readable on a phone. The long cut carries the code and the short outro points at it.

## Output naming

```
TopicName_AdwaitChangan_YYYY-MM-DD.mp4          # 16:9 master
TopicName_AdwaitChangan_YYYY-MM-DD-short.mp4    # 9:16 derivative, in short/
```

Set as `metadata.slug` in each `beat_sheet.json` so `compile.py` emits it directly. Build
folders keep the repo's convention, `fellows/adwait-c/<YYYY-MM-DD>-<kebab-slug>/`.

## Build contract (per episode)

```bash
source /Users/adwaitchangan/Study/Brutalist/brutalist.art/.venv/bin/activate
cd /Users/adwaitchangan/Study/Brutalist/brutalist.art
python3 runtime/scripts/generate_audio_kokoro.py <REEL>   # audio is the clock
python3 runtime/scripts/remotion_scenes.py <REEL>         # render every beat
python3 runtime/scripts/compile.py <REEL> --review        # review cut
# frame-level VISUAL QC at 95% of each beat's span → _qc/REPORT.md → fix → re-render
./art final <REEL>                                        # 4K clean master
python3 runtime/scripts/shorts.py <REEL> --drop … --handle "@HumanitariansAI"
python3 runtime/scripts/compile.py <REEL>/short --height 3840
```

GATE P (`PEDAGOGY.md`, signed `VERDICT: PASS`) binds before audio, and `short/` needs its
own. **Nothing publishes from this repo.** Masters go to the Drive by hand; media is
gitignored and never committed.
