# BUILD-LOG — The Gatekeeper Needs Ground Truth

Reel: `claude-hai-gatekeeper-ground-truth`
Skill: `ai-explainer` (claude-explainer) · Voice: Liam, Kokoro `am_onyx` (free)
Authored: 2026-09-13 · **Not yet rendered.**

---

## Environment — INSTALLED 2026-09-13

The toolkit was not installed when this reel was authored; it is now. `./setup
--install` reports all seven features ready, and `./art smoke` **PASSES** (real
935 KB mp4, both streams decode, GATE V 0 BLOCKER / 0 MAJOR, audio mean −24.2 dB).

| Dependency | State |
|---|---|
| Python | 3.12.10 (winget `Python.Python.3.12`) — outranks the Store alias |
| ffmpeg / ffprobe | 9.0.1 (winget `Gyan.FFmpeg`) |
| Kokoro `.onnx` model | present (~340 MB) |
| `runtime/remotion/node_modules` | 189 packages installed |
| Scene index | **regenerated** — 616 renderable, 0 unresolved |

### Every shell needs this preamble

Git Bash does not inherit the post-install PATH, and the scripts print Unicode that
Windows' cp1252 console cannot encode:

```bash
export PATH="/c/Users/Tapan/AppData/Local/Programs/Python/Python312:/c/Users/Tapan/AppData/Local/Programs/Python/Python312/Scripts:/c/Users/Tapan/AppData/Local/Microsoft/WinGet/Packages/Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe/ffmpeg-9.0.1-full_build/bin:$PATH"
export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
```

Without `PYTHONUTF8=1`: `[art] REFUSED: 'charmap' codec can't encode character '←'`.
Also note: Windows Python ships no `python3.exe` (which `art` and `setup` both call),
so `python.exe` was copied to `python3.exe` in the Python 3.12 install directory.

### Render log — previz built 2026-09-13

`ART_FACTS=0 ./art run` → **12/12 slots filled**, 195.6s (3:15),
`claude-hai-gatekeeper-ground-truth-slate.mp4` (16.1 MB),
**GATE V: 24 frames, 0 BLOCKER, 0 MAJOR**.

Defects found and fixed during the render (all verified on frame, not just re-run):

- **B01 seed type.** Passed `20260913` as a number; the schema wants a string.
- **B01 phrase triggers.** `BrutalistHesitantWriter` matches whitespace-delimited word
  cores only, so the SKILL.md's phrase-level correction never matched. Re-authored to a
  single-word swap. Full reasoning in CHECKS-REPORT.md.
- **B01 overran title-safe.** `fontSize: 62` pushed line 1 past the right edge → GATE V
  BLOCKER. Now 52.
- **B01 never finished typing.** Three lines + two corrections did not fit the 10.5s
  window (checked at 95%: still mid-line-2). Cut to two lines / one correction, with
  `charMs: 30`, `hesitateBetween: 6`, `hesitateWithin: 1`. The pauses, not the
  keystrokes, were eating the window.
- **B07 payload card bled off-frame.** The travelling claim card is wider than a node,
  so centring it on the last node pushed it past the right edge → GATE V BLOCKER.
  Left edge is now clamped into SAFE (`GatekeeperVerifyLoop.tsx`).

Two warnings left standing, both deliberate — see CHECKS-REPORT.md §Open items:
`remotion` carries 91% of beats (MOTION.md wants ~40%), and SKIN LINT wants
`ClaudeTitleOutro` where D3 deliberately uses `GatekeeperTitleOutro`.

### D7 — new channel `claude-gatekeeper`

GATE L (`beat_lint.py` rule 7) enforces a fixed per-channel kicker from
`runtime/qc/brand_labels.json`. `claude-hai` is registered there as the series
*Irreducibly Human*, which this dev log is not. Per that file's own instruction
("Edit freely; add channels as needed"), a new entry was added:

```json
"claude-gatekeeper": { "kicker": "Provenance Gatekeeper", "chip": "@HumanitariansAI" }
```

The beat sheet's `metadata.channel` is now `claude-gatekeeper` and the kicker reads
`Provenance Gatekeeper` on all three composer beats. The chip is unchanged. The folder
slug stays `claude-hai-gatekeeper-ground-truth`.

### Five toolkit bugs fixed to get the render green

All three are Windows/ffmpeg issues in the toolkit itself, unrelated to this reel.
The repo is not under git, so there is no version-control safety net for these edits.

1. **`runtime/scripts/build_safety.py`** — slug regex leading character class
   `[A-Za-z0-9]` → `[A-Za-z0-9_]`. The shipped `examples/_smoke` fixture has slug
   `_smoke`, which its own validator rejected, so `./art smoke` could never pass.
   Traversal is still blocked — `..`, `../evil`, `/abs`, `a/b`, `.hidden` and `''`
   all verified to fail.
2. **`runtime/scripts/compile.py`** — added `fg_path()`, which escapes a path for use
   inside an ffmpeg filtergraph. A raw Windows font path broke the parser
   (`No option name near 'Onkarbrutalist…'`). Normalising to `/` and escaping the
   drive colon is **not** sufficient; the value must also be single-quoted, verified
   against ffmpeg 9.0.1.
3. **`runtime/scripts/compile.py`** — review-cut overlays (beat chip, title card,
   timecode burn-in) moved from a flat 16px margin to the 5% title-safe inset. At
   16px, GATE V scored every review cut as a BLOCKER `edge-bleed` — the gate was
   failing the cut on its own scaffolding. Only fires where ffmpeg was built with
   `drawtext`, which is why it never surfaced on the author's machine.
4. **`runtime/scripts/remotion_scenes.py`** — `subprocess.run(["npx", …])` died with
   `[WinError 2]` on every beat. On Windows `npx` is `npx.cmd` and CreateProcess does
   no PATHEXT lookup. Added an `NPX` constant resolved via `shutil.which()`, which
   honours PATHEXT on Windows and is a plain PATH lookup elsewhere.
5. **`runtime/qc/brand_labels.json`** — added the `claude-gatekeeper` channel (see D7).
   Not a bug fix; a registration the toolkit explicitly invites.

### Still outstanding for this reel

1. **GATE L ran against the index file, not the tool.** The library-first search was
   done directly against `runtime/remotion/src/scenes.json` because `./art scenes`
   could not execute at authoring time. Same evidence, different entry point. The six
   new components have since been confirmed `RENDERABLE` via `./art scenes --check`.
2. **No audio yet.** Narration MP3s do not exist, so `actual_duration_s` is absent on
   every beat and `estimated_duration_s` is still an estimate. Audio is the master
   clock; the sheet is not locked until Kokoro has run.
3. **No visual QC yet.** `_qc/` does not exist for this reel. VISUAL QC LAW is
   unsatisfied and the reel is NOT done.
4. **Paperwork gate.** `./art run` enforces GATE F: the reel needs `FACTCHECK.md`,
   `SHOTLIST.md` and `PROMPTS.md` before it will render. `ART_FACTS=0` is the
   previz-only exception.

---

## Decisions

### D1 — Palette: Claude fidelity skin, not the source's dark Brutalist palette

`Week2.md` specifies `#0A0A0A` / `#F2F0EB` / `#E8452C` / `#6B6B6B`. That is the
nbb / teardown skin. This was commissioned as a **claude-explainer**, a FIDELITY
brand that `CLAUDE-BRAND.md` forbids retinting. Built in the Claude palette
(`#FAF9F5` page, `#F2F0E9` stage, `#3D3929` ink, `#D97757` spark); the source's
intent — visible grid, exposed labels, zero radius, hard cuts, one reserved accent
— is carried across intact.

*If the dark palette is the point rather than the Claude skin, the right move is the
`nbb` skill, not a retint of this one — that is a rebuild of the six components
against `tokens/teardown.ts`, not a prop change.*

### D2 — Channel: Liam narrating on `@HumanitariansAI`

The brief asks for the Liam voice and a sign-off naming Onkar Bhujbal and
Humanitarians AI. `ai-explainer` ships a `claude-hai` channel (chip
`@HumanitariansAI`) and its `profile` modifier already establishes the precedent of
Liam narrating under that chip. So: persona Liam, voice `am_onyx`, chip
`@HumanitariansAI`, slug `claude-hai-*`.

IN-FOR-BEAR LAW rule 1 (say the voice out loud) is honoured — B00 opens "this is
Liam." Rule 2's "in for Bear" sign-off is a `@NikBearBrown` convention and does not
apply on this channel; the sign-off is the one the author specified, verbatim.

### D3 — Outro card: `GatekeeperTitleOutro`, not `ClaudeTitleOutro`

`OUTRO-LOCK.md` scopes `ClaudeTitleOutro` to claude-liam / `@NikBearBrown` reels
only — the handle is hardcoded, there is a mandatory mascot, and sublines are
banned. That same file says other channels have their own outros. So this reel got
one: HAI mark full size (LOGO LAW), exact title restate in poster serif with the
terracotta period, `@HumanitariansAI` beneath, credit line for the fellow.
The slug is `claude-hai-*` precisely so the lock's scope test cannot misfire.

### D4 — B05 renders as a slate (the one justified HOLD)

The real `ingest.py` was not supplied. Fabricating a listing and presenting it as
the project's code would violate DOUBLE-CHECK LAW, so B05 renders as a PIPELINE
slate naming exactly what is missing — the SELF-DEMO LAW feasibility fallback.
Never silently skipped, never faked.

**Resolve:** paste the real `ingest.py` into `media/B05.code.txt`, trim to ~16 lines
(read path, `encode` call, `collection.add` call), set the `code` prop, re-render.

### D5 — Illustrative rows are labeled as such

Only `doc_01` comes from the source. `doc_02`–`doc_04` on B02 and two of the three
claim/truth pairs on B03 were constructed to demonstrate the classes the source
names, and are flagged in SOURCES.md with a replace-before-publish action.

### D6 — No performance metric appears anywhere

The source reports none. `RESULT = INTERCEPTION READY` is a state, not a score.

---

## Runtime

Authored estimate: **234s (3:54)**. The source script targets **2:45**.

Duration is an output of the content, never a target (`duration-planner`), so
nothing was compressed to hit 2:45. If 2:45 is a hard channel constraint, the fix is
a **narration cut, not a timing hack** — regenerate audio and recompile, never
re-time by hand. Cheapest ~70s, in order:

1. `BHTF` 32s → ~20s — keep the prompt verbatim, cut one discussion line (−12s)
2. `B03` 22s → ~15s — the three classes are fully legible on screen; the voice can
   name them and drop the per-class gloss (−7s)
3. `B05` 21s → ~14s — trim the "no fine-tuning, no GPU" aside (−7s)
4. `B08` 22s → ~16s — the artifact page carries all four lines; narrate two (−6s)
5. `B02` 22s → ~16s — the table shows the pairs; cut the read-aloud of doc_01 (−6s)

Anything past that starts costing the teaching arc.

---

## Next steps

```bash
# 1. install the toolkit (ffmpeg + a real Python must exist first)
winget install Gyan.FFmpeg Python.Python.3.12
./setup --install

# 2. make the new components findable
./art scene-index

# 3. audio first — the master clock
python3 runtime/scripts/generate_audio_kokoro.py G:/Onkar/youtube/claude-hai-gatekeeper-ground-truth

# 4. review cut
./art run G:/Onkar/youtube/claude-hai-gatekeeper-ground-truth

# 5. visual QC (mandatory — the mp4 probe is not QC)
#    sample frames, READ the PNGs, audit the 9-point rubric, log _qc/REPORT.md

# 6. master, only after zero BLOCKER / zero MAJOR
./art final G:/Onkar/youtube/claude-hai-gatekeeper-ground-truth --out G:/Onkar/youtube/claude-hai-gatekeeper-ground-truth
```

Never publish. Output stays in this folder for human review.
