# Week 30 work video: fact-check (draft 1)

Every number and claim in `READ-ALOUD.md` (long) and `READ-ALOUD-SHORT.md` (Short), read from `nikbearbrown/mycroft` `main` (the committed files, via
`git show upstream/main`, read-only) by `factcheck_numbers.py` in this folder; output in `factcheck_numbers.out`.
Result: **33 of 33 facts as expected.** Re-run it before Gate P and again before audio.

Verdicts: **VERIFIED** (read from a committed file), **VERIFIED-RUN** (reproduced by running it), **QUALIFY** (true, but the wording should be tightened),
**FRAMING** (the film's own teaching move, not a factual claim about the repo).

## Reproduction (verified)
Exporting `main` to a clean folder and running the step 2 script with the clock pinned (`--now 2026-11-09T00:00:00+00:00 --sample`, no credential set) exited 0
and produced `source-check.json`, `ingest-audit.md` and both `ingested.json` files **byte-identical** to the committed ones. So "clone it, run it, read the page"
is true for step 2. (The full six-step transcript in `full-sample-run-2026-11-09.md` was made on a scratch copy of the tree; the film's terminal shot should be
a fresh recording, not that file.)

## Claim by claim

| # | Where | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Mycroft is a public repository of recipes an agent runs and a person reads | `gh repo view` → PUBLIC; same description as the Week 29 film | VERIFIED |
| 2 | B00b | One command runs six steps in order and ends "All 6 steps completed" | transcript: six arrows in order, `All 6 steps completed.` | VERIFIED (shown on scratch copy; re-record) |
| 3 | B00b | "Nothing was contacted" | `live_calls`, `network`, `database_writes` all false; every source `live_call_performed: false`; the script imports nothing that can reach a network (self-test check) | VERIFIED for step 2 and for sample mode; see Q1 |
| 4 | B00b | "No key was read" | the script asks `bool(os.environ.get(name))` for two names, so a value is fetched for that test and discarded; the transcript's own words are "no credential read" | **QUALIFY**: say "no key's value was kept or written" (Q1) |
| 5 | B01 | The recipe is a scenario stress testing agent taking an invented portfolio and a market shock | recipe step 3 contract (holdings, `scenario_type`, `custom_scenario`); sample corpus is invented; the recipe's own Purpose paragraph is generic | VERIFIED (from the step 3 contract; no Purpose line to quote) |
| 6 | B01 | Earlier I built steps one, three, four, five and six | #74 (steps 1, 3, 5), #81 (steps 4, 6), #82 (correction to #81), all by Tanmay-Kulk and merged | VERIFIED |
| 7 | B01 | Step two is the one that "checks the sources and the credentials before anything runs" | the recipe calls it the conductor's "Source and Credential Check"; but the transcript shows step 1 (provenance) runs **before** it | **QUALIFY**: it runs before any request is checked or any tool runs, not before anything (Q2) |
| 8 | B03, S03 | The workflow names four sources | `source-check.json`: 4 entries (webhook, chat trigger, Groq call, Alpha Vantage request) | VERIFIED |
| 9 | B03 | Groq row: status approval required; reason a live model call that sample mode never makes | JSON row, reason text | VERIFIED |
| 10 | B04 | Credential name `GROQ_API_KEY`; the script asks the environment whether the name is set; the answer here is no | JSON `credential_env`, `credential_present: false`; script line 129 `bool(os.environ.get(env_name))`; no subscript reads | VERIFIED |
| 11 | B04, S04 | "The value is never read into a variable or a file" / "The value is never read" | the audit's own sentence says "never read into a variable or a file"; strictly, `os.environ.get` hands the value to `bool()` for an instant | **QUALIFY**: "never stored or written down" is exact; "never read" over-states by one step (Q3) |
| 12 | B04b | A value can end up in a log, report, screenshot or message; a yes or no cannot | general knowledge, not a repo fact; the self-test's scan of output files and screen for the dummy values supports the second half | FRAMING (keep as reasoning, not as measured) |
| 13 | B05, S05 | Approval record none; approved for live action false; live call performed false | JSON row + top-level `approval_record_present: false` | VERIFIED |
| 14 | B05, S05 | "Saying yes is a person's act" | recipe approval gate ("require an approval record"); the runner's closing text: gate decisions are "a separate, human act" | VERIFIED |
| 15 | B06 | Webhook available: 22 invented requests, each with a fingerprint recorded when frozen, checked before keeping | JSON `records: 22`; manifest holds 22 SHA-256 values; audit: "keeps each request body exactly as it was frozen" | VERIFIED |
| 16 | B06 | Twelve clean, ten faulty, none rejected | audit table: clean 12 / 0, defective 10 / 0 | VERIFIED |
| 17 | B06 | Chat skipped with a reason; the second live service approval required | JSON | VERIFIED |
| 18 | B06 | "Every source ends up in one of those states, each with a reason" | hand-off condition text and `handoff_condition_met: true` | VERIFIED |
| 19 | B07, S06 | The test builds two dummy values while it runs, from pieces | self-test line 34: `"-".join([...])`, comment "assembled at run time so no credential-shaped text sits in this file" | VERIFIED |
| 20 | B07 | "A made-up key typed into a test file looks, to a reader or a scanner, exactly like a real one that leaked" | my reason for the design (recorded in my build notes); not measured, and no scanner is configured in the repo | **QUALIFY**: "can look like" (Q4) |
| 21 | B07, S06 | The test looks in every file the step writes, for either value | self-test: scans every file under `data/raw/.../ingest/` plus stdout and stderr, with both credentials set | VERIFIED; say "every file the step writes, and the screen" |
| 22 | B07 | It checks every question the script puts to the environment is a yes or a no | self-test: every `os.environ.get` sits inside `bool()`, no subscript read | VERIFIED |
| 23 | B07, S06 | Thirty-seven checks pass | `ingest-self-test-results.md`: "37 of 37 checks came out as expected" | VERIFIED |
| 24 | B08 | Clone, run the command, read one page of what a live run would need, nothing contacted | reproduction above; audit table lists credential name, set or not, and why | VERIFIED-RUN |
| 25 | B10 | Recipe still a draft; going live is a person's decision | frontmatter `status: DRAFT`, `todos_open: 0`, `recipe_version: 0.4.0`; approval gate | VERIFIED |
| 26 | B10 | Pull request eighty five built step two, and it is merged | #85 MERGED 2026-11-09, merge commit `573c96a` | VERIFIED |
| 27 | B02 | A source has three different facts: is it there, who says yes, what is the value | the row's fields map to the first two; the third is deliberately absent | FRAMING |

## Wording fixes (Q1 to Q4: all applied 2026-11-09 in `build_scripts.py`, scripts regenerated, lint clean; the B07 line also now says "and on the screen")
- **Q1.** B00b: "nothing was contacted, and no key was read" → "nothing was contacted, and no key's value was kept." (The runner's own transcript says "no credential read"; ours is more exact.)
- **Q2.** B01: "the one that stands at the door: it checks the sources and the credentials before anything runs" → "the one that stands at the door: before any request is checked or any tool runs, it lists what the pipeline would reach for."
- **Q3.** B04: "never read into a variable or a file" → "never stored, and never written to a file". S04: "The value is never read, so a yes or a no is all there is to leak." → "The value is never stored, so a yes or a no is all there is to leak."
- **Q4.** B07: "looks, to a reader or a scanner, exactly like a real one that leaked" → "can look, to a reader or a scanner, like a real one that leaked." S06 already says "looks like a real leak": same softening.
- **Boundary kept:** steps 3 to 6 still read the fixture folder directly, so the film never says they consume step 2's output; the six-step run shows the order, nothing more.
- **Off screen:** the safe-diff guard, plan files and proof reviews; the W29-adjacent items (stop conditions, planted key in the report self-test) are not mentioned.

## Added after the proof-review edits (2026-11-09)
| # | Where | Claim | Source | Verdict |
|---|---|---|---|---|
| 28 | B07b, S06 | With both keys set, the page says yes for each, and the values appear in no file the step writes and not on the screen | self-test: both credentials set, each reported `true`, `leaked = none` over every file under `ingest/` plus stdout and stderr (FACTCHECK #21) | VERIFIED |
| 29 | B01 | Step two comes right after the provenance check | transcript order: `verify-provenance`, then `ingest-inputs` | VERIFIED |
| 30 | B01 | "I have built five of its six steps in earlier weeks" | #74 (steps 1, 3, 5), #81 (steps 4, 6) | VERIFIED |
| 31 | B03 | Groq is "an AI model hosted by a company" | the node is `lmChatGroq`, role "live model call (llama-3.1-8b-instant)"; the hosting description is general knowledge | FRAMING (plain-words gloss) |
| 32 | B03 | Sample mode is "the practice mode with invented data" that never makes a live call | run envelope: sample mode, no live calls, no network, no database writes; the 22 requests are invented | VERIFIED |
| 33 | B06 | "recorded when the set was fixed" (the manifest's SHA-256 values) | audit: each body "exactly as it was frozen"; manifest holds 22 hashes | VERIFIED |
| 34 | B08 frame | On-screen footer quotes the audit: "A credential is reported only as set or not set; its value is never read into a variable or a file." (second half dimmed) | `ingest-audit.md`, line 23, quoted exactly; narration says "never stored, and never written to a file" (Q3) | VERIFIED as a quote; narration is the tighter wording |
| 35 | B07b frame | `found: none` is the test's own output string for the leak scan | self-test: `f"found: {leaked or 'none'}"` | VERIFIED |
| 36 | B00b frame | `live_calls`, `network`, `database_writes` all false | `source-check.json` top level | VERIFIED |
| 37 | B00b frame | The terminal shows a fresh run: six steps in order, last line `All 6 steps completed.` | `node scripts/snickerdoodle.mjs run scenariostresstestingagent --sample` re-run 2026-11-09 on a clean export of `upstream/main` with no key set: exit 0, same six steps in the same order, same last line (`terminal_run_2026-11-09.out`) | VERIFIED-RUN |
