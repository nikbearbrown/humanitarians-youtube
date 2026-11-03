# HAI tool-tutorial pipeline — the shared playbook

**Read this before starting any video, in any series.** Every rule here was paid
for once already, on the Suno series (3 videos, Aug 2026). Nothing is theoretical.

Toolkit: `D:\Rohan\Claude\HAI\RohanClaudeHAIbrutalist.art` (brutalist.art)
Series:  `D:\Rohan\Claude\HAI\<program>\youtube\<tool>-part-N\`

Per-series companions:
- `<program>/youtube/<TOOL>-UI-SPEC.md` — the element-by-element UI ground truth
- `<program>/youtube/SERIES-PLAN.md` — scope, video count, what each part owns

---

## 0. Non-negotiables

- `export PYTHONUTF8=1` before **every** python step. Windows cp1252 corrupts the
  beat sheet's en-dashes and typographic quotes, and crashes scripts that print them.
- **Every master ships at 3840x2160. No exceptions.**
  The one way to break that: calling `runtime/scripts/compile.py` directly, whose
  `--height` argument defaults to 720. Nothing in this pipeline calls it directly —
  `bash art final <reel>` is the only compile path and it forces `--height 2160`.
  The default is recorded here as a guardrail, not as a description of output.
  **Verify after every compile:** `ffprobe -v error -select_streams v:0
  -show_entries stream=width,height -of csv=p=0 <master>` must print `3840,2160`.
- **Never run two Remotion renders at once.** They fight over the same headless
  Chrome and one deadlocks silently. This cost 13.7 hours on Suno Part 1: the job
  sat at ~10 CPU-seconds total while I waited for a notification that never came.
  One render at a time, and verify by checking the output file — never by waiting.
- **Never publish.** The master stays in the reel folder.
- **No screen recordings, ever.** All UI is rebuilt as native Remotion scenes
  (REBUILD LAW). Screenshots are reference only and never appear in a frame.

---

## 1. The build order

Steps 2a-2c are one unit. Splitting them is what desynced Suno Part 1.

```
1.  beat_sheet.json          author show blocks FIRST, then narration + cues.json anchors
2a. generate_audio_kokoro.py writes actual_duration_s back into the beat sheet
2b. align.py                 THE WORD CLOCK -> mp3/words.json
2c. sync_cues.py             resolves anchors -> props.cues + prints frame counts
3.  Root.tsx                 durationInFrames = round(actual_duration_s * 30)
4.  npx tsc --noEmit         cheap; catches scene errors without a render
5.  remotion_scenes.py --force
6.  bash art final <reel>    the 4K master
7.  final_frame_check.py     Gate V, then LOOK at the frames yourself
```

Re-run **2b, 2c, 3** after *any* narration change, however small.

---

## 2. Sync — the thing that bit hardest

Scenes animate on fractions of `durationInFrames`. Authored by hand those
fractions are guesses, and guesses drift. Measured drift on the first Suno cut:

| cue | guessed | measured | error |
|---|---|---|---|
| "Song Description" | 0.28 | 0.559 | **~6.1s early** |
| "Home" | 0.06 | 0.268 | ~4.5s early |

**Two conditions must both hold:**

1. Cues come from the word clock. `cues.json` maps cue names to anchor phrases;
   `sync_cues.py` resolves them against `words.json` and writes fractions into
   `beat_sheet.json` at `shot.remotion.props.cues`. Scenes take an optional
   `cues` prop with authored fallbacks.
2. `durationInFrames` **equals** `round(actual_duration_s * 30)`. A few frames off
   stretches every fraction. `sync_cues.py` prints the right number per beat.

Anchors: a distinctive 2-4 word phrase. Single common words mis-anchor. Validate
every anchor resolves against its narration before audio lock — a reworded line
silently orphans its anchor.

---

## 3. Layout — use the kit, never hand-roll coordinates

`runtime/remotion/src/scenes/sunoKit.tsx` is the reusable chassis (the name is
historical; it is not Suno-specific):

- `SceneFrame` owns the vertical rhythm (kicker / title / spark) and hands you a
  `CONTENT` rect of **x 96, y 174, w 1728, h 768**.
- `splitStage()` derives an app-window + annotation-rail split whose right edge
  lands on the safe edge **by construction**.
- `PaperGround` — the cream page with laid-paper texture. Carries `zIndex: -1`;
  that is load-bearing (see §6).
- `Callout`, `WaveBars`, `SunoWindow`, `SunoModal`, `SUNO` tokens.

**For a new tool, build the equivalent of `sunoAdvancedPanel` early.** When five
beats show the same product panel, five hand-rolled copies drift. One shared
component built from the UI spec cannot.

**Title-safe: x 96-1824, y 54-1026.** Nothing readable crosses it.

---

## 4. Gate V — how it actually measures

**What Gate V does NOT check.** It measures the SAFE boundary, canvas fill and
surface contrast. It has no notion of a child overflowing its parent. On
Midjourney Part 1 three annotation cards rendered their last line of body text
*below their own border* and the gate passed the frame twice — the text was well
inside SAFE, so nothing tripped. **Any card with a FIXED height and flowing text
needs a crop check**, because that defect is invisible to every automated gate
in the pipeline. The fix is to derive the height from what is left over AND to
budget the copy for it: title + N lines + padding, measured, not eyeballed.


- **Canvas fill is a BOUNDING-BOX test**, not pixel density: `bbox/SAFE >= 0.55`,
  sampled at **50% and 85% of every beat**. The composition must already span the
  safe area by the halfway frame — land structural surfaces early, resolve
  *content* later.
- **`INK_DELTA = 28` per channel.** `CLAUDE.CARD` (#FFFFFF, delta 10) and
  `CLAUDE.BORDER` (#E5E2D9, delta **28** — not strictly greater) do **not** count
  as ink on the cream page. A white card with a hairline border is invisible to
  the gate. Give it a terracotta rule or a dark fill.
- **Judge the settled state.** Mid-transition frames legitimately show translucent
  overlays; the rubric excludes them. Re-sample ~1.5-3s after a cue before calling
  something a defect.
- Its `low-contrast` check compares *surfaces*, not text against its own
  background. Measure before believing it — on Suno it flagged a card that was
  WCAG AAA at 9.0:1.

Reveal structure **early and dimmed**, emphasise later. Inactive elements hold at
~0.52 opacity on cream — but see the opacity rule in §6.

Readable annotation text **>= 24px**. App chrome may sit at 15-22px as texture.

---

## 5. Render performance

At `--scale=2` (3840x2160) anything covering the whole frame is paid for on every
frame of every beat.

| full-frame treatment | cost |
|---|---|
| none | ~2.6 min/beat |
| live SVG `feTurbulence` | **never finished one beat in 50 min** |
| pre-rendered tile + `mix-blend-mode` | ~8 min/beat |
| pre-rendered RGBA tile, normal compositing **(current)** | ~5.8 min/beat |

- Never use an SVG filter as a full-frame layer. Bake it to a bitmap once.
- Avoid `mix-blend-mode` on a full-frame layer. Multiplying a tint by a grey tile
  is *exactly* compositing black at `alpha = 1 - L/255`, so bake grain into the
  ALPHA channel instead. Verified pixel-identical (max channel diff 0).
- **Budget ~6 min/beat.** A 12-beat part is ~70 minutes. Run it in the background,
  and check the output file rather than waiting for a notification.

---

## 6. Failure modes that fake success

- **A beat can fail silently.** `remotion_scenes.py` prints `FAIL: <Scene>` and
  **still exits 0**, leaving the previous `media/<BID>.mp4` in place. A stale beat
  compiles happily into the master. **Always** read the render log AND diff
  `media/` timestamps before compiling. This fired twice on Suno; the second time
  the beat was missing entirely, not stale.
- **A render that never STARTED also exits 0.** On Midjourney Part 1 the job was
  launched with `--scale=2`; that is not an argument `remotion_scenes.py` accepts
  (it hardcodes `--scale=2` internally, see the script's own render call), so
  argparse rejected it, printed a usage block, and the background task reported
  **exit code 0 / completed**. Nothing rendered. The `media/` directory did not
  even exist. Treat "the task finished" as no evidence at all: the only proof of
  a render is **files on disk with fresh timestamps**.
- **A long render is not yet a running render.** Remotion bundles before it
  renders, so for the first minute or two there are node processes and *no*
  chrome workers. Do not read "no chrome" as a deadlock during that window —
  check that `media/` starts filling instead.
- **Never EDIT scene source while a render is bundling.** Remotion bundles the
  whole of `Root.tsx` and everything it imports on every invocation, so a scene
  file saved mid-bundle can be picked up half-written — and the failure would
  land in a beat whose source now looks correct. On midjourney-part-2 an edit
  and two `npx tsc --noEmit` runs during a bundle also starved it badly enough
  that the render did not begin for **26 minutes**. Diagnose the difference by
  process start time, not by elapsed wall time: fresh node PIDs mean it is
  working, not hung.
- **NEVER open a file in `media/` while a render is running.** On Windows a
  read handle blocks a rename. `remotion_scenes.py` finishes each beat by
  writing `media/_ext_<BID>.mp4` and `shutil.move`-ing it over
  `media/<BID>.mp4`; an `ffprobe` on `media/*.mp4` at that instant raised
  `PermissionError: [WinError 32]` and **killed the whole render after one
  beat**. The partial victim looked plausible — right dimensions, 2 frames
  short — which is worse than an obvious failure. Wait for the render task to
  report done, then probe. Checking on a render is not free.
- **A hung render looks like a slow one.** Check CPU seconds on the chrome workers.
  A live 4K render burns thousands; a deadlocked one sits near zero.
- **Paint order.** Absolutely-positioned elements paint ABOVE static content, so a
  full-frame background covered an outro's title and subline — the handle survived
  only because its `opacity: 0.9` created a stacking context. Backgrounds carry
  `zIndex: -1`.
- **A scene-level fade can encode a BLACK FRAME.** Putting `opacity` on an
  `AbsoluteFill` *including its background* makes frame 0 fully transparent, which
  encodes as pure black. Beats are hard-concatenated, so that is a one-frame flash
  on the cut. **Fade the content, never the ground.** Detect it by sampling the
  first frames of the BEAT mp4, not the master — one frame is easy to step over.
- **Partial opacity is direction-dependent.** A dark surface at 0.3-0.6 alpha over
  the cream page composites to a flat grey slab that reads as a rendering error.
  A translucent cream card over a dark app window turns to mud. **Dark surfaces
  are opaque or absent; cards over dark windows stay opaque and de-emphasise with
  a filter or clip-wipe.** Both directions shipped as defects on Suno.
- **A child of an absolutely-positioned box is ALREADY relative to it.**
  `MjEditorWindow` positioned its container at `left: x, top: y` and then its
  children at `left: x + RAIL + PAD`, `top: y + PAD`. `x` and `y` were applied
  twice, so the tool column landed 96px right and 174px down: it overlapped the
  canvas, collided with the Layers panel, and lost its bottom card to
  `overflow: hidden`. **Gate V and `tsc` both passed it** — the box still spans
  the safe area and the arithmetic is valid TypeScript. It survived to a
  delivered master.
  Three defences, in order of strength:
  1. **Take the props out of scope.** Destructure as `x: winX, y: winY`, use
     them on the outer div only. A stray `x` in a child is then a compile error.
  2. **`bash art coord-lint`** (`runtime/qc/coord_lint.py`) flags `x - x`
     no-ops as blockers and the double-application shape as a warning. A
     coordinate no-op is never intentional — it is written by someone unsure
     which space they are in.
  3. **Assert the layout arithmetically before rendering.** Reproducing the
     component's maths in ten lines of Python and printing every inter-element
     gap costs seconds and catches what a 4K frame takes 25 minutes to reveal.
  Sibling containers legitimately share a page-space offset, so the lint's
  additive warning has real false positives — read them, do not silence them.
- **Never draw an explanatory mark over recreated UI from outside its window
  container.** A magenta "datum line" drawn outside the window painted across the
  panel and read as a stray red bar. Annotation belongs on the cream rail;
  anything inside the window must be part of the product being depicted.
- **Zod `.default()` on a shared component breaks other reels.** It makes the prop
  *required* in Remotion's `defaultProps` type. Use `.optional()`.
- **Composition too short = a frozen still.** `remotion_scenes.py` freeze-holds the
  last frame to fill any gap. 300 frames against 21s of narration is ~11s of still
  image. This is why step 3 exists.
- **A regex written through nested string layers gets silently corrupted.**
  Authoring a checker via `bash heredoc -> python string -> file` put a literal
  BACKSPACE (0x08) into a pattern, because `` is a valid Python escape in a
  non-raw string. The pattern became `r'<BS>Part\s+\d<BS>'` and never matched,
  so an exemption I had just written did nothing and the checker kept reporting
  warnings I thought I had silenced. Python emitted `SyntaxWarning: invalid
  escape sequence` and I skimmed past it. **Never skim a SyntaxWarning**, and
  verify a written regex with `sed -n '<line>p' file | cat -A` before trusting
  its output. It failed loud rather than silent this time - the checker
  over-reported. The same corruption in a pattern used to FORBID something
  would have failed open.
- **A reference document can itself carry the error.** A UI spec put two menu
  entries on one line of a code block; a line-count then read "four submenus" when
  the product has five, and that reached a narration draft. When a spec states a
  COUNT, write the count out explicitly and put one item per line.
- **A fact fix is never one edit.** Correcting a count meant changing the
  narration, the spark line, the scene's ring set AND the annotation rail copy.
  After any factual correction, grep the scene for the old number and the old
  wording — hardcoded copy does not follow the data. This bit three times.
- **Heteronyms will be mispronounced and you cannot hear it.** Kokoro read "where
  the actions **live**" as /laɪv/. Prefer rewording over a phonetic gamble. Scan
  narration before audio lock for: live, read, lead, bow, close, record, present,
  use, wind, tear, object, produce, contract, content, subject, separate, minute.

---

## 7. Register and content rules

- **Internal volunteer training, not promotion.** Never sell the organisation's
  generosity or the vendor's product. State access mechanically, once.
- **Host:** opens "Hi, I'm Rohaan from Humanitarians AI"; full name spoken
  **exactly once**, in the outro. Phonetic spellings for Kokoro are deliberate —
  `Rohaan` = Row-Haan. Do not "correct" them.
- **Body beats ~45-70 words.** The screen carries evidence; the voice carries
  judgment. Author the `show` block before the narration.
- **End card:** episode title restated, handle beneath, name in small print.
- **Every on-screen claim goes in `FACTCHECK.md`**, with a "deliberately NOT
  claimed" section for research that was excluded.
- **Never put a version number on screen.** It dates the video, and third-party
  sources routinely disagree about which version is current.
- **Do not commit the series to a video COUNT in narration** until the scope is
  settled. Suno Part 1 said "the first of three training videos", which later
  forced a cramped Part 3 rather than a clean split.

---

## 8. Evidence discipline — the rule that mattered most

**Nothing goes on screen that is not in a capture.** Every factual error that
shipped in the Suno series came from secondhand evidence — web research, a prior
note, or a summary of a screenshot rather than the screenshot itself:

| shipped error | source of the error |
|---|---|
| a "Custom" tab that does not exist | help docs lagging a product rename |
| "Extend adds +15s or +30s" | a blog; the real control is a KEEP/RECREATE split |
| a five-item menu | memory; the real menu has ten |
| a "Regenerate" button | invented |

The fix is procedural, not attentional:

1. Read every capture **first-hand** before authoring. Not an agent's summary of
   it, not your own earlier notes.
2. Write the `<TOOL>-UI-SPEC.md` element by element, one item per line, counts
   stated explicitly.
3. **Verify the beat sheet against the spec with a script**, not by eye — element
   coverage, beat order vs product order, and any count the narration asserts.
4. Keep a "known gaps" list in the spec. If a beat needs an element that is not
   captured, request the capture; do not infer it.
