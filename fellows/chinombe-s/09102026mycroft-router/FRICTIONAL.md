# Frictional log — Adaptive Model Routing Gateway, Sprint 3

## 2026-09-10 — task policy, the router, and a frozen test set

- **Video (progress):** https://www.youtube.com/watch?v=MiWZyDMCR50
- **Drive:** https://drive.google.com/drive/folders/1xOoXuHBwvOA8mb8O3YAUd3hiCSPezVJB?usp=drive_link
- **Evidence of commit:** https://github.com/nikbearbrown/mycroft/commit/68bbeb5d1ee5b7e53bd283d17dc516024a2b5589


**What I was working on.** Locking down the six kinds of task Mycroft actually
does, building the router that sends each one to a tier, and hand-labelling a
test set  before any model had been run on it.

**What I tried, and what I expected.**
- I expected to build the test set from real requests the repo had already made.
- I expected the router's choices to mostly agree with my own labels, and to
  treat disagreement as a bug in the router.
- I expected to include the break-even rule (route cheap only when the cheap
  model's expected quality justifies it) right away, since it is the actual
  idea behind the project.

**Where it resisted, and what I did next.**
- **There was no real request corpus.** I went looking and found 203 of 217
  sample payloads were generic placeholders, the sentiment sample folder
  declares itself synthetic, and the mock transactions file holds zero records.
  So the fixtures are 24 synthetic cases with fictional companies, and every
  claim in this project is scoped to *how models handle these task types*  not
  to Mycroft's real traffic mix. Writing that limitation down instead of
  glossing it was the sprint's least comfortable decision.
- **My first labelling session was bad and I had to redo it.** I put every
  fixture on the cheap tier, including the ones I had deliberately written as
  traps  I was labelling how hard the text *looked*, not what getting it right
  requires. Redid the whole set against two questions: is there a trap here, and
  does answering need a reasoning step?
- The labelling tool didn't show me what the task even was  for a sentiment
  fixture, whether the label is sentiment toward the named company or toward the
  news. Added a `TASK:` line, plus `--redo` and `--ids`.
- The router agreed with my labels on only **9 of 24**. My instinct was to
  adjust the router until it matched me. I didn't, because my labels are
  predictions, not measurements  and if I tune the router to agree with my
  guesses, Sprint 7 measures nothing.
- I left the break-even rule out on purpose, for the same reason: it needs
  measured pass rates to be anything but a guess with arithmetic on top, and if
  the simple router isn't built first there is no baseline for the clever one to
  beat.
- Review then flagged **my own answer key**: `sent-001` keyed negative for a
  headline about beating estimates and raising guidance, `sent-004` negative
  where the named company won the contract. I noted both and did not fix them.
  Three weeks later they are still wrong, and Sprint 5 caught them again.

**What Claude contributed, and what I did with it.**
- I wrote `policy.json`, `policy.py`, `router.py` and the bench tooling. Claude
  did all the labelling and ran the freeze.
- Accepted: the router measures input length in **characters, not tokens**,
  because token counts differ per model  the router must not need a model to
  make its decision.
- Accepted: an unknown or pinned task type raises rather than falling back to a
  default tier. A silent default is how a request ends up on the wrong model
  forever.
- Accepted: task types and routing rules live in one file so they cannot drift
  apart, and each type cites the evidence file it came from, with a test that
  fails if that path disappears.
- Accepted: `expected_tier` means *the cheapest tier I expect to get it right* 
  a judgment, deliberately not the router's rule applied by hand.
- Evidence: `bench/manifest.json` (24 fixtures, SHA-256 per file);
  `FINDINGS.md` section 6; labeller tiers cheap 6 / mid 11 / strong 7 against
  the router's cheap 8 / mid 16 / strong 0.

**What I understand now, and what I still do not.**
- Understood: a test set has to be frozen and labelled *before* you see what the
  models do, or you will label to fit the results without noticing.
- Understood: a deterministic check catches a malformed answer, not a wrong one.
  A model that misreads a trap returns a perfectly valid label and nothing
  escalates. That is the whole reason Sprint 5 exists.
- Not understood: whether my tier labels are any good. One labeller, no
  agreement measure, and the answer-key errors found in review suggest the
  answer is "partly".
- Open from this sprint: 4 fixtures per type against a target of 30; no
  long-input fixtures, so the router's length promotion is covered by unit
  tests only.