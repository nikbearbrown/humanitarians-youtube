# Video Script — "The Number That Wasn't There" (Vox-style weekly update)

**Subject:** Cross-Agent Validation's first live run, everything it found, and what got fixed —
covering 2026-08-28 → 2026-08-29. Third video in the series; a follow-up to
`video-script-cross-agent-validation.md` (the v1 build) and the prior draft of this file (the
fixture-to-real-producer swap). Assumes the viewer has seen at least one prior video; a compressed
recap covers both.
**Target runtime:** ~10:40 (≈1,600 words of actual VO at ~150 wpm — counted from the draft below).
This is a deliberately expanded cut: Chapter 3 now walks all five verification tests in full detail
(what each test is, why it was run, what a clean result should look like, the exact parameters
used, what actually happened, and what that means) rather than the ~95-second summary in the
original draft. This supersedes that draft's own "expand to 9–10 minutes" note — this cut goes
slightly past it because the parameter-level detail was requested explicitly. See the "If you need
to cut" section for a path back to something closer to the original 6:20 runtime if that's needed
for a different format.
**Sources:** `logs/RUN_LOG.md`, all entries dated 2026-08-28 and 2026-08-29 (nine entries across
the two days); `work.md`, all matching entries; `divij/model-test-report-2026-08-29.md` (both the
original and its "Update" section); `divij/sdd.md` Open Question 1; `divij/cross-agent-validation-proposal.md`
§6.4; `cross_validation.py`, `claims.py`, `consistency.py`, `verification.py`,
`run_cross_agent_live.py`, `adapters/ollama_adapter.py`, `middleware.py`.
**Confirmed directly against this checkout's live source** (see `SOURCES.md` for the full pass):
`claims.py`'s and `consistency.py`'s and `verification.py`'s shared quantitative-number regex
(no bare-decimal case); `adapters/ollama_adapter.py`'s default `temperature=0.0, seed=42`;
`middleware.py`'s retry-then-halt structure. **Not confirmed from this checkout** (file absent —
see `SOURCES.md`): the exact run parameters actually used for the specific test batch (whether the
adapter's defaults were used unmodified, or overridden), the literal `RUN_LOG.md` entries, and
`work.md`. Narration below states adapter *defaults* as confirmed code facts and is careful not to
assert that the live run necessarily used them unmodified — flagged plainly in the relevant beat.
**Git state at time of writing:** all of this period's changes are written, tested, and logged,
**not yet committed** (`git status` would show them modified/untracked). Say "written and tested,"
never "shipped," for anything from this period.

**Style rules for the read:** short declaratives. One idea per sentence. The turn word is "but."
Never let the narration claim more than the logs support. State capability vs. observation as two
separate facts wherever both matter — this is the one system in the project whose whole premise
requires that distinction to be kept explicit. **New for Chapter 3:** every test gets the same
six-part treatment, spoken AND shown on screen as a card: WHAT IT IS → WHY WE RAN IT → WHAT A GOOD
RESULT LOOKS LIKE → PARAMETERS → WHAT ACTUALLY HAPPENED → WHAT IT MEANS. Don't skip a field even
when the answer is short — a one-clause "what it means" is still a field, not an omission.

---

## 0:00 — COLD OPEN

> **VO:** Two weeks ago, this project built something that runs two AI agents on the same company
> and flags when their numbers disagree.
>
> Last week, both agents finally became real.
>
> This week, it ran for the first time. And the first thing it produced wasn't a disagreement.
>
> It was a number that came from nowhere.

**VISUAL:** A thought_log excerpt fades in, one line at a time: *"Calculated the debt-to-equity
ratio as 0.34 [SOURCE: SEC Filings, https://www.sec.gov/]."* The citation link pulses, then a red
X stamps over it.

**TITLE CARD:** THE NUMBER THAT WASN'T THERE
**SUBTITLE:** Cross-Agent Validation — the first live run

---

## 0:22 — RECAP (two prior videos, compressed)

**CHAPTER CARD:** 1 · SIXTY SECONDS ON WHAT ALREADY EXISTED

> **VO:** Fast version. Cross-Agent Validation runs two independently-reasoning agents on one
> company, pulls the numbers out of each conclusion, and flags anything that doesn't match. Set
> arithmetic — no model, no judge.
>
> It started with one real agent and one fixture — a hand-written stand-in you configure with
> whatever answer you want, used on purpose to prove the detector works before pointing it at
> anything real. Last week, the fixture was replaced with a second real grader reading the same
> SEC filing through a different lens: balance sheet versus earnings quality.
>
> A hundred forty-three tests passed. Zero lines changed in the comparator itself. But nobody had
> actually watched two real agents talk to each other yet.

**VISUAL:** Quick two-panel: "FIXTURE" crossed out, replaced by "EARNINGS_GRADER.PY — REAL SEC DATA."
Then a grey chip: OBSERVED — still empty.

---

## 1:08 — CHAPTER 2: THE FIRST LIVE RUN

**CHAPTER CARD:** 2 · WHAT HAPPENED THE FIRST TIME IT ACTUALLY RAN

> **VO:** The second agent ran on a model set up locally. Once it ran: real filing data went in. A
> real independent model came back with a conclusion for each side.
>
> Producer A, reading assets, revenue, and net income, wrote: *"Calculated the debt-to-equity
> ratio as 0.34."* Its input data contained no debt and no equity figures. Not close, not derived —
> the concept wasn't in the data at all.

**VISUAL:** Split screen. Left: the three real numbers Producer A was actually given (Assets,
Revenues, NetIncomeLoss). Right: the invented line, "debt-to-equity ratio as 0.34," with a
question-mark icon where its source data should be.

> **VO:** Producer B, reading real earnings figures, cited zero numbers. It described them —
> "consistent," "significantly large" — but never wrote one down.
>
> The system flagged a contradiction. It was right to. But not for the reason you'd hope.

---

## 2:06 — CHAPTER 3: FIVE TESTS, IN FULL

**CHAPTER CARD:** 3 · TESTING THE THING THAT JUST HAPPENED

> **VO:** One surprising result could be noise. So five separate tests ran against it — not a quick
> pass or fail on each, but the full treatment: what the test is, why it was run, what a clean
> result should look like, exactly what was fed into it, what actually came back, and what that
> means. Here's all five.

**VISUAL:** A blank five-slot scorecard appears — TEST 1 through TEST 5, all greyed out, waiting to
fill in one at a time.

### Test 1 — Claim Verification

> **VO:** Test one: claim verification. Here's what it is — for every citation in a thought_log
> that points at a real URL, this mechanism fetches that source and checks whether the numbers
> being claimed actually appear in it, within one percent tolerance.
>
> Here's why it exists: this is the system's dedicated defense against exactly this failure — a
> citation that looks real but isn't backed by what it points to.
>
> Here's what a clean result looks like: a true number should confirm against the source. A
> fabricated number should come back checked-and-not-found. Either outcome means the mechanism is
> doing its job — a hundred percent pass rate isn't the goal, a hundred percent honest verdict is.
>
> Here's what it was actually given: the citation under test was the debt-to-equity line, pointing
> at the same SEC filing already fetched for Producer A's real inputs.
>
> Here's what happened: verification never got the chance to check that number at all. One layer
> upstream, claim extraction only recognizes figures shaped like a dollar amount, a percentage, a
> multiple, or basis points. A bare decimal ratio — 0.34, no symbol attached — matched none of
> those patterns. It was invisible before verification ever ran.
>
> Here's what it means: a verification layer is only as reliable as what gets handed to it. A gap
> in extraction can silently starve a working checker of the one claim it most needed to see.

**VISUAL:** Test-card fills in: WHAT — fetch + match source. WHY — catch fake citations. GOOD
RESULT — honest confirm/not-found. GIVEN — the debt-to-equity citation + its SEC source, 1% tolerance.
HAPPENED — extraction never captured "0.34" (regex: `$…|…%|…x|…bps`, no bare-decimal case).
MEANS — the checker was starved upstream, not broken itself. Scorecard slot 1 fills: grey → amber
("upstream gap").

### Test 2 — Determinism

> **VO:** Test two: determinism. What it is — run the identical question through the identical
> model, same temperature, same fixed seed, five separate times, and compare all five answers.
>
> Why it matters: it separates two very different problems. A wrong answer that changes every time
> is noise — annoying, but survivable. A wrong answer that repeats identically is a stable pattern
> in the model's reasoning — worse, but at least diagnosable.
>
> What a clean result looks like: either all five converge on the same, hopefully correct, answer —
> or, if something's wrong, the same wrong answer keeps recurring, because a repeatable failure is
> one you can actually target.
>
> What was actually given: the project's own local-model adapter defaults to temperature zero and a
> fixed seed of 42 — that part is confirmed straight from the adapter's source code. Whether this
> specific run used those defaults unmodified isn't independently confirmed from this checkout —
> flagged plainly, not glossed over.
>
> What happened: four of the five runs converged on the same invented pair of ratios, off by one
> digit in the last decimal place. The original debt-to-equity number — the one from the first
> run — never came back across the other four.
>
> What it means: fixing temperature and seed narrows the model's behavior, but doesn't collapse it
> to one single deterministic answer — there's still an outlier. And the outlier was exactly the
> fabrication this video is about. Seen only once, it would have looked like the model's normal
> behavior instead of the one time it strayed furthest from it.

**VISUAL:** Test-card fills in: WHAT — same input, 5x. WHY — noise vs. stable pattern. GOOD RESULT —
converge, or repeat the same failure. GIVEN — temp 0 (code-confirmed default), seed 42
(code-confirmed default, this-run use unconfirmed). HAPPENED — 4-of-5 clustered, 1 outlier never
repeated. MEANS — narrows but doesn't collapse behavior; the fabrication was the outlier. Five
response bubbles: four cluster together glowing the same color, one sits apart labeled "ORIGINAL —
NEVER REPEATED." Scorecard slot 2: grey → amber ("real gap, but informative").

### Test 3 — Consistency Probe

> **VO:** Test three: the project's own consistency probe — a separate mechanism from determinism,
> built for exactly this situation. What it is: run a second, fully independent pass on the same
> input, then score how much the two conclusions actually overlap — words, weighted lightly at
> point-four, specific numbers, weighted heavily at point-six, because a real number is much harder
> to fabricate identically twice than a general phrase is.
>
> Why it exists: unlike verification, it needs no external source at all — genuine reasoning from
> real evidence should converge across independent runs on its own.
>
> What a clean result looks like: high agreement, and — this is the important part — a specific
> hard flag the moment any number shows up in one run and never in the other, no scoring required.
>
> What it was given: the same subject, the same agent identity, a fresh independent run, weights
> of 0.4 on word overlap and 0.6 on number overlap.
>
> What happened: the debt-to-equity figure appeared exactly once across every run collected —
> never a second time. The hard divergence flag fires exactly the way it's designed to.
>
> What it means: of all five tests here, this is the one that worked precisely as intended, with no
> workaround needed. It didn't need to know anything about the real world. It only needed the
> fabrication to fail at being consistent with itself — and it did.

**VISUAL:** Test-card fills in: WHAT — second independent pass, scored overlap. WHY — catch drift
without needing outside truth. GOOD RESULT — high agreement, or a hard flag on divergence. GIVEN —
weights 0.4 word / 0.6 number. HAPPENED — number appeared once, never repeated → flag fires. MEANS —
worked as designed, no gap. Scorecard slot 3: grey → green ("worked as intended").

### Test 4 — Guardrail Stress Test

> **VO:** Test four: a guardrail stress test, and it's the odd one out — it isn't testing whether
> the agents are *right*. It's testing whether they can even speak the required format at all.
>
> Why that matters on its own: every other test here assumes the response actually parsed into a
> valid structure to begin with. If that layer breaks, nothing downstream even runs.
>
> What a clean result looks like: a first-attempt parse success rate at or near a hundred percent,
> and zero forced halts — proof the format-enforcement layer holds up against real, not
> fixture-generated, model output.
>
> What it was given: twenty-four real calls across the live batch, the same directive version each
> time, first attempt only counted — a retry wouldn't count as a clean pass.
>
> What happened: twenty-four for twenty-four. Zero retries triggered. Zero halts.
>
> What it means: whatever else is wrong this week, it isn't the format layer. That part held
> perfectly, at least at this sample size. The failure lives entirely in what the model reasoned,
> not in whether it could describe that reasoning in the shape the pipeline requires.

**VISUAL:** Test-card fills in: WHAT — structural parse check, not content check. WHY —
everything downstream depends on this layer. GOOD RESULT — ~100% first-try parse, 0 halts. GIVEN —
24 real calls, first attempt only. HAPPENED — 24/24, 0 retries, 0 halts. MEANS — format layer solid;
failure is in content, not structure. Scorecard slot 4: grey → green ("held").

### Test 5 — Breadth Test

> **VO:** Test five: breadth. What it is — run the same two-producer comparison across twelve
> different real companies, not just the one from the first live run.
>
> Why: one company could be a fluke — an unusual filing, a missing field, anything. Testing across
> a spread of real companies is what tells you whether a pattern is general or a one-off.
>
> What a clean result looks like: flags that correlate with actual factual contradictions — a low
> false-positive rate across a genuinely diverse batch of real filings.
>
> What it was given: twelve real tickers, real SEC filings pulled for each, both producers run per
> company, the existing contradiction flag left completely unmodified.
>
> What happened: eleven of twelve got flagged. The one exception was the single company where
> neither agent cited a number at all — nothing to compare, so nothing to flag. And manually
> checking one of those eleven flagged cases showed both agents were completely correct — one
> reported assets and revenue, the other reported earnings per share. Different concepts, zero
> actual conflict, and the flag fired anyway.
>
> What it means, and this is the part that actually redirected the project this week: eleven out of
> twelve looked like an alarming contradiction rate at first glance. It was actually revealing that
> the flag can't yet tell the difference between two agents disagreeing and two agents simply
> talking about different things.

**VISUAL:** Test-card fills in: WHAT — same comparison, 12 companies. WHY — rule out a one-company
fluke. GOOD RESULT — flags track real contradictions. GIVEN — 12 tickers, flag unmodified. HAPPENED
— 11/12 flagged, 1 clean case inspected shows false-positive. MEANS — flag conflates disagreement
with topical non-overlap. Twelve ticker tiles: eleven flip to red, one — the zero-numbers company —
stays grey. Scorecard slot 5: grey → red ("real gap found").

> **VO:** Five tests. One upstream extraction gap, one informative outlier, one mechanism that
> worked exactly as designed, one clean structural pass, and one real, project-redirecting flaw in
> what the flag actually measures.

**VISUAL:** Full scorecard, all five slots filled and colored: amber, amber, green, green, red.

---

## 8:02 — CHAPTER 4: TWO FIXES, ONE LEFT DELIBERATELY OPEN

**CHAPTER CARD:** 4 · WHAT GOT FIXED, AND WHAT DIDN'T

> **VO:** The missing-number problem — Test 1's gap — turned out to be duplicated in three separate
> files, not one. The same regex, copied three times, all with the same blind spot. All three got
> widened the same way — an unfixed duplicate left behind would have been worse than not fixing it
> at all.

**VISUAL:** Three file names — `claims.py`, `consistency.py`, `verification.py` — each with an
identical highlighted line, all three updated in sync.

> **VO:** Test 5's problem needed an actual decision, not a patch. The honest constraint: nothing
> in this system currently knows which real-world concept a number came from — only that a number
> exists. So a genuinely complete fix wasn't available without much bigger changes.
>
> The decision that shipped: a number cited by only one side no longer counts as a contradiction
> by itself. That fixes the case where one agent simply wasn't asked about something.
>
> It does not fix two agents citing real, correct, unrelated numbers. That gap is named in the
> code, tested as a known limit, and left open on purpose — not quietly dropped.

**VISUAL:** Text on screen, verbatim from the test report: *"a mismatch between two design
decisions that had never been tested against each other with real data before this run."*

---

## 9:04 — CHAPTER 5: CHECKING THE FIX AGAINST REAL DATA

**CHAPTER CARD:** 5 · DOES THE FIX ACTUALLY HELP

> **VO:** The fix wasn't just tested against hand-built examples. It was checked against the same
> twelve real companies from Test 5, recalculated, not re-run.
>
> Under the old rule: eleven of twelve flagged. Under the new rule: seven of twelve. Four
> companies — where one agent simply hadn't quantified anything — stopped being false alarms.
> The other seven, where both agents cited real numbers about different things, are still flagged.
> That's the honest, measured size of the fix. Not everything. Something specific and countable.

**VISUAL:** A bar drops from 11 to 7, with four ticker tiles shown turning from red to grey.

---

## 9:36 — HONEST LEDGER

**CHAPTER CARD:** 6 · SO, DOES IT WORK

> **VO:** Two separate questions, two separate answers.
>
> Does the machinery work — real filings, real independent reasoning, a full audit trail, a
> guardrail that held on every one of twenty-four real calls? Yes. Provably, not just
> theoretically.
>
> Does the flag reliably mean "these two agents disagree"? Not yet. Most of what it flags right
> now is agents discussing different things, not agents contradicting each other. And the one real
> fabrication this system produced was caught by a person reading the output, not by the system
> itself.

**VISUAL:** Two chips again. INFRASTRUCTURE — solid green. JUDGMENT — half-filled, labeled "NOT YET PROVEN."

---

## 10:10 — CLOSE

> **VO:** A system built specifically to distrust fluent, confident answers just produced one —
> and then ran five separate tests on itself to measure exactly how wrong it was, instead of
> hiding it.
>
> That's not a finished detector. It's a detector that's now told on itself, twice, in two days —
> once about a number, once about what its own flag actually measures.
>
> The smallest true claim, not the biggest: this proved the plumbing. It did not yet prove the
> judgment.

**VISUAL:** The debt-to-equity line from the cold open returns, now stamped: CAUGHT BY A HUMAN, NOT THE SYSTEM. Cut to black.

**END CARD:**
Cross-Agent Validation, first live run · 5 tests run in full: upstream gap / informative outlier /
worked as designed / structural pass / real flag limitation · contradiction flag: 11/12 → 7/12
after the fix · disjoint-concept false positives still open · source: `logs/RUN_LOG.md`
2026-08-28/29, `divij/model-test-report-2026-08-29.md`, `adapters/ollama_adapter.py`

---

## PRODUCTION NOTES

### Figures to build (D3 v7, per `brutalist/D3.md`)

| # | Figure | Used at |
|---|---|---|
| 1 | `unsourced-number` — thought_log line with citation stamped X | 0:00, 10:10 |
| 2 | `recap-two-panel` — fixture crossed out / real grader in; empty OBSERVED chip | 0:22 |
| 3 | `input-vs-invented` — Producer A's real 3 inputs vs. the invented ratio | 1:08 |
| 4 | `test-scorecard` — 5-slot scorecard, fills in one test at a time across Ch. 3 | 2:06 (persistent through Ch. 3) |
| 5 | `test-card-template` — reusable 6-field card (WHAT/WHY/GOOD RESULT/GIVEN/HAPPENED/MEANS), one instance per test | 2:06–8:02, ×5 |
| 6 | `regex-gap` — the pattern with the missing bare-decimal case | Test 1 |
| 7 | `five-bubbles-cluster` — 4 clustered responses + 1 outlier | Test 2 |
| 8 | `twelve-tiles-flag` — 12 tickers, 11 flip red, 1 stays grey | Test 5 |
| 9 | `three-files-synced` — claims/consistency/verification, same fix landing in all three | 8:02 |
| 10 | `eleven-to-seven` — bar drop with 4 tiles flipping red→grey | 9:04 |
| 11 | `two-chips-final` — infrastructure solid, judgment half-filled | 9:36 |

Run `npm run audit:layout` after generating, then the `ACCURACY-REVIEW.md` pass — layout first,
substance second.

### Fact-check pass before recording

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
`divij/model-test-report-2026-08-29.md`, `divij/sdd.md` are absent from this checkout, its git
history, and the one other worktree present on this machine. Every claim sourced only to those
files (all the specific run figures: the exact thought_log text, the 4-of-5 clustering, the 24/24
count, the 11/12 and 7/12 counts) is carried as *reported*, not independently re-verified. Claims
sourced to files that DO exist here (`claims.py`, `consistency.py`, `verification.py`,
`financial_grader.py`, `adapters/ollama_adapter.py`, `middleware.py`) have been read directly and
are confirmed. A human with access to the actual run environment should confirm the unconfirmed
rows before Gate P sign-off.

### Things this script deliberately refuses to say

- That the system "caught" its own fabrication. It didn't — a person read the thought_log. Said
  plainly, twice (cold open payoff and honest ledger).
- That 24/24 and 11/12 are stable rates for "this model" in general. They're measured results on
  a specific, still-small sample (24 agent-runs, 12 tickers) — real, but not yet large enough to
  generalize from. The honest ledger says "not yet proven," not "proven small."
- That fixing the presence/absence false positive fixes the flag. It fixes four of eleven cases on
  this dataset. Seven remain, and the script says so with the same number, not a vaguer "some
  remain."
- That this is a finished, working contradiction detector. It's a detector that has now been
  pointed at real data once, found to work mechanically and to not yet work semantically, and
  partially patched. The close says "proved the plumbing, not the judgment" specifically to avoid
  rounding this up to "it works now."
- **New:** that the exact parameters used in this specific test batch (seed, temperature, model
  version) are confirmed facts. Only the *adapter's defaults* are confirmed, from live code. Test
  2's narration says this explicitly rather than presenting an inferred parameter as an observed one.

### If you need to cut to ~6:20 (closer to the original draft's length)

Compress Chapter 3 back down: keep the six-field structure but drop to one sentence per field
instead of two—three, and cut Test 4 (the guardrail stress test) to a single combined line inside
Test 5's setup ("format held across all of this — 24/24, zero halts — so every failure below is a
content failure, not a structural one"). This gets Chapter 3 back to roughly 90–110 seconds while
keeping all five tests nominally present. Do not drop the "what it means" field for any test even
in the compressed cut — that field is where the actual argument of the video lives.

### If you need to expand further (12+ minutes)

Add: the exact WSL/venv debugging detour (symlink resolution on a Windows-mounted drive) as a
short "even getting the test to run was its own small lesson in environment isolation" beat; a
walkthrough of the `qwen2.5:7b` model choice and hardware constraints (16GB RAM, ~4-6GB VRAM) as
context for why a 7B local model was the right tradeoff; and a beat on JPM's Producer B, which
correctly wrote "the lack of reported OperatingIncomeLoss is noteworthy" instead of inventing a
number — the one clear case of the model doing the right thing under missing data, worth
including so the video doesn't read as uniformly damning.
