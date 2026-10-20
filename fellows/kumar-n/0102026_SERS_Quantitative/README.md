# Why SERS Is Hard to Make Quantitative

Sensitive is not the same as quantitative: two reasons SERS calibration is hard, and one common fix.

## About

SERS signal saturates as the metal surface fills with analyte, so calibration curves bend into a Langmuir-type plateau. On top of that, hot spots make raw intensity swing from spot to spot. Internal standards — ratioing to a reference molecule on the same surface — steady the measurement, but compete for surface sites, can overlap peaks, and can photodegrade.

| | |
|---|---|
| **Slug** | `sers-quantitative` |
| **Length** | see `SHOTLIST.md` (~1:35) |
| **Format** | 16:9, 1920×1080 |
| **Narrator** | Liam, in for Kumar Karthik (Kokoro TTS, `am_liam`) |
| **Greeting** | Olá, Liam |
| **Series** | SERS explainers (hot spots · quantitation · gold vs silver) |

## Structure

| Beat | Act | Lane | On screen |
|------|-----|------|-----------|
| B00 | Ask | Remotion | `/explain why won't my SERS calibration curve stay straight?` |
| B01 | BLUF | Remotion | "Signal / keeps / rising / forever." → *forever* retyped as *until full* |
| B02 | The surface fills up | Manim | Calibration curve plateaus as eight surface sites fill (illustrative) |
| B03 | The hot-spot lottery | Manim | One sample, three spots, three intensities (illustrative) |
| B04 | The internal standard | Manim | Analyte + standard bars per spot; level ratio bars; caveats (idealized) |
| B05 | Verdict | Remotion | "Sensitive is not the same as quantitative" + six lines |
| B06 | Handoff | Remotion | `/check where does my SERS calibration curve start to bend?` |
| B07 | Outro | Remotion | Title card · @KumarKarthik |

## Sources

1. Bell, S. E. J., Charron, G., Cortés, E., Kneipp, J., Lamy de la Chapelle, M., Langer, J., Procházka, M., Tran, V., & Schlücker, S. (2020). Towards reliable and quantitative SERS: from key parameters to good analytical practice. *Angew. Chem. Int. Ed.* 59(14), 5454–5462. doi:10.1002/anie.201908154
2. Plasmonic electronic Raman scattering as internal standard for spatial and temporal calibration in quantitative SERS. *J. Phys. Chem. Lett.* (2020). doi:10.1021/acs.jpclett.0c03056
3. Nanogap-engineered core-shell-like nanostructures for comprehensive SERS analysis. arXiv:2412.13882 (Langmuir-consistent signal saturation) — *preprint*
4. Fang, Seong & Dlott (2008), *Science* 321 — hot-spot distribution

Full claim-by-claim verification is in [`FACTCHECK.md`](FACTCHECK.md).

## Fact-check notes

- The Langmuir plateau is typical of surface adsorption, not universal; B02's curve is labeled illustrative.
- B04's ratio bars are drawn perfectly level and labeled *idealized*.
- "Calibrate within the range where the response is still rising" is presented as standard analytical practice.

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
R=examples/_test/sers-quantitative

# Static pre-flight on the Manim scenes
T=$(mktemp -d); cp $R/scenes.py "$T/"
for S in B02_SurfaceFills B03_HotSpotLottery B04_InternalStandard; do
  PYTHONPATH="$PWD/manim" python3 runtime/qc/static_scene_check.py "$T/scenes.py" --class "$S"
done

# Narration audio (fresh beat sheet only)
python3 runtime/scripts/generate_audio_kokoro.py $R

# Review cut + QC gates
ART_FACTS=0 ./art run $R

# Final master (needs FACTCHECK.md, SHOTLIST.md, PROMPTS.md and zero MAJOR defects)
./art final $R
```

Output: `renders/sers-quantitative.mp4`.

> Once audio exists, patch `beat_sheet.json` field-by-field. Replacing the whole file wipes the stamped `audio_file` / `actual_duration_s` values.

## Credits

- **Narration:** synthetic voice (Kokoro TTS, `am_liam`), presented as "Liam, in for Kumar Karthik."
- **Visuals:** all code-rendered (Remotion components and Manim scenes). No third-party footage, images, or music.
- **AI use:** scripts, scenes, and fact-checks were written with Claude and reviewed by the author. See `PROMPTS.md`.
- **Handle:** @KumarKarthik
