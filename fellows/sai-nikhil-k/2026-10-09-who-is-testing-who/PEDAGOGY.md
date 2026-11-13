# PEDAGOGY — Who Is Testing Who?

Reel `weekly_updates/2026-10-09-who-is-testing-who/` · slug `claude-sai-who-is-testing-who`
· host Sai (Kokoro `am_onyx`) · `@HumanitariansAI` · Computational Skepticism weekly.
The week's **second** reel: a general explainer, not Sai's project.

Intake (2026-10-09): Sai gave the source —
https://alexgherghe.com/articles/some-unit-tests-are-useless.html (Alexandru Gherghe,
"A Lot Of Unit Tests Are Worse Than Useless", 2026-07-13). From Claude's proposals he
chose the ONE idea, the title (the essay's closing line) and **no AI angle**.

## The ONE idea

**A test that mirrors the code can't catch the code being wrong.** The essay's test
mocks all five collaborators of a `BookService` and verifies each was called once. Run
for real (a Python port), against five planted bugs and two harmless refactors: the mock
tests caught 2 of 5 bugs — none of the three in the query — and failed both refactors.
Four tests on a real SQLite database caught 5 of 5 and passed both.

Two honest edges the reel keeps in view:

- **The essay is an opinion piece; the reel tests it, it doesn't just repeat it.** The
  mock suite was given its strongest fair form (the essay's test plus three more in the
  same style, and unit tests for every collaborator that needs no mock), and the bug list
  was fixed before either suite ran against it. Mocks *do* catch wiring mistakes inside
  the service (B4, B5) — the reel says so.
- **Unit tests aren't the villain.** On pure logic (the essay's own pricing-calculator
  example) plain unit tests caught 28 of 30 behaviour mutants. The problem is glue code
  with the database mocked away. The reel ends there, as the essay does.

## Act structure

| Beat | Act | Pattern | Carries |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | "This is Sai." The essay, its example, the port. Its question: what does a test like that test? |
| B01 | THE TEST | `ClaudeScienceChipGrid` | Everything the essay's test checks: five calls, once each, and a title the mock itself supplied. |
| B02 | THE BUGS | `DivergentFates` | Five planted bugs: three in the query, two in the service's wiring. Mocks 2/5 (no query bugs); real DB 5/5. |
| B03 | THE REFACTOR | `BinaryBranch` | Two behaviour-preserving refactors. Mocks fail both; real DB passes both. "What assurance do they give anymore?" |
| B04 | THE METRIC | `TypesetMath` | coverage = lines run / lines; the service under mocks: 17/17 = 100%; mutation score = mutants caught / mutants. Inozemtseva & Holmes; Just et al. |
| B05 | THE RUN | `ExecutedData` | mutmut: mocks 78.6%, real DB 97.6%, mocks on the query code 0%, unit tests on pricing 93.3% (behaviour mutants). |
| B06 | WHERE THEY WIN | `DivergentFates` | Pure logic: 28/30, the two misses a real zero-price gap. Glue, mocked: query code 0/9. Spotify's honeycomb. |
| B07 | VERDICT | `ClaudeVerdictArtifact` | One page, four bare sentences. |
| B08 | HANDOFF | `ClaudeComposerAsk` (`greeting: "Your turn."`) | List what each mock assumes; find the smallest bug it would pass. Read aloud and discussed. |
| B09 | OUTRO | `LogoOutro` | "Who is testing who? Sai." (5 words, inside the 4 s card) |

## ILLUSTRATE LAW check

- Claude UI only at B00, B07, B08. ✔
- Every body beat illustrates. ✔
- No two consecutive body beats share a pattern: ChipGrid · DivergentFates · BinaryBranch ·
  TypesetMath · ExecutedData · DivergentFates (asserted by `build_beats.py --check`). ✔
- SHOW-DON'T-TELL: every beat has an ordered `show` block. ✔
- MATH + EVIDENCE: B04 typesets the two measures the run computes, with the service's own
  17/17; B05 is the run (`evidence/bookservice/mutation_run.out`). ✔
- No positional references in narration. ✔

## 9:16 constraint

Every pattern has a registered `*916` sibling (ClaudeComposerAsk916,
ClaudeScienceChipGrid916, DivergentFates916, BinaryBranch916, TypesetMath916,
ExecutedData916, ClaudeVerdictArtifact916, LogoOutro916). No user media.

## Evidence and honesty

- `evidence/bookservice/` — the port, the three suites, `experiment.out` (bugs and
  refactors), `mutation_run.out` (coverage + mutmut, every surviving mutant listed with
  what it changed). See its README to rerun.
- `evidence/sources_check.out` — the essay's quotes, Spotify's honeycomb, both papers.

Choices a reviewer should know about:

- **"Thirteen mock tests"** = 13 pytest test runs: 10 test functions, one of them
  parametrized over 4 bad ids. The database suite is 4 functions, 4 runs.
- **Mutants set aside:** 11 that only reword an exception message (no test in any suite
  checks messages) and 2 that only change the SQL's letter case (SQLite ignores it). The
  classification is code in `mutation_run.py` (`classify`), and the raw score with them
  included is printed too: mocks 60.0%, real DB 74.5%, pricing 84.8%.
- **The mock suite wins one:** its unit test of `MetricsService` counts twice, so it
  kills `+= 1 → = 1`; the database suite only counts once and misses it. That is the
  database suite's 1 of 42. Not hidden — FACTCHECK lists it.
- **Python, not Java.** Mockito's `verify(...).times(1)` is `assert_called_once_with`;
  the shape of the test is the same. Testcontainers/DataJpaTest is stood in for by an
  in-memory SQLite — the point (a real query runs) holds.
- The planted bugs were written into `experiment.py` before it was first run; nothing
  was dropped or added after seeing a result.

**Not claimed:** that mocks are always wrong; that integration tests are free (the
essay concedes they're slower — the reel doesn't time them); anything about Java tooling.

## Attribution

The essay and its example are Alexandru Gherghe's; the reel names him in B00 and
DESCRIPTION. The port, the bugs, the refactors and the runs were made by Claude for this
video at Sai's request. Spotify's article is André Schaffer's (2018).

## Attribution override

Hosted by Sai in his own name (B00 "This is Sai", B09 "Sai."), voice Kokoro `am_onyx`,
handle `@HumanitariansAI`. The guide's IN-FOR-BEAR LAW is deliberately suspended.

## Expected build noise (not bugs)

- SKIN LINT wants `ClaudeTitleOutro`; `LogoOutro` is deliberate.
- GATE V `underfill` on B07/B09; B09 declares `qc.sparse`.
- The portrait slate's burn-in edge-bleed.

## Spoken respellings

"Gair-gay" (Gherghe, Romanian [ˈɡerɡe]) — checked with Kokoro's phonemizer.

## Portrait-only edits (in `vertical/beat_sheet.json`, not the parent)

**One** (2026-10-09, applied before the portrait render): B03 `data.question` →
`"Same behaviour, new code: which suite passes?"`. The parent's 65-character question
would wrap to three lines in `BinaryBranch916`'s fixed-height card (seen on the week's
other reel). Re-apply after every `shorts.py --vertical`.

## Review checklist (Sai)

- [x] The ONE idea, the title, no AI angle (chosen 2026-10-09).
- [ ] Nothing here should be left out of a public video.
- [ ] Naming the essay's author on screen and in narration is fine.

## Narration

<!-- NARRATION:BEGIN (generated by fill_narration.py — do not edit by hand) -->

### B00 · ASK — `ClaudeComposerAsk` · 16.9s measured (59 words)

> This week's second video is a general one. Alexandru Gair-gay has an essay
> called A Lot of Unit Tests Are Worse Than Useless. This is Sai. His example is
> a book service with five dependencies, all mocked. I ported it to Python and
> planted bugs in it. The question is his: what does a test like that actually
> test?

### B01 · THE TEST — `ClaudeScienceChipGrid` · 17.8s measured (57 words)

> Here is everything the article's test checks. The validator was called once.
> The permission check, once. The repository, once. The mapper, once. The
> metric, once. And the title that comes back is the title it told the mock
> mapper to return. His point: it mirrors the method's implementation, not its
> behaviour. The real database never takes part.

### B02 · THE BUGS — `DivergentFates` · 19.6s measured (71 words)

> So I planted five bugs, one at a time. Three were in the query, his broken
> assumptions about what would be returned: columns in the wrong order, a raw
> row instead of a book, an error where not found should be. Two were wiring
> mistakes in the service. Thirteen mock tests caught the two wiring mistakes,
> and passed all three query bugs. Four tests against a real database caught all
> five.

### B03 · THE REFACTOR — `BinaryBranch` · 18.5s measured (63 words)

> Now the other direction: two changes that keep the behaviour. Move the not-
> found check into the repository. Build the reply in the service instead of the
> mapper. The database tests passed both. The mock tests failed both, because
> they check which calls were made, not what came back. He asks: if a refactor
> means rewriting the tests, what assurance do they give anymore?

### B04 · THE METRIC — `TypesetMath` · 21.5s measured (74 words)

> Coverage won't show this. It asks whether a line ran, and the mock tests run
> every line of the service: seventeen of seventeen. Mutation testing asks
> whether a test notices when a line is wrong: change the code one small way at
> a time, and count the changes that make a test fail. Across thirty-one
> thousand test suites, once their size was held fixed, coverage was only weakly
> to moderately tied to catching faults.

### B05 · THE RUN — `ExecutedData` · 20.8s measured (72 words)

> So I ran it on all three test sets. Set aside the mutants that only reword an
> error message, which no test here checks. Of forty-two left, the mock tests
> caught thirty-three, and the four database tests forty-one. In the query code,
> the mocks caught none. Plain unit tests on pure pricing logic caught twenty-
> eight of thirty. Every mutant the mocks missed sits in that query code, which
> no mock test runs.

### B06 · WHERE THEY WIN — `DivergentFates` · 19.6s measured (62 words)

> He is not against unit tests. They shine on pure logic, like his pricing
> calculator: input in, output out, nothing to mock. The two mutants mine missed
> point at a real gap, a zero-price item. The trouble is glue: code that moves
> data through a database you mocked away. Spotify's testing honeycomb, which
> the essay cites, puts most tests there, at integration.

### B07 · VERDICT — `ClaudeVerdictArtifact` · 15.9s measured (52 words)

> So: one page. A test that mirrors the code can't catch the code being wrong.
> Here the mock tests ran every line of the service, missed every query bug, and
> failed both harmless refactors. Four tests against a real database caught what
> they missed. Unit tests earn their place on pure logic.

### B08 · HANDOFF — `ClaudeComposerAsk` · 14.4s measured (51 words)

> Your turn. Take one unit test you trust, with its mocks, and paste this. Ask
> what each mock assumes about the real thing behind it. Then ask for the
> smallest bug in that real thing your test would still pass. If there is one,
> that is where an integration test belongs.

### B09 · OUTRO — `LogoOutro` · 2.3s measured (5 words)

> Who is testing who? Sai.

**Total: 566 words** → 167.3s measured (2:47). No 180s cap applies to the --vertical cut; audio remains the master clock.

<!-- NARRATION:END -->

VERDICT: __________ — reviewer: ___ date: ___
