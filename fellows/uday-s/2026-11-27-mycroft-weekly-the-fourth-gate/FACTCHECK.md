# FACTCHECK — The Fourth Gate

Episode 14. Subject: `D:\Projects\mycroft` @ **`20795b2`**, branch
**`chore/promote-scenariostresstestingagent`**, pushed and contained in origin.

**The mycroft tree was treated read-only throughout.** No `snickerdoodle run`,
no `snickerdoodle gate` (it writes a decision record), no conformance pass (it
compiles Python and would leave `__pycache__`). Every gate test below was
reproduced in a **scratch folder outside the repository**, against files broken
on purpose, from command text read with `git show`.

---

## Verified, and on screen

| Claim | Beat | How it was checked | Result |
|---|---|---|---|
| Branch, HEAD `20795b2`, pushed | meta | `git rev-parse`, `git branch -r --contains` | ✓ in origin |
| The recipe diff is **only** `status` and `last_gate` | B01 | `git show 20795b2 -- recipes/scenariostresstestingagent.md` | ✓ 2 fields, 4 diff lines |
| `recipe_version` stays `0.4.0` | B09 | same diff | ✓ unchanged |
| Live execution stays blocked, no gate 5 record | B01, B09 | commit body + `logs/gate-decisions/` absent | ✓ |
| Gate 1 ends in `\|\| true` | B04, B05 | recipe line 54, verbatim | ✓ |
| Gate 3 is `find … -exec python3 -m json.tool {} \;` | B04, B05 | recipe line 56, verbatim | ✓ |
| Gate 6 tests a literal `[DATE]` filename | B04, B05 | recipe line 59, verbatim | ✓ |
| Gate 1 returns 0 when the pattern is present | B05 | scratch repro | ✓ exit 0 |
| Gate 1 returns 0 when the pattern is absent | B05 | scratch repro | ✓ exit 0 |
| Gate 1 returns 0 **when the file does not exist** | B05 | scratch repro | ✓ exit 0 — not claimed by the commit |
| Gate 3's `json.tool` exits 1 on a broken file, `find` still exits 0 | B05 | scratch repro, deliberately invalid JSON | ✓ 1 and 0 |
| Gate 6 exits **1** | B05, B07 | scratch repro, real dated file present | ✓ exit 1 |
| No literal `[DATE]` file is tracked | B07 | `git ls-tree -r \| grep -F '[DATE]'` | ✓ none; real dated logs exist |
| Clean corpus: 12 records, 12 accepted, 0 rejected | B08 | `data/verified/…/clean/validated.json` | ✓ |
| Defective corpus: 10 records, 0 accepted, 10 rejected | B08 | `data/verified/…/defective/validated.json` | ✓ |
| Both corpora declare `mode: sample` | B08 | same two files | ✓ |
| Self-tests 27/27, 31/31, 37/37 | B08 | the four committed result JSONs | ✓ 27 checks/27 as_expected; 31/31; 37/37 |
| 12/12 deliberate breaks caught | — | `self-test-results.json` | ✓ (not shown — see below) |
| **94 DRAFT + 3 RUNNABLE-SAMPLE = 97 recipes** | B08 | status frontmatter of every `recipes/*.md` at `20795b2` | ✓ exactly |
| 99 `.md` files in `recipes/`, 2 without status | B08 | same sweep | ✓ `README.md`, `_shared.md` |
| The two `[TODO: DEV]` judgment calls | — | `produce-human-report.py` tracked; `respond-to-webhook.py` absent | ✓ both as the signer described |
| The handoff's next action changed from "promote" to "make its gate tests real" | B09 | `git show 20795b2 -- session-handoff.md` | ✓ verbatim |

---

## Findings that are MINE, not the commit's

### 1. A fourth gate that cannot fail (B06)

The commit names gates 1, 3 and 6. **Gate 4 has the same property and is not
mentioned.** Its test is:

```
test -f scripts/ingest/<recipe>-ingest-inputs.py || rg --fixed-strings "[TODO: DEV]" "recipes/<recipe>.md"
```

The fallback searches the recipe for `[TODO: DEV]` — and that literal string is
**inside gate 4's own test command, which is written in the file being
searched**. The gate matches itself.

Counted at `20795b2`: the recipe contains **9** occurrences of `[TODO: DEV]`,
**6** of them inside notes explicitly marked `Closed`, and **1** of them is the
gate's own test line.

Reproduced in the scratch folder with a file containing *only* the gate
definition line — no script on disk, no real TODO entries — and it exits **0**.

### 2. The commit message is wrong about gate 6 (B07)

The commit groups gates 1, 3 and 6 as *"cannot fail as written"*. Measured:

| | measured | so it is |
|---|---|---|
| gate 1 | exit 0 in every case | cannot fail |
| gate 3 | exit 0 with a real failure inside | cannot fail |
| **gate 6** | **exit 1** | **cannot pass** |

No file named with a literal `[DATE]` exists, and the real artifacts are dated
(`…-2026-11-01.json`, `…-2026-11-09.json`), so the `test -f` finds nothing.

These are **opposite defects with opposite consequences**: a check stuck on pass
hides problems silently and indefinitely; a check stuck on fail is noticed the
first time anyone runs it. The reel states the correction on screen.

---

## Recorded, not shown

- **Parity is 24 of 24 matching, out of 25 rows.** `parity-results.json` gives
  `matching: 24`, `mismatching: 0`, `not_modelled: 1`, `rows: 25`. The commit's
  "24/24" is true as stated — 24 compared, 24 matched — but the denominator is
  24, not 25. B07 says so.
- **A skipped-count difference.** The RUN_LOG entry describes the signer's
  scratch run as "27/27, 12/12 deliberate breaks caught, 1 skipped". The
  committed `self-test-results.json` records `skipped: 0`. Different runs on
  different machines; neither contradicts the 27/27. B07 says so.
- **The CLI does not execute gate tests at all.** `snickerdoodle gate` records a
  human decision and hashes path-shaped tokens out of the test string; it
  explicitly notes it cannot distinguish a `[DATE]` template from a missing
  file. So these tests are commands a human is expected to run — which is why
  "can it fail" is a question about the human's workflow, not the CLI's. This
  shapes B02 and B10 but is not asserted as a figure.
- `missing_fields: ["custom_scenario", "scenario_type"]` in the clean corpus is
  consistent with `required_fields_present: true` — neither is in the contract's
  `required_fields`. Checked, not a defect, not shown.
- The ingest self-test reads 36/37 on Windows because it compares paths written
  with `/`. The committed artifact (the author's run) is 37/37. B08 shows the
  committed 37/37; the Windows false alarm is not shown, because it is a
  property of my machine rather than of the code.
