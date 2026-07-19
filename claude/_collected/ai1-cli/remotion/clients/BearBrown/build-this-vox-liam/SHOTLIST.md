# SHOTLIST — build-this-vox-liam

Typed work order for every slot. `archive` slots need a provenance sidecar (`<beat>.source.txt`).
Drop filled media into `media/<beat>.png` or `media/<beat>.mp4`; rerun compile — only that slot rebuilds.

---

## Beat Map

| beat_id | type | source | motion | slot status | notes |
|---|---|---|---|---|---|
| B00 | CARD | own | kinetic | SLATE — Remotion CARD | Opening title card — "Build This" serif, terracotta period, "The FAANG window." subtitle |
| B01 | GRAPHIC | own | isotype | SLATE — Manim | Isotype dot grid: engineer silhouettes (crimson subset) + FAANG timeline bar |
| B02 | DOCUMENT | own | drawon | SLATE — Manim/Remotion | Three-column draw-on: MATCH → SPEC → SUPPORT with annotation arrows |
| B03 | GRAPHIC | own | isotype | SLATE — Manim | Two-column bar: $35 (dusty navy) vs $200+/months (terracotta) + hand-off guarantee |
| B04 | STILL | ai | kenburns | SLATE — needs AI still | Grad at laptop, campus workspace; newsprint treatment; focus [0.5, 0.4] |
| B05 | CARD | own | kinetic | SLATE — Remotion CARD | CTA: bearbrown.co, #BuildThis, @NikBearBrown handle |

---

## Slot Details

### B00 — CARD (own, kinetic)
**What it needs:** A Remotion composition or a designed PNG that renders the title card.
- Title: "Build This" (large charcoal serif on newsprint ground `#F3EBDD`)
- Period after: terracotta `#D35F43`
- Subtitle: "The FAANG window."
- Sign: "Olá, Liam" (vox greeting in upper left, smaller italic)
- Bottom: "@NikBearBrown" hairline underline, terracotta
**Reuse option:** Adapt the original `Scene-01-hook.tsx` typography — same heading, different sub.
**Prompt (AI-generated PNG):** `minimalist editorial card, newsprint cream background, large serif text "Build This" with terracotta period, subtitle "The FAANG window", clean typography, no clutter`

---

### B01 — GRAPHIC (own, isotype)
**What it needs:** Manim `IsotypeDotGrid` scene — engineer silhouettes, FAANG timeline.
**Manim scene:** `IsotypeDotGrid` with ~24 silhouettes, ~6 highlighted crimson ("the ones Bear knows").
Below: horizontal timeline bar — FAANG search arc spans "months" width.
Label chips: "Available now" (navy) | "Hired — window closed" (ink).
**vizdata:** count=24, highlight=6, timeline_months=6
**Note:** verify 24/6 split is defensible. Adjust before render.

---

### B02 — DOCUMENT (own, drawon)
**What it needs:** Three-column document card with animated draw-on strokes.
**Columns:**
1. MATCH — "web → web / AI → AI" (draw-on arrows)
2. SPEC — "written before code" (hand-drawn underline sweeps onto spec text)
3. SUPPORT — "Bear on call" (telephone icon draw-on)
**Manim or Remotion:** use `StateCardPair` or a custom Manim three-column layout.
Terracotta annotation arrows between columns animate beat-by-beat with narration.

---

### B03 — GRAPHIC (own, isotype)
**What it needs:** Two-bar price comparison + hand-off guarantee.
**Bar left:** "$35 / hr" — dusty navy `#3D5A80`, height ~30% of frame
**Bar right:** "$200+ / hr · months to hire" — terracotta `#D35F43`, height ~90%
**Below bars:** Hand-off sequence: grad silhouette → arrow → new grad silhouette. Label: "You don't lose a day."
**Manim scene:** Use `IsotypeFraction` or custom bar chart. Duration = 28s beat — animate bars first (10s), hand-off sequence after (8s), hold on comparison (10s).

---

### B04 — STILL (ai, kenburns toward [0.5, 0.4])
**What it needs:** A still image of a grad at a laptop in a campus workspace.
**Treatment:** newsprint — desaturate 80%, contrast 1.15
**Prompt (FLUX / nano-banana):** `young engineer or graduate student working at laptop, modern university workspace, warm natural light, candid, documentary photography style, high resolution`
**Restoration pass:** NATGEO (modern image)
**Label chips (overlay, NOT baked in):** Left: "Real work + income" (dusty navy label chip); Right: "Your build ships" (terracotta label chip)
**Source sidecar:** create `media/B04.source.txt` with provenance URL when downloaded.

---

### B05 — CARD (own, kinetic)
**What it needs:** CTA card — Remotion or PNG.
- Large serif: "bearbrown.co" (charcoal `#2F2A26`)
- Terracotta hairline beneath the URL
- "#BuildThis" tag (terracotta, smaller)
- "@NikBearBrown" handle (bottom right, small, hairline underline)
- Sign-off: "Liam, in for Bear." (italic, small, ink)
**Reuse option:** Adapt CTA block from `Scene-06-cta.tsx` — same URL, update typography.

---

## Rhythm Audit

Sequence: CARD → GRAPHIC → DOCUMENT → GRAPHIC → STILL → CARD
Max consecutive same-type: 1 (no violations). ✓
Motion histogram: kinetic×2, isotype×2, drawon×1, kenburns×1 (no language > 40%). ✓

---

## Assets to Reuse from Original `build-this/`

| Original asset | Where | Reuse in |
|---|---|---|
| `public/build-this/audio/slide-04.mp3` | ElevenLabs narration | Not reused — replaced by Kokoro B03 |
| `src/scenes/Scene-06-cta.tsx` | CTA Remotion component | Adapt typography for B05 card |
| `src/scenes/Scene-01-hook.tsx` | Hook title component | Adapt for B00 card |

No original audio reused — all beats generated from Ogilvy copy via Kokoro am_onyx.
