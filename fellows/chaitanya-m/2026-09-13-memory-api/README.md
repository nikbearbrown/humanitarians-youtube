# Memory API — Medhavy Hub

How the Medhavy hub lets a tutor remember a student across different textbooks:
two endpoints, two tables, and one string that decides whether two books are
talking about the same person. Plus the honest finding — the machinery is built
and nothing is calling it yet.

| | |
|---|---|
| **Runtime** | 2:51.32 (171.32 s), both cuts |
| **Format** | 3840×2160 and 2160×3840, 24 fps, h264, yuv420p, bt709 |
| **Voice** | Kokoro `af_bella` — local, free, no API · the series voice from this reel onward |
| **Beats** | 7 · 6 deck scenes + sign-in · **no slates**, 7/7 filled |
| **Presenter** | Chaitanya M. |
| **Series** | Medhavy research log |
| **Built with** | [brutalist.art](https://github.com/nikbearbrown/brutalist.art), used read-only |
| **Status** | Built · fact-checked · GATE P signed 2026-09-17 · **not published** |

## Through-line

The cross-book mechanism is a naming convention, not identity resolution. It
works exactly as far as every book follows it — and right now, none do.

---

# How I made this

Seven steps, in the order they happened.

## 1 — Research the subsystem and write two scripts

I read the Memory API in `medhavi-hub` — the migration, both routes, the auth
helper — and wrote it up twice:

- [`script-longform.md`](script-longform.md) — the 7–8 minute version for
  developers joining the project, researched against `main` @ `efcc3f5`. This is
  the research document.
- [`script.md`](script.md) — the 2:50 cut that was actually filmed, ~400 words,
  paced to the deck.

Both open with the same warning, and it's the most useful thing in either: the
natural framing for this video is *"how a tutor remembers a student across
books"* — **verify that's true before you say it on camera.** The hub provides
the API, but the cancer textbook's architecture doc describes local SQLite. I
couldn't settle it at writing time, so the script carries two versions of
Scene 5 and an instruction to resolve it before filming.

## 2 — Build the deck as the real artifact

[`memory-api-deck.html`](memory-api-deck.html) is a self-contained 16:9
presentation deck — six scenes, auto-advancing, each with its duration in a
`data-dur` attribute. It sizes everything in container-query units (`cqw`), which
is the decision that made step 4 possible.

It's a usable deck in its own right: open it, press `F` then `Space`.

## 3 — Generate narration first, because audio is the clock

```bash
<venv>/bin/python <ART_HOME>/runtime/scripts/generate_audio_kokoro.py . --no-gate
```

Measured 171.32 s against the deck's 170 s of `data-dur`. The total is close;
the per-scene fit is not. B02, B03 and B05 overrun their windows by 1.6–3.0 s,
and the other three undershoot by 4–5 s.

Holding to `data-dur` would cut the narration off mid-sentence three times.
Holding the short scenes open would add ~13.7 s of silence. I cut the beats to
measured narration instead, which the script explicitly permits — *"Adjust if
your read runs long."* Full drift table in [`BUILD-LOG.md`](BUILD-LOG.md).

## 4 — Render the actual deck, don't reimplement it

```bash
python3 scenes/capture_deck.py --width 3840 --height 2160 --out media
```

Headless Chrome at a 3840×2160 viewport. Because the deck sizes in `cqw`, the
stage is *exactly* 3840×2160 and all type is vector-crisp — native 4K, not an
upscale. Every frame in B01–B06 is the real deck.

Two things had to be got right, both found by inspection rather than by reading
docs:

1. **`--virtual-time-budget` is not a clock.** Page load consumes the budget, so
   a nominal *t* lands somewhere later in the animation — a box with a 0.45 s
   delay was already fully visible at a nominal 200 ms. Replaced with explicit
   seeking: freeze all animations in CSS from frame one, then rewrite
   `animation-delay` to `(original − t)`.
2. **The deck declares `.d1`–`.d7` with `!important`**, so an inline style loses.
   The seek has to use `setProperty(..., 'important')`. Before that fix the
   `.rise` elements never appeared at all.

Freezing from frame one also killed a race where entrances finished during load
and the seek arrived too late — which had produced non-monotonic output, where
t=0.6 s showed *more* than t=1.3 s. Each frame is now a pure function of `t`.

## 5 — Derive the 9:16 the deck's way

`shorts.py` handled duration correctly on its own: 171.3 s is under the 180 s
cap, so it took the "full reformat, no beats cut" path. Nothing dropped.

Aspect handling needed intervention. The default centre-cut keeps a 1214 px
strip of a 3840 px frame — 68% of the width gone. On scene 2 that left the
headline missing, the left box empty, and `LEARNER_PROFI` truncated mid-word.
Every two-column layout in the deck breaks identically.

Fixed with `shorts.py`'s own documented escape hatch rather than an out-of-tree
crop: `pantry/<beat>-916.*` is "the human's slot, wins over every path," and the
tool prints exactly that remedy per beat. Portrait versions went there and it
re-ran reporting `pantry override` on all seven. The deck is scaled to 2160 wide
and letterboxed on its own paper white — **nothing cropped**.

I also dropped the endcard (`--no-endcard`). The default is the toolkit's
`@nikbearbrown` card — dark charcoal, serif, terracotta rule — which is the
wrong channel for this deck, and it was being upscaled from 1080×1920. The reel
already ends on its own RECAP scene.

## 6 — Fact-check after the fact

[`FACTCHECK.md`](FACTCHECK.md) checks all eight structural claims against
`medhavi-hub` @ `3775687`, reading the schema and routes directly. This is the
step [`SOURCES.md`](SOURCES.md) explicitly did *not* do — its claims table has
"Verified by this build?" as **No** on every row, because the build agent had no
repo access. It does now.

**Eight pass.** Two things the narration gets slightly wrong, and one it omits:

- **"Twenty-four turns, forty-eight rows" is a default, not a rule.** `maxTurns`
  is a caller-supplied field clamped to `[2, 100]`, defaulting to 24. A backend
  posting `maxTurns: 100` gets a 200-row window. The rolling-window *shape* of
  the claim is right; the numbers aren't fixed.
- **Auth is skipped in non-production.** B05 says "shared-secret auth," which is
  true — but if `MEMORY_API_SECRET` is unset, a non-production environment skips
  the check entirely. An omission rather than an error, flagged because someone
  wiring up a book could come away thinking otherwise.
- **Scene 5's flagged claim is confirmed**, and more strongly than the narration
  claims. See below.

## 7 — Build the chapter list with a validator, not by hand

A beat is not a chapter. B00 measures **7.98 s**, and YouTube requires every
chapter to be **at least 10 seconds**. One short chapter doesn't get dropped —
it **disables the entire list**, so the video publishes with no chapters and
nothing warns you. Caught in review, not by the build.

So short beats merge *forward*. Chapter one becomes sign-in + THE PROBLEM and
runs 29.19 s.

```bash
python3 chapters.py          # paste-ready list + a rule audit
```

[`chapters.py`](chapters.py) generates the list from `beat_sheet.json`, merges
any sub-10 s beat forward automatically, and **exits non-zero rather than
printing a list YouTube would discard**. It enforces all four rules: first
timestamp at 00:00, three chapters minimum, every chapter ≥10 s, ascending
order. It reads `actual_duration_s` only — never estimates — so timestamps
always match the rendered master. It's reel-agnostic; point `--sheet` anywhere.

If this reel is ever regenerated with different beat durations, re-run it and
replace the list in `description.txt`. The current timestamps are valid only for
the 171.32 s master.

Chapters don't apply to the 9:16 cut — at 171.32 s YouTube treats it as a Short,
and Shorts don't render chapter lists.

## The Scene 5 question — resolved

The build kept the PRIMARY narration and left the claim standing, correctly:
the script flags it, the operator hadn't confirmed it, and the primary version
states its own uncertainty aloud ("if that's still current"), so it's honest
either way.

**It's now confirmed.** The cancer textbook's doc set lives inside the hub repo
and says SQLite for memory across four files. And the supporting check is the
stronger one: `grep -rn "x-memory-api-secret"` across `medhavi-hub` returns
three hits — the auth helper that reads the header, and two docs telling future
authors to send it. **No caller.**

Two details sharper than the narration: the cancer book keys memory off a
**session cookie**, not `hub:{clerkUserId}`, and keeps **10** turns, not 24. So
it isn't one subject-string away from joining — it's a different identity model.

The alternate Scene 5 ("ONE STUDENT, MANY BOOKS") should **not** be substituted.
The evidence runs the other way. Caveat: only the book's *docs* are in this
repo, not its code, and `DEVELOPER.md:82` calls that doc set "partially stale" —
so this confirms the documentation, not the running system. The script's own
remedy (grep a book repo, or ask Prarthana) is still the definitive test.

---

## What is in this folder

**Committed** — text only:

```
memory-api-deck.html     the deck — this IS the visuals, not a mockup of them
beat_sheet.json          every beat: narration, shot, motion, measured duration
short/beat_sheet.json    the 9:16 cut, same 7 beats, nothing dropped
timings.json             the measured clock the beats were cut to
script.md                the 2:50 filmed script (+ the alternate Scene 5)
script-longform.md       the 7-8 min research version
scenes/capture_deck.py   the deck renderer — deterministic, Chrome -> ffmpeg
scenes/intro.html        the B00 sign-in card, built from the deck's own CSS
chapters.py              emits + VALIDATES the YouTube chapter list; refuses
                         to print one YouTube would silently discard
README.md                this file
SHOTLIST.md              beat-by-beat: measured vs data-dur, motion, on screen
FACTCHECK.md             every claim, its source, its verdict
SOURCES.md               provenance: narration, visuals, toolchain
PEDAGOGY.md              GATE P — signed, VERDICT: PASS
BUILD-LOG.md             what actually happened, including the two capture bugs
description.txt          YouTube description + chapter markers
.gitignore               enforces the media rule below
```

**Never committed** — these live outside the repo:

```
mp4/     the finished cuts        media/   per-beat 4K captures
mp3/     narration, one per beat  pantry/  the 9:16 portrait overrides
clips/   per-beat conform output  _qc/     QC frames
```

## Open before publication

1. ~~**Voice does not match the series.**~~ **Resolved 2026-09-17.** This reel's
   `af_bella` is now the series voice, recorded as an explicit re-voice decision
   in the [fellow README](../README.md#re-voice-decision--2026-09-17). Nothing
   to change here; the earlier Concept Map reel (`am_onyx`) is the outlier, and
   re-voicing it is optional.
2. **Palette and brand differ too.** This is `brutalist-deck` — ink `#000`,
   paper `#fff`, accent `#FFE500`, alert `#FF3B00`, Archivo Black + IBM Plex
   Mono — against the previous reel's four-value script palette and
   Helvetica/Menlo. Defensible, since the deck is the artifact and it came with
   its own design, but it means the series has two visual identities after two
   episodes. Worth settling now rather than at episode five.
3. ~~**GATE P is unsigned.**~~ **Signed 2026-09-17** by Chaitanya (operator).
   [`PEDAGOGY.md`](PEDAGOGY.md) now reads `VERDICT: PASS`. Note what the
   signature covers: the *narration*. It is not a sign-off on the fact-check
   items below, nor on frame-level QC, which was never written for this reel.
4. **Two narration inaccuracies** from the fact-check (the 24/48 default, the
   dev-mode auth skip). Neither is a re-cut in itself; both are now stated in
   `description.txt` so the video doesn't mislead unaddressed.
5. **Channel not assigned.** The reel carries no channel bug and
   `description.txt` names no handle. Needs confirming before upload.
6. **The audio has not been listened to**, and no frame-level QC report was
   produced for this reel — the source folder has `_qc/` frames but no written
   rubric pass, unlike the previous episode. Pacing, whether the letterboxed
   9:16 actually reads on a phone, and whether the deck's 62% `slam` motion mix
   feels monotonous are all open human judgments.
7. **`short/beat_sheet.json` metadata says `canvas: 3840x2160`** while
   `aspect_ratio` is `9:16` and the cut actually renders 2160×3840. Cosmetic
   metadata inconsistency, worth correcting for anyone reading the sheet.

## Rebuilding it

```bash
<venv>/bin/python <ART_HOME>/runtime/scripts/generate_audio_kokoro.py . --no-gate
python3 scenes/capture_deck.py --width 3840 --height 2160 --out media
```

Then `./art final <this-folder>` from the brutalist checkout for the 16:9, and
`shorts.py <this-folder> --no-endcard` followed by
`./art final <this-folder>/short --height 3840` for the 9:16 — pantry overrides
must exist first. Audio first, always.
