# BUILD-PROMPT.md — zero-for-sixteen

Paste-ready build for this reel, end to end. Never publishes; the master
stays in this folder. **16 beats (B00–B15)** — see CHECKS-REPORT.md
"Beat-count deviation" for why this isn't the ai-explainer default of 10.

## Precondition — GATE P

`PEDAGOGY.md` currently reads **`VERDICT: PENDING`**. A human must read it,
resolve the open checklist items at its end (the runtime — cut from an
original ~12:55 to ~8:19 using the script's own cut-to-6:00 guidance, see
PEDAGOGY.md "Runtime — recomputed, then cut" — and the B12/B13 Chapter-7
split), replace that line with `VERDICT: PASS`, and sign it **before**
running Step 2. Kokoro is free, so this is a quality gate, not a cost gate.

The signature also covers the deviations logged in PEDAGOGY.md / SOURCES.md:
the beat count (16, not 10 or the prior reel's 15), the original B15
sign-off line not present in the source script, the ~8:19 post-cut runtime
and the three specific items cut from it (B03's timings, B06's
`_latest_value` case, B11's stale-ledger footnote — all three still
recorded in SOURCES.md), and the one-file git-status drift (56 scripted vs.
57 measured at build time).

## Environment (every new shell)

`./art run` shells out to `python3`, which on this machine is a Microsoft
Store alias, not the real interpreter — it prints "Python was not found"
and silently no-ops. Use the explicit path below.

```bash
export PATH="/c/ffmpeg:$PATH"
export PYTHONUTF8=1
PY="/c/Users/divij/AppData/Local/Programs/Python/Python312/python"
TOOLKIT="/c/Users/divij/Desktop/mycroft/brutalist.art"
REEL="/d/Code/humanitarians-youtube/fellows/divij-pawar/Mycroft6_DivijPawar_09-07-2026_zero-for-sixteen"
```

## Step 1 — verify the sheet (free, instant)

```bash
$PY "$TOOLKIT/runtime/qc/sheet_check.py" "$REEL" --strict
```

Not yet run against this reel (see CHECKS-REPORT.md "Slate rules audit") —
run this before spending any time on renders.

## Step 2 — audio (the master clock)

```bash
$PY "$TOOLKIT/runtime/scripts/generate_audio_kokoro.py" "$REEL"
```

Writes `mp3/beat-B00.mp3` ... `beat-B15.mp3` and fills `actual_duration_s`
in `beat_sheet.json` for all 16 beats. Projected pre-audio total is ~8:19
(1,248 words at 150 wpm, after the 2026-09-08 runtime-cut pass) against the
requested ~8:00 target — see PEDAGOGY.md "Runtime — recomputed, then cut";
this is only a planning estimate, not measured.

## Step 3 — RETIME the Manim scenes against real audio ⚠

**Do not skip this.** Every scene in `scenes.py` currently sets `TARGET` to
the pre-audio `estimated_duration_s` — a placeholder, not yet measured
against real Kokoro output for this reel. Once Kokoro reports real
durations, compare:

```bash
$PY - <<'EOF'
import json
d = json.load(open('beat_sheet.json', encoding='utf-8'))
for b in d['beats']:
    m = b['shot'].get('manim')
    if m:
        est, act = b['estimated_duration_s'], b['actual_duration_s']
        print(f"{b['beat_id']}  {m['scene_class']:<32} est {est:>3}s  actual {act}")
EOF
```

Any beat off by more than ~1.5s: adjust that scene's `TARGET` constant and
`self.wait(...)` holds in `scenes.py` before rendering. Per
`fellows/divij-pawar/CLAUDE.md` §5, spread added/trimmed time across
several of the longer holds near a beat's end, not into one static dump.
**B13 (79s) is by far this reel's longest beat, followed by B02 (42s) and
B03 (38s)** — B13 is the most likely to need redistribution, but per
PEDAGOGY.md and CHECKS-REPORT.md, its content (Chapter 7's "still not true"
list and the uncommitted state) is explicitly protected from being cut for
time; if its measured Kokoro duration differs from the 79s estimate,
retime `self.wait()` holds within B13, don't shorten its narration.

## Step 4 — render Manim (B01–B14)

```bash
cd "$REEL"
declare -A S=( [B01]=B01_RecapAndGap [B02]=B02_LedgerTable
               [B03]=B03_OneFetchNotTwo [B04]=B04_ProvenanceRows
               [B05]=B05_SnapshotDiff [B06]=B06_DedupCollapse
               [B07]=B07_LayeringViolations [B08]=B08_CorpusBuckets
               [B09]=B09_DisjointVocabularies [B10]=B10_TwoFixesOneRecord
               [B11]=B11_RegexTruncation [B12]=B12_TrueNowList
               [B13]=B13_StillNotTrueAndUncommitted [B14]=B14_SixteenZeroReprise )
for B in B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 B11 B12 B13 B14; do
  $PY -m manim -qh --fps 30 scenes.py "${S[$B]}" -o "$B.mp4"
done
```

**Then move the clips where compile.py actually looks** — it reads
`manim/<BID>.mp4` only, never Manim's own cache path. Skip this and every
beat compiles as a slate while the render reports success:

```bash
mkdir -p manim
for B in B01 B02 B03 B04 B05 B06 B07 B08 B09 B10 B11 B12 B13 B14; do
  cp "media/videos/scenes/1080p30/$B.mp4" "manim/$B.mp4"
done
```

(Use `media/videos/scenes/2160p30/` instead if rendering `-qk` for the
final 4K pass — see Step 6.)

## Step 5 — render Remotion bookends (B00, B15)

```bash
for B in B00 B15; do
  $PY "$TOOLKIT/runtime/scripts/remotion_scenes.py" "$REEL" --only "$B" --force
done
```

Needs Node.js. If one beat fails with an ffmpeg `create-silent-audio` /
`merge-audio-track` error, that is a transient temp-dir race — retry that
beat alone. **`--only` takes exactly ONE beat id per invocation.**

> ### ⚠ Never `rm -rf media/` between renders
> Remotion writes its bookends to `media/<BeatID>.mp4` — the **same
> folder** Manim uses for its own render cache (`media/videos/...`).
> Wiping `media/` to force a clean Manim slate silently destroys the cold
> open and outro. If only Manim scenes changed, overwrite
> `manim/<BeatID>.mp4` in place and leave `media/` alone.

## Step 6 — compile

```bash
# fast preview
$PY "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 1080 --fps 30
# final master (4K UHD 3840x2160) — render Manim at -qk first (repeat Step 4 with -qk)
$PY "$TOOLKIT/runtime/scripts/compile.py" "$REEL" --height 2160 --fps 30
```

**Read the retiming lines it prints.** The stretch factor must stay under
**~1.15x** — add `self.wait()` inside the Manim scene rather than let
compile.py paper over a large factor.

**Verify no beat silently slated:**

```bash
$PY -c "import json;m=json.load(open('clips/manifest.json'));print(m)" | tr ',' '\n' | grep -i slate
```

Any hit means that beat has no rendered clip — fix and re-render rather
than reaching for `--allow-slates`.

## Step 7 — visual QC (mandatory; the mp4 probe is not QC)

```bash
mkdir -p _qc/frames
ffmpeg -i "$REEL/zero-for-sixteen.mp4" -vf fps=2 _qc/frames/%05d.png -y
```

**Read the PNGs** against the 8-point rubric in
`brutalist.art/CLAUDE-CODE-VISUAL-QC-CHECK.md`: edge bleed, title-safe
margins, container overflow, collision, offscreen anchors, legibility,
brand bug, aspect/letterbox. Sample mid-scene frames too, not just settled
final frames — watch specifically:

- **B13's stacked layout** (7-line warning list + git panel + file counter
  + closing caption, all uncleared in one scene) — confirm nothing
  collides at 4K; this is the densest single frame in the reel (see
  CHECKS-REPORT.md "Legibility contract").
- **B14's end-card bullet list beneath the sixteen-zero counter reprise** —
  confirm the auto-scaled bullet list stays legible and doesn't visually
  compete with the counter above it.
- **B09's dashed 'EMPTY INTERSECTION' gap box** — confirm the dashed
  rectangle and its two-line label don't collide with the vocabulary lists
  on either side at 4K.
- **B11's regex boundary sweep** (`13,971,000,000.0` greying out to
  `000.0`) — confirm the two mono text mobjects (`discard`/`keep`) stay
  visually adjacent with no gap or overlap once repositioned.
- **B12 → B13 transition** — confirm this reads as one continuous "honest
  ledger" movement despite being two independent Manim renders (see
  CHECKS-REPORT.md "Risk flagged").

## Step 8 — captions and final files (last of all)

**End state: exactly two final video files, both already carrying muxed
captions** — `zero-for-sixteen.mp4` (4K, 16:9) and
`zero-for-sixteen_shorts.mp4` (9:16) — per `fellows/divij-pawar/CLAUDE.md`
§2/§3. There is no separate unsubtitled master and no separately-named
`_subtitled` copy at any point; captions are muxed **in place** into the
one file that ships.

```bash
# 1. generate the caption source (after audio is final and after the last 16:9 compile)
$PY "$TOOLKIT/runtime/scripts/align.py" "$REEL" --model base --language en
$PY "$TOOLKIT/runtime/scripts/make_srt.py" "$REEL"
# writes captions.srt — the source-of-truth subtitle file, not itself a delivered format

# 2. derive the 9:16 cut from the captioned-or-not-yet-captioned 16:9 master
$PY "$TOOLKIT/runtime/scripts/shorts.py" "$REEL"
# writes zero-for-sixteen_shorts.mp4

# 3. mux captions.srt as a soft mov_text stream into BOTH final files, in place —
#    never burned in, never written to a new *_subtitled.mp4 or *_captioned.mp4 path
ffmpeg -i "$REEL/zero-for-sixteen.mp4" -i "$REEL/captions.srt" \
  -map 0 -map 1 -c copy -c:s mov_text \
  -metadata:s:s:0 language=eng "$REEL/_tmp_master.mp4" \
  && mv "$REEL/_tmp_master.mp4" "$REEL/zero-for-sixteen.mp4"

ffmpeg -i "$REEL/zero-for-sixteen_shorts.mp4" -i "$REEL/captions.srt" \
  -map 0 -map 1 -c copy -c:s mov_text \
  -metadata:s:s:0 language=eng "$REEL/_tmp_shorts.mp4" \
  && mv "$REEL/_tmp_shorts.mp4" "$REEL/zero-for-sixteen_shorts.mp4"
```

Re-run `sheet_check.py` against the derived short's own sheet (not this
16:9 sheet) before muxing — the `*916` Remotion patterns have sharply
tighter text limits (see `agents.md`'s 9:16 table); at ~8:19 of source
runtime, `./art shorts`'s auto-shortening will still need to cut
significantly to fit a Shorts-length portrait cut — expect it to select
only a subset of beats, and sanity-check which ones before shipping,
especially that it doesn't drop B13 (the uncommitted-state beat) for time.
Re-run visual QC on the
9:16 render separately, before muxing captions into it.

**Do not skip the mux step or leave an intermediate file behind as if it
were a deliverable.**

## Step 9 — clean the folder

Only these survive: `beat_sheet.json`, the gate docs, this file,
`scenes.py`, `graphics_lib.py`, `manim/*.mp4`, `media/<BeatID>.mp4`, the
archival `zero-for-sixteen.md`, `captions.srt`, and **exactly the two final
deliverables**: `zero-for-sixteen.mp4` (4K 16:9, captions already muxed in)
and `zero-for-sixteen_shorts.mp4` (9:16, captions already muxed in).
Everything else is regenerable scratch:

```bash
rm -rf "$REEL/_qc" "$REEL/media/videos" "$REEL/__pycache__"
```

Note `media/videos` — the Manim cache — **not** `media/` itself, which
holds the two rendered Remotion bookends.

**Verify the end state before calling this done:**

```bash
ls "$REEL"/*.mp4
# expected: exactly zero-for-sixteen.mp4 and zero-for-sixteen_shorts.mp4 —
# no unsubtitled master, no *_subtitled.mp4, no *_captioned.mp4, no third file.
```

## Shorts status (2026-09-08) — complete

`short/zero-for-sixteen-short.mp4` is built: 1080×1920, 2:37.8, captioned.
The auto-plan's default (dropping the longest beats first, no content
awareness) wanted to cut **B12 and B13 — the entire "honest ledger"
chapter** — which directly conflicts with the script's explicit "never cut
Chapter 7" floor. Per an explicit decision (asked and answered): **B12 and
B13 were force-kept** via `shorts.py --keep B12 B13`, with 11 other beats
(B01–B11 except B00/B06's later exclusion — see `dropped_beats` in
`short/beat_sheet.json` for the exact list) dropped instead to fit the
3:00 cap. The short is therefore B00 (cold open) → B12 → B13 → B14 → B15
(rewritten outro) → silent endcard — almost entirely the honest-ledger
chapter plus bookends, which is a genuine trade-off (very little of
Chapters 1–6 survives) but keeps the one thing the script insists must
never be cut.

Two things were hand-corrected beyond what the tooling produced automatically:

1. **The auto-generated outro narration** concatenated truncated fragments
   of the three highest-word-count dropped beats' opening text ("Quick
   recap. Cross-Agent Validation compares…, The ask was specific: don't…
   and Version two came from a…") — replaced with a clean, complete
   sentence naming what was cut in plain language.
2. **The default `--handle @nikbearbrown`** (the tool's generic default,
   not this channel's) was overridden to `--handle @DivijPawar` for both
   the rewritten outro card and the silent end card.

`short/scenes.py` required genuinely new authoring — three portrait
re-layouts (`B12_TrueNowList916`, `B13_StillNotTrueAndUncommitted916`,
`B14_SixteenZeroReprise916`), following the exact convention established
in `../Mycroft5_DivijPawar_08-28-2026_the-number-that-wasnt-there/short/scenes.py`
(frame_width ~4.5, safe frame x∈[-2,2], `BID_Name916` naming,
`graphics_lib.py` copied unchanged). **Visual QC on this new portrait
layout caught one real collision**: B13's file-counter label ("CHANGED OR
NEW FILES") overlapped the closing caption below it, because the original
code hand-placed both at fixed y-coordinates without accounting for actual
rendered text height. Fixed by switching to `.next_to()` chaining (each
element positioned relative to the one above it) instead of guessed
absolute coordinates — the same "computed, not hand-tuned" principle the
parent reel's `fit_fields()` helper already documents. Verified fixed
against a re-rendered frame before finalizing.

`ClaudeComposerAsk916` **is** registered in `Root.tsx` (an earlier grep in
this build session missed it by not scrolling far enough — corrected here
for the record) — no toolkit-level gap existed after all; both B00 and B15
re-rendered in portrait without issue.

One soft (non-hard) `sheet_check.py` finding was also fixed: B00's
composer text (`command`, `output[]`, `runningText`) had been copied
verbatim from the 16:9 parent, exceeding the much tighter 9:16 recommended
limits (e.g. `command` recommended ≤40 chars vs 16:9's ≤100). Shortened to
fit; re-rendered; `sheet_check.py --strict` now reports clean.

## Never publish

Output stays in this folder for human review.
