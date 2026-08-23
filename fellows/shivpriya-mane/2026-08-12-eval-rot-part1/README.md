# Why AI Evaluation Benchmarks Stop Working (Part 1)

**Fellow:** Shivpriya Mane
**Week ending:** August 12, 2026
**Research source:** Fellow-compiled research synthesis on AI evaluation pipeline evolution — covering Goodhart's Law and benchmark saturation, the "Benchmark Self-Evolving" multi-agent framework, and related automated-eval literature.
**Source status:** Original research synthesis compiled by the fellow from published work on AI evaluation methodology; all claims verified against the synthesis text (see Evidence section in `PEDAGOGY.md`).

This video explains why AI evaluation benchmarks lose their usefulness over time and walks through one real, fully automated fix. The video's core question: **once a benchmark becomes the target teams optimize against, how do you keep it honest?**

The video covers Goodhart's Law and benchmark saturation as the root cause, real numbers from MMLU's saturation timeline (GPT-3 ~43% to GPT-4 86.4% in about three years), and a deep walkthrough of the Benchmark Self-Evolving system — a four-agent-role pipeline that automatically generates harder test cases from existing ones, including its real limitation (it tests robustness through surface-level transformations, not deeper capability drift).

This is **Part 1 of a two-part series**. Part 2 (planned) covers a real production case study (continuous benchmark generation from developer intent documents), the LLM-as-judge drift problem, and when to retire a metric versus patch it.

The beat sheet contains 14 beats: a cold open, an executive summary, the root-cause explanation, real MMLU evidence, the Benchmark Self-Evolving mechanics (agent roles, reframing operations, results, limitation), the generalized generator-verifier pattern, a verdict card, a handoff, and a title-restate outro marked "Part 1 of 2."

## Production state

- Plan approval: complete
- Fact-check gate: complete (`PEDAGOGY.md`, VERDICT: PASS)
- Narration approval: complete (GATE P signed off)
- Audio lock: complete — Kokoro `af_bella` (Bella), Pragmatist register
- Slate previz: rendered and reviewed
- Final render: complete — 3840x2160 (4K, verified via `ffprobe`), 16:9, ~3:31
- Publishing: uploaded to shared Google Drive per program submission process; not published to YouTube by the fellow

## Copyright note

No figures, charts, or diagrams from any source paper are reproduced anywhere in this reel. All visual beats are original diagrams built natively in the toolkit from the underlying facts and numbers, per the toolkit's REBUILD LAW — a deliberate choice since this reel may publish to the org's YouTube channel, where reproducing paper figures would carry real copyright risk even with citation.

<!-- BEGIN BRUTALIST REBUILD GUIDE -->

## What this video is about

**Topic:** AI Evaluation — Why Benchmarks Rot (Part 1)

This is HAI (Bella), for Humanitarians AI. This episode explains why AI evaluation benchmarks quietly stop measuring what they were built to measure, and walks through one real automated system — Benchmark Self-Evolving — built to generate fresh, harder test cases without human intervention.

The current plan contains **14 beats**. Its runtime is derived from measured audio (~3:31). The source recorded by the project is the fellow's own compiled research synthesis on AI evaluation pipeline evolution.

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

See `PEDAGOGY.md` for the full evidence table. Every claim in the narration (MMLU's specific saturation numbers, the four-agent-role architecture, the two named reframing operations, the verifier's result) traces directly to the fellow's research synthesis. Where the source names only two of six reframing operations explicitly, the video states this honestly ("+ four more reframing operations") rather than inventing plausible-sounding names for the rest.

## Build and review loop actually followed

1. **Research and scope:** the fellow's research synthesis covered four distinct paradigms for automated eval evolution; scope was deliberately narrowed to one thesis (Goodhart's Law → Benchmark Self-Evolving mechanics) for a focused first video, with the remaining material split into a planned Part 2.
2. **Beat sheet authored:** cold open → executive summary → root cause (Goodhart's Law, benchmark saturation) → real MMLU evidence → the quieter "drift" failure mode → Benchmark Self-Evolving mechanics (pre-filter, creator, reframing operations, verifier, result) → limitation → generalized pattern → verdict → handoff → outro.
3. **Visual approach decided:** the fellow flagged copyright risk in reproducing paper figures for a video that may publish to the org's YouTube channel. Resolved by using only original, toolkit-native diagrams (REBUILD LAW) throughout — no screenshots or reproductions of any source figure.
4. **Fact-check:** `PEDAGOGY.md` written with a claim-by-claim evidence table sourced from the research synthesis, explicitly noting where the source under-specifies detail (the four unnamed reframing operations) so the video doesn't overstate what's known.
5. **Gate P — narration review:** full narration reviewed by the fellow line by line before any audio was generated; `VERDICT: PASS` recorded in `PEDAGOGY.md`.
6. **Audio generated locally:** Kokoro voice `af_bella` (Bella), Pragmatist register. All 14 beats generated successfully on the first pass. Measured duration (~3:31) confirmed to exceed the program's 3-minute Shorts cap — flagged for trimming when the 9:16 derivation is produced.
7. **Compiled and rendered:** `./art final` used directly (not bare `compile.py`) to ensure the true 4K master, following a resolution issue identified in a prior submission. Resolution verified via `ffprobe` (3840x2160) before considering the render complete.
8. **Reviewed:** fellow reviewed the full compiled cut and confirmed it as final without further revision.
9. **Published only by fellow decision:** master uploaded to the shared Google Drive per program instructions; not uploaded to YouTube directly by the fellow.

## Voice and persona

- **Bella — `af_bella`:** Humanitarians AI pragmatist register; used throughout this episode.

## Useful project files

- `beat_sheet.json` — narrative and visual plan (14 beats)
- `PEDAGOGY.md` — narration gate, human approval, and claim-level evidence table
- `media/` — rendered beat clips (all Remotion-native, no external images)
- `mp3/` — generated Kokoro narration per beat (gitignored — not tracked)
- `*.mp4` — compiled video file (gitignored — not tracked; uploaded separately to Google Drive per submission process)

## Final human checklist

- [x] Can a new viewer state the question after the opening? — Yes: once a benchmark becomes the optimization target, how do you keep it honest?
- [x] Does motion carry the explanation rather than merely decorate it? — Structural diagrams (layer stacks, chip grids) show the actual pipeline mechanics and comparison data.
- [x] Is every important claim supported? — Yes, every figure and mechanism traces to the fellow's research synthesis; unverified details (the unnamed reframing operations) are explicitly flagged as such rather than invented.
- [x] Can the viewer distinguish evidence, interpretation, and opinion? — Real MMLU numbers are shown as hard evidence; the verdict beat is clearly framed as the episode's synthesis.
- [x] Does the payoff visibly resolve the opening case? — Yes, the verdict beat directly answers the Goodhart's Law problem raised in the opening with the generator-verifier pattern, while honestly noting what it doesn't solve.
- [x] Is the "Your Turn" prompt concrete enough to use immediately? — Yes: viewers are asked to audit a benchmark they rely on for the same exploitable-pattern risk.
- [x] Did a human watch the complete output and request at least one refinement pass? — Narration was approved on first draft with only a scope decision made in advance (splitting into two videos); the compiled cut was approved without further changes.

<!-- END BRUTALIST REBUILD GUIDE -->
