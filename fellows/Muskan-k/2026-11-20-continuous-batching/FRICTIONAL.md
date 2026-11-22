# Frictional log — Continuous Batching (AI, Explained)

## 2026-11-20 — weekly STEM explainer (concept, framework-first), 16:9 + 9:16

- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md` (GATE P: PASS),
`PROOF-REVIEW.md` (10/12, gate PASS), `_qc/REPORT.md`, `continuous-batching.mp4`,
`short/continuous-batching-short.mp4`. (YouTube: TBD.)

**What I was working on.** A dedicated explainer on continuous batching. The catch: I'd
already covered it as *one beat* inside the vLLM reel two weeks earlier, so the real risk
was repeating myself. I split the subjects deliberately — the vLLM reel is about *memory*
(PagedAttention), with batching as its coda; this reel is about *scheduling*, with memory
as the coda. Same spine the Fellows' thread keeps returning to (serving is about not
wasting the GPU), seen from the other side: occupancy is throughput, and the enemy is
waiting — to fill a batch, and on the slowest request.

**What I tried, and what I expected.**
* Expected the now-routine audio-first build. The content work was making the static-vs-
  continuous contrast land without hand-waving: both *waits* of static batching (fill, and
  lockstep-to-the-longest) plus head-of-line blocking, then the per-token evict/admit loop,
  then an honest cost beat (prefill stalls + KV-memory ceiling) so it doesn't read as a
  free lunch.

**Where it resisted, and what I did next.**
* Length, again. First audio pass was **3:09** — over the Shorts 3:00 cap, with B02 and
  B04 both clocking ~32s. Dropping a beat from a concept explainer isn't acceptable, and
  timing is never fixed by hand (audio is the master clock), so I tightened the narration
  on B01, B02, and B04 and regenerated. Landed at **2:54**, no beat cut. This is the
  second week running the first pass overshot — these deep-dive topics are dense, so next
  time I'll budget ~26s/body-beat in the draft rather than discovering it at the audio step.
* The rest ran clean: cards legible first try (including B02's longer "padded, waiting"
  quote, which I'd worried would overflow), Short pipeline correct with `--out short/media`
  from the reel root and stale `-916.mp4` stubs cleared before the portrait bookends.

**What Claude contributed, and what I did with it.**
* Mine: the topic, the decision to frame this as *scheduling* (distinct from the vLLM
  reel's *memory*), the two-waits structure, GATE P sign-off.
* Claude's: drafted the eight beats under DOUBLE-CHECK (verified against Orca's iteration-
  level scheduling and the serving literature), trimmed to fit the cap without cutting a
  beat, built both cuts, and ran PROOF (10/12) — docking one point on the "N for ~the cost
  of one" shorthand (true only in the memory-bound decode regime), which I accepted with
  the "~/almost" hedge rather than crowding the card with the caveat.

**What I understand now, and what I still do not.**
* Understood: PagedAttention and continuous batching are two halves of one answer — page
  the KV cache to make room, then schedule per token so that room is always in use. The
  memory ceiling in B04 is literally where this reel hands back to the vLLM one.
* Still open: the one claim I asserted rather than bounded on screen is the batching
  speedup and the "cost of one" amortization; a throughput-vs-batch-size curve (showing
  where it turns compute-bound) would close both, and would make a natural third reel with
  KV caching (16 Oct) and vLLM (6 Nov).
