# What Changed in Section 4.5?

A two-week update on §4.5, *Training Strategies for Limited Data*, of the ML-for-SERS review paper.

## About

The revised section matches each training strategy to the shortage it fixes: augmentation when spectra are scarce, self-supervised pretraining when labels are. It replaces an uncited "this is a gap" statement with two recent results (SMAE and SemiRaman) and is honest that both used conventional Raman spectra of bacteria, not SERS.

| | |
|---|---|
| **Slug** | `sers-ml-4-5-update` |
| **Length** | 2:03 |
| **Format** | 16:9, 1920×1080 |
| **Narrator** | Liam, in for Kumar Karthik (Kokoro TTS, `am_liam`) |
| **Greeting** | Jambo, Liam |
| **Series** | Paper 2 update videos (§4.4 · §4.5 · §4.6) |

## Structure

| Beat | Act | Lane | On screen |
|------|-----|------|-----------|
| B00 | Ask | Remotion | `/review what changed in section 4.5?` with a three-line outline |
| B01 | BLUF | Remotion | "Pretraining / helps. / On SERS: / proven." → *proven* retyped as *untested* |
| B02 | Which bottleneck? | Manim | "What is actually scarce?" forks to augmentation (spectra) or pretraining (labels) |
| B03 | Augment realistically | Manim | Noise band around a spectrum swells past realism, then returns (illustrative) |
| B04 | The cost asymmetry | Manim | Big cheap unlabeled pool vs a few expensive labels → pretrain, then fine-tune |
| B05 | The evidence | Manim | SMAE 83.90% vs ResNet 83.40%; SemiRaman 89.2% / 92.0% at 5% / 10% labels; not-SERS caveat |
| B06 | Verdict | Remotion | "Match the strategy to the shortage" + six revision lines |
| B07 | Handoff | Remotion | `/diagnose am I short on spectra or on labels?` |
| B08 | Outro | Remotion | Title card · @KumarKarthik |

## Sources

1. Ren, P., Zhou, R.-G., & Li, Y. (2025). A self-supervised learning method for Raman spectroscopy based on masked autoencoders (SMAE). arXiv:2504.16130; *Expert Systems with Applications* 292, 128576
2. Sun, Z., & Wang, Z. (2026). SemiRaman: A self-supervised contrastive representation learning-based framework for semi-supervised Raman spectral identification of pathogenic bacteria. *Spectrochimica Acta Part A* 349, 127356. doi:10.1016/j.saa.2025.127356

Full claim-by-claim verification is in [`FACTCHECK.md`](FACTCHECK.md).

## Fact-check notes

- SemiRaman's 5% / 10% label results were checked by the author against the full paper (they are not in the abstract).
- B01's "proven → untested" swap is framed in narration as a *tempting conclusion*, not as something either draft claimed.
- B03's spectrum and noise bands and B04's dot counts are illustrative or schematic.

## Open items for the paper

These are fixes to the **paper**, surfaced while fact-checking the video. Details are in `FACTCHECK.md`.

- [ ] Soften the opening of §4.5 ¶4 — the new evidence is on conventional Raman, and the SERS gap the original described still stands.
- [ ] Add a citation for "excessive augmentation noise degrades performance."
- [ ] Confirm the ESWA version of Ren et al. reports the same numbers as the arXiv version.

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
R=examples/_test/sers-ml-4-5-update

# Static pre-flight on the Manim scenes
T=$(mktemp -d); cp $R/scenes.py "$T/"
for S in B02_WhichBottleneck B03_AugmentRealism B04_CostAsymmetry B05_Evidence; do
  PYTHONPATH="$PWD/manim" python3 runtime/qc/static_scene_check.py "$T/scenes.py" --class "$S"
done

# Narration audio (fresh beat sheet only)
python3 runtime/scripts/generate_audio_kokoro.py $R

# Review cut + QC gates
ART_FACTS=0 ./art run $R

# Final master (needs FACTCHECK.md, SHOTLIST.md, PROMPTS.md and zero MAJOR defects)
./art final $R
```

Output: `renders/sers-ml-4-5-update.mp4`.

> Once audio exists, patch `beat_sheet.json` field-by-field. Replacing the whole file wipes the stamped `audio_file` / `actual_duration_s` values.

## Credits

- **Narration:** synthetic voice (Kokoro TTS, `am_liam`), presented as "Liam, in for Kumar Karthik."
- **Visuals:** all code-rendered (Remotion components and Manim scenes). No third-party footage, images, or music.
- **AI use:** scripts, scenes, and fact-checks were written with Claude and reviewed by the author. See `PROMPTS.md`.
- **Handle:** @KumarKarthik
