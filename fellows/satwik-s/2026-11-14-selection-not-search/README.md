# Weekly Research Report: Selection, Not Search (Stage 4b Matching)

**Fellow:** Satwik Reddy Sripathi
**Week ending:** November 14, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** `sources/` - `weekly_report_2026-11-14.md`, `matching_selection.md`, `matching_signal_ablation.md`, `matching_signal_ablation.json`, `matching_signal_ablation.png`. Every on-screen number traces to these.
**Source status:** The ablation is **measured and reproducible** (`scripts/ablation_matching_signals.py`), swept over K so it is not cherry-picked, and isolates **one stage** (matching, Stage 4b) with no sequencing involved. It runs on **faculty-review draft** section metadata, so it measures the **mechanism**, not approved content, and makes **no learning-outcome claim**. Embedder is the general-domain `all-MiniLM-L6-v2`.

This is the stage where the system decides which sections a project actually needs. The headline design claim of
the whole project is that this is a selection problem, not a retrieval problem. So this week -

**I measured it at the matcher: of the top-20 most similar sections, 85% (one project) and 60% (the other) share
no specific project vocabulary, so a pure similarity search would fill the roadmap with topically-near but
project-irrelevant reading. The matcher instead selects on shared vocabulary, labels each section with a role,
and logs every high-similarity rejection, which is the cleanest proof it selects rather than retrieves.**

The final beat sheet contains **10 beats**. The complete video is generated locally with the free Brutalist
toolkit, delivered as a **4K 16:9 master**, reviewed end to end (including a PROOF skeptical-explainer pass).

## What was done this week

- **Built the matching-signal ablation** (`scripts/ablation_matching_signals.py`): two arms on the two standing
  projects, same embeddings, swept over K in {10, 20, 30}. Retrieval = top-k by similarity; selection = the real
  matcher. Isolates Stage 4b; no sequencing.
- **Measured.** Top-20 similar sections sharing no specific project vocabulary: **17/20 (85%)** for LNP-siRNA,
  **12/20 (60%)** for photothermal; consistent across the K sweep. The matcher selects **32** and **26**
  sections as a role-labelled structure (core platform / supporting method / foundational background / optional
  extension) and logs **864** and **559** exclusions, of which **109** and **63** are "high similarity, no shared
  vocabulary".
- **Grounded** it in the information-retrieval distinction between topical similarity and task relevance, and
  wrote it up as paper-ready Stage-4b evidence (`docs/matching_selection.md`).

## How this connects to the series

This is the matching episode of the **pipeline component series** (`docs/pipeline_work_plan.md`): build the
textbook model, read the student, **select (this week)**, make it reproducible, prove it personalizes. Last week
measured the project parser (reading the student); this week measures what the system does with that reading.

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## Central question

> If you ranked every section by similarity to the project and took the top ones, would you get the same reading
> set the matcher chooses - or is selection doing something a similarity search cannot?

The answer: 60 to 85% of the most similar sections share no specific project vocabulary, so similarity alone
would fill the roadmap with the wrong sections. The matcher selects on shared vocabulary, labels each section by
role, and logs every high-similarity rejection. Measured, swept, reproducible.

## Main ideas presented (10 beats)

1. **The challenge (hook).** "Isn't matching just semantic search?" The fair test: rank by similarity and see if
   you get the same sections the matcher selects.
2. **The setup (framework-first).** Two arms, same project, same embeddings: retrieval = top-k by similarity;
   selection = include a section only if it shares a specific project term, and label it by role.
3. **The two signals.** Similarity (paraphrase-tolerant, imprecise) and shared controlled vocabulary (precise).
   Relevance to *this project* is a vocabulary property, not a distance property.
4. **Similarity is not relevance (the number).** Of the top-20 most similar sections, 85% (LNP-siRNA) and 60%
   (photothermal) share no specific project vocabulary. (The figure: tall crimson bars.)
5. **It is robust.** The pattern holds across K = 10, 20, 30 - not cherry-picked.
6. **Selection produces structure, not a list.** The matcher selects 32 and 26 sections, each with a role
   assigned by which metadata category overlapped. Similarity alone cannot produce that structure.
7. **The weights do not decide the structure.** Role is category membership, not a tuned threshold; the signal
   weights only order sections within a role.
8. **The exclusion log is the evidence.** 864 and 559 rejects, of which 109 and 63 are "high similarity, no
   shared vocabulary": exactly what a top-k search would return, set aside with a recorded reason.
9. **The honest boundary.** General embedder; faculty-review draft metadata; two standing projects; no
   learning-outcome claim. A biomedical embedder reorders "similar", not the structural result.
10. **Verdict / CTA.** Selection, not search - and the cleanest proof a system selects is the list of what it
    rejected.

## Current implementation boundary

- **Measured and reproducible**; swept over K; isolates Stage 4b (no sequencing).
- Runs on **faculty-review draft** metadata - measures the mechanism, not approved content.
- **General-domain embedder.**
- **No learning-outcome claim.**

## The reusable framework

1. **To prove selection beats search, remove the selection signal and measure what changes** (ablation), do not
   argue it.
2. **Measure the right thing** - here, how much of a pure ranker's output shares no task-specific signal, not
   just overlap counts.
3. **Sweep the free parameter** (K) so the result is robust.
4. **Treat the reject log as a result** - what a system refuses to return is as informative as what it returns.

## Research grounding

The gap between topical similarity and task relevance is long established in information retrieval (nearness in a
vector space is aboutness, not relevance); controlled-vocabulary term matching (the MeSH indexing tradition) is
the precise-relevance counterpart; role- or facet-labelled results are the established alternative to a single
ranked list; ablation is the standard attribution method. Citations in `sources/matching_selection.md`.

## Research prompt

> Research the "Selection, Not Search" explainer. Begin with `sources/weekly_report_2026-11-14.md`,
> `matching_selection.md`, `matching_signal_ablation.json`, and `matching_signal_ablation.png`. Identify: the two
> arms; the two signals; top-20 no-vocabulary 17/20 (85%) and 12/20 (60%); K-sweep robustness; selection of 32
> and 26 with role structure; 864 and 559 exclusions with 109 and 63 "high similarity, no shared vocabulary".
> Return a claim table with exact source lines. Do not invent numbers. Never present draft metadata as approved,
> and never claim a learning gain.

## Fact-check prompt

> Audit `beat_sheet.json` beat by beat against `sources/`. For each claim: beat ID, claim, verdict
> (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, correction. Attend to: 85% and 60% top-20
> no-vocabulary; K-sweep robustness; 32 and 26 selected; role structure; 864 and 559 exclusions; 109 and 63
> high-similarity-no-vocabulary; general embedder; draft metadata; no learning claim.

## Typical commands

```bash
PYTHONUTF8=1 ".venv/Scripts/python.exe" runtime/scripts/generate_audio_kokoro.py "/abs/path/to/selection-not-search"
TMPDIR=d:/_remotion_tmp TEMP=d:/_remotion_tmp TMP=d:/_remotion_tmp \
  PYTHONUTF8=1 ART_REMOTION_SCALE=2 ART_REMOTION_CONCURRENCY=2 \
  python runtime/scripts/remotion_scenes.py "/abs/path/to/selection-not-search"
```

## Beat-sheet and visual rules

- `beat_sheet.json` is the source of truth; audio duration is the clock.
- Show the framework (two arms + two signals) before any number.
- B04 is the figure (top-k similar with no project vocabulary vs the matcher's rejects); B08 is the exclusion
  log; each claim beat holds its figure >=2s.
- **CRIMSON = similarity-only / rejected, TEAL = selection / shared vocabulary, SLATE = role structure / scale,
  GOLD = the "similarity is not relevance" finding, SAGE = robustness across K.**
- Never present draft metadata as approved; never claim a learning gain.

## Voice and narration

Kokoro `af_bella` ("Bella"); register pragmatist / skeptical-explainer; greeting "Hello, fellows"; sign-off
"This is Satwik for Humanitarians AI."

## Useful project files

- `sources/` - frozen story source (weekly report, the results writeup, the raw results md+json, the figure)
- `output/selection-not-search/` (to be produced) - PREMISE, SOURCES, NARRATION-GATE-P, PEDAGOGY, VISUAL-PLAN,
  beat_sheet.json
- final `.mp4` - the 4K 16:9 master

## Build result for this report

- **Built.** `output/selection-not-search/week16_selection-not-search_nov14.mp4` — **4K 16:9** (3840×2160),
  **4:46** (video stream 286.00 s), 30 fps, AAC 192 kbps, volumedetect mean **-21.5 dB**.
- **10 beats, all present and 4K**, each clip extended to its measured narration (via `remotion_scenes.py`):
  B00 29.9 s · B01 30.3 s · B02 28.8 s · B03 29.5 s · B04 24.7 s · B05 32.5 s · B06 29.9 s · B07 33.1 s ·
  B08 34.9 s · B09 12.7 s.
- **PROOF gate:** PEDAGOGY `VERDICT: PASS`; GATE P (NARRATION-GATE-P) passed; `FACT-CHECK.md` `VERDICT: PASS`
  with no corrections — every on-screen number traces to `matching_signal_ablation.json`.
- **Numbers verified on the rendered master:** top-20 no-vocabulary 85% (17/20) / 60% (12/20) (B03); K-sweep
  LNP 90/85/83%, photothermal 80/60/57% (B04); selection 32 / 26 with role structure (B05); exclusions 864 / 559
  with 109 / 63 high-similarity-no-vocabulary (B07). Totals reconcile (864=577+109+178; 559=63+234+262).
- **QC:** `output/selection-not-search/_qc/REPORT.md` (per-beat frames + specs) — **PASS**.
- Video content is pure research progress; the explainer email to Prof. Nik is the separate deliverable
  (`output/selection-not-search/email_week16_selection_not_search.md`).

## Current limitations

- general-domain embedder (a biomedical model would reorder "similar", not the structural result);
- faculty-review draft metadata;
- two standing projects (robust across K, not a many-project benchmark);
- **no learning-outcome claim.**

## Future work

- re-run on a larger project suite in the personalization-at-scale week;
- optionally re-run with a biomedical embedder to confirm the structural result is embedding-independent.

## Final human checklist

- Does the video show the two arms and the two signals before any number?
- Does B04 show how much of the top-k similar set shares no project vocabulary?
- Does B08 make the exclusion-log point (what a top-k search would have returned, set aside)?
- Is robustness across K shown, and every figure traceable to `sources/`?
- Draft metadata never shown as approved; no learning-outcome claim?
- Did a human watch the full output, and has an authorized reviewer approved publication?

## Publication note

The final MP4 is shared separately with the Humanitarians AI publishing team. A successful local build is not
itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
