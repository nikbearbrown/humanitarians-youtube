# Week 31 work video: angle (proposal)

**Contribution:** [nikbearbrown/mycroft#90](https://github.com/nikbearbrown/mycroft/pull/90), opened 2026-11-17 and merged 2026-11-17 (merge commit `894be6c`), one commit (`1eb38b5`) on a new branch of the fork, `Tanmay-Kulk/mycroft` @ `portfolio-price-fetcher-quality-check-and-report`, from upstream `main` @ `7315128`.
GitHub compare against `main`: ahead 1, behind 0, **50 files, all added, 0 modified, 0 removed, 0 renamed.** Mergeable and clean; the repository's `verify` check **passed** (14 s). **It builds on** #64 (steps 1, 3, 5 of the same recipe, Week 26).
**Status:** **APPROVED by Tanmay, 2026-11-17: angle D, "What Draft Is Waiting For"** (title: *What Draft Is Waiting For: Reading a Status as a Claim*), after a uniqueness audit (the uniqueness audit against the thirteen earlier work videos, summarised in this file) in which the first recommendation, A, failed. Scripts drafted for both formats. Standing instructions carried from Week 30: show nothing negatively; introduce what the work gives before what is left; say nothing about other fellows' work; humble register. New this week, from Tanmay: **do not change any existing file** (the guard now refuses any modification at all, not just edits outside an allowlist).

## 0. What #90 changed, as the basis for the film

Recipe `recipes/portfolio-price-fetcher.md` (a stock-price fetch and portfolio summary, from the workflow "Portfolio Price Fetcher"). It names a script for step 4 (transform and quality check) and step 6 (produce human report). Both now exist.

| | Before (`main` @ `7315128`) | After (#90) |
|---|---|---|
| Steps built (`snickerdoodle list`) | 3/6: steps 1, 3 and 5 have scripts | 5/6: steps 4 and 6 added; step 2 (ingest) still unbuilt, as before |
| What looks across the set | nothing: step 3 judges each response file alone, step 5 prices what step 3 promoted | step 4: duplicates, missing holdings, fallbacks, large moves, far-from-buy prices |
| The report | the recipe's template only | a report and an agent log for a clean run and for a run with a duplicate, from real files |
| Evidence | earlier self-test of 15 checks | plus a self-test of 24 checks (break tests on both scripts, and a comparison of steps 3 and 5 against step 4) |

**What the new steps do (committed, checkable):**
- Step 4 reads step 3's promoted records and asks five set-level questions: is any ticker there twice (identical copies collapse; copies that differ are **both** rejected, since nothing in the files says which is right); is any holding without a price (named, with the cost basis the summary would leave out); did any price come from the previous close; is any day move over 15%; is any price over 3x or under a third of the buy price. The three numeric lines are labelled "ours, a judgment" in every output.
- Step 6 writes the report (the recipe's fifteen sections, reader and decision enabled) and the agent log (its sixteen fields) from the files steps 1, 3, 4 and 5 leave behind. It judges the four stop conditions from evidence, reports the six gates as what the files show (none cleared), cross-checks step 4 against step 3 and step 5's totals against its own stocks, and recommends only a sample-mode next phase.
- Four invented fixture sets (duplicate, missing holding, large move, far from buy price) frozen in their own manifest; every price says it is invented.

**The measured finding that can carry a film (our own earlier step, found while writing the comparison test):** with two valid NVDA responses (504.5625 and 530.0), step 3 passes both, and step 5 prices NVDA with **whichever file sorts last**: `NVDA.json` beats `NVDA-restated.json` because `.` sorts after `-`, total value **65,098.13**. Rename the second file `NVDA2.json` and the same two prices give **66,370.00**, a 1,271.87 difference from a file name. Step 4 gives the same answer both ways: reject both, name NVDA missing, ask a person. (Committed: the comparison in self-test section E shows one-of-two; the rename run was done in a scratch folder this session and is **not yet committed**, see section 4.)

**Committed evidence the film may show:** `data/verified/portfolio-price-fetcher/quality-duplicate/quality-audit.md` and `quality-checked.json`, `reports/generated/portfolio-price-fetcher-2026-11-17*.md`, the step 4 and 6 scripts, `logs/portfolio-price-fetcher/quality-report-self-test-results.md`, `README-steps-4-6.md`, #90 itself.
**Off screen (workshop):** the safe-diff guard and its test record, plan files, proof reviews.

**Deliberate-boundary check.** Nothing here is a gap: `DRAFT` and the `[TODO: DEV]` markers stay because the rule this week was to add files and edit none; step 2 and live mode are human-gated and open by design; every price is invented. The recipe's step table and TODO markers are a small follow-up edit for the maintainers, written out in `README-steps-4-6.md`; the film says so as the next step, never as a flaw.

## 0b. Where the recipes stand now (our merged and open PRs)

| Recipe | Our PRs | Built (`snickerdoodle list`) |
|---|---|---|
| contradiction-detection-agent | #60 | 6/6, RUNNABLE-SAMPLE |
| portfolio-price-fetcher | #64, **#90** | 5/6 (step 2 open) |
| what-if-simulation-agent | #70 | 3/6 (steps 2, 4, 6 open) |
| scenariostresstestingagent | #74, #81, #82, #85 | 6/6 (DRAFT) |
| portfolio-dashboard | #64 (step 1) | 1/6 |

The earlier case-study pull requests (#2 to #54) are a different kind of contribution and not part of this film.

---

## 1. Where the earlier films already stand

Narration search: every work-video beat and read-aloud, Weeks 16 to 30 (645 text sources, about 154,000 words with the stage copies, topic videos excluded), then each hit read in context.

| Idea searched | Hits | Verdict |
|---|---|---|
| the winner decided by file order / sorted / alphabetical / file name / "last one wins" | 0 | open |
| judging a set as a set, "each file on its own" vs "across the set", per-file | 0 | open |
| "a person decides", "who decides", reject both | 0 (W19 "human decides" is the general labor-split line) | open |
| coverage (a holding with no price) | 36 in W20, 21, 23 (test and control coverage, a different subject) | open for this meaning |
| duplicate | 4, all W25: the report said "Duplicates: not checked, step 4 did not run" | **close in vocabulary only**; that was a log/report mismatch, this is two prices for one ticker |
| previous close, fallback, "zero counts as missing" | 16 and 8, **W26 (this very recipe's story)** | **avoid as a beat.** The previous-close record is last time's film; here it is one flag among five and gets one clause at most |
| quietly / silently | 36 and 12, W18 to 26 | avoid "quietly": it is W26's hook word for the previous-close pick |
| disagree | 62, W21 to 29 (W27 B09: Python and JavaScript disagree) | use "two prices that differ", not "disagree" |
| threshold(s) | 40, W18 to 28 | the three lines are a labelled aside, never the thesis |
| fingerprint, hash, "byte for byte", "the set was fixed" | W30 | do not reuse; the film is about a set read **after** it is frozen |
| invented portfolio of chip stocks, "validator protects the sum" | W28 | different recipe; do not echo |

---

## 2. Candidates, after the uniqueness audit (the uniqueness audit against the thirteen earlier work videos, summarised in this file)

The audit checks each candidate against all thirteen earlier work videos on claim, teachable move, shape, hook and vocabulary. **A, B and C fail** (reasons below); **D is new and passes**.

### D. "What 'Draft' Is Waiting For" (recommended)
> **A status word is a claim, and each rung of a status ladder asks for a different piece of evidence. Ask which rung, then ask to see the evidence.**

- **Teachable move:** put any "it works" claim (a model, a pipeline, a tool) on a ladder, name the rung it is on, and ask for that rung's evidence and for a written "did not test" list. The viewer can do this to the next status claim they hear.
- **Shape (new):** **one ladder, five markers.** Five rungs (draft, specified, runnable on samples, runnable live, verified), each with the evidence it asks for. My five recipes stand on it: contradiction detection on the third rung with a logged gate record, the stress-test recipe with six of six steps built and no open TODO, the price fetcher at five of six after this week, the what-if recipe at three, the dashboard at one. One rung is climbed on screen with a real evidence panel: this week's self-test, which lists what was run, what was seen, what was expected, and **what was not tested**.
- **Built upon:** every earlier film that ended "it says draft, on purpose" (W27, W28, W30) and the whole sample-mode series (#60, #64, #70, #74, #81, #85, #90): this film says what that word was waiting for.
- **The turn (real, positive, checkable):** looking at the stress-test recipe, six of six steps and no open TODO, I expected the next rung to be more code. The table says the rung after "specified" asks for a full sample run, passing checks, and **audits generated and read**; the last of those is a person, with a logged record, not another script. The film lets that sound like a discovery ("Not a script. A person."), then pulls back: what is claimed is only what the files show.
- **What it gives the viewer first:** the ladder and one sentence to carry away; and a way to read their own project's status with it (`node scripts/snickerdoodle.mjs list` lists the rung and step count for any recipe).
- **Why it is distinct (audit):** zero hits on ladder, rung, lifecycle, attestation, "did not test", promote, maturity; no earlier film's shape is a ladder. Meta-level cousins only: W20 and W24 ("a word stronger than I've earned", "a line is earned or marked"). Wording, shape and move are different; watch items in the audit.
- **Risks (all handled in the audit):** do not use W24's "earned or marked"; do not close on "draft, on purpose"; show only our own recipes, never another fellow's. The claim that the stress-test recipe is ready for a higher rung is **inferred**, and says so: the table suggests it, the promotion is a person's decision with a logged record.
- **Needs:** no new code in the repository. One fact to confirm before drafting: the exact current status lines and step counts of our five recipes (read from `main` at the time of writing, recorded in `FACTCHECK.md`).

### A. "Every File Passed" (set against per-file checks): **fails the audit**
A check that approves every file can be wrong about the set; step 5 prices a duplicated ticker with the file whose name sorts last (65,098.13, or 66,370.00 after a rename), and step 4 reads the set. **Claim = W26's** (an unwritten rule picks the price; a later step takes an earlier step's word) in a new instance, and the planned hook ("same two prices, two totals") is **W25's** "one number, two answers". The measured finding is real and stays in this file as evidence; it is not used as a thesis. It could appear as one supporting beat of D (one rung's evidence), told in new words.

### B. "Neither, and Why" (reject both and ask a person): **fails the audit**
Thesis is a refusal, which the W29 and W30 angle notes ruled out as a thesis or a beat; nearest films W22 and W30.

### C. "New Files Only" (add without editing): **fails as a thesis**
The beats it rests on ("nothing deleted, nothing renamed", added and modified counts, the guard) are W25 B11, W29 and W30. Usable only as a closing clause.

---

## 3. Recommendation

**D.** It is the only candidate with a claim, a teachable move and a shape no earlier film has, it uses this week's work (the self-test's "did not test", the recipe's step counts) and the progress across our five recipes, and it explains the line that W27, W28 and W30 ended on. A, B and C survive only as single beats inside it.

## 4. Open items before drafting

1. **Pick the angle** (D recommended). If you prefer one of the others, say which and I will redo the audit on the choice.
2. **No second commit on #90 is needed for D.** (The rename run was only needed for A.)
3. **Confirm the facts D rests on** (status lines and step counts of the five recipes; the ladder's gate tests) and put them in `FACTCHECK.md` before the read-aloud.
4. **Mechanical guard:** a word-run and vocabulary check against all earlier work videos runs on every draft before Gate P and its result goes into `PROOF-REVIEW.md`.
5. **Formats:** a long film and a Short as in Week 30, each its own script.
