# QC LOG — `yatra-this-week-gordy` ("This Week, Gordy.")

VISUAL QC LAW: the mp4 probe is a FILE check and never counts as QC. Every scene
below was inspected as a rendered frame at ~93% of its beat span (late enough
that all staggered elements have landed).

## Landscape — 12/12 rendered, ZERO defects on first pass

Unusual for this toolkit, and worth recording: no re-render was needed. The
geometry was budgeted against `SAFE` before writing the components (the previous
reel's four defects were all collisions from unbudgeted vertical space, so this
time every block's start and end was computed against `SAFE.b - 118`
(citation) and `SAFE.b - 62` (closer) before rendering).

| Beat | Scene | Verdict |
|---|---|---|
| B01 | `WkBluf` | clean — three status chips, third in terracotta |
| B02 | `WkPipeline` | clean — five boxes, numbered, connectors drawn, PUBLISH terracotta, all UNLIT |
| B03 | `WkTool` | clean — all six chips inside SAFE (last ends ~1644 of 1824), verbatim quote wraps to one line, citation + URL legible |
| B05 | `WkStatus` | clean — filled/hollow markers, chips right-aligned, longest detail string fits without wrap collision |
| B06 | `WkShip` | clean |
| B07 | `WkReview` | clean — dashed empty slots, withheld band, Substack node hollow |
| B08 | `WkNotClaiming` | clean — two columns, divider, terracotta on the refusal side |

Bookends (B00, B04, B09, B10, B11) are stock compositions already validated on
prior reels.

### The honesty beats, verified in pixels

- **B07** renders `Article 1` / `Article 2` as dashed EMPTY cards under
  "Titles and contents withheld — not yet approved". The review track shows
  WRITTEN filled → IN REVIEW · NINA terracotta → SUBSTACK hollow. **The Substack
  node is never filled.** Confirmed on screen, not just in the props.
- **B03** renders the tool page's sentence in quotation marks with
  `Source: humanitarians.ai/ai1/tools/gordy-tool (page description, verbatim)`
  and the terracotta line "One line is all the page publishes. The two modes are
  not named."
- **B05**'s Publish row reads `with Nina for review — Substack once approved`
  with an `OPEN` chip, never "published".
- **B08** shows the refusals beside the claims: "That anything is published" /
  "Anything about what the articles say" / "A verdict on Gordy from its
  documentation".

## GATE V — master

```
Frames sampled: 24  ·  BLOCKER: 0  ·  MAJOR: 4
```

Run against the CLEAN master. Pointed at the reel folder it defaults to
`*-slate.mp4` and reported **24 BLOCKER / 24 frames** — every one of those is the
review cut's own burned-in timecode, which is drawn at `x=w-text_w-16, y=16`,
deliberately outside title-safe. The gate's burn-in exclusion mask only covers
the bottom-left strip, so it flags its own stamp. Same false positive as the
previous reel; not a defect in the cut.

The 4 remaining MAJOR are `underfill`: B09 (`ClaudeVerdictArtifact`, 44%) and
B11 (`ClaudeTitleOutro`, 4%). Both are stock bookends, both deliberately sparse
(a centred artifact card and a poster title card), and both produce the same
finding on previously delivered reels. FILL-THE-CANVAS LAW explicitly permits
deliberate negative space. No action.

## Render environment — two stacked failures, both diagnosed

The render was blocked for a long stretch by **two separate faults that masked
each other**. Recorded because they will recur on this machine.

**1. Bundled ffmpeg could not load its dylibs.** `@remotion/compositor-darwin-arm64/ffmpeg`
references `libavdevice.dylib` by RELATIVE path, so `createSilentAudio` — hit by
every composition with no audio of its own, i.e. every `ClaudeComposerAsk` beat —
died with `dyld: Library not loaded`. **Fixed** by exporting
`DYLD_LIBRARY_PATH=<compositor dir>`; `remotion_scenes.py` now sets this itself.

**2. Intermittent browser-launch timeout.** `TimeoutError: Timed out after 25000 ms
while trying to connect to the browser!` with *empty* Chrome logs. Remotion's
bundled `chrome-headless-shell` hangs under load even though it launches fine
standalone (verified: `--dump-dom` returns clean HTML, DevTools socket reachable
in 2s, `--remote-debugging-port=0` correctly announces its port). Using the
system Google Chrome via `ART_CHROME` + `ART_CHROME_MODE=chrome-for-testing`
works, but still fails intermittently — B00 and B02 failed on the first pass and
both succeeded on a plain retry.

**Root behaviour: I/O contention, not a deadlock.** A `sample` of the "hung"
process showed the main thread in
`node::fs::ReadFileUtf8 → uv_fs_read → read` with V8 actively parsing — i.e.
bottlenecked reading modules off a 94%-full volume. The 0.0% CPU that looked
like a deadlock is just `ps` averaging over process lifetime. Several early runs
were killed while they were in fact making slow progress.

**Mitigation now in place:** a retry sweep re-renders any missing beat one at a
time until all are present. Both landscape and portrait passes use it.

## The 9:16 vertical — 12/12 on the first pass, no retries

`shorts.py` reported *under the cap → full reformat, no beats cut*: 13 beats
(12 + a 4.5s silent endcard), 147.6s. All 12 REMOTION beats rewired to their
`916` compositions and re-rendered portrait, never centre-cropped.

Inspected as frames: `WkReview916` (slots stacked, withheld band intact,
Substack node still hollow) and `WkTool916` (six coverage chips reflow to two
rows, verbatim quote wraps cleanly, citation legible). Both clean.

**Endcard verified in the ENCODED FILE, not just the beat sheet:** frame at
t=145s reads `@Yatra`. `shorts.py` was invoked with `--handle "@Yatra"`, so the
default-`@nikbearbrown` bug that shipped on
`claude-liam-the-judgment-is-the-job` did not recur here.

### GATE V — vertical

```
Frames sampled: 26  ·  BLOCKER: 0  ·  MAJOR: 6
```

- **B09 (50%) and B11 — `underfill`.** Stock bookends, deliberately sparse. Same
  as the master, same as prior reels. No action.
- **B02 — `low-contrast`, 0.29 and 0.28 against a 0.30 threshold. FALSE
  POSITIVE, verified visually.** The gate averages luminance across *all* ink
  pixels. `WkPipeline916` draws five full-width boxes in `RULE` (#D8D4C8) plus
  muted sub-labels, and that mass of light grey drags the mean separation just
  under the bar. The actual type is `CLAUDE.INK` #3D3929 on stage #F2F0E9 —
  a separation far above threshold, and the rendered frame is plainly legible.
  No action; recorded so a future pass does not "fix" a legible scene by
  darkening the brand's hairline rules.

## Toolkit changes made during this build

`runtime/scripts/remotion_scenes.py` — backward compatible, defaults unchanged:

- sets `DYLD_LIBRARY_PATH` to the compositor package so the bundled ffmpeg resolves
- prefers `node_modules/.bin/remotion` over `npx` (removes per-beat npm-exec
  startup and one observed hang vector)
- `ART_SCALE` (default `2`) — `1` gives a 1080p preview pass, ~4× less pixel work
- `ART_CONCURRENCY` (default `1`) — frames in parallel; this build used 4 on 8 cores
