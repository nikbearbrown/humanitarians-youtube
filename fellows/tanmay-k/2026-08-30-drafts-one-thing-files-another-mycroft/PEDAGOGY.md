# GATE P — pedagogy sign-off

**Film:** "Morgan Stanley's AI Drafts One Thing and Files Another"
**Week 20 work video · 14 beats · 1170 words · ~6:25 · voice `af_bella` (Pragmatist)**

**VERDICT: PASS** — signed by Tanmay Kulkarni, 2026-08-28, after reading the narration and
reviewing every beat frame.

---

## What the viewer walks away able to do

Three questions, on a card, applicable to any build made from someone else's spec:

1. What does the source treat as two different things?
2. Are they still two different things in the code?
3. Is there a line that fails if someone makes them one?

That is a **method**, not a topic. It is stated once (B02), used twice on screen (pass one on
Morgan Stanley's release, pass two on this repository), and handed to the viewer with their
own project as the subject (B12) in verbatim identical wording.

## Why this passes

**It teaches by using the instrument, not by describing it.** The card is built in B02 and
then *run* — the viewer watches it produce an answer twice, the second time on a case that
could not have been staged, because the film found it while being made.

**The claims are the viewer's to check.** Every number about the repository was computed and
re-run for this video: 29 tests across 10 files (all passing), 2 pipelines, 12 modules, four
test files diffed, the full forbidden-word list re-run against all four modules. Every claim
about Morgan Stanley comes from the **primary release**, fetched and quoted directly — not
from a summary of it.

**It says less than it could on the beat where saying more would be easy.** B10 refuses the
dramatic reading of its own finding ("the code is correct today"). B11 concedes there is no
observable failure at all, and volunteers a second limit of the method nobody would have
found. B13 leaves the gap open on purpose rather than fixing it off camera.

**The one overstatement was found and removed before build.** `PROOF-REVIEW-PREBUILD.md` F1:
the film's original headline claimed the Salesforce save was "the only thing either tool does
on its own", inherited from a summary. The case study's own workflow table marks five steps
autonomous. Corrected to the defensible claim — the only output confirmed *finished* rather
than waiting — and the title changed to match.

## The strongest thing in it

Fetching the primary source changed the film rather than tidying a citation. Morgan Stanley's
verb is **creates**, not "drafts"; `drafts` and `follow-up` appear **zero** times on the page.
The real sentence is three parallel verbs with a ten-word qualifier on exactly one of them, so
the distinction is *harder* to see in the original than in the paraphrase that replaced it.
That is the film's best evidence and it was unavailable while reading a reading.

## Known and accepted at sign-off

- **6:25 runtime**, longer than Week 19's 5:15. Two trim passes returned 65 words; what
  remains is load-bearing. Runtime follows the teaching.
- **12/12 teaching is self-assessed** by the person who built it. The defensible claim is
  that no criterion is obviously unmet.
- **The framework lands at ~46s**, later than PROOF's ~20s target, flagged not fudged: the
  intro-summary must name the subject in plain words first (PLAYBOOK §1c), and the framework
  still precedes the worked example at ~99s.
- **The `write` guard gap is left open on purpose**, and the film says so.

## Cleared for audio

Gate B (Manim layout audit): **0 errors, 0 warnings** on all three scenes.
Typecheck: exit 0. All 11 Remotion beats rendered. No time-stretch on any Manim beat.
