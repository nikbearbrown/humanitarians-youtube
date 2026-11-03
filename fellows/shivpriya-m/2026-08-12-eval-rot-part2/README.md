# Why AI Evaluation Benchmarks Stop Working (Part 2)

**Fellow:** Shivpriya Mane
**Week ending:** August 12, 2026
**Research source:** Fellow-compiled research synthesis on AI evaluation pipeline evolution (same source as Part 1) — covering a Microsoft continuous-benchmark-generation case study, LLM-as-judge drift, and benchmark retirement criteria.
**Source status:** Original research synthesis compiled by the fellow from published work on AI evaluation methodology; all claims verified against the synthesis text (see Evidence section in `PEDAGOGY.md`).

This video is Part 2 of a two-part series on why AI evaluation pipelines stop measuring what they were built to measure. Where Part 1 covered automating the generation of harder test cases, Part 2 covers the two things that generation alone doesn't solve: whether the judge scoring everything is still trustworthy, and knowing when a metric is genuinely dead rather than just in need of a patch.

The video covers a real production case study (an enterprise agent migrating services between deployment platforms, and Microsoft's fix of generating benchmarks from developer intent documents), the LLM-as-judge drift problem (Goodhart's Law operating one layer down, inside the scoring harness itself), concrete recalibration practices (cross-family judging, a 100–500 example gold set, a 75% agreement threshold), and the criteria for retiring a benchmark versus simply replacing it with a harder version.

The beat sheet contains 16 beats: a cold open, an executive summary that recaps Part 1's scope, the Microsoft case study, the judge-drift problem and its fixes, metric-retirement criteria, a closing full-loop diagram (an original visualization built by the fellow), a verdict card, a handoff, and a title-restate outro marked "Part 2 of 2."

## Production state

- Plan approval: complete
- Fact-check gate: complete (`PEDAGOGY.md`, VERDICT: PASS)
- Narration approval: complete (GATE P signed off)
- Audio lock: complete — Kokoro `af_bella` (Bella), Pragmatist register
- Slate previz: rendered and reviewed
- Final render: complete — 3840x2160 (4K, verified via `ffprobe`), 16:9, ~3:49
- Publishing: uploaded to shared Google Drive per program submission process; not published to YouTube by the fellow

## Copyright note

No figures, charts, or diagrams from any source paper are reproduced anywhere in this reel. The closing diagram (B12) is an original visualization the fellow built herself synthesizing the full evaluation loop (production signals → generator → verifier → CI/CD gate → human calibration); it was rebuilt at native 3840x2160 resolution (originally a lower-resolution image) so it renders crisply without upscaling artifacts. Every other visual beat is a native toolkit diagram built from underlying facts and numbers only, per the toolkit's REBUILD LAW.

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## What this video is about

**Topic:** AI Evaluation — Judge Drift and Metric Retirement (Part 2)

This is HAI (Bella), for Humanitarians AI. This episode explains what automated test-case generation alone doesn't solve: the LLM judge that scores everything can itself drift, and even a well-maintained benchmark eventually needs retiring rather than endless patching.

The current plan contains **16 beats**. Its runtime is derived from measured audio (~3:49). The source recorded by the project is the fellow's own compiled research synthesis on AI evaluation pipeline evolution.

## Make your own version

Download the free local toolkit:

```bash
git clone https://github.com/nikbearbrown/brutalist.art.git
cd brutalist.art
./setup --install
./setup
```

The toolkit uses local Kokoro narration and does not require an API key. The beat sheet is the source of truth: one beat per moment, with narration, visual intent, and shot instructions. For this project, start with `beat_sheet.json`. Preserve it before experimenting; make a copy or a branded variant rather than overwriting a finished plan.

Builder used: **`ai-explainer`** (channel `claude-hai`, Pragmatist register).

## Fact-check summary

See `PEDAGOGY.md` for the full evidence table. Every claim in the narration (the Microsoft case study details, the specific calibration-set size and recalibration threshold, the named benchmark-retirement pairs) traces directly to the fellow's research synthesis. Where the source authors explicitly flag a limitation (e.g. their case study's generalizability being unproven), the video states that honestly rather than smoothing it over.

## Build and review loop actually followed

1. **Research and scope:** continuing the two-part series; Part 2 covers the Microsoft case study, judge drift, and metric retirement — material deliberately excluded from Part 1 to keep each video to one focused thesis.
2. **Beat sheet authored:** cold open → executive summary (recapping Part 1) → the Microsoft case study and its honest caveat → judge drift and the fixes (cross-family judging, calibration cadence) → metric retirement criteria → closing full-loop diagram → verdict → handoff → outro.
3. **Visual approach:** continued the copyright-safe, no-external-figures approach from Part 1. One exception handled carefully: the closing diagram (B12) is the fellow's own original synthesis visualization, not a reproduction of any published figure — still legitimate to use, but its original resolution (1092x966) was too low for a clean 4K render, so it was rebuilt at native 3840x2160 before compiling, avoiding upscale blur.
4. **Fact-check:** `PEDAGOGY.md` written with a claim-by-claim evidence table sourced from the research synthesis.
5. **Gate P — narration review:** full narration reviewed by the fellow line by line before any audio was generated; `VERDICT: PASS` recorded in `PEDAGOGY.md`.
6. **Audio generated locally:** Kokoro voice `af_bella` (Bella), Pragmatist register. All 16 beats generated successfully on the first pass.
7. **Compiled and rendered:** `./art final` used directly for the true 4K master (established practice after a resolution issue on a prior submission). A `MOTION.md` upscale warning was raised on the first compile pass (B12's low-resolution source image), resolved by rebuilding that image natively at 4K and recompiling — the warning did not appear on the second pass.
8. **Reviewed:** fellow reviewed the full compiled cut and confirmed it as final without further revision.
9. **Published only by fellow decision:** master uploaded to the shared Google Drive per program instructions; not uploaded to YouTube directly by the fellow.

## Voice and persona

- **Bella — `af_bella`:** Humanitarians AI pragmatist register; used throughout this episode, consistent with Part 1.

## Useful project files

- `beat_sheet.json` — narrative and visual plan (16 beats)
- `PEDAGOGY.md` — narration gate, human approval, and claim-level evidence table
- `media/` — rendered beat clips, plus the original fellow-made 4K diagram used in B12
- `mp3/` — generated Kokoro narration per beat (gitignored — not tracked)
- `*.mp4` — compiled video file (gitignored — not tracked; uploaded separately to Google Drive per submission process)

## Final human checklist

- [x] Can a new viewer state the question after the opening? — Yes: generation alone doesn't fix an eval pipeline — who checks the judge, and who decides a metric is dead?
- [x] Does motion carry the explanation rather than merely decorate it? — Structural diagrams (chip grids, layer stacks, source flow) show the actual mechanisms; the closing diagram visualizes the complete loop discussed across both videos.
- [x] Is every important claim supported? — Yes, every figure and mechanism traces to the fellow's research synthesis; the source authors' own caveats are preserved rather than smoothed over.
- [x] Can the viewer distinguish evidence, interpretation, and opinion? — The Microsoft case study and named benchmark pairs are presented as documented fact; the verdict beat is clearly the episode's synthesis.
- [x] Does the payoff visibly resolve the opening case? — Yes, the verdict beat directly answers the recap question from B01/B02 (what generation alone doesn't solve) with the two things that stay human.
- [x] Is the "Your Turn" prompt concrete enough to use immediately? — Yes: viewers are asked to check when their own LLM judge was last validated against real human labels.
- [x] Did a human watch the complete output and request at least one refinement pass? — Yes: the fellow identified the B12 image-quality issue after the first compile, requested a higher-resolution version, and approved the final cut after the rebuild.

<!-- END BRUTALIST REBUILD GUIDE -->
