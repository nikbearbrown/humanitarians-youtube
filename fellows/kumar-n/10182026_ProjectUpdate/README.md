# What Changed in Section 4.6?

A two-week update on §4.6, *Practical Deployment Considerations*, of the ML-for-SERS review paper.

## About

Three subsections, three different fixes. Compute was reframed: compression is the default path to field deployment, with an expected accuracy cost because the evidence comes from outside SERS. Interpretability was updated with real progress (CRIME, GRASS). Generalization was qualified: early SERS cross-device work now exists, but cross-site and cross-substrate generalization remain open.

| | |
|---|---|
| **Slug** | `sers-ml-4-6-update` |
| **Length** | 1:50 |
| **Format** | 16:9, 1920×1080 |
| **Narrator** | Liam, in for Kumar Karthik (Kokoro TTS, `am_liam`) |
| **Greeting** | Ciao, Liam |
| **Series** | Paper 2 update videos (§4.4 · §4.5 · §4.6) |

## Structure

| Beat | Act | Lane | On screen |
|------|-----|------|-----------|
| B00 | Ask | Remotion | `/review what changed in section 4.6?` with a three-line outline |
| B01 | BLUF | Remotion | "All three / parts / needed / rewriting." → *rewriting* retyped as *checking* |
| B02 | Compute: reframed | Manim | Model block shrinks (prune → quantize → distill) → field device → "Accuracy on real SERS? Untested" |
| B03 | Interpretability: updated | Manim | Noisy point-wise attribution regroups into regions (GRASS); CRIME for SERS mixtures (illustrative) |
| B04 | Generalization: qualified | Manim | New instrument gets "early SERS work"; new site and new batch stay "still open" |
| B05 | Verdict | Remotion | "Three subsections, three fixes" + six lines |
| B06 | Handoff | Remotion | `/check would my model survive a new instrument?` |
| B07 | Outro | Remotion | Title card · @KumarKarthik |

## Sources

1. Zaki, J. K., Tomasik, J., McCune, J. A., Bahn, S., Lió, P., & Scherman, O. A. (2025). Explainable deep learning framework for SERS bioquantification. *ACS Sensors* 10(9), 6597–6606. doi:10.1021/acssensors.5c01058
2. Yang, Z., Meng, L., Rui, W., Shen, L., Zhao, S., & Shi, L. (2026). Enhancing explainability in Raman spectroscopy classification with SHAP and spectral segmentation. *Spectrochimica Acta Part A* 344, 126394. doi:10.1016/j.saa.2025.126394
3. Mahmud, S., Sayem, F. R., Hassan, M., Yang, Y., Chowdhury, M. E. H., Zughaier, S. M., et al. Deep learning-based cross-device standardization of surface-enhanced Raman spectroscopy for enhanced bacterial recognition. PMID 40991976

Full claim-by-claim verification is in [`FACTCHECK.md`](FACTCHECK.md).

## Fact-check notes

- **Generalization softened.** The fact-check found Mahmud et al., a SERS-specific cross-device study, so the video says early cross-device work exists rather than "no proof-of-concept."
- The paper's "one to two orders of magnitude" compression figure is uncited, so it is not shown or narrated.
- Kalatzis & Nega (2026) is omitted because it could not be located during checking.
- B03's spectrum and attribution bars are illustrative.

## Open items for the paper

These are fixes to the **paper**, surfaced while fact-checking the video. Details are in `FACTCHECK.md`.

- [ ] Cite Mahmud et al. in the generalization paragraph and remove "not yet produced even an initial proof-of-concept."
- [ ] Add a citation for the compression savings figure.
- [ ] Resolve [U-29] (still marked CITATION NEEDED).
- [ ] Verify Kalatzis & Nega (2026) and GRASS's comparison against GradCAM/LIME from the full texts.

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
R=examples/_test/sers-ml-4-6-update

# Static pre-flight on the Manim scenes
T=$(mktemp -d); cp $R/scenes.py "$T/"
for S in B02_ComputeReframed B03_InterpretUpdated B04_GeneralizeQualified; do
  PYTHONPATH="$PWD/manim" python3 runtime/qc/static_scene_check.py "$T/scenes.py" --class "$S"
done

# Narration audio (fresh beat sheet only)
python3 runtime/scripts/generate_audio_kokoro.py $R

# Review cut + QC gates
ART_FACTS=0 ./art run $R

# Final master (needs FACTCHECK.md, SHOTLIST.md, PROMPTS.md and zero MAJOR defects)
./art final $R
```

Output: `renders/sers-ml-4-6-update.mp4`.

> Once audio exists, patch `beat_sheet.json` field-by-field. Replacing the whole file wipes the stamped `audio_file` / `actual_duration_s` values.

## Credits

- **Narration:** synthetic voice (Kokoro TTS, `am_liam`), presented as "Liam, in for Kumar Karthik."
- **Visuals:** all code-rendered (Remotion components and Manim scenes). No third-party footage, images, or music.
- **AI use:** scripts, scenes, and fact-checks were written with Claude and reviewed by the author. See `PROMPTS.md`.
- **Handle:** @KumarKarthik
