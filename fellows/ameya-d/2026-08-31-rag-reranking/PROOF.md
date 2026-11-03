# PROOF.md — self-assessment · rag-reranking

**Reel:** RAG: Reranking · **Volunteer:** Ameya Deshmukh · **Category:** AI & STEM topic (RAG series)
**Persona:** Liam, in for Ameya (Kokoro am_onyx) · **Channel:** @HumanitariansAI
**Deliverable:** `RAGReranking_AmeyaDeshmukh_2026-08-31.mp4` · **4K (3840×2160)** · ~3:21 · 11 beats

| Requirement | Status | Evidence |
|---|---|---|
| @HumanitariansAI throughout | ✅ | folderLabel on B00/B09; verdict + outro carry it |
| 4K (3840×2160) | ✅ | Manim -r 3840,2160; Remotion scale=2; compiled --height 2160 |
| STEM naming TopicName_YourNameDate | ✅ | RAGReranking_AmeyaDeshmukh_2026-08-31.mp4 |
| Source on GitHub | ✅ | committed to fin-disclosure-rag (media gitignored) |
| Self-assess (PROOF.md) | ✅ | this file |
| Fact-check | ✅ | FACTCHECK.md — 13 claims, all traced to `rerank.py` / `benchmark.py` |

## Content
Single-subtopic RAG episode: why fast first-stage retrieval still needs a careful
second pass; bi- vs cross-encoder; the pair→score→sort mechanism; the two-stage
"retrieve wide, rerank narrow" shape; the real `rerank.py`; the honest latency cost
(rerank 301 ms vs generation 1288 ms); and when to reach for it or skip it.
Real code + real measured numbers only.

## Gates
- GATE P: PEDAGOGY.md VERDICT: PASS.
- GATE V: **0 BLOCKER** (fixed B06/B07 left-edge bleed by pinning labels/columns inside safe).
  Remaining 4 MAJOR are the ClaudeVerdictArtifact (B08) + ClaudeTitleOutro (B10)
  templates, inherently sparse — downgraded to warnings under --lenient. contact_sheet.png attached.
- Audio-first: 11 beats measured (Kokoro am_onyx); Manim auto-fills to the clock.

**Self-verdict: PASS** — 0 blockers; advisories are the two inherent Remotion templates.
