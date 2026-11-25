# Week 29 work video: Two Customers, One Run

*Two Customers, One Run: Writing a Pipeline's Results for a Program and a Person.* Tanmay Kulkarni, in for Humanitarians AI.
Text and code only. The two masters are uploaded to YouTube.

## The contribution

This week's contribution to Mycroft (`nikbearbrown/mycroft`) builds on the Scenario Stress Testing Agent recipe:

- **Pull request #81** (merged): steps 4 and 6 in sample mode. A quality check that re-derives every stress result (14 checks), then the recipe's Output Contract for each run: a 16-field agent log for the next script and a 15-section human report for the person deciding, for a clean set and for ten deliberately flawed requests. https://github.com/nikbearbrown/mycroft/pull/81
- **Pull request #82** (merged): the correction that came from reading both pages as their readers. Each of the four stop conditions is judged from evidence, the report says how many triggered, and four new checks guard it (30 of 30). https://github.com/nikbearbrown/mycroft/pull/82
- It builds on pull request #74 (steps 1, 3 and 5). The recipe stays a draft on purpose, with three items open. The contribution's code lives in that repository and is linked here, not copied.

## The film

- **Angle:** *a run has two readers, a program and a person; build both pages from the same facts and they cannot disagree.* The angle, the boundaries against earlier films and the rejected candidates are in `ANGLE.md`.
- **Method the film teaches:** for each output of your own pipeline, write down who reads it next, what they do with it, and what must be on their page; then generate both pages from one set of facts and check that the counts agree.
- **Long, "one fact, two desks":** one fact followed from the agent log's field to the report's sentence, three times (a count, a reason, a call); the turn (reading my own log as its reader found a stop condition recorded wrongly, now fixed and guarded); what keeps the pages agreeing; the viewer's three questions; the recipe's status.
- **Short, one continuous scene:** written for a viewer who never sees the long film: the claim at 0 s (every run needs two different pages), your introduction, who needs to know what a pipeline did, the two pages, one fact lit on both, the call, the mistake found by reading as the person, the three questions, the long film's exact title; it ends on its own opening frame.

## The files

| | File | | |
|---|---|---|---|
| **Long** | `two-customers-one-run-mycroft.mp4` | 3840×2160 · 30 fps · 4:02 (241.6 s) | −14.6 LUFS / −1.9 dBFS |
| **Short** | `two-customers-one-run-mycroft-short.mp4` | 2160×3840 · 30 fps · 1:37 (96.6 s) | −14.7 LUFS / −1.9 dBFS |

Each film carries its captions (`.srt` and `.vtt`) and its YouTube title, description, chapters and tags (`*-youtube.md`). Narration is Kokoro `am_onyx`.
The scripts are the working ones, kept as a record: they expect the working layout (a `short/` subfolder, the audio and stills folders) and, for the figures, the committed Mycroft files.

## How it was checked

| | Long | Short |
|---|---|---|
| Rubric | `PROOF.md` teaching rubric /12 + production gate | Shorts rubric /12 + gate on the compiled file |
| Result | 12/12 on the script and stills (`PROOF-REVIEW.md`, `PROOF-REVIEW-STILLS.md`); gate 8 of 8 (`MOTION-CHECK.md`, `MOTION-GATE.txt`) | 12/12 (`PROOF-REVIEW-SHORT-VIDEO.md`); gate 10 of 10 |
| Gate P (narration read aloud) | signed 2026-11-01 (`GATE-P-SIGNOFF.md`) | signed 2026-11-01; the opening line re-signed the same day (same file) |
| Numbers | 35 facts read from the committed Mycroft files and asserted (`FACTCHECK.md`, `factcheck_numbers.py`); every figure on screen is checked against them (`proof_stills.py`) |

## Links

| | Link |
|---|---|
| Long film (YouTube) | <!-- YOUTUBE_LINK_LONG --> (when published on YouTube, this placeholder will be updated) |
| Short (YouTube) | <!-- YOUTUBE_LINK_SHORT --> (when published on YouTube, this placeholder will be updated) |
