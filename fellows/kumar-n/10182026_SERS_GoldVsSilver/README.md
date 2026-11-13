# Gold vs. Silver: Matching the Metal to the Laser

Why the right SERS metal depends on your laser, and why the absorbance peak isn't the whole story.

## About

SERS enhancement peaks when the laser drives the metal's plasmon near resonance, which gives the common defaults of silver with 532 nm and gold with 785 nm. But clustering — where hot spots form — shifts the resonance, so a suspension's absorbance peak is an unreliable guide to the best laser. Add silver's oxidation versus gold's stability, and the real rule is: test your actual substrate at your actual wavelength.

| | |
|---|---|
| **Slug** | `sers-gold-vs-silver` |
| **Length** | see `SHOTLIST.md` (~1:40) |
| **Format** | 16:9, 1920×1080 |
| **Narrator** | Liam, in for Kumar Karthik (Kokoro TTS, `am_liam`) |
| **Greeting** | Bonjour, Liam |
| **Series** | SERS explainers (hot spots · quantitation · gold vs silver) |

## Structure

| Beat | Act | Lane | On screen |
|------|-----|------|-----------|
| B00 | Ask | Remotion | `/explain should I use gold or silver for my SERS substrate?` |
| B01 | BLUF | Remotion | "Pick / the / brightest / metal." → *metal* retyped as *match* |
| B02 | Ride the resonance | Manim | Laser line slides onto a plasmon band; enhancement meter rises (schematic) |
| B03 | The common pairing | Manim | Silver + 532 nm, gold + 785 nm; Mikac et al. 2022 caption |
| B04 | Clusters shift the peak | Manim | Isolated vs clustered particles; resonance red-shifts; laser follows (schematic) |
| B05 | Brightness vs shelf life | Manim | Silver signal fades with oxidation; gold holds (schematic) |
| B06 | Verdict | Remotion | "Match the metal to the laser" + six lines |
| B07 | Handoff | Remotion | `/check does my laser match my substrate?` |
| B08 | Outro | Remotion | Title card · @KumarKarthik |

## Sources

1. Mikac, L., Rigó, I., Škrabić, M., Ivanda, M., & Veres, M. (2022). Comparison of glyphosate detection by surface-enhanced Raman spectroscopy using gold and silver nanoparticles at different laser excitations. *Molecules* 27(18), 5767. doi:10.3390/molecules27185767
2. Ameer, F. S., Zhou, Y., Zou, S., & Zhang, D. (2014). Wavelength-dependent correlations between UV-vis intensities and SERS enhancement factors of aggregated gold and silver nanoparticles
3. Layered bimetal nanoporous platforms for SERS sensing. arXiv:2510.14706 — *preprint*
4. The performance of plasmonic gold and silver nanoparticle-based SERS. *Iraqi Journal of Science* (Univ. of Baghdad)

Full claim-by-claim verification is in [`FACTCHECK.md`](FACTCHECK.md).

## Fact-check notes

- Silver's oxidation is described as fading "over time"; no timescale is stated because sources differ.
- "Silver often gives stronger enhancement" is hedged — the best metal depends on the laser line.
- B02, B04, and B05 are schematic, not data.

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
R=examples/_test/sers-gold-vs-silver

# Static pre-flight on the Manim scenes
T=$(mktemp -d); cp $R/scenes.py "$T/"
for S in B02_RideResonance B03_CommonPairing B04_ClusterShift B05_ShelfLife; do
  PYTHONPATH="$PWD/manim" python3 runtime/qc/static_scene_check.py "$T/scenes.py" --class "$S"
done

# Narration audio (fresh beat sheet only)
python3 runtime/scripts/generate_audio_kokoro.py $R

# Review cut + QC gates
ART_FACTS=0 ./art run $R

# Final master (needs FACTCHECK.md, SHOTLIST.md, PROMPTS.md and zero MAJOR defects)
./art final $R
```

Output: `renders/sers-gold-vs-silver.mp4`.

> Once audio exists, patch `beat_sheet.json` field-by-field. Replacing the whole file wipes the stamped `audio_file` / `actual_duration_s` values.

## Credits

- **Narration:** synthetic voice (Kokoro TTS, `am_liam`), presented as "Liam, in for Kumar Karthik."
- **Visuals:** all code-rendered (Remotion components and Manim scenes). No third-party footage, images, or music.
- **AI use:** scripts, scenes, and fact-checks were written with Claude and reviewed by the author. See `PROMPTS.md`.
- **Handle:** @KumarKarthik
