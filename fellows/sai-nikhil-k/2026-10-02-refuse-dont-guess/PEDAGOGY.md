# PEDAGOGY — Refuse, Don't Guess

Reel `weekly_updates/2026-10-02-refuse-dont-guess/` · slug `claude-sai-refuse-dont-guess`
· host Sai (Kokoro `am_onyx`) · `@HumanitariansAI` · Computational Skepticism weekly.
Subject: **Gavia 0.3.0 + 0.3.1** (both released 2026-09-29): batch checking of up
to 25 images or a zip, and updates from GitHub Releases with an off switch.

Intake (2026-10-02): Sai gave the repo as the update, chose the ONE idea and
title from three proposals, asked for the app's UI on screen (the batch flow and
Settings → Updates), recorded from the real app by Claude, with freely licensed
Commons photos. He named nothing to leave out.

## The ONE idea

**When a batch doesn't fit, refuse the whole thing and say why — never trim it
and hope nobody notices.** Gavia 0.3.1 takes 25 photos per check. Pick 26 and it
checks none, with "That's 26 images. You can check up to 25 at a time." The
source says why: *refused outright rather than cut short, because which images
got left out would be a guess.* A survey with a silent hole looks complete.

Two honest edges the reel keeps in view:

- **Refusal is for the count, not for bad files.** A file Gavia can't check (a
  `notes.txt`, a photo over 20 MiB) is *left out and named*, and the rest go
  through. The rule distinguishes "I can't read this" from "I'd have to guess".
- **The count still needs a reviewer.** On this video's 25 photos (22 loons, 3
  empty lakes) the app says *loons in 23 of 25*. The truth is 22: one empty lake
  got a box on a pine branch at 41%. The reel shows that photo in the app.

## Act structure

| Beat | Act | Pattern | Carries |
|---|---|---|---|
| B00 | ASK | `ClaudeComposerAsk` | "This is Sai." Continuity: last week promised a folder, a total, a CSV. The skeptical ask: what happens to the 26th photo? |
| B01 | THE BATCH | screen recording (`make_ui.py`) | The real app: survey.zip → 25 checked in ~3.5 s → "Loons in 23 of 25" → photo-19, the false box. |
| B02 | THE FORK | `BinaryBranch` | Trim to 25 (a gap that looks complete) vs refuse all 26 (the reviewer picks). Resolver quotes `batch.ts`. |
| B03 | THE RULE | `TypesetMath` | n counts zip contents; checked(n) = n·[n ≤ 25]; the zip cap 25 × 20 MiB = 500 MiB is derived, not chosen. |
| B04 | THE RUN | `ExecutedData` | `selectImages()` run on these photos: 25 → 25, 26 → 0, zip of 25 + 1 → 0, 24 + one oversized → 24. |
| B05 | THE ONE CALL | screen recording (`make_ui.py`) | 0.3.0's updater: what it sends, the measured sockets (one, GitHub, at launch), the switch turned off. |
| B06 | AGAINST THE PLAN | `DivergentFates` | Last week's plan vs this week's ship: 25 per check shipped; folder, total and CSV did not. |
| B07 | VERDICT | `ClaudeVerdictArtifact` | One page, four bare sentences. |
| B08 | HANDOFF | `ClaudeComposerAsk` (`greeting: "Your turn."`) | "Limit plus one": a prompt for any tool with a cap. Read aloud and discussed. |
| B09 | OUTRO | `LogoOutro` | "Refuse, don't guess. Sai." (4 words, inside the 4 s card) |

## ILLUSTRATE LAW check

- Claude UI only at B00, B07, B08. ✔
- Every body beat illustrates: two are the app itself, four are deck/maths/data
  patterns. ✔
- No two consecutive body beats share a pattern: recording · BinaryBranch ·
  TypesetMath · ExecutedData · recording · DivergentFates. ✔
- SHOW-DON'T-TELL: every beat has an ordered `show` block in `beat_sheet.json`. ✔
- MATH + EVIDENCE: B03 from `src/lib/batch.ts`; B04 from a run made for this
  video (`evidence/batch_rules.out`). ✔
- No positional references in narration ("the top row"): one mp3 serves both aspects. ✔

## 9:16 constraint

`shorts.py --vertical` builds the same film. The eight Remotion beats rewire to
their `*916` siblings (all registered in `Root.tsx`: ComposerAsk916,
BinaryBranch916, TypesetMath916, ExecutedData916, DivergentFates916,
ClaudeVerdictArtifact916, LogoOutro916). The two recordings use
**`pantry/B01-916.mp4` and `pantry/B05-916.mp4`**, re-composed by `make_ui.py`
as stacked rows (whole window above, a magnified loupe of the same frame below,
the loupe's region outlined on the window). Never centre-cut.

## The screen recordings — how they were made, what was changed

- **What:** the installed **Gavia 0.3.1** (`/Applications/Gavia.app`), run with
  `GAVIA_DATA_DIR` pointed at a scratch folder so Sai's own history in
  `~/Library/Gavia` was never opened. Recorded 2026-10-02 on an M2 Pro by ffmpeg
  (avfoundation screen capture, window crop 3040×1710, 60 fps). Driven by
  `ui/rec/take_batch.sh` and `ui/rec/take_updates.sh` (pointer moves and clicks,
  keystrokes into the file dialog). The app was not modified.
- **Cuts:** B01 drops the file dialog (it showed a long local path and an iCloud
  warning) and a scroll down the grid; each cut is a 6-frame dissolve. **No
  segment is sped up**: the check is shown in real time, which is what lets the
  narration say "about three and a half seconds".
- **Covered:** in B05, the Storage location field showed the scratch path
  (`/private/tmp/claude-501/…/gavia-take`). It is covered by a box reading
  "covered: scratch folder", tracked through the scroll by template matching
  every frame; the caption says so. The line "Set by GAVIA_DATA_DIR, so it can't
  be changed here." is left visible — it is true of this recording.
- **Restored afterwards:** the take turns the Updates switch off; Claude turned
  it back on through the accessibility API and confirmed it on after a relaunch
  (the switch lives in the app's WebKit storage, shared with Sai's real copy).
- **Theme:** the app is in Sai's own dark theme; nothing was changed for the
  recording.

## Evidence and honesty

Every number on screen was re-measured for this video and is kept in `evidence/`
(details in FACTCHECK.md, disagreements in SOURCES.md):

- `vitest.out` (257/257) and `cargo_test.out` (115/115) at `760e465` (v0.3.1).
- `batch_rules.out` — the shipped `selectImages()` on this reel's photos.
- `ui_batch.out` — the app's own per-photo results for the take, and the 3.52 s.
- `ui_network.out` — sockets the app held during both takes.
- `release_and_ci.out` — assets, update manifests, CI jobs on both tags.

Corrections the reel makes against the repo's prose:

- README says a "43 MB download"; the 0.3.1 DMG is **48,342,473 B = 46.1 MiB**.
  The reel shows no download size at all this week; logged for Sai to fix.
- The app says "20 MB" per image; the code's limit is **20 × 2²⁰ = 20,971,520 B
  (20 MiB)**. B03 typesets MiB and gives the byte count in its note.
- The 0.3.1 commit says it is "the first release an installed copy should update
  to on its own". Measured: CI **skipped** 0.3.0's update-manifest job; its
  `latest.json` was uploaded by hand (`nikhil-kunapareddy`, 04:03:20Z). 0.3.1's
  was the first CI published itself (`github-actions[bot]`, 04:52:49Z).
- The README says Gavia "finds 88% of labelled loons, and 91% of the boxes it
  draws are real loons" (val split). This reel makes no accuracy claim beyond
  what the app did to these 25 photos, and shows the false box.

**Continuity with last week's reel** (2026-09-25, B06): it ended "Next is survey
counting: a whole folder, one total, one CSV." This week's B00 and B06 say
plainly that only part of that shipped.

**Not claimed:** speed in general (only this run, this laptop); download counts;
"no network at all" (the update check is on by default and was measured).

## Attribution

All commits in the week window (after 2026-09-25 through `760e465`) are Sai's,
plus Dependabot branches that are not merged into `main`. No collaborator work is
narrated this week.

Photos: 26 Wikimedia Commons files (public domain, CC BY 2.0/4.0, CC BY-SA
2.0/3.0/4.0), authors and licences in `evidence/batch_manifest.json` and
DESCRIPTION.md; 25 of them are on screen.

## Attribution override

Hosted by Sai in his own name (B00 "This is Sai", B09 "Sai."), voice Kokoro
`am_onyx`, handle `@HumanitariansAI`. The guide's IN-FOR-BEAR LAW is deliberately
suspended for this series (`metadata.greeting_note`).

## Expected build noise (not bugs)

- `./art run` SKIN LINT asks for `ClaudeTitleOutro` — wrong for this channel (its
  handle is hardcoded `@NikBearBrown`); `LogoOutro` is deliberate.
- GATE V `underfill` on B07/B09 (centred cards); B09 declares `qc.sparse`.
- The portrait slate reports edge-bleed on every frame (its own burn-in); the
  verdict that counts is `./art final`'s gate on the clean candidate.

## Portrait-only edits (in `vertical/beat_sheet.json`, not the parent)

**None.** `shorts.py --vertical` output was rendered as derived; every portrait
beat passed the frame review (FACTCHECK.md) without a portrait-only string edit.
If a re-derive ever needs one, list it here and in BUILD-PROMPT.md.

## Human review checklist

- [ ] The ONE idea is the one you want, in your words.
- [ ] B01: the false box on photo-19 is fair to show — it is the app's real output.
- [ ] B05: "the only thing it sends over the internet" is the app's own wording;
      the reel adds what was measured (one socket, to GitHub, at launch).
- [ ] B06: you're comfortable saying the CSV and survey total have not shipped.
- [ ] B07 line 4: the hand-uploaded 0.3.0 manifest is OK to mention publicly.
- [ ] Commons credits in DESCRIPTION.md are complete before anything is posted.
- [ ] The narration below reads as you.

## Full narration, as it will be spoken

<!-- NARRATION:BEGIN (generated from beat_sheet.json) -->

### B00 · ASK — `ClaudeComposerAsk` · 16.8s measured (61 words)

> Last week I said Gavia's next step was survey counting: a whole folder, one
> total, one CSV. This week it got part of the way: twenty-five photos at once,
> or a zip of them. This is Sai. But a tool that takes a batch has to decide
> what happens to the photo that does not fit. That decision is this video.

### B01 · THE BATCH — screen recording (`make_ui.py`, take `batch`) · 19.1s measured (69 words)

> Here it is in the real app, with freely licensed photos: one zip, twenty-five
> pictures, three of them empty lakes. Gavia checks them one at a time; on this
> laptop, all twenty-five took about three and a half seconds. Its count: loons
> in twenty-three of twenty-five. The truth is twenty-two. Open the extra, and
> it is an empty lake, with a box on a pine branch at forty-one percent.

### B02 · THE FORK — `BinaryBranch` · 17.3s measured (64 words)

> Now the hard case. Pick twenty-six photos, and something has to give. The easy
> fix is to check the first twenty-five and drop one. But which one was dropped
> would be a guess, and a survey with a silent hole in it looks exactly like a
> complete one. So Gavia refuses the whole selection, says how many it counted,
> and lets the reviewer choose.

### B03 · THE RULE — `TypesetMath` · 18.9s measured (67 words)

> Here is the rule, from the source. Every image is counted, including the ones
> inside zips, before anything is checked. Twenty-five or fewer, and all of them
> are checked. One more, and none are. The zip limit follows from the same
> numbers: twenty-five images at twenty megabytes each is five hundred
> megabytes, so a zip bigger than any legal batch is turned away before it is
> opened.

### B04 · THE RUN — `ExecutedData` · 21.2s measured (69 words)

> I ran Gavia's own selection code on this video's photos. Twenty-five photos:
> all twenty-five go through. Twenty-six: none do, and the message says twenty-
> six. A zip of twenty-five plus one loose photo is refused the same way,
> because what is inside the zip counts. But a file it cannot read is different.
> Twenty-four photos and one oversized file: the twenty-four are checked, and
> the one left out is named.

### B05 · THE ONE CALL — screen recording (`make_ui.py`, take `updates`) · 20.1s measured (70 words)

> The other change came one release earlier: updates. When Gavia starts, it asks
> GitHub for a small file naming the newest release. If that is newer, it
> downloads it in the background, checks its signature, and offers a restart; it
> never restarts by itself. I watched its connections during this video's run:
> one, to GitHub, at launch, and none while the photos were checked. This switch
> turns even that off.

### B06 · AGAINST THE PLAN — `DivergentFates` · 16.3s measured (61 words)

> So how does this square with last week's plan? Part of it shipped: twenty-five
> photos per check, a Stop button, and a count of photos with loons. Part of it
> did not: there is no whole folder yet, no single total of loons, and no CSV.
> Those are next on the roadmap. The batch is the first step, not the survey.

### B07 · VERDICT — `ClaudeVerdictArtifact` · 15.4s measured (53 words)

> So: one page. Gavia checks twenty-five photos, or a zip, at a time, and its
> count still needs a reviewer. A twenty-sixth refuses the selection rather than
> guessing which to drop. A file it cannot read is left out, and named. And its
> one call home is an update check, with a switch.

### B08 · HANDOFF — `ClaudeComposerAsk` · 15.7s measured (60 words)

> Your turn. If something you are building has a limit, paste this before you
> ship it. Ask what happens at the limit plus one. If the answer is that
> something is quietly dropped, ask who would notice, and when. A refusal costs
> your user one more click. A silent drop costs them an answer that is wrong and
> looks right.

### B09 · OUTRO — `LogoOutro` · 2.4s measured (4 words)

> Refuse, don't guess. Sai.

**Total: 578 words** → 163.2s measured (2:43). No 180s cap applies to the --vertical cut; audio remains the master clock.

<!-- NARRATION:END -->

---

VERDICT: __________ — reviewer: ___ date: ___
