# FRICTIONAL — Chat With Your Own Data, Zero API Calls

- **Folder:** `2026-09-21-onprem-rag-bot` · reporting week **2026-09-21 → 2026-09-27**
- **Dates inside this folder's artifacts:** source guide pasted into the build 2026-08-23
  (before the reporting week — see the README evidence index)
- Append dated entries below; never rewrite an earlier one.

---

## Entry — week of 2026-09-21 · written later, on 2026-10-28

> Reconstructed after the fact from the files in this folder, not written at the time.
> Drafted with Claude Code from those files; reviewed and confirmed by Mohammed on 2026-10-28.

**1. Date and what I was working on**
- A reel on a private, on-prem "chat with your data" stack: Open WebUI + Ollama in Docker,
  with RAG (chunk → embed → store → retrieve → generate). Built from a guide I supplied.

**2. What I tried, and what I expected**
- B03 shows the guide's `docker-compose.yml` verbatim; B04 redraws its hardware table.
- Revision cycle: a RAG answer that cites nothing (no embedder configured) → pull
  `nomic-embed-text`, set it as the embedder, re-check retrieval.

**3. Where it resisted, and what I did next**
- The guide describes the failure only in general terms, so the demo (an HR handbook, a
  remote-work question, a fabricated "3 days" answer) had to be **constructed**. Disclosed
  as illustrative in three places rather than presented as a real run.
- The hardware table gives RAM-or-VRAM ranges; simplified to RAM-only bars and captioned
  "Redrawn (simplified)".
- Manim scenes were test-rendered only at 480p15 at the audit stage; the full render waited
  for audio lock.

**4. What Claude or another person contributed — accepted, changed, rejected**
- Claude drafted the beat sheet, `scenes.py` and the fact-check against my guide.
- I signed GATE P (confirmed 2026-10-28); `PEDAGOGY.md` still reads "awaiting your sign-off"
  because the signature was not written back. The `work/qc-*.png` frames are the only render evidence here.

**5. What I understand now, and what I still do not**
- Understood: privacy here comes from `OLLAMA_BASE_URL` pointing at the Ollama container,
  and without an embedding model nothing is vectorised, so nothing is retrieved — the model
  answers fluently from its own memory.
- Open: no QC report or final runtime in this folder.

**Evidence in this folder**
- [`FACTCHECK.md` — 13 claims against the source guide](FACTCHECK.md) · [`SOURCES.md`](SOURCES.md)
- [`PEDAGOGY.md` — GATE P audit](PEDAGOGY.md) · [`PROMPTS.md`](PROMPTS.md) · [`scenes.py`](scenes.py)
- Frame checks: [`work/qc-B05.png`](work/qc-B05.png) (broken pipeline) · [`work/qc-B08.png`](work/qc-B08.png) (grounded)
