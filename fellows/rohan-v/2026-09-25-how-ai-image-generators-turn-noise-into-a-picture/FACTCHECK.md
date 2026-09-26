# FACTCHECK — How AI Image Generators Turn Noise Into a Picture

Every spoken and on-screen claim, its source, and its verdict. Checked
2026-09-25. "The run" means `train_toy_diffusion.py` → `evidence/run.log` /
`evidence/toy_diffusion.json` (SHA-256 `766cab72…5ccf`).

## Claims

| # | Beat | Claim | Source | Verdict |
|---|---|---|---|---|
| 1 | B00 | Opening line "Hi, I am … and this video is about …" | `docs/FELLOWS-SUBMISSION.md` — required wording | ✅ verbatim |
| 2 | B00 | AI narration disclosed | on-screen disclosure line + `metadata.ai_disclosure` | ✅ |
| 3 | B00 | A prompt returns four images | Midjourney returns four images per job — on the web, **one row of four** (Rohan's 29 captures, Midjourney series; the week-03 reel records that the planned '2×2 grid' was wrong) | ✅ — B05's caption was first drafted as "your grid of four" and corrected to "the four images Midjourney hands back" before the final render; the toy's four seeds are laid out 2×2 for space, not to depict Midjourney's layout |
| 4 | B00 | "Nothing was searched for, nothing pasted together" | Diffusion samples from noise (Ho et al. 2020, Alg. 2); the run's nearest-training-picture check: the seed-7 heart differs from its closest training picture by 14.5/255 on average — generated, not retrieved | ✅ for the method and the toy; Midjourney's internals are not published, so the reel states the method, not Midjourney's code |
| 5 | B01 | Midjourney's guide says every image begins as random noise like TV static | Midjourney docs "Seeds": "the random noise you see on a TV screen — it's the first step before your image comes to life" | ✅ quoted (9 words), attributed on screen |
| 6 | B01 | That starting noise comes from a number called a seed | same page: seeds are whole numbers 0–4294967295 that set the starting noise | ✅ |
| 7 | B01 | The model removes a little noise at a time, repeatedly | DDPM sampling, Alg. 2; the toy takes 1,000 steps | ✅ ("1,000 TIMES IN THIS TOY" is labelled as the toy's number) |
| 8 | B02 | Adding noise is simple arithmetic | forward process, eq. 4 — the strip is computed with no model (labelled on screen) | ✅ |
| 9 | B02 | The model is trained to guess what the picture looked like one step earlier | Training predicts the noise ε; sampling uses it to step from x_t to x_{t−1} (eq. 11, Alg. 2) | ✅ — "one drop earlier" is the analogy's wording for one reverse step |
| 10 | B03 | The noisy picture is part picture plus part noise | x_t = √ᾱ_t·x₀ + √(1−ᾱ_t)·ε (eq. 4) | ✅ see algebra below |
| 11 | B03 | At every step the picture's share shrinks and the noise's grows | ᾱ_t = ∏(1−β_s) is strictly decreasing for β_s ∈ (0,1) | ✅ |
| 12 | B03 | By step one thousand, less than one percent of the picture is left | √ᾱ₁₀₀₀ = 0.006353 (export.log); in variance terms ᾱ₁₀₀₀ ≈ 4.0 × 10⁻⁵ — under 1% either way | ✅ measured |
| 13 | B03 | Training shows the model millions of these mixes | the run: 24,000 steps × 256 pictures = 6,144,000 noisy examples | ✅ measured |
| 14 | B03 | …and asks one question: which part is the noise? | L = ‖ε − ε_θ(x_t, t)‖² (eq. 14, "L_simple") | ✅ |
| 15 | B04 | Tiny model, trained on a laptop, no graphics card | run.log: numpy only, `Windows-11`, CPU; 1,626,880 parameters | ✅ |
| 16 | B04 | Twelve thousand pictures of hearts and music notes, 16 pixels across | run.log: "2 prompts x 6000 pictures, 16x16" | ✅ |
| 17 | B04 | About half an hour of training | run.log: "trained in 1862 s" = 31 min | ✅ |
| 18 | B04 | Given pure static and asked for a heart, a thousand steps, ends in a heart | the seed-7 heart run (toyData runs[0]); T = 1000 | ✅ — the result is shown, not described |
| 19 | B05 | Same static + different prompt → a note | seed 38 under both prompts (fork run, export.log) | ✅ — **seed 38, not 7**: chosen by `scan_seeds.py`'s logged rule (best worse-of-two score among 40 seeds; all 40 produced both prompts recognisably). Seed 7's note scored 18.2 — faint — and was not used for this comparison. Disclosed in BUILD-LOG and on screen ("SEED 38") |
| 20 | B05 | Same prompt, different seed → a different heart every time | seeds 101/202/303/404: mean pixel difference between the four pictures 52.2/255 (run.log) | ✅ measured |
| 21 | B05 | That's why Midjourney shows four pictures: one prompt, four starting points | Midjourney docs: "If you don't choose a seed, Midjourney will use a new random one every time, giving you a variety of outcomes" | ✅ — reel says four starting points, not four copies of one seed |
| 22 | B05 | Same seed + same prompt reproduces exactly (on-screen footnote material) | run.log: "seed 7 heart, re-run identical: True" — true of the toy; Midjourney says seeds are "99% identical" and "Not Always Predictable" | ✅ scoped to the toy; not claimed for Midjourney |
| 23 | B06 | Lock the seed when testing a prompt change; it's like a control in an experiment | Midjourney docs: "Lock a seed when testing different elements in your prompts. It's like having a control in an experiment." | ✅ |
| 24 | B06 | Don't use a seed to keep a style or character | docs: "Seeds can't capture or bookmark a specific style, character, or appearance across different prompts" | ✅ |
| 25 | B06 | It only sets the starting static, and has the least effect | docs: "They only influence the initial layout of noise"; "they have the least impact on the final image" | ✅ |
| 26 | B06 | Use style references instead | docs: "we recommend style references, omni references, and personalization" | ✅ |
| 27 | B06 | Add --seed and any whole number | docs: "Add --seed # to the end of your prompt"; range 0–4294967295 | ✅ |

## Algebra, checked separately from the typography (MATH-TYPESETTING.md)

- **Forward process.** x_t = √ᾱ_t·x₀ + √(1−ᾱ_t)·ε, with ε ~ N(0, I), ᾱ_t = ∏_{s=1..t}(1−β_s),
  β linear from 10⁻⁴ to 0.02, T = 1000. Free index: t ∈ {1,…,1000}; x₀ is the clean
  picture (bound); ε is the noise draw. The coefficients satisfy (√ᾱ_t)² + (√(1−ᾱ_t))² = 1,
  which is why the two shares in B02/B03 are **multipliers, not percentages that add to
  100%** — the reel shows them as "× 0.78 / × 0.62", never as percentages.
- **Numerical case.** t = 1000: ᾱ = 4.036 × 10⁻⁵ → √ᾱ = 0.006353, √(1−ᾱ) = 0.99998.
  Computed twice independently (numpy `cumprod` in the exporter; JS `ABAR` in
  `diffusionKit.tsx`, same β schedule) — the on-screen live readout and the typeset
  "≈ 0.0064" agree.
- **Loss.** L = ‖ε − ε_θ(x_t, t)‖² — the model's noise guess ε_θ, compared with the true ε.
  The typeset form keeps the same free variables (x_t, t) as the forward equation.
- **Approximation vs equality.** "≈ 0.0064" is an approximation (rounded) and is
  typeset with ≈, not =.
- **Renderer.** All three rows are outlined SVG from `runtime/scripts/typeset_math.py`
  (matplotlib MathText, STIX); no raw-text fallback was used. Frame checks of the
  revealed equations at 15/50/85% are in `_qc/`.

## What the reel does not claim

- That Midjourney uses this exact model, schedule, step count or guidance weight.
  Midjourney's architecture is not published; the toy is labelled "not Midjourney"
  on screen in B01 and B04.
- That seeds reproduce Midjourney images exactly (Midjourney's own docs say they may not).

## Portrait (9:16) wording

The vertical cut carries shortened on-screen strings (`vertical/beat_sheet.json`)
so its text meets the 9:16 type floor; narration is identical in both cuts. "UNDER
1% LEFT" (12), "GUESS THE NOISE" (14), "ONE SEED, TWO PROMPTS" / "ONE PROMPT, FOUR
SEEDS" (19, 20), "Testing? Lock the seed: --seed 7" (23, 27), "Same style? Use
style references" (24, 26), and the "TOY MODEL" sticker (the honesty label, kept in
both cuts).
