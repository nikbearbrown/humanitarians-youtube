# Frictional Log — which-of-gardners-eight-intelligences (Week 24 topic video)

**Record provenance:** drafted 2026-09-28 with Claude from this folder's own records
(`TOPIC-DECISION.md`, `PEDAGOGY.md`, `PROOF-REVIEW-FINAL.md`, `PROOF-REVIEW-SHORT.md`, `SHORT.md`),
after the work was done rather than while it happened. Reviewed by Tanmay. Every entry below points
at the record it comes from.

## 2026-09-26 — Picking a topic nobody had built

- **Work and expectation:** take an unbuilt topic from this repo's library and make it a film.
  I expected the first random draw to be usable.
- **Where it resisted:** draws 1 and 2 were both fellow-authored sources (credited to a fellow in
  their `SOURCES.md`), so building them would have meant re-doing someone else's work.
- **What I did next:** excluded all 44 fellow-authored singletons and took draw 3, Nik Bear Brown's
  essay "Introducing Theorist.ai". Before building, I checked it against `main` and all 46 fellow
  branches, read-only, on a separate bare mirror so nothing in the shared repo was touched.
- **AI and other contributions:** Claude ran the draw and the uniqueness sweep. I set the rule that
  git in the shared repo stays read-only and can't affect anyone else's work.
- **Evidence:** [TOPIC-DECISION.md](TOPIC-DECISION.md).

## 2026-09-26 — Script and Gate P

- **What I tried:** a room-by-room structure ("EIGHT ROOMS") instead of a list of questions, with a
  light that comes on only where Gardner's own writing says a machine does what the room is for.
- **Where it resisted:** the mechanical lint raised 22 flags (long sentences, lone letters,
  acronyms). "Stachura" had no settled pronunciation for the voice.
- **What I did next:** split the long sentences and respelled for the voice, then read the whole
  script aloud against the slates. I signed Gate P with one note: *"say Stachura as sta-HOO-ra"*.
- **AI and other contributions:** Claude drafted the script from the fact-check and ran the lints.
  I read it aloud, judged the rhythm and signed it off.
- **Evidence:** [PEDAGOGY.md](PEDAGOGY.md), [READ-ALOUD.md](READ-ALOUD.md).

## 2026-09-26 — The first review said no

- **Expectation:** the first master would pass PROOF.
- **Where it resisted:** it was scored *unlisted-until-fixed*. The production gate failed on one
  claim (B17 named a book and year that nothing on screen supported), with four smaller edits
  recommended.
- **What I did next:** approved fixes 1–4, all on-screen text only, so the narration and Gate P
  stood. On re-review it was clear-for-public, with 35 of 35 claims on screen when spoken.
- **Evidence:** [PROOF-REVIEW-FINAL.md](PROOF-REVIEW-FINAL.md), "Re-review".

## 2026-09-27 — Too much of one picture

- **Where it resisted:** a pacing check found the static floor plan filled 52% of the runtime, with
  one unbroken 87s stretch.
- **What I did next:** added room interiors and camera moves. The plan's share fell to 29%, and the
  longest same-visual run to 41s. Frame checks caught five defects on the way:
  - scenes froze before their ending;
  - camera moves pushed rooms past the safe edge;
  - a blank flash at cuts;
  - a stray dot I spotted in a screenshot;
  - a speech bubble over a head.

  All five were fixed before the build.
- **Evidence:** [PROOF-REVIEW-FINAL.md](PROOF-REVIEW-FINAL.md), "Review — visual-variety master".

## 2026-09-27 — The Short

- **What I tried first:** a Short cut from the long's room beats.
- **Where it resisted:** it felt like beats stitched together. My note at the time: the Short should
  be a trailer but *"feel complete like not 2-3 beats stiched together"*.
- **What I did next:** rejected v1. The Short got its own script ("ONE HOUSE, ONE CAMERA"): one
  continuous take with its own ending, and continuity checked on frames at every cut.
- **What building it turned up in the long:**
  - one black frame at 5:50;
  - the voice reading digit years wrongly ("nineteen hundred eighty three").

  Both were fixed in the long too. Years are now written in words for the voice, and the captions
  keep the digits.
- **Evidence:** [SHORT.md](SHORT.md), [PROOF-REVIEW-SHORT.md](PROOF-REVIEW-SHORT.md),
  [PROOF-REVIEW-FINAL.md](PROOF-REVIEW-FINAL.md) addenda.

## 2026-09-27 — Timing, and knowing when to stop

- **Where it resisted:** cues pinned to pauses in the audio drifted from the words in some beats
  (mean 0.51s, max 1.17s).
- **What I did next:** I allowed a local Whisper model only *"if it's necessary"*. It checked every
  beat. The pause timing held within 0.23s everywhere except seven beats, and only those seven were
  re-timed and re-rendered. When a background process was still running that we didn't need, I asked
  for it to be stopped.
- **Evidence:** this folder's README, "Timing note".

## What I'm taking forward

- **Where the time went:** this week's time went mostly to re-rendering and recompiling after late
  checks. Renders were 58% of machine time, compiles 25%, and there were about 9 renders per beat.
- **So for the next film, before the first full render:**
  - run Whisper timing;
  - check phonemes for every year and name;
  - check stills in both aspects.
- **One compile per batch of fixes.**
- **A Short gets its own script from the start.**

**What I learnt**

- **Checking a count:** a number like "six of eight" is only as good as the test that produced it.
  The film's key moment came from asking *which* inspection lit each room (the 2024 paper's
  performance-style signs, not the 1983 criteria), and that habit applies to any source.
- **Structure from the subject:** Gardner's theory really is a floor plan, so a house with rooms
  made it easy to follow. A generic question list wouldn't have.
- **Checks that look for different things catch different defects:**
  - the black frame at 5:50 got past both the compile check and the 2% sweep, and was only found
    by the Short's overlay-zone scan;
  - the misread years were only found by checking phonemes.
- **What a Short is:** stitching the long's beats together didn't make a Short. It needed its own
  arc and its own ending.

**Going forward**

- Draw a topic and check it for uniqueness first, and treat any fellow-authored source as excluded
  from the start.
- Run every check that has already caught something (phonemes, Whisper timing, the per-frame dark
  scan, the overlay-zone scan) on the first compile, not after "final".
- Review stills of every beat in both aspects before rendering, so layout problems cost a still,
  not a render.
- Keep a runtime budget for any single picture, so a static plan never takes half the film again.

## Still open

- YouTube links for both films (the Drive links are in the README).
- The optional B02–B03 41s plan run, which the review left as a watch-test.
