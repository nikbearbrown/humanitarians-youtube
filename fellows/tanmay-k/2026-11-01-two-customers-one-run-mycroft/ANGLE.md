# Week 29 work video: angle (proposal)

**Contribution:** [nikbearbrown/mycroft#81](https://github.com/nikbearbrown/mycroft/pull/81), merged 2026-11-02 (merge commit `9684f46`).
`main` gained 14 added and 2 modified files, 0 removed, 0 renamed. **It builds on** #74 (merged 2026-10-26, `5d60312`: steps 1, 3 and 5 of the
same recipe) and, behind that, the sample-mode series #60, #64 and #70.
**Status:** **APPROVED by Tanmay, 2026-11-02: angle D, "Two Customers, One Run".** Angle A was proposed first and set aside because it read
negatively (see §2); Tanmay had asked that the angle not reflect our work negatively. Standing instruction from Week 28: *show nothing negatively;
where an instance could read that way, reframe it positively.*

**The turn, updated after approval (a real one, found while preparing this film).** Reading the committed agent log the way its reader would, stop
condition 1 was recorded as triggered although nothing was hardcoded: step 6 had tested whether a script reads the environment and matched its own
source line, three of the four conditions had no check behind them, and the report's page did not mention stop conditions, so the machine's page and
the person's page disagreed. It is fixed on the fork (`scenario-stress-testing-stop-condition-fix`, commit `890c90f`): each condition is judged from
evidence, the report says "Stop conditions: N of 4 triggered", and four new self-test checks guard it (30 of 30). Framed as the method working: two
pages built from one source of facts are only trustworthy if someone reads both, and a check now guards the agreement. **The earlier turn (the first
report showed sixteen steps because the generator also read the recipe's preserved notes) stays available as a smaller supporting beat.** The fix landed as [#82](https://github.com/nikbearbrown/mycroft/pull/82), merged 2026-11-02 as `255ddf8`, so the film can describe the fixed state as it is in `main`.

---

## 0. What #81 changed, as the basis for the film

Recipe `recipes/scenariostresstestingagent.md` (the only existing recipe edited, plus an appended `RUN_LOG.md` entry).

| | Before (`main` @ `874620c`, after #74) | After (#81, merge `9684f46`) |
|---|---|---|
| Steps 4 and 6 | `[TODO: DEV]` | built and exercised; each has a `Closed 2026-11-01` line (original wording kept) and a status line |
| `todos_open` / `recipe_version` | 5 / 0.2.0 | 3 / 0.3.0; status stays `DRAFT` |
| Quality check | none | every stress result re-derived from the workflow's own template shocks and reconciled (14 checks); duplicates by id and by content; 11 advisory flags on the clean set |
| Human report | none | the recipe's Output Contract: reader, decision enabled, fifteen sections, plus the agent log's sixteen fields; for the clean set and the defective set |
| Evidence | #74's self-test (27) and parity (24) | plus a self-test of 26 checks (11 deliberate breaks, 3 refusals) |

**What it built upon (#74, committed):** the step-3 validator, the step-5 port of four workflow nodes, 22 invented requests with a SHA-256
manifest, `approval_state` in the step-1 log, and the step-5 hand-offs recorded with `approved_for_live_action: false`. The recipe lifecycle
(`DRAFT → SPECIFIED → RUNNABLE-SAMPLE → RUNNABLE-LIVE → VERIFIED`, each rung needing evidence) is the constitution's, not ours.

**The committed report ends with three recommendations**, each computed from the files (not typed):
- **Approve for the next phase (sample mode only): YES.** 12 accepted, 11 reconciled, 1 handed off, 0 failures, 0 duplicates, 0 rejects.
- **Request source or schema fixes: NO.**
- **Block live execution: YES.** No approval record; step 2 (ingest) open; the Groq call, the Alpha Vantage request and the webhook reply are only
  recorded hand-offs.
Its "Human approvals" section reads: *None recorded.* On the defective set the same code says approve **NO**, fixes **YES**, block **YES**.

**Committed evidence the film may show:** the recipe, the report `reports/generated/scenariostresstestingagent-2026-11-01.md` and its
`-defective` twin, `quality-check.json`, the agent log, `report-self-test-results.md`, the `RUN_LOG` entry, #81 and #74 themselves.
**Off screen (workshop):** the safe-diff guard, the fixture builder, the plan files, the proof reviews.

**Deliberate-boundary check (read before forming the angle).** Nothing here is a gap: the recipe is `DRAFT` on purpose, step 2 is open on purpose,
the recommendation can only approve a sample-mode phase on purpose, and the report says "None recorded" for approvals on purpose. The film must
present each as the design, never as something missing.

---

## 1. Where the earlier films already stand (the boundary this one must not cross)

| Film | Thesis / shape | Nearest ground to this week |
|---|---|---|
| W24 *Read the Receipt Backwards* | audit an agent's purchase line by line, backwards | a gate with no built-in rule (DD004): the gate's *criteria* are deliberately absent |
| W25 *Same Logic, Two Languages* | two versions agreeing only counts where they could disagree; three matches | parity |
| W26 *Four Mornings* | what a dashboard takes on trust; four mornings | quiet hand-offs |
| W27 *Minutes of the Meeting* | what an AI is handed; a meeting and its minutes; closes on "five items open, still says draft, on purpose" | the hand-offs recorded as not approved; the DRAFT line as a closing beat |
| W28 *The Sum Behind the Number* | a number is a sum that can be taken apart; blocks of a sum | decomposing a figure |
| W18 B11 / W19 B08 | a gate "refuses to run until somebody hands it criteria"; "fails closed, on purpose" | refusing to run, fail-closed |

### Narration search (378 work-video beats, Weeks 16 to 28; topic videos excluded)
| Idea searched | Hits | Verdict |
|---|---|---|
| "exit code", non-zero, exit status | 0 | open |
| "denominator", what was counted | 0 | open |
| "inferred" / "verified finding" | 0 | open |
| machine verifies vs human judges, adequacy, conformance | 0 | open |
| a run where nothing ran; empty set; nothing to report | 0 | open |
| "could not look" vs "found something" | 0 | open |
| a clean run that is still not approved | 0 | open |
| recommend / approve / "block live" | 2, both W18 B11 (auto-approve criteria for a reviewer) | different idea; open |
| refuse / halt / fail closed | 29, nearest W18 B11 and W19 B08 | **close**: do not make refusal a thesis or a supporting beat |
| assert / could not fail | 20 (W20, W21, W23, W25, W26) | **close**: do not make the self-test's assertions a thesis or a beat |
| original wording kept / word for word | 2 (W25 B05, in another sense) | open |
| two readers: a machine log and a human report | 0 (one W25 false hit: "a flag for a person to review") | open |
| one source of facts, "cannot disagree", generated from the same data | 0 | open |
| diff / change one input and watch what moves | 0 | open |
| a status line: input, output, how it stops, evidence | 0 | open |
| regenerate / same bytes / idempotent | 2 (W20 B01, "run it twice", another sense) | open |
| one page / the report is the product | 0 | open |
| lifecycle / DRAFT / todos | W27 B10 and W28 B09 only as a closing sentence | the DRAFT line is a closing beat, never a thesis; keep it a closing beat |

---

## 2. Angle A, set aside, and why
*"Approve What, Exactly?"* (close-read the sentence "Approve for the next phase (sample mode only): YES", beside "Block live execution: YES").
Clean on uniqueness (no overlapping narration) but **it reads negatively**: its images are *blocked*, *None recorded*, *sample mode only*, *open
items*, *DRAFT*. It shows the report's limits first, which is the framing the standing instruction and the Week 17 note warn against (a blueprint
should be introduced by what it gives, with the honest remaining gap second). Kept on record; not recommended.

## 3. Three positive candidates

### D. "Two Customers, One Run" (recommended)
> **A run has two readers who need different pages: the program that carries on from it, and the person who has to decide. Build both pages from
> the same facts and they cannot disagree.** Step 6 turns one run into an agent log for the machine and a report for the person, and both say the
> same thing in the form each reader can use.

- **The teachable move:** for each output of your own pipeline, write down who reads it next (a script or a person), what they do next, and what
  must be on the page for them to do it, then generate both pages from one set of facts and check that their counts agree.
- **Shape (new):** **one fact followed through two pages**, a split of two desks. The machine's desk is the agent log (sixteen fields); the
  person's desk is the report (fifteen sections). Chapters follow three facts, one at a time, from the log's field to the report's sentence:
  a count (`records_seen`), a reason (`rejects`), and a call (`gate_decisions` to the recommendation). No list of rooms, mornings, lines,
  matches or blocks, and no close reading of one sentence.
- **Built upon:** #74 already wrote JSON for the next script (`validated.json`, the step-1 and step-5 logs) and a note for a person
  (`validate-audit.md`). #81 closes the pair the recipe's Output Contract had promised from the start: `quality-check.json` with
  `quality-notes.md`, then the final agent log and the human report. The recipe names both readers in its own contract.
- **The turn (a real one, framed as the method working):** I read my own first report the way its reader would and the step table had sixteen
  rows, because the generator had also read the old workflow notes the recipe keeps beside the new steps. Reading the page as its reader is a
  test no field check replaces; the fix was to read only the recipe's own steps section, and the report's counts are now checked against the log's.
- **What it gives the viewer first:** clone the repo, run two commands, and get both pages for a sample run; then the honest edge as an invitation
  (step 2 and live mode are the next pieces, left open by design).
- **Why it is distinct:** zero narration hits on two readers or one source of facts; it is about the *output side* of a run, where W27 is about the
  *input an AI is handed*; W26's reader is the dashboard viewer, a different idea.
- **Risk:** W27 (writing for a reader: minutes for an AI). Boundary: W27's subject is what the model sees; this one is two renderings of results.
  Avoid "minutes", "meeting" and "what an AI is handed" entirely.

### E. "Change One Input, Watch the Page"
> **A report is a function of its inputs, so you can test it like one: change one request and see exactly which sentences move.**
- **Shape:** a controlled experiment: regenerate the report with nothing changed (same bytes), change one weight (only that request's lines and the
  counts move), add one bad request (the recommendation changes and says why). Diff on screen each time.
- **Distinct:** zero hits on diff or "what moves".
- **Risk (real):** the structure (vary an input, watch the output) is W28's "same crash, different holdings"; it would read as the same device on a
  report. Better as a single beat inside D than as the film.

### F. "The Four-Line Status"
> **A script is only closed when four lines are true: what goes in, what comes out, how it stops, what proves it.** The recipe records each closure
> that way; step 4 and step 6 are two more worked examples.
- **Shape:** build one status line, line by line, for step 6; then fill the same four lines for a script of the viewer's own.
- **Distinct:** zero hits.
- **Risk (real):** it is a four-part checklist, the skeleton the "each film needs its own structure" note rules out for topic videos, and it
  leans on the closure convention (a process) more than on anything the build discovered.

**Recommendation: D.** It is positive by construction (it is what step 6 delivers), has no overlap on thesis or structure, draws on what #74
already built, has a real turn with a good outcome, and ends on something a viewer can do. E belongs inside D as one beat (the report counts
agree with the log's); F is a possible Short topic, not a film.

---

## 4. How the two formats would differ (Short written fresh, not cut from the long film)

- **Long (16:9, about 4 to 5 minutes):** "What this is" early (Mycroft, the recipe, #74 then #81, in a sentence); the two desks; three facts followed
  through; the turn (reading my own report as its reader); the viewer's task at the end; one open question; no checklist skeleton.
- **Short (9:16, about 80 to 90 s, one continuous scene, not cut from the long film):** context first (an AI pipeline finishes a run; who needs
  to know what happened), then the two pages for the same run, one fact lit on both, the person's call, and the long film's exact title;
  calm, about 3.0 words a second overall, pauses under a second, one idea at a time.

## 5. To confirm before scripting
1. Angle D (recommended), E or F?
2. The film shows the committed report, agent log and `RUN_LOG` entry on screen (all public); the guard and plan files stay off screen. OK?
3. Tone: positive and humble throughout; nothing about other fellows' work; the open items presented as the next pieces, never as shortfalls.
