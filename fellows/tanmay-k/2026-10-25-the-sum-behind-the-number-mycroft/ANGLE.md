# Week 28 work video: angle (proposal)

**Contribution:** [nikbearbrown/mycroft#74](https://github.com/nikbearbrown/mycroft/pull/74), merged 2026-10-26 01:34 UTC
(merge commit `5d60312`). `main` gained 40 added and 2 modified files, 0 removed, 0 renamed.
**Status:** **APPROVED by Tanmay, 2026-10-25: angle A, "The Sum Behind the Number".** Standing instruction with the approval:
*show nothing negatively; where an instance could read that way, reframe it positively.* See §8 for how that was applied.

---

## 0. What #74 changed, as the basis for the film

Recipe: `recipes/scenariostresstestingagent.md` (the only existing recipe edited, plus an appended `RUN_LOG.md` entry).

| | Before (upstream `main` @ `5f39a10`) | After (#74, merge `5d60312`) |
|---|---|---|
| Recipe lifecycle | no status frontmatter | `status: DRAFT`, `todos_open: 5`, `recipe_version: 0.2.0` |
| Steps 1, 3, 5 | `[TODO: DEV]` | built and exercised, each with a status line (input, output, how it stops, evidence); the original TODO text kept, dated |
| Node mappings | the engine and the portfolio check had no mapped script | *Validate Portfolio* → the step-3 script; *Stress_Test_Engine* and *Save_Portfolio_Before_LLM* "also covered" by the step-5 port |
| Left open on purpose | | steps 2, 4, 6, and the report mappings. The 8 generated stubs and the n8n twin are untouched |

What the workflow does: it takes a portfolio and a scenario name. **Validate Portfolio** rescales weights to 1.0 when
they are off by more than 0.01. **Load_Template_Scenario** picks one of five scenarios (Tech Sector Crash, Aggressive
Rate Hike, AI Regulation, Semiconductor Supply Shock, Black Swan), each a list of named shocks. **Stress_Test_Engine**
gives every holding the **sum** of the shocks that match it: the market shock, its sector's shock, an AI-stocks shock,
a growth-stocks shock. It then sorts by loss, names the top three losers, and sets a risk level from the drawdown
(CRITICAL above 30%, HIGH above 20%, MODERATE above 10%). A custom scenario would go to Groq first; #74 never calls it.

What #74 adds: a validator with the node's own rules, a Python port of four code nodes checked against the original
code run from the workflow JSON (24/24 identical), 22 invented portfolios (12 clean, 10 defective) with a SHA-256
manifest, a self-test (27 checks, 12 deliberate breaks), and the recipe's status lines.

Committed evidence the film may show: the recipe, the PR, `stress-results.json`, `validated.json`, the audit, the
`parity-results.json`, `self-test-results.md`, the `RUN_LOG` entry, and the workflow's own README (a vendored file).
Workshop tools (the guard, the fixture builder) stay off screen.

**Deliberate-boundary check (read before forming the angle).** The workflow's own README says the engine applies
**compound** shocks ("market + sector + category"), shows NVDA at **−90%** in the Tech Crash as its worked example,
calls the rule "Current (Additive)" and says "can exceed 100%", and tells the reader how to change the sector map and
the combining rule. So the stacking is **documented design, not a defect**. The README's six documented shock
categories are exactly the six the engine reads. The film describes the engine as it is documented and never as wrong.

## 1. What this film must not repeat

The three earlier Mycroft contribution films are the nearest neighbours.

- **W25, *Same Logic, Two Languages*:** porting, parity, rounding ties, thresholds with "test data standing on the line". So no film about parity, rounding, or the 10-percent boundary (c11).
- **W26, *Four Mornings*:** hand-offs taken on trust; a missing value quietly becoming a plausible one; the same fact written twice. So no film about the sector-map default (an unmapped ticker is treated as `tech_sector`) or the rescaled weights (c06, c08).
- **W27, *Minutes of the Meeting*:** three voices weighed into one verdict (0.45, 0.35, 0.20), and the briefing an AI is handed. So no film about weights-into-a-verdict, an AI's briefing, or the Groq / database hand-offs.
- **W24's receipt, W21's lights, W20's card, W23's matrix:** earlier devices. Not reused.

So this film is **not about** porting or parity as a thesis, rounding, thresholds, quiet defaults, hand-offs or approvals,
weighted votes, or the model's briefing. Parity appears as one piece of evidence, never as the point.

## 2. Narration search

Every narration file for W17–W27 work videos (70 read-aloud and script files, long cuts and Shorts; topic videos
excluded), each idea searched with synonyms and the hits read in context.

| Idea | Hits | Nearest, and the boundary |
|---|---|---|
| A number made of named parts that **add** ("adds up", "stack", "compound", "sum of") | **0** as a subject; "stack" appears only as layout (W19–W23, W27) | W27's weights combine three *votes* into a verdict; ours adds *shocks* per holding. The boundary: W27 is about who had a vote; this is about what was added |
| "Worst case", "ranking", "drawdown", "shock", "black swan", "tail" | **0** | none |
| "Stress" | 2 | W27 "the stress tests" = Sim 3's sensitivity checks; W23 "an explicit stress-test" of the addition. Neither is a stress-test engine |
| A scenario, named, with a story | 2 | W17 (an "illustrative scenario" label), W22 (inventing a scenario Capital One never described). Neither is a financial scenario |
| A list that decides what you are hit by (a lookup table) | **0** | W26's quiet default is a missing value, not a list's membership |
| A percentage taken apart term by term | **0** | W18 "same number, different year" is about meaning |

Rejected as too close to earlier films, and why:

- **"The scenario that needs a model" (c10, the custom scenario stops at Groq).** W25–W27 already own hand-offs and approvals.

## 3. Recommended angle A, "The Sum Behind the Number"

> **A stress-test percentage is a sum, and a sum can be taken apart.** "Tech crash: minus seventy-eight percent"
> sounds like one fact about the market. It is the market shock plus a sector shock plus an AI shock, added for each
> holding. My contribution lets you take any such number apart, run the original engine and my port side by side on
> every case, and see that each term is the one the workflow documents, before anyone acts on the total.

**What the viewer leaves with:** when you read a stress-test result, ask which shocks were added, from which lists,
and whether the engine that added them has ever been run beside the original.

**Why it fits Mycroft:** P1 says machines verify conformance so humans can judge adequacy. The breakdown is what
lets a human judge adequacy of a number; the port, the parity check and the validator are the machine half.

### Structure: one number, taken apart (shape taken from the subject)

The film's unit is **a block of loss that grows one term at a time**. Each beat adds one named shock to one holding's
bar and reads the running total, until the number the workflow reports has been rebuilt from its parts. The through-line
is the stack of blocks on screen; nothing is shown as a pair of columns, a matrix, a meeting or a morning.

| # | Beat | What happens | Committed evidence |
|---|---|---|---|
| S0 | Cold open | "Tech Sector Crash: −78%." One invented portfolio of three chip stocks. Where does seventy-eight come from? | `stress-results.json` c01 |
| S1 | What this is | Presenter. Mycroft in one line; what I contributed (#74); every ticker and number invented; not investment advice | the recipe; PR #74 |
| S2 | One holding, one block at a time | NVDA in c01: the market shock (−15), then its sector (−35), then the AI list (−40). The bar grows to −90 | c01 `all_positions`; the workflow's README worked example |
| S3 | The same crash, a different holding | TSM in c01 is hit by market and sector but is not on the AI list: −50. The portfolio's −78 is a weighted sum of −90, −90 and −50 | c01 |
| S4 | A tame scenario, a hard number | An ordinary rate hike on four growth names (c12): TSLA is on three lists and takes −45, the others −30; the book loses 33.75% and reads CRITICAL | c12 |
| S5 | **The turn: does my version add the same way?** | I wrote a second adder (the port). Run beside the original code taken from the workflow JSON, on the same twenty-four cases, every field matches. The shim and the one JavaScript node are shown running | `parity-results.json` |
| S6 | What stops before the adding starts | Weights that don't sum to one are rescaled; all-zero weights and a missing ticker stop the run; the validator says which and why. A sum of nothing is not a number | `validate-audit.md`, defective set |
| S8 | Close | "Next time a stress test says one number, ask what was added." | |
| S9 | Outro | | |

About 4–5 minutes, about 750 words.

**Why the structure is new** (against the W17–W27 survey: ledger W18, labels W19, a card run twice W20, lit and dark
stages W21, five-stage interrogation W22, a matrix W23, a document read line by line W24, pairs W25, mornings W26, a
meeting W27): it is a **running total**, a block that grows one term at a time, with the number rebuilt on screen
rather than explained after the fact. Its mid-film turn (S5) is a *check on my own adder*, not a sabotage.

**Honest risks:**
- **W27's neighbour.** Both films are about how parts combine into a result. The difference is the parts (named shocks added per holding, not votes weighed by a chair) and the question (what was added, not who had a vote). If you want it further away, S5 can come out and the film can end on S6.
- **It describes a documented design.** The workflow's README already shows the −90. The film does not present stacking as a discovery about the workflow. Its claim is about the *reader*: most people do not ask what was added. If that feels thin, the alternative below is stronger on novelty and weaker on safety.

**Short (9:16, one arc):** the number on screen, a block that builds NVDA's −90 term by term, the book's −78, and the question. Name at both ends.

## 4. Alternative B, "Same Crash, Different Holdings"

The film is one scenario applied to three invented holdings: the same Tech Crash gives NVDA −90, TSM −50 and a name off
the map −15. Thesis: *a scenario's size is set by whose list you are on; ask which lists your holdings are on.* It is a
reader to hold the lookup table in mind. I would choose A over B; B is a good Short.


## 6. Framing rules (carried from earlier weeks and memory)

2. **Any defect I found in my own build is evidence the checking worked**, not a confession; humble first person on the genuine turns only (S5).
3. **Committed files only on screen.** No workshop tools, nothing from this assistant's session. The workflow's README is a vendored file in the repo and may be shown.
4. **Every ticker and number invented**, said once in S1 and labelled on screen wherever a number appears. Not investment advice, said once.
5. **No fellows named or compared**, and no author named for the workflow.
6. **Human narration**, first-person curiosity, no lecture register; FACTCHECK claims stay unweakened.

## 7. To confirm before scripting

- The angle (A, B or C).
- For A: whether S4 uses c12 (TSLA on three lists) or a cleaner stacking case; and whether S5 stays in or the film ends on S6.
- Whether the README's own −90 worked example may be shown on screen as the workflow's own text (it is a vendored file in the repo).

