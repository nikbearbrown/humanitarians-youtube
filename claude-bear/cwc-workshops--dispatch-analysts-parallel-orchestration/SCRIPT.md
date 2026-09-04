# Fan Out: Coordinating Dozens of Agents in Parallel Without Blocking — Narration Script (Plain register)

*Skill: `hai-simple`, mode `redo`. Register: **Plain**. 12 beats ≈ 2:40.*
*Carry-out written first (CARRY-OUT.md). Every beat lands it.*

**Cold open:** `BrutalistHesitantWriter` (hai-simple WRITER LAW — no puppet,
no human step). **Narrator:** Liam, Kokoro `am_onyx`.

| Beat | Move | Narration | Visual |
|---|---|---|---|
| **B00** | writer cold open | "You might picture fifty separate chats, each with an analyst, running together. That's not it — one call, and the server spawns fifty sessions for you. So how does one agent coordinate dozens without blocking?" | Writer types "How do I run / fifty analysts / in fifty separate / conversations at once?" — hesitates on "conversations", corrects to "sessions" |
| B01 | 1 stakes + question | The question: how does a single agent coordinate long-running parallel sub-agents — without opening multiple separate conversations, or blocking the whole flow? | `CwcOrchestrationQuestion` |
| B02 | **2 wrong guess** | The natural guess: to get three analysts working at once, you open three separate Claude conversations yourself, and copy the results between them by hand. | NEW GRAPHIC — three chat windows, copy-paste arrows between them |
| B03 | **2 break it / 3 mechanism** | A custom tool becomes the orchestration trigger. When the head agent calls dispatch analysts with a list of tickers, the server intercepts that call. It doesn't run the analysis itself — it spawns three independent analyst sessions, each with its own full context window, each running in parallel. The head agent pauses. The server monitors the sessions. When all three finish, the server resumes the head with the accumulated results. Fan out, fan in. | `CwcFanOutConcept` |
| B04 | **4 anchor planted** | Here is the flow. Head of research receives the prompt: sweep NVDA, AMD, and MU, rank by margin durability. It calls dispatch analysts with the three tickers. The server intercepts. Three analyst sessions spawn simultaneously. Each reads twenty pages of SEC filings independently, scores on a rubric, returns a grade. The head waits — it doesn't block your terminal, it doesn't lock the conversation. The server monitors all three in the background. When all three finish: NVDA scores nine, AMD scores six, MU scores four. The head resumes, reads the accumulated table, synthesizes a ranked report. One conversation. Three parallel analysts. One merged report. | `CwcFanOutFlow` — THE ANCHOR |
| B05 | 3 mechanism | The spread is the mechanism. One call fans out into N parallel sessions. Each session is fully isolated — its own context, its own tools, its own errors. They converge when they finish, not when the head decides to check. The server is the coordinator, not the agent. | `CwcSpreadMechanism` |
| B06 | **4 anchor payoff** | The timing difference is not incremental — it is categorical. Serial execution: fifty analysts, each taking thirty seconds, one after another. That is twenty-five minutes. Parallel fan-out: fifty analysts dispatched simultaneously — all fifty finish in the time the slowest one takes, about thirty seconds. Serial is a queue. Parallel is a wave. | `CwcFanOutSpeedGain` — pays off B00's "fifty analysts" |
| B07 | 3 mechanism | When the analysts finish, their results don't merge themselves. Each session returns its result as a chip: ticker, score, findings. The chips arrive at different times. The aggregator holds them until the last one lands, then runs three operations: deduplicate, rank by score, merge into one structured report. It is not smart — it is a collector that waits for the full set before it hands anything back. | `CwcResultAggregation` |
| B08 | **5 both directions** | Both sides follow a fixed contract: the head sends a task ID, ticker, and query focus; the analyst returns a task ID, findings, confidence, and sources. The aggregator checks every result against that shape. An off-schema result gets rejected on its own — one broken session doesn't corrupt the others. Skip the contract, and one bad session can corrupt the merged report silently instead. | `CwcOrchestrationContract` |
| **BCRY** | **6 carry-out** | Fanning out isn't opening more chats. It's one call that spawns isolated sessions the server waits on, and merges for you. | `WantQuote` — the sentence, alone |
| BHTF | handoff | Your turn. Paste this into Claude: fan this workload out across parallel sub-agents, then merge their results into one ranked decision. Watch what happens if one sub-task fails, and whether the merge waits for the slowest session before it hands back an answer. | `ClaudeComposerAsk`, "Your turn." |
| BOUT | outro | Fan Out: Coordinating Dozens of Agents in Parallel Without Blocking. Liam, in for Bear. | `OutroCTA`, @HumanitariansAI |

## Register audit (Plain)

| Check | Where |
|---|---|
| Stakes before mechanism | B00–B01; mechanism waits until B03 |
| Wrong guess surfaced *and falsified by a case* | B02 states the "open separate chats, copy-paste by hand" read; B03 breaks it — one tool call, server-spawned sessions, no manual chats |
| Exactly one inference flag | None — direct, confirmed mechanism description throughout (this is how the fan-out tool pattern works, not an inference about Claude); `one_flag: "N/A"` in metadata |
| One anchor, planted early, paid off late | B04 (NVDA/AMD/MU flow, fifty-analyst framing echoed from B00) → B06 (the fifty-analyst timing collapse) |
| Both failure directions | B08: with the schema contract, one bad session is rejected cleanly (positive) vs. without it, one bad session can corrupt the merged report silently (negative) |
| No design judgment | B08 rewritten from the source's "not clever engineering… not overhead… the entire reason it works" framing to a plain statement of what the contract does and what happens without it — no verdict on whether the design is *good* |

## Deliberately not claimed

- **Not "parallel is always thirty seconds."** The reel's timing claim is
  specific: the wall-clock collapses to roughly the duration of the
  slowest single analyst, not a fixed number — thirty seconds is the
  source's worked example, not a universal constant.
- **Not a verdict on whether this orchestration pattern is well-engineered.**
  The source (Teardown register) framed the schema contract as "the entire
  reason fan-out works at scale" and dismissed it as "not overhead" — design
  judgment. Plain register keeps the same facts (fixed schema in, fixed
  schema out, off-schema rejected) without ruling on whether that is a
  particularly clever or necessary design choice.
- **No claim that every parallel-agent setup uses this exact tool-call
  intercept mechanism.** The reel describes the source's specific
  fan-out/fan-in pattern (custom tool → server intercept → spawned
  sessions → aggregator), not a claim that this is the only way to
  parallelize agents.

## Handoff prompt (BHTF, read aloud)

> "Fan this workload out across parallel sub-agents, then merge their
> results into one ranked decision."

Why it's worth running: it doesn't require the SEC-filing analyst setup
from the video — any workload with independent sub-tasks (research
questions, files to summarize, options to compare) can be fanned out the
same way. Watching what happens when one sub-task fails or finishes late is
the source's own handoff idea, generalized so today's viewer can try it on
their own workload.

## Beat-count note (redo)

Source (`dispatch-analysts-parallel-orchestration`, Teardown) ran 11
main-line beats (B00 puppet-style `ClaudeComposerAsk` ask, B01 the-question,
B02 core-idea, B03 visual-centerpiece, B04 spread-move, B05 fan-out-speed,
B06 result-aggregation, B07 orchestration-contract, B08 verdict recap, B09
your-turn, B10 outro) plus three duplicate `lane: BOOKEND` beats (BVDT/BHTF/
BOUT) used for the source's own short-form cut. This redo runs 12: B00
(writer) absorbs the same stakes-setting job as the source's B00 host ask;
B01 keeps the source's the-question beat verbatim; B02 is new — the
wrong-guess beat Plain register requires and the Teardown source skips
straight past (it goes directly from question to mechanism); B03–B08 keep
the source's B02–B07 mechanism/anchor/aggregation/contract beats, narration
re-registered Teardown → Plain (softened judgment language in B08, described
below); the source's B08 verdict-recap beat is dropped — its content is
compressed into the carry-out (BCRY) instead of restated as a separate
recap; BHTF and BOUT replace the source's B09/B10 with the humanitarians
skin. No facts added or dropped — the tool-intercept mechanism, the
NVDA/AMD/MU worked example, the timing collapse, the aggregator's three
operations, and the schema contract all carry over unchanged.
