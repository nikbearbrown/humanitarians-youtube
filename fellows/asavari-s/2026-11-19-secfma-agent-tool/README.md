# SEC agent as a tool other agents can call

**Fellow:** Asavari (Ash) Shejwal &nbsp;·&nbsp; **Team:** Agents & Jobs (PM: Tanmay Sangam) &nbsp;·&nbsp; **Started:** 2026-11-19

My first Agents & Jobs task, proposed to my Project Manager for confirmation: package my SEC Filings Financial Metrics Agent as a deterministic tool, `get_verified_financials`. Other Mycroft agents can call it for verified financials (values, provenance, PASS/FAIL/UNKNOWN validation) instead of asking a model for a number.

## Evidence

- **Code:** [`2c51c84` feat(finance): add get_verified_financials agent tool](https://github.com/nikbearbrown/mycroft/commit/2c51c84), branch `feature/secfma-agent-tool`, stacked on [PR #13](https://github.com/nikbearbrown/mycroft/pull/13).
- **Tests:** 16 offline tests (`tests/test_tool.py`), passing on Python 3.9 and 3.11.
- **Live check:** 16/16 golden-set rows (MSFT, JNJ, XOM) match within 0.5% through the tool.
- **Log:** [`FRICTIONAL.md`](FRICTIONAL.md)

## What's next

- Confirm the task with my PM.
- Open the pull request (target: Nov 30).
- Wire the tool into one Mycroft agent.
- Settle the equity question raised by the XOM check (see the log).
