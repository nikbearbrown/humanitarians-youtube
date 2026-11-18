# Frictional log — Agent Swarms (AI, Explained)

## 2026-11-13 — weekly STEM explainer (concept, framework-first), 16:9 + 9:16

- **Drive:** https://drive.google.com/drive/folders/1zhv9xw6eNUDYDYet6ezF8uMIOTIlg__G

Evidence in this folder: `beat_sheet.json`, `PEDAGOGY.md` (GATE P: PASS),
`PROOF-REVIEW.md` (10/12, gate PASS), `_qc/REPORT.md`, `agent-swarms.mp4`,
`short/agent-swarms-short.mp4`. (YouTube: TBD.)

**What I was working on.** A framework-first explainer on agent swarms — multi-agent
systems — built to pass PROOF. The spine I committed to before writing a single card:
a swarm is many agents that *divide · work in parallel · converge*, and it only wins
when the task genuinely decomposes. The reusable test the viewer leaves with: *can you
name the split and the merge?* Deliberately non-dating — no product, framework, or
version names, so the piece doesn't rot.

**What I tried, and what I expected.**
* The hard call was scope. "Agent swarms" invites a tour (orchestrator vs peer-to-peer,
  blackboards, voting schemes, specific frameworks). A tour fails PROOF — it teaches
  trivia, not one transferable idea. So I cut to one worked shape (orchestrator → workers
  → critic) and spent the back half on the *boundary*: when a swarm is the wrong tool.
* Expected a routine audio-first build: cards → audio (the clock) → bookends → compile,
  16:9 then the 9:16 reformat.

**Where it resisted, and what I did next.**
* The one real snag was mine, in the Short pipeline. I generated the portrait cards with
  `make_cards.py --aspect 9x16 --out media` run from inside `short/` — but `--out` is
  resolved against the beat sheet's own dir, so the 9:16 cards landed in the *parent*
  `media/` and overwrote the 16:9 cards there. No harm to the already-compiled 16:9
  master (frames were baked), but the folder was briefly inconsistent. Fix: the canonical
  call is `--out short/media` run from the reel root. I regenerated both sets explicitly
  (16:9 → `media/`, 9:16 → `short/media/`) and verified dimensions before compiling.
* Also deleted the stale center-cut `-916.mp4` stubs the scaffold warned about, so the
  portrait bookends rendered clean from the 916 compositions (B00/B05/B06/B07), all
  2160×3840.

**What Claude contributed, and what I did with it.**
* Mine: the topic, the framework-first spine, the decision to spend the ending on the
  "don't use it" case, the Pragmatist register, GATE P sign-off.
* Claude's: drafted the eight beats under DOUBLE-CHECK (no dating claims, costs as ×N),
  built both cuts, and ran PROOF (10/12) — flagging B04 (the trade) as the beat that
  earns the piece and B02's "combine or vote" as the one gain asserted, not shown.

**What I understand now, and what I still do not.**
* Understood: the honest version of the swarm pitch is conditional — "wins *only when*
  the work splits." The gains (parallelism, specialization, diversity) and the costs
  (×N tokens, conflict, convergence) are two readings of the same property: decomposition.
* Still open: the diversity/voting gain deserves its own worked example (ensembling,
  self-consistency) — a candidate sequel rather than a crammed beat here.
