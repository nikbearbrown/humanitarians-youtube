# AUDIO PLAN — `hai-reallocation-engine`

**The Reallocation Engine** · Humanitarians AI cut · Plain register
Narrator: Sanjana Alapati · Engine: **Kokoro (local, free, no key)** · Voice: **`af_bella`**

> **Audio-first.** Every number in the "estimate" column below is a *projection*, not a
> setting. Narration MP3s are generated and **measured** first; the measured durations
> become the master clock and every visual conforms to them. Timing is never fixed by
> hand — regenerate audio, recompile. (`CLAUDE.md` rule 2.)

---

## 1 · Voice configuration

| Field | Value | Where it lives |
|---|---|---|
| `metadata.engine` | `kokoro` | `beat_sheet.json` |
| `metadata.voice_kokoro` | `af_bella` | `beat_sheet.json` — folder default |
| `beat[*].voice` | `af_bella` | set explicitly on every spoken beat |
| Language (G2P) | `en-us` | derived from the `af_` prefix by `generate_audio_kokoro.py` |
| Cost | **$0.00** | Kokoro runs locally; no account, no key |

`generate_audio_kokoro.py` validates the voice code against the model's own voice
table at run time and refuses anything it does not know. `af_bella` is a stock
Kokoro v1.0 voice.

---

## 2 · Per-beat audio plan

Estimates assume ~144 wpm effective for `af_bella` — deliberately below a flat
reading rate, because B03 and B05 are comma-separated lists and B07 ends in two
short sentences, and Kokoro inserts real breath at every one of those boundaries.

| Beat | Act | Words | Est. | MP3 | Measured |
|---|---|---:|---:|---|---|
| B00 | ASK | 22 | 9.0 s | `mp3/beat-B00.mp3` | — |
| B01 | BLUF | 32 | 13.0 s | `mp3/beat-B01.mp3` | — |
| B02 | WHO IT IS FOR | 27 | 11.0 s | `mp3/beat-B02.mp3` | — |
| B03 | THE SIGNALS | 35 | 14.5 s | `mp3/beat-B03.mp3` | — |
| B04 | WEIGHTS AND GATES | 34 | 14.0 s | `mp3/beat-B04.mp3` | — |
| B05 | THE RECOMMENDATION | 24 | 10.5 s | `mp3/beat-B05.mp3` | — |
| B06 | WHERE IT FAILS | 33 | 13.5 s | `mp3/beat-B06.mp3` | — |
| B07 | TAKEAWAY | 26 | 11.5 s | `mp3/beat-B07.mp3` | — |
| B08 | OUTRO | 0 | 5.0 s | *silent card* | fixed |
| | **TOTAL** | **233** | **≈ 1:42** | | |

1:42 sits inside the requested 1–2 minute window with room on both sides. If the
measured total lands outside it, the fix is a narration edit, not a speed change —
`./art duration-planner <reel>` prints the beat-level overage.

### Pronunciation watch-list

Read these back on the first listen; they are the ones a TTS engine gets wrong:

| Written | Expected | Fallback if it misreads |
|---|---|---|
| `Sanjana Alapati` | san-JAH-na ah-la-PAH-ti | respell in `narration_text` only |
| `F-1 OPT` | "F one O P T" | write `F-one O P T` |
| `OPT` | "O P T" (initialism) | write `O P T` |

`generate_audio_kokoro.py` normalizes symbols (`·`, `—`, `≤`, …) before synthesis, so
the em-dashes in the on-screen card copy never reach the voice — only
`narration_text` is spoken, and it contains none.

---

## 3 · The loop (run in this order)

```bash
# 1 — audio becomes the clock (writes mp3/, fills actual_duration_s)
python3 runtime/scripts/generate_audio_kokoro.py <reel>

# 2 — review cut with beat markers
./art run <reel>

# 3 — what is still unfilled, and how to fill it
./art todo <reel>

# 4 — clean 4K master (no beat markers)
./art final <reel> --out <your folder>
```

Step 1 is a **dry-run first** (`--dry-run`) to confirm nine beats route to
`af_bella` and B08 is correctly skipped as silent, before any synthesis runs.

Nothing in this list publishes. `./art final` writes a file to a folder you name and
stops there (`RENDER-TARGETS.md`).

---

## 4 · Environment readiness — **READY** (2026-09-06)

`./setup` readiness table on this machine:

| Feature | Status |
|---|---|
| audio (Kokoro Bella/Onyx) | ✅ ready — real phrase synthesized + decoded at −21.8 dB |
| captions + word clock | ✅ ready |
| Manim beats | ✅ ready |
| Remotion beats + bookends | ✅ ready |
| slates / previz / compile | ✅ ready |
| fonts (EB Garamond + Oswald) | ✅ ready |
| Manim **equation** beats | ❌ blocked — needs LaTeX + `dvisvgm`. **This reel has no Manim beats, so it is not a blocker.** |

Installed to get there: ffmpeg 9.0.1 (winget `Gyan.FFmpeg`), Node 24.19.0 LTS
(winget `OpenJS.NodeJS.LTS`), Remotion's 189 node packages, the Kokoro model files
(`kokoro-v1.0.onnx` 325 MB + `voices-v1.0.bin` 28 MB), and the Python deps.

### The toolkit runs from its own virtualenv — not Anaconda base

The first `./setup --install` landed in the **Anaconda base environment** and
upgraded `numpy` 1.26.4 → 2.2.6 and `protobuf` 3.20.3 → 7.36.1, which broke the
`numpy<2` pins held by `tensorflow`, `streamlit`, `numba`, `contourpy` and
`pywavelets`, and broke `manim` through a `scipy` compiled against numpy 1.x.

That was reverted: base is back to `numpy` 1.26.4 / `protobuf` 3.20.3 / `click`
8.1.7, all toolkit packages were removed from it, and `pip check` reports **no
broken requirements**. The toolkit now lives in its own venv at
`brutalist.art-main/.venv/`.

> Unrelated pre-existing issue, left alone: `tensorflow` 2.19 in Anaconda base fails
> to import with `DLL load failed while importing _pywrap_tensorflow_internal`. It
> fails the same way with numpy 1.26.4 restored and from a clean PowerShell PATH, so
> it is not caused by the install above.

### ⚠ `onnxruntime` must stay pinned at **1.20.1**

`onnxruntime` 1.29.0 and 1.22.0 both install fine on this machine and both fail at
import with `DLL load failed while importing onnxruntime_pybind11_state: A dynamic
link library (DLL) initialization routine failed`. **1.20.1 loads.** `kokoro-onnx`
only requires `>=1.20.1`, so the pin is safe.

`requirements.txt` does not pin it. **Re-running `./setup --install` will upgrade
`onnxruntime` and break audio again.** If that happens:

```bash
.venv/Scripts/python.exe -m pip install "onnxruntime==1.20.1"
```

### Running the pipeline

`ffmpeg` and `node` are on PATH for new shells, but `python3` must resolve to the
venv, not Anaconda:

```bash
export PATH="/c/Program Files/nodejs:$PATH"
alias python3="/c/Users/sanjana/Downloads/brutalist.art-main/brutalist.art-main/.venv/Scripts/python.exe"
```

---

## 5 · Doctrine notes on this cut

- **GATE L (library-first) was run before authoring.** No beat is slated and no
  component was punted. Two candidates were rejected on inspection rather than
  trusted from the index: `FluencyScale` hardcodes `SUBMISSIONS` / `PASSED
  UNDETECTED` / `94%`, and `FluencyDivergence` hardcodes the kicker *"fluency is not
  provenance."* `FluencyChipGrid` is used **without** its `foundation` prop for the
  same reason — that block carries hardcoded "shared assumption" copy.
- **`ClaudeTitleOutro` is deliberately not used.** `OUTRO-LOCK.md` hardcodes
  `@NikBearBrown` into that card. The HAI outro (`OutroSeries`) is the correct one
  here and carries no personal name.
- **No GitHub URL and no author name** appears in any on-screen string or in any
  narration line.
- **Plain register requirement met by the author's own words.** The HAI register
  requires a "when NOT to / where it fails" beat; B06 is it.
- **Two doctrinal beats are absent by choice** — see the note in the plan handed to
  the author. Both would add spoken narration beyond the eight scenes supplied.

---

## 6 · BUILD RECORD — measured, rendered, verified (2026-09-06)

Narration generated with Kokoro `af_bella`, measured, and used as the master clock.
Every visual was conformed to the measured length, never the other way round.

| Beat | Act | Component | Est. | **Measured** |
|---|---|---|---:|---:|
| B00 | ASK | ClaudeComposerAsk | 9.0 s | **8.81 s** |
| B01 | BLUF | BrutalistHesitantWriter | 13.0 s | **13.06 s** |
| B02 | WHO IT IS FOR | FormACard | 11.0 s | **12.25 s** |
| B03 | THE SIGNALS | FluencyChipGrid | 14.5 s | **14.81 s** |
| B04 | WEIGHTS AND GATES | FluencySourceFlow | 14.0 s | **14.12 s** |
| B05 | THE RECOMMENDATION | ClaudeVerdictArtifact | 10.5 s | **9.05 s** |
| B06 | WHERE IT FAILS | FormACard | 13.5 s | **13.59 s** |
| B07 | TAKEAWAY | FormACard | 11.5 s | **9.30 s** |
| B08 | OUTRO | OutroSeries | 5.0 s | **5.00 s** |
| | | | | **99.99 s = 1:40.0** |

Master audio level: mean −21.2 dB, peak −1.4 dB.

### Visual QC — frames inspected, three defects found and fixed

Per `CLAUDE.md` rule 4 the render was verified by LOOKING at extracted frames, not by
the mp4 probe. Pass 1 failed on three counts:

1. **Mojibake on every beat carrying a middot or em-dash.** `remotion_scenes.py`
   reads the beat sheet with `Path(p).read_text()` and no encoding, so on Windows a
   UTF-8 sheet was decoded as cp1252: `·` rendered as `Â·`, `—` as `â€"`, `…` as
   `â€¦`. Fixed by running the whole pipeline under **`PYTHONUTF8=1`**.
2. **B01 never finished typing.** `BrutalistHesitantWriter` is registered at 606
   frames (20.2 s); the clip is truncated to the 13.06 s beat, so the correction
   never landed. Typing sped up (`charMs` 78 → 42, mistakes/hesitations reduced);
   the full sentence now completes with ~2 s to hold.
3. **B04 `FluencyThreshold` is structurally broken for any label.** Its gate label is
   absolutely positioned 88 px above the track and lands on top of the centred axis
   label. Replaced with **`FluencySourceFlow`** — prop-driven chips, no hardcoded
   copy, no collision.

### Two more Windows-only blockers hit during the build

- **`npx` is not an `.exe`,** so `subprocess.run(["npx", ...])` in
  `remotion_scenes.py` fails with `FileNotFoundError`. Worked around with a distlib
  launcher shim (`npx.exe`/`npm.exe`) on PATH.
- **`--review` crashed in ffmpeg.** The review-only `drawtext` timecode interpolates
  a raw Windows font path (`fontfile=C:\...`), which ffmpeg's filtergraph parser
  splits on the drive colon. The toolkit's own escape hatch — **`ART_NO_DRAWTEXT=1`**
  — takes the documented PIL-overlay path instead. Beat labels are unaffected; only
  the corner timecode is absent.
- **B08 made the whole reel silent.** `build_master_audio` requires an mp3 for
  *every* beat (`all(p.exists() …)`); the silent outro had `audio_file: null`, so the
  first compile muxed `anullsrc` over the entire film. Fixed by generating a real
  5.0 s silent `mp3/beat-B08.mp3`.

### Accepted lint

```
[art] SKIN LINT: B08: palette=claude but the outro is 'OutroSeries'
                 — OUTRO LAW wants ClaudeTitleOutro
```

**Deliberate.** `OUTRO-LOCK.md` hardcodes `@NikBearBrown` into `ClaudeTitleOutro` and
scopes that card to `claude-liam` reels only. `OutroSeries` is the correct HAI
sign-off and carries no personal name.

### Outputs

| Artifact | Path |
|---|---|
| Review cut (1080p, beat labels) | `book/youtube/hai-reallocation-engine/hai-reallocation-engine-slate.mp4` |
| **4K master (3840×2160, 24 fps)** | `brutalist.art-main/renders/hai-reallocation-engine.mp4` |
| QC contact sheet | `book/youtube/hai-reallocation-engine/qc-sheet.png` |

Nothing was published or uploaded. Per `RENDER-TARGETS.md` the master went to the
toolkit's default `renders/` folder; what happens to it next is a human decision.
