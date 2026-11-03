# Frictional Log: minutes-of-the-meeting (Week 27 work video)

**Record provenance:** drafted 2026-10-17 with Claude from this folder's own records (`ANGLE.md`, `FACTCHECK.md`, `SCRIPT.md`,
`PEDAGOGY.md`, the `PROOF-REVIEW*.md` files, the Short's equivalents) and from the Mycroft contribution's
committed records (the recipe, `logs/RUN_LOG.md`, PR #70), and the working session, after the work was done rather than while it
happened. **Awaiting Tanmay's review.** Every entry points at the record it comes from.

## 2026-10-17: A recipe nobody else was on

- **Work and expectation:** make a moderate, real contribution to a recipe in `nikbearbrown/mycroft` `main`, not a rubber stamp, and
  do not touch anyone else's work.
- **Where it resisted:** 93 of the 99 recipes have open `[TODO: DEV]` items and no status, so most were candidates. The question was
  which one holds real work. Open pull requests (11), upstream branches (9) and all 31 branches across the 12 forks were checked
  with read-only calls; none touched `what-if-simulation-agent`, its workflow or its scripts.
- **What was done:** the What-If Simulation Agent was chosen. All six of its steps were generic `[TODO: DEV]`, and its workflow holds
  a deterministic chain of six local steps (parse, three simulators, aggregate and score, build the AI briefing) before any network
  call. That is a unit with decisions in it.
- **Decided by:** Tanmay set the scope and the rule that nothing is pushed or opened until he says; the uniqueness check decided the recipe.
- **Record:** `../mycroft-recipe-contribution/README.md`, `logs/RUN_LOG.md` in the repository.

## 2026-10-17: A port that agreed with the original everywhere except where a number was not a number

- **Work and expectation:** port the six steps to Python so they run on test data, and check the port against the original JavaScript.
- **Where it resisted:**
  - JavaScript and Python differ in small places that matter: `Math.round` rounds halves up, `toFixed` works on the exact binary
    value, `parseFloat` takes a numeric prefix, `??` and `||` treat zero differently, and `Math.min` with a NaN returns NaN where
    Python's `min` may return the other value.
  - The parity run found that last one: on two requests (growth typed as "abc", sentiment left as empty text) the port gave a
    different verdict.
  - The first sample corpus also missed two of the nine growth-and-sentiment cells.
- **What was done:** `js_min` and `js_max` were written to copy JavaScript; two more fixtures closed the matrix; a self-test with 10
  deliberate breaks (a renamed node, a changed fixture, a port with Python's rounding or min and max, and others) now has to fail each
  time. The port matches the original on all 23 object-shaped requests, prompt string included. Whether the workflow itself should
  reject a NaN is recorded as a question for the maintainers, not a finding.
- **Decided by:** the checks decided the fix; the open question is the maintainers'.
- **Record:** the recipe's step 5 status line, `logs/RUN_LOG.md` ("Fixed while building"), `logs/what-if-simulation-agent/parity-results.json`, `self-test-results.md`.

## 2026-10-17: Pushing and merging, with a go-ahead each time

- **Work and expectation:** put the contribution on a new branch of the fork, additive only, then open and merge a pull request.
- **Where it resisted:** nothing technical; the care was in the order. A check run before every commit confirmed that nothing was
  deleted or renamed and that shared files were only appended to; the branch was pushed plainly (never forced) and verified against
  GitHub's own comparison (45 files, 43 added, 2 modified, 0 removed, 0 renamed) before the pull request was opened.
- **What was done:** PR #70 was opened at Tanmay's go-ahead and merged at his request once CI `verify` passed and the pull request was
  clean (merge commit `8665a9f`, 2026-10-17 20:44 UTC). The fork branch is kept.
- **Decided by:** Tanmay, at each step.
- **Record:** PR #70; `../mycroft-recipe-contribution/README.md` and `PR-DRAFT.md`.

## 2026-10-17: An angle that had to be new against two earlier Mycroft films

- **Work and expectation:** choose an angle and a structure that do not repeat any earlier work video.
- **Where it resisted:** two of the first ideas (an empty request that still gets a full answer; a value that is not a number)
  turned out to belong to Week 26's family, a bad or missing value quietly becoming a plausible one. A third (where the answer
  flips) was Week 25's territory. A narration search across the 43 earlier beat sheets (210 unique beats) found no earlier film about
  what a model is handed, nor one built on several weighted voices.
- **What was done:** the angle became "Minutes of the Meeting": three voices read one invented stock, a chair weighs them, and an AI
  is handed the minutes. The structure is the meeting itself, not a document, pairs, columns or mornings. Three angles were put to
  Tanmay with the nearest earlier beat for each; he chose this one.
- **Decided by:** Tanmay chose; the search ruled out the others.
- **Record:** `ANGLE.md`.

## 2026-10-17: Two questions the first script left open

- **Work and expectation:** a script that Tanmay reads aloud for Gate P, then a review before anything is built.
- **Where it resisted:** the review read the script as a first-time viewer would.
  - The chair weighs the voices 45, 35 and 20, then the pieces come out as 0.37, 1.75 and 0.05. The biggest weight contributed the
    least, and nothing said why.
  - "Requests where a number wasn't a number" was never shown, and the last lines of the turn repeated a device from Week 25
    (breaking my own copy on purpose).
  - The framework arrived only at the close, and the closing task had no good answer or weak one.
- **What was done:** B07 now says the chair's scale runs one to five, so a smaller weight on the top can outweigh a bigger one on the
  bottom; B09 names the two requests and drops the repeated device; B02 states the question early; B11 gives a good answer and a
  weak one. The script scored 10/12 before and 12/12 after. Four beats changed, so Tanmay re-read those four and signed again.
- **Decided by:** the PROOF review proposed; Tanmay's re-read decided.
- **Record:** `PROOF-REVIEW.md`, `PEDAGOGY.md`.

## 2026-10-17: Defects that only looking found

- **Work and expectation:** render one slate per beat, drawn in code, with every figure read from the merged repository.
- **Where it resisted:**
  - The checks passed while the pictures were wrong: text sitting on rule lines or clipped by card edges (mixed fonts anchored at their
    tops), a column running off the right edge in B07, a scale label colliding with the table, the fixed Python line printed over the
    broken one in B09.
  - A contrast check found small text at 4.1 to 4.2 to 1 on the tinted and pill backgrounds.
  - The review found "aggressive" spoken while the card said "high", and a "someone typed" card that read like a recorded request.
- **What was done:** one baseline system for every text; the palette's soft ink and accent text darkened to 4.7:1; the card says
  "high · aggressive"; the typed card says "someone types, for example". Then 12/12 on the stills.
- **Decided by:** the renders and the checks decided; Tanmay looked at all twelve and had no changes.
- **Record:** `PROOF-REVIEW-STILLS.md`.

## 2026-10-17: Defects in the cut, one made by my own fix

- **Work and expectation:** compile once and run the checks on the compiled file.
- **Where it resisted:** it took six compiles. The spoken "about 470 words" appeared on screen six seconds after it was said; the
  closing caption of B08 held 1.85 s; B02, B06 and B09 opened on a bare heading for 5 to 10 s. The fix for B02's bare opening
  printed the recipe's path over the README quote, which the 50% and 85% frames showed.
- **What was done:** the word count got its own stage on its phrase; B08 got a one-second hold; B02 carries the recipe path from the
  start, B06 shows its rows earlier and B09 builds its two minute-takers' cards as they are named; the B02 layout was re-spaced.
  A spoken-figure check on the Whisper clock now runs on every figure.
- **Decided by:** the frames and the checks.
- **Record:** `PROOF-REVIEW-CUT.md`.

## 2026-10-17: "It feels like slow motion"

- **Work and expectation:** the first master passed every check (Whisper, loudness, holds, silences, cue timing).
- **Where it resisted:** Tanmay listened and said the audio felt like slow motion. No machine check could say that. The cause was
  that each sentence had been synthesised alone, which Kokoro reads about 30% slower than a whole paragraph (2.5 words a second
  against 3.5, the pace Week 26's audio has). The voice, its speed and the sample rates were all correct.
- **What was done:** each beat is now synthesised whole, with the sentence times for the captions taken from the Whisper clock; the
  film went from 5:08 to 3:54. Kokoro also merged "What-If" into "wudif"; it is now voiced "what if". The topic video and its Short
  were built the same way, so they were rebuilt too (6:23 to 4:49 and 0:54 to 0:47).
- **Decided by:** Tanmay's ear found it; the comparison against Week 26's stored audio explained it.
- **Record:** `PROOF-REVIEW-CUT.md` (pace correction), the topic video's `PROOF-REVIEW-CUT.md` addendum.

## 2026-10-17: A Short that should not rush

- **Work and expectation:** a 9:16 trailer with its own script, one continuous arc.
- **Where it resisted:**
  - The first plan ran 47 s, and Tanmay asked for more room and for the Short to say what the full film will show.
  - The Shorts review scored the plan 9/12: the question came 8 s in, four previews around one sheet could not fit a 30 px type
    size, and the event plan left gaps up to 7.7 s.
  - The first gate run on the compiled file was 9/12: the name line, the channel and a pipeline tag were in the script but not in
    the scene, leaving a 5 s static stretch.
- **What was done:** the Short became 84 s with its own line about the full film; S01 opens on the question; previews arrive one at a
  time; 55 events keep every gap under 3 s; the missing text was added. Gate 12/12.
- **Decided by:** Tanmay on length and purpose; the review and the gate on the rest.
- **Record:** `SCRIPT-SHORT.md`, `PROOF-REVIEW-SHORT.md`.

## 2026-10-17: Transitions that lagged, then switched

- **Work and expectation:** a Short whose headings change smoothly.
- **Where it resisted:** Tanmay saw the headings change with a lag, then switch. Every Shorts check had passed. The cause was in the
  canvas, shared with the topic Short: Pillow ignores the alpha of a text fill, and an RGBA base replaces pixels instead of blending,
  so every fade was a pop. An element appeared at full strength the moment its alpha passed 0.01, and during a headline change the old
  line stayed at full strength while the new one popped over it. The swaps also began on the first word of the new line, so they
  landed about 0.3 s late.
- **What was done:** the canvas is now an RGB base with real alpha blending and text drawn through an alpha-scaled mask; every fade
  starts 0.15 s before the word that names it; headline swaps are one eased crossfade with a small slide, finished as the new line
  begins. The largest frame-to-frame change fell from 5.45 to 1.75 grey levels. Both Shorts were rebuilt and the gate was 12/12 again.
- **Decided by:** Tanmay saw it; sampling pixels across a fade found it.
- **Record:** `PROOF-REVIEW-SHORT.md` (build findings, row 7), the topic Short's addendum.
