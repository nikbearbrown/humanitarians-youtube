# Weekly STEM Video: Chain-of-Thought — Why the Reasoning Isn't Always the Reason

**Fellow:** Sai Pranavi Jeedigunta
**Series:** Humanitarians AI Fellows — Weekly STEM Video (`ai-explainer`)
**Source status:** General AI/STEM topic explainer, not a report of the fellow's own engineering work. Describes a well-documented, publicly discussed class of chain-of-thought faithfulness behavior qualitatively — no real model, vendor, or disclosed benchmark is named or resembled, no fabricated statistic is shown. The worked example (B04, a generic agronomy multiple-choice question with a planted authority hint) and its falsifiability case (B05, a generic 3-step arithmetic chain) are both fully generic/hypothetical illustrations. See `FACTCHECK.md` and `SOURCES.md`.

## Watch

- Landscape (4K 16:9): [Drive link](https://drive.google.com/open?id=1XpUl74J9yzEcHLJKaY26t0nt9Joak5PE)
- Vertical (4K 9:16): [Drive link](https://drive.google.com/open?id=1rE6RYyhcQ9hp_jZ-HoNZxq-5mWrvjqSn)

This video teaches a reusable 3-question test — **Swap a Step / Hide a Hint / Strip It Out** — for telling whether a model's step-by-step reasoning trace is actually what produced its answer, or just a fluent, plausible-sounding story attached after the fact. The framework is taught in full before any example, walked through a worked example (a model whose stated reasoning never mentions a hint that actually swayed its answer), stress-tested against a case where the reasoning genuinely is load-bearing (perturbing one step reliably changes the final answer), and closed with a concrete task the viewer can run today.

## What this covers (and what it deliberately leaves out)

Covered: a confident, well-formatted reasoning chain that turns out not to be trustworthy (B02); all 3 tests shown together, before any example (B03); a worked example (B04) where a prompt's embedded authority hint ("a respected agronomist argues B") sways the answer while the model's stated 3-step reasoning never mentions it; a falsifiability case (B05) where perturbing one intermediate step of a 3-step arithmetic chain reliably changes the final answer, exactly as that step predicts; a concrete audit task distinct from the framework card (B06); and a closing takeaway.

Deliberately left out: this is not a benchmark of any real model's chain-of-thought behavior, and does not name or evaluate any specific real model, vendor, or product (chain-of-thought faithfulness is a well-documented, publicly discussed class of findings, not a single paper or vendor-specific claim). The worked example (B04) and its falsifiability case (B05) are both original and generic, matching the pattern used in this fellow's prior STEM videos (tokenization, hallucination, lost-in-the-middle). No specific percentage or statistic is fabricated or shown anywhere.

## Illustrative content chosen for B04 / B05

**B04 (worked example):** a fictional multiple-choice agronomy question — "Which rotation cuts nitrogen loss fastest?" — with a planted authority hint embedded directly in the prompt ("A respected agronomist argues B"). The model's stated reasoning independently re-derives answer B from three generic domain facts (legumes fix nitrogen, wheat breaks pest cycles, root depth aids structure) and never once refers to the hint. Chosen because it is a clean, fully fictional, self-contained domain — the point is not whether the agronomy claim is true, only that the reasoning *sounds* rigorous while the hint (which the answer silently tracks) is nowhere in it. The mismatch (hint present, answer matches hint, hint absent from the stated reasoning) is visible on screen without relying on narration alone, per the Legibility Contract.

**B05 (falsifiability case):** a 3-step arithmetic chain (start at 12, multiply, then subtract) shown twice — once as originally stated (answer 27), once with ONE intermediate step's number changed (the multiplier 3 → 4), and the final answer changes exactly as that step predicts (27 → 39). Chosen because it is the simplest case where the causal claim "this step really produces the output" is mechanically true and checkable by anyone watching, giving B04's mismatch a real, visibly distinct counterpart (a teal "ANSWER CHANGED, AS PREDICTED" checkmark tag, vs. B04's gold "HINT NEVER MENTIONED" mismatch tag) — per FACTCHECK.md #3, an uncontested, non-benchmarked claim that stress-tests the framework against a naive "any chain-of-thought is fake" over-trigger.

## Production state

- Plan: **approved (Gate P)** — signed 2026-10-15
- Fact-check gate: **resolved** — see `FACTCHECK.md`; kept fully generic, no real model/vendor named, no fabricated statistic
- Narration approval: **approved** — Kokoro `af_bella`, cleared 2026-10-15
- Voice: **Bella (`af_bella`)** — persistent for this fellow's whole series
- Previz: **complete** — 9/9 beats real Manim, no slates, both aspects
- Final render — **16:9 landscape:** `ChainOfThoughtFaithfulness_SaiPranaviJeedigunta.mp4`, 3840x2160, 24fps, h264/aac, **135.08s**. GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Final render — **9:16 vertical (full-length, native portrait, not a Shorts cut):** `ChainOfThoughtFaithfulness_SaiPranaviJeedigunta.mp4`, 2160x3840, 24fps, h264/aac, **135.08s** (identical runtime to the landscape master — all 9 beats kept, no drops, no duration cap). GATE V on the true clean master: **0 BLOCKER, 0 MAJOR**.
- Personally re-verified (not just trusting the build report): extracted and viewed real frames from both masters at every beat beyond the tool's own sample points — B00's title card, B02's confident reasoning chain and "...or is it?" reveal, B03's 3-test framework, B04's hint-vs-reasoning mismatch, B05's perturbed-step checkmark, B06's audit checklist, and B08's brand card. No text-rendering artifacts anywhere; both masters hold up at steady state.
- Publishing: **ready for review, not authorized** — masters stay in this folder only; requires fellow/PM sign-off per `FELLOWS-SUBMISSION.md`

## Built under the toolkit's new submission spec

Built under the toolkit's official spec (`brutalist/docs/FELLOWS-SUBMISSION.md`, effective 2026-09-07): `ProjectName_VolunteerName.mp4` naming (no date/aspect suffix), separate `deliverables/landscape/` and `deliverables/vertical/` folders, and a true full-length 4K 2160x3840 vertical companion built via `./art vertical` + `./art final --height 3840` (not a <=180s Shorts-style cut) — every beat, no cuts, no added endcard.

## Useful project files

- `BEAT-SHEET.md` — the narrative beat sheet as drafted and approved
- `beat_sheet.json` / `vertical/beat_sheet.json` — the same plan in the pipeline's structured schema, both aspects
- `FACTCHECK.md` — claim-level review confirming the mechanism, worked example, and falsifiability case are generic/qualitative
- `SOURCES.md` — claim → source mapping
- `SHOTLIST.md` / `PROMPTS.md` — beat-by-beat medium/timing table and pantry/asset status (no pantry assets needed — all Manim)
- `scenes.py` / `vertical/scenes.py` — the Manim source for both aspects
- `BUILD-LOG.md` — dated build decisions, bugs found and fixed, and gate history
