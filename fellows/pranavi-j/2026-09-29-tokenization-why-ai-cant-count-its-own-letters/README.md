# Weekly STEM Video: Tokenization: Why AI Can't Count the Letters in Its Own Words

**Fellow:** Sai Pranavi J.
**Week ending:** September 29, 2026
**Format:** general AI/STEM topic explainer (`ai-explainer`), distinct from this fellow's weekly
project-update report
**Source status:** general AI/STEM topic explainer, not a report of the fellow's own engineering
work. The worked example illustrates a widely-known, generic class of tokenization behavior — not
a benchmark of any specific real model (tokenizer behavior changes between model versions). See
`SOURCES.md` and `FACTCHECK.md`.

## Watch

- Landscape (4K 16:9): [Drive link](https://drive.google.com/open?id=1HifrCasAyqc7Dnw-48EC-_U_JDm7camO)
- Vertical (4K 9:16): [Drive link](https://drive.google.com/open?id=1-wFRtNdLAjKS3yZ-yDvBhZ7FQabTlGSi)

This video covers one real, well-known mechanism behind a common AI failure mode: language models
don't read text letter-by-letter, they read it in sub-word chunks called tokens, and a word's
token split often doesn't line up with its actual letters — which is why asking a model to count a
letter in a word is unreliable even though the same model writes fluent prose. It teaches a
reusable 3-question rubric for predicting this kind of failure, walks through a generic "how many
R's in strawberry"-style worked example (the model's token-level tally miscounting 2 vs the true
3), and stress-tests the mechanism by showing the same word, same model, spelled out
letter-by-letter first — now counting correctly.

## What this covers (and what it deliberately leaves out)

Covered: the token-split mechanism shown as a real segmentation (not just asserted), a worked
example with the token-level tally and the true count both visible together (mismatch clear), a
falsifiability case using the exact same word and model with only the spelling-out changed, and a
concrete 3-question task the viewer can run today.

Deliberately left out: this is not a benchmark or disclosed test of any specific real model's
tokenizer — the worked example is a fully generic, original illustration of a widely-documented
class of behavior, kept intentionally hypothetical per `FACTCHECK.md`.

## Production state

- Plan: **approved (Gate P)** — 2026-10-02
- Fact-check gate: **resolved** — see `FACTCHECK.md`; worked example kept fully generic, no real
  model/vendor named or benchmarked
- Narration approval: **approved** — Kokoro `af_bella`, locked 2026-10-02
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `Tokenization_SaiPranaviJ.mp4`, 3840x2160, 24fps,
  h264/aac, **121.17s**. GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):**
  `Tokenization_SaiPranaviJ.mp4`, 2160x3840, 24fps, h264/aac, **121.17s** (same duration as
  landscape, all 9 beats present, no drops). GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Personally re-verified (not just trusting the build report): extracted and viewed real frames
  from B05 (spelled-out fix, both aspects) and B08 (brand sign-off, both aspects) directly from the
  final deliverables. No text-rendering artifacts, legible contrast, clean composition.
- Publishing: **not authorized** — masters stay in this folder only

## Built under the toolkit's official submission spec

Built under `brutalist/docs/FELLOWS-SUBMISSION.md` (effective 2026-09-07): `ProjectName_VolunteerName.mp4`
naming (no date/aspect suffix), separate `deliverables/landscape/` and `deliverables/vertical/`
folders, and a true full-length 4K 2160x3840 vertical companion built via `./art vertical` (not a
≤180s Shorts-style cut) — every beat, no cuts, no added endcard.

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured
  schema, both aspects
- `FACTCHECK.md` — claim-level review (dramatization check: no real model named/benchmarked)
- `SOURCES.md` — claim → source mapping
- `SHOTLIST.md` / `PROMPTS.md` — beat-by-beat medium/timing table and pantry/asset status
  (no pantry assets — all 9 beats are self-contained Manim scenes)
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `BUILD-LOG.md` — dated build decisions, real bugs found and fixed, and gate history
