# General-AI-Topic Explainer: RAG — Why "Looking It Up" Doesn't Guarantee It's True

**Fellow:** Sai Pranavi Jeedigunta
**Date:** September 14, 2026
**Format:** `ai-explainer` (framework-first structure, same register as this fellow's prior STEM videos)
**Source status:** General AI/STEM topic explainer, not a report of the fellow's own engineering work. Both worked examples (a support-bot RAG system retrieving a stale policy document, and an internal-product-launch question where retrieval genuinely helps) are generic, illustrative, hypothetical scenarios — no real product, vendor, or RAG system is named. See `FACTCHECK.md`.
**Submission spec:** first video built under the toolkit's **NEW** submission spec (effective 2026-09-07, `brutalist/docs/FELLOWS-SUBMISSION.md`) — deliverable naming `ProjectName_VolunteerName.mp4` (no date/aspect suffix), separate `deliverables/landscape/` and `deliverables/vertical/` folders, full-length 4K 2160×3840 vertical companion via `./art vertical` (not a Shorts-style cut). See this fellow's sibling weekly-work video's beat sheet for the same note.

## Watch

- Landscape (4K 16:9): [Drive link](https://drive.google.com/open?id=1OtMMy-O_rEf-E3g0LtwYlj5LtYZ2GJmS)
- Vertical (4K 9:16): [Drive link](https://drive.google.com/open?id=1W6tT1ChQoEVxFWZo9vMMckBljGxMeblN)

This video opens on a silent title card, then teaches a reusable 3-question rubric — "Is the source actually Relevant? Is it actually Current? Is the model actually Grounded in it, or just remembering it?" — for deciding whether a Retrieval-Augmented Generation (RAG) system's answer is really grounded in what it retrieved. It shows the framework in full before any example, walks it through a worked example (a support bot that retrieves a real but eight-months-stale policy document and answers confidently from it anyway), stress-tests the rubric against a case where retrieval genuinely is the fix, and closes on a concrete audit task.

## What this covers (and what it deliberately avoids)

Covered: the framework-first structure (all 3 rubric questions shown together before any example), a worked example walking the rubric through a stale-source failure, a falsifiability case (a genuinely different, currently-accurate source) that stress-tests the rubric against an absolutist "retrieval always fixes hallucination" reading, and a concrete 3-question audit task restated as a checklist distinct from the framework card.

Deliberately avoided: naming or benchmarking any specific real RAG product, vendor, or vector database. Both worked scenarios are generic and illustrative by design — see `FACTCHECK.md` for what was considered and set aside (an external citation for the "RAG is treated as the fix for hallucination" framing was skipped and left as general/uncited).

## Production state

- Plan: **approved (Gate P)** — 2026-09-17
- Fact-check gate: **resolved** — citation skipped, left as general/uncited framing; both worked examples generic by design; see `FACTCHECK.md`
- Narration: **locked** — 2026-09-17, unchanged since
- Voice: **Bella (`af_bella`)** — persistent voice for this fellow's series
- Audio lock: **locked** — Kokoro `af_bella` for B01–B08; real silent mp3 (`ffmpeg anullsrc`, `audio_policy: "silence"`) for B00. Measured durations: B00 4.05s, B01 18.74s, B02 17.30s, B03 26.35s, B04 17.14s, B05 25.39s, B06 18.86s, B07 9.48s, B08 1.51s — **138.83s total**.
- Previz: **complete** — all 9 beats are real Manim scenes (`scenes.py`), no slates. GATE A/W clean on every class.
- Final landscape render: **complete** — `deliverables/landscape/RAGGrounding_SaiPranaviJeedigunta.mp4`, **3840×2160 @24fps, 139.04s**, verified receipt (`sha256: bf5f35e8...`).
- Landscape GATE V (true clean master, not the watermarked `-slate.mp4`): **0 BLOCKER, 0 MAJOR** — plus direct manual frame extraction at 12+ timestamps across all 9 beats, which caught and fixed two real defects the automated bbox-based canvas-fill metric missed on an earlier draft (content clustered in the upper half of the frame behind an oversized invisible border; a WCAG contrast bug in `teal`-on-`ink` text). See `BUILD-LOG.md`.
- Vertical companion: **complete** — built via `./art vertical` (full-length portrait companion, all 9 beats retained, no Shorts cap, no added endcard) with a genuine hand-redesigned `vertical/scenes.py` (B04/B05's landscape LEFT/RIGHT panels re-composed as TOP/BOTTOM stacks for the narrow 4.5-wide portrait frame). Final: `deliverables/vertical/RAGGrounding_SaiPranaviJeedigunta.mp4`, **2160×3840 @24fps, 139.04s**, verified receipt (`sha256: 1a973546...`).
- Vertical GATE V (true clean master): **0 BLOCKER, 0 MAJOR** — manual frame extraction additionally caught and fixed a real title/question text overlap in B05 and a mid-word text-wrap defect in B06. See `BUILD-LOG.md`.
- Self-assessment: see `PEDAGOGY.md` (against `PROOF.md`'s teaching rubric, copied from the closest sibling reel)
- Publishing: **not authorized** — masters stay in this folder only

## Compliance note

B08 (`@HumanitariansAI, in for Sai Pranavi Jeedigunta`) is the channel/fellow sign-off card, matching this fellow's other videos' established pattern for demonstrably attributing the video to the volunteer.

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted (premise, legibility contract, beats, production gate self-check)
- `beat_sheet.json` — the same plan in the pipeline's structured schema, with the completed `metadata.gates` record
- `FACTCHECK.md` — claim-level review, including why both worked scenarios are generic rather than sourced
- `SOURCES.md` — sourcing status
- `SHOTLIST.md` — beat-by-beat medium/timing table
- `PROMPTS.md` — pantry/asset status (N/A — all-Manim reel)
- `PEDAGOGY.md` — self-check against `PROOF.md`'s teaching rubric
- `BUILD-LOG.md` — dated build decisions, real defects found (and how), gate history
- `scenes.py` / `vertical/scenes.py` — landscape and portrait Manim scene sources
- `deliverables/landscape/RAGGrounding_SaiPranaviJeedigunta.mp4` — 3840×2160, 139.04s
- `deliverables/vertical/RAGGrounding_SaiPranaviJeedigunta.mp4` — 2160×3840, 139.04s
