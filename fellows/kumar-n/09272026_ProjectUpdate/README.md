# What Changed in Section 4.4?

A two-week update on §4.4, *Hybrid and Multi-Task Architectures*, of the ML-for-SERS review paper.

## About

Section 4.4 went from describing hybrid models to telling readers when they're worth it. The video walks through the revision: an uncited claim that multi-task learning "often" helps is replaced with a controlled, leakage-audited counterpoint; a two-model pipeline becomes the default when tasks aren't naturally coupled; and the physics-constrained autoencoder result gets its missing mechanism.

| | |
|---|---|
| **Slug** | `sers-ml-4-4-update` |
| **Length** | 2:18 |
| **Format** | 16:9, 1920×1080 |
| **Narrator** | Liam, in for Kumar Karthik (Kokoro TTS, `am_liam`) |
| **Greeting** | Namaste, Liam |
| **Series** | Paper 2 update videos (§4.4 · §4.5 · §4.6) |

## Structure

| Beat | Act | Lane | On screen |
|------|-----|------|-----------|
| B00 | Ask | Remotion | `/review what changed in section 4.4?` with a three-line outline |
| B01 | BLUF | Remotion | "Multi-task / learning / helps / often." → *often* retyped as *sometimes* |
| B02 | Before → after | Manim | Two draft paragraphs grow into four revised ones, each with a job |
| B03 | The correction | Manim | Uncited claim boxed; multi-task (AMTLNet) vs single-task (CNN-LSTM) on a leakage-audited split: 84.12% vs ≈ same, Tukey p = 1.0 |
| B04 | Protocol + default | Manim | Naive split swings 0 ↔ 99.9%; audited split ≈30%; decision fork → classifier + regressor |
| B05 | The mechanism | Manim | Negative concentration bars snap non-negative under a physics constraint (illustrative) |
| B06 | Verdict | Remotion | "Complexity has to be earned" + six revision lines |
| B07 | Handoff | Remotion | `/audit was my data split by sample or by spectrum?` |
| B08 | Outro | Remotion | Title card · @KumarKarthik |

## Sources

1. Shamim, M. M. R., et al. (2026). Leakage-robust evaluation and data-scale sensitivity of attention-enhanced multi-task learning for joint fault diagnosis and remaining useful life estimation. arXiv:2607.16493 — *preprint, not peer-reviewed; not SERS*
2. Tan, A., He, Y., Shi, B., Mu, H., Zhang, Y., & Zhao, Y. (2026). ResFusionNet-TSMT: A residual network for pesticide detection using surface-enhanced Raman spectroscopy. *Talanta* 298, 128852. doi:10.1016/j.talanta.2025.128852
3. Georgiev, D., Fernández-Galiana, Á., Vilms Pedersen, S., Papadopoulos, G., Xie, R., Stevens, M. M., & Barahona, M. (2024). Hyperspectral unmixing for Raman spectroscopy via physics-constrained autoencoders. *PNAS* 121. doi:10.1073/pnas.2407439121

Full claim-by-claim verification is in [`FACTCHECK.md`](FACTCHECK.md).

## Fact-check notes

- **B03 reworded.** The 84.12% / Tukey p = 1.0 result compares AMTLNet with a single-task CNN-LSTM that uses a *different* encoder, so the video does not call it an identical-backbone test.
- **B04 corrected.** The audited-split dot shows ≈30% (IMS Bearing, same data and model as the 0–99.9% swing), not the 84.12% C-MAPSS figure.
- **B06 narrowed.** Only verified ResFusionNet design features (dual-stream inputs, attention pooling) are stated.
- B05 bar values are illustrative and labeled on screen.

## Open items for the paper

These are fixes to the **paper**, surfaced while fact-checking the video. Details are in `FACTCHECK.md`.

- [ ] Reword the Shamim et al. comparison in §4.4 — drop "identical-backbone", or cite their §4.5 after reading it.
- [ ] Confirm the low-concentration class-attention claim against the full Tan et al. text.
- [ ] Confirm the [U-55] → Georgiev et al. (PNAS 2024) attribution is applied everywhere.

## Files

| File | What it is |
|------|------------|
| `beat_sheet.json` | Beat-by-beat script: narration, components, props, and stamped audio durations |
| `scenes.py` | Manim scenes for the body beats |
| `FACTCHECK.md` | Every narrated or on-screen claim, its source, and a verdict |
| `SHOTLIST.md` | Per-beat lane, component, duration, and visual source |
| `PROMPTS.md` | On-screen prompts and how AI was used to make the reel |

## Build

Requires the `brutalist.art` toolkit (Kokoro TTS + Remotion + Manim). From the toolkit root:

```bash
R=examples/_test/sers-ml-4-4-update

# Static pre-flight on the Manim scenes
T=$(mktemp -d); cp $R/scenes.py "$T/"
for S in B02_BeforeAfter B03_Correction B04_ProtocolDefault B05_PhysicsConstraint; do
  PYTHONPATH="$PWD/manim" python3 runtime/qc/static_scene_check.py "$T/scenes.py" --class "$S"
done

# Narration audio (fresh beat sheet only)
python3 runtime/scripts/generate_audio_kokoro.py $R

# Review cut + QC gates
ART_FACTS=0 ./art run $R

# Final master (needs FACTCHECK.md, SHOTLIST.md, PROMPTS.md and zero MAJOR defects)
./art final $R
```

Output: `renders/sers-ml-4-4-update.mp4`.

> Once audio exists, patch `beat_sheet.json` field-by-field. Replacing the whole file wipes the stamped `audio_file` / `actual_duration_s` values.

## Credits

- **Narration:** synthetic voice (Kokoro TTS, `am_liam`), presented as "Liam, in for Kumar Karthik."
- **Visuals:** all code-rendered (Remotion components and Manim scenes). No third-party footage, images, or music.
- **AI use:** scripts, scenes, and fact-checks were written with Claude and reviewed by the author. See `PROMPTS.md`.
- **Handle:** @KumarKarthik
