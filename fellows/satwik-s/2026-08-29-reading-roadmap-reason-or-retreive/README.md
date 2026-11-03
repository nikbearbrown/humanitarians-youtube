# Weekly Research Report: Does It Reason, or Just Retrieve?

**Fellow:** Satwik Reddy Sripathi
**Week ending:** August 29, 2026
**Research project:** Personalized, Project-Driven Reading Roadmaps (CaNCURE)
**Research sources:** See `progress/output/reading-roadmap-reason-or-retrieve/SOURCES.md` and the single frozen source `progress/sources/week5_video_numbers.md` (every figure carries a trace path into the `personal_roadmap` repo).
**Source status:** This video demonstrates the dependency-graph reordering using **DRAFT, auto-proposed** prerequisite edges (the authoritative graph still has **0 edges**, pending faculty sign-off), and reports the tagging verdict as **provisional (grader 1)**, now hardened with a bootstrap confidence interval. The gold-set second grading, faculty approval of prerequisite links, and any learning-outcome evaluation are presented as future work, not completed results.

This weekly research video asks:

**Does the system actually reason about what to read, or is it just a fancy search — and how would you tell the difference?**

The video answers with a **reusable, four-step "reasons or retrieves?" method**, then walks the dependency graph through it: run the roadmap **with vs. without** the graph, count what a similarity search **could never reach**, name the mechanism **precisely** (insertion vs. reorder), and mark what is still **draft**. The conclusion — the system *selects and sequences*, it doesn't just retrieve — is delivered with its limits shown: the effect is prerequisite **insertion, not reshuffle**, and the edges are **draft, not authoritative**.

The final beat sheet contains **10 beats**. The complete video was generated locally using Brutalist, delivered in **two 4K masters (16:9 + 9:16)** plus **three ≤60-second vertical Shorts**, reviewed end to end (including a PROOF skeptical-explainer pass). The MP4s live in the reel folder and are distributed separately.

## Production state

- Premise / reusable-framework gate (PROOF Phase 1): completed (`PREMISE.md`)
- Plan and beat structure: completed
- Narration generation: completed (Kokoro `af_bella`, run under `PYTHONUTF8=1`)
- Audio timing: completed (measured durations are the clock; total ≈ 3:31)
- Visual beats: 10 of 10 filled (16:9 `ReadingRoadmapsReorder.tsx` + portrait `ReadingRoadmapsReorder916.tsx`)
- Local compilation: completed — **4K 16:9 (3840×2160)** + **4K 9:16 (2160×3840)** via stream-copy assembly
- Vertical Shorts: three ≤60s 4K cuts (hook-led, A/B-led, insertion-led)
- Full-video review + PROOF production gate: completed (teaching 12/12; gate PASS)
- Formal claim-level fact-check: figures traced to `SOURCES.md`; requires final human sign-off before publication
- YouTube publishing: handled separately through the Humanitarians AI review process

## Deliverables

| File (`progress/output/reading-roadmap-reason-or-retrieve/`) | Aspect | Resolution | Duration |
|---|---|---|---|
| `week5_reading-roadmap-reason-or-retrieve.mp4` | 16:9 | 3840×2160 (4K) | 3:31 |
| `short/…-short.mp4` | 9:16 | 2160×3840 (4K) | 3:31 |
| `short/…-short60.mp4` (hook-led) | 9:16 | 2160×3840 (4K) | 0:53 |
| `short/…-short60-abtest.mp4` (A/B-led) | 9:16 | 2160×3840 (4K) | 0:49 |
| `short/…-short60-insertion.mp4` (insertion-led) | 9:16 | 2160×3840 (4K) | 0:55 |

Portrait cuts are **true re-layouts** (the `916` components), not center-crops.

---

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## What this video is about

**Topic:** The dependency graph, turned on — demonstrating selection-and-sequencing vs. retrieval.

For five films the reading-roadmap pipeline has selected sections for a student's project, but the **dependency ordering sat dormant** — 0 prerequisite edges, awaiting faculty. That left a fair skeptical question open: does the system actually *reason* about what to read first, or is it a top-k similarity search in disguise? This week turns the graph **on in draft** (non-destructive) and A/Bs each demo roadmap with it and without it.

The result is turned into a **reusable method** a viewer can apply to any "does my system reason or just search?" question: A/B the mechanism, count what retrieval can't reach, name the mechanism precisely, and mark what's draft.

## Central question

> A retrieval system returns what is *similar*; a reasoning system adds what is *required*. How do you prove — honestly, with the limits shown — that a system does the second, not just the first?

The proposed answer is to run the mechanism with vs. without, count the items a similarity search could never return, name exactly what changed (insertion vs. reorder), and refuse to call a draft authoritative.

## Main ideas presented (10 beats)

1. The dependency graph has been dormant (0 authoritative edges) while faculty review of the prerequisite links is pending — which leaves "reasons or retrieves?" genuinely open.
2. The four-step test: A/B the mechanism · count the unreachable · name it precisely · mark what's draft — shown **before** any result (framework-first).
3. The A/B: same book, same project, only the graph toggled. LNP-siRNA **64 → 100** sections; Photothermal **45 → 64**. The graph grows the list rather than trimming it.
4. What retrieval can't reach: the extra **+36 (LNP) / +19 (PT)** sections are foundations (cell death, what defines a cancer) not similar to the project — a top-k search never returns them, yet they're required first.
5. That is the clearest evidence the system **selects and sequences**, rather than retrieving.
6. Name it precisely: **0 of 64 / 0 of 45** originally-matched sections were reordered — the effect is **insertion** (foundations added and placed first), **not reshuffle** (the matched rank is unchanged).
7. A true similarity-rank inversion needs a small proposer refinement that has not been built — so the reshuffle claim is explicitly withheld.
8. The edges are **DRAFT** (`provenance=metadata_derived`, auto-proposed); the authoritative graph still has **0 edges**; the whole-book proposer flagged **1,483** candidate links — the size of the one-time faculty review, ranked and capped.
9. The tagging verdict (from last week) is **hardened**: dictionary F1 **0.89** [0.85, 0.93] vs model **0.35** [0.27, 0.43]; the F1 gap **0.54, 95% CI [0.44, 0.64]** clears zero — not a small-sample fluke — still provisional (grader 1).
10. Provenance explains *why* the dictionary wins: rule-only tags **85%** correct, model-only **12%**, both-agreed **94%**.

## Current implementation boundary

The video establishes that turning on the dependency graph **adds required foundations a search cannot reach and states explicit read-before links** — evidence of selection and sequencing. It does **not** claim the matched reading list is reordered, and it does **not** claim the ordering is authoritative or that learning outcomes improved.

The result should be understood as follows:

- the reordering is demonstrated on **draft** edges (auto-proposed), run non-destructively; the authoritative graph stays at **0 edges**;
- the effect is **prerequisite insertion + foundations-first**, not a rank inversion of the matched set (0 matched sections moved);
- the tagging win is **provisional (grader 1)**, now with a confidence interval that excludes zero;
- **1,483** is the *size of the faculty review*, not a set of approved edges.

The following require additional evaluation or remain future work: faculty approval of the prerequisite links (activates authoritative ordering); the proposer refinement that would produce a true rank inversion; the gold-set second grading + reconciliation; any learning/engagement claim.

## The reusable method (apply it to a new case)

A viewer can run the same four steps on any "does it reason or just search?" decision:

1. **A/B the mechanism** — run the system with the component and without it, everything else fixed.
2. **Count the unreachable** — the items it adds that a pure retrieval/top-k search could never return.
3. **Name it precisely** — insertion or reordering? Claim only what actually moved.
4. **Mark what's draft** — if it rests on auto-proposed data, label it and say what makes it authoritative.

Decision rule: retrieval returns what's similar; reasoning adds what's required. A good result is a mechanism shown to add the unreachable, claimed precisely; a bad result is calling insertion "reordering," or a draft demo "done."

## How faculty review is used

Faculty review resolves the one expert-judgment step the system deliberately leaves open: whether each **auto-proposed "read A before B" link** is authoritative. The proposer generated **1,483** candidate links (ranked and capped for triage); a single faculty `approve = yes` turns the draft graph authoritative and switches ordering on. Until then the demo is a **preview**, and the video says so on screen (the DRAFT stamp, "authoritative graph: 0 edges").

## Research prompt

Use the following prompt before substantially rewriting the project:

> Research the "Does It Reason, or Just Retrieve?" dependency-graph demonstration for an educational explainer. Begin with `progress/sources/week5_video_numbers.md`, `SOURCES.md`, `PREMISE.md`, and `beat_sheet.json`. Identify the with/without-graph A/B (64→100, 45→64), the +36/+19 foundations a similarity search would miss, why this shows selection-and-sequencing rather than retrieval, the honest caveat (insertion not reshuffle; 0 matched sections reordered), the DRAFT status (auto-proposed edges; authoritative graph 0; 1,483 review size), and the hardened tagging verdict (F1 0.89 vs 0.35; gap CI [0.44, 0.64]). Return a claim table: claim, exact source, pinpoint evidence, confidence, and what still requires verification. Do not invent numbers, model identifiers, or approved edges. Never present a draft edge as authoritative, or insertion as reshuffle.

## Fact-check prompt

Run the following prompt after any narration or beat-sheet change:

> Audit `beat_sheet.json` beat by beat. Extract every factual, numerical, and capability claim and compare each with `week5_video_numbers.md` and `SOURCES.md`. Produce a table with beat ID, claim, verdict (SUPPORTED / QUALIFY / UNSUPPORTED / OUTDATED), evidence, source, and required correction. Pay particular attention to: the 64→100 / 45→64 A/B, the +36/+19 foundations, the "0 matched sections reordered" fact, the DRAFT / authoritative-0 framing, the 1,483 review size, the F1 figures and the gap CI [0.44, 0.64], and the provenance 94/85/12. Flag any framing that calls insertion "reshuffle," any draft edge presented as authoritative, and any tagging figure not marked provisional. Do not silently rewrite narration; list corrections for human review.

## Typical commands

Run from the Brutalist toolkit root. On Windows, prefix Python with `PYTHONUTF8=1` so on-screen em-dashes / middots / arrows do not corrupt, and use the toolkit venv Python for Kokoro.

```bash
PYTHONUTF8=1 python runtime/scripts/generate_audio_kokoro.py "/abs/path/to/reason-or-retrieve"
PYTHONUTF8=1 python runtime/scripts/remotion_scenes.py "/abs/path/to/reason-or-retrieve" --force   # 4K beats
PYTHONUTF8=1 python runtime/scripts/compile.py "/abs/path/to/reason-or-retrieve" --height 2160      # 16:9 clips
# 9:16: rewire beats to the 916 portrait compositions, render, then assemble
```

Final masters were assembled with a **stream-copy concat** of the rendered 4K beats + an audio mux (`ffmpeg -f concat -c copy` + `+faststart`) rather than compile's slow re-encode — it completes atomically and cannot be left half-written.

## Beat-sheet and visual rules

- Treat `beat_sheet.json` as the source of truth; audio duration is the timing clock.
- Show the four-step framework **before** any result (framework-first).
- Every claim beat shows its real table/number, legibly, at the moment the claim is made; comparisons side-by-side, held ≥2s.
- Mark the reordering **DRAFT** (authoritative = 0) and the tagging **provisional (grader 1)** wherever they appear.
- Frame the effect as **insertion, not reshuffle**; never present a draft edge as authoritative or 1,483 as reviewed.
- Portrait (9:16) is a true re-layout via the `916` components, never a center-crop.

## Voice and narration

Kokoro `af_bella` ("Bella"), recorded in `beat_sheet.json`; greeting "Hello, fellows"; sign-off "This is Satwik for Humanitarians AI." Review narration before generating audio; regenerate + remeasure whenever narration changes; on Windows always run audio/render/compile under `PYTHONUTF8=1`.

## Useful project files

- `progress/output/reading-roadmap-reason-or-retrieve/PREMISE.md` — the 4-step framework + falsifiability (insertion, not reshuffle) + CTA
- `SOURCES.md` — no-source-no-verdict ledger (verified figures; what must not be claimed)
- `NARRATION-GATE-P.md` — spoken lines + GATE P (VERDICT: PASS)
- `PEDAGOGY.md` — act structure + PROOF rubric (teaching 12/12)
- `VISUAL-PLAN.md` — per-beat visual treatment + legibility contract
- `beat_sheet.json` (+ `short/beat_sheet.json`) — narration, timing, props, build state (16:9 + 9:16)
- `remotion-src/ReadingRoadmapsReorder.tsx` (16:9) + `…Reorder916.tsx` (portrait) — reel-local components
- `_qc/` — frame-level QC + PROOF production-gate result
- final `.mp4` files — the two 4K masters + three Shorts

## Build result for this report

The reviewed local build produced:

- 10 of 10 filled beats; measured per-beat narration (Kokoro `af_bella`, under `PYTHONUTF8=1`);
- a **4K 16:9** master (3840×2160) and a **4K 9:16** master (2160×3840), both ≈ 3:31, stream-copy assembled;
- **three ≤60s vertical Shorts** (0:53 / 0:49 / 0:55) cut from the portrait beats;
- a complete end-to-end human review plus a PROOF pass (teaching 12/12; production gate PASS).

Build notes: two beats hit a transient Chrome-launch timeout during the 4K render and were topped up individually; an early compile left a truncated master (moov atom missing), which the stream-copy assembly fixed. The `illustrate` motion language carried 6 of 10 beats (above the recommended balance) — expected for a six-body-beat explainer, not a defect.

## Current limitations

- the reordering rests on **draft, auto-proposed** edges; the authoritative graph is empty (0 edges);
- the effect is **insertion + foundations-first**, not a rank inversion of the matched set (0 matched moved);
- the tagging verdict is **provisional (grader 1)**; the CI hardens it but a second grader is pending;
- **1,483** is a review burden, not approved edges;
- single model (`qwen2.5-coder:7b`, temp 0), single gold sample — no learning/engagement claim.

## Future work

- faculty approval of the prerequisite links → activate authoritative ordering → regenerate ordered roadmaps;
- the proposer refinement that would produce a genuine similarity-rank inversion;
- the gold-set second independent grading + reconciliation → final tagger verdict;
- a companion evaluation across more projects and any outcome/engagement study.

## Final human checklist

- Can a new viewer state the four steps and apply them to a new "reasons or retrieves?" case?
- Is the A/B (with vs without graph) clear, and the +36/+19 shown as foundations a search misses?
- Is the result framed as **insertion, not reshuffle**, with "0 matched sections reordered" on screen?
- Is the ordering marked **DRAFT** (authoritative = 0), and 1,483 shown as review size, not approved edges?
- Is the tagging verdict marked **provisional (grader 1)**, with the gap CI clearing zero?
- Are the portrait cuts true re-layouts (not crops), and both masters genuinely 4K?
- Did a human watch the complete output and complete at least one refinement pass?
- Has an authorized human reviewer approved publication?

## Publication note

The final MP4s live in the reel folder and are shared separately with the Humanitarians AI publishing team. After review, the authorized channel manager may upload them (16:9 long + vertical Shorts) to the appropriate Humanitarians AI playlist. A successful local Brutalist build is not itself permission to publish.

<!-- END BRUTALIST REBUILD GUIDE -->
