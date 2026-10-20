# Weekly Work Report: The Keyword That Cried Wolf

**Fellow:** Sai Pranavi Jeedigunta
**Week ending:** September 29, 2026
**Project:** Project 29 — Financial Regulatory Intelligence System (`mycroft` repo, `scripts/regulatory-intel/`)
**Source status:** Real engineering work. Every claim traces to `C2-VERIFICATION.md` and the matching `logs/RUN_LOG.md` entry in the `mycroft` repo — a live local-LLM (Ollama) second-pass review built and verified against real named false positives and a genuine true positive.

## Watch

- Landscape (4K 16:9): [Drive link](https://drive.google.com/open?id=1xRBkIelRa25VoVRR74hVnege1Tbcodx1)
- Vertical (4K 9:16): [Drive link](https://drive.google.com/open?id=1Vo2qrD9PMBYoC1Xzmf1oiushQyL-AgqG)

This video covers a real fix to the pipeline's keyword scorer: two named noise patterns from `FINDINGS.md` (a routine Medicare payment rule scored 10/Critical from the word "emergency" appearing in a law's proper name; a boilerplate Nasdaq SRO filing scored 9/Critical from "Immediate Effectiveness") now get caught by a local-LLM second opinion before they'd trigger an alert — without touching the original keyword scorer at all, and failing open if the model itself breaks.

## What this covers (and what it deliberately leaves out)

Covered: the exact scoring rule that causes the misfire (quoted verbatim), both real trigger words shown in their actual harmless context, the fail-open review design (confirm / downgrade / model-fails-goes-through-anyway), live verdicts for all 3 test cases shown together, and 3 honestly-stated limitations.

Deliberately left out: this is not a full labeled-benchmark evaluation of the scorer — it targets the 2 specific patterns already named and measured in `FINDINGS.md`, not a general claim about all possible misfires.

## Production state

- Plan: **approved (Gate P)** — signed 2026-09-29
- Fact-check gate: **resolved** — see `FACTCHECK.md`; B06 gets a "not reviewed — below alert threshold" label for clarity, B07's honest-limits beat kept at full weight
- Narration approval: **approved** — Kokoro `af_bella`, locked 2026-09-29
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole report series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `KeywordReScoring_SaiPranaviJeedigunta.mp4`, 3840x2160, 24fps, h264/aac, **135.54s**. GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):** `KeywordReScoring_SaiPranaviJeedigunta.mp4`, 2160x3840, 24fps, h264/aac, **135.42s**. GATE V on the true clean master: **0 BLOCKER, 2 MAJOR** (both on B08, the brand/sign-off card, borderline underfill right at the 55% floor — the same accepted minor-cosmetic category as every sibling video's brand cards; personally visually confirmed legible and well-composed).
- Personally re-verified (not just trusting the build report): extracted and viewed real frames from B05 (fail-open flow diagram), B06 (3-case results table), and B08 directly from the final vertical deliverable. No text-rendering artifacts anywhere; B06 explicitly reads "not sent to model" / "UNTOUCHED" for the SEC case, matching the FACTCHECK-required precision exactly.
- Publishing: **not authorized** — masters stay in this folder only

## Built under the toolkit's new submission spec

This is one of the first `pranavi-j`-path projects built fresh under the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`, effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate `deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K 2160x3840 vertical companion built via `./art vertical` (not a ≤180s Shorts-style cut) — every beat, no cuts, no added endcard.

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured schema, both aspects
- `FACTCHECK.md` — claim-level review against `C2-VERIFICATION.md`
- `SOURCES.md` — claim → source mapping
- `SHOTLIST.md` / `PROMPTS.md` — beat-by-beat medium/timing table and pantry/asset status
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
