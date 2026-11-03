# Week 26 work video — angle (proposal)

**Contribution:** [nikbearbrown/mycroft#64](https://github.com/nikbearbrown/mycroft/pull/64), merged 2026-10-11
(merge commit `5097a8f`). Four `[TODO: DEV]` closures in the Portfolio Visualization Agent: provenance for
`portfolio-price-fetcher` and `portfolio-dashboard`, data-shape validation, and the calculation step, all in
sample mode.
**Status:** APPROVED by Tanmay, 2026-10-10: **angle A, "Four Mornings"**, with the opening and closing dashboard
shown as an **illustration** of our verified sample summary, labelled as such (not the workflow's own HTML node).

---

## 0. What this film must not repeat

Last week's work video, *Same Logic, Two Languages* (W25), was also a Mycroft recipe contribution. Its
thesis: "two versions agreeing only counts where they had a chance to disagree". Its structure: **three
pairs that must agree**. It opened on a JavaScript-vs-Python rounding tie (0.625), and covered the `||` seam,
a parity check and test data "standing on the line".

PR #64 repeats several of those mechanics (a `toFixed` tie, `||`, a parity check). So this film is **not about
porting, parity or rounding**: none of them is a thesis, a beat or a cold open. They appear at most as one
clause of evidence.

## 1. What #64 has that no earlier film does

Narration search across every earlier work video (W15–W25: 35 beat sheets, 375 narration beats):

| Idea, as it exists in #64 | Earlier hits |
|---|---|
| One workflow calling another (the dashboard calls the price fetcher) | **0** |
| A link that holds **by name only** (`YOUR_WORKFLOW_1_ID` placeholder) | **0** |
| The same fact written **twice in one workflow** (the portfolio in Define Portfolio and in Calculate Metrics) | **0** |
| A price of **zero** treated as missing (yesterday's close shown instead) | **0** |
| A test that **passed when it should have failed** (my self-test compared a file the broken run never made) | **0** by phrase; nearest is W25 B07 (a change my comparison didn't notice because no test data stood on the line), a different mechanism. Boundary noted |

Rejected as too close to earlier films: invented or fixture data as a theme (W19, W25); "where I stopped" as
a theme (W19, W25 B10); provenance read line by line (W24 work's receipt).

## 2. Recommended angle: A, "Four Mornings"

> **A dashboard is only as honest as the quiet hand-offs behind it.** The person who opens it sees one
> clean number. Behind it, one workflow trusts another by name; a calculation trusts that a list written
> twice still says the same thing; a missing price quietly becomes yesterday's. My contribution doesn't
> change what the dashboard shows. It puts a check at each hand-off, so when one of them slips, the run
> stops and says why, before anything reaches the person reading it.

**What the viewer leaves with:** when you rely on a dashboard, ask what it is quietly taking on trust, and
where something would *say so* if that trust broke.

**Why it fits Mycroft:** P5 says every run produces a report for the human, and P1 says machines verify
conformance so humans can judge adequacy. A check at the hand-off is the machine half of that.

### Structure: four mornings with the dashboard (shape taken from the subject)

The film's unit is **one morning in the life of the person who reads this portfolio dashboard**. Each act
is the same opening shot (they open the dashboard over coffee), and each morning one thing upstream has
quietly gone wrong. The question every time: *what would they have seen, and what would have said so?*
The answer is shown on the committed files: the step that stops, and its record.

| # | Beat | The morning | What says so now (committed evidence) |
|---|---|---|---|
| M0 | Cold open | The dashboard as its reader sees it: five holdings, one total, a percentage. "Everything on this screen arrives through four hand-offs. Let's spend four mornings with it." | `portfolio-summary.json` (sample) |
| M1 | What this is | Presenter. Mycroft in one line; the two recipes (the dashboard calls the price fetcher); what I contributed (#64, merged); every price in this film invented and labelled | the two recipes; PR #64 |
| M2 | **Morning 1: a price of zero** | The quote service sends 0 for one stock. In this workflow, `regularMarketPrice \|\| previousClose` treats 0 as missing, so the screen shows yesterday's close. Nothing is wrong with the arithmetic; the reader just doesn't know. My port copies this on purpose, and the recipe now says so for the maintainers to decide. Step 3 records which price each holding used | `validated.json` (`price_source: previousClose` for META); recipe *Notes from porting* |
| M3 | **Morning 2: a ticker that isn't in the portfolio** | A response comes back for a symbol the portfolio doesn't hold. The original calculation step would throw. Now step 3 rejects it with a reason, and step 5 refuses to run on rejected data: nothing half-computed reaches the screen | `defective/validated.json`; step 5 refusal (self-test C) |
| M4 | **Morning 3: someone edits one copy of the portfolio** | The portfolio is written in two places in the same workflow. Change the shares in one, and the total silently uses the other. Now step 1 compares the two and stops, naming the difference | provenance record (`portfolio_consistent`); self-test A (NVDA 50 vs 55) |
| M5 | **Morning 4: the dashboard calls the wrong workflow** | The dashboard doesn't contain the prices; it calls the Price Fetcher, and the link holds by its name (its workflow id is a placeholder to set on import). Now the dashboard's step 1 checks the name points where it should, and stops if not | dashboard provenance record; self-test A |
| M6 | **The morning it was my own check** | The turn. I broke my own calculation on purpose to see the checks catch it, and my test said everything passed. It had compared a file the broken run never wrote. A check that can't fail is worse than none, because it looks like one. The test now insists the broken run actually ran, and then it catches the break | self-test D (the fixed check); RUN_LOG |
| M7 | What the reader still sees | The same dashboard as M0. Nothing on it changed; what changed is behind it. Four hand-offs that now speak up, and the ones still on trust: steps 2, 4, 6, live prices. Both recipes stay DRAFT, on purpose | recipe frontmatter (`todos_open` 4, 7); RUN_LOG open issues |
| M8 | Close | One open question: "Pick a number you check every morning. What is it quietly taking on trust?" | — |
| M9 | Outro | — | — |

About 4–5 minutes, ~700 words.

**Why the structure is new** (against the Weeks 15–25 structure audit):
- **Not a document read line by line** (W24 receipt, W23 matrix rows): the unit is a scenario that happens
  to a person.
- **Not pairs that must agree** (W25).
- **Not stages walked in order** (W17, W22).
- **Not deliberate sabotage as the frame** (W21): only M6 breaks something, and it's my own check.
- **No numbered framework and no "your turn" rubric.**
- The repeated morning shot gives each act the same frame and a different failure: a structure only a
  dashboard-for-one-reader subject could have.

**Short (9:16, one complete arc):** one morning only, the zero price. The clean total, then "this number
used yesterday's price for one stock and didn't say so", what now records it, and the question. Name at
both ends.

## 3. Alternative: B, "Taking Its Word For It"

The same four hand-offs, told from inside the pipeline instead of from the reader's chair. The film walks
the call chain once, from the dashboard to the price fetcher to the calculation to the price. At each link
it asks "whose word is this part taking?", and then shows the check that now asks for proof. It ends on my
own test, which took a stale file's word. It's more technical and less human. The risk: walking a chain
link by link sits closer to W24's "read the receipt backwards".

## 4. Framing rules (carried from W25 and memory)

1. **No critique of the original workflow or anyone's work.** The zero-price and two-copies behaviours are
   described neutrally, as how the workflow works and what can happen upstream, and the recipe leaves them
   to the maintainers. The only gap called a mistake is **mine** (M6), shown with its fix.
2. **My gap is evidence the checking worked**, not a confession.
3. **Humble, first person** on the genuine turns only (M2, M6).
4. **Committed files only on screen:** the PR, the recipes, the scripts' records, the self-test results, the
   RUN_LOG. No workshop tools (the guard, the fixture builder) and nothing from this assistant's session.
5. **Every price invented**, said once in M1 and labelled on screen whenever a number appears.
6. **No fellows named or compared**, and no claims about how n8n resolves the placeholder id. The film says
   only what step 1 checks.

## 5. To confirm before scripting

- The angle (A or B).
- M2's wording: "treats 0 as missing" is exactly what the code does. The film doesn't speculate about why a
  quote service might send 0.
- Whether the dashboard image in M0 and M7 is our verified summary laid out as a dashboard (an
  illustration, labelled as such) or the summary file itself. Rendering the workflow's own HTML node would be
  new work outside #64, so it's left out unless you want it.
