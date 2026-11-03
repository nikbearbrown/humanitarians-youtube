# Frictional Log — why-a-coin-flip-beats-this-learning-algorithm (Week 25 topic video)

**Record provenance:** drafted 2026-10-05 with Claude from this folder's own records (`TOPIC-DECISION.md`, `ANGLE.md`,
`FACTCHECK.md`, `BEATS-DRAFT.md`, `PEDAGOGY.md`, `PROOF-REVIEW.md`), after the work was done rather than while it
happened. Reviewed by Tanmay. Every entry points at the record it comes from.

## 2026-10-01 — Choosing a topic nobody had taken

- **Work and expectation:** pick this week's topic from the `humanitarians-youtube` library at random, as in earlier
  weeks. My condition: *"ensure that the topics you select is not taken by any other fellows and is not taken by us as
  well"*.
- **Where it resisted:** the library is large (5,068 topic folders) and full of near-duplicates, so "nobody has taken
  it" had to be checked, not assumed.
- **What I did next:**
  - The pool was narrowed to topics that appear exactly once, and filtered out anything:
    - in a collection we used in Weeks 20–24;
    - already produced;
    - a variant or near-duplicate of another topic;
    - touched on any fellow branch;
    - authored by a fellow.
  - Six topics were left. An unseeded draw put `claude-for-education/reinforcement-learning-an-introduction` first, and
    it was accepted.
  - A grep of `main`, every diverging fellow branch and our own Weeks 1–24 found no one building or extending it.
- **AI and other contributions:** Claude ran the sweep and the draw, read-only, on an isolated mirror; nothing in the
  shared repo was checked out or changed. I set the uniqueness bar.
- **Evidence:** [TOPIC-DECISION.md](TOPIC-DECISION.md).

## 2026-10-01 — Finding an angle in an unbuilt topic

- **Where it resisted:** the topic folder was an unbuilt auto-conversion, mostly boilerplate. I asked for an angle
  built on what the topic actually says.
- **What I did next:** the one concrete, checkable case in the source is Sutton & Barto's short-corridor example
  (Example 13.1). The angle: in that corridor, every fixed rule fails, and the best policy is a coin set to land
  "right" 2 − √2 ≈ 58.6% of the time. Then the film asks when randomness is the best move, and when it's only covering
  for what the player can't see.
- **AI and other contributions:** Claude read the source and proposed the angle. I accepted it.
- **Evidence:** [ANGLE.md](ANGLE.md).

## 2026-10-01 — Checking it against the book

- **Where it resisted:** when the fact-check started, I asked *"how does it relates to our chosen topic?"*. The film
  had to stay tied to the review it came from, not drift into a general lecture.
- **What I did next:** every claim was checked against the book's own pages (2nd ed., printed page numbers). I agreed
  to download the authors' free PDF on one condition: *"delete it after its usage is over because it will take up lots
  of space"*. It was deleted after each use. The review's own three statistics were audited too, and one (the 19% /
  27% controller figures) needed a qualifier. The film's numbers come from our own runs (`experiment/corridor.py`,
  `rps.py`), labelled as ours.
- **Evidence:** [FACTCHECK.md](FACTCHECK.md) (A1–A25), `experiment/`.

## 2026-10-01 — From 9/12 to 12/12

- **Where it resisted:** the first script scored an estimated 9/12. The framework arrived late, the rubric was only a
  portable question, and the viewer task depended on code that wasn't published yet.
- **What I did next:** I asked how to get to 12/12 and approved all three changes:
  - "every rule is a coin" stated before the first answer;
  - the blindfold test, with both of its outcomes (sight; rock-paper-scissors);
  - the code published and linked.
  Then: *"keep B17"* (the goalkeeper task). A second read-through also removed three overclaims (for example, "it works
  anywhere" became "you can carry it to other problems") and closed a gap in the puzzle: someone who can count their
  steps wouldn't need a coin, so the film now says you can't.
- **Evidence:** [BEATS-DRAFT.md](BEATS-DRAFT.md).

## 2026-10-01 — The Short

- **Where it resisted:**
  - The first Short didn't have my name in it, unlike the long film.
  - It was the long film's beats in order, shortened. My bar was that it give real context of the full film, *"not
    just 3-4 beats stiched together"*.
- **What I did next:** the Short was rewritten around one question carried through ("why does a coin beat a learning
  algorithm here?"), with the blindfold test inside it and my name at the start and end. When I asked whether it could
  reach 12/12, a task beat (the goalkeeper) was added. Gate P was signed on the new script.
- **Evidence:** [PROOF-REVIEW.md](PROOF-REVIEW.md) (Reviews 3 and 5).

## 2026-10-01 — Labels on the line

- **Where it resisted:** reviewing the stills, I noticed chart labels sitting on the curve. My note: *"try not place
  the text on the line, we can place it next to the dots"*.
- **What I did next:** one rule for every chart: near the steep ends a label sits beside its dot, away from the curve;
  in the middle it sits above or below. Checked on every chart in both formats.
- **Evidence:** [PROOF-REVIEW.md](PROOF-REVIEW.md) (Review 4).

## 2026-10-01 — What the voice actually said

- **Where it resisted:** Whisper, run on the generated audio, heard three phrases wrong: "weight" as "wait", "the
  book's number too" as "number two", and "right two minus root two" as "right to…". A page lint can't catch these.
- **What I did next:** reworded ("bias", "setting", "the book reports the same number"), regenerated, and re-read
  those five beats for a fresh Gate P signature. The lint now flags those words.
- **Evidence:** [PEDAGOGY.md](PEDAGOGY.md), [PROOF-REVIEW.md](PROOF-REVIEW.md) (Review 6).

## 2026-10-01 to 2026-10-04 — Finishing

- **Where it resisted:**
  - The compiler refused a final until the shot list and prompt records existed.
  - The Short first compiled as a 16:9 crop (a metadata key was wrong).
  - One Short beat filled too little of the frame.
  - Five captions on the final file stated a point before the narration reached it.
- **What I did next:** each was fixed and re-checked on the final file. Loudness stopped at −15.0 LUFS, the edge of
  tolerance; a limiter pass gained only 0.1 LU, so it was kept.
- **Result:** I watched both cuts end to end: *"its perfect now"*. Both films clear for public, teaching 12/12 on
  both.
- **Evidence:** [PROOF-REVIEW.md](PROOF-REVIEW.md) (Review 7, final verdict).

## 2026-10-04 — Publishing

- **What I tried:** publish the text and code to my folder only. My conditions:
  - *"it should not be pushed outside of that folder"*;
  - *"don't create a pr yet and ensure that no videos files have been pushed"*.
- **What I did next:** everything went into `fellows/tanmay-k/` on my branch, with no video files; both masters are on
  the shared Drive. The long film's description links the published experiment code (B17 promises it).
- **Still open:** the YouTube links once the films are live, and the Short's `[FULL VIDEO LINK]`.
- **Evidence:** [README.md](README.md).
