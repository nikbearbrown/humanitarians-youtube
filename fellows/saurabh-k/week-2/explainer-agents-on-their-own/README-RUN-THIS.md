# README-RUN-THIS — hai-agents-on-their-own

Everything below runs from the toolkit root. This reel was built against
**brutalist.art** at commit `4115560`.

## 0. Every new terminal session starts here

```bash
cd <path-to>/brutalist.art
source .venv/bin/activate
```

Skip this and Kokoro is not on the path, and step 1 fails in a confusing way.

## 1. Generate the narration — this is the master clock

```bash
python3 runtime/scripts/generate_audio_kokoro.py <reel-dir>
```

Every beat's final length is however long its own mp3 runs. The planning numbers in
`estimated_duration_s` auto-retime to the real figure in `actual_duration_s`.
This reel uses voice `am_onyx`; keep it, the series is voice-locked.

## 2. Render, QC and review cut

```bash
./art run <reel-dir>
```

10 beats at 3840x2160. Every beat renders from a Remotion pattern —
there is no `scenes.py` and no Manim in this reel.

## 3. Type gate before the clean master

```bash
./art final <reel-dir>
```

**Read the output, do not assume it.** `art final` prints
`GATE T skipped — missing deps (pip install pillow numpy scipy)` and carries on with a
zero exit when Pillow, numpy or scipy are missing. A skipped gate is not a passing gate.
Install the three first:

```bash
pip install pillow numpy scipy
```

TYPECHECK.md FAILs block the final cut with exit 2. That is the behaviour you want.

## 4. Vertical cut

```bash
./art vertical <reel-dir>
```

2160x3840. Re-run the type gate against the vertical build separately — it is its own
design, not a crop, and the landscape pass does not cover it.

## Useful while building

```bash
./art scenes <query>     # search existing Remotion patterns before authoring a new one
./art todo <reel-dir>    # what is still unfilled
```
