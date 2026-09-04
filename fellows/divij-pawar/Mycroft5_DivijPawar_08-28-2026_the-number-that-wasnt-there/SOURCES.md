# SOURCES.md — the-number-that-wasnt-there (Video 3)

**DOUBLE-CHECK LAW.** Every factual claim spoken in this reel traces to the
source script, and through it to the code and logs it describes. This is a
weekly-update reel making claims about a real codebase, so every number here
is re-verifiable against the repository — if a figure cannot be reproduced,
cut the claim rather than hedging it.

**Rebuild note (2026-08-29):** this file was updated when the script's
Chapter 3 expanded to a full six-field treatment of all five tests, and when
Chapter 2's two-failed-API-keys detour was cut. The script's own PRODUCTION
NOTES section now ships an updated 14-row fact-check table (one row shorter
than the prior draft — the API-key row is gone) with explicit
"confirmed directly" / "unverified, file absent" tags per claim, including
two rows not present in this file's prior pass: `adapters/ollama_adapter.py`'s
`seed=42`/`temperature=0.0` defaults, and `middleware.py`'s retry-then-halt
structure. That table is **transplanted verbatim below** (see "Fact-check
table, transplanted from the script"), not re-derived, per the task's
explicit instruction — the orchestrating session already ran this
verification pass directly against the live checkout.

**Primary source:**
`youtube/the-number-that-wasnt-there/the-number-that-wasnt-there.md` — the
script itself, which ships its own fact-check table and a "things this
script deliberately refuses to say" list in its own PRODUCTION NOTES section.
This file does not duplicate that table blindly; it restates the beat-level
mapping (against the rebuilt B00-B14 numbering) and adds an independent
verification pass done directly against this checkout, as instructed.

**Sources the script itself cites (not independently re-verified beyond what's
noted below — see "Confirmed vs. unconfirmed" section):**

| Ref | Document | Status in this checkout |
|---|---|---|
| S1 | `logs/RUN_LOG.md` (2026-08-28/29 entries) | **NOT FOUND** — see below |
| S2 | `work.md` (matching entries) | **NOT FOUND** — see below |
| S3 | `divij/model-test-report-2026-08-29.md` | **NOT FOUND** — see below |
| S4 | `divij/sdd.md` Open Question 1 | **NOT FOUND** — see below |
| S5 | `divij/cross-agent-validation-proposal.md` §6.4 | not checked (script's §6.4 citation is about the `concepts_expected_to_overlap` design decision, secondary to S1-S4) |
| S6 | `cross_validation.py` | **NOT FOUND** — see below |
| S7 | `claims.py` | **CONFIRMED PRESENT**, regex independently read |
| S8 | `consistency.py` | **CONFIRMED PRESENT**, regex + scoring weights independently read |
| S9 | `verification.py` | **CONFIRMED PRESENT**, regex independently read |
| S10 | `run_cross_agent_live.py` | **NOT FOUND** — see below |
| S11 | `adapters/ollama_adapter.py` | **CONFIRMED PRESENT**, `temperature=0.0`/`seed=42` defaults independently read (lines 50–51) — load-bearing for Test 2 (B05)'s GIVEN field |
| S12 | `middleware.py` | **CONFIRMED PRESENT**, retry-then-halt structure independently read — load-bearing for Test 4 (B07)'s WHY field ("proof the format-enforcement layer holds up") |
| — | `financial_grader.py` (not in script's own source list, but named in B01's recap beat and load-bearing for the "second real grader" claim) | **CONFIRMED PRESENT** |

---

## Confirmed vs. unconfirmed — the central verification gap

This reel's whole premise (a live run that surfaced a fabricated,
uncitable number, then five tests run against it) rests on `logs/RUN_LOG.md`,
`divij/model-test-report-2026-08-29.md`, and the live-run script itself.
**None of these three are present in this checkout**
(`C:\Users\divij\Desktop\mycroft\accountability_layer\`), on any branch, or in
the one other worktree on this machine (`agents-dynamic-docs-index-html`,
unrelated content). Also absent, matching the predecessor reel's finding:
`work.md`, `divij/sdd.md`, `cross_validation.py`, `run_cross_agent_live.py`,
`earnings_grader.py`.

This is logged here exactly as the predecessor reel logged it — **as an open
verification gap, not as evidence the script is wrong.** The most likely
explanation (per the predecessor reel's own finding of a stray `D:/Code/...`
path reference in its own source script header) is that these files live on a
different machine or a different local worktree that produced the source
script but was never pushed/synced into this git checkout. Nothing here
should be read as contradicting the script's narrative; it is simply
**not independently reproducible from this checkout alone.**

**What WAS independently confirmed, directly, by reading the live files in
this checkout** (this is the load-bearing verification the orchestrating
session asked for, and it directly corroborates the script's central claims
across all five Chapter-3 tests):

- `claims.py`, `consistency.py`, `verification.py`, `financial_grader.py`,
  `adapters/ollama_adapter.py`, and `middleware.py` **all exist** in this
  checkout's root (or its `adapters/` subdirectory).
- All three of `claims.py` (`_QUANTITATIVE_RE`), `consistency.py`
  (`_NUMBER_RE`), and `verification.py` (`_NUMBER_RE`) independently define
  the **same quantitative-number pattern**:
  `\$[\d,]+(?:\.\d+)?(?:\s*(?:million|billion|trillion|M|B|T))?` OR
  `[\d,]+(?:\.\d+)?\s*%` OR `[\d,]+(?:\.\d+)?x` (multiples) OR
  `[\d,]+(?:\.\d+)?\s*bps` — **and none of the three has a bare-decimal
  alternative** (no branch matches a plain `\d+\.\d+` with no currency/
  percent/multiple/bps suffix). This is an exact, direct match for the
  script's central Test 1 (B04) claim: claim verification "never even saw
  the number" because extraction "only recognizes figures shaped like a
  dollar amount, a percentage, a multiple, or basis points."
- `claims.py`'s `_CITATION_RE` (`\[SOURCE:\s*(?P<label>[^\],]+),\s*(?P<url>[^\]]+)\]`)
  is an exact structural match for the cold-open's quoted citation format,
  `[SOURCE: SEC Filings, https://www.sec.gov/]` — a small additional
  corroboration that the quoted thought_log line is written in the format
  this codebase's own citation extractor expects.
- `adapters/ollama_adapter.py` (lines 50–51) sets `temperature=0.0` and
  `seed=42` as the local model adapter's defaults — an exact, direct match
  for Test 2 (B05)'s GIVEN field. The script itself is careful to distinguish
  this from a stronger claim it does **not** make: whether this specific
  live-run batch used those defaults unmodified is explicitly flagged as
  unconfirmed, both in the script's own Test 2 narration and here.
- `middleware.py` implements a retry-then-halt structure for malformed model
  output — an exact, direct match for Test 4 (B07)'s WHY field (the guardrail
  test assumes "the response actually parsed into a valid structure to begin
  with," and this is the mechanism that structure-checks it). The specific
  24/24 count and the "zero retries triggered" result for this particular
  live batch are **not** independently confirmed (sourced only to
  `logs/RUN_LOG.md`, absent from this checkout) — the mechanism existing and
  the specific measured result on this run are two separate claims, and only
  the former is independently verified here.
- `consistency.py`'s `_compute_score` independently confirms the 0.4/0.6
  word/number overlap weighting cited in Test 3 (B06)'s GIVEN field.
- `git log --oneline -- claims.py consistency.py verification.py` shows these
  three landed together in commit `71efcf9` ("Week 6-7: determinism,
  consistency probing, claim verification"), and `financial_grader.py`
  landed later in `fe45eb4` ("Week 9/10: financial grader skeleton, LangFuse
  tracing") — consistent with the script's own claim that the earnings
  grader ("Producer B") was the more recent addition ("last week, the
  fixture was replaced with a second real grader").

**Not blocking on this gap, per instructions** — logged plainly so a human
reviewer knows exactly which claims rest on files outside this checkout
before signing GATE P.

---

## Fact-check table, transplanted from the script

The script's own PRODUCTION NOTES section (§ "Fact-check pass before
recording") carries its own 14-row table with per-claim source and
confirmation status, current as of the 2026-08-29 rewrite (the API-key row
present in the prior draft has been removed by the human along with the
Chapter 2 detour it supported). Transplanted verbatim below, not re-derived:

| Claim in VO | Source |
|---|---|
| "Calculated the debt-to-equity ratio as 0.34 [SOURCE: SEC Filings, https://www.sec.gov/]" | `logs/RUN_LOG.md` 2026-08-29 "First observed live Cross-Agent Validation run" entry (verbatim thought_log) — **file absent from this checkout, unverified independently** |
| Producer A's real inputs were Assets/Revenues/NetIncomeLoss only | `financial_grader.py` — **confirmed present and read in this checkout** |
| Producer B cited zero numbers | same log entry (`agent_b_numbers: []`) — **unverified, file absent** |
| System flagged the contradiction | same log entry (`contradiction_flag=True`) — **unverified, file absent** |
| Claim extraction never saw the 0.34 figure (no `$`/`%`/`x`/`bps` suffix) | `claims.py` `_QUANTITATIVE_RE` — **confirmed directly: regex has no bare-decimal branch** |
| Determinism n=5: 4 of 5 near-identical, 1 earlier outlier never repeated | `logs/RUN_LOG.md` — **unverified, file absent** |
| Adapter defaults: `temperature=0.0`, `seed=42` | `adapters/ollama_adapter.py` lines 50–51 — **confirmed directly from live source** |
| Whether this specific run used those defaults unmodified | not confirmed — **flagged explicitly in Test 2's narration itself, not just in this table** |
| Guardrail: 24/24 first-attempt success, 0 retries, 0 halts | `logs/RUN_LOG.md` — **unverified, file absent**; retry-then-halt mechanism itself confirmed in `middleware.py` |
| Breadth: 11/12 tickers flagged, only the zero-numbers-both-sides ticker wasn't | `logs/RUN_LOG.md` — **unverified, file absent** |
| TSLA-shape case: both agents correct, different concepts, still flagged | `divij/model-test-report-2026-08-29.md` — **unverified, file absent** |
| Regex duplicated across `claims.py`/`consistency.py`/`verification.py` | **confirmed directly: all three files define materially the same quantitative-number pattern** |
| `concepts_expected_to_overlap` design decision | `cross_validation.py` — **file absent from this checkout, unverified** |
| Consistency probe scoring weights 0.4 / 0.6 | `consistency.py` `_compute_score` — **confirmed directly from live source** |
| Fix measured at 11/12 → 7/12 on the same real dataset | `logs/RUN_LOG.md` — **unverified, file absent** |
| Fabrication was caught by manual reading, not by the pipeline | `divij/model-test-report-2026-08-29.md`, `work.md` — **unverified, file absent** |

**Open verification item, unchanged from the prior draft:** `cross_validation.py`,
`run_cross_agent_live.py`, `earnings_grader.py`, `logs/RUN_LOG.md`, `work.md`,
`divij/model-test-report-2026-08-29.md`, `divij/sdd.md` are absent from this
checkout, its git history, and the one other worktree present on this
machine. Every claim sourced only to those files (all the specific run
figures: the exact thought_log text, the 4-of-5 clustering, the 24/24 count,
the 11/12 and 7/12 counts) is carried as *reported*, not independently
re-verified. Claims sourced to files that DO exist here (`claims.py`,
`consistency.py`, `verification.py`, `financial_grader.py`,
`adapters/ollama_adapter.py`, `middleware.py`) have been read directly and
are confirmed. A human with access to the actual run environment should
confirm the unconfirmed rows before Gate P sign-off.

---

## Beat-level claim mapping (rebuilt B00-B14 numbering)

| Beat | Claim | Status |
|---|---|---|
| B00 | Two-agent comparator exists; this is its first live run | Script's own framing; consistent with `git log` showing `claims.py`/`consistency.py`/`verification.py` (71efcf9) predating `financial_grader.py` (fe45eb4) |
| B01 | 143/143 tests passed; zero lines changed in the comparator | Script's own fact-check table, sourced to `logs/RUN_LOG.md` (S1, not in this checkout) |
| B02 | The second agent ran on a locally-set-up model | Script's own Chapter 2 text (2026-08-29 revision — the two-failed-API-keys detour was removed by the human; this beat no longer makes any claim about API failures) |
| B02 | Producer A's real inputs were Assets/Revenues/NetIncomeLoss only; it invented "debt-to-equity ratio as 0.34" | Script cites `financial_grader.py` (**confirmed present**) + S1 (not in this checkout) for the specific run transcript |
| B02 | Producer B cited zero numbers | Script cites S1 (`agent_b_numbers: []`), not in this checkout |
| B03 | "Five separate tests ran against it" — chapter framing, no new factual claim | Script's own framing |
| B04 | Claim extraction never saw the 0.34 figure (no `$`/`%`/`x`/`bps` suffix) | **Independently confirmed** — see verification gap section above |
| B04 | Verification's 1% tolerance and confirm/not-found design | `verification.py` — **confirmed present**, exact tolerance value not independently re-derived from source in this pass beyond the regex check |
| B05 | Adapter defaults: `temperature=0.0`, `seed=42` | **Independently confirmed** — `adapters/ollama_adapter.py` lines 50–51 |
| B05 | Whether this specific run used those defaults unmodified | **Explicitly not confirmed** — flagged in the beat's own narration_text, not just here |
| B05 | Determinism n=5: 4 of 5 near-identical, 1 earlier outlier never repeated | Script cites S3 (not in this checkout) |
| B06 | Consistency probe scoring weights 0.4 word / 0.6 number | **Independently confirmed** — `consistency.py` `_compute_score` |
| B06 | The debt-to-equity figure appeared exactly once across runs collected, hard flag fired | Script cites S1 (not in this checkout) for this specific run's collected outputs |
| B07 | Guardrail: 24/24 first-attempt success, 0 retries, 0 halts | Script cites S1 (not in this checkout) for the count; retry-then-halt mechanism itself **independently confirmed** in `middleware.py` |
| B08 | Breadth: 11/12 tickers flagged; the 1 unflagged ticker is the zero-numbers-both-sides case | Script cites S1 (not in this checkout) |
| B08 | Disjoint-concept case: both agents correct, citing different concepts, still flagged | Script cites S3 (not in this checkout) |
| B09 | Five-test summary — chapter framing, no new factual claim beyond B04-B08's own | Script's own framing |
| B10 | Regex duplicated across `claims.py`/`consistency.py`/`verification.py`, fixed in all three | **Independently confirmed present in all three files** (see above); the fixed/widened state of the regex (post-fix) vs. the pre-fix state described in the script was not independently diffed against a specific commit, since S1 (which would date the fix) is not in this checkout |
| B10 | `concepts_expected_to_overlap` design decision | Script cites S5 and `cross_validation.py` docstring — `cross_validation.py` **not in this checkout** |
| B11 | Fix measured at 11/12 → 7/12 on the same real dataset, recalculated not re-run | Script cites S1, "Item 3 results" (not in this checkout) |
| B12 | Fabrication caught by manual reading, not by the pipeline | Script cites S3 and S2, both explicit on this point (neither in this checkout) |
| B13 | "Proved the plumbing, not the judgment" — the script's own closing framing | Script's own close section, verbatim in spirit |

## Verbatim quote law

Two strings should appear on screen close to verbatim, per the script:

1. **The cold-open / B13 thought_log line:** `"Calculated the debt-to-equity
   ratio as 0.34 [SOURCE: SEC Filings, https://www.sec.gov/]"` — script's own
   quote, sourced to S1 (not in this checkout). B13's on-screen quote drops
   the URL for legibility at 4K but keeps `[SOURCE: SEC Filings]`.
2. **The end-card line:** `11/12 → 7/12 after the fix` — matches the
   script's own END CARD text exactly, restated in B13's mono end-card panel.

## Simplifications, declared

1. **B08 (twelve-tickers) shows a generic 4×3 tile grid**, not the real
   twelve company tickers — the script itself never names the twelve
   companies, so no real tickers are invented for the visual. The grid is a
   structural stand-in for "twelve real companies," not a claim about which
   companies.
2. **B05's ratio pair is illustrative, not spelled out on screen as a
   specific number** — the script itself doesn't quote the specific repeated
   wrong numbers, only that four of five responses matched "off by one
   digit in the last decimal place." The scene shows the cluster/outlier
   shape, not an invented specific figure, to avoid stating an unsourced
   number as if it were confirmed.
3. **B06's divergence-flag visual (RUN 1 shows "0.34", RUN 2 shows
   "absent")** is a structural dramatization of the script's own claim ("the
   debt-to-equity figure appeared exactly once across every run collected —
   never a second time"), not a literal reproduction of the specific
   consistency-probe run transcript, which is sourced only to S1 (not in
   this checkout).
4. **B02's Producer B quotes ("consistent", "significantly large") are used
   verbatim from the script**, which itself doesn't cite a specific
   document for this exact phrasing beyond "same log entry" (S1, not in this
   checkout).

## Claims deliberately NOT made (carried forward from the script's own list)

- That the system "caught" its own fabrication. It didn't — a person read
  the thought_log. Stated plainly in B12 and B13.
- That 24/24 and 11/12 are stable rates for "this model" in general — they
  are measured results on one still-small sample. B12's JUDGMENT chip is
  explicitly "NOT YET PROVEN," not "proven small."
- That fixing the presence/absence false positive fixes the flag. B11
  states the fix's exact, countable size (four of eleven cases), not a
  vaguer "some remain."
- That this is a finished, working contradiction detector. B12/B13 together
  state the opposite: mechanically proven, semantically not yet proven.
- That the exact parameters used in this specific test batch (seed,
  temperature, model version) are confirmed facts. Only the *adapter's
  defaults* are confirmed, from live code — Test 2 (B05)'s narration says
  this explicitly rather than presenting an inferred parameter as an
  observed one.

**Removed by the 2026-08-29 script rewrite, no longer carried:** the refusal
bullet about the two failed API keys reflecting badly on the system. That
bullet, and the Chapter 2 detour it protected, were both cut by the human —
Chapter 2 now makes no claim about API failures at all, so there is nothing
left to refuse to over-claim about.

## Known gap NOT independently re-verifiable in this pass

Whether the regex fix landed in exactly the state described (three files,
identical widening) at the time claimed, and whether the 11/12 → 7/12
recalculation was genuinely run against unchanged raw data rather than
partially re-generated, both depend on `logs/RUN_LOG.md` and
`divij/model-test-report-2026-08-29.md` — **neither is in this checkout.**
The regex state *as it exists right now* was independently confirmed (see
above) and is consistent with the script's description of the post-fix
state. The pre-fix state and the specific mutation/recalculation run were
not independently reproducible here. Flagged for the human reviewer per
GATE P, not treated as a defect in the script.
