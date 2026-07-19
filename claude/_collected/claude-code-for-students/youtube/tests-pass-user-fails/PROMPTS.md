# PROMPTS — tests-pass-user-fails

## ElevenLabs voice

Voice ID: TyW6NH39JcFb5M3xdIIk (same as all claude-code-for-students reels)

---

## Beat narrations (paste to generate_audio.py — handled automatically)

B01: Seth finishes Phase 1 of his college application tracker. Nine of nine tests pass. The page loads. Persistence works. He is about to commit. He re-reads the SDD aloud: 'The user should be able to see at a glance which applications remain to submit and which are already in.' He looks at the running build. Six applications scattered in insertion order. At a glance fails. Every test passed. The build failed its user.

B02: A test suite that passes all cases should confirm correctness. Nine tests passed. Why did the build fail the user?

B03: Tests verify code against tests. The suite passes because the code matches the tests — not because the build satisfies the need that motivated it. Seth's score had rows for addApplication, toggleSubmitted, deleteApplication. No row existed for display order. The SDD buried it in a prose sentence. By row 5, he had stopped reading section 2.3. The test suite was structurally incapable of catching the failure — because the failure was never enrolled as a test.

B04: The 2026 version of this failure is sharper. If Claude wrote the tests and read the spec, both sides may share the same misreading. The tests pass because the code matches the tests — and the tests match the wrong reading of the spec. The loop is self-consistent and wrong. Code passes its self-generated tests at high rates while failing human-written tests at much lower rates. The gap between those two numbers is the gap between tests pass and needs met.

B05: Tony Hoare made the formal version of this argument in 1969. A program is correct with respect to a specification — never in the abstract. Correctness is a relation between code and spec, not a property of code alone. Tests are evidence about whether the code meets the spec. A test suite that does not include the user need is evidence about the wrong question.

B06: Verification runs in three passes. Pass 1: does it run on the happy path? Pass 2: does it handle the boundaries the SDD names? Both passes are partially automatable. Both are blind to Pass 3. Pass 3: read each user-need sentence aloud against the running build — not by running a test, by using the build, by looking at it, by asking whether a person who had not just built it would experience the sentence as true. Pass 3 is the pass you cannot automate. It is the pass Claude cannot run.

B07: Pass 3 fails when the build is functionally correct and needfully wrong. Seth's code was correct. His at-a-glance need was not met. The resolution: fix the code — sort not-yet-submitted first, submitted below, each subgroup in insertion order. New handoff condition: three unsubmitted and three submitted, unsubmitted render above submitted on every refresh. Claude writes a six-line change and one new test. Ten of ten pass. Pass 3: green. The build is done.

B08: The practice is concrete. Before you commit, open the SDD to the User Needs section. Read each sentence aloud. After each sentence, look at the running build and ask: does a user who has not just built this experience the sentence as true? This is not a test. It is judgment. The at-a-glance need cannot be asserted by a runner. It has to be seen. The cheapest moment to run Pass 3 is right before the commit — when the build is live and the needs are fresh.

B09: Tests passing is not done. Done means the needs the SDD named are satisfied — a strictly larger claim. The test suite catches what it was written to catch. The user need that was never enrolled as a test can pass nine automated checks and still fail the person it was built for. Read the user-need sentences aloud against the running build. Every time. Pass 3 is the one you cannot skip.
