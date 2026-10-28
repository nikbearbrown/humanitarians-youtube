# SCRIPT — "Myelin: Teaching Agents Habits"

Skill: ai-explainer · Channel: claude-hai (@HumanitariansAI, kicker "Irreducibly Human") · Voice: Kokoro `af_bella`
Formats: 16:9 + native 9:16 (built together) · Target ~2:00 (draft v3 ≈ 2:00–2:05; verified after audio, trimmed if over)
Status: **DRAFT v3 — awaiting narration approval (GATE P). No audio generated.**
Source: `Downloads\myelin` (README, docs/DESIGN_SPECIFICATION.md, insights/EMPIRICAL_FINDINGS.md, data/historical_trajectories).
Framing: generic (any AI agent), and explicit that Myelin is an **initial plan**: nothing is built or measured yet beyond the trace counts.
No dates or times on screen. No speed or cost figure is shown as a result.

---

## B00 — Opening (ClaudeComposerAsk) · ~10 s
**Show:** composer, `Hi, Nidhi`. Ask: *"Why does my AI agent ask the model the same thing over and over?"* Results: `find the habits` · `compile them` · `say "unsure"`.
> Hi, I'm Nidhi. This video walks through the initial plan for Myelin, an idea for making AI agents stop re-asking the model routine questions. The voice is Bella, an AI narrator.

## B01 — Overview (BrutalistHesitantWriter) · ~8 s
**Show:** writer types *"Ask the model every time."* — strikes "every time", types "only when unsure".
> The idea: routine decisions run as plain code, and the model is asked only when that code is unsure. That saves the model for the questions that really need it.

## B02 — Agents repeat themselves · ~12 s
**Show:** horizontal bars drawn from the trace counts: *look up a booking 1,419* · *look up an order 1,029* · *search flights 538* · *look up a user 486*; source line *public customer-service agent traces (tau-bench)*.
> Agents repeat themselves. In public traces of customer-service agents, the same few calls show up again and again: one booking lookup alone appears over fourteen hundred times.

## B03 — A habit, up close · ~11 s
**Show:** a customer card with six booking codes; six separate "model turn" steps light up one per code; beside it, a 3-line loop. Small note: *common pattern in the traces*.
> Here's what a habit looks like. A customer has six bookings, and the agent spends six separate model turns, one per booking. A three-line loop could walk that list.

## B04 — Patterns, not puzzles · ~8 s
**Show:** three generic inputs → their patterns: *ID* → `name_name_1234` · *code* → `AB12CD` · *date* → `YYYY-MM-DD`; label *a pattern, not a puzzle*.
> Many inputs follow fixed patterns too: IDs, codes, dates. That's a pattern, not a puzzle.

## B05 — Why "Myelin" · ~9 s
**Show:** a drawn nerve fibre; the busiest pathway gets wrapped in sheath segments and its pulse runs faster than an unwrapped neighbour.
> In biology, myelin wraps the brain's busiest nerve pathways so their signals travel faster. The plan does the same for an agent's habits.

## B06 — The planned pipeline · ~13 s
**Show:** five stations: *mine logs* → *group repeats (≥ 50)* → *write Python* → *sandbox test* → *registry*; a "no network · no model" badge on the sandbox; header *planned*.
> The plan: mine an agent's past logs, keep decisions that repeat at least fifty times, have a strong model write a small Python function for each, and test it in a sandbox with no network and no model.

## B07 — The abstention rule · ~13 s
**Show:** `return "unsure"` → arrow back to the model; then the planned gate, typeset per MATH-TYPESETTING.md: agreement = correct ÷ (total − unsure) ≥ 0.98, on *later sessions*.
> Each function follows one rule: when it isn't sure, it says so, and the model takes over. Where it does answer, it must agree with the model at least ninety-eight percent of the time, on later sessions it never saw.

## B08 — A fair test · ~11 s
**Show:** a timeline split *oldest 70% → build* | *newest 30% → test*; three baseline chips on the test side: *semantic cache* (sub-label *reuses the answer to the most similar past input*) · *small classifier* · *small local model*.
> It would be tested against simpler options: a semantic cache, which reuses the answer to the most similar past input, a small classifier, and a small local model.

## B09 — What the plan delivers · ~13 s
**Show:** header *initial plan*; two planned deliverables drawn as objects: a package box *habit compiler* and a dashboard sketch *map of compiled habits*; below, *measured so far: call counts* ✓ · *not yet: speed, cost, savings*.
> The plan delivers two things: a habit compiler, a Python package that runs this pipeline, and a dashboard that maps which habits have been compiled. So far, only the call counts are measured. Any savings are still targets.

## B10 — Your Turn (ClaudeComposerAsk) · ~12 s
**Show:** composer, title *Try it on your own agent*. Prompt (read verbatim): *"Here's a log from my AI agent. List the decisions it repeats most, and for each, say whether a simple rule could handle it, or when it should answer unsure."*
> Your turn. Paste this into Claude with a log from your own agent: here's a log from my AI agent. List the decisions it repeats most, and for each, say whether a simple rule could handle it, or when it should answer unsure.

## B11 — Outro (Manim, HAI) · ~5 s
**Show:** *Myelin* / *Teaching Agents Habits* · *an initial plan*, HUMANITARIANS AI wordmark, @HumanitariansAI.
> Myelin: compile the habits, and keep the model for the hard parts.

---

## FACTCHECK notes (verified by re-counting the raw trace files)

| Claim | Source | Verdict |
|---|---|---|
| booking lookups 1,419 (airline, 377 GPT-4o + 1,042 Sonnet, 600 conversations) | tool_calls counted per file | ✅ |
| order lookups 1,029 (retail, GPT-4o, 460 conversations) | same | ✅ |
| flight searches 538 (141 + 397) · user lookups 486 (120 + 366) | same | ✅ |
| six bookings → six model turns | airline task 2: 9 of 12 runs made exactly 6 lookups (the docs' "Episode 2" run made 3) | ✅ as a common pattern; ⚠️ docs' citation wrong |
| Sonnet retail "460 episodes / 3,410 calls" (docs) | file has 920 / 7,086 | ⚠️ docs wrong — not used on screen |
| 15,000 tokens · 9 s · 0.002 ms · 15,000× · 60–80% · 0.0% hallucination | no token or timing fields in the traces | ❌ not shown; B09 says savings are targets |
| ≥ 50 repeats · 70/30 time split · ≥ 98% gate · three baselines · habit-compiler package · dashboard | DESIGN_SPECIFICATION.md §1, §3, §5, §6, §7 | ✅ as plan, not results |
| B04 example patterns | generic illustrations (ID/code shapes from EMPIRICAL_FINDINGS §4B; date format generic) | ✅ illustrative |
| myelin speeds nerve signals | standard neurobiology | ✅ (no figure quoted) |
