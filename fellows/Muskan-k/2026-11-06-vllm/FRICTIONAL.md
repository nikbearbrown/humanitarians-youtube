# Frictional log — vLLM (AI, Explained)

## 2026-11-06 — weekly STEM explainer (concept, framework-first), 16:9 + 9:16

- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md` (GATE P: PASS),
`PROOF-REVIEW.md` (10/12, gate PASS), `_qc/REPORT.md`, `vllm.mp4`,
`short/vllm-short.mp4`. (YouTube: TBD.)

**What I was working on.** A framework-first explainer on vLLM — efficient LLM inference
and serving. The topic names a real system, so the risk was the opposite of my usual one:
instead of over-generalizing, I could slide into a feature tour ("vLLM has X, Y, Z"). I
held the line on one transferable idea: *serving is memory-bound; vLLM treats the KV
cache like an operating system treats RAM* — PagedAttention to reclaim wasted memory,
continuous batching to keep the GPU full. The lesson is meant to outlive the tool: when a
system is memory-bound, stop reserving for the worst case — page it and keep the pipeline
full.

**What I tried, and what I expected.**
* Expected a routine audio-first build. The content work was getting the mechanism right
  without a figure I couldn't defend: KV cache as the real bottleneck, ~60–80% waste
  under naive contiguous allocation, block-table paging to under 4%, copy-on-write block
  sharing, iteration-level scheduling. I deliberately kept the headline speedup
  qualitative ("several× / many times, same latency") rather than quoting one benchmark
  number that would date or mislead.

**Where it resisted, and what I did next.**
* The one real snag was length. First audio pass came in at **3:08** — over the Shorts
  3:00 cap, which would force the scaffold to *drop a beat* from the Short. For a concept
  explainer every beat carries weight, so dropping one isn't acceptable. Rather than
  hand-fix timing (forbidden — audio is the master clock), I tightened the narration on
  the three densest beats (B01, B02, B03 — B03 alone was 35s) and regenerated audio.
  Landed at **2:58**, under the cap, no beat cut.
* Applied the Short-pipeline lesson from last week up front: generated the portrait cards
  with `--out short/media` from the reel root (not from inside `short/`), scaffolded with
  `shorts.py` first and regenerated native portrait cards after, and cleared the stale
  center-cut `-916.mp4` stubs before rendering the 916 bookends. No misplaced files this
  time.

**What Claude contributed, and what I did with it.**
* Mine: the topic, the framework-first spine (serving = memory; page it), the decision to
  keep speedups qualitative, GATE P sign-off.
* Claude's: drafted the eight beats under DOUBLE-CHECK (verified against the
  PagedAttention SOSP'23 / Orca OSDI'22 work), trimmed to fit the Shorts cap without
  cutting a beat, built both cuts, and ran PROOF (10/12) — flagging B01 (the
  memory-vs-compute reframe) as the beat that makes it teach and B04's "batch stays full"
  as the one claim shown rather than measured.

**What I understand now, and what I still do not.**
* Understood: PagedAttention and continuous batching are the *same* idea in two places —
  manage the KV cache like virtual memory, then keep the freed capacity busy. The waste
  (B02) and the fix (B03) are one story about fragmentation.
* Still open: the throughput win is the one thing I asserted rather than showed. A
  throughput-vs-batch-size curve would make a strong follow-up, and ties back to the
  KV-caching explainer from 16 Oct.
