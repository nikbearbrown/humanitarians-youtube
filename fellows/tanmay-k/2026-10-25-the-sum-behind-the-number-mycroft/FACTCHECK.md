# FACTCHECK: The Sum Behind the Number (long film and Short)

Verdicts: SUPPORTED (a committed file or the vendored README says it, and I re-ran it), NOTE (a framing choice).
Every number below was re-derived from the committed files on 2026-10-25; the branch is merged as `5d60312`.

| # | Claim in the film | Verdict | Where it comes from |
|---|---|---|---|
| W1 | c01: a Tech Sector Crash on NVDA 40% / AMD 30% / TSM 30% (initial 10,000) ends at 2,200, a drawdown of −78.0%, risk level CRITICAL | SUPPORTED | `data/verified/scenariostresstestingagent/clean/stress-results.json` (c01) |
| W2 | Mycroft is "both a book and a working agentic repository" | SUPPORTED | the repo README (quoted on screen) |
| W3 | The Scenario Stress Testing Agent recipe shocks a portfolio with a named scenario and reports what is left | SUPPORTED | `recipes/scenariostresstestingagent.md` (Purpose; the workflow's steps) |
| W4 | PR #74 merged (`5d60312`, 2026-10-26 01:34 UTC) | SUPPORTED | `gh pr view 74` (state MERGED, merge commit) |
| W5 | Tech Sector Crash names five shocks: market −0.15, tech_sector −0.30, semiconductor −0.35, ai_stocks −0.40, volatility_spike 2.5 | SUPPORTED | the workflow's `Load_Template_Scenario` node (read by the parity check from the workflow JSON) |
| W6 | The engine adds, for each holding, the shocks that belong to it | SUPPORTED | the workflow's `Stress_Test_Engine` node; the README's "Current (Additive)" |
| W7 | The first holding (NVDA): market −15, semiconductor −35 (its sector), AI stocks −40 (on the list) = −90; loss −3,600 | SUPPORTED | c01 `all_positions` (shock_pct −90.0, loss −3,600.0); the sector map and `ai_stocks` list in the engine |
| W8 | The workflow's README prints this exact sum as its worked example (market −15%, semiconductor −35%, AI stocks −40%, total −90%) | SUPPORTED | `docs/mycroft-main/n8n_Workflows/Scenario_Stress_Testing_Agent/README.md` ("For NVDA in Tech Crash scenario") |
| W9 | The third holding (TSM) is a semiconductor stock not on the AI list: −15 −35 = −50; the second (AMD) takes −90 | SUPPORTED | c01 `all_positions` (−90, −90, −50) |
| W10 | 0.40 × 90 + 0.30 × 90 + 0.30 × 50 = 36 + 27 + 15 = 78 | SUPPORTED | arithmetic on W9; matches c01 `drawdown_pct` −78.0 |
| W11 | Aggressive Rate Hike: market −10, growth stocks −20, technology sector −15 (plus a volatility number) | SUPPORTED | the workflow's `Load_Template_Scenario` node |
| W12 | c12: four growth names at 25% each; three take −30, the one filed under the technology sector takes −45; the book loses 33.75%, risk level CRITICAL (above 30%) | SUPPORTED | c12 `all_positions` (−45, −30, −30, −30), `drawdown_pct` −33.75; the engine's thresholds (30 / 20 / 10) |
| W13 | The port is checked against the original code, extracted from the workflow JSON at run time; 24 of 24 requests identical (every number, label and message), 0 mismatching | SUPPORTED | `logs/scenariostresstestingagent/parity-results.json` (requests 24, matching 24, mismatching 0) |
| W14 | The self-test records 27 checks, 12 deliberate breaks, each caught | SUPPORTED | `logs/scenariostresstestingagent/self-test-results.md` |
| W15 | The port is a Python copy of the engine and its first steps (Validate Portfolio, Load_Template_Scenario, Save_Portfolio_Before_LLM, Stress_Test_Engine) | SUPPORTED | the step-5 script; the recipe's step-5 status line |
| W16 | Weights totalling 0.6 or 1.2 are accepted (c06, c08); the workflow rescales weights to one when the total is more than 0.01 from it | SUPPORTED | `validate-audit.md` (c06, c08 accepted); the `Validate Portfolio` node |
| W17 | Ten of ten deliberately flawed portfolios are rejected, each with its own reason | SUPPORTED | the defective-set audit (10 in, 10 rejected) |
| W18 | The model call, the market-data request and the reply to a caller are recorded as hand-offs with `approved_for_live_action: false`; nothing live is called | SUPPORTED | the step-5 run log (`live_handoffs`) |
| W19 | Five items are open (`todos_open: 5`); the recipe is `DRAFT` | SUPPORTED | the recipe frontmatter |

## Names and wording

- **Invented:** every portfolio is mine. The tickers (NVDA, AMD, TSM, TSLA, META) are the workflow's own sector map; the
  film makes no claim about any real company and says once that the numbers are scenario arithmetic, not predictions.
- **NOTE (framing):** the "−90%" is the workflow's documented worked example, credited to its README. The film does not
  present it as a surprise about the workflow.
