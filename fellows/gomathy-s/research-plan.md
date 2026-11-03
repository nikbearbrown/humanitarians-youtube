# Insider-Trading Signal Agent (Mycroft)

Research plan for the requested period, 2 Nov 2026 – 22 Jan 2027. The work lives in the
Mycroft repository as a new module, `insider-signals/`, modeled on `congressional-signals/`.

## Research question

Do open-market purchases by company insiders, especially clusters of insiders buying
together, show signal after adjusting for the market, and how often should they be skipped?

## Why it matters

Most insider trades are routine and carry no signal. They are stock grants, option
exercises and shares withheld for tax. The value of the project is filtering honestly: keep
only real open-market purchases, adjust for the market, and say plainly how much of what
looks like "insider buying" is noise.

## Data source

- **SEC EDGAR Form 4**, the filing insiders use to report changes in their holdings.
- **Recommended for the first version: SEC's Insider Transactions Data Sets.** These are
  quarterly bulk files that SEC extracts from Forms 3, 4 and 5, covering January 2006 to the
  latest quarter (2026 Q3 today). A study needs about a dozen downloads instead of thousands
  of per-filing requests. The data is already in tables with SEC-defined keys, and each
  quarterly file can be hashed for provenance. SEC says the data sets are "not a substitute"
  for the filings, so a random sample is checked against the individual Form 4 filings, and
  every reported signal links to its filings. Individual filings become the main source in
  a later version if the project moves to monitoring.
- **SEC access rules:** every request carries a User-Agent with a name and contact email,
  and the request rate stays under SEC's limit of 10 requests per second. The pipeline uses
  1 per second and refuses to run without the User-Agent.
- **Prices:** daily adjusted closes for each stock and for SPY via Yahoo Finance (`yfinance`).

## Pipeline

- **INGEST:** download SEC's quarterly insider data sets with a User-Agent and the rate
  limit, recording a hash for each file.
- **PARSE:** read the Form 4 tables and transaction codes. Only code P open-market
  purchases count as buys; grants, option exercises and tax-withholding sales are excluded.
- **GIGO:** run conformance checks, then promote raw data to verified only when every check passes.
- **ENRICH:** compute market-adjusted returns against SPY over a fixed window starting the
  trading day after the filing date.
- **SIGNALS:** score cluster buys (2+ insiders at one company within 30 days), weighted by
  role and purchase size, as STRONG / WATCH / SKIP.
- **AGENT:** run a LangGraph pipeline with gates that ends in a human attestation step
  before anything is reported.
- **REPORT:** produce a sourced report linking every signal to its SEC filings.

## 12-week plan (Nov 2, 2026 – Jan 22, 2027)

| Week | Dates | Engineering milestone | Weekly-work video topic | STEM video topic |
|---|---|---|---|---|
| 1 | Nov 2 – Nov 8 | Spec, data contract, gate table | Designing the agent | What is a Form 4? |
| 2 | Nov 9 – Nov 15 | Ingest with fair-access rules, checkpoint/resume, tests | Pulling filings from the SEC | Why rate limits exist |
| 3 | Nov 16 – Nov 22 | Parse transaction codes; keep only open-market purchases | Filtering real buys | Signal vs. noise |
| 4 | Nov 23 – Nov 29 | Conformance checks and the raw → verified gate | Validating the data | Garbage in, garbage out |
| 5 | Nov 30 – Dec 6 | Prices and market-adjusted returns | Adjusting for the market | Alpha vs. beta |
| 6 | Dec 7 – Dec 13 | Cluster detection and scoring | Scoring insider clusters | Base rates and skip rates |
| 7 | Dec 14 – Dec 20 | LangGraph agent with gates and human attestation | Building the agent | Why agents need hard stops |
| 8 | Dec 21 – Dec 27 | Honest backtest | Testing the signal | Look-ahead bias |
| 9 | Dec 28 – Jan 3 | MCP tools and the report | Packaging the tools | Survivorship bias |
| 10 | Jan 4 – Jan 10 | Edge cases (amended filings, missing tickers), more tests | Hardening | Multiple comparisons |
| 11 | Jan 11 – Jan 17 | Comparison with congressional-signals | Insiders vs. politicians | Correlation vs. causation |
| 12 | Jan 18 – Jan 22 | Documentation, research report, PR | Wrapping up | What the project taught me |

## Risks

- **Amended filings.** A Form 4/A can change an earlier filing. Mitigation: keep the
  original, and let the amendment count only from its own filing date, so a backtest never
  uses a correction that wasn't public yet.
- **Transaction-code noise.** Code P covers private as well as open-market purchases, and
  plan-based (10b5-1) buys are pre-scheduled. Mitigation: flag both, report how many, and
  don't let flagged buys score STRONG.
- **Look-ahead bias.** Mitigation: measure from the filing date, not the trade date; start
  returns the next trading day; fix every threshold in a pre-registration file before
  looking at outcomes.
- **Small sample sizes.** True cluster buys may be rare, and a handful of big winners can
  dominate an average. Mitigation: report counts alongside every average, and don't claim
  signal from a few cases.
- **Data gaps.** Blank or outdated tickers, delisted companies, and SEC's own caveat that
  the bulk data "may contain redundancies, inconsistencies, and discrepancies". Mitigation:
  record every missing price with a reason, report coverage at the G3 gate, and spot-check a
  sample against the original filings.

## Reporting

- A weekly update to my PM.
- Bi-weekly GitHub commits with completed work, challenges, goals and hours.
- A `FRICTIONAL.md` for each week's work folder, written as the work happens.

## Definition of done

- A tested `insider-signals/` module merged to Mycroft.
- A research report.
- Two videos per week (one on the week's engineering work, one STEM explainer).
