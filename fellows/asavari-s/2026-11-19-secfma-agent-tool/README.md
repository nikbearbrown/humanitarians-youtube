# SEC agent as a tool other agents can call

**Fellow:** Asavari (Ash) Shejwal &nbsp;·&nbsp; **Team:** Agents & Jobs (PM: Tanmay Sangam) &nbsp;·&nbsp; **Started:** 2026-11-19 &nbsp;·&nbsp; **Status:** first version committed; task pending PM confirmation

## What and why

Mycroft's agents need financial figures. If they ask a language model, they can get a confident number that doesn't match the filing. This task turns my SEC Filings Financial Metrics Agent into one tool, `get_verified_financials`. An agent calls it with a ticker and a fiscal year and gets back SEC-reported values, where each one came from, and whether the figures hang together. No language model is involved anywhere in that path. (Mycroft is one of the [Humanitarians AI Agents projects](https://www.humanitarians.ai/agents), so this is Agents & Jobs work.)

## What I built

| Piece | Where |
|---|---|
| The tool: `get_verified_financials(ticker, fiscal_year, metrics)` | [`secfma/tool.py`](https://github.com/nikbearbrown/mycroft/blob/feature/secfma-agent-tool/scripts/sec-filings-financial-metrics/secfma/tool.py) |
| `run_tool(arguments)`: takes raw tool-call arguments and validates them | same file |
| Tool definition (`TOOL_SPEC`, plus the OpenAI function format) | same file; `python3 -m secfma.tool --spec` |
| Command line: `python3 -m secfma.tool --ticker MSFT --year 2024` | same file |
| 16 offline tests on the bundled sample company | [`tests/test_tool.py`](https://github.com/nikbearbrown/mycroft/blob/feature/secfma-agent-tool/scripts/sec-filings-financial-metrics/tests/test_tool.py) |
| Usage docs, an example response, and how an agent calls it | [package README](https://github.com/nikbearbrown/mycroft/blob/feature/secfma-agent-tool/scripts/sec-filings-financial-metrics/README.md#agent-tool-get_verified_financials) |
| Recipe v0.3.0: tool listed, claims corrected, open issues recorded | [`recipes/sec-filings-financial-metrics.yaml`](https://github.com/nikbearbrown/mycroft/blob/feature/secfma-agent-tool/recipes/sec-filings-financial-metrics.yaml) |

## How it behaves

| Promise to a calling agent | What it means | Tested by |
|---|---|---|
| Deterministic | Same inputs and same cached SEC data give the same output | `test_deterministic` |
| Never guesses | A metric with no reliable source is `MISSING`, with `value: null` and a reason. Never 0. | `test_missing_is_never_zero` |
| Provenance on every value | XBRL tag, how it was resolved (`us-gaap` / `custom-extension` / `derived`), accession, form, filed date, EDGAR link | `test_value_matches_filing_and_carries_provenance`, `test_custom_extension_is_labelled` |
| Validation travels with the numbers | PASS / FAIL / UNKNOWN checks run on exactly the values returned | `test_validation_attached_for_the_period` |
| Errors are data, not crashes | `{"ok": false, "error": {"type": ...}}` for a bad ticker, year, metric, arguments, or a network failure | `ErrorTests`, `RunToolTests` |

## Verification

| Check | Result | Evidence |
|---|---|---|
| Offline unit tests | 16/16 pass on Python 3.9 and 3.11 | [`tests/test_tool.py`](https://github.com/nikbearbrown/mycroft/blob/feature/secfma-agent-tool/scripts/sec-filings-financial-metrics/tests/test_tool.py) |
| Live golden-set check through the tool | 16/16 rows match within 0.5% (MSFT FY2023–25, JNJ FY2024, XOM FY2024) | [Mycroft `RUN_LOG`, 2026-11-19](https://github.com/nikbearbrown/mycroft/blob/feature/secfma-agent-tool/logs/RUN_LOG.md) |
| Mycroft conformance (`scripts/conformance.mjs`) | All changed files conform | same log entry |
| Exxon FY2024 validation | Accounting identity **FAILs** by 1.52%: parent-only equity leaves out the $6.9B non-controlling interest. An R&D restatement is flagged UNKNOWN. Both are correct signals to the calling agent, not tool errors. | same log entry |

**Commits:** [`2c51c84` the tool and tests](https://github.com/nikbearbrown/mycroft/commit/2c51c84) · [`79a6435` recipe v0.3.0 and docs](https://github.com/nikbearbrown/mycroft/commit/79a6435). Branch `feature/secfma-agent-tool`, stacked on [PR #13](https://github.com/nikbearbrown/mycroft/pull/13).

## Still open

- **PM confirmation:** Tanmay hasn't confirmed this as my task yet.
- **Code review:** I haven't reviewed Claude's code yet; I'll do it before opening the pull request.
- **Equity in the identity check:** should it use total equity (including non-controlling interest) when that's available? This needs a decision, not a silent change.
- **No calling agent yet:** the tool isn't wired into an agent. Candidates: finance-event-signals, Agentic Runway-Risk Pipeline.
- **Benchmark coverage:** 5 of 13 base metrics and none of the derived ratios. Walmart total liabilities is still UNKNOWN.

## Next steps

| Deliverable | Target |
|---|---|
| Task confirmed with my PM | 2026-11-25 |
| Review the code, open the pull request (stacked on PR #13) | 2026-11-30 |
| Wire the tool into one Mycroft agent | after confirmation |

**Log:** [`FRICTIONAL.md`](FRICTIONAL.md)
