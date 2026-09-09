# BUILD-LOG — "BLIP: Noisier Data, Better Model?"

Built 2026-09-08 on the operator's Mac (Apple Silicon). Free/local end to end: Kokoro TTS,
Remotion, ffmpeg. Total spend **$0.00**.

Second reel in the fellows/ritik-b series, and deliberately built to be cheaper than the
first: the sibling reel's 16 layout defects almost all had one root cause — *sizes written
as magic numbers instead of derived from the safe box* — so that lesson is written into
`ReelKit.tsx`'s header comment and was applied from the first line of every new scene. The
defect count fell from 16 to 12, and none of the 12 were edge-bleed.

## The pipeline, as run

```bash
python3 author_sheets.py                                   # ONE beat list -> BOTH sheets
python3 runtime/scripts/generate_audio_kokoro.py <reel>     # Kokoro am_onyx, the clock
python3 conform_durations.py                               # measured length -> durationS
python3 runtime/scripts/remotion_scenes.py <reel>          # 11 beats, --scale=2 -> 4K
python3 runtime/scripts/compile.py <reel> --height 2160    # 9:16 twin: --height 3840
python3 runtime/qc/final_frame_check.py <reel>             # GATE V
```

Renders need the sandbox disabled on this machine (headless Chrome cannot launch sandboxed)
and `python3`/`ffmpeg` must be PATH-prefixed, since the toolkit scripts call the bare names
and non-login shells resolve them to CLT 3.9.6 and an Intel ffmpeg:

```bash
PATH="/Library/Frameworks/Python.framework/Versions/3.11/bin:/opt/homebrew/bin:$PATH" …
```

The `@rspack/binding-darwin-arm64` fix from the sibling reel's log was already in place and
held. No npm changes were needed for this build.

## What was built

| | |
|---|---|
| New scene components | 5 (`BlipMed`, `BlipCapFilt`, `BlipIndependence`, `BlipDiversity`, `BlipLadder`) |
| Promoted from the sibling reel | 3 (`ReelKit` ← `VqaKit`, `ReelExecSummary` ← `VqaExecSummary`, `ReelFramework` ← `VqaFourMoves`) |
| Compositions registered | 14 (7 components × 2 canvases) |
| Toolkit files modified | 1 (`Root.tsx`) + 3 converted to re-export shims |
| Beats | 11, all VIDEO, zero slates |

### The promotion, and why it is not just tidying

`VqaKit.tsx` was written for one reel and immediately needed by a second. Rather than copy
176 lines, the reusable half moved to `ReelKit.tsx` and `VqaKit.tsx` became a re-export shim
that keeps only `SceneGlyph` (genuinely VQA-specific). Same for the BLUF and framework beats.
`ReelFramework` gained two optional props — `accentIndex` and a per-row `receipt` — whose
defaults reproduce the sibling reel's render exactly, so its fourteen compositions and its
beat sheet were untouched and `tsc` stayed at its 5 pre-existing errors throughout.

The one place this diverges: `ReelExecSummary` also took a canvas-fill fix here (defect 1
below). The sibling reel's shipped snapshot is the pre-fix version, which is correct — that
is what its masters were rendered from.

## Content parity, by construction

The sibling reel maintained two hand-edited beat sheets and verified afterwards that they
had not drifted. This reel inverts that: `author_sheets.py` holds ONE beat list and emits
both sheets, with the portrait one a mechanical transform (slug, `aspect_ratio`, the `916`
pattern suffix). There is no editing step in which the cuts could diverge. The mp3s are
copied, not regenerated, so the two cuts are the same audio to the byte.

## Gates

| Gate | Where | Result |
|---|---|---|
| PROOF GATE (authoring) | `CHECKS-REPORT.md` | 11 SHOW / 0 HOLD / 0 PUNT; teaching arc complete |
| GATE P (narration) | `PEDAGOGY.md` | **PASS — self-signed by the build agent at the operator's instruction.** Not a human review; flagged in the README, `PROOF-REVIEW.md` and the PR body. |
| GATE L (beat mix) | `runtime/qc/beat_lint.py` | see below |
| GATE V (frame QC) | `runtime/qc/final_frame_check.py`, per orientation | see below |
| VISUAL QC LAW | `_qc/` frames read by hand, both cuts | see below |
| Runtime cap (≤ 2:00) | measured audio | **1:58.7** — the first pass was 2:02.3 |

## Narration: over the cap, then under it

The first Kokoro pass measured **122.33s**, past the operator's 2:00 ceiling. Kokoro expands
decimals, so a beat like B07 ("78.4 … 80.6 … 79.6") costs about nine more spoken words than
its written length suggests — the written total of 344 words was never the binding number.

Six beats (B01, B03, B05, B06, B07, B08) each lost one trailing clause, taking the reel to
**118.74s**. Nothing was cut from the evidence: every clause removed was a restatement of
something already on screen. B06's "the filter makes it affordable" survives as that beat's
closing card; it just stopped being said out loud as well.

## Defects found and fixed

Frames were sampled at ~88–94% of each beat's span — the point where every reveal has landed
— and **read**, per orientation. The mp4 probe was treated as a file check, not QC.

| # | Beat | Defect | Severity | Fix |
|---|---|---|---|---|
| 1 | B01 | roadmap cards are ~300px tall at 16:9 and their content was top-anchored, leaving a dead band under all three | MAJOR (canvas-fill) | card content centres in **both** orientations, not just portrait; numeral 52→58, label 31→34, body 28→31 |
| 2 | B03 | the three SA/CA/FFN chips sat at content height — ~150px of a ~700px card — with the loss footer pushed to the bottom by `marginTop: auto`, so the slack pooled in the middle of every card | MAJOR (canvas-fill) | each chip is `flex: 1 1 0` inside a growing stack, so the chips ARE the card; footer back to `flex: 0 0 auto`; chip type up ~15% |
| 3 | B04 | the whole left half of the beat was empty: a `safe.w × 0.17` image with captions beside it clustered in the top third | MAJOR (canvas-fill) | image to `safe.w × 0.30` landscape / `× 0.50` portrait and moved ABOVE the captions, so the captions get the panel's full width; the panel distributes with `space-between` |
| 4 | B04 | the filter's strike drew **between** two wrapped lines of `Tw` and read as an underline on the first — the verdict was illegible as a verdict | MAJOR (legibility) | captions are `nowrap` + ellipsis, so the background-gradient strike is unconditionally a strike-through instead of depending on the string and the canvas width |
| 5 | B04 | the strike then ran the full flex width, well past the last word — a rule, not a strike | MINOR | the text element is `flex: 0 1 auto`, so it sizes to its content and the strike ends where the sentence does |
| 6 | B04 | 20 caption tiles were 4:1 pills on a wrapping flex row and read as blank list rows, with a void above them | MAJOR (canvas-fill) | a CSS grid (`repeat(5, 1fr)` × `repeat(4, 1fr)`) that stretches to whatever the panel gives it, each tile carrying two grey bars so it reads as a caption; rejected tiles get a terracotta border AND the strike |
| 7 | B06 | 48px bars in ~200px row slots read as three thin lines floating in air | MINOR (canvas-fill) | `BAR_H` 48→68 landscape / 46→62 portrait |
| 8 | B07 | the axis caption was clipped mid-token — "ViT-B/1" — by `nowrap` + `overflow: hidden` in a `LABEL_W` box | MAJOR (legibility) | font 25→23 so it fits, `textOverflow: ellipsis` so a future longer string degrades **visibly** instead of silently, and the truncation disclosure moved onto the tick itself ("axis 77") where there is room |
| 9 | B07 | the axis-break glyph was 18×16 and read as a stray mark, colliding with its floor tick — a disclosure nobody can see is not a disclosure | MINOR | 30×26 on its own cream patch, drawn at the axis rule's weight in `INK_SOFT`, tick moved clear |
| 10 | B02 (9:16 only) | each axis row stacks in portrait and was `flex: 1` — ~375px of box for ~120px of content — so the slack fell between the detail line and the `receipt`, parking every receipt just above the NEXT axis's label. "§3.3" sat directly above "JUDGE" and read as its receipt | **MAJOR** (misattribution) | in portrait the receipt rides the label line (`justifyContent: space-between` on the label row) and rows are auto-height distributed by the container. Landscape is untouched. |

| 11 | B06 (9:16 only) | the closing line wrapped at a width **wider than the safe box** and lost a word to the stage's clip: "Sampling writes wh" / "is not." The axis disclosure was cut mid-word too ("COCO TR@1 — axis start") | **MAJOR** (legibility) | two fixes, one structural and one local. The axis labels **wrap** instead of `nowrap` + clip, so the disclosure survives the narrower portrait cell; and every Blip scene root got `minWidth: 0`. |

| 12 | B07 (9:16 only) | with defect 8's `textOverflow: ellipsis` guard in place, the portrait axis caption degraded **visibly** to "COCO 5K test · TR@1 · ViT…" — working as designed, but the truncated token was `ViT-B/16`, the control variable the entire ablation rests on | MINOR | the caption keeps only what fits the 350px portrait box ("COCO 5K test · TR@1") and the backbone moves to the `source` slot, which wraps and has the room. Nothing is lost on either canvas. |

Defect 12 is the ellipsis guard from defect 8 doing its job, and is included because the
outcome is the point: a *visible* truncation is not automatically an *acceptable* one. The
reel's narration says "same images, same backbone" — that clause is what makes the five bars
a valid comparison rather than five unrelated numbers — so `ViT-B/16` is load-bearing, not
metadata. Sizing the caption to the narrower canvas and moving the backbone to a slot that
wraps costs nothing and keeps every piece of the claim legible in both orientations.

Defect 11 took the longest to find and is the most transferable, so it is worth spelling
out. A flex item's *automatic minimum width* is its **min-content width**, not zero. The
axis row's two `whiteSpace: nowrap` cells made that row unshrinkable below its text, which
widened the scene's root column past `safe.w` — and once the root is wider than the safe
box, **every paragraph inside it wraps at the wrong width** and then gets clipped by
`Stage`'s `overflow: hidden`. The visible symptom (a truncated sentence three elements away,
in one orientation only) is nowhere near the cause (a nowrap label). Two lessons:

- `minWidth: 0` on a flex item is not defensive noise; without it, one unshrinkable
  descendant silently re-sizes everything around it. It is now on every scene root here.
- `whiteSpace: nowrap` + `overflow: hidden` is a legibility trade, not a layout fix. It
  buys a clean single line and pays with a silently truncated string on whichever canvas is
  narrower. Use it only where the string is short and authored, and pair it with
  `textOverflow: ellipsis` so the truncation is visible when it happens.

Defect 10 is worth generalising from too. It was invisible in landscape and invisible
in the beat sheet — the receipt was correct, attached to the right axis in the data, and
still read as belonging to a different claim on the 9:16 canvas. **A dual-orientation reel
has to be READ in both orientations; a component that is correct in one is not evidence
about the other.** Defects 10 and 11 were both 9:16-only, and both were invisible in the
beat sheet, in `tsc`, and in the landscape frames. Nothing but looking at the portrait frame would have caught it, which is
exactly what VISUAL QC LAW is for.

**Zero edge-bleed defects in either orientation.** That is the one class the sibling reel hit
three times, and the reason is structural, not luck: every size in every new scene derives
from `safe`, entrance animations use `translateY` (never `translateX`, which slides content
through the title-safe margin mid-entrance), and `ReelKit.Stage` clips its illustration band
so a layout bug surfaces as visible truncation rather than as ink past the edge on a 4K
master.

## Self-inflicted: a deleted temp file killed the render pass

Mid-render I deleted the stale landscape clips for five fixed beats so the pipeline's retry
pass would re-render them — and included `media/_ext_*.mp4` in the glob. `_ext_B09.mp4` was
being written by `extend_clip_to_duration` at that moment, so `shutil.move` raised
`FileNotFoundError` and took `remotion_scenes.py` down with it.

The retry loop found 6 missing beats and rendered them, so the crash itself cost nothing.
**The consequence, three steps downstream, is the part worth recording.** `B09.mp4` had
already been written by the render before the extend crashed, so the retry pass reported
"B09: filled already (skip)" and left it at the composition's full **30.06s** instead of the
beat's 11.88s. `compile.py` then did what it should with a clip three times too long — it
**centre-cut** it:

```
[art] B09: clip 30.1s center-cut to 11.9s (skip 9.1s head/tail)
```

Which silently deleted the beat's whole point. B09 is the HANDOFF, one of the only two beats
in the reel where typing is legal, and the centre cut started *after* the prompt had finished
typing: 11.9 seconds of a static card while the narration reads the prompt aloud. A PPT-test
failure that no gate would have caught, because the frame is perfectly legible — it is just
the wrong eleven seconds. It also broke parity: the portrait twin extended correctly to
11.90s, so the two cuts were running different clips for the same beat.

Found by comparing `media/` and `clips/` durations across both folders rather than by looking
at a frame. Fixed by forcing a re-render of landscape B09, and turned into a standing check:
**`check_clips.py`** in this folder asserts every clip is the length its beat asked for and
says which way `compile.py` will paper over the difference. It runs before the compile, not
after, because after the compile the evidence is gone.

Three lessons, in order of how much they cost:

- **`remotion_scenes.py`'s `_ext_*` files are live working state, not leftovers.** Deleting a
  beat's output to force a re-render is safe; globbing the temp files is not.
- **"filled already (skip)" is not "correct".** The retry loop checks existence, not
  duration. After any crash mid-pass, compare each beat's clip length against its
  `actual_duration_s` before trusting the pass.
- **`compile.py`'s centre-cut is a rescue, not a no-op.** When it prints "skip Xs head/tail"
  on a beat whose animation is front-loaded, it has thrown away the animation. Treat that log
  line as a defect report.

## Known-flaky, not caused here

`remotion_scenes.py` intermittently fails a beat with *"Could not find composition with ID
&lt;X&gt;. Available compositions: CodexComposerAsk"* — the script's own comments document it as
undiagnosed and unfixed by `--timeout`, and it succeeds on retry. The build script therefore
runs up to three passes; because the script skips beats whose media already exists, a retry
pass only re-renders what actually failed.
