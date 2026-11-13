# BUILD-PROMPT — Lookup, Not Training

Paste-ready prompt that rebuilds this reel end to end. Run from `~/dev/`.
Free, local, no keys. **Never publishes.**

---

Rebuild the reel at `research/youtube/claude-hai-lookup-not-training/`. It is an
**ai-explainer** on the default fidelity brand (claude palette), **claude-hai**
channel, **@HumanitariansAI**, narrated by **Bella** (`af_bella`), Pragmatist
register. Read `brutalist/skills/make/ai-explainer/SKILL.md` in full first.

Environment: Remotion needs Node ≥ 20 — `export
PATH="$HOME/.nvm/versions/node/v20.20.2/bin:$PATH"`. Python deps are in
`brutalist/.venv`, so call `brutalist/.venv/bin/python` (`./art doctor` reports
blocked against system python; that is the venv, not a missing dep).

```bash
cd ~/dev
export PATH="$HOME/.nvm/versions/node/v20.20.2/bin:$PATH"
B=brutalist; R=research/youtube/claude-hai-lookup-not-training

# 0. GATE P — must already read "VERDICT: PASS". Never bypass with --no-gate.
grep -q "VERDICT: PASS" $R/PEDAGOGY.md || { echo "GATE P unsigned"; exit 1; }

# 1. AUDIO — the master clock.
$B/.venv/bin/python $B/runtime/scripts/generate_audio_kokoro.py $R

# 2. CONFORM COMPOSITIONS TO THE CLOCK. Each composition in Root.tsx is
#    registered at exactly its beat's actual_duration_s * 30. If any mp3 changed
#    length, update the matching durationInFrames before rendering.
$B/.venv/bin/python -c "
import json;d=json.load(open('$R/beat_sheet.json'))
[print(b['beat_id'], b['shot']['remotion']['pattern'], round(b['actual_duration_s']*30)) for b in d['beats']]"

# 3. VISUALS — foreground only, never a hand-rolled npx remotion render.
$B/.venv/bin/python $B/runtime/scripts/remotion_scenes.py $R --now "$(date -u +%FT%TZ)"

# 4. THE 4K MASTER.
$B/.venv/bin/python $B/runtime/scripts/compile.py $R --height 2160 --fps 30

# 5. SUBTITLES.
$B/.venv/bin/python $B/runtime/scripts/align.py $R
python3 $R/make_srt.py

# 6. VISUAL QC — mandatory. See the sampling warning below.

# 7. CHAPTERS — BEFORE writing description.txt. Confirm no segment under 10s.
python3 $R/chapters.py --sheet $R/beat_sheet.json --names "…"

# 8. THE 9:16 SHORT.
$B/.venv/bin/python $B/runtime/scripts/shorts.py $R --drop B10 B11 B12 --keep B07 --handle @HumanitariansAI
$B/.venv/bin/python $B/runtime/scripts/generate_audio_kokoro.py $R/short
$B/.venv/bin/python $B/runtime/scripts/remotion_scenes.py $R/short --now "$(date -u +%FT%TZ)"
$B/.venv/bin/python $B/runtime/scripts/compile.py $R/short --height 1920 --fps 30
$B/.venv/bin/python $B/runtime/scripts/align.py $R/short
python3 $R/short/make_srt.py --out claude-hai-lookup-not-training-short.srt
```

## QC SAMPLING — read this before trusting any frame you pull

**`ffmpeg -ss <t> -i <file>` seeks on the input side and snaps to the nearest
keyframe.** On a 4K master that is seconds of error. It will hand you a frame from
the previous beat and you will label it with this beat's id. The first QC pass on
this reel did exactly that and hid a real defect.

Sample by **exact frame index** instead:

```bash
ffmpeg -v error -i master.mp4 -vf "select=eq(n\,$FRAME),scale=1280:-1" -vsync 0 -frames:v 1 out.png
```

And sample **near t=0 for every scene**, not just mid and end — the defect that
catches is a beat opening on a half-built frame.

## Things this reel will bite you on

1. **Blank frames between clips.** The shared `ClaudeComposerAsk` and
   `ClaudeVerdictArtifact` animate in from nothing, which leaves up to 0.5s of empty
   cream at a beat boundary. `illustrations/haiKit.tsx` wraps them in
   `<Sequence from={-20}>` to pre-play the intro. If you re-point a bookend at the
   raw shared component, the holes come back. Re-sweep every boundary by exact
   frame index after any render.
2. **`--keep B07` is not optional.** B07 is the cost comparison — the author's
   designated "detail people repeat". Trim anything else first.
3. **The auto short plan is not enough.** `shorts.py`'s own plan lands at 180.1s,
   still over the cap. Use the explicit `--drop B10 B11 B12`.
4. **`shorts.py` hardcodes a dark endcard.** Regenerate with
   `endcard_png(..., dark=False)` and verify the ground pixel is `(243,235,221)`.
   Do not patch `shorts.py` — dark is right for the teardown brands.
5. **`chapters.py` splits `--names` on commas.** A label containing a comma
   silently becomes two names and the script exits with a count mismatch.
6. **SKIN LINT will warn on B00 / B13.** Expected — those are wrappers. See
   `_qc/REPORT.md`.

## Hard constraints — re-verify every rebuild

- **Never say or show "RAG", "embeddings", "vector search", "retrieval-augmented."**
  The mechanism is "looking things up" / "searching the book". Check narration,
  props, card text, chapter names, the description **and the .srt**.
- **Land "open-book exam, not a study session" exactly once**, in B04, undressed.
  The episode title is "Lookup, Not Training." specifically so the outro cannot
  dilute it. Don't rename it to something containing "open-book".
- **State no count that isn't verified against source.** No source gives the number
  of passages retrieved, so none is stated or implied — `PassagePull` and
  `HandedTogether` carry a trailing ellipsis card for exactly this reason. Don't
  remove it, and don't add "three passages" anywhere.
- **Keep the "by default" hedge** on the reindex claim until someone confirms the
  trigger against a book repo's `package.json` (see `SOURCES.md`, Open item 1). It
  is on screen as well as in the voice.
- **Say "before that question reaches the model that writes the answer"** — not
  "before it goes anywhere near the AI", which is false in the hybrid configuration.

## Sources

Script: `open-book-not-trained-script.md`. Verified against `medhavi-hub`:
`docs/how-the-tutor-uses-the-textbook.md`, `docs/ai-models.md`, the per-book
architecture docs, and `medhavy_documentation/STAKEHOLDER_OVERVIEW.md`.
Full claim ledger, corrections and open items: `SOURCES.md`.

**Never publish.** The masters stay in this folder.
