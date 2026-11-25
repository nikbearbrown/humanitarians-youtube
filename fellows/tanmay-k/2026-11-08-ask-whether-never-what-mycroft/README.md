# Week 30 work video: Ask Whether, Never What

*Ask Whether, Never What: Checking a Pipeline's Keys Without Reading Them.* Tanmay K., in for Humanitarians AI.
Text and code only. The two masters are uploaded to YouTube.

## The contribution

This week's contribution to Mycroft (`nikbearbrown/mycroft`) builds on the Scenario Stress Testing Agent recipe:

- **Pull request #85** (merged 2026-11-09, merge commit `573c96a`): step 2, the conductor's "Source and Credential Check", in sample mode. It reads the 22 invented requests, checks each against its SHA-256 in the manifest and keeps each exactly as frozen (12 clean, 10 faulty, none rejected); lists the workflow's four sources (webhook available, chat skipped, the Groq model call and the Alpha Vantage request approval-required); asks the environment only whether `GROQ_API_KEY` and `ALPHA_VANTAGE_API_KEY` are set; and is guarded by a self-test of 37 checks. With it the recipe's last open item closes and all six steps run end to end. https://github.com/nikbearbrown/mycroft/pull/85
- It builds on pull requests #74, #81 and #82 (steps 1, 3, 4, 5 and 6, and a correction), all merged. The recipe stays a draft on purpose: going live, an approval record and the gate decisions are a person's acts. The contribution's code lives in that repository and is linked here, not copied.

## The film

- **Angle:** *a pipeline can find out everything it needs to know about a secret without ever looking at the secret: ask whether it is there, who has to say yes, and stop.* The angle, the boundaries against earlier films and the rejected candidates are in `ANGLE.md`.
- **Method the film teaches:** for each outside thing a pipeline reaches for (a key, a service, an account), write three facts apart: is it there, who has to say yes, what is the value. Record the first two on a page and design the third so nothing downstream needs it.
- **Long, "one pre-flight walk":** one source, the model call, followed as its row fills in field by field; why a yes or a no has nothing to copy; who says yes; the other sources; the turn (a test of a promise to keep a secret needs a secret, and the hard case with both keys set); what you get; the viewer's three lines; where the recipe stands.
- **Short, one persistent scene:** written fresh for a viewer who never sees the long film: the puzzle at 0 s, your introduction, the same row filling cell by cell, the test, and the long film's exact title; it ends on its own opening frame so it loops.

## The files

| | Film | | |
|---|---|---|---|
| **Long** | 16:9 | 3840×2160 · 30 fps · 3:30 (209.8 s) | −14.6 LUFS / −1.9 dBFS |
| **Short** | 9:16 | 2160×3840 · 30 fps · 1:20 (80.1 s) | −14.6 LUFS / −1.9 dBFS |

The films are not in this repository: the two masters are uploaded to YouTube (links below). Narration is Kokoro `am_onyx` (recorded as `voice_kokoro` in both beat sheets).
Visuals are original code-drawn animations; the type is Arial and Menlo (macOS system fonts), not the open-licence fonts of Weeks 27 to 29.

## How it was checked

- **Teaching rubric:** `PROOF.md` rubric 12/12 for the long film, and the Shorts rubric 12/12 for the Short, with the production gate passing on the compiled files (`PROOF-REVIEW.md`). Every one of 38 claims has its evidence on screen at the spoken word.
- **Gate P** (narration read aloud): signed 2026-11-09 for both films; `READ-ALOUD.md` and `READ-ALOUD-SHORT.md` are the signed text.
- **Numbers:** 37 rows read from the committed Mycroft files and asserted, plus a byte-for-byte reproduction of step 2 on a clean copy (`FACTCHECK.md`).

## Records in this folder

`README.md`, `ANGLE.md`, `READ-ALOUD.md` and `READ-ALOUD-SHORT.md`, `beat_sheet.json` and `beat_sheet-short.json` (narration, picture plan and timing per beat), `FACTCHECK.md`, `PEDAGOGY.md`, `FRICTIONAL.md` (drafted after the work from its records; awaiting the fellow's review), `PROOF-REVIEW.md`.
The captions, the YouTube text, the build, caption and check scripts, the measured outputs and the earlier stage reviews are kept locally; they need the local audio and video, which are not in the repository.

## Links

| | Link |
|---|---|
| Long film (YouTube) | <!-- YOUTUBE_LINK_LONG --> (when published on YouTube, this placeholder will be updated) |
| Short (YouTube) | <!-- YOUTUBE_LINK_SHORT --> (when published on YouTube, this placeholder will be updated) |
