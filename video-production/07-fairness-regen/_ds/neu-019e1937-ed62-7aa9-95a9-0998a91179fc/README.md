# Northeastern University — Design System

A working visual constitution for any creative or digital output produced under the Northeastern University brand: course materials, data visualizations, slide decks, reports, web components, and print collateral.

> **Source of truth:** [brand.northeastern.edu](https://brand.northeastern.edu). When this system and the Brand Center conflict, the Brand Center wins.
> **Governance:** All externally-facing work requires brand review at [brand.northeastern.edu/brand-reviews](https://brand.northeastern.edu/brand-reviews/).

## Index

- `colors_and_type.css` — design tokens (colors, type, spacing, motion) as CSS variables + semantic element classes
- `assets/` — wordmark and N-monogram placeholders (see Caveats)
- `preview/` — design-system cards rendered in the Design System tab
- `ui_kits/marketing/` — high-fidelity marketing-site UI kit (header, hero, story cards, footer, etc.)
- `SKILL.md` — Agent Skills entry point

---

## Content fundamentals

Northeastern speaks with the confidence of a major research university and the warmth of a community shaped by experiential learning. Copy is grounded, specific, and human — not bureaucratic, not over-promotional.

**Voice:**
- **Bold but measured.** "Our bold design expresses our personality and caliber." Confident framing, never hype.
- **Active and specific.** Real people, real cities, real outcomes. "From Boston to London to Oakland" beats "across our global network."
- **Plural and inclusive.** "We," "our," and "students and faculty" — the institution speaks as a community, not from a tower.
- **AP Stylebook** with Northeastern-specific adjustments (see `brand.northeastern.edu` editorial style).

**Casing:**
- **Sentence case** for headlines, UI labels, button text, and most titles. ("Apply now" — never "Apply Now.")
- **Title case** only for proper nouns and official program names ("Khoury College of Computer Sciences").
- **ALL CAPS** only on eyebrow labels (11px, letter-spacing 0.12em) above a heading.

**Vibe & tone moves:**
- Lead with the human, follow with the institution. "Mira, BS '26, Khoury College" before "Northeastern students…"
- Numbers are evidence, not decoration. "14 global campuses" works; bare stat blocks of unsourced figures don't.
- No exclamation marks in formal communications. None.
- No emoji on branded surfaces.
- We refer to ourselves as **Northeastern**, not NU or N.E.U., except in athletics or where licensed.

**Examples (drawn from brand.northeastern.edu):**
- ✓ "Our identity system is designed to be flexible, meeting needs across the global university."
- ✓ "By working together, our brand is stronger."
- ✗ "Unlock your potential!! 🎓" — wrong voice, wrong tone, wrong punctuation.

---

## Visual foundations

**Palette.** Three working colors, one accent: NU Red (`#C8102E`, 27% usage target), Black (35%), White (35%), Gold (`#A4804A`, 3% — ceremonial only). Every piece of collateral contains red. Red on red is never permitted. White is the default surface; off-white, cream, or gray require approval.

**Type.** Lato across all hierarchy. Headings H1–H3 are **regular weight 400** (a deliberate brand choice — do not "improve" by bolding). H4 and below are bold 700. Sentence case is the default. Eyebrow labels are the only place ALL CAPS appears (11px, 0.12em tracking).

**Spacing.** 8px base unit, scaling 4 → 8 → 12 → 16 → 24 → 32 → 48 → 64 → 96.

**Backgrounds.** White is the standard. Black is acceptable for high-impact reverse layouts. Photography appears full-bleed with a black-to-transparent legibility scrim when type overlays it. **No gradient backgrounds, no repeating patterns, no glassmorphism, no textures.** No hand-drawn illustrations as decoration.

**Animation.** `0.3s ease` is the system default (`cubic-bezier(0.4, 0, 0.2, 1)`). Hover on links → `color: #C8102E`. Hover on white buttons → background darkens to NU Red. No bounce, no parallax, no scroll-jacking.

**Hover & press states.**
- Link hover: color shifts to NU Red, optional underline.
- Primary button hover: background `#A50C25` (darken 15%). Pressed: `#870A1F` (darken 25%).
- Secondary (outlined) button hover: inverts — black fill, white text.

**Focus states.** Visible, high-contrast, 2px solid — **never removed**.

**Borders.** 1px hairlines in `--border-1` (`#E3E3E3`) for surfaces; 1.5–2px in black for form inputs and buttons. Squared corners are the default — Northeastern is not a rounded-corner brand.

**Shadows.** Used sparingly. No drop shadows on type. Three steps:
- `shadow-1` — 0 1px 0 rgba(0,0,0,.06) — separator
- `shadow-2` — 0 2px 8px rgba(0,0,0,.08) — floating chip / overlay
- `shadow-3` — 0 8px 24px rgba(0,0,0,.12) — modal

**Transparency & blur.** Used only for photographic scrims (linear-gradient transparent → black for type legibility). Not used as a decorative motif. No frosted glass.

**Corner radii.** `0` is the default. Inputs may use `2px`. Tags and pills only when the tag is purely categorical. Cards do **not** have rounded corners — they have squared edges (per Website Experience Standards: "Squared corners: Images should have squared corners for a clean and professional appearance.").

**Card anatomy.** White surface, 1px `#E3E3E3` border (no shadow), squared corners. Internal padding 18–24px. Optional 32px × 3px NU Red rule beneath the title — a recurring brand-signal device that lets non-red cards still "contain red."

**Imagery vibe.** Warm, authentic, active. Students and faculty in real learning contexts. Natural light. Avoid staged stock-photo looks. Photography can be full color, **red duotone** (`#870A1F` shadows → `#C8102E` highlights, for brand-forward applications), or black-and-white (editorial / historical). Gradient overlays exist only for legibility, never as decoration.

**Layout rules.** Single-column body with full-bleed hero is the default. Generous left/right margins (≥ 48px on desktop). Headlines top-aligned and balanced. Sticky red top-of-page accent rule (3–4px) is a recurring device on long-form pages.

---

## Iconography

**System pick: Lucide** (open source, MIT). Northeastern's own kernl-ui pattern library uses a mixed inline-SVG set without a distributed icon font; Lucide is the closest free, well-maintained match in spirit — **minimal line iconography, 1.75 stroke, square caps, 24×24 base grid**.

- Color: `#000000` by default. Never colorize icons with NU Red unless the icon **represents** the brand (e.g. logo favicon, "N" mark).
- Hover state on interactive icons: opacity 1 → 1; the **container** (link / button) drives the hover, not the icon.
- Sizes: 16, 20, 24, 32. Avoid in-between values.
- **No emoji** on branded surfaces.
- **No filled / Material-style** icons in the same surface as line icons. Pick one style and commit.
- **Favicon:** the N monogram in NU Red, per brand.northeastern.edu favicon rule.

Where the codebase already uses bespoke SVG illustrations, keep them — don't substitute Lucide for an existing brand-specific drawing. CDN: `https://unpkg.com/lucide@latest`.

---

## Caveats — read before publishing anything

1. **Logo assets are placeholders.** The official wordmark, N-monogram, and seal files are gated behind a Northeastern login at `brand.northeastern.edu/logos/`. The SVGs in `assets/` use a stylized N and text-set wordmarks to capture the brand feel; they are **not** the official marks and must not ship to external audiences. Download the real files (EPS / PNG / SVG packages) from the Brand Center before any production work.
2. **Typography substitution.** brand.northeastern.edu now lists **Real Head Pro (FF Real)** as the primary digital typeface, with **Lato** as the approved alternative. Real Head Pro is licensed via Adobe Fonts and cannot be embedded freely, so this system uses **Lato** throughout. If you have a Real Head Pro license, swap it into `--font-display` / `--font-sans` in `colors_and_type.css`.
3. **No codebase or Figma was attached** for this build — the system is derived from the DESIGN.md brief plus the public Brand Center, including the kernl-ui pattern library at northeastern.netlify.app. Confirm against any internal Figma library before locking decisions.
4. **Color palette is intentionally minimal.** Resist the urge to add accent hues. The brand depends on red doing the work.

---

## Next steps

- Drop in official logo files from the Brand Center → overwrite `assets/wordmark-*.svg` and `assets/monogram-*.svg`.
- If you have a Real Head Pro license, swap the font stack.
- Submit anything externally-facing to [brand.northeastern.edu/brand-reviews](https://brand.northeastern.edu/brand-reviews/).
