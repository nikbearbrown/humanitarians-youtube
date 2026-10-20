# Tanmay K.

**Role:** Financial Analyst  
**Project:** _to be filled in_  
**GitHub:** [@Tanmay-Kulk](https://github.com/Tanmay-Kulk)

Weekly work reports for the **Agentic AI in Financial Services** case-study
series. Each episode pairs a primary-sourced case study with a working
reference implementation, and the video walks the build rather than
summarising the findings.

Each episode folder begins with `YYYY-MM-DD` and is dated to the **work week
being reported on**, not the day the video was rendered.

## Voice

**Kokoro `am_onyx` is the voice for this series.** `af_bella` ("Bella") was the
original standing choice (see below) and is recorded in every episode's
`beat_sheet.json` under `metadata.voice_kokoro` — but as of 2026-09-20 four
consecutive weeks (2026-08-30, 09-03, 09-13, 09-20) have shipped `am_onyx`, so
per this section's own stated rule, the standing choice is corrected here
rather than logging a fifth exception to a default that no longer describes
the work. Episodes before 2026-08-30 remain accurately described by their own
notes below.

**Documented re-voice, 2026-07-29.** The first episode (CommBank) was produced
in the Teardown register with `am_onyx`. From the Klarna episode onward the
series moved to the Pragmatist register with `af_bella`, because these reports
teach a method rather than dismantle a claim, and the warmer register suits a
walkthrough. Recording it here per `fellows/README.md`, which asks that a voice
change be an explicit, documented decision rather than a per-episode default.
`af_bella` is the standing choice; any future change gets logged the same way.

**Documented exception, 2026-08-06 — `am_onyx` for the self-verification
episode.** That film is a first-person investigation with a confession and a
reversal in it rather than a walkthrough, and it wanted a narrator. It keeps the
**warm first-person register**, *not* the Teardown register the toolkit
conventionally pairs with Onyx — register is a writing style and voice is a
timbre, and rewriting that film's wince or its moment of disbelief into Teardown
clip would have flattened the arc the script is built on. This is an exception
for one episode, reasoned in its `SCRIPT.md`. **`af_bella` remains the standing
choice for the series.**

**Documented exception, 2026-09-03 — `am_onyx` for both Week 21 films.** The topic
video is narration over a measurement rather than a walkthrough, the same reason
Week 20's topic video used Onyx. The work video follows it because **both films
name the same presenter aloud and ship the same week** — one presenter, released
together, should not arrive in two timbres.

Worth recording how close this came to going wrong: the work video's first draft
specified `af_bella` on the strength of Week 19's `SCRIPT.md` header, while Week
19's `beat_sheet.json` — the file that actually generated its audio — says
`am_onyx`. The document and the artifact disagreed. **`metadata.voice_kokoro` in
the beat sheet is the record**, per this section's own instruction; a header is
not.

**Documented exception, 2026-09-13 — `am_onyx` for both Week 22 films.** Same
reasoning as Week 21, and now the third consecutive week to take it: the topic
video is narration over a measurement, and the work video ships the same week
with the same presenter named aloud, so both carry the same timbre. Recorded as
an exception rather than quietly assumed, because this section is the record.

Three weeks running makes this worth flagging rather than logging a fourth time:
**`af_bella` is still written here as the standing choice, but `am_onyx` is what
has actually shipped since 2026-08-30.** If the next episode uses Onyx too, the
honest move is to change the standing choice and log `af_bella` as the exception
— not to keep adding exceptions to a default that no longer describes the work.

**Week 23 confirms it — standing choice updated, 2026-09-20.** Both Week 23
films (topic and work) ship `am_onyx`, for the same reason as Weeks 21–22: the
topic video narrates a reading rather than a walkthrough, and the work video
ships the same week with the same presenter named aloud, so both carry the
same timbre. That's four consecutive weeks on Onyx, which is exactly the
condition this section said would trigger changing the default rather than
adding a fifth exception — so the opening line above now names `am_onyx` as
the standing choice, and `af_bella` is the one carried as history.

## Episodes

| Week reported | Folder | Subject |
|---|---|---|
| 2026-07-28 | [`2026-07-28-case-study-video`](./2026-07-28-case-study-video/) | CommBank — untangling two conflated AI systems |
| 2026-07-29 | [`2026-07-29-ai-crossroads-build-or-buy-video-klarna`](./2026-07-29-ai-crossroads-build-or-buy-video-klarna/) | Klarna — build-or-buy, read through the Productivity J-Curve |
| 2026-08-05 | [`2026-08-05-lemonade-claims-bot-mycroft`](./2026-08-05-lemonade-claims-bot-mycroft/) | Lemonade — building the claims workflow, and what production would demand |
| 2026-08-06 | [`2026-08-06-can-ai-catch-its-own-mistakes`](./2026-08-06-can-ai-catch-its-own-mistakes/) | Self-verification — testing a repo topic's claim, and finding it doesn't hold |
| 2026-08-12 | [`2026-08-12-bs-01-pick-and-scope`](./2026-08-12-bs-01-pick-and-scope/) | Job descriptions — four questions that make a generic one specific enough for AI |
| 2026-08-13 | [`2026-08-13-hsbc-agentic-adjacent-ai-mycroft`](./2026-08-13-hsbc-agentic-adjacent-ai-mycroft/) | HSBC — reading an AI announcement without adding to it |
| 2026-08-23 | [`2026-08-23-the-ai-was-right`](./2026-08-23-the-ai-was-right/) | DBS — a true claim, and the inference it invites |
| 2026-08-23 | [`2026-08-23-where-the-record-stops`](./2026-08-23-where-the-record-stops/) | DBS credit-memo — labelling a build CONFIRMED, CONSTRUCTED or BLANK |
| 2026-08-30 | [`2026-08-30-a-quantum-sphere-stem-video`](./2026-08-30-a-quantum-sphere-stem-video/) | A quantum sphere is never the size it looks — the cross section that refuses to be classical |
| 2026-08-30 | [`2026-08-30-drafts-one-thing-files-another-mycroft`](./2026-08-30-drafts-one-thing-files-another-mycroft/) | Morgan Stanley — the distinction a review pass surfaced, and the one line that keeps it |
| 2026-09-03 | [`2026-09-03-the-cell-next-door-stem-video`](./2026-09-03-the-cell-next-door-stem-video/) | The cell next door — a survival number, its own fact-check, and both of them wrong |
| 2026-09-03 | [`2026-09-03-the-stages-that-stayed-dark-mycroft`](./2026-09-03-the-stages-that-stayed-dark-mycroft/) | Zurich/Clara — move one line, and 27 of 28 tests still pass |
| 2026-09-13 | [`2026-09-13-two-per-second-stem-video`](./2026-09-13-two-per-second-stem-video/) | Three witnesses to two per second — three fields agree, and one only ever said "in English" |
| 2026-09-13 | [`2026-09-13-what-had-to-be-invented-mycroft`](./2026-09-13-what-had-to-be-invented-mycroft/) | Capital One — five stages, and the three honest moves when the record runs out |
| 2026-09-20 | [`2026-09-20-same-room-different-argument-stem-video`](./2026-09-20-same-room-different-argument-stem-video/) | Same room, different argument — four names across forty years, and the popular retelling nobody checked |
| 2026-09-20 | [`2026-09-20-the-emptiest-row-mycroft`](./2026-09-20-the-emptiest-row-mycroft/) | Lloyds — four AI systems scored on the same two axes, and the one row that came back empty |
| 2026-09-27 | [`2026-09-27-which-of-gardners-eight-intelligences-stem-video`](./2026-09-27-which-of-gardners-eight-intelligences-stem-video/) | Which of Gardner's eight intelligences can a machine do? — eight rooms, and a light only where Gardner's own writing turns it on |
| 2026-09-27 | [`2026-09-27-read-the-receipt-backwards-mycroft`](./2026-09-27-read-the-receipt-backwards-mycroft/) | Mastercard Agent Pay — read the receipt backwards, and name the step that earned each line |
| 2026-10-04 | [`2026-10-04-why-a-coin-flip-beats-this-learning-algorithm-stem-video`](./2026-10-04-why-a-coin-flip-beats-this-learning-algorithm-stem-video/) | Why a coin flip beats this learning algorithm — Sutton & Barto's short corridor, a coin biased 2 − √2, and the blindfold test for when randomness is the best move |
| 2026-10-04 | [`2026-10-04-same-logic-two-languages-mycroft`](./2026-10-04-same-logic-two-languages-mycroft/) | Same Logic, Two Languages — rewriting a finance detector from JavaScript to Python, and putting a test exactly where two versions could disagree |
| 2026-10-11 | [`2026-10-11-how-a-room-changes-music-stem-video`](./2026-10-11-how-a-room-changes-music-stem-video/) | How a room changes music — one cellist, seven concert halls, and a slowdown at both ends |
| 2026-10-11 | [`2026-10-11-four-mornings-mycroft`](./2026-10-11-four-mornings-mycroft/) | Four Mornings — one portfolio dashboard, four quiet hand-offs behind it, and the morning my own test passed when it shouldn't have |
| 2026-10-18 | [`2026-10-18-the-birthday-paradox-three-things-stem-video`](./2026-10-18-the-birthday-paradox-three-things-stem-video/) | The birthday paradox, three things you could change — how many people, how uneven the days, how many days, and the square-root rule that falls out |
| 2026-10-18 | [`2026-10-18-minutes-of-the-meeting-mycroft`](./2026-10-18-minutes-of-the-meeting-mycroft/) | Minutes of the Meeting — three simulators read one invented stock, a chair weighs them, an AI is handed the minutes, and the one place my own copy disagreed with the original |

## Two lanes

These reports come in two kinds, and they are deliberately not mixed:

- **Work-derived** — a film about the week's actual work (CommBank, Lemonade).
- **Repo-topic** — a film built from a topic already in this repo, replacing an
  earlier draft with real research (Klarna; self-verification). Each of these
  episodes names its source folder, what was wrong with it, and what was added
  on top, in its own README.

They carry different registers and different act structures. Referencing a
previous episode for *format conventions* is fine; content, visuals and
structure are built fresh for each film.

## Standards

Every episode is built to two documents kept outside this repo:

- **`PLAYBOOK.md`** — production discipline: audio-first timing, one bounded
  render at a time, verify by looking at frames rather than probing the mp4,
  4K output confirmed by `ffprobe`, deliverables kept separate from the raw
  working folder.
- **`PROOF.md`** — the content standard: a six-criterion teaching rubric scored
  out of 12, plus a binary production gate (evidence legible at the moment of
  assertion, sources on screen rather than only voiced, comparisons held
  side-by-side). Public release requires ≥8/12 **and** a passing gate.

Every shipped master is reviewed against `PROOF.md` before release. Each episode
folder carries its own `QC-REPORT.md` logging every defect found and fixed, the
gate verification, and any finding that sent the cut back before publishing. The
review documents themselves are kept outside this repo alongside the two
standards.

## Rebuild toolkit

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

Brutalist is audio-first and local: the beat sheet drives narration, measured
audio becomes the clock, generated visual beats compile immediately, and
unavailable media remains as labeled slates until a human fills the pantry. The
human conducts, watches, fact-checks, refines, and decides whether anything is
published.

**Note on `compile.py`:** it is a hard-cut concat with no transition or pause
mechanism. The 1.0s hold before every cut used across this series is a separate
pass — see `pacing_pass.py` in the Lemonade episode folder — and must be re-run
after any recompile.

## Frictional log

Every work subfolder here carries its own `FRICTIONAL.md` — a dated record of the process
behind that specific piece of work, kept beside the evidence it describes: what was tried
and expected, where it resisted and what was done next, what Claude or another person
contributed and what was accepted, changed or rejected, and what is now understood or
still open. Append as you go; never rewrite an earlier entry. It is not graded and not a
performance review. See <https://www.humanitarians.ai/fellows> for what an entry contains.
