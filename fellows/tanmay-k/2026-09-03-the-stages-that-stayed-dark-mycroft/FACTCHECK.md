# FACTCHECK — *The Stages That Stayed Dark*

Every factual claim the work video makes, with its verdict, the beat that consumes it, and the
evidence. Per the source README's protocol: nothing is silently repaired, and gaps are marked
`[VERIFY: …]` rather than filled by guessing.

**Twelve of the thirteen claims are executable.** They are not asserted here — they are produced by
[`verify_claims.py`](verify_claims.py), saved to [`VERIFY-RESULTS.txt`](VERIFY-RESULTS.txt),
and re-runnable on a stock `python3` with no dependencies:

```bash
python3 verify_claims.py            # human-readable
python3 verify_claims.py --strict   # exit 1 if any claim fails
```

Current state: **13/13 verified.**

Confidence grades: **A** = executed this pass, output in `VERIFY-RESULTS.txt`; **B** = read from
a primary text this pass; **C** = not verified — **may not be spoken.**

---

## Part 1 — W1–W13, the claims the film makes

| ID | Beat | Claim | Verdict | Evidence | Conf |
|---|---|---|---|---|---|
| **W1** | B01 | The pipeline is five stages: Intake → Extraction → Coverage Check → Authorization Gate → Resolve | **SUPPORTED** | Call order read from `orchestrator.py`: `validate_intake → extract → check_coverage → AuthorizationGate → resolve` | A |
| **W2** | B02 | 28 tests, all passing | **SUPPORTED** | 28 counted by AST-shaped regex, **28 executed**, 6/6 files report `OK`. Stdlib `unittest` — **pytest is not installed and is not required**; a reader who runs `pytest` will conclude the suite is broken | A |
| **W3** | B03 | Low extraction confidence halts before Coverage Check, with its own named reason | **SUPPORTED** | `escalated` / `low_extraction_confidence` | A |
| **W4** | B05 | An output-only assertion passes on **both** the correct and the broken build | **SUPPORTED** | Both return the identical dict, including the `detail` string: `document type=flight_notice extraction_confidence=0.4` | A |
| **W5** | B06 | The break is one line moved — `+1 / −1` | **SUPPORTED, and corrected** | `check_coverage(...)` placed above the extraction halt, removed from below it. **The angle document called this "the three-line diff"; measuring it before scripting showed it is one.** The stronger fact was the true one | A |
| **W6** | B07 | The broken build fetches the customer's policy record; the correct build does not | **SUPPORTED** | Spy on `coverage_check.get_policy_record`: correct `fetched=False`, broken `fetched=True` | A |
| **W7** | B08 | `assert_not_called` fails on the broken build | **SUPPORTED** | Follows from W4 + W6: outputs identical, fetch differs | A |
| **W8** | B09 | Eight negative assertions across the suite | **SUPPORTED** | `assert_not_called` counted 8 across `tests/` | A |
| **W9** | B10 | A malformed gate decision reaches **neither** `resolve` nor `escalate`; it raises | **SUPPORTED** | `raised ValueError · resolve called=False · escalate called=False` | A |
| **W10** | B11 | Zurich confirms Clara maintains "a transparent and auditable trail of the reasoning behind decisions" | **SUPPORTED** | Phrase present in case study §3.2, sourced there to Zurich's Agentic AI Hyper Challenge campaign page | B |
| **W11** | B13 | On the happy path both builds are indistinguishable — the method sees nothing | **SUPPORTED** | Outputs equal **and** both fetch the record. This is the film's falsifiability case and it is verified rather than conceded | A |
| **W12** | B09 | The four halt conditions require **3, 2, 1 and 2** dark stages, and 3+2+1+2 = the 8 assertions of W8 | **SUPPORTED** | `incomplete_intake` 3 (extract, coverage, gate) · `low_confidence` 2 (coverage, gate) · `no_matching_policy` 1 (gate) · `invalid_decision_fn` 2 (resolve, escalate). **The eight are not an arbitrary count — they are the four shadows summed** | A |

**W10 is the only claim about Zurich in the entire film**, and it is the one sentence of theirs
the whole method serves. Everything else is about our own repository, which is on disk.

---

## Part 2 — Claims verified and deliberately NOT made

Each of these is true, checked, and kept out of the narration. Recorded so the work is not lost
and so nobody re-adds one without knowing what it costs.

| Claim | Status | Why it is not in the film |
|---|---|---|
| A different, unrelated **"Clara"** exists — Agent Workforce by Digital Workforce Services Plc — with **six named agents** (Anders, Fiona, Dalia, Nora, Petra, Sera) and **"confidence threshold configurable per decision class"** | **VERIFIED** directly against `agent-workforce.com`, not taken from the case study | It answers both of Zurich's open questions in near-identical language, so it is a genuine sourcing trap the build avoided. But "two things that look like one" is **Week 18's and Week 20's** teachable claim. Third use would be a pattern |
| A **third** "CLARA" — CLARA Analytics, a separate insurance-claims AI company | **VERIFIED** (exists, same domain, same name) | Ours, not the case study's — it names only two misattribution risks. Same reason as above |
| The **"11 modular AI Agents"** figure belongs to Wangari Global's Etio, a different Hyper Challenge winner | Case study §6.4 | Same family |
| `authorization_gate.py` contains **zero approval criteria** — no numeric literals in the class at all | **VERIFIED** (measured earlier this session) | The empty gate as a *thesis* is **Week 19's film**, near-verbatim. The gate appears in B10 doing a different job: the stage that must not be reached |
| Clara carries **no outcome figure of any kind** while three sibling Zurich tools each carry one | Case study §5.4, §6.1 | The strongest *finding* in the case study, and not this film's subject. A work video is about building |
| The case study says "28 tests across **seven modules**" — there are 7 source modules but **6** test files | **VERIFIED** | Accurate count, loose noun. Too small to spend narration on; recorded because loose phrasing is where the next error gets in |

---

## Part 3 — Standing requirements on the frames

0. **B09 shows the same diagram three times.** That is deliberate and must survive any trim:
   the beat's content is that the dark region *recedes* (3 → 2 → 1), which cannot be shown on a
   single frame. The running count completes `3 + 2 + 1 = 6 … + 2 = 8` with the fourth
   condition's two slots left **empty**, so B10 has something to fill.
1. **The broken build appears as the diff and nothing else.** Creator decision. One `+`, one
   `−`, exactly as measured. No file listing, no second implementation on screen.
2. **B11's audit-trail point is stated once and not restated.** Creator decision. No callback
   in B12, none in the outro. If a later pass finds itself explaining it again, cut the
   explanation, not the beat.
3. **B13 must ship.** It is the falsifiability case — the one place the method sees nothing.
   A film about proving a negative that never states its own limit would be doing the thing it
   warns against.
4. **Any on-screen test count reads `28 tests · stdlib unittest`.** Omitting the runner invites
   a reader to try `pytest` and conclude the suite fails.

---

## Part 4 — Claims deliberately NOT made

- **No claim that Clara does or does not work.** The film makes exactly one claim about Zurich
  (W10) and it is about their published language, not their system's behaviour.
- **No claim that this repository resembles Clara's actual architecture.** It is built from five
  confirmed sentences; the case study's own §4b states this and so does the repo README.
- **No claim that eight assertions make a system safe.** W11 exists precisely to bound this.
- **No claim about how other teams test.** B05 says "most test suites *I* have written" — first
  person, about my own work, because the general claim is unmeasured.

---

## Keeping this table honest

If a beat changes, its row changes in the same commit. Re-run the evidence at any time:

```bash
python3 verify_claims.py --strict
```

A `PASS` with nothing under it is the defect this file is written against — the inherited
source variant of this week's *topic* video shipped a 138-byte `FACTCHECK.md` reading
`VERDICT: PASS` over an empty table.

---

## Addendum — W13, added during Gate P

| ID | Beat | Claim | Verdict | Evidence | Conf |
|---|---|---|---|---|---|
| **W13** | B08 | Running the real 28-test suite against the broken build: **27 pass, exactly 1 fails** | **SUPPORTED** | `correct: 28 run, 0 failing` · `broken: 28 run, 1 failing → test_low_confidence_halts_before_coverage_check_and_gate_are_called` | A |

B08 originally said the negative assertion was *"the only thing in the suite that does"* fail —
a qualitative claim standing in for a number nobody had measured. Gate P's read-through flagged
it as checkable, so it was checked, and the measured version is stronger: **27 of 28 tests pass
on a pipeline that is wrong.**

**A false all-clear en route, recorded because it nearly shipped.** The first attempt swapped
`orchestrator.run_pipeline` for a broken function that held its own module-level references to
`check_coverage` and friends. The tests patch `orchestrator.check_coverage`, so the patches
never reached the broken code — and the suite reported **0 failures**, which reads exactly like
"the broken build passes everything." Wiring the broken pipeline to resolve its stages *through
the orchestrator module*, as the real one does, produced the true answer of 1. A verification
harness can fail open in precisely the way this film is about.
