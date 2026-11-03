# BUILD-LOG — Memory API (Medhavy Hub)

**Built:** 2026-09-13
**Sources:** `../memory-api-deck.html` · `../memory-api-script-2min.md`
**Toolkit:** brutalist — used **read-only** (`git status` identical before/after)
**Voice:** Bella — Kokoro `af_bella` (hai persona)

## Outputs

| Cut | File | Resolution | Frames | Duration |
|---|---|---|---|---|
| 16:9 | `memory-api.mp4` | **3840×2160** | 4111 | 171.32 s |
| 9:16 | `short/memory-api-short.mp4` | **2160×3840** | 4111 | 171.32 s |

Both 24 fps, h264, yuv420p, bt709. Both exactly 8,294,400 px — the UHD count.

## How the visuals were made

The deck was **rendered, not re-implemented**. Chrome headless at a 3840×2160
viewport; the deck sizes everything in `cqw`, so the stage is exactly 3840×2160
and all type is vector-crisp — native 4K, not an upscale.

Per scene: a standalone HTML copy with that `<section>` pre-marked `.on` and the
deck's controller stripped, so nothing resets the active scene. All animations
are frozen in CSS from the first frame, then seeked to an exact time by
rewriting `animation-delay` to `(original − t)`.

Two things had to be got right, both found by inspection:

1. **`--virtual-time-budget` is not a clock.** Page load consumes the budget, so
   a nominal *t* lands somewhere later in the animation — the `d2` box (0.45 s
   delay) was already fully visible at a nominal 200 ms. Replaced with explicit
   seeking.
2. **The deck declares `.d1`–`.d7` delays with `!important`**, so an inline
   style loses. The seek must use `setProperty(..., 'important')`. Before this
   fix the `.rise` elements never appeared at all.

Freezing animations in CSS from frame one also removes a race where entrances
finished during load and the seek arrived too late — that race produced
non-monotonic output (t=0.6 s showed *more* than t=1.3 s).

Entrances are sampled at true 24 fps until they settle (1.3–3.3 s per scene);
after that the deck is static, so the settled frame is captured once and held.
The progress rail is composited afterwards by ffmpeg across each beat's real
duration, so it still reaches 100% exactly at scene end.

Visuals land in `media/<beat>.mp4` — top slot in `compile.py:resolve_slot()` —
so the toolkit consumes them with no modification.

## Timing: narration vs the deck's `data-dur`

**The narration does not fit the deck's windows.** Three scenes overrun:

| Beat | measured | `data-dur` | delta |
|---|---|---|---|
| B00 | 7.98 s | — | added sign-in beat |
| B01 | 21.21 s | 26 s | −4.79 |
| **B02** | **31.59 s** | 30 s | **+1.59** |
| **B03** | **36.43 s** | 34 s | **+2.43** |
| B04 | 21.95 s | 26 s | −4.05 |
| **B05** | **33.02 s** | 30 s | **+3.02** |
| B06 | 19.14 s | 24 s | −4.86 |
| | **171.32 s** | 170 s | **+1.32** |

Holding to `data-dur` would cut Bella off mid-sentence on B02, B03 and B05.
Holding the three short scenes open to `data-dur` would add ~13.7 s of silence.

Resolved by the script's own instruction — *"Scene durations live in the
`data-dur` attribute… **Adjust if your read runs long**"* — so beats are cut to
measured narration. The **total** lands at 171.32 s against a 170 s deck and a
2:50 target: **+1.32 s**. Per-scene, it drifts as tabled above.

If exact per-scene `data-dur` fidelity matters more than an unhurried read, the
three overrunning beats fit their windows at `--speed 1.06 / 1.08 / 1.11` — a
5–11% faster read, against the script's "read at a normal pace, don't rush."

## Scene 5 — primary narration kept

The **PRIMARY** narration is used. The alternate was **not** substituted, per
instruction: the script flags the local-SQLite claim as possibly stale and the
operator has not confirmed it. The primary version states the uncertainty aloud
("if that's still current", "finding out which side it's on is the first thing
to check"), so it is honest under either outcome. See PEDAGOGY.md and SOURCES.md.

Switching later is **not** just an audio swap — it also needs the deck headline
changed from `BUILT ≠ WIRED` to `ONE STUDENT, MANY BOOKS` and the two status
panels replaced with the flow.

## The 9:16 cut

Run through `shorts.py`, brutalist's native path.

- **Duration handling worked as intended.** `171.3 s < 180 s cap` → "under the
  cap → full reformat, **no beats cut**." Nothing dropped, nothing condensed.
- **Aspect handling did not.** The default centre-cut keeps a 1214 px strip of a
  3840 px frame and discards 68% of the width. On scene 2 that left a fragment:
  headline gone, the left box empty, `LEARNER_PROFI` truncated mid-word. Every
  two-column layout in this deck (`grid2`, `statusgrid`, `endgrid`, `keyline`)
  breaks the same way.
- **Fixed with `shorts.py`'s own override**, not an out-of-tree crop: the tool
  documents `pantry/<beat>-916.*` as "the human's slot, wins over every path",
  and prints exactly that remedy per beat. Portrait versions were placed there
  and `shorts.py` re-run; it reported `pantry override` for all seven beats.
  The deck is scaled to 2160 wide and letterboxed on its own paper white —
  **all content preserved**, nothing cropped.
- **Endcard removed** (`--no-endcard`). The default silent endcard is the
  toolkit's `@nikbearbrown` card — dark charcoal, serif, terracotta rule — which
  is the wrong channel for a Medhavy Hub deck, and it was being upscaled from
  1080×1920 to 2160×3840 (the tool warned about this itself). The reel already
  ends on its own RECAP scene, so the endcard added nothing but a miscredit.

Tradeoff to be aware of: letterboxing means the deck occupies about a third of
the vertical frame. That is the honest cost of a 16:9 deck in a 9:16 slot —
the alternative loses two thirds of every slide.

## Chapters — B00 must NOT be its own chapter

**A beat is not a chapter.** B00 (the spoken sign-in) measures **7.98 s**, and
YouTube requires every chapter to be **at least 10 seconds**. A single
under-length chapter does not get dropped — it **disables the entire chapter
list**, so the video publishes with no chapters and nothing warns you.

This was caught in review after the build, not by the build. The fix is to
merge B00 forward into chapter one, which then starts at `00:00` and runs
29.19 s. Published list, verified against the measured master:

| Timestamp | Chapter | Length |
|---|---|---|
| 0:00 | Sign-in + THE PROBLEM | 29.19 s |
| 0:29 | TWO TABLES | 31.59 s |
| 1:00 | THE KEY | 36.43 s |
| 1:37 | ROLLING WINDOW | 21.95 s |
| 1:59 | BUILT ≠ WIRED | 33.02 s |
| 2:32 | RECAP | 19.14 s |

Shortest chapter 19.14 s; total 171.32 s, exactly the master's runtime.

`chapters.py` in this folder regenerates and **validates** that list from
`beat_sheet.json`, merging any sub-10 s beat forward automatically and exiting
non-zero rather than emitting a list that would be silently discarded:

```bash
python3 chapters.py            # prints the paste-ready list + a rule audit
```

It reads `actual_duration_s` only — never estimates — so timestamps always
match the rendered master. It is reel-agnostic; point `--sheet` at any beat
sheet.

**If this reel is ever regenerated with different beat durations, re-run
`chapters.py` and replace the description's list.** The timestamps above are
valid only for the 171.32 s master described at the top of this file.

Chapters do not apply to the 9:16 cut: at 171.32 s YouTube treats it as a
Short, and Shorts do not render chapter lists.

## Toolkit lints, not silenced

- **`SKIN LINT: NO RENDERABLE BEATS`** — no beat carries
  `shot.remotion.pattern`. Expected for browser-captured visuals; it then
  reported `7/7 filled … VIDEO`. A false positive for this architecture.
- **`'slam' carries 5/8 beats (62%) — over the ~40% cap`** (on the endcard
  build) — the motion labels are read off the deck's own animation classes
  (`.slam`, `.wipe`, `.rise`), so they are accurate. Relabelling to satisfy a
  linter would misdescribe the deck.

## Reproduce

```bash
# 1. audio (the clock)
<venv>/bin/python <ART_HOME>/runtime/scripts/generate_audio_kokoro.py . --no-gate

# 2. visuals — renders the actual deck
python3 scenes/capture_deck.py --width 3840 --height 2160 --out media

# 3. 16:9 master
cd <ART_HOME> && ./art final <this-folder>                      # 3840x2160

# 4. 9:16 short (pantry overrides must exist first)
python3 <ART_HOME>/runtime/scripts/shorts.py <this-folder> --no-endcard
cd <ART_HOME> && ./art final <this-folder>/short --height 3840  # 2160x3840
```
