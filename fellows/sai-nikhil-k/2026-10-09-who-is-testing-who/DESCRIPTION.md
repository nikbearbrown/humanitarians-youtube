A unit test can run every line of your code and still miss the bug that ships.

This week's second video is a general one. It's built on Alexandru Gherghe's essay "A Lot Of Unit Tests Are Worse Than Useless" (July 2026). His example is a BookService with five dependencies. Its unit test mocks all five and verifies that each was called once. We ported the example to Python and put it to the test.

The bugs. We planted five bugs, one at a time. Three were in the database query, which Gherghe calls "broken assumptions about what would be returned": the columns came back in the wrong order, the repository returned a raw row instead of a Book, and a missing id raised an error where "not found" should have come back. The other two were wiring mistakes inside the service. The mock suite (13 test runs) caught the two wiring mistakes and passed all three query bugs. Four tests against a real SQLite database caught all five.

The refactors. We then made two changes that keep the behaviour the same: moving the not-found check into the repository, and building the reply in the service instead of the mapper. The database tests passed both. The mock tests failed both, because they check which calls were made, not what came back.

The metric. The mock tests run every line of the service: 17 of 17, so 100% coverage. Mutation testing asks a harder question: does a test notice when a line is wrong? We ran mutmut 3.8 on each suite, setting aside the mutants that only reword an error message:

- The mock tests caught 33 of 42 mutants (78.6%).
- The four database tests caught 41 of 42 (97.6%).
- Of the mutants in the query code, the mock tests caught none, because no mock test runs that code.
- Plain unit tests on pure pricing logic caught 28 of 30. The two they missed point at a real gap: no test has a zero-price item.

This matches the research. Inozemtseva & Holmes (ICSE 2014) studied 31,000 test suites and found only a low-to-moderate correlation between coverage and effectiveness once suite size was held fixed. Just et al. (FSE 2014) found that catching mutants correlates with catching real faults, independently of coverage.

Gherghe isn't against unit tests. They shine on pure logic. The trouble is glue code with the database mocked away, which is why Spotify's testing honeycomb puts most tests at integration. His summary: "test behavior, not implementation."

Try it yourself: pick one unit test you trust and list what each of its mocks assumes about the real dependency behind it. Then find the smallest bug in that dependency your test would still pass. If there is one, that's where an integration test belongs.

Chapters:
0:00 What does a test like this actually test?
0:16 Everything the essay's test checks
0:34 Five planted bugs: mocks 2, real database 5
0:54 Two harmless refactors: mocks fail both
1:12 Coverage vs mutation score
1:34 The run: 78.6% vs 97.6%, and 0% on the query
1:55 Where unit tests win: pure logic
2:14 Verdict
2:30 Your turn: what does your mock assume?
2:44 Outro

Sources:
Alexandru Gherghe, "A Lot Of Unit Tests Are Worse Than Useless" (2026) — https://alexgherghe.com/articles/some-unit-tests-are-useless.html
André Schaffer, "Testing of Microservices," Spotify Engineering (2018) — https://engineering.atspotify.com/2018/01/testing-of-microservices
Inozemtseva & Holmes, "Coverage Is Not Strongly Correlated with Test Suite Effectiveness," ICSE 2014 — https://doi.org/10.1145/2568225.2568271
Just et al., "Are Mutants a Valid Substitute for Real Faults in Software Testing?," FSE 2014 — https://doi.org/10.1145/2635868.2635929
mutmut — https://github.com/boxed/mutmut · coverage.py — https://coverage.readthedocs.io

Hosted by Sai. Voice: Kokoro am_onyx, free and local, no account. AI-generated narration. Motion graphics were built with Remotion, and the equations were typeset locally as outlined SVG. Every number on screen comes from scripts run for this video: a Python port of the essay's example, run with pytest 9.1.1, coverage.py 7.16.2 and mutmut 3.8.0. The planted bugs were fixed before either suite ran. The essay's Java tools (Spring, Mockito, Testcontainers) are stood in for by unittest.mock and an in-memory SQLite. No image was generated. No human-performed audio or video in this production.

Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: unit testing, mocks, mocking, integration testing, test doubles, mutation testing, mutmut, code coverage, test pyramid, testing honeycomb, refactoring, software testing, Python, pytest, SQLite, Alexandru Gherghe, Humanitarians AI, Computational Skepticism, weekly

#UnitTesting #MutationTesting #SoftwareTesting #Python #CodeCoverage #Refactoring #HumanitariansAI #ComputationalSkepticism
