# Weekly Research Report: Reordering, Not Retrieval

**Fellow:** Satwik Reddy Sripathi
**Week ending:** October 31, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** `sources/` - `weekly_report_2026-10-31.md`, `ablation_reorder_not_retrieve.md`, `ablation_graph_vs_retrieval.md`, `ablation_graph_vs_retrieval.json`, `ablation_graph_vs_retrieval.png`. Every on-screen figure traces to these.
**Source status:** The ablation is **measured and reproducible** (`scripts/ablation_graph_vs_retrieval.py`), swept over K so it is not cherry-picked. The prerequisite edges it runs on are faculty-review **drafts**; this measures the **mechanism**, not approved content, and makes **no learning-outcome claim**. Embedder is the general-domain `all-MiniLM-L6-v2`.

This is the core experiment of the whole project: **does the dependency graph actually change the roadmap, or
is it just a fancy search?** Week 5 asked this on a draft graph with zero authoritative edges and could only
show "insertion, not reshuffle." The graph is now real, so this week -

**I measured it: a similarity ranker leaves prerequisites unreachable and out of order, while the graph method
guarantees a dependency-valid sequence and pulls in the foundations the project needs.**

The result overturns week 5's own finding: with the real graph, the effect is not just insertion, it is a
substantial reorder (Kendall tau at or below zero).

The final beat sheet contains **10 beats**. The complete video is generated locally with the free Brutalist
toolkit, delivered as a **4K 16:9 master**, reviewed end to end (including a PROOF skeptical-explainer pass).

## What was done this week

- **Built the graph-vs-retrieval ablation** (`scripts/ablation_graph_vs_retrieval.py`): two arms (pure top-k vs
  select-and-sequence), four metrics, swept over K in {10, 20, 30}.
- **Measured, at K=20:** the graph inserts **34 / 31** prerequisite sections top-k never reaches; pure retrieval
  **breaks 3 / 2 prerequisites and misses 17 / 12**, the method arm breaks **0 / 0**; order correlation Kendall
  tau = **-0.44 / 0.00** (substantial reshuffle); personalization core Jaccard **0.25**.
- **Robustness:** every finding holds across K = 10, 20, 30.
- **Grounded** it in the prerequisite-learning and rank-correlation literature, and wrote it up as paper-ready
  Results (`docs/ablation_reorder_not_retrieve.md`).

## How this connects to the series

Weeks 02-04 ablated the tagging; week 05 argued reason-vs-retrieve qualitatively on a draft graph; weeks 08-13
built, tiered, audited and recall-fixed the real prerequisite graph. **Week 14 is the payoff:** with the graph
finally real, the reordering-not-retrieval claim is measured, not asserted. It is the core Results evidence.

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## Central question

> Does the dependency graph actually change the roadmap, or is a similarity search enough - and how do you
> measure the difference?

The answer: a similarity ranker leaves prerequisites unreachable and out of order; the graph guarantees a
dependency-valid sequence and inserts the foundations retrieval cannot reach. Measured, swept, reproducible.

## Main ideas presented (10 beats)

1. **The challenge (hook).** "Isn't this just semantic search with extra steps?" The fair test: run it with and
   without the graph.
2. **The setup (framework-first).** Two arms, same project, same embeddings: retrieval = top-k by similarity;
   method = same core + prerequisite closure, ordered by topological sort.
3. **The metrics.** Insertion, prerequisite violations (missing + mis-ordered), Kendall-tau reordering,
   personalization - before any number.
4. **Insertion.** The graph pulls in 34 / 31 prerequisite sections top-k never reaches.
5. **The order is broken.** Pure retrieval misses 12-17 prerequisites and mis-orders 2-3; the graph breaks 0.
   (The figure: retrieval tall, method zero.)
6. **It reorders, not just inserts.** Kendall tau -0.44 / 0.00 - the method order is uncorrelated with, even
   reversed from, similarity. This overturns week 5's "insertion, not reshuffle."
7. **It personalizes.** Two projects' focus sets overlap only 0.25; they share the common biology foundations
   (0.615), which is correct pedagogy.
8. **It's robust.** Every finding holds across K = 10, 20, 30 - not cherry-picked.
9. **The honest boundary.** General embedder; runs on the authoritative CSV (graph.json since reconciled to it);
   draft edges; no learning-outcome claim.
10. **Verdict / CTA.** Reordering, not retrieval - and the way to prove a graph earns its place is to delete it
    and measure what breaks.

## Current implementation boundary

- **Measured and reproducible**; swept over K.
- Runs on **faculty-review draft** edges - measures the mechanism, not approved content.
- **General-domain embedder**; reads the authoritative prereq CSV directly (Stage-3 `graph.json` since reconciled to it).
- **No learning-outcome claim.**

## The reusable framework

1. **To prove a component earns its place, remove it and measure the delta** (ablation), do not argue it.
2. **Choose metrics that capture what the component is for** - here, dependency reachability and order, not just
   overlap.
3. **Sweep the free parameter** (K) so the result is robust, not cherry-picked.
4. **Report the honest mechanism** - insertion vs reshuffle - and let the numbers update your earlier claims.

## Research grounding

Prerequisite relation learning (Liang, Wu, Huang & Giles, EMNLP 2015; Pan et al., ACL 2017; Liang et al. 2018);
topological ordering of a prerequisite DAG as the standard study-order formalization; Kendall (1938) for rank
correlation; ablation as the standard attribution method. Citations in `sources/ablation_reorder_not_retrieve.md`.

## Research prompt

> Research the "Reordering, Not Retrieval" explainer. Begin with `sources/weekly_report_2026-10-31.md`,
> `ablation_reorder_not_retrieve.md`, `ablation_graph_vs_retrieval.json`, and `ablation_graph_vs_retrieval.png`.
> Identify: the two arms; the four metrics; at K=20 insertion 34/31, retrieval breaks 3/2 and misses 17/12,
> method 0/0, Kendall tau -0.44/0.00, core Jaccard 0.25; robustness across K=10/20/30; the overturning of week
> 5's "insertion, not reshuffle." Return a claim table with exact source lines. Do not invent numbers. Never
> present draft edges as approved, and never claim a learning gain.

## Fact-check prompt

> Audit `beat_sheet.json` beat by beat against `sources/`. For each claim: beat ID, claim, verdict
> (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, correction. Attend to: insertion 34/31;
> retrieval 3/2 mis-ordered and 17/12 missing; method 0/0; Kendall tau -0.44/0.00; core Jaccard 0.25; K-sweep
> robustness; "overturns week 5"; general embedder; runs on the authoritative CSV (graph.json since reconciled); draft edges; no learning claim.

## Typical commands

```bash
PYTHONUTF8=1 ".venv/Scripts/python.exe" runtime/scripts/generate_audio_kokoro.py "/abs/path/to/reorder-not-retrieve"
TMPDIR=d:/_remotion_tmp TEMP=d:/_remotion_tmp TMP=d:/_remotion_tmp \
  PYTHONUTF8=1 ART_REMOTION_SCALE=2 ART_REMOTION_CONCURRENCY=2 \
  python runtime/scripts/remotion_scenes.py "/abs/path/to/reorder-not-retrieve"
```

## Beat-sheet and visual rules

- `beat_sheet.json` is the source of truth; audio duration is the clock.
- Show the framework (two arms + metrics) before the numbers.
- B05 is the figure (retrieval breaks N, method 0); B06 is the Kendall-tau reorder point; each claim beat holds
  its figure >=2s.
- **CRIMSON = retrieval / broken order, TEAL = graph method / zero violations, SLATE = insertion / scale,
  GOLD = the reorder (tau) finding, SAGE = robustness.**
- Never present draft edges as approved; never claim a learning gain.

## Voice and narration

Kokoro `af_bella` ("Bella"); register pragmatist / skeptical-explainer; greeting "Hello, fellows"; sign-off
"This is Satwik for Humanitarians AI."

## Useful project files

- `sources/` - frozen story source (weekly report, the results writeup, the raw results md+json, the figure)
- `output/reorder-not-retrieve/` (to be produced) - PREMISE, SOURCES, NARRATION-GATE-P, PEDAGOGY, VISUAL-PLAN, beat_sheet.json
- final `.mp4` - the 4K 16:9 master

## Build result for this report

- **Built.** `output/reorder-not-retrieve/week14_reorder-not-retrieve_oct31.mp4` — **4K 16:9** (3840×2160),
  **4:07** (video stream 246.97 s), 30 fps, AAC 192 kbps, volumedetect mean **-21.4 dB**.
- **10 beats, all present and 4K**, each clip extended to its measured narration (via `remotion_scenes.py`):
  B00 31.0 s · B01 24.9 s · B02 27.1 s · B03 28.3 s · B04 24.1 s · B05 29.7 s · B06 22.2 s · B07 18.5 s ·
  B08 30.1 s · B09 11.3 s.
- **PROOF gate:** PEDAGOGY `VERDICT: PASS`; GATE P (NARRATION-GATE-P) passed; `FACT-CHECK.md` `VERDICT: PASS`
  with no corrections — every on-screen number traces to `sources/ablation_graph_vs_retrieval.json`.
- **Numbers verified on the rendered master:** insertion 34 / 31 (B03); dependencies broken 20 / 14 vs method
  0 / 0 (B04); Kendall tau -0.44 / 0.00 (B05); personalization 0.25 / 0.615 (B06); K-sweep method 0/0/0, graph
  inserts 32/34/42, tau -0.33/-0.44/-0.34 (B07).
- **QC:** `output/reorder-not-retrieve/_qc/REPORT.md` (per-beat frames + specs) — **PASS**.
- Video content is pure research progress; the explainer email to Prof. Nik is the separate deliverable
  (`output/reorder-not-retrieve/email_week14_reorder_not_retrieve.md`).

## Current limitations

- general-domain embedder (a biomedical model would shift the ranking, not the structural result);
- runs on the authoritative prereq CSV (Stage-3 `graph.json` since reconciled to it);
- prerequisite edges are faculty-review drafts;
- **no learning-outcome claim.**

## Future work

- done since: reconciled Stage 3 `graph.json` with the authoritative prereq CSVs and regenerated both demo
  roadmaps, so Stage 4 now runs on the real graph;
- fold these numbers into the paper's Results;
- optionally re-run with a biomedical embedder to show the structural result is embedding-independent.

## Final human checklist

- Does the video show the two arms and the metrics before any number?
- Does B05 show retrieval breaking the order vs the method at zero?
- Does B06 make the reorder (Kendall tau) point and note it overturns week 5?
- Is robustness across K shown, and every figure traceable to `sources/`?
- Draft edges never shown as approved; no learning-outcome claim?
- Did a human watch the full output, and has an authorized reviewer approved publication?

## Publication note

The final MP4 is shared separately with the Humanitarians AI publishing team. A successful local build is not
itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
