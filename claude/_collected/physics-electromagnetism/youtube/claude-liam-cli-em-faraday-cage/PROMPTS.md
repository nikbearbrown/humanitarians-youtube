# PROMPTS — claude-liam-cli-em-faraday-cage

Beat-prefixed prompts for any open slots.

## B01 — PROBLEM slate
If upgrading to a graphic:
```
Generate a Manim or Remotion title card: top line "Faraday cage" (large serif),
sub-line "field inside conductor = 0  [Gauss's law]", 
third line "holds only if  d_copper >> δ  (skin depth)",
palette: white background, dark ink, terracotta accent on the >> symbol.
```

## B04 — Manim: B04_SkinDepth
Auto-rendered by run.sh from scenes.py:B04_SkinDepth.
If re-prompting: two log-log panels; left δ(f) copper, right A_dB(f) copper 1mm;
MRI 64 MHz marker on both; annotation "8.4 μm → 1033 dB/mm".

## B06 — Manim: B06_Materials
Auto-rendered by run.sh from scenes.py:B06_Materials.
If re-prompting: three log-log curves (copper/aluminum/SS304); 64 MHz marker;
legend with delta_um values; note "Cu conductivity 44× better than SS304".

## B07 — SUMMARY slate
If upgrading to a graphic:
```
Generate a Remotion/Manim recap card:
  Title: δ = √(2ρ / ωμ₀)
  Three-row table: Material | δ @ 64 MHz | A_dB (1mm)
    Copper     | 8.4 μm  | 1033 dB
    Aluminum   | 10.5 μm |  823 dB
    SS 304     | 54 μm   |  160 dB
  Caption: "One prompt. One formula. Every RF-shielded room."
  Palette: white bg, dark ink, terracotta accent on copper row.
```
