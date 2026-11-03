# Mycroft 7 — "Fifteen Of Sixteen"

**Type:** periodic update (per `divij/video-script-writing-guide.md` §1)
**Runtime target:** 8:57 · ≈1,343 words of VO at ~150 wpm (written first, timed after — see guide
§7; this period's content matched Mycroft 6's density more than the initial 6:30 estimate assumed,
and grew again once the "how we know 15/16 is real" methodology beat was added to chapter 2, so the
target was corrected to the actual draft rather than the draft cut to fit a pre-set number)
**Covers:** 2026-09-11, both sessions — the concept-linkage prototype + the first overlapping-concept
live test, then wiring the fix into production the same day
**Sources read before drafting:** `logs/RUN_LOG.md`'s two entries dated 2026-09-11 (in full);
`divij/work.md`'s matching entries; `web/self_report.py` (`build_self_report()` run directly for
current ledger status and test count — not quoted from memory of an earlier turn); `git log` /
`git status`.
**Suite state at drafting:** re-ran `python -m unittest discover -s tests -t .` → **242 tests, OK**.
**Sequel to:** `Mycroft6_DivijPawar_09-07-2026_zero-for-sixteen` — this script assumes that video's
recap chapter is common knowledge and does not re-teach it.
**Visual system:** `brutalist/DESIGN.md` tokens, `brutalist/D3.md` (D3 v7, `var(--color-*)`).

**Style rules (guide §5):** short declaratives, one idea per sentence, "but" is the turn word, no
rounding for rhythm, and capability is never narrated as observation.

---

## 0:00 — COLD OPEN

> **VO:** Last video ended on a number. Zero for sixteen. Zero real conflicts, out of sixteen
> flagged runs.
>
> This video, the fix landed. Fifteen of those sixteen false positives — gone.

**VISUAL:** The `16 FLAGGED` / `0 GENUINE CONFLICTS` card from the prior video, held for one beat.
Then `15 KILLED` stamps over the sixteen in accent color, with `1` left circled.

> **VO:** But the test built to prove that fix actually works found something else instead. Two
> agents, given the exact same data. One of them didn't read it. It invented a different quarter,
> for a filing that doesn't exist, and cited a source URL nobody gave it.

**VISUAL:** Two identical context blocks side by side, both showing real Apple financial data.
One agent's output overlays real figures. The other's overlays a fabricated fiscal quarter and a
struck-through fake URL.

> **VO:** That's not a comparator bug. That's a model that doesn't do the reading.

**TITLE CARD:** FIFTEEN OF SIXTEEN
**SUBTITLE:** Mycroft 7 · 2026-09-11

---

## 0:36 — CHAPTER 1: THE TWO THREADS LEFT OPEN

**CHAPTER CARD:** 1 · WHAT LAST WEEK LEFT UNRESOLVED

> **VO:** Quick recap, for anyone new. Sixteen of thirty-one real runs this tool ever produced were
> false positives — two agents flagged as disagreeing when they'd simply been asked about different
> things. Zero were real conflicts.
>
> The diagnosis named two ways forward. Link each number to the concept it came from, so the
> comparator stops comparing apples to someone else's oranges. Or actually test whether two agents
> can ever be shown the *same* fact — because nothing in thirty-one runs had put them in that
> position.
>
> One day. Both threads. In that order.

**VISUAL:** Two paths branching from last week's closing card: `LINK CONCEPTS` and `TEST OVERLAP`.

---

## 1:12 — CHAPTER 2: TEACHING THE COMPARATOR WHAT A NUMBER MEANS

**CHAPTER CARD:** 2 · TAG THE NUMBER, NOT JUST THE DIGITS

> **VO:** The idea is simple to say. Every number a producer cites gets tagged with the concept it
> came from — Assets, Revenue, Diluted Earnings Per Share. If a number's concept could never
> plausibly come from the other producer, its absence there stops counting as a disagreement.
>
> The two producers' concept lists don't overlap at all, by design. So a tagged number is excluded
> from comparison entirely. Only the untagged ones — bare ratios with no label nearby — still get
> compared the old way.

**VISUAL:** A conclusion sentence with each number getting a colored tag: `Assets`, `Revenue`, and
one number left grey — untagged.

> **VO:** Three bugs surfaced before the numbers could be trusted. A decimal point inside a figure
> was mistaken for the end of a sentence, which hid a concept label sitting earlier in the same real
> sentence. The tagger only recognized natural-language phrasing — "diluted EPS" — and missed that
> the actual prompt format is the raw label itself, "EarningsPerShareDiluted," which models echo
> back verbatim. And distance to a label was measured from its *start*, not its *end* — which
> mis-matched two numbers named together in one sentence, closest label winning for the wrong one.
>
> All three caught by tests before the measurement was trusted.

**VISUAL:** Three bug cards, each struck through with `FIXED` and a one-line cause.

> **VO:** Then the actual test. Not a new example built to prove the point — the sixteen real runs
> already sitting in last week's labeled record, the ones already flagged as false positives.
> Replay all sixteen through the new rule and count what's left.

**VISUAL:** The sixteen labeled record tiles from last video, filing one at a time through a gate
labeled `concept_aware`.

> **VO:** Fifteen stop flagging.
>
> The sixteenth doesn't — and that's the one where a number really was fabricated. It's supposed to
> still flag. Zero new false positives anywhere else in the corpus.
>
> Checked twice, not once. Once against the tagging logic by itself. Then again through the exact
> function the live comparison route actually calls — to confirm that wiring it in didn't quietly
> change the answer on the way.

**VISUAL:** Two check panels side by side: `MODULE, DIRECT: 15/16` and `PRODUCTION API: 15/16`,
both landing on the same number.

> **VO:** Fifteen of sixteen real false positives, killed. The one survivor is the one confirmed
> real catch on record — a fabricated number this tool has ever actually caught.

**VISUAL:** The `15 KILLED` / `1` card again, now labeled: the 1 is `TRUE POSITIVE, PRESERVED`.

---

## 3:23 — CHAPTER 3: THE TEST THAT HAD NEVER BEEN RUN

**CHAPTER CARD:** 3 · SAME DATA, TWO MODELS

> **VO:** Here's the test nothing in thirty-one runs had ever performed. Give both agents the exact
> same evidence — not two different lenses on one company, the identical numbers — and see if a real
> disagreement can even happen.
>
> Two local models. Same prompt, same data, same directive. Four runs: Apple twice — once with the
> models in each role, to rule out a role effect rather than a model effect — Microsoft, Nvidia.

**VISUAL:** One shared context block, forking into two model icons: `qwen2.5:7b` and `mistral-7b`.

> **VO:** Four for four, flagged. The first time this flag has ever fired on evidence both sides
> actually saw.
>
> But not because the two models disagreed about a number. In three of the four runs, one model
> cited zero of the real figures. It invented a fiscal quarter that isn't in the data and a source
> URL nobody gave it.

**VISUAL:** The real Apple context on the left. On the right, the fabricated quarter and struck-out
URL, with a red `0 REAL NUMBERS CITED` stamp.

> **VO:** In the fourth run — roles swapped, so this isn't about which seat the model sat in — it did
> read the real numbers. And still turned a real one hundred one billion, four hundred sixty-four
> million dollars of net income into a "net income loss" of negative one hundred one million. Wrong
> sign. Wrong by a factor of a thousand.
>
> The other model got every real figure right, all four times. It just wasn't clean either — it also
> added a return-on-equity number that appears nowhere in what it was given.

**VISUAL:** Split scoreboard: model A — 4/4 correct figures, 1 unsupported ratio added. Model B —
0/4 runs grounded in real data.

> **VO:** So the mechanism works. It found a real problem. Just not the one it was built to find.

---

## 5:00 — CHAPTER 4: FROM DIAGNOSIS TO PRODUCTION, SAME DAY

**CHAPTER CARD:** 4 · WIRING THE FIX IN

> **VO:** A second session, same day, turned the measurement into a decision: ship it. The live
> comparison route now runs the concept-aware check by default, not the old rule.
>
> Two things came along for free.

**VISUAL:** `/api/compare` route diagram, old rule struck through, new rule wired in.

> **VO:** First — the old rule had its own quiet failure. It required both agents to cite at least
> one number before flagging anything, which is what suppressed that one confirmed true positive in
> the first place. The new rule never had that requirement. Switching to it fixed a second, separate
> bug, with no extra code.
>
> Second — a real extraction bug, found while building last week's corpus: a large number with commas
> and no dollar sign was getting truncated to its last three digits. Thirteen billion, nine hundred
> seventy-one million dollars was extracting as the string zero-zero-zero point zero. Fixed, and
> confirmed against the real historical case, not just a new example built to pass.

**VISUAL:** `"13,971,000,000.0"` crossing out `"000.0"`, replaced with the corrected full string.

> **VO:** And the fabrication check that already existed for single-agent chats — extract every claim
> a model makes, check it against its own cited source — had never once been connected to this
> comparison route. It is now. Replayed against the exact historic fabrication, not a clean example:
> the citation supports none of the numbers under it. A real, automatic signal. Not "this number is
> fake" — but "this source doesn't back what's claimed here," which is what actually caught it.

**VISUAL:** The real 2026-08-29 thought log, citation highlighted, `VERIFICATION RATE: 0.0` stamped
beside it.

---

## 6:32 — CHAPTER 5: THE HONEST LEDGER

**CHAPTER CARD:** 5 · WHAT'S TRUE NOW, AND WHAT ISN'T

> **VO:** True now that wasn't a week ago.

**VISUAL:** List one, building line by line.

> **VO:** Fifteen of sixteen real false positives, gone, measured against every run this tool has
> ever produced — not four, sixteen. The one suppressed true positive fires again, as a side effect
> of the same fix. A comma-formatted number extracts correctly instead of losing everything but its
> last three digits. Claim verification runs on this comparison route for the first time, and
> produces a real signal against the one case that matters. Four ledger issues closed in one day.
> The comparison route has automated tests for the first time ever — three of them. Two hundred
> forty-two tests, up from two hundred twenty-four, green at every step.
>
> Still not true.

**VISUAL:** List two, in warning color, held on screen. Do not clear it.

> **VO:** A legitimate ratio and a fabricated one still look identical to this system. Both are just
> numbers with no label nearby — narrowing that gap from "any disconnected number" to "any unlabeled
> one" is not closing it.
>
> Whatever's actually wrong with one of the two local models used in this test — reading its own
> input, some specific quantization, this prompt shape — hasn't been investigated. It's flagged, not
> fixed, and it's a different kind of problem than anything this tool was designed to catch.
>
> The comparison route has three tests now. Every other route, and every line of interface code,
> still has zero. The four critical security findings from the original audit are exactly as open as
> they were. And the pile of work sitting outside version control got bigger again — eleven more
> files, on top of everything already sitting there uncommitted.

**VISUAL:** `git log` at the same commit as last time, file counter ticking up again.

---

## 8:16 — CLOSE

> **VO:** So here's the smallest true claim.
>
> The tool got better at not crying wolf. Fifteen fewer false alarms, for free, the same day they
> were measured. That's real.
>
> It did not get better at telling a real number from a convincing fake one. Those are different
> problems. A comparator that stops over-flagging and a comparator that catches fabrication solved
> zero-for-sixteen for one reason and stayed unsolved for another — and mixing those two up is
> exactly the overclaim this format exists to catch.
>
> Fifteen of sixteen. One left. And one model that, this week, showed it can't be trusted to read
> its own homework.

**VISUAL:** Return to `15 KILLED` / `1 TRUE POSITIVE`. Hold. Cut to black.

**END CARD:**
- 15 of 16 real disjoint-concept false positives killed · the 1 remaining is the confirmed true positive
- The untagged-ratio ambiguity is narrowed, not solved — a real number and a fabricated one still look alike
- 1 of 2 tested local models did not ground its answers in the real data it was given, in 3 of 4 live runs
- Claim verification now runs on the comparison route — confirmed against the real historic fabrication
- `/api/compare` has 3 automated tests now; every other route and all interface code still has 0
- 4 critical security findings from the original audit remain exactly as open as before
- **Nothing described here is committed** (still the same last commit as last video, now 11 more files deep)
*source: `logs/RUN_LOG.md` 2026-09-11 (×2) · `divij/work.md`*

---
---

## PRODUCTION NOTES

### Figures to build (D3 v7, per `brutalist/D3.md`)

| # | Figure | Timestamp |
|---|---|---|
| 1 | `sixteen-to-fifteen` — the prior video's card, `15 KILLED` stamping over it, `1` circled | 0:00, 8:16 |
| 2 | `fabricated-quarter` — real vs. invented context, side by side | 0:12 |
| 3 | `open-threads` — two branching paths, link-concepts vs test-overlap | 0:36 |
| 4 | `number-tagging` — one conclusion sentence, numbers getting colored concept tags | 1:12 |
| 5 | `three-bugs` — three bug cards, each struck through `FIXED` | 1:46 |
| 6 | `replay-through-gate` — the 16 labeled tiles from last video, filing through a `concept_aware` gate | 2:27 |
| 7 | `checked-twice` — two check panels, `MODULE, DIRECT: 15/16` and `PRODUCTION API: 15/16`, landing together | 2:55 |
| 8 | `true-positive-preserved` — the 15/1 card relabeled | 3:12 |
| 9 | `shared-context-fork` — one context block forking into two model icons | 3:23 |
| 10 | `zero-real-numbers` — fabricated quarter, struck URL, red stamp | 4:05 |
| 11 | `sign-and-magnitude` — real $101B income vs. mislabeled "-$101M loss" | 4:16 |
| 12 | `model-scoreboard` — 4/4 correct + 1 unsupported ratio vs. 0/4 grounded | 4:45 |
| 13 | `route-rewire` — `/api/compare` diagram, old rule struck, new rule wired | 5:00 |
| 14 | `regex-fix` — `"13,971,000,000.0"` crossing out `"000.0"` | 5:40 |
| 15 | `verification-rate-zero` — real thought log, citation highlighted, `0.0` stamp | 6:10 |
| 16 | `uncommitted-growing` — `git log` unchanged commit, file counter incrementing | 8:00 |

After generating: `npm run audit:layout`, then the `ACCURACY-REVIEW.md` pass. Layout first,
accuracy second.

### Fact-check table

Every spoken claim, mapped to its source. Re-walk this against the live files before recording
(guide §9) — several of these numbers move as the suite grows.

| Claim in VO | Source |
|---|---|
| 16 of 31 false positives, 0 genuine conflicts (prior period's finding) | `logs/RUN_LOG.md` 2026-09-07; carried forward as the recap |
| 15 of 16 disjoint-concept false positives killed; 1 preserved is the true positive | `logs/RUN_LOG.md` 2026-09-11 (first entry), Result |
| 0 new false positives introduced | same entry, Result |
| Concept tagging excludes known-concept numbers from comparison entirely | same entry, Outputs |
| Bug 1: decimal point mistaken for sentence boundary (GOOGL run `2c3c4f23`) | same entry, Result item 1 |
| Bug 2: tagger missed raw XBRL tag-name echoes ("EarningsPerShareDiluted") | same entry, Result item 2 |
| Bug 3: distance measured from label start instead of end, mis-tagged a Diluted/Basic pair | same entry, Result item 3 |
| The 16 flagged runs replayed are the same real, previously-labeled 2026-09-07 corpus, not new synthetic examples | `tests/fixtures/cross_agent_real_runs_corpus.json` (`label: "disjoint_concepts"`, 16 entries); `logs/RUN_LOG.md` 2026-09-07 |
| Measured once via `validation/concept_linkage.py` directly | `tests/test_concept_linkage.py::TestConceptAwareFlagAgainstCorpus` |
| Measured again via the actual production function, `run_cross_agent_validation(..., contradiction_rule="concept_aware")`, to confirm the wiring reproduces the module-level result | `tests/test_real_run_corpus.py::TestConceptAwareRuleAgainstCorpus` |
| Local Ollama found running with `qwen2.5:7b` and `mistral-7b` pulled | same entry, Inputs |
| 4 live runs: AAPL ×2 (roles swapped), MSFT, NVDA | same entry, Commands |
| 4 of 4 overlapping-concept runs flagged — first time on evidence both sides actually saw | same entry, Result |
| 3 of 4 runs: one model cited zero real figures, invented a fiscal quarter + fake URL | same entry, Result |
| 4th run (roles swapped): real Assets/Revenue cited correctly, NetIncomeLoss mangled — wrong sign, 1000x magnitude | same entry, Result |
| The other model transcribed every real figure correctly in all 4 runs, but added an unsupported ROE figure (NVDA) | same entry, Result |
| `mistral-7b-context-grounding-failure` opened as a new, separate ledger issue | same entry, Outputs |
| Tests 224 → 232 | same entry, Tests line |
| Old rule required both sides non-empty, which is what suppressed the true positive; new rule has no such gate | `logs/RUN_LOG.md` 2026-09-11 (second entry), Result |
| Fixing the wiring resolved that suppression as a side effect, no separate patch | same entry, Result |
| Comma-grouped regex bug: `"13,971,000,000.0"` was extracting as `"000.0"` | same entry, Outputs (core/numeric.py) |
| Fixed and confirmed against the real historical case | same entry, Commands |
| Claim verification wired into `/api/compare` for the first time | same entry, Outputs (web/server.py) |
| Replayed against the real 2026-08-29 fabrication case: `verification_rate = 0.0` | same entry, Result |
| 4 ledger issues moved OPEN → RESOLVED same day | same entry, Outputs (web/self_report.py) |
| First automated tests ever for any route in `web/server.py` — 3 tests | same entry, Outputs (tests/test_compare_route.py) |
| Tests 232 → 242 | same entry, Result |
| Untagged-ratio ambiguity narrowed, not solved | both 2026-09-11 entries' Open issues |
| Mistral-7b issue explicitly out of scope for the wiring session | second entry, Open issues |
| `audit-criticals` and `session-scope-leak` unchanged | second entry, Open issues |
| Still uncommitted; 11 more files added this period | both entries, Open issues |
| 242 tests passing | re-run at drafting: `python -m unittest discover -s tests -t .` → OK |
| Current ledger: 15 issues, 4 resolved this arc, 9 open/unverified, 1 critical | `build_self_report()`, run directly at drafting |

### Things this script deliberately refuses to say

Considered and rejected, per guide §6:

- **"The comparator now catches fabrication."** It runs a check that produces a real signal against
  one confirmed case. It has never been shown to catch a fabrication it hadn't already been pointed
  at. The script says "a real, automatic signal," never "catches."
- **"Mistral-7b is broken" / "Mistral-7b doesn't work."** Four runs on one machine, one prompt
  shape, one quantization. The script says "flagged, not fixed" and names exactly what wasn't
  ruled out — model-specific, quantization-specific, or prompt-specific — rather than a verdict on
  the model in general.
- **"This proves the tool works."** Four for four flagged is presented as proof the *mechanism*
  fires correctly on real evidence, immediately followed by the "but" that it fired for a reason
  the project didn't design it to catch. Never let the two facts blur into one triumphant beat.
- **"Fifteen of sixteen" as if the sixteenth doesn't matter.** The script keeps the sixteenth
  on screen as `TRUE POSITIVE, PRESERVED` every time the number appears — it's the one that matters
  most, not a rounding error left over.
- **"Four ledger items resolved" as if the subsystem is now more trustworthy overall.** The honest
  ledger chapter states, right after that count, that the security findings and the untagged-ratio
  ambiguity are completely unchanged — resolved counts up, remaining risk does not move in lockstep.
- **"Shipped."** Nothing is committed. The close names the same commit hash context as last video
  and states the file count grew, not that anything shipped.
- **"Checked twice, so it's fully verified."** The double-check in chapter 2 confirms the wiring
  reproduces the module's own measured result on *this* corpus — it is not evidence the rule
  generalizes to a run this corpus doesn't contain. The script says "confirm... didn't quietly
  change the answer," which is a claim about wiring correctness, not about future accuracy.

### If the runtime needs to shrink (to ~6:30)

Cut in this order: (1) the fourth-run sign/magnitude detail in chapter 3 — keep the headline 3-of-4
zero-grounding finding, drop the specific "-$101 million" wrong-sign case; (2) the three-bug list in
chapter 2 — keep bug 2 (the XBRL tag-name miss, the most instructive one) and cut bugs 1 and 3 to a
single line ("two more caught the same way"); (3) the regex-bug figure detail in chapter 4 — keep
the fact it was fixed, drop the exact truncation mechanism; (4) chapter 1's recap — cut to the
single "sixteen false positives, zero real conflicts" line and drop the two-branching-paths framing,
since the cold open already restates the headline number.

**Never cut chapter 5**, and never cut the "still not true" list inside it. Also protect the
replay-through-sixteen-real-runs / checked-twice beat in chapter 2 (the "Then the actual test..."
through "...didn't quietly change the answer" passage) even under time pressure — it's the specific
answer to "how do we know 15/16 is real and not a projection," and cutting it would leave the
headline number as an assertion instead of a shown measurement, which is the exact failure this
format exists to avoid. This is the shortest *wall-clock* period this series has covered so far
(one day, not weeks) but not the thinnest content — the temptation to let four resolved ledger
items read as unambiguous progress is exactly the overclaim-by-omission this format exists to
prevent.

### If the runtime needs to grow (to ~11:00)

Add: (1) a worked walkthrough of exactly how the concept-tagger decides which label is "closest" to
a number — the start-vs-end distance bug is a genuinely teachable example of a plausible-looking
heuristic failing on a real case; (2) the full four-run transcript comparison, not just the
headline pattern — showing all four models' actual conclusion text side by side is stronger
evidence than describing it; (3) why `concept_aware` mode reports *fewer* divergent numbers than
the old rule by design, not by accident — a good beat on how disclosure and detection are two
different knobs, not one.
