# Week 27 work video: angle (proposal)

**Contribution:** [nikbearbrown/mycroft#70](https://github.com/nikbearbrown/mycroft/pull/70), merged 2026-10-17
(merge commit `8665a9f`, CI `verify` passing). `main` gained 43 added and 2 modified files, 0 removed, 0 renamed.
**Status:** PROPOSAL, awaiting Tanmay's pick. No script, no beat sheet yet.

---

## 0. What #70 changed, as the basis for the film

Recipe: `recipes/what-if-simulation-agent.md` (the only existing recipe edited; plus an appended `RUN_LOG.md` entry).

| Change to the existing recipe | What it is |
|---|---|
| Status frontmatter | `status: DRAFT`, `todos_open: 5`, `recipe_version: 0.2.0`, `last_gate: null`, `attestation: null` |
| Steps 1, 3, 5 closed | each keeps the original `[TODO: DEV]` text, dated, with a status line: input, output, how it stops, evidence |
| Two node-to-script mappings | *Parse & Validate Input* → the step-3 script; *Aggregate & Score All Simulations* → the step-5 script |
| Left open on purpose | steps 2, 4, 6; the respond-to-webhook and report-script mappings. The 8 generated stubs and the n8n twin recipe are byte-identical |

What the workflow does (its own six local nodes, in order): parse the request and fill defaults; **Sim 1** reads
growth against sentiment in a 3×3 matrix; **Sim 2** judges the same stock for a conservative, a balanced and an
aggressive investor; **Sim 3** sweeps growth and sentiment to find where the verdict would change; **Aggregate**
weighs the three (0.45, 0.35, 0.20) into one verdict, three scenarios and risk flags; **Build AI Prompt** writes a
461-word briefing. Only then would Groq and PostgreSQL be called, and #70 never calls them.

What #70 adds: a validator with the node's own rules, a Python port of the six nodes checked against the original
JavaScript (23/23 identical, prompt string included), 25 invented requests with a SHA-256 manifest, a self-test
(18 checks, 10 deliberate breaks), two audits.

Committed evidence the film may show: the recipe, the PR, `simulation-results.json`, `validated.json`, the audits,
`parity-results.json`, `self-test-results.md`, the RUN_LOG. Workshop tools (the guard, the fixture builder) stay off screen.

## 1. What this film must not repeat

The two earlier Mycroft contribution films are the nearest neighbours.

- **W25, *Same Logic, Two Languages*:** porting, parity, rounding ties (`0.625`), `||` against Python's `or`, "test data standing exactly on the line" (B07, B08, B12, S06, S07), three pairs that must agree.
- **W26, *Four Mornings*:** hand-offs taken on trust, a price of zero quietly replaced by yesterday's close, the same fact written twice, one workflow calling another by name, a test that could not fail, "the record now says which price was used" (B03), a repeated morning as the frame.

So this film is **not about** porting, parity, rounding, thresholds-and-the-line, a bad or missing value quietly
becoming a plausible one, or a self-test that could not fail. None is a thesis, a beat or a cold open here.

## 2. Narration search

All 43 beat sheets for W15–W26 (topic videos and previews excluded; long cuts and Shorts), 210 unique narration
beats, each idea searched with synonyms and the hits read in context.

| Idea | Hits | Nearest, and the boundary |
|---|---|---|
| A model handed a briefing assembled upstream | **0** as a subject; 6 incidental "prompt" mentions | W17 B04: the Lemonade scaffold uses a deterministic fake adapter because "a real model won't" be. That is about testing, not about what the model is told |
| Several judges combined by weights into one verdict | **0** | W22 B04/B09 (two lists allowed to disagree) and W25 B03/B12 (two versions disagree) are *pairs*, not weighted voices |
| The same subject judged differently depending on who asks | **0** | W18 B08 "same number, different year" is about meaning, not the asker |
| A what-if / sensitivity sweep, "where does it tip" | **0** by the words; the *test* version is W25 | W25 owns "a test on the line". A film about tipping points would land there |
| Defaults filling a request left empty | 14 loose hits | W23 B11 (a question sent as nothing crashed, loudly), W26 B03 (record which fallback was used). Same family as W26; see angle C |
| A value that is not a number | **1** | W24 B08, one clause ("a value that isn't a number… slipped through"), about validating at the door |
| Test coverage of every cell of a decision table | 3 near | W21 (stages that stayed dark), W20 B10 (coverage of guards), W23 B15 (the emptiest row) |

Rejected as too close to earlier films, and why:

- **"Nine cells" (a 3×3 grid lighting up as tests reach it).** My first corpus reached 7 of 9 cells; fixtures c14 and c15 closed it. It is true and teachable, but it is W21's light-and-dark device on W23's matrix idea.
- **"A number that isn't a number" (NaN).** The mechanism is real (`parseFloat("abc")` is NaN, every comparison with NaN is false, so "reject if outside the range" waves it in, and Sim 1 reads it as LOW growth). But the shape is W26's: a bad value quietly becomes a plausible one. The porting catch (Python's `min` against `Math.min`) is W25's. It stays one clause of evidence at most.
- **"Where the answer flips."** W25 territory.

## 3. Recommended angle A, "Minutes of the Meeting"

> **When three checks vote and an AI is handed the result, the minutes are all the AI has.** The model never
> sees the request. It sees 461 words that six local steps wrote from it: three voices, each reading the stock
> its own way, and a chair who weighs them 45, 35 and 20. My contribution lets anyone read those minutes, and
> prove each line matches the original, before any model ever sees them.

**What the viewer leaves with:** when an AI step sits behind a pipeline, ask for the briefing it will be handed,
and ask who had a vote in it and how much.

**Why it fits Mycroft:** P5 says one artifact cannot serve both customers: the run's log for the agent, the
report for the human. The briefing is the third reader nobody planned for, and the recipe already treats it as a
hand-off with `approved_for_live_action: false`.

### Structure: minutes of one meeting about one invented stock (shape taken from the subject)

The workflow is literally three voices, a chair and a record. The film is the meeting. The chair's weights are the
through-line, and **the AI is the one party not in the room.**

| # | Beat | What happens | Committed evidence |
|---|---|---|---|
| M0 | Cold open | The last lines of the briefing: "Your `action_plan.immediate` must strictly match STRONG_SELL." Someone wrote that to hold an AI to a verdict. Who? Let's go to the meeting | `simulation-results.json` (`ai_prompt`, c03) |
| M1 | What this is | Presenter. Mycroft in one line; what I contributed (#70); every company invented | the recipe; PR #70 |
| M2 | The chair opens | A request arrives; the chair fills the empty seats with defaults. A stock is in the room | validator audit (fields the workflow's defaults filled) |
| M3 | First voice | Sim 1: growth against sentiment, nine possible readings | `validated.json`, results |
| M4 | Second voice | Sim 2: the same stock for three temperaments | results |
| M5 | Third voice | Sim 3: not "what is it" but "how close is it to changing its mind" | results (`stability_score`) |
| M6 | **They disagree** | One case where the first voice says STRONG_SELL and the second says ENTER_FULL_POSITION (c11). The chair weighs 45, 35, 20 and writes SELL. Nobody is wrong; the weighting decides | `simulation-results.json` c11 |
| M7 | The minutes | What the AI will be handed, and what it will not be told: it cannot tell a typed number from a defaulted one | the briefing; audit |
| M8 | **The turn: my minute-taker** | I wrote a second minute-taker (the port). Run beside the original on the same meeting, it wrote one line differently, on a number that wasn't a number. Fixed, then identical on all 23. A defect I found in my own build, and proof the comparison could fail | `parity-results.json`; RUN_LOG |
| M9 | Adjourned | Groq and the database are never called; the hand-off says so. Steps 2, 4, 6 stay open. DRAFT, on purpose | recipe frontmatter; hand-off log |
| M10 | Close | One open question: "If an AI is going to summarise your next meeting, have you read the minutes?" | |
| M11 | Outro | | |

About 4–5 minutes, ~750 words.

**Why the structure is new** (against the W15–W26 survey: documents read line by line W24/W23; pairs W25; columns W18/W19; stages walked W17/W22; sabotage W21; a repeated morning W26; a card W20; experiments W17):
- It is a **meeting with a vote**, not a document, pairs, columns or mornings.
- The weights and the absent party give it a shape (voices → weighing → a record for someone not present) that only a weighted-vote pipeline with an AI at the end has.
- It has a mid-film reversal (M6) that is a *result*, not a sabotage.
- No numbered framework; no "your turn" rubric; one open question at the end.

**Honest risk:** the seats follow pipeline order, so a reader could call it "stages walked" (W17/W22). The difference is the frame: voices that disagree, a chair who weighs, a record read by an absentee. If you want it further from stage-walking, M3–M5 can be told as one scene (the three voices answering the same question) instead of three.

**Short (9:16, one arc):** the briefing's last line, the three voices on one stock, the disagreement and the chair's weighing, the question. Name at both ends.

## 4. Alternative B, "Same Stock, Three Chairs"

The film is one invented stock handed to a conservative, a balanced and an aggressive investor, each deciding by
its own limits (growth floor, sentiment floor, P/E ceiling, debt ceiling, position size, stop-loss). Thesis: *a
verdict belongs to the asker's limits as much as to the stock; ask whose limits produced it.* No earlier film has
it (0 hits). It is the cleanest of the three on uniqueness, but it explains the workflow's design more than our
contribution, and it needs **one new committed fixture**: the committed corpus has all three appetites, but never
the same stock through all three. Without it the film would show numbers #70 doesn't contain.

## 5. Alternative C, "Who Answered?"

A request is stripped one field at a time down to nothing, and the verdict barely moves, because the workflow
fills every gap with a default (the empty request lands on HOLD, c06). The audit now lists which fields were
filled. Thesis: *ask how much of an answer came from you.* A strong, visual subtraction structure no film has.
**The risk is the thesis:** it is W26's family, a missing value quietly becoming a plausible one, with the same
remedy (the record says which). I would not choose it over A or B.

## 6. Framing rules (carried from earlier weeks and memory)

1. **No critique of the workflow or anyone's work.** Defaults, the weighting and the NaN behaviour are described as how the workflow works. The only gap called a mistake is **mine** (M8), shown with its fix. The finance is not judged; the simulators are ported faithfully.
2. **My defect is evidence the checking worked**, not a confession; humble first person on the genuine turns only (M6, M8).
3. **Committed files only on screen.** No workshop tools, nothing from this assistant's session.
4. **Every company and number invented**, said once in M1 and labelled on screen wherever a number appears. Not investment advice, said once.
5. **No fellows named or compared.**
6. **Human narration**, first-person curiosity, no lecture register; FACTCHECK claims stay unweakened.

## 7. To confirm before scripting

- The angle (A, B or C).
- For A: whether M6 should use c11 (growth and sentiment both at the bottom, an aggressive investor, ENTER_FULL_POSITION from the second voice), or a cleaner disagreement case.
- For A: whether the line "must strictly match STRONG_SELL" is quoted on screen, as it is the workflow's own text in the briefing.
- For B: permission to add one committed fixture (one stock, three appetites) to the contribution before the film is built.
