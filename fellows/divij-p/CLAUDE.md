# CLAUDE.md — humanitarians-youtube\fellows\divij-pawar

This directory is the **channel workspace** — where finished reels actually
live (`STEM1/`, `STEM2/`, …, `accountability-mesh/`, `chain-of-trust/`,
etc.). It is **not** the toolkit.

> **The toolkit lives at `C:\Users\divij\Desktop\mycroft\brutalist.art`.**
> All the actual code for video production — Manim scenes/renderer, Remotion
> components, Kokoro TTS, clip compilation, the `./art` CLI, font/graphics
> helpers — is there, not here. **It has its own `CLAUDE.md`** with its own
> project instructions; read that one too, don't assume this file's rules
> are the only ones in effect when you `cd` into `brutalist.art`. The two
> files aren't duplicates — this one governs what gets *produced and
> submitted* from this channel; `brutalist.art/CLAUDE.md` governs how the
> *tool itself* is built and used.

Read `brutalist.art/instructions.md` (human step-by-step) or
`brutalist.art/agents.md` (agent pipeline + exact text limits) before
building anything here; this file only covers **what's specific to this
channel's output** — deliverables, naming, format requirements, and the
authoring/QC discipline learned from building STEM1–STEM4.

---

## 1. Weekly deliverables

Two videos are expected every week:

| Video | Content | Filename pattern |
|---|---|---|
| **Weekly work video** | Recaps the work completed that week (see `accountability-mesh/`, `chain-of-trust/`, `three-files-twenty-one-tests/`, `when-two-agents-disagree/` for the established register) | `Mycroft_<YourName>_<Date>` |
| **Weekly STEM video** | Any AI & STEM topic (see `STEM1/`–`STEM4/` — currently an "Agents" series, but the slot isn't locked to that theme) | `<TopicName>_<YourName>_<Date>` |

Date format observed in this directory: `MM-DD-YYYY` (e.g. `08-24-2026`).
Zero-pad the month and day going forward for consistent sorting — some
earlier files used `8-14-2026` / `7-28-2026`; don't propagate the
inconsistency.

**Uploading to shared Drive:** the folder/item name uses the *undated*
project form — `<ProjectName>_<VolunteerName>` — distinct from the
per-file, per-week naming above. Don't conflate the two: the Drive folder
name doesn't carry a date, the video filename does.

---

## 2. Format requirements — every video, no exceptions

- **Resolution: 4K (3840×2160).** This is `compile.py --height 2160 --fps
  30` after rendering Manim at `-qk`. Never ship a 1080p file as final —
  1080p is only for fast preview cuts during iteration.
- **Both 16:9 and 9:16.** Every video — including anything that's
  conceptually a "Short" — must be rendered in **both** aspect ratios.
  Build the 16:9 master first (the whole pipeline in `agents.md` targets
  16:9 by default), QC it, then derive the portrait cut:

  ```bash
  ./art shorts <reel>        # derives the 9:16 cut, caps text, auto-shortens
  ```

  **The 9:16 variant has sharply tighter text limits** — `agents.md`'s
  "9:16 portrait" table shows `topic` dropping from ~125 to ~45 chars,
  `greeting` from ~55 to ~21, etc. Copy that fits the 16:9 canvas will not
  automatically fit portrait. Run `./art check` against the **derived**
  short's sheet, not just the source reel, and re-QC the 9:16 render
  separately — it is a different composition (`*916` pattern variants),
  not just the same footage cropped.
- **Exactly two final video files per reel, no more.** One 4K 16:9 master
  and one 9:16 shorts derivation — that's the complete deliverable set.
  Don't leave an unsubtitled master and a separately-named `_subtitled`
  copy both sitting in the folder as if either were a final output; mux
  captions directly into the one file that ships. Anything else produced
  along the way (fast 1080p preview cuts, intermediate Manim/Remotion
  clips) is scratch, not a deliverable — clean it up per §5/§9 of
  `BUILD-PROMPT.md`, don't ship it alongside the two real files.
- **Captions are soft-encoded on both final files, never burned in.** Mux
  as a real `mov_text` subtitle stream (see §5 step 9) into both the 16:9
  master and the 9:16 derivation — a viewer with subtitles off should see
  clean video, not hardcoded text baked into the frame. `captions.srt`
  stays in the folder as the source-of-truth subtitle file used to
  produce the muxed stream, not as a second delivery format.

---

## 3. Reel folder structure

Every reel gets its own folder here, matching the pattern established in
STEM1–STEM4:

```
<reel-slug>/
  0N_<slug>.md                  source script (verbatim, archival)
  0N_narration_tts_ready.txt    condensed, TTS-normalized narration by beat
  beat_sheet.json               single source of truth — beats, timing, shot specs
  PEDAGOGY.md                   GATE P — human sign-off, blocks audio generation
  SOURCES.md                    fact-check table, declared simplifications
  CHECKS-REPORT.md              nopunt SHOW/HOLD/PUNT classification + teaching-arc audit
  BUILD-PROMPT.md               paste-ready commands for this specific reel
  graphics_lib.py               house Manim helpers — copy unchanged, don't rewrite per reel
  scenes.py                     one Manim Scene class per GRAPHIC beat, named B<ID>_<Name>
  assets/                       any real photos/screenshots sourced for the reel (see §5)
  mp3/                          beat-B00.mp3 … (Kokoro output — ground truth durations)
  manim/                        rendered B<ID>.mp4 clips (compile.py reads ONLY this path)
  media/                        rendered Remotion bookend clips — same folder Manim
                                 caches into, so never `rm -rf media/` (see §6)
  clips/manifest.json           per-beat content hash — verify NO beat reads "slate"
  <slug>.mp4                    FINAL deliverable #1 — 4K 16:9 master, soft
                                 mov_text captions already muxed in. This is
                                 the only 16:9 file that ships — no separate
                                 unsubtitled copy, no separate `_subtitled`
                                 copy; caption-muxing happens in place.
  <slug>_shorts.mp4             FINAL deliverable #2 — 9:16 derivation from
                                 `./art shorts`, same soft-caption
                                 requirement, muxed in place the same way.
  captions.srt                  16:9 caption source (feeds the mux step;
                                 not itself a delivered format)
```

Exactly two video files ship per reel: `<slug>.mp4` and `<slug>_shorts.mp4`,
both already carrying soft-encoded captions. If a step's output doesn't
match this, something upstream was skipped — don't paper over it (e.g.
don't hand-splice a clip, don't fake a manifest hash, don't leave an extra
unsubtitled or `_subtitled`-suffixed file behind as a stray deliverable).

---

## 4. Script-writing & authoring discipline

**GATE P is a hard rule, not a suggestion.** `PEDAGOGY.md` must contain
`VERDICT: PASS`, signed by a human, before `generate_audio_kokoro.py` runs.
Kokoro is free, so this isn't a cost gate — once audio exists, its duration
becomes the master clock for every downstream render, so the gate exists to
catch teaching-arc and factual problems *before* that time gets spent.

**A script that only walks through one case study is not enough.** If a
review pass calls a script "thin," the fix is to add genuinely
**transferable** frameworks — a decision test the viewer can apply to their
own work, a named architecture choice, a derivation method for the specific
mechanism being shown — not to pad the existing walkthrough. Give the
falsifiability beat its own moment: show where the approach breaks or gets
misused, not just where it works.

**Verify claims about any real external project against the live source.**
If a script describes a real system (a GitHub repo, a paper, a product),
fetch it — README, docs, actual numbers — before finalizing. Specific
figures, scope claims, and mechanism descriptions that can't be found in
the real source get corrected or dropped, not carried as fact because they
sounded plausible. Log corrections and citations in `SOURCES.md` (DOUBLE-CHECK
LAW). When a real, permissively-licensed asset exists (a project's own
documentation photo, a real diagram), prefer it over a generic drawn
stand-in — it's a stronger nopunt HOLD than an invented illustration, as
long as it's attributed.

**No PUNT costumes.** Per nopunt: a generic stock image or icon standing in
for a concept is a PUNT. Either it's a genuine archival photo/screenshot of
the real thing being discussed (a legitimate HOLD), or it's a diagram that
actually enacts the sentence in motion (a SHOW). "A stock photo of a
handshake" is neither.

**One idea per beat**, framework stated before the worked example that uses
it, and every claim-bearing beat carries its own on-screen artifact — no
beat should be a headline read over a static paragraph (the PPT test).

---

## 5. Build & retiming pipeline (summary — see `agents.md` for full detail)

1. Write `beat_sheet.json`, gate docs, `scenes.py`.
2. Get GATE P signed.
3. Generate audio (`generate_audio_kokoro.py`) — durations are ground truth.
4. **Retime every Manim scene's `self.wait()` calls against the real
   `actual_duration_s`, not the pre-audio estimate.** Don't assume your
   estimate was close — measure the *built* scene's actual runtime (render
   at `-ql`, `ffprobe` the duration) before deciding whether to add or trim
   time. This session's scenes came out shorter than estimated by 3–15
   seconds each; assuming the opposite direction would have caused
   `compile.py` to center-crop content unnecessarily. Spread added/trimmed
   time across several of the longer holds near a beat's end rather than
   dumping it all into one hold — a single 15–20s static frame reads as
   dead air even when narration is still playing over it.
5. Render Manim at `-qk` (4K), copy into `manim/<BID>.mp4` — Manim's own
   cache path is not where `compile.py` looks.
6. Render Remotion bookends. Never `rm -rf media/` after Manim scenes
   change — it also deletes the Remotion clips living in the same folder.
7. Compile at `--height 2160 --fps 30`. Check the retiming lines it
   prints — a stretch factor over ~1.15x means a scene needs more
   `self.wait()`, not a bigger stretch tolerance.
8. Derive the 9:16 cut (`./art shorts`) — see §2.
9. Captions last, after the final compile (`align.py` then `make_srt.py`),
   muxed as a real `mov_text` subtitle stream, not burned in — into BOTH
   `<slug>.mp4` and `<slug>_shorts.mp4` directly, in place. Don't produce a
   separate `_subtitled` copy of either file; the muxed file *is* the final
   deliverable. That's the complete output: two files, both captioned.

**Two real, recurring defect classes to watch for** (both caught this
session by actually looking at rendered pixels, never by the render
succeeding):

- **Layout collisions from `next_to()` assumptions.** `next_to(line, DOWN)`
  centers under a mobject's *midpoint*, not an endpoint — two labels
  positioned this way under the two ends of a forked line collided into
  each other. Anchor off explicit coordinates when precision matters.
  Check every element against the safe frame bounds (~x: -6.4 to 6.4, y:
  -3.6 to 3.6 in Manim units for 16:9) — an arrow or label positioned by
  formula, not verified by rendering, is exactly the kind of thing that
  runs off-canvas.
- **Default Manim `Text()` kerning is loose for Montserrat specifically.**
  `graphics_lib.py`'s `label()`/`title()`/`serif()`/`mono()` now apply a
  tuned `letter_spacing` correction automatically (Montserrat tightened,
  EB Garamond lightly tightened, PT Mono left alone to preserve column
  alignment) — this is already fixed at the source, don't re-derive it or
  bypass `label()`/`title()` with a raw `Text()` call for body copy.

---

## 6. Visual QC — mandatory, not optional

The mp4 probe (duration, resolution, frame count) is a **file** check, not
a **pixel** check. It has never once caught a real layout defect. Before
calling any reel done:

1. Extract frames across the whole compiled master (`ffmpeg -vf fps=2` or
   denser), not just the beats you think you changed.
2. Actually read the PNGs against the 8-point rubric in
   `brutalist.art/CLAUDE-CODE-VISUAL-QC-CHECK.md`: edge bleed, title-safe
   margins, container overflow, overlap/collision, offscreen anchors,
   legibility, brand bug, aspect/letterbox.
3. For dense or newly-added scenes, sample **mid-scene** frames too (render
   a low-quality video, extract at 1s intervals), not just the settled
   final frame — a collision that only exists while other elements are
   still on screen won't show up in a final-frame-only check.
4. Fix defects in the source (`scenes.py` / beat-sheet props), never by
   hand-editing the rendered mp4. Re-render only the affected beat,
   re-compile, re-check.
5. Repeat for the 9:16 derivation separately — it's different geometry,
   not a guaranteed-clean crop of the 16:9 pass.

---

## 7. Self-review before submission — PROOF.md

`PROOF.md` (in this directory) is a reviewer protocol built on one rule:
**no source, no verdict.** An explainer that asserts without showing is
broken, in two specific ways PROOF hunts for:

- **Empty center** — a thesis bolted onto examples with no *shown* method;
  the framework is narrated after the fact instead of demonstrated, or its
  categories map suspiciously one-per-example (reverse-engineered to fit
  whatever cases were already on hand).
- **Invisible evidence** — the artifact under discussion is illegible or
  off-screen at the moment the claim about it is made. A video that argues
  "no source, no verdict" and doesn't show its own sources on screen is
  self-refuting.

PROOF reviews from **pasted frames at the moment of each claim + the
narration/transcript** — it doesn't watch the finished file. Before
submission, self-run it: pull the `_qc/frames/` PNGs from §6 at each
claim-bearing beat, pair each with that beat's `narration_text` from
`beat_sheet.json`, and score honestly.

**The rubric (0–2 each, total /12):** explicit framework shown before the
examples · a reusable rubric a viewer could apply to a new case · a worked
example walked through live (the reasoning, not just the conclusion) ·
falsifiability — the framework stress-tested against a counterexample or
ambiguous case · an active task (never "ask Claude" with no scaffold) ·
friction — the viewer resolves a real tension, not just receives facts.

**The production gate (binary — vetoes publish regardless of rubric
score):**
- Evidence legible at the moment of assertion (no sub-40%-opacity fades, no
  center overlap, no clipped labels, text scaled to its segment).
- Sources on screen, not just voiced — every factual claim carries a
  visible source or artifact.
- Side-by-side at the moment of comparison, held ≥2 seconds, whenever the
  script claims "X says A but reality is B."

**Ship rule:** public requires **teaching ≥ 8/12 AND production gate PASS
AND the video passes its own stated standard.** Anything short of that
ships **unlisted, not public** — log the gap as `unlisted-until-fixed` with
the specific beat/frame and fix, not a vague "needs polish" note.

**This substantially overlaps with what §4 and `CHECKS-REPORT.md` already
track** — nopunt's FRAMEWORK/WORKED-EXAMPLE/FALSIFIABILITY/SCAFFOLDED-TASK
checklist maps directly onto four of PROOF's six rubric criteria. Treat
`CHECKS-REPORT.md` as where that overlap gets caught *during* authoring,
and the PROOF pass as the final, adversarial check before submission — not
a redundant re-derivation. Where PROOF adds something new: the binary
production gate (legibility/sourcing/side-by-side, all frame-specific,
independent of teaching quality) and the numeric ship threshold.

Log the self-review itself (even briefly) — e.g. `_qc/PROOF-REVIEW.md` —
scored against the rubric and gate above, with the ship verdict. Treat it
as an additional gate alongside GATE P (§4) and the visual QC pass (§6) —
it doesn't replace either; a video can pass GATE P and still fail here on
legibility or an empty-center framework.

---

## Companion references

- `brutalist.art/instructions.md` — human step-by-step build guide (exact
  commands, this machine's environment quirks: `python3` Store-alias
  bug, ffmpeg PATH, `npx.cmd` fix).
- `brutalist.art/agents.md` — full agent pipeline, exact per-field text
  limits (16:9 and 9:16), rebranding template, end-to-end checklist.
- `brutalist.art/CLAUDE-CODE-VISUAL-QC-CHECK.md` — the frame-level QC
  rubric referenced in §6.
- `brutalist.art/tips.txt` — hard-won specifics (font registration, glyph
  gaps, box auto-sizing, frame-bounds gotchas) from building the first
  reels in this channel.
