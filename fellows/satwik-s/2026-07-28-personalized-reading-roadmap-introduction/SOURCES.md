# SOURCES — Personalized, Project-Driven Reading Roadmaps

## The only source

| Source | Path | Kind | Access |
|---|---|---|---|
| Paper draft (manuscript) | `weekly-videos/week-01-paper-introduction/sources/manuscript.pdf` | 14-page working draft, design/methods paper | Extracted to text via `pdftotext -layout` for scripting |

**Rule:** the reel is built **only** from this draft. No external facts, no web lookups, no invented numbers. DOUBLE-CHECK LAW: the source is rewritten in the Pragmatist register, never parroted; anything that would date the video or isn't supported by the draft is stripped.

## What the draft actually supports (used on screen / in voice)

| Claim used | Where in draft | On-screen use |
|---|---|---|
| Trainees get a **fixed, topic-organized** textbook; each works a **different lab project** | Abstract; §1.1 | B00, B01 |
| **38-chapter** volume | Abstract ("fixed 38-chapter textbook"); §1.1 ("a 38-chapter volume") | B00/B01 ("thirty-eight-chapter") |
| The textbook **is not read** — a known failure mode | Abstract; §1.1 | B01 |
| "This is **not a content problem. It is an ordering problem.**" | §1.1 (verbatim thesis) | B02 (the reframe) |
| Framed as a **reordering problem, not a retrieval/summarization problem** | Abstract; §1.4; §5.1 | B02 |
| Similarity is **one signal to select**; the sequencer **reorders under the dependency graph**; "a similarity ranker cannot express 'read A before B'; the graph can" | §3.3; §3.4b; §5.1 | B02, B04 |
| High-similarity sections **deliberately excluded** → logged in `exclusions.json` (selection, not retrieval) | §3.4b; §4.3; §5.1 | B02 (held-back tray), B05 |
| **Four-stage pipeline:** section extraction → metadata tagging → dependency graph → project-aligned sequencing; each stage produces an **inspectable, human-editable artifact** | Abstract; §3 intro; §3.1–3.4; §6 | B03 |
| Stage artifacts: `sections.json`, `metadata/*.yaml`, `graph.json` / `graph.graphml`, `roadmap.md` / `.json` / `.csv` | §3.1–3.4 | B03 chips |
| Stages **1–3 run once per textbook; stage 4 runs per student** | §3 intro | B03 bracket |
| Dependency graph: **sections = nodes, learning dependencies = typed edges** | §3.3 | B04 |
| **Prerequisite edges from the faculty-specified field are authoritative**; LLM proposes conceptual/method/application edges that carry confidence and are **reviewed in the faculty session** | §3.3 (two-pass construction) | B04 |
| Stage 4 output item carries: **Section + role label + reason (why) + lab task it supports + recommended week + matched terms**; ordered by **topological sort over the prerequisite subgraph**, prerequisites auto-included | §3.4c | B05 (what/why/task/first) — reel states the pull-forward **conditionally** ("once faculty-approved prerequisites are available"), see corrections log |
| **Distinct projects → visibly distinct roadmaps** (Projects A LNP–siRNA & B photothermal) | Abstract; §4 | B05 |
| Concept/mechanism/technique examples: particle stability, surface functionalization, cellular uptake, in-vivo pharmacokinetics; zeta potential, endosomal escape, DSPE-PEG; DLS, TEM, MTT | §1.1; §3.2 | B04/B05 node & column labels |
| **Single textbook**; multi-textbook generalization **deferred by design** | §2.3; §5.2; §5.3 | B06 |
| Lab-phase timing is an **advisor-calibrated heuristic, not learned, not adaptive in v1** | §2.3; §3.4a; §5.2 | B06 |
| Stage-3 edge inference is **model-proposed and faculty-reviewed**; LLM outputs are stochastic → mitigated by editable artifacts + faculty review of flagged items | §3.3; §5.4 (LLM dependence) | B04 |
| **Stage-2 tagging is rule-based and deterministic in the current implementation** (author correction — overrides the draft's §3.2 "LLM-assisted first pass"); uncertain metadata + any future model-assisted suggestions stay subject to faculty review | Author direction (2026-07-27); cf. §3.2, §5.4 | B06 (see corrections log) |
| **No learning-outcome claim** — method described & demonstrated; evaluation **deferred to subsequent work** | Abstract; §1.4; §5.3; §6 | B06, B07 |
| Future: **adaptive timing** if usage/progress data become available | §5.2; §5.4 | B06 (deferred panel) |
| Authors & program (Satwik Reddy Sripathi, Riya Singh, Evin Gultepe, Srinivas Sridhar, Nik Bear Brown; CaNCURE, Northeastern) | Title block; §2.1 | Narrator persona (Satwik), sign-off, metadata credit |

## Guardrail ledger — what must NOT appear (per user brief + draft `[TO DO]`s)

| Do NOT claim / show | Why | Enforcement |
|---|---|---|
| **Improved learning outcomes** (any "students learn better / more" claim) | Draft reports none; "This paper does not report learning outcomes" (§1.4, §5.3, §6) | B06 flag "no outcome data yet"; B07 line "Learning outcomes: future work"; nowhere else |
| **All prerequisite relationships are faculty-approved** | Only the faculty-*specified* prerequisite field is authoritative; model-proposed edges are **still under review** (§3.3) | B04 always shows dashed **under-review** edges; verdict says "review is ongoing" |
| **Real-time / adaptive student-progress updating as implemented** | v1 timing is a static advisor heuristic; adaptation is future work (§2.3, §5.2, §5.4) | B06 future panel is greyed + stamped **DEFERRED · not implemented** |
| **Hattie effect sizes** (d ≈ 0.94 / 0.50 / 0.75 / 0.65) | Every d in the draft is a `[TO DO: confirm d-value / edition]` placeholder (§1.2–1.3, References) | No numeric d in voice or on screen; instructional-variable framing omitted to avoid over-claim |
| **Textbook title / authors / edition** | §2.2 is a `[TO DO]` placeholder | Referred to generically ("38-chapter, topic-ordered textbook") |
| **Pilot data, correction rates, graph statistics, Jaccard values, section counts** | All are `[TO DO: insert]` placeholders (Abstract, §3.2, §3.3, §4.2, §4.3) | The roadmap table rows in B05 are ILLUSTRATIVE structure only, drawn from the draft's own dependency example (stability→functionalization→uptake→PK), never presented as measured results |
| **Specific parse_confidence / difficulty thresholds, scoring-function weights, embedding model, prompt text** | All `[TO DO]` in §3.1/§3.2/§3.4b and Appendix A | Not shown; pipeline described at the level the draft states plainly |

## Verbatim quotes shown on screen

| Beat | Quote | Source in draft |
|---|---|---|
| B02 | "This is not a content problem. It is an ordering problem." (compressed on the strike card) | §1.1, final line |

Any other on-screen text is a paraphrase of the draft in the Pragmatist register, not a verbatim lift.

## Numbers appearing in the reel

| Number | Value | Basis |
|---|---|---|
| Textbook chapters | 38 | Stated in Abstract & §1.1 (note: §2.2 tags "38 per architecture document" `[TO DO: confirm]` — used because the Abstract/Intro assert it as fact) |
| Pipeline stages | 4 | §3 (extract, tag, graph, sequence) |
| Program length | (not spoken) | §2.1 says 6 months but inside a `[TO DO]` block → kept out of narration to be safe |

No other quantities are stated. If the draft's `[TO DO]`s are later filled with real figures, revise this file and the affected beats before regenerating audio.

## Corrections / register rewrites applied (DOUBLE-CHECK LAW log)

- De-sensationalized: the draft's educational-theory motivation (effect sizes, four instructional variables) is **omitted** from the reel rather than restated, because its supporting d-values are unconfirmed placeholders — including them would over-claim.
- Version-proofing: no model/version numbers in the body; the composer's `modelLabel` ("Opus 4.8") is UI chrome, not a source claim.
- Framing kept as **argument, not finding**: "reordering, not retrieval" is presented as the paper's *thesis and design rationale* (which the draft supports), never as an empirically validated superiority.

### Post-review corrections (2026-07-27, author-directed)

- **B05 — prerequisite pull-forward made conditional.** Replaced "Prerequisites get pulled earlier automatically" with **"Once faculty-approved prerequisites are available, required background sections can be pulled earlier automatically."** The reel no longer implies prerequisites are *already* actively reordering sections; the pull-forward is stated as contingent on faculty-approved prerequisites existing. B05 visuals (props/show) updated to match (conditional pull-forward). (+8 words → est. 18s→21s.)
- **B06 — tagger corrected to rule-based/deterministic.** The current implementation does **not** use an LLM as the default tagger. Replaced "The tagging uses a language model, so every uncertain tag is reviewed by hand" with **"The current tagging pass is rule-based and deterministic. Uncertain metadata and any future model-assisted suggestions remain subject to faculty review."** This overrides the draft's §3.2 description of an "LLM-assisted first pass." B06 limits chip + show event updated. (+6 words → est. 23s→25s.) **Scope note:** this correction covers the **Stage-2 metadata tagger only**. B04 (Stage-3 dependency-edge inference) retains the draft's "model proposes edges → faculty review" description and was outside this correction — a reviewer should extend it to B04 if the current Stage-3 implementation is also non-LLM.
- **B08 — handoff narration shortened.** Replaced the verbatim-read prompt with a shorter spoken **summary + discussion** ("…draft a dependency-ordered reading roadmap and flag every prerequisite that needs human approval. The goal is not to hide judgment — it is to make that judgment visible."). The composer still shows the full paste-ready prompt on screen; the voice now describes rather than reads it verbatim — a deliberate relaxation of HANDOFF LAW's read-aloud clause. (71→45 words → est. 24s→16s.)
- **Net timing:** estimated total 189s (3:09) → **186s (3:06)**; still inside the 2–3 min target.
