# How RAG Works — a 4K explainer that carries one question through a toy RAG pipeline

**Week:** 1–7 Nov (Drive Week 2) · built 2026-11-22 to 2026-11-24

**Project:** STEM AI explainer series

**Toolkit:** brutalist.art

- **Drive:** https://drive.google.com/drive/folders/1w-Bz0R9QjZE2HX4Egg_fujYbSnVPtRb2
- **Frictional log:** [FRICTIONAL.md](FRICTIONAL.md)
- **Video:** `exports/landscape/show-tell-how-rag-works.mp4` (16:9, 3:36)

## What this film is for

A viewer has heard "RAG" and wants the mechanism. The film uses a small shop handbook (three documents, six chunks) and one question, and shows each step with executed numbers: chunk, embed (29 key words), store, retrieve (0.58 / 0.25 / 0), prompt, answer (30 days). It then adds a stale 2019 FAQ page that outranks the right chunk (0.68 over 0.38), shows the wrong answer that follows, and fixes it by removing the page, not by retraining.

## What was built

| Part | What it does |
|---|---|
| Script / narration | 18 beats; Kokoro `am_onyx`; pronunciation pin `RAG` → ɹˈæɡ. B00, B01 and BVDT narration written for the 2026-11-24 conversion. |
| `demo/rag_demo.py` | Deterministic TF-IDF cosine in numpy; no models, no APIs, no randomness. Three runs: handbook; handbook plus stale FAQ; stale page removed. Self-checks assert every ranking claim. |
| `B10_Handbook`, `B11_ThreePages` | The box of documents, and the three pages: returns, shipping, warranty. |
| `B12_Chunks`, `B13_Scanner`, `B14_Drawers` | Cut into six chunks; each stamped with its real 29-slot embedding strip; filed in a vector store. |
| `B15_Question`, `B16_Ranking` | The question becomes a strip; drawn ranking with open score bars 0.58 / 0.25 / 0.00. |
| `B17_Prompt`, `B18_Answer` | Top two chunks pasted into the prompt; the "30 days" answer, tagged "illustrated", threaded back to its source. |
| B19 `ShowTellCard` (`tabs`) | Before → After ranking: the 2019 FAQ page at 0.68, the right chunk drops to 0.38. |
| `B20_WrongAnswer`, `B21_Fix`, `B22_Scale` | The confident "14 days"; the page removed and 0.58 back on top; 21M passages, per Lewis et al. 2020. |
| Remotion bookends | B00 `ClaudeComposerAsk` cold open; B01 `BrutalistHesitantWriter` ("from what it memorized" → "from what it just looked up"); BVDT `ClaudeVerdictArtifact` (six lines); BHTF `ClaudeComposerAsk` (Your Turn prompt plus two checks); BOUT `ClaudeTitleOutro`. |

## Results

| Measure | Value |
|---|---|
| Length | 216.1 s (3:36) master |
| Slots | 18/18 filled (12 Manim, 6 video: 5 Remotion bookends and the B19 card) |
| GATE V | 36 frames, BLOCKER 0, MAJOR 0 |
| GATE T | PASS, 18 beats, 0 FAILs |
| Bookend check | PASS (ai-explainer final, 2026-11-24) |
| Strip check | PASS — 108/108 frames sampled every 2.0 s; label corner and bottom band 0 hits |
| Master check | PASS — 3840×2160, 24 fps, yuv420p, h264, 216.083 s |
| Loudness | PASS — −24.16 LUFS integrated, −3.23 dBTP true peak (window −28 to −18 LUFS, ceiling −1.0 dBTP) |
| BVDT fill | 5-line card 51%; six lines used, fill check not waived |
| Clip timing (show-tell previews) | every Manim clip −0.04% to −0.38% against its audio; none longer than its audio |
| Hand QC | all 18 beats clean after the conversion |

## Problems found by running it

1. **"RAG" was spelled letter by letter** in context (whisper heard "R.A.G." and "Ragee"); the planning note had phonemized it alone. Pinned `RAG` → ɹˈæɡ; B01, B12 and BOUT (old ids) regenerated and re-checked at ratio 1.000.
1. **Previews ran 1.8–2.8% short:** Manim floors `wait()` frames, and each wait dropped one. `Clock.at` now waits exactly frames/fps.
1. **Overlaps in hand QC:** the open box drew inner walls over its front faces (z-index), pages overlapped the box, and the answer thread and question strip collided with labels. Each was moved.
1. **GATE V, B00 midpoint low contrast (0.23 < 0.30)** on the first 4K run. The dark model block now arrives at about 2.0 s, so it is on the 50% frame; the floor shadow went to BAR2.
1. **GATE T §8.6b on the B06** `search` **card:** bordered result rows read as text runs enclosing the labels. B06 was redrawn as the Manim scene `B06_Ranking` (now `B16_Ranking`); its zero-score stub bar then read as part of "0.00", so it became a dot.
1. **GATE T §8.1 on B08/B10/B11:** a dark answer-card squiggle read as a 36 px text run. The squiggles are now soft grey (BAR1); the "illustrated" tag went from 32 to 36.
1. **GATE T §8.1 on BDEFS (40 px):** fixed in the toolkit component, `ClaudeDefinitions` meanSize 48 → 52. BDEFS was later retired in the conversion.
1. **A concurrent writer reverted the B06 change** in `beat_sheet.json` within seconds; it was re-applied a minute later and held.
1. **The ai-explainer BVDT card measured 51% fill with five lines.** A sixth line from the B22 body ("The 2020 paper that named it searched 21 million Wikipedia passages.") was added instead of waiving the check.

## Evidence

In the film folder `show-tell-how-rag-works/`:

- `FACTCHECK.md` — 28 rows; corrections in rows 9, 20, 21 and 25 (beat ids are the pre-conversion show-tell ids)
- `SOURCES.md` — primary paper: Lewis et al. 2020, "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", NeurIPS 2020, arXiv:2005.11401
- `demo/rag_demo.py`, `demo/evidence.json`, `demo/RUN-LOG.txt` (script sha256 `ef0b6742…6be`)
- `exports/landscape/show-tell-how-rag-works.verified.json` — status `ready`, sha256 `86ea9132db8987ef4abc4e74396884f4f670f6b073e0d426046403ea30e61c06`
- `final.log`, `TYPECHECK.md`, `LOUDNESS.md`, `MASTERCHECK.md`, `_qc/REPORT.md`
- `SCRIPT.md`, `SHOTLIST.md` and `CHECKS-REPORT.md` were refreshed to the ai-explainer build on 2026-11-24; the show-tell versions are kept under a History heading in each. `FACTCHECK.md` has a dated conversion section (rows 29–42).
- Drive week folder: https://drive.google.com/drive/folders/1w-Bz0R9QjZE2HX4Egg_fujYbSnVPtRb2 (Drive copy to be replaced with the clean master)
