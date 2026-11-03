# FACTCHECK: Week 25 work video, *Same Logic, Two Languages*

Every claim the script makes, with its verification level. **Nothing enters the script until its row reads ✅.**

**Levels:**
- **live run**: executed on 2026-10-04 (Node and Python 3.9 on this machine, or the recipe's scripts on a copy of the pushed commit).
- **repo record**: stated in a committed file on `Tanmay-Kulk/mycroft` @ `add-contradiction-detection-recipe` (commits `dd60da6`, `d9cd514`) or upstream `nikbearbrown/mycroft` `main` @ `f596c75`.

Framing rule: every gap shown is in **my** work. The original workflow is never criticised and no author is named.

---

## Part 1: the two languages (live)

| # | Claim | Level | Evidence | Status |
|---|---|---|---|---|
| L1 | JavaScript `(0.625).toFixed(2)` gives "0.63"; Python `f"{0.625:.2f}"` (and `round(0.625, 2)`) gives "0.62" | live run | Node: `0.63`; Python: `0.62` / `0.62` | ✅ "the everyday way" = format/round. 0.625 is exact in binary, so this is a real tie |
| L2 | JavaScript prints 1.0 as "1"; Python prints "1.0" | live run | Node `String(1.0)` → `1`; Python `str(1.0)` → `1.0` | ✅ |
| L3 | `[] \|\| "x"` keeps `[]` in JavaScript; Python `[] or "x"` gives `'x'` | live run | Node `[]`; Python `'x'` | ✅ "keeps an empty list … skips past it" |

## Part 2: Mycroft and the recipe (repo record)

| # | Claim | Level | Evidence | Status |
|---|---|---|---|---|
| R1 | Mycroft "is both a book and a working agentic repository" | repo record | upstream `README.md` line 9 | ✅ verbatim. "for finance" is my gloss, outside the quote |
| R2 | Mycroft's P6: "Disagreement between recipe, script, and run is a logged defect — no artifact silently wins." | repo record | upstream `SNICKERDOODLE.md` P6 | ✅ The script says "no artifact silently wins" (verbatim fragment) |
| C1 | Recipes are reusable pipelines (recipe = spec + scripts) | repo record | `SNICKERDOODLE.md`; `recipes/` | ✅ plain-words paraphrase |
| C2 | I worked on a contribution: rewrote the core logic (the two JavaScript code nodes) into Python; the recipe now has scripts that run | repo record | `…-run-approved-tools.py` docstring; recipe step Status lines | ✅ "so the recipe has scripts that run" (neutral: says what we added) |
| C3 | Five evidence sources, six patterns, every flag for human review | repo record | recipe; flags carry `requires_human_review: true` | ✅ |
| C4 | 16 invented companies, every name ends "Fixture Co"; no real company represented | repo record | `FIXTURE_MANIFEST.md`; `expected-flags.json` (Alpha … Romeo Fixture Co) | ✅ |
| C5 | Expected flags were written by reading the JavaScript **before** any Python existed: 13 flags across 16 companies | repo record | `expected-flags.json` basis: "Reasoned from the ORIGINAL JavaScript before any port existed"; 13 flags counted | ✅ |
| C6 | The parity check extracts the original JavaScript from the workflow file, runs it under Node beside the Python, and compares field by field (flags, evidence text, IDs, summaries); 16/16 agree | repo record + live run | `…-parity-check.py` docstring; run on `d9cd514`: exit 0, 16/16 | ✅ Not claimed: "first time" (unknown, dropped) |
| C7 | The port imitates JavaScript on each seam (`js_to_fixed`, `js_str`, `js_or`), and flag text carries such numbers | repo record | `…-run-approved-tools.py` L53–83; FXQ flag: `confidence=1`, `avg score 0.63` | ✅ |
| C8 | With the test companies that existed before FXQ and FXR, the comparison noticed neither 0.6 → 0.61 nor Python rounding | live run | scratch copy of `d9cd514` with FXQ/FXR removed: real port 14/14, 0.61 → 14/14, rounding → 14/14 (2026-10-04); matches my build notes | ✅ On screen labelled "scratch run". Said as "my test companies", not "my sixteen" |
| C9 | Romeo Fixture Co (FXR): confidence exactly 0.6. Quebec Fixture Co (FXQ): news average exactly 0.625. With them, 0.61 fails only on FXR and rounding only on FXQ | repo record + live run | `FIXTURE_MANIFEST.md`; `guidance-signals.json` (FXR 0.6); live run: 15/16, disagreeing [FXR] / [FXQ]; self-test section B | ✅ |
| C10 | At the gate-6 review, the defective-run report said 13 rejected rows and its agent log said 0; the log counted only step 4, which never ran | repo record | commit `dd60da6`: report "Rejects 13 …", log `rejects` length 0; `d9cd514` message | ✅ "the run that's designed to stop early" = the defective set, stops at step 3 by design |
| C11 | Now one list feeds both; unchecked items say "not checked"; a new test compares the two | repo record | `d9cd514`: produce-human-report; self-test section G (fails on the old version: 3 unexpected) | ✅ |
| C12 | Sample data only; no database, news API or model ever called; live data, model answers and live failures untested; live mode declined at gate 5 with written preconditions | repo record | gate-5 record (`deny`, 4 preconditions); self-test `live_call_performed: false`; recipe "Not claimed" | ✅ "That call belongs to the people with live access" |
| C13 | 115 added, 3 modified (recipe page, two appended shared files), 0 removed, 0 renamed; on my fork, awaiting review | live run | GitHub compare `main...Tanmay-Kulk:add-contradiction-detection-recipe`, 2026-10-04 | ✅ Narration no longer mentions the fork or review (removed at Tanmay's request, 2026-10-04); only the comparison numbers are claimed |

## Wording checks (no critique, humble)

- Scanned: no "bug/defect/flaw/wrong" about the original workflow; no author named.
- Avoided earlier films' signatures: "break", "attack", "gently", "coverage", "receipt", "fails closed", "dark", "watch it catch". "On purpose" once (B06); B07's "changed on purpose" is on screen only.
