# Week 30 work video: angle (proposal)

**Contribution:** [nikbearbrown/mycroft#85](https://github.com/nikbearbrown/mycroft/pull/85), merged 2026-11-09 (merge commit `573c96a`).
`main` gained 14 added and 8 modified files, 0 removed, 0 renamed. **It builds on** #74, #81 and #82 (steps 1, 3, 4, 5, 6 of the same recipe).
**Status:** **APPROVED by Tanmay, 2026-11-09: angle A, "Ask Whether, Never What"**, scripts for both formats to be drafted. Standing instructions: show nothing negatively; introduce what the work gives before what is left;
say nothing about other fellows' work; humble register.

## 0. What #85 changed, as the basis for the film

Recipe `recipes/scenariostresstestingagent.md`, step 2, "Source and Credential Check" (the conductor's own name for it). The step now exists.

| | Before (`main` @ `beef915`) | After (#85, merge `573c96a`) |
|---|---|---|
| Step 2 | `[TODO: DEV]`, no script | built; closure line and status line, original wording kept |
| `todos_open` / `recipe_version` | 1 / 0.3.2 | 0 / 0.4.0; `status` stays `DRAFT` |
| Runner | `snickerdoodle run ... --sample` stops at step 2 | all six steps run end to end: `All 6 steps completed.` (`full-sample-run-2026-11-09.md`) |
| Evidence | earlier self-tests (27, 24, 31) | plus a self-test of 37 checks (20+ deliberate breaks on scratch copies) |

**What the step does (committed, checkable):**
- Reads the 22 invented requests, checks each against its SHA-256 in the manifest, keeps every body exactly as frozen. Clean 12, defective 10, 0 rejected.
- Names the workflow's four sources and gives each one status, reason and credential name: webhook **available** (22 records); chat **skipped** (no fixture); Groq and Alpha Vantage **approval-required**.
- Asks the environment only whether `GROQ_API_KEY` and `ALPHA_VANTAGE_API_KEY` are *set* (`bool(os.environ.get(...))`); the value is never read into a variable or a file. `live_calls: false`, `network: false`, `live_call_performed: false` on every source.
- States its hand-off condition and whether it was met: *every source is available, skipped with a reason, or approval-required.*

**Committed evidence the film may show:** `data/raw/scenariostresstestingagent/ingest/source-check.json` and `ingest-audit.md`, the step 2 script, the self-test
results, the recipe's step 2 block, `README-step-2.md`, `full-sample-run-2026-11-09.md`, #85 itself.
**Off screen (workshop):** the safe-diff guard, plan files, proof reviews.

**Deliberate-boundary check.** Nothing here is a gap: `DRAFT` is deliberate, live mode and approval records are human acts left open by design, chat is
skipped because the invented corpus has no chat fixture. Each is shown as the design, never as something missing.

---

## 1. Where the earlier films already stand

Narration search: every work-video beat, Weeks 16 to 29 (148 sheets/read-alouds, about 10,750 words; topic videos excluded), then each hit read in context.

| Idea searched | Hits | Verdict |
|---|---|---|
| a secret asked about as *set / not set*, never read; presence vs value | 0 | open |
| fingerprint, hash, SHA, checksum | 0 | open |
| the whole chain run end to end for the first time | 0 | open |
| a source "available / skipped / approval-required", status with a reason | 0 (W22 B02 "confirm, construct or refuse" is a different idea: sourcing facts) | open |
| derived not typed, hard-coded | 0 | open |
| credentials, key, secret, token | 3: W24 B04 (agent credentials failed vs unknown, commerce), W24 B11 (a token restriction), W29 (stop condition about a hard-coded credential) | **close in vocabulary only**: none is about checking whether a credential exists. Avoid W29's "hard coded" and the stop-condition story entirely |
| byte for byte / word for word / unchanged | 2: W21 B06 (a refactor leaves output identical), W29 (a line carried word for word) | **close**: do not make "identical output" a beat; the fingerprint idea here is about the *input* staying whole |
| sample mode / no live call | 2: W19 B09, W21 B08 | present as background only |
| intake / first step | 7 (W21 pipeline stages, W26 B05, W28 B07) | different subject (stage names); open |
| refuse / halt / fail closed | 29 (W18 B11, W19 B08 nearest) | **close**: refusal must not be a thesis or a beat |
| still open / DRAFT as a closing line | W20 B13, W27 B10, W28 B09 | a closing beat only |

---

## 2. Three candidates

### A. "Ask Whether, Never What" (recommended)
> **A pipeline can find out everything it needs to know about a secret without ever looking at the secret. Ask whether it is there, ask who has to agree to use it, and stop.**

- **Teachable move:** for each outside thing your pipeline touches (a key, a service, an account), write three separate facts: *is it there*, *who must say yes*, *what is the value*. Record the first two on the page, and design the third so nothing downstream ever needs it. The viewer can do this for their own project in five minutes.
- **Shape (new, not a list of N):** **one pre-flight walk.** A pilot checks that the fuel gauge reads, not the fuel's chemistry. The film follows a single source, the model call (Groq), from "named in the workflow" to a row on the page: name, status, reason, `GROQ_API_KEY`, set: no, approval: none, call made: no. The other three sources appear only as contrast (available, skipped, a second approval-required). The viewer watches a row fill in one cell at a time.
- **Built upon:** #74 and #81 already carry `approved_for_live_action: false` on every hand-off; step 2 is where that false first gets its reasons.
- **The turn (real, framed as the method working):** to prove the script never leaks a key, the self-test needs a key. A fake key typed into a test file looks exactly like a leaked one to a reader or a scanner, so the dummy values are assembled while the test runs and exist only for its duration; then the test checks that neither value appears in any output file, and that every `os.environ.get` in the script sits inside `bool()`. To test a promise to keep a secret, you first have to manufacture one that is safe to lose.
- **What it gives the viewer first:** run `node scripts/snickerdoodle.mjs run scenariostresstestingagent --sample` and watch all six steps run for the first time; read one page that says what a live run would need, with nothing contacted.
- **Why it is distinct:** zero hits on presence-vs-value, on source status, on manufacturing a safe secret for a test. Nearest vocabulary (W24, W29) is a different idea.
- **Late finding (grep for "fake / dummy / planted"):** W29 B09 says "a planted fake key is caught by a new check". So a fake key in a test is not new vocabulary. This film's turn is different (the fake value is *assembled while the test runs* so no key-shaped text sits in any file, and the test is about a promise to keep a secret), but the script must not say "planted" or "caught", must not mention stop conditions, and must not call the dummy a "fake key caught by a check".
- **Risk:** W29's turn also involved a check reading its own source. Boundary: that story is not told or referenced; this turn is about the *test data*, not the check's match. If the AST check is shown, keep it to "every get sits inside bool()".

### B. "Whole on the Way In"
> **A step that is supposed to change nothing can prove it: fingerprint every input before, compare after, and name the one case you refuse.**
- **Shape:** 22 requests, 22 fingerprints; change one character on a scratch copy and watch exactly that request get rejected with the reason (missing, changed, unlisted, not JSON).
- **Distinct:** zero hits on hash/SHA.
- **Risk:** reads close to W21 B06 and the W25 parity idea ("identical"); the "reject on change" beat leans on refusal, which the audit marks as saturated. Better as one beat inside A.

### C. "The Last Link"
> **A chain only counts as a chain when its last piece arrives; the first full run is a different kind of evidence than six separate ones.**
- **Shape:** the runner's six steps lighting in order for the first time.
- **Distinct:** zero hits on whole-chain.
- **Risk (real):** it is about the project's completeness, so it pulls toward "what was missing before", which is the framing the standing instruction warns against, and the runner "refusing" an unbuilt step sits in saturated ground. Better as the film's opening image than its thesis.

**Recommendation: A**, with B's fingerprint as one beat (the 22 bodies come through whole) and C's six-step run as the cold open. It is positive by construction (it is what step 2 delivers), has a real turn with a good outcome, shows a method a viewer can apply to their own keys, and ends on something to do. The closing beat is the recipe staying `DRAFT` and live mode being the next human decision, stated as the design.

---

## 3. How the two formats would differ (Short written fresh, not cut from the long film)

- **Long (16:9, about 4 to 5 minutes):** cold open on the six steps running; what Mycroft and the recipe are, in one sentence, with #74, #81 and #82 behind this; the pre-flight walk down one row; the three facts split apart; the turn (the safe fake secret); the viewer's own five-minute exercise; the closing `DRAFT` beat.
- **Short (9:16, about 80 to 90 s, one persistent scene, not cut from the long film):** the puzzle first (can you check a key without looking at it?), one row filling in cell by cell, the two answers ("set: no", "approval: none"), the line "the value is never read", and the long film's exact title. Calm, about 3.0 words a second.

## 4. To confirm before scripting
1. Angle A (recommended), B or C?
2. The film shows the committed `source-check.json`, `ingest-audit.md` and the step 2 script on screen (all public in `main`); guard and plan files stay off screen. OK?
3. Tone: positive and humble throughout; nothing about other fellows' work; the open items as the next pieces, never as shortfalls.
4. Fonts: Week 30's topic films use Arial and Menlo (recorded, kept). Same for the work video, or switch to the open fonts the Week 27 to 29 work videos used?

## 5. Fact boundary for the script
Steps 3 to 6 still read the fixture folder directly (as built); the script must not say they consume step 2's output. The recipe is `DRAFT`; live mode, approval records and gate decisions are human acts.
