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
  16:9 by default), QC it, then derive the portrait companion:

  ```bash
  ./art vertical <reel>      # required weekly companion: full report, no cap, no endcard
  ./art shorts <reel>        # OPTIONAL separate derivative: can cut beats, caps duration
  ```

  **`vertical` and `shorts` are not the same artifact.** Per
  `brutalist.art/docs/PIPELINE-SAFETY.md`: the required full-length 9:16
  companion is `./art vertical` — it keeps every beat and the full report,
  applies no Short duration cap, and adds no endcard. `./art shorts` is a
  *separate*, optionally-produced derivative that can plan cuts to ordinary
  middle beats to hit a Shorts-length target, but still cannot silently drop
  a supplied source report to meet that cap. Don't ship a `shorts` cut as if
  it satisfies the weekly vertical-companion requirement — it's a different
  video with a different duration budget.

  **The 9:16 variant has sharply tighter text limits** — `agents.md`'s
  "9:16 portrait" table shows `topic` dropping from ~125 to ~45 chars,
  `greeting` from ~55 to ~21, etc. Copy that fits the 16:9 canvas will not
  automatically fit portrait. Run `./art check` against the **derived**
  vertical/short's sheet, not just the source reel, and re-QC that render
  separately — it is a different composition (`*916` pattern variants),
  not just the same footage cropped.
- **Exactly two final video files per reel, no more.** One 4K 16:9 master
  and one 9:16 vertical/shorts derivation — that's the complete deliverable
  set. Don't leave an unsubtitled master and a separately-named `_subtitled`
  copy both sitting in the folder as if either were a final output; mux
  captions directly into the one file that ships. Anything else produced
  along the way (fast 1080p preview cuts, intermediate Manim/Remotion
  clips) is scratch, not a deliverable — clean it up per §5/§9 of
  `BUILD-PROMPT.md`, don't ship it alongside the two real files.
  **Stop producing the dated `<slug>_DivijPawar_<date>.mp4` duplicate** —
  every reel from STEM4 onward has shipped this as a byte-identical copy
  of `<slug>.mp4`, apparently to satisfy Drive naming. It doesn't: §8's
  Drive convention (from `FELLOWS-SUBMISSION.md`) is explicitly *undated*
  — `ProjectName_VolunteerName.mp4`, no dates, no `v2`/`final`. The dated
  copy is both an undocumented extra file and a violation of the actual
  naming rule. Rename in place for Drive upload; don't keep both.
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
                                 copy, no dated duplicate (see §2); caption-
                                 muxing happens in place.
  captions.srt                  16:9 caption source (feeds the mux step;
                                 not itself a delivered format)
  short/                        full PARALLEL pipeline for the 9:16 cut, not
                                 just a derived file — its own beat_sheet.json,
                                 scenes.py, graphics_lib.py, manim/, media/,
                                 mp3/, clips/, captions.srt, all scoped to
                                 the short's own (possibly trimmed) beat set
  short/<slug>-short.mp4        FINAL deliverable #2 — 9:16 derivation,
                                 hyphenated singular `-short` suffix (not
                                 `_shorts`), same soft-caption requirement,
                                 muxed in place the same way, no dated
                                 duplicate
```

Exactly two video files ship per reel: `<slug>.mp4` and
`short/<slug>-short.mp4`, both already carrying soft-encoded captions. If a
step's output doesn't match this, something upstream was skipped — don't
paper over it (e.g. don't hand-splice a clip, don't fake a manifest hash,
don't leave an extra unsubtitled, `_subtitled`-suffixed, or dated file
behind as a stray deliverable).

---

## 4. Script-writing & authoring discipline

**GATE P is a hard rule, not a suggestion.** `PEDAGOGY.md` must contain
`VERDICT: PASS`, signed by a human, before `generate_audio_kokoro.py` runs.
Kokoro is free, so this isn't a cost gate — once audio exists, its duration
becomes the master clock for every downstream render, so the gate exists to
catch teaching-arc and factual problems *before* that time gets spent.

**A second, separate gate now covers voice choice and any Professor Bear
notes beat** (`brutalist.art/docs/PIPELINE-SAFETY.md`). Declare exactly one
persistent Kokoro voice in `metadata.voice`/`metadata.voice_kokoro` — no
inferring approval from a suggested voice or file existence. Run
`./art approvals /path/to/reel --fingerprints` to print the review subjects
(this is not itself an approval), then record real sign-offs in
`metadata.approvals` with `status`, reviewer name, an ISO timestamp, and the
exact fingerprint reviewed — start those records `"pending"`, never invent a
signature. Pending, missing, or stale approval records block Kokoro
generation, Remotion rendering, review assembly, and final export outright;
`--no-gate` cannot bypass it, and changing the voice or notes text
invalidates the prior approval.

**A script that only walks through one case study is not enough.** If a
review pass calls a script "thin," the fix is to add genuinely
**transferable** frameworks — a decision test the viewer can apply to their
own work, a named architecture choice, a derivation method for the specific
mechanism being shown — not to pad the existing walkthrough. Give the
falsifiability beat its own moment: show where the approach breaks or gets
misused, not just where it works.

**Verify claims about any real external project against the live source —
but know which series that applies to.** STEM-series videos are conceptual
explainers, not project accounts: they do **not** need to match Divij's
real codebase, and should be fact-checked against general/standard
practice, not gated on whether a specific repo implements what's being
explained. **Mycroft weekly work-recap videos are different** — they
describe real, current work, so their claims must check against the actual
code at `D:\Code\mycroft\verification-layer`. Do **not** check either
series against `C:\Users\divij\Desktop\mycroft\accountability_layer` — that
is an older/draft location with similarly-named modules (`claims.py`,
`verification.py`, `consistency.py`) that caused a mis-fact-check on STEM6
when it was checked against by mistake. For any other real system named in
a script (a GitHub repo, a paper, a product), fetch it — README, docs,
actual numbers — before finalizing. Specific figures, scope claims, and
mechanism descriptions that can't be found in the real source get corrected
or dropped, not carried as fact because they sounded plausible. Log
corrections and citations in `SOURCES.md` (DOUBLE-CHECK LAW). When a real,
permissively-licensed asset exists (a project's own documentation photo, a
real diagram), prefer it over a generic drawn stand-in — it's a stronger
nopunt HOLD than an invented illustration, as long as it's attributed.

**No PUNT costumes.** Per nopunt: a generic stock image or icon standing in
for a concept is a PUNT. Either it's a genuine archival photo/screenshot of
the real thing being discussed (a legitimate HOLD), or it's a diagram that
actually enacts the sentence in motion (a SHOW). "A stock photo of a
handshake" is neither.

**Run the example instead of shopping for a picture of it.** Per
`brutalist.art/docs/EXECUTABLE-EVIDENCE.md` (mandatory, not optional): for
code, arithmetic, tables or toy examples, run the local code/data, preserve
the exact code/environment/seed/stdout/stderr, and render the real result —
don't fabricate a screenshot, terminal photo, or invented output. Reserve
pantry for genuinely irreplaceable source evidence (an actual historical
photo, document, or external recording), not as a shortcut for something
that could be computed and shown.

**Math gets typeset, not narrated in prose.** Per
`brutalist.art/docs/MATH-TYPESETTING.md` (mandatory for every film,
including Mycroft/STEM): any equation or derivation uses a structured
renderer (MathTex/KaTeX/MathJax/etc.) with real fraction bars, subscripts,
and sized delimiters — never raw TeX or ambiguous `a / b * c` strings in a
text card. Verify the algebra itself (signs, indices, domains, at least one
reproducible numerical case) separately from the typography, and inspect
the actual equation frames at 15/50/85% of the beat in the shipped aspect
ratio before calling it done.

**Write `narration_text` for Kokoro's punctuation weighting, not just for
reading.** Kokoro (`generate_audio_kokoro.py`) has no SSML/break-tag
support — it synthesizes raw text and lets the model's own prosody decide
pause length per punctuation mark, and that weighting is flat: a comma
gets barely less pause than a period, so a long compound sentence reads as
a rushed run-on with no real breath. Two concrete rules for every
`narration_text` string in `beat_sheet.json`:

- **One clause per sentence, terminated with a real period.** Don't join
  two complete thoughts with a comma or a semicolon hoping for a natural
  breath — split them into two short sentences. Periods are the only
  punctuation mark that reliably buys a real pause from this model.
- **Never rely on an em dash (`—`) for a dramatic beat.**
  `generate_audio_kokoro.py`'s `normalize_for_tts()` silently rewrites every
  em dash to a plain comma (`", "`) before synthesis — a script that reads
  "the model failed the test — twice" for a hard stop will be *heard* as a
  throwaway comma pause. If the beat needs a genuine dramatic pause, write
  it as two sentences, or use an ellipsis (`...`) for a held beat — don't
  spend an em dash on pacing, it does not survive to the audio.

Check this by ear, not just by reading the beat sheet: listen to the
rendered `mp3/beat-<ID>.mp3` for any beat with a compound sentence or a
dash before treating that beat's audio as final — a script that scans fine
on the page can still come out of Kokoro as a rushed, poorly-enunciated
run.

**If a beat still comes out slurred after the text fixes above, try
`--speed 0.92`–`0.95` on just that beat** (`generate_audio_kokoro.py
<reel> --only <BID> --speed 0.94`) before rewriting it again. A slightly
slower rate gives the model more time per phoneme to articulate consonant
clusters instead of running them together — cheap to test since Kokoro is
free and regeneration costs nothing but time. Don't apply a global
`--speed` across the whole reel for one bad beat: a reel-wide slowdown
throws off every other beat's already-tuned Manim retiming (§5 step 4).

**One idea per beat**, framework stated before the worked example that uses
it, and every claim-bearing beat carries its own on-screen artifact — no
beat should be a headline read over a static paragraph (the PPT test).

**Cut the "it's not X, it's Y" AI-speak contrastive tic.** This construction
(and cousins like "here's precisely why," "worth sitting with," "this
sounds obvious, it isn't") recurred on both STEM6's and STEM7's drafts from
the source-drafting pipeline at
`C:\Users\divij\Desktop\mycroft\accountability_layer\youtube\` — it's a
systemic pattern in that pipeline's output, not a one-off. Proactively scan
narration for it when authoring `0N_<slug>.md` / `0N_narration_tts_ready.txt`
from that source, even when not explicitly flagged, and vary sentence
rhythm instead (a direct statement, a rhetorical question, a dash) without
changing meaning or facts.

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
- **`./art shorts`'s auto-drop plan ("cheapest beats under the cap") ships
  incoherent cuts by default.** It has produced a short that opens
  mid-mechanism with a dangling reference to a beat it just cut, on STEM5,
  STEM6, and STEM7 in a row — each reel's own `BUILD-PROMPT.md` just noted
  "same failure STEM<n-1> flagged" and manually overrode it with
  `--drop`/`--keep` to rebuild a self-contained arc (cold open + one
  fully-illustrated beat + verdict + task + outro). Check the auto-drop
  plan before accepting it, every time — don't wait to discover it fresh
  per reel.

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

Log the self-review itself (even briefly) — **at the reel root, e.g.
`PROOF-REVIEW.md` next to `CHECKS-REPORT.md`, never under `_qc/`** — scored
against the rubric and gate above, with the ship verdict. `_qc/` is deleted
by `BUILD-PROMPT.md`'s own cleanup step (`rm -rf "$REEL/_qc" ...`); logging
there means the record doesn't survive the pipeline that's supposed to
produce it — only STEM5 has a surviving `PROOF-REVIEW.md` out of every reel
built so far, and every later one lost it to cleanup. Treat this log as an
additional gate alongside GATE P (§4) and the visual QC pass (§6) — it
doesn't replace either; a video can pass GATE P and still fail here on
legibility or an empty-center framework.

---

## 8. Weekly handoff — GitHub for source, Drive for media

Per `brutalist.art/docs/FELLOWS-SUBMISSION.md`, this channel's build output
and the actual weekly submission are two different things — building the
two files in §3 is not itself the handoff.

- **Every video opens with the required line**: "Hi, I am [name] and this
  video is about [topic]." Keep it even under a branded bookend. Disclose
  AI narration and whose work is presented — never let an AI voice pass as
  a recording of you or Professor Brown.
- **GitHub gets source only, under 25 MB per file**: beat sheet, script,
  README, `scenes.py`, checks, prompts. Never drag `mp3/`, `manim/`,
  `media/`, `clips/`, or the rendered `.mp4`s into the repo — prepare a
  source-only folder first.
- **Drive gets every rendered file**, even small ones: both final `.mp4`s,
  named `ProjectName_VolunteerName.mp4` (no dates, no `v2`/`final`) with
  landscape and vertical in separate folders so same-named files don't
  overwrite each other. Record each exported file's SHA-256 and source
  commit so a reviewed export can be matched back to its recipe.
- **Browser-only upload**: branch off `main` (named for you), upload the
  source-only folder under `fellows/`, commit with a real message, open a
  PR (`base: main` ← your branch) linking both the source and Drive folder,
  then notify your PM with both URLs. Merging into `main` is a maintainer
  decision, not implied by pushing your branch.
- **README template** (per file, at the reel root pushed to GitHub): this
  week's contribution, human vs. AI work breakdown, what was rejected or
  unverified, Brutalist version/commit used, both Drive links + SHA-256,
  and PM/publication status left as `pending` — never invented sign-offs.
- **PM review covers six gates** before it moves to the Q playlist: current
  format followed, native 4K verified (including the post-upload YouTube 4K
  playback check — not provable locally), both aspect ratios present,
  legible on desktop and mobile, the required intro line present, and a
  specific viewer takeaway. Queue placement is not final publish approval —
  that's Professors Brown and Nina's call.

---

## 9. Opening beat and last-3-beats template

Every reel in this channel — STEM and Mycroft alike — shares one opening
template and a common "keep the true final beat simple" rule, verified
against `brutalist.art/skills/make/ai-explainer/SKILL.md`,
`brutalist.art/skills/make/fellows/SKILL.md`, and the actual `beat_sheet.json`
of STEM7 and Mycroft7. The two series diverge in the beat immediately before
the outro — don't copy one series' closer onto the other.

**Opening — B00, identical shape both series (COLD OPEN LAW):** a single
`ClaudeComposerAsk` Remotion beat, `act: "cold open"`. Props: `command` (the
question the whole video answers), `topic` (short caps label), `segment`
(the episode title), `greeting` (a world-language hello + name, e.g. "Olá,
Divij" / "Hola, Divij" — rotate the language per episode, never `"Hello,
Divij"` every time), `runningText` (a short present-participle status line),
`output` (2–3 resolved lines, the *last* of which is the hook the whole
video pays off — don't bury the hook in line 1), plus the fixed
`folderLabel`/`modelLabel`/`effortLabel` chip. This is the reel's title
card and its thesis-in-miniature; it is never a custom Manim animation.

**STEM series — last 3 beats:**
1. **Verdict** (`ClaudeVerdictArtifact`, `act: "verdict"`) — `artifactTitle`
   "Summary", `artifactHeading` (the one-sentence takeaway), `artifactLines`
   (3–4 bullets synthesizing the episode, not a beat-by-beat recap).
2. **Your Turn** (`ClaudeComposerAsk`, `act: "your turn"`) — same pattern as
   the cold open but `greeting: "Your turn."`; `command`/`output` form a
   scaffolded task the viewer can actually run (never a vague "ask Claude").
3. **Outro** (`ClaudeTitleOutro`, `act: "outro"`) — `title` (exact episode
   title restate), `handle` (`@DivijPawar`), `subline` (one short imperative
   sentence). No stats, no bullets — the verdict beat already carried them.

**Mycroft weekly-recap series — last 3 beats (OUTRO-LAW convention,
confirmed across Mycroft6/Mycroft7 precedent):**
1. **Chapter close / honest ledger** (Manim, e.g. `act: "chapter 5b..."`) —
   the "still not true" / open-items beat: what's still unresolved, held on
   screen uncleared, never softened into a win.
2. **Close — the dense end-card reprise** (Manim, `act: "close - ..."`) —
   this is where the payoff density lives: reprises the cold open's own
   hook card exactly, then 5–7 END CARD bullets synthesizing the whole
   episode's real numbers/claims. This beat carries the stats; the true
   final beat deliberately does not.
3. **Outro** (`ClaudeTitleOutro`, `act: "outro"`) — same shape as STEM's:
   title restate, handle, subline, **kept free of stats on purpose** since
   the previous Manim beat already carried the dense content. Mycroft
   reels do **not** get a "Your Turn" beat — that's a STEM-series-only beat
   (the `fellows`/Mycroft skeleton has no handoff-task slot at this
   position).

**The shared rule, regardless of series:** the true final Remotion beat
(`ClaudeTitleOutro`) is always the simplest beat in the reel — title,
handle, one line. Whatever beat sits second-to-last (verdict artifact for
STEM, end-card reprise for Mycroft) is where the dense synthesis actually
lives. Don't invert this by cramming stats into the outro card or leaving
the second-to-last beat thin.

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
- `brutalist.art/docs/FELLOWS-SUBMISSION.md` — the actual weekly handoff:
  GitHub/Drive split, README template, PM review gates (§8).
- `brutalist.art/docs/PIPELINE-SAFETY.md` — the `vertical`/`shorts`
  distinction (§2), report-audio preservation, and the voice/notes approval
  gate (§4).
- `brutalist.art/docs/MATH-TYPESETTING.md` and
  `brutalist.art/docs/EXECUTABLE-EVIDENCE.md` — mandatory rules for any
  math or code-output beat (§4).
- `brutalist.art/skills/make/ai-explainer/SKILL.md` and
  `brutalist.art/skills/make/fellows/SKILL.md` — the source doctrine for
  the opening/closing beat template in §9.
