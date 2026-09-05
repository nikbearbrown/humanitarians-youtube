# BUILD-PROMPT — `yatra-this-week-gordy`

Paste-ready prompt that finishes this reel. Everything up to the render is
already done and on disk: narration (12 MP3s, 2:23 measured), `beat_sheet.json`,
all 14 scene registrations, and the paperwork set.

---

## ⚠ READ FIRST — the renderer is currently blocked on this machine

**Status at handoff: audio ✅ · scenes ✅ · registrations ✅ · render ❌ (0/12 beats).**

Remotion cannot launch a browser. Every render dies with:

```
TimeoutError: Timed out after 25000 ms while trying to connect to the browser!
Chrome logged the following:            ← note: EMPTY
```

**This is environmental, not a defect in this reel.** Proven by control test:
`LnkStat` — a composition from the previous reel that rendered perfectly earlier
the same day — fails with the identical error. Nothing in `WeekGordy.tsx` is
implicated.

### There are TWO separate failures. One is FIXED, one is not.

**FAILURE 1 — B00 (`ClaudeComposerAsk`): bundled ffmpeg cannot load its dylibs. ✅ FIXED.**

```
at async createSilentAudio (@remotion/renderer/dist/create-silent-audio.js)
dyld: Library not loaded: libavdevice.dylib
```

Remotion's bundled ffmpeg at
`node_modules/@remotion/compositor-darwin-arm64/ffmpeg` references its dylibs by
RELATIVE path, so it only resolves when the working directory is the compositor
dir. Compositions with no audio of their own (every `ClaudeComposerAsk` beat)
hit `createSilentAudio`, which shells out to it, and it dies.

**Confirmed fix** — export this before rendering:

```bash
export DYLD_LIBRARY_PATH="$PWD/runtime/remotion/node_modules/@remotion/compositor-darwin-arm64"
```

Verified: with it set, `ffmpeg -f lavfi -i anullsrc -c:a pcm_s16le` produces a
valid wav; without it, dyld fails. (Running the binary from inside its own
directory also works — same root cause.)

**FAILURE 2 — B01+: Remotion cannot connect to the browser. ❌ NOT FIXED.**

Setting `DYLD_LIBRARY_PATH` does NOT clear this one. It is intermittent in a
telling way: sometimes it errors at 25s with a full log (version warning →
`Bundling 6%` → `TimeoutError`), sometimes it produces **no output whatsoever**
and hangs indefinitely at 0% CPU with no browser process ever spawned. That
inconsistency is the signature of a wedged system state, not a misconfiguration.

Every layer was verified working *in isolation*:

| Check | Result |
|---|---|
| `node -e` | ✅ ok |
| `remotion versions` | ✅ ok (4.0.486) |
| headless-shell launch, `--dump-dom about:blank` | ✅ clean HTML, exit 0 |
| DevTools socket on a fixed port | ✅ reachable in 2s |
| `--remote-debugging-port=0` stderr announcement | ✅ `DevTools listening on ws://127.0.0.1:58278/...` |
| `DevToolsActivePort` file in profile | ✅ written |
| `--headless` **and** `--headless=old` | ✅ both fine |
| ffmpeg `lavfi`/`anullsrc` (PATH ffmpeg) | ✅ ok |
| **Remotion's own browser launch** | ❌ 25s timeout, empty logs |

Ruled out with tests, not guesses: sandboxing (already disabled), `npx` (direct
binary fails too), `TMPDIR` (fresh dir fails too), stale locks (none),
quarantine (none), the headless-shell binary itself (launches fine),
proxy/`no_proxy` env vars (none set), node→loopback connectivity (works),
a partial package upgrade (all `@remotion/*` dirs dated Aug 20, untouched
today), and `DYLD_LIBRARY_PATH` (fixes failure 1, not this one).

**One environmental factor worth clearing before retrying:** the data volume is
at **94% capacity, ~12 GiB free**. The toolkit renders with
`--image-format=png --scale=2`, i.e. 3840×2160 PNG frames spooled to temp, so a
long beat can need several GB of scratch. That is not proven to be the cause —
Remotion's own temp dirs are all empty and `/var/folders` totals only 3 GB — but
it is tight enough to be worth freeing space before a full 12-beat 4K pass.

**The only intervening event between working and broken was the machine going to
sleep.** So try, in order:

1. **Reboot** — highest confidence. The identical commands worked before sleep.
2. If a reboot is not possible, try a fresh login shell / new terminal session
   (the failure may be scoped to a wedged process-group state).
3. Then re-run step 3 below and confirm B00 renders before letting the full pass
   run unattended.

There is also a **pre-existing Remotion version mismatch** in this project
(`remotion` resolves 4.0.486 while `@remotion/paths` etc. resolve 4.0.490;
`package.json` pins only `remotion: ^4.0.0`). Remotion's own warning says this
can cause "failed renders and unclear errors." It was present during the
successful renders earlier, so it is probably not the cause — but if a reboot
does not fix the hang, pinning every `@remotion/*` to one exact version is the
next thing to try.

---

## The build

```
Finish the reel at ~/Desktop/brutalist-reels/youtube/yatra-this-week-gordy.
Free path only — Kokoro + Remotion + ffmpeg, no paid API, never publish.

Read first:
  ~/Desktop/brutalist.art-main/skills/make/ai-explainer/SKILL.md   (doctrine)
  ~/Desktop/brutalist.art-main/CLAUDE-BRAND.md                     (fidelity palette)
  ./FACTCHECK.md   ./CHECKS-REPORT.md   ./SHOTLIST.md

HARD CONSTRAINTS — the reason this reel exists:
  1. The two articles are IN REVIEW, not published. Never say or render
     otherwise. WkReview has NO title/summary/content prop by design — do not
     add one, and do not fill the Substack node.
  2. Do not invent anything about the articles' content.
  3. Gordy's description renders VERBATIM from its tool page, in quotes, with
     its citation. The page says "two-mode" but never names the modes — do not
     name them. The on-screen note that one line is the whole public
     description stays.
  4. No count of graphics, and no claim they are live. WkShip's chip says MADE.
  5. WkShip draws no artwork. A mock-up would be a fabricated artifact.

STEPS:

  cd ~/Desktop/brutalist.art-main && source .venv/bin/activate && export ART_HOME=$PWD
  # REQUIRED — fixes the bundled-ffmpeg dyld failure on every no-audio beat:
  export DYLD_LIBRARY_PATH="$PWD/runtime/remotion/node_modules/@remotion/compositor-darwin-arm64"
  # NOTE: system python is 3.14 and has no wheels for the pinned deps; the venv
  # is CPython 3.12 (uv). manim is NOT installed and is NOT needed — this reel
  # has zero Manim beats, so run.sh skips that stage cleanly.

  # 1. audio is already measured — regenerate ONLY if narration changed:
  # python3 runtime/scripts/generate_audio_kokoro.py <REEL>
  #    If it changes, retarget durationInFrames for the seven Wk* compositions
  #    AND their 916 twins in Root.tsx: frames = round(seconds * 30).

  # 2. sanity-check ONE beat before the full pass (see the blocker above):
  cd runtime/remotion && ./node_modules/.bin/remotion render src/index.ts WkBluf \
      /tmp/_probe.mp4 --frames=0-5 --concurrency=1 --image-format=png
  #    If this times out on the browser, STOP and fix the environment first.

  # 3. render all beats, compile both cuts, run GATE V
  bash runtime/scripts/run.sh \
      ~/Desktop/brutalist-reels/youtube/yatra-this-week-gordy --height 2160

  # 4. VISUAL QC LAW — the mp4 probe is a FILE check and never counts as QC.
  #    Sample frames and actually LOOK at them. Highest-risk layouts here:
  #      · WkTool     — six chips laid out on a fixed pitch; check the last one
  #                     does not cross SAFE.r, and that the italic quote wraps
  #      · WkStatus   — the Publish row's detail is the longest string on screen
  #      · WkReview   — the withheld band must not collide with the slots above
  #                     or the review track below
  #      · WkPipeline — five boxes on one row; check the sub-labels do not clip
  #    Log every defect and fix in _qc/QC-LOG.md. Fix ROOT CAUSES in
  #    runtime/remotion/src/scenes/WeekGordy*.tsx and re-render.
  #    Re-render a single beat with:  --only B0X --force   (ONE id per call —
  #    `--only B02 B06` errors out and renders NOTHING while still exiting 0)

  # 5. GATE V must run against the CLEAN MASTER, not the slate cut:
  python3 runtime/qc/final_frame_check.py <REEL> --mp4 <REEL>/yatra-this-week-gordy.mp4
  #    Pointed at the reel folder it prefers *-slate.mp4 and flags that cut's
  #    own burned-in timecode (top-right, outside title-safe) as edge-bleed on
  #    EVERY frame — 28 phantom BLOCKERs. Expect underfill MAJORs on the outro
  #    card; those are by design and match every prior reel.

  # 6. the 9:16 derivative — PASS THE HANDLE:
  python3 runtime/scripts/shorts.py <REEL> --handle "@Yatra"
  #    shorts.py's --handle DEFAULTS TO @nikbearbrown and never reads
  #    metadata.channel_handle. Omitting it ends the vertical on the wrong
  #    channel. (The delivered reel claude-liam-the-judgment-is-the-job has
  #    exactly this bug in its short/beat_sheet.json.)
  #    At 2:23 the reel is under the 3:00 cap, so NO beats should be dropped.
  #    If the planner proposes dropping any, stop and say so.
  python3 runtime/scripts/remotion_scenes.py <REEL>/short     # portrait renders
  python3 runtime/scripts/compile.py <REEL>/short --height 1920

  # 7. report durations, gate results, QC verdict. Do NOT publish.
```

---

## Deliverables this produces

| File | What it is |
|---|---|
| `yatra-this-week-gordy.mp4` | 16:9 master, 3840×2160 — YouTube |
| `yatra-this-week-gordy-slate.mp4` | review cut with beat markers |
| `short/yatra-this-week-gordy-short.mp4` | 9:16, 1080×1920 — Instagram / LinkedIn |
| `_qc/QC-LOG.md` + `_qc/frames/` | the frame-level visual QC pass |
| `mp3/` + `mp3/timings.json` | narration and the master clock (already built) |

## Scene source (edit here, never in the reel folder)

```
runtime/remotion/src/scenes/WeekGordy.tsx      # 16:9 — seven components
runtime/remotion/src/scenes/WeekGordy916.tsx   # 9:16 — re-banded, not scaled
runtime/remotion/src/Root.tsx                  # registrations + frame counts
```
