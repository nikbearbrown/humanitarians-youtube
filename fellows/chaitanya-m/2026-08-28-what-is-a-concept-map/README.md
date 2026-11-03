# What Is a Concept Map

A research-log teardown of the Concept Map subsystem in `medhavi-hub` — what a
concept map is, why the review editor exists, and the finding that the verified
output it produces currently has zero consumers. Brutalist format: type, rule,
and diagram on a fixed frame, four colours, hard cuts only.

| | |
|---|---|
| **Runtime** | 3:48.86 (16:9) · 2:40.04 (9:16 short) |
| **Format** | 3840×2160 and 2160×3840, 24 fps, h264, yuv420p, bt709 |
| **Voice** | Kokoro `am_onyx` — local, free, no API · **predates the 2026-09-17 re-voice** |
| **Beats** | 10 · 9 script scenes + spoken intro · **no slates**, 10/10 filled |
| **Presenter** | Chaitanya M. |
| **Series** | Medhavy research log |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art), used read-only |
| **Status** | Built · QC'd · fact-checked · GATE P signed 2026-09-17 · **not published** |

## Through-line

The review pipeline is complete and correct. The consumption side is empty.

---

# How I made this

Seven steps, in the order they actually happened. Each one produced a file in
this folder, so the trail is inspectable rather than described.

## 1 — Audit the subsystem, then write the script

The video started as a code audit, not a topic. I read the Concept Map
subsystem in `medhavi-hub` end to end — the schema, the S3 layer, six API
routes, the editor client, the admin tab, both sample fixtures — and wrote up
what I found as [`script.md`](script.md).

Two rules I set for myself there, and they shaped everything downstream:

- **Every number on camera gets read off the code or the fixtures.** No
  estimates, no "roughly." The script's Appendix C maps each claim to a file and
  line at a specific commit.
- **The art direction is part of the script, not a later decision.** Palette,
  type scale, grid, and hard rules are written into the document before a single
  scene. That is what made the build mechanical later.

The script also decides what stays *off* camera: the import/permissions defects
I found are implementation bugs, not part of *what a concept map is*, so they
are held for a separate segment.

## 2 — Turn the script into a beat sheet

Nine scenes became beats B01–B09, unsplit and in order. B00 is the one addition
— a spoken intro the script doesn't have.

[`beat_sheet.json`](beat_sheet.json) is the source of truth: per beat, the
narration verbatim, the shot type, the motion, a timestamped `show` list of what
appears when, and the metadata block carrying voice, palette, fps, and canvas.
Narration is copied from the script **verbatim** — nothing paraphrased,
compressed, or added.

## 3 — Generate the narration first, because audio is the clock

```bash
python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py . --no-gate
```

This is the part that trips people up: **duration is an output, never a target.**
Kokoro speaks the narration, the measured length of each clip is written back
into the beat sheet as `actual_duration_s`, and the visuals conform to *that*.

The script targeted 5:15. The narration measured 3:48.86 — 96 seconds under. I
did not pad the gap with holds; that buys runtime with dead air. The shortfall
is logged in [`BUILD-LOG.md`](BUILD-LOG.md) with the per-beat drift table and
three honest options for closing it. [`timings.json`](timings.json) is
the measured clock everything else was cut against.

## 4 — Render the visuals out-of-tree

The constraint was "don't change anything in brutalist." Custom Remotion scenes
would mean editing `runtime/remotion/src/` and registering them in `Root.tsx` —
toolkit edits. So instead:

```bash
python3 scenes/render_scenes.py --aspect 16:9 --out media
```

[`scenes/render_scenes.py`](scenes/render_scenes.py) draws every frame
deterministically with Pillow and encodes with ffmpeg, natively at 3840×2160.
The output lands in `media/<beat>.mp4`, which is the **top** slot precedence in
`compile.py:resolve_slot()` — so the toolkit picks it up with no modification.

brutalist stayed read-only throughout: Kokoro narration, the conform/mux pass,
and the 9:16 derivation. Python deps went into a project-local `.venv`, never
the toolkit's. Verified with `git status` on the toolkit after every build.

Nothing here came from an image model. There are no image prompts to record:
the renderer executes the script's art-direction section as code, so re-running
it on the same inputs produces the same frames — no seed, no sampler, no model.
The brief it executes is the palette, type scale, grid, and hard rules written
into [`script.md`](script.md).

## 5 — Assemble, then actually look at the frames

```bash
cd <brutalist> && ./art final <this-folder>
```

Then QC — and the rule I'd underline: **an mp4 probe is a file check, not QC.**
I pulled frames with ffmpeg and looked at them against a 9-point rubric.

That found six defects, two of them MAJOR: the node table filling only ~32% of
frame height when the script says it "fills frame," and B08's three dependency
edges merged into one bus with a single arrowhead — which meant "the three red
edges remain" simply failed once the box was cut. Both were re-rendered and
re-inspected; zero BLOCKER and zero MAJOR remain. The four MINOR fixes were
panel-band proportions and portrait leading.

One defect was **not** fixed, deliberately: the script sets mono captions at
32 px, which lands near 9 px on a 1080p transcode. Those strings are exposed
technical furniture (`FIG. 03 — NODE RECORD`, `SOURCE: export/route.ts:62`),
not content, and the brief was to follow the art direction exactly — so they
stayed at spec. All content type is well clear of the floor. If mobile
legibility of the labels matters more than spec fidelity, raise the caption
tier to ~44 px in `render_scenes.py` (`Layout.caption`).

A later pass caught a seventh the first QC had missed: B04 opened with 7.5
seconds of empty chart, reading as failed media. The first pass sampled frames
at 55% and 92% of each beat and landed on settled states both times. **Sampling
settled states cannot find a bad opening.** Beats are now spot-checked near t=0
too.

## 6 — Derive the 9:16 short under the 3:00 cap

`shorts.py` planned the cut: B05 and B08 dropped as the longest unprotected
middle beats, B00 and B09 protected, endcard appended. Result: 2:40.04, twenty
seconds under.

Three of its defaults I overrode, each because the tool assumes a Claude-branded
reel and this isn't one — centre-cuts replaced with native portrait re-layouts
(a centre cut of 3840×2160 keeps 1215 px of width and would have destroyed the
bar chart), the auto-rewritten outro replaced because it spliced unspeakable
mid-sentence fragments, and the endcard rebuilt in this reel's palette. Full
reasoning in BUILD-LOG.

One thing worth knowing if you do this: **regenerate the outro before trusting
the cap arithmetic.** `shorts.py` first reported "STILL OVER" using a 20 s
*estimate* for the un-regenerated outro. The real audio was 15.30 s and no third
beat needed dropping.

## 7 — Fact-check against the source, at the commit

[`FACTCHECK.md`](FACTCHECK.md) re-verifies all 14 on-camera claims directly
against `medhavi-hub` @ `7f10aaa` — fixture counts recomputed from the JSON
rather than copied from the script, route behaviour read from the file, the
zero-consumers claim re-grepped.

Thirteen passed. **One failed**, and it's the reason this step is not optional:
the `wikipedia_categories` row on screen in B06 shows
`["Taxanes", "Antineoplastic"]`, but the fixture has
`["Taxanes", "Mitotic inhibitors", "Chemotherapy drugs"]`. It was flagged as
invented in [`SOURCES.md`](SOURCES.md) during the build and never checked. It's
never spoken aloud, so nothing said is false — but it is a fabricated value
presented as a real record, and it should not ship uncorrected.

---

## Beats

| Beat | | |
|---|---|---|
| B00 | Intro | "Hi, I am Chaitanya" — title card, the only beat not in the source script |
| B01 | Cold open | A TOC struck through — `THIS IS NOT A MAP` |
| B02 | Definition | Sequence vs. dependency — node = one teachable idea, edge = prerequisite |
| B03 | Anatomy of a node | The Paclitaxel record — `THE EDGE IS THE POINT` |
| B04 | Why humans | 9 high / 10 medium / 6 low — the pipeline marks its own weak spots |
| B05 | The four stages | Generate → import → review → export — `ZERO PENDING OR NOTHING` |
| B06 | What gets thrown away | Three fields stripped — `SCAFFOLDING ≠ CONTENT` |
| B07 | The honest finding | The pipeline that ends in nothing — `STORED, NOT SPENT` |
| B08 | The crack | Remove a load-bearing node, keep the edges — the dangling-edge defect |
| B09 | Close | Four lines, ending on `CONSUMERS = 0` |

Beat-by-beat timing, motion, and on-screen content: [`SHOTLIST.md`](SHOTLIST.md).

## What is in this folder

**Committed** — text only:

```
beat_sheet.json          the reel itself: every beat, its narration, its
                         visual, its measured duration, its build stamp
short/beat_sheet.json    the 9:16 cut, 2:40.04, capped under 3:00
timings.json             the measured clock — what the visuals conform to
short/timings.json       same, for the short
script.md                the source script: art direction, nine scenes, appendices
scenes/render_scenes.py  the renderer — deterministic, Pillow → ffmpeg
README.md                this file
SHOTLIST.md              beat-by-beat: timing, motion, what's on screen
FACTCHECK.md             every claim, its source, its verdict — one FAIL open
SOURCES.md               provenance: narration, on-screen strings, toolchain
PEDAGOGY.md              GATE P — signed, VERDICT: PASS; register, vocabulary,
                         and what was cut from the narration
BUILD-LOG.md             what actually happened, including revision 2
description.txt          YouTube description + chapter markers
.gitignore               enforces the media rule below
```

**Never committed** — these live outside the repo:

```
mp4/   the finished cuts         media/  per-beat 4K renders
mp3/   narration, one per beat   _qc/    QC frames and contact sheets
clips/ per-beat conform output
```

There is no `vertical/`. An early full-length 228.9 s 9:16 was built by
bypassing `shorts.py`, which was the wrong call — the 3:00 cap is a real
constraint. `short/` supersedes it and is the only 9:16 deliverable.

## Voice: this reel is the outlier

Built with Onyx (`am_onyx`), which was the series voice at the time. The series
moved to Bella (`af_bella`) on 2026-09-17 — an explicit re-voice decision
recorded in the [fellow README](../README.md#re-voice-decision--2026-09-17).

This reel stays `am_onyx` on disk. Re-voicing it is optional: audio is the
clock, so new narration changes every beat duration and forces a re-cut of both
masters. Worth doing if the series is ever published as a set.

## Open before publication

1. **B06 `wikipedia_categories` is wrong on screen** — see step 7 above.
   One-line fix in `scenes/render_scenes.py` → `NODE_ROWS_FULL`, then re-render
   B06 and re-cut.
2. **Runtime is 96 s under the script's 5:15 target.** Closing it means writing
   more narration for the thin beats (B02 and B03), not adding holds.
3. **Channel not assigned.** This reel carries no channel bug by design; it is
   neither `@NikBearBrown` nor `@HumanitariansAI` branded. The series handle
   needs confirming before upload.
4. **The audio has not been listened to.** Narration was verified as text
   (exact-match against the script) and as measured duration, not by ear. Nor
   does frame QC prove the reel is any good — pacing, whether a cut lands,
   whether the argument persuades. Those are human judgments and still open.
5. **The short's QC coverage is partial.** Frame QC was run against the
   superseded full-length 9:16. The portrait layouts carry over unchanged, since
   the short's slots came from the same renderer pass, so those fixes still
   apply. But two things in the short were never in the inspected set: the
   rebuilt endcard, and B09 with its rewritten outro narration. Those want a
   frame check before upload.

## A note on what this is not

This is a Brutalist reel, **not** a Claude-branded `ai-explainer`. No
`ClaudeComposerAsk` cold open, no verdict page, no HANDOFF beat, no
title-restate outro, no channel logo bug, and the Claude fidelity palette is not
used anywhere. Where the script and `ai-explainer` frame law conflicted, the
script won — every departure is enumerated with its justification in BUILD-LOG.
It should not be described as an `ai-explainer`.

## Rebuilding it

```bash
python3 <brutalist>/runtime/scripts/generate_audio_kokoro.py . --no-gate
python3 scenes/render_scenes.py --aspect 16:9 --out media
```

Then, from the brutalist checkout, `./art final <this-folder>` for the 16:9.
Audio first, always.
