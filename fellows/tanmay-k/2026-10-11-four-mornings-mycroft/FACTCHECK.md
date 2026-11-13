# Week 26 work video — FACTCHECK

**Film:** *Four Mornings* (working title) · angle in `ANGLE.md`
**Source of every claim:** `nikbearbrown/mycroft` `main` @ `5097a8f` (the merge of PR #64), read with
`git show`, plus the PR page itself. Committed files only (memory: external reports exclude internal tooling).
**Checked:** 2026-10-10

Verdicts: **SUPPORTED** · **QUALIFY** (true with a stated condition or wording fix) · **INVENTED** (our sample
data, so the film must label it)

| # | Claim | Verdict | Evidence (main @ 5097a8f) |
|---|---|---|---|
| W1 | Mycroft describes itself as a book and a working repository; its pipelines are called recipes | SUPPORTED | `README.md` ("both a book and a working agentic repository"); `recipes/README.md` |
| W2 | Two recipes sit behind the dashboard: the price fetcher (fetches prices, does the math) and the dashboard (calls it, draws the screen) | SUPPORTED | `recipes/portfolio-price-fetcher.md` node table (Fetch Stock Prices, Calculate Metrics, Aggregate Summary); `recipes/portfolio-dashboard.md` node table (Call Portfolio Price Fetcher, Generate HTML Dashboard) |
| W3 | PR #64 added checks to both recipes, rebuilt the math step (Calculate Metrics + Aggregate Summary) to run on test data, and is merged | SUPPORTED | PR #64: merged 2026-10-11, merge commit `5097a8f`; 29 files added, 3 modified; `scripts/tools/portfolio-price-fetcher-run-approved-tools.py` (step 5) |
| W4 | The dashboard numbers: five stocks, total 65,098.13, up 21% | INVENTED (sample) | `data/verified/portfolio-price-fetcher/clean/portfolio-summary.json`: totalCurrentValue "65098.13", totalReturn "21.00". Every price is invented (`_fixture_note` in each fixture). Label on screen whenever it appears |
| W5 | The workflow reads the price as `regularMarketPrice \|\| previousClose`; JavaScript treats 0 as false, so a price of 0 falls back to the previous close | SUPPORTED | The declared workflow's Calculate Metrics node (`…/Portfolio_Visualization_Agent/Portfolio Price Fetcher.json`); recipe *Notes from porting*, bullet 1 |
| W6 | In the sample, META's price came back as 0 and the previous close, 590, was used | INVENTED (sample), SUPPORTED as a record | `sample/clean/META.json` (regularMarketPrice 0, previousClose 590.0); `clean/validated.json` (META `price_source: previousClose`) |
| W7 | The port keeps that behaviour, and the recipe flags it for the maintainers | SUPPORTED | recipe *Notes from porting* ("Whether any of them should change is the maintainers' call") |
| W8 | The record now says, for every stock, which price it used | SUPPORTED | `clean/validated.json`: `price_source` on all 5 records |
| W9 | For a symbol the portfolio doesn't hold, the original calculation finds no shares and stops with an error | SUPPORTED (from the code) | Calculate Metrics: `const myStock = portfolio[ticker]; const shares = myStock.shares;` (undefined → TypeError); `sample/manifest.json` describes it as "the original throws on undefined shares" |
| W10 | Now step 3 sets such a response aside with a reason, and step 5 refuses to run on rejected data | SUPPORTED | `defective/validated.json` (unknown-ticker: "meta.symbol 'ZZZZ' is not in the workflow's portfolio"); self-test C ("refuses a set step 3 rejected: exit 1") |
| W11 | The portfolio is written twice in the same workflow; one copy decides which prices to fetch, the other does the math | SUPPORTED (from the code) | Define Portfolio node (the list feeds Fetch Stock Prices); Calculate Metrics node (its own object of shares and buyPrice); recipe *Notes from porting*, bullet 3 |
| W12 | Editing the shares in the first copy leaves the math using the second, and nothing says so | QUALIFY | True from the code: Calculate Metrics reads shares only from its own copy. Say "the math keeps using the other copy"; do not claim what any person did or would do |
| W13 | Step 1 reads both copies and stops if they disagree, naming the difference | SUPPORTED | provenance record (`portfolio_consistent: true`); self-test A ("the two portfolio definitions disagree (NVDA shares 50 vs 55): exit 1") |
| W14 | The dashboard holds no prices; it calls the price workflow and finds it by name; the id is a placeholder | SUPPORTED | Dashboard workflow's Call Portfolio Price Fetcher node (`cachedResultName: "Portfolio Price Fetcher"`, `value: "YOUR_WORKFLOW_1_ID"`); `logs/portfolio-dashboard-provenance-2026-10-10.json` finding |
| W15 | The dashboard's step 1 checks the name is the price workflow's real name, and stops if not | SUPPORTED | dashboard provenance (`calls_price_fetcher: true`); self-test A ("dashboard calls a different workflow by name: exit 1") |
| W16 | I broke my own calculation on purpose; the test meant to catch it passed, because the broken version never ran and the test compared a file left from the good run | SUPPORTED | `scripts/tools/portfolio-price-fetcher-self-test.py`, section D comment: "a first version of this check passed against the good summary left in a copied folder, because the broken run had failed" |
| W17 | Now the test grades nothing unless the broken version actually ran, and then it catches the break, a single cent | SUPPORTED | self-test D row: "broken port ran: True; summary.totalGainLoss: original '11298.13', port '11298.12'" |
| W18 | Both recipes are still drafts; still open: live prices, three more steps in one recipe, five in the other | SUPPORTED | frontmatter `status: DRAFT`, `todos_open` 4 and 7; open steps: price fetcher 2, 4, 6; dashboard 2–6 (`RUN_LOG.md` 2026-10-10 open issues) |
| W19 | Nothing on the dashboard changed; the checks sit behind it | SUPPORTED | PR #64 adds checks and records; the dashboard's own nodes are untouched (`portfolio-dashboard-webhook.py` and `-call-portfolio-price-fetcher.py` byte-identical) |
| W20 | In the sample, GOOGL's quote had no current price (null), so it also got the previous close, 166: two of the five prices on the dashboard are the previous close | INVENTED (sample), SUPPORTED as a record | `sample/clean/GOOGL.json` (regularMarketPrice null, previousClose 166.0); `clean/validated.json` (GOOGL and META `price_source: previousClose`; AMD, MSFT, NVDA `regularMarketPrice`); recipe *Notes from porting* bullet 1 ("as does a missing or null one") |
| W21 | The record is written by a check that runs before any math: step 3 (validate data shape) writes `price_source`, and step 5 (the calculation) reads step 3's promoted records | SUPPORTED | `recipes/portfolio-price-fetcher.md` step 3 ("the effective price, regularMarketPrice \|\| previousClose… Output: … promoted records") and step 5 ("reads step 3's promoted records") |
| W22 | "Previous close" is the price at the end of the last trading day | QUALIFY (general meaning of the field) | `previousClose` is the quote's own field name, read by Calculate Metrics. Its meaning (the prior session's closing price) is the standard one, not defined in any committed file. Say "the last trading day", never "yesterday" (a Monday's previous close is Friday's) |

## Not claimed (and why)

| Item | Why it stays out |
|---|---|
| Why a quote service might send 0 (a trading halt, etc.) | Not in any committed file. The film says only what the code does with a 0 |
| How n8n resolves a placeholder workflow id | Not verified. The film says only what step 1 checks |
| Rounding, parity, porting as themes | W25's subject (ANGLE §0). The cent in W17 is the only trace, as evidence of the fixed test |
| The guard, the fixture builder, the session's merge permission | Workshop tooling, not committed (memory: external reports exclude internal tooling) |
