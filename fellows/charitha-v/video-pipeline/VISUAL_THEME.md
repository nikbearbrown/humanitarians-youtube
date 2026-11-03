# Humanitarians AI — video visual theme

**Source:** [humanitarians.ai](https://www.humanitarians.ai/) CSS tokens + [@humanitariansai](https://www.youtube.com/@humanitariansai) explainer format (e.g. [XML tags video](https://www.youtube.com/watch?v=I5eBnDGoRCM))  
**Use in:** CapCut · Descript · Adobe Rush intro/outro layers

---

## Palette (locked)

| Token | Hex | Use on screen |
|-------|-----|----------------|
| **Obsidian** | `#1B1B1B` | Title text, lower-third bars, outro background |
| **Blood red** | `#7A0000` | Accent line, keyword highlight, “Your turn” label |
| **Warm clay** | `#A89068` | Subtitle, section labels, left rule on cards |
| **Dim gray** | `#4A4D4F` | Secondary body, captions metadata |
| **Mist** | `#797C7F` | Muted labels, figure captions |
| **Silver** | `#8F8F8F` | Borders, dividers |
| **White** | `#FFFFFF` | Card backgrounds, primary text on dark bars |

**Do not use:** bright blues, gradients, drop shadows, rounded “app” UI. Structural honesty only.

**Physics project overlap** (if sim is on screen): embed chrome already uses ochre `#C8860E` and ink `#121212` — that’s fine inside the demo; **overlays** stay on HAI tokens above.

---

## Typography

| Role | Font | Weight | Size (1080p) |
|------|------|--------|----------------|
| **Title (claim)** | Inter | 700–800 | 48–56 px |
| **Subtitle** | Inter | 500 | 22–26 px |
| **Lower third** | Inter | 600 | 28–32 px |
| **Body overlay** | Inter | 400 | 24 px |
| **Code / paths / XML** | JetBrains Mono or Courier New | 400 | 22–24 px |
| **Recap formula** | Inter | 800 | 40 px, centered |
| **Outro tag** | Inter | 500 | 18 px |

CapCut: search **Inter** in text styles. Save as preset **HAI — Title**, **HAI — Lower third**, **HAI — Mono**.

Descript: Brand kit → add these hex values + Inter if available.

---

## Reusable layers (every video)

### 1. Intro title card (3 sec)

```
┌─────────────────────────────────────────────┐
│ ▌                                           │  ← 6px warm clay (#A89068) left bar
│ ▌  [CLAIM AS TITLE — 2 lines max]          │  ← obsidian, Inter Bold 52px
│ ▌  Physics Vol. 1 · Ch. 4                   │  ← dim gray, Inter Medium 24px
│                                             │
│                              humanitarians ai│  ← mist, 16px, bottom-right
└─────────────────────────────────────────────┘
   white background #FFFFFF, no shadow
```

### 2. Lower third (hook, problem labels, recap)

- Bar: obsidian `#1B1B1B`, height ~72px, width ~55% of frame, bottom-left
- Text: white Inter Semibold 30px
- Optional 3px blood-red top edge on bar
- Examples: `P1 — Wrong "done"` · `Same words. Different result.`

### 3. Keyword highlight (during “Why” beat)

- Single word or short phrase in **blood red** `#7A0000` while rest stays obsidian
- Do not animate — hard cut or static overlay

### 4. Code / demo callout

- White box, 1px silver border `#8F8F8F`
- Monospace 22px obsidian
- 4px warm-clay left border (matches textbook figure chrome)

### 5. “Your turn” banner

- Full-width strip, bottom of frame
- Background: warm clay `#A89068` at 95% opacity **or** white with blood-red left bar
- Label **YOUR TURN** in blood red 14px tracked caps
- Instruction line in obsidian Inter 26px

### 6. Outro (5 sec)

```
┌─────────────────────────────────────────────┐
│         obsidian background #1B1B1B        │
│                                             │
│     [Title claim — white, Inter Bold]       │
│     humanitarians ai · Physics Vol. 1       │  ← warm clay
│                                             │
└─────────────────────────────────────────────┘
```

Channel outros often repeat the title claim + tag (see XML video outro pattern).

---

## Captions (CapCut auto-caption style)

| Setting | Value |
|---------|--------|
| Font | Inter Bold |
| Color | White `#FFFFFF` |
| Stroke / background | Black 60% box **or** 2px obsidian stroke |
| Position | Bottom center, above “Your turn” if present |
| Max chars/line | ~32 (punchy, not paragraph blocks) |

Fix in post: `utils.js`, `FigureWithSim`, `postMessage`, commit hashes.

---

## Contrast demo (A vs B) — split layout

When showing two treatments (gallery vs side-by-side, plain vs XML):

| Panel | Label chip |
|-------|------------|
| **A** | Obsidian bar, white text: `WITHOUT` |
| **B** | Blood-red bar, white text: `WITH` |

Labels top-left of each half. 1px silver divider between panels. No diagonal wipes — hard cut or 0.2s fade.

---

## CapCut preset checklist

Create once, reuse on both videos:

- [ ] **HAI Intro** — white slide, clay left bar, title + subtitle text blocks
- [ ] **HAI Lower third** — obsidian bar template
- [ ] **HAI Your turn** — bottom banner
- [ ] **HAI Outro** — obsidian full frame
- [ ] **Caption style** — Inter white + dark stroke
- [ ] **Mono callout** — bordered code box

Import screen recording → apply intro 3s → add lower thirds at beat markers → captions → outro 5s → export 1080p H.264.

---

## Title card HTML

Pre-built intro/outro frames (open in browser @ 1280×720, screenshot or OBS capture):

`title-cards.html` — same folder.

---

## Video 1 & 2 — copy for cards

| Video | Intro title (obsidian) | Subtitle (dim gray) |
|-------|------------------------|---------------------|
| **1** | Why a green build still ships a broken physics demo | Physics Vol. 1 · Ch. 4 · canvas embeds |
| **2** | Why putting the simulation at the bottom breaks the lesson | FigureWithSim · Ch. 4 scope |
