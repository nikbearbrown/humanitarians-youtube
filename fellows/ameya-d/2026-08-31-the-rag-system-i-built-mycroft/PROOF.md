# PROOF.md — self-assessment · mycroft-rag-walkthrough

**Reel:** The RAG System I Built · **Volunteer:** Ameya Deshmukh · **Category:** Weekly work report
**Persona:** Liam, in for Ameya (Kokoro am_onyx) · **Channel:** @HumanitariansAI
**Deliverable:** `Mycroft_AmeyaDeshmukh_2026-08-31.mp4` · **4K (3840×2160)** · ~3:57 · 12 beats

| Requirement | Status | Evidence |
|---|---|---|
| @HumanitariansAI throughout | ✅ | folderLabel on B00/B10; verdict + outro carry it |
| 4K (3840×2160) | ✅ | Manim -r 3840,2160; Remotion scale=2; compiled --height 2160 |
| Work naming Mycroft_YourNameDate | ✅ | Mycroft_AmeyaDeshmukh_2026-08-31.mp4 |
| Source on GitHub | ✅ | committed to fin-disclosure-rag (media gitignored) |
| Self-assess (PROOF.md) | ✅ | this file |
| Fact-check | ✅ | FACTCHECK.md — 14 claims traced to run_eval/compare_embeddings/weight_sweep/benchmark |

## Content
A measured walkthrough of the `fin-disclosure-rag` system: 600-doc synthetic corpus,
the golden set, the pipeline, and three levers with real numbers — chunking
(MRR 0.833 → 1.000), embedding-model choice (384-dim beat 768-dim), hybrid search
(MRR 0.655 → 0.810). Then the latency reality (vector search ~0.2%), the real
`hybrid.py` RRF fusion, and three surprises. Corpus is synthetic (disclosed);
every figure is a measured script output.

## Gates
- GATE P: PEDAGOGY.md VERDICT: PASS.
- GATE V: **0 BLOCKER** (fixed B01 right-edge bleed and B06 left-edge label bleed).
  Remaining 4 MAJOR are the ClaudeVerdictArtifact (B09) + ClaudeTitleOutro (B11)
  templates, inherently sparse — warnings under --lenient. contact_sheet.png attached.
- Audio-first: 12 beats measured (Kokoro am_onyx); Manim auto-fills to the clock.

**Self-verdict: PASS** — 0 blockers; advisories are the two inherent Remotion templates.
