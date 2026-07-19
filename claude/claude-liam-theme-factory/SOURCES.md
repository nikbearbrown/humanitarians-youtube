# SOURCES — claude-liam-theme-factory ("Claude, Restrained.")

Source skill: `books/anthropics/skills/skills/theme-factory/` (Anthropic,
github.com/anthropics/skills). Modifier: skill-teardown
(skills/make/ai-explainer/SKILL.md). Audio: Kokoro am_onyx (free, local),
generated 2026-07-18 in the Cowork cloud session; durations are ground truth.

## Verbatim quotes (VERBATIM QUOTE LAW)

| Beat | On-screen/spoken quote | Source line (SKILL.md) |
|---|---|---|
| B03 | "Get explicit confirmation about the chosen theme" | Usage Instructions, step 3 ("Wait for selection: Get explicit confirmation about the chosen theme") |
| B07 | "show it for review and verification" | Create your Own Theme section ("After generating the theme, show it for review and verification.") |
| B08 | "Ensure proper contrast and readability" | Application Process, step 3 |
| B02 | "restaurant presentations, hospitality brands, fall campaigns" | themes/golden-hour.md, Best Used For |

## Theme data (all hexes verbatim from themes/*.md)

- Golden Hour (themes/golden-hour.md): Mustard Yellow #f4a900 · Terracotta
  #c1666b · Warm Beige #d4b896 · Chocolate Brown #4a403a · FreeSans Bold /
  FreeSans.
- Midnight Galaxy (themes/midnight-galaxy.md): Deep Purple #2b1e3e · Cosmic
  Blue #4a4e8f · Lavender #a490c2 · Silver #e6e6fa.
- Ten theme names + one-line descriptors (B04): SKILL.md "Themes Available"
  list, items 1–10, order preserved.

## Computed values (DOUBLE-CHECK LAW — nothing invented)

WCAG 2.x contrast ratios, computed from the verbatim hexes
(relative-luminance formula; script in BUILD-LOG):

| Pair | Ratio | Grade |
|---|---|---|
| Midnight Galaxy: Silver #e6e6fa on Deep Purple #2b1e3e | 12.57:1 | AAA |
| Golden Hour: Chocolate Brown #4a403a on Warm Beige #d4b896 | 5.32:1 | AA |
| Golden Hour: Mustard Yellow #f4a900 on Warm Beige #d4b896 | 1.05:1 | FAIL |
| Midnight Galaxy: Cosmic Blue #4a4e8f on Deep Purple #2b1e3e | 2.05:1 | FAIL (not narrated; reserve) |

Byte counts (ls, 2026-07-18): SKILL.md 3,124 B ("about three kilobytes");
themes/*.md 513–544 B ("around five hundred bytes each"); narrated as
approximations, exact values here.

## Corrections applied (DOUBLE-CHECK LAW)

- SKILL.md's typo "font and color themes themes" and "that has been
  creating" not quoted — paraphrased around, not reproduced.
- "A theme touches colors and fonts and nothing else" (B04) reflects the
  theme files' actual scope (palette + typography only); spacing/layout
  changes are out of scope per the files themselves.

## Self-demo feasibility (SELF-DEMO LAW)

- Ten-skins gallery (B04), theme card (B02), custom theme (B07): fully
  buildable in the free pipeline from the hex/font data above — no paid
  APIs. No PIPELINE slates required at authoring time.
- theme-showcase.pdf is REBUILT natively (Figure 4), never shown as an
  image — caption "Redrawn from theme-showcase.pdf", once, small.
