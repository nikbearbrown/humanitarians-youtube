# Beat 2 — The Dial

**Visual type:** Remotion
**Duration:** ~12 seconds

## What the viewer sees

A token probability distribution chart — a vertical bar chart where each bar represents a possible next token, and bar height represents probability.

The temperature dial from Beat 1 sits in the top-left corner, showing the current setting.

**Temperature 0.0 (0-4s):**
Dial points to 0.0. Label: "T = 0.0"

The bar chart shows one dominant bar towering over everything else. All other bars are nearly flat. An arrow points to the tallest bar: "Always picks this one."

Below the chart: "Deterministic. Same input → same output."

The distribution feels rigid, locked, certain.

**Temperature 0.5 (4-8s):**
The dial animates to 0.5. Label updates: "T = 0.5"

The bars smoothly redistribute. The tallest bar shrinks by about 30%. The second and third bars grow noticeably. The rest grow slightly. The model mostly picks the top bar, but now second place has a real shot.

Below: "Slight variation. Mostly predictable."

**Temperature 1.0 (8-12s):**
The dial animates to 1.0. Label: "T = 1.0"

The distribution flattens dramatically. Many bars are now similar heights. The previously dominant bar is barely taller than the fifth or sixth bar. Rare tokens at the tail end have visible probability mass.

Below: "Creative. Unpredictable."

The distribution feels loose, chaotic, anything-goes.

## Technical notes

- The three distributions should animate smoothly between each other as the dial turns — not jump cuts
- Use ~15-20 bars to represent the token distribution — enough to show the shape, not so many it's cluttered
- The tallest bar's color could shift from cool blue (stable) at T=0.0 to warm red (volatile) at T=1.0
- The dial turning is the visual driver — everything responds to it
- Keep token labels abstract (don't show actual words) — the shape of the distribution is the point
