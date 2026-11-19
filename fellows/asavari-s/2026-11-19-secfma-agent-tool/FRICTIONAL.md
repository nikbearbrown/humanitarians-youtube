# Frictional log — SEC agent as a tool other agents can call

- **Evidence:** [`2c51c84`](https://github.com/nikbearbrown/mycroft/commit/2c51c84) on `feature/secfma-agent-tool` in nikbearbrown/mycroft · [README](README.md)

## 2026-11-19 — first version of `get_verified_financials`

**What I was working on.** My first Agents & Jobs task, chosen today: turn the SEC agent into a tool that other Mycroft agents can call. Mycroft is one of the Humanitarians AI Agents projects, so the work sits inside the team. My Project Manager hasn't confirmed it yet.

**What I tried, and what I expected.**
- I expected the wrapper to be thin glue around the existing pipeline, plus a JSON tool definition.
- I expected tests on the bundled sample company to pass the first time.

**Where it resisted, and what I did next.**
- **Validation needed its own path.** The pipeline's existing `run_all` groups records by the raw XBRL `fy` field, which mislabels prior-year comparatives. That was the original fiscal-year bug. So the tool runs the period checks on exactly the values it returns, rather than filtering `run_all`'s output.
- **The first test run didn't run.** `unittest discover -t .` failed because `tests/` isn't a package. The fix was to run `discover -s tests` instead. After that, all 16 tests passed on Python 3.9 and 3.11.
- **The live check passed, and raised a real question.** All 16 golden-set rows came back correct through the tool. But on Exxon FY2024 the accounting identity FAILs by 1.52%. Exxon reports parent-only equity, so the $6.9B non-controlling interest is the gap. A later filing also revised Exxon's R&D from $987M to $1,000M, which the tool flags as UNKNOWN. I logged the equity question as open in Mycroft's `RUN_LOG` instead of changing the check quietly.

**What Claude contributed, and what I did with it.**
- **Claude:** wrote the tool, the tests, the README section and the `RUN_LOG` entries, then ran the tests, conformance and the live check. It also added a late `RUN_LOG` entry for the 2026-10-31 fixes, which had never been logged.
- **Me:** chose this task over the other three options. Reviewing the code is mine to do before I open the pull request.

**What I understand now, and what I still do not.**
- **Understood:** for an agent, a FAIL is useful output, not an embarrassment. The Exxon result tells a calling agent the balance sheet doesn't tie on parent-only equity, instead of handing it a number to trust blindly.
- **Not resolved:**
  - Should the identity check use total equity (including NCI) when it's available?
  - Which agent should call the tool first?
  - The recipe doesn't list the tool yet, and my Project Manager hasn't confirmed the task.

## 2026-11-19 (later) — documenting the tool

**What I tried, and what I expected.** I wanted the tool documented wherever a reviewer would look: the Mycroft recipe, the package README, and this folder. I expected that to be write-up only.

**Where it resisted, and what I did next.**
- **The recipe was stale.** It didn't mention the tool, the 2026-10-31 fixes, or the open issues.
- **It also overstated the verification.** `verified_against` said "Microsoft FY2020–2025 … balance sheet balances to the dollar." The package README said the same. The golden set was never FY2020–2025: it's FY2023–25, and it now covers 10 companies with 46/46 scored rows. I corrected both and bumped the recipe to v0.3.0 ([79a6435](https://github.com/nikbearbrown/mycroft/commit/79a6435)).
- **The example response was checked, not copied.** The README example was verified against a real `--sample` run (6 PASS, gross margin 0.6167).

**What Claude contributed, and what I did with it.**
- **Claude:** wrote the recipe and README changes and this folder's reviewer page, and found the stale claim.
- **Me:** asked for the work to be documented. Claude made the correction; reviewing it is part of my code review before the pull request.

**What I understand now, and what I still do not.**
- **Understood:** an overstated claim in a recipe is worse than in a video, because other agents and people treat the recipe as the record.
- **Not resolved:** the same open items as above.
