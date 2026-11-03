# Mycroft 6 — "Zero For Sixteen"

**Type:** periodic update (per `divij/video-script-writing-guide.md` §1)
**Runtime target:** 8:00 · ≈1,200 words of VO at ~150 wpm
**Covers:** 2026-09-04 (Compare UI v1, Compare UI v2, SOLID restructure) → 2026-09-07 (real-run
regression corpus + structural diagnosis)
**Sources read before drafting:** `logs/RUN_LOG.md`'s four entries dated 2026-09-04 and 2026-09-07
(in full); `divij/weekly-update-2026-09-04-to-2026-09-07.md`; `divij/work.md`;
`divij/cross-agent-validation-status.md` §3.4 (the gap this period closed);
`divij/cross-agent-validation-disjoint-concepts-diagnosis.md`; `git log` / `git status`.
**Suite state at drafting:** re-ran `python -m unittest discover -s tests -t .` → **224 tests, OK**.
**Visual system:** `brutalist/DESIGN.md` tokens, `brutalist/D3.md` (D3 v7, `var(--color-*)`).

**Style rules (guide §5):** short declaratives, one idea per sentence, "but" is the turn word, no
rounding for rhythm, and capability is never narrated as observation.

---

## 0:00 — COLD OPEN

> **VO:** This tool has flagged sixteen contradictions between two AI agents.
>
> None of them were real.

**VISUAL:** Black. `16 FLAGGED` types on in accent color. Beat. Below it, `0 GENUINE CONFLICTS`.

> **VO:** Not "probably wrong." Not "needs review." I turned all thirty-one runs this thing has ever
> stored into a labeled corpus, replayed every one of them through today's code, and counted.
> Sixteen false positives. Zero cases of two agents citing different values for the same fact.
>
> And the one time it did catch something real — a number an agent invented — the fix I shipped to
> reduce the false positives now suppresses that catch too.

**VISUAL:** A single record card labeled `f4a4c782` slides in, stamped `TRUE POSITIVE`. Then a
second stamp lands over it: `SUPPRESSED TODAY`.

> **VO:** That's this week. Not a feature. A measurement.

**TITLE CARD:** ZERO FOR SIXTEEN
**SUBTITLE:** Mycroft 6 · 2026-09-04 → 09-07

---

## 0:30 — CHAPTER 1: WHERE WE LEFT OFF

**CHAPTER CARD:** 1 · WHAT ALREADY EXISTED

> **VO:** Quick recap. Cross-Agent Validation compares two agents' conclusions about the same
> company and flags when they cite numbers that don't match. It doesn't decide who's right. It
> records the disagreement and hands it to a person.
>
> It runs on top of an accountability layer — append-only storage, one immutable record per agent
> per attempt.

**VISUAL:** Reuse the two-column agent diagram from the prior video. Fast cuts, no new build.

> **VO:** And the last video disclosed one limitation plainly: it over-flags. Seven of twelve
> tickers came back flagged, and the reason was suspected but never measured.
>
> There was also a second gap, and this is the project's own description of it, verbatim:

**VISUAL:** Quote card from `divij/cross-agent-validation-status.md` §3.4:

> "`web/static/index.html` and `app.js` are, as of this document, **completely unmodified** for
> Cross-Agent Validation."

> **VO:** The backend had existed since August twenty-eighth. Nothing in the interface called it.
> Four sessions this period. Two of them closed that gap. One restructured the code underneath.
> And the last one measured the thing everyone had been guessing about.

---

## 1:20 — CHAPTER 2: AN INTERFACE THAT LEADS WITH ITS FAILURES

**CHAPTER CARD:** 2 · THE HONEST LEDGER

> **VO:** The ask for the UI was specific. Not a demo of the happy path — show what's actually been
> tested, and what's actually going wrong.
>
> So the first new module isn't a view. It's `web/self_report.py`: a single source of truth for
> what's broken. Every known issue carries a status — open, resolved, by-design, or unverified — and
> a citation to the record that established it.

**VISUAL:** The ledger table rendering, statuses color-coded.

> **VO:** Two details that matter more than the layout.
>
> First: the test count isn't a number in a file. It's computed by live `unittest` discovery, so the
> interface cannot drift from the suite as the suite grows. Every previous version of that claim in
> the README had gone stale — it said one hundred forty-three tests, in three separate places, and
> was wrong in all three.
>
> Second: the warning above the button that runs a comparison is generated from that ledger, not
> hard-coded. So "this comparator over-flags" appears directly above the thing that over-flags, and
> it updates if that issue's status ever changes.

**VISUAL:** The compare runner, with the generated caveat sitting above the button. Arrow from the
ledger entry to the caveat.

> **VO:** And a halted run renders as "no comparison possible," stating that the contradiction flag
> is `null`, not `false`. Because "couldn't check" and "checked and found nothing" are different
> facts, and that distinction is the whole reason this subsystem exists.

**VISUAL:** Two chips: `null` → "NO COMPARISON WAS POSSIBLE." `false` → "CHECKED. FOUND NOTHING."

---

## 2:30 — CHAPTER 3: CHECKING THE CRITIQUE BEFORE BUILDING FOR IT

**CHAPTER CARD:** 3 · IT WAS WORSE THAN THE CRITIQUE SAID

> **VO:** Version two came from a sharper critique: the layout hides how each agent actually got
> there, and a reader could misread the timeline of the data fetches.
>
> Before designing around that, I went and checked whether it was true. It was — and worse than
> stated.

**VISUAL:** The assumed design: two agent columns, each with its own EDGAR call, running side by
side. It gets a red strike.

> **VO:** The comparison route makes exactly one EDGAR fetch. Not two. Both producers receive the
> identical data object and read different *lenses* over the same payload. And they run
> sequentially — agent A to completion, then agent B — not concurrently.
>
> A tidy symmetric two-column layout would have invented an HTTP request that never happens and a
> concurrency that doesn't exist. It would have looked more professional and been a lie.

**VISUAL:** The corrected four-band layout: setup → one shared spine → two agent columns → verdict.
Band 2 labeled "one payload, reused by BOTH producers."

> **VO:** So the layout renders the real shape. One shared fetch — `lookup_cik` at seven hundred
> sixty-six milliseconds, `fetch_company_facts` at eight hundred twelve — then a fork into two
> columns.
>
> Two things became visible that never had been.
>
> One: the retry path. The validation loop has always retried once on a structural parse failure,
> then halted. Until this UI, that had only ever been *observed* in the test suite's scripted mock
> failures. Now it renders in the HTTP layer with real sequence numbers.
>
> Two: every cited number traced back to that agent's own input. On the real Apple case,
> `$383.266 billion` marks a checkmark — it reconciles to the raw fact `Assets: 383266000000.0`,
> despite completely different formatting. And the `0.34` debt-to-equity ratio marks a warning,
> because it appears nowhere in the input at all.

**VISUAL:** Two provenance rows: `$383.266 billion` ✓ next to `383266000000.0`, and `0.34` ⚠ next
to "not present in input."

> **VO:** That `0.34` is a fabrication. Before this, finding it required a human reading a raw
> reasoning log by hand.

---

## 4:00 — CHAPTER 4: THE REFACTOR THAT WAS SUPPOSED TO DO NOTHING

**CHAPTER CARD:** 4 · ZERO BEHAVIOR CHANGE, PROVEN TWICE

> **VO:** Third session: sixteen modules sat flat at the directory root, importing each other by
> bare name. One of them was called `parser.py`, which shadows a standard library module. There was
> no way to even state a dependency direction, let alone enforce one.
>
> Everything moved into layers. Core, adapters, pipeline, datasources, producers, validation.
>
> The requirement was zero behavior change, and that was verified two ways. The full suite had to
> pass after every one of eight incremental moves, not just at the end. And for the web server —
> which has no automated tests at all — I snapshotted the entire route table and the responses for
> nine calls *before* touching the file, then diffed after every edit. Byte-identical, every time.

**VISUAL:** Eight move-steps in sequence, each with a green suite check. Then the snapshot diff:
`0 differences`.

> **VO:** Three duplications came out, and each one had a specific failure mode it was already
> risking.
>
> The number-extraction regex existed three times, verbatim, each copy carrying a comment asking the
> reader to keep it in sync by hand. All three feed evidence — which figures become claims, which
> count as divergence, which get verified. A drifted copy wouldn't raise an error. It would just
> quietly report a claim it never verified.
>
> A "latest value" helper was duplicated in both producers, and one producer was importing its data
> access from the *other* producer. If those two ever disagreed about what "latest fact" means, the
> comparator would have reported that as a contradiction between the agents — when it was really one
> bug in shared code.
>
> And forty-seven new tests. The one I care about is `test_layering.py`, which reads the imports as
> a syntax tree and fails if a layer reaches somewhere it shouldn't.

**VISUAL:** The three duplications collapsing into one shared module each.

> **VO:** A passing architecture test is worthless if it can't fail. So I broke the layering three
> times on purpose — one import at a time — and confirmed each violation produced a failure naming
> the offending file and line. Then restored it.

**VISUAL:** Three deliberate violations, three named failures, then `RESTORED`.

---

## 5:20 — CHAPTER 5: COUNTING INSTEAD OF GUESSING

**CHAPTER CARD:** 5 · THIRTY-ONE RUNS, LABELED

> **VO:** Which brings us back to the cold open.
>
> "Seven of twelve tickers over-flag" was prose. Anyone who wanted to check it had to re-derive it
> out of SQLite by hand. So all thirty-one real runs this system has ever stored became a versioned
> fixture — each one labeled, and each one replayed through today's actual comparator, not
> hand-predicted.
>
> Sixteen of thirty-one are disjoint-concept false positives. Zero are genuine conflicts.

**VISUAL:** Thirty-one record tiles sorting into labeled buckets. The `genuine_conflict` bucket
stays visibly empty.

> **VO:** And here's the structural reason, which is the actual finding.
>
> Every single flagged run pairs producer A's Assets, Revenues, and Net Income against producer B's
> Earnings Per Share and Operating Income. Those vocabularies never intersect. By design — the
> earnings producer's own docstring says the disjointness is deliberate.
>
> So no amount of tuning the comparator's number-matching can ever produce a genuine-conflict
> finding. The two agents are structurally never asked about the same fact. You cannot detect
> disagreement between two witnesses who were asked different questions.

**VISUAL:** Two vocabulary lists side by side, with an empty intersection in the middle.

> **VO:** The fix, if it's wanted, is upstream of the comparator: link concepts on the extracted
> numbers, or give the two producers genuinely overlapping ones. That wasn't this session's job —
> diagnosis was the ask, not the patch — so nothing in the comparator changed. Eight new tests,
> including one that asserts the zero-genuine-conflicts finding as an executable canary rather than
> a sentence in a document.

---

## 6:20 — CHAPTER 6: TWO THINGS NOBODY HAD MEASURED

**CHAPTER CARD:** 6 · FOUND BY BUILDING THE CORPUS

> **VO:** Building that corpus surfaced two findings that were not written down anywhere — not in
> the run log, not in the docs, not in the ledger.
>
> First. Replay the historic fabrication case — the one run that ever proved this tool catches
> something real — through today's code, and it would not flag today.
>
> Two fixes shipped on the same day back in August. One widened the number regex, which now
> correctly extracts that `0.34`. The other required both agents to have cited at least one number
> before flagging, to cut the false positives. In that run, producer B's side is empty. So the
> second fix suppresses the flag entirely.
>
> Neither fix is wrong on its own. Nobody had replayed that specific case against both of them
> together until this session did.

**VISUAL:** Timeline: two fixes on the same date, converging on one record, which goes dark.

> **VO:** Second. A real extraction bug. The shared regex truncates a large comma-grouped number
> with no currency symbol down to its last digit group. An operating income of thirteen billion,
> nine hundred seventy-one million dollars extracts as the string `"000.0"`.
>
> Confirmed reproducing against today's code, not just against the historical capture.

**VISUAL:** `"13,971,000,000.0"` → `"000.0"` in monospace, with the discarded digits greyed out.

> **VO:** Both went into the ledger as open issues. Neither is fixed.
>
> And while writing this period's own summary, I found a third, smaller one: a ledger entry whose
> detail text had gone stale — it still asserts the old single-adapter behavior as current fact,
> after version two of the UI shipped per-producer model fields. Noted rather than quietly
> corrected, because fixing ledger prose wasn't in scope for the two tasks that were actually asked
> for.

---

## 7:10 — CHAPTER 7: THE HONEST LEDGER

**CHAPTER CARD:** 7 · WHAT'S TRUE NOW, AND WHAT ISN'T

> **VO:** True now that wasn't before this period.

**VISUAL:** List one, building line by line.

> **VO:** The interface calls the comparison route, and leads with the subsystem's own failures
> instead of a demo. The one-fetch-two-lenses design and the sequential execution are rendered
> honestly. The retry path is visible outside the test suite for the first time. A fabricated number
> is findable without reading a raw log by hand. The code sits in enforced layers, with the
> enforcement proven able to fail. The over-flagging claim is now a versioned corpus and eight
> executable tests instead of a sentence. Two hundred twenty-four tests, up from one hundred
> sixty-nine, green at every step.
>
> Still not true.

**VISUAL:** List two, in warning color, held on screen. Do not clear it.

> **VO:** The comparison route, the trace module, and every line of JavaScript have zero automated
> tests. Everything in those first two sessions was verified by hand, in a browser.
>
> None of this week's UI work has ever been exercised against a real language model. No working
> Gemini key, no Ollama running here. Every "verified" claim in those sessions used a mock adapter
> or fixture data.
>
> The retry and halt path is still only observed against scripted mock failures, never a live model.
>
> The over-flagging isn't fixed. The suppressed true positive isn't resolved — that one needs a
> human judgment call, not a patch. The regex bug is still corrupting a real figure every time it's
> hit. Fourteen entries in the ledger now, twelve of them open or unverified, one critical, up from
> eleven at the start of the period. Nothing was resolved this period.
>
> And the largest one: none of this is committed. The last commit in this repository predates all
> four sessions. Fifty-six changed or new files, sitting in a local working tree.

**VISUAL:** `git log` showing the last commit, `c53746a`, with its date. Then a file counter: `56`.

> **VO:** That's not a technical risk I discovered. It's one this project already named after the
> previous period's check, still true, and now bigger.

---

## 7:50 — CLOSE

> **VO:** So here's the smallest true claim I can make about this week.
>
> The interface got honest. The code got layers. And the headline feature got measured, for the
> first time, against every run it has ever produced — and the measurement says it has never once
> caught the thing it was built to catch.
>
> That's not a good week for the feature. It is exactly what the verification layer is for. A tool
> that can't produce evidence against itself isn't a verification tool. It's a demo.
>
> Sixteen flags. Zero conflicts. Written down, versioned, and executable — so the next person
> doesn't have to take my word for it.

**VISUAL:** Back to the cold open. `16 FLAGGED` / `0 GENUINE CONFLICTS`. Below, a cursor blinks
beside `tests/fixtures/cross_agent_real_runs_corpus.json`. Hold. Cut to black.

**END CARD:**
- 16 of 31 stored runs are false positives · 0 are genuine conflicts
- The one confirmed true positive would not flag today
- `/api/compare`, `step_trace.py`, and all JS have zero automated tests
- No UI work this period has run against a live model
- 12 of 14 ledger entries open or unverified · 1 critical
- **Nothing described here is committed** (last commit `c53746a`)
- Corpus labels are AI-assigned and not yet human-reviewed
*source: `logs/RUN_LOG.md` 2026-09-04 (×3) and 2026-09-07 · `divij/work.md`*

---
---

## PRODUCTION NOTES

### Figures to build (D3 v7, per `brutalist/D3.md`)

| # | Figure | Timestamp |
|---|---|---|
| 1 | `sixteen-zero` — the cold-open counter; reused in the close | 0:00, 7:50 |
| 2 | `ledger-table` — self-report entries with statuses, arrow to the generated caveat | 1:20 |
| 3 | `one-fetch-not-two` — the wrong symmetric layout struck through, then the four-band layout | 2:30 |
| 4 | `provenance-rows` — `$383.266 billion` ✓ vs `0.34` ⚠ | 3:30 |
| 5 | `snapshot-diff` — eight move-steps, green suite each time, `0 differences` | 4:00 |
| 6 | `dedup-collapse` — three duplications collapsing into one module each | 4:45 |
| 7 | `layering-violations` — three deliberate violations, three named failures, restored | 5:00 |
| 8 | `corpus-buckets` — 31 tiles sorting; the `genuine_conflict` bucket stays empty | 5:20 |
| 9 | `disjoint-vocabularies` — two concept lists, empty intersection | 5:55 |
| 10 | `two-fixes-one-record` — the suppression timeline | 6:20 |
| 11 | `regex-truncation` — `"13,971,000,000.0"` → `"000.0"` | 6:50 |
| 12 | `uncommitted` — `git log` at `c53746a`, then the count `56` | 7:35 |

After generating: `npm run audit:layout`, then the `ACCURACY-REVIEW.md` pass. Layout first,
accuracy second.

### Fact-check table

Every spoken claim, mapped to its source. Re-walk this against the live files before recording
(guide §9) — several of these numbers move as the suite grows.

| Claim in VO | Source |
|---|---|
| 16 of 31 disjoint-concept false positives; 0 genuine conflicts | `logs/RUN_LOG.md` 2026-09-07, Result; diagnosis doc |
| 31 runs replayed through today's code via `fixture_adapter` | `logs/RUN_LOG.md` 2026-09-07, Commands |
| Historic true positive `f4a4c782` would not flag today | `logs/RUN_LOG.md` 2026-09-07, Result (new finding 1) |
| Both-sides-non-empty gate is the suppressing mechanism | same entry (`bool(a_set) and bool(b_set)`) |
| `"13,971,000,000.0"` → `"000.0"`, run `515f263a` | `logs/RUN_LOG.md` 2026-09-07, Result (new finding 2) |
| "7 of 12 tickers" was the prior, unmeasured claim | `logs/RUN_LOG.md` 2026-09-04 (UI v2), Open issues |
| §3.4 verbatim quote ("completely unmodified") | `divij/cross-agent-validation-status.md` §3.4 |
| Backend routes existed since 2026-08-28 | `logs/RUN_LOG.md` 2026-09-04 (UI v1), Recipe |
| Test count from live `unittest` discovery, not hard-coded | `logs/RUN_LOG.md` 2026-09-04 (UI v1), Outputs |
| README's stale "143 tests" claim, wrong in three places | `logs/RUN_LOG.md` 2026-09-04 (SOLID), Also fixed |
| Caveat above the compare button generated from the ledger | `logs/RUN_LOG.md` 2026-09-04 (UI v1), Result |
| Halt renders `contradiction_flag: null`, not `false` | same entry, Result |
| Exactly one EDGAR fetch; both producers get the identical `DataSource`; sequential not concurrent | `logs/RUN_LOG.md` 2026-09-04 (UI v2), "Verifying the critique" |
| `lookup_cik` 766ms, `fetch_company_facts` 812ms | same entry, Result |
| ADR-07 retry rendered in the HTTP layer for the first time | same entry, Result |
| `$383.266 billion` ✓ reconciles to `Assets: 383266000000.0`; `0.34` ⚠ | same entry, Result |
| 16 flat root modules; `parser.py` shadowed a stdlib name | `logs/RUN_LOG.md` 2026-09-04 (SOLID), Recipe |
| Eight incremental moves, suite green after each | same entry, Commands |
| Byte-identical route/response snapshot across nine calls | same entry, Commands |
| Regex duplicated three times with "keep in sync" comments | same entry, Outputs (duplication 1) |
| `_latest_value` duplicated; one producer imported from its sibling | same entry, Outputs (duplication 2) |
| +47 tests (169 → 216); `test_layering.py` is AST-read | same entry, Outputs — tests |
| Three deliberate layering violations each produced a named failure | same entry, Result |
| +8 tests (216 → 224); zero-genuine-conflicts asserted as a test | `logs/RUN_LOG.md` 2026-09-07, Outputs |
| 224 tests passing | re-run at drafting: `python -m unittest discover -s tests -t .` → OK |
| Earnings producer's docstring calls the disjointness deliberate | `logs/RUN_LOG.md` 2026-09-07, Result |
| Zero tests on `/api/compare`, `step_trace.py`, JS | all four entries, Open issues |
| No live-model run of this period's UI work (no Gemini key, no Ollama) | `logs/RUN_LOG.md` 2026-09-04 (UI v2), Open issues |
| Retry/halt observed only via `mock_adapter.py` | weekly update §8; `retry-halt-unproven` |
| 14 ledger entries, 12 open/unverified, 1 critical, up from 11 | weekly update §7 |
| Stale `http-no-model-override` detail text | weekly update §6.4 |
| Nothing committed; last commit `c53746a`; 56 changed/new files | `git log`, `git status --short -- verification-layer \| wc -l` |
| Corpus labels are AI-assigned, unreviewed | `logs/RUN_LOG.md` 2026-09-07, Open issues |

### Things this script deliberately refuses to say

Considered and rejected, per guide §6:

- **"The UI is done" / "shipped."** Nothing is committed. The script says "sitting in a local
  working tree" and names the commit hash. It never uses "shipped" for this period's work.
- **"The comparator now catches fabrications."** The provenance markers made one fabrication
  *visible in the interface*. The comparator's own rule is untouched, and the fabrication ledger
  entry `fabrication-not-caught` is still OPEN. Nearly wrote "now catches" in chapter 3 — cut.
- **"We fixed the over-flagging."** Diagnosis was the ask. `validation/cross_validation.py` and
  `core/numeric.py` were not modified this period, and the script says so.
- **"The refactor improved the system."** It was required to change nothing observable, and the
  proof of that is the byte-identical snapshot. Framing a no-op as an improvement would invert the
  actual achievement.
- **"224 tests" as evidence of correctness.** The script uses the count as a delta, never as proof.
  Three of the largest surfaces in this period have zero tests, and that's chapter 7.
- **Any implication the retry path is proven.** It is *rendered* now. It has still never been
  observed against a live model — capability vs. observation, stated as two facts (guide §5).
- **"Zero for sixteen means the tool doesn't work."** Also an overclaim, in the other direction.
  It means the two producers were never asked the same question. The script says that explicitly
  rather than letting the hook stand as a verdict on the comparator.

### If the runtime needs to shrink (to ~6:00)

Cut in this order: (1) chapter 4's duplication detail — keep the byte-identical snapshot and the
deliberate layering violations, drop the `_latest_value` and adapter-construction cases; (2) the
`766ms` / `812ms` timings in chapter 3; (3) the third, smaller stale-ledger finding at the end of
chapter 6.

**Never cut chapter 7**, and never cut the "nothing is committed" beat inside it. Removing the
honest ledger under time pressure is the exact overclaim-by-omission this format exists to prevent,
and the uncommitted state is the single most consequential fact in the period.

### If the runtime needs to grow (to ~12:00)

Add: (1) a full walkthrough of the five corpus labels and what each one means, which is the most
teachable artifact of the period; (2) the `_REL_TOL` of 0.1% as a worked example of a judgment call
disclosed as a judgment call — it absorbs real restatement rounding but has never been tuned
against data; (3) how the provenance markers were verified, since the mock adapter emits no numbers
at all — `window.fetch` stubbed for one route while driving the *real* render path, which is a good
concrete beat on the difference between testing shipped code and testing a re-implementation of it.
