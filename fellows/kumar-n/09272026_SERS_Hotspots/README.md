# Hot Spots: Where SERS Signal Comes From

Why SERS spectra vary from spot to spot, and why that matters for machine learning.

## About

SERS signal is concentrated, not spread out. Enhancement scales roughly with the fourth power of the local field, the field piles up in nanometre-scale gaps between metal particles, and in a classic measurement the hottest 63 sites per million produced a quarter of the total signal. That lopsidedness is the physical root of SERS variability, and the reason spectra from one substrate must stay on one side of a train/test split.

| | |
|---|---|
| **Slug** | `sers-hot-spots` |
| **Length** | see `SHOTLIST.md` (~1:50) |
| **Format** | 16:9, 1920×1080 |
| **Narrator** | Liam, in for Kumar Karthik (Kokoro TTS, `am_liam`) |
| **Greeting** | Hallo, Liam |
| **Series** | SERS explainers (hot spots · quantitation · gold vs silver) |

## Structure

| Beat | Act | Lane | On screen |
|------|-----|------|-----------|
| B00 | Ask | Remotion | `/explain why do my SERS spectra vary spot to spot?` |
| B01 | BLUF | Remotion | "SERS / signal / comes from / everywhere." → *everywhere* retyped as *hot spots* |
| B02 | The fourth power | Manim | Log-scale bars: field ×2 → signal ×16; field ×10 → signal ≈ ×10,000 |
| B03 | Where the field piles up | Manim | Two nanoparticles with a glowing nanometre gap (schematic) |
| B04 | 63 in a million | Manim | Share of molecules 0.0063% vs share of signal 24% (Fang et al. 2008) |
| B05 | Why your model cares | Manim | Three spots on one substrate → three different spectra → split by sample (illustrative) |
| B06 | Verdict | Remotion | "Most signal, almost no sites" + six lines |
| B07 | Handoff | Remotion | `/check do my splits keep spots from one substrate together?` |
| B08 | Outro | Remotion | Title card · @KumarKarthik |

## Sources

1. Fang, Y., Seong, N.-H., & Dlott, D. D. (2008). Measurement of the distribution of site enhancements in surface-enhanced Raman scattering. *Science* 321, 388–392
2. Le Ru, E. C., Etchegoin, P. G., & Meyer, M. (2006). Enhancement factor distribution around a single SERS hot-spot and its relation to single molecule detection. *J. Chem. Phys.* 125, 204701. doi:10.1063/1.2390694
3. Dewanjee, U., et al. (2026). Next-generation SERS probes. *Nanomaterials* 16(10), 628 (|E|⁴ scaling, as cited in Paper 2)

Full claim-by-claim verification is in [`FACTCHECK.md`](FACTCHECK.md).

## Fact-check notes

- The |E|⁴ rule is shown as an approximation; ×16 and ×10,000 are arithmetic under that rule.
- Fang et al.'s 63-per-million / 24% result is for one substrate (330 nm Ag-coated nanospheres) and one probe molecule; it is presented as a measured example, not a universal constant.
- B03 is schematic; B05's spectra and hot-spot positions are illustrative.

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
R=examples/_test/sers-hot-spots

# Static pre-flight on the Manim scenes
T=$(mktemp -d); cp $R/scenes.py "$T/"
for S in B02_FourthPower B03_GapHotSpot B04_SixtyThree B05_WhyModelCares; do
  PYTHONPATH="$PWD/manim" python3 runtime/qc/static_scene_check.py "$T/scenes.py" --class "$S"
done

# Narration audio (fresh beat sheet only)
python3 runtime/scripts/generate_audio_kokoro.py $R

# Review cut + QC gates
ART_FACTS=0 ./art run $R

# Final master (needs FACTCHECK.md, SHOTLIST.md, PROMPTS.md and zero MAJOR defects)
./art final $R
```

Output: `renders/sers-hot-spots.mp4`.

> Once audio exists, patch `beat_sheet.json` field-by-field. Replacing the whole file wipes the stamped `audio_file` / `actual_duration_s` values.

## Credits

- **Narration:** synthetic voice (Kokoro TTS, `am_liam`), presented as "Liam, in for Kumar Karthik."
- **Visuals:** all code-rendered (Remotion components and Manim scenes). No third-party footage, images, or music.
- **AI use:** scripts, scenes, and fact-checks were written with Claude and reviewed by the author. See `PROMPTS.md`.
- **Handle:** @KumarKarthik
