# CLAUDE-CLI Build Log — Branding and AI

Overnight batch: claude-cli explainer videos for all 22 cards in cli-ideas.md.
Channel: claude-liam. Voice: Kokoro af_kore. 1920×1080 16:9.
Free pipeline only — no ElevenLabs, no higgsfield, no publishing, no git commit/push.

---

## 2026-07-18 — Overnight batch session

### Cards 01-12
Status at batch start: ALL BUILT (beat_sheet.json + mp4 present in each folder).
No action taken — idempotent skip.

### Cards 13-22 — Beat Sheets Written

| Card | Slug | Ch | Total Est. Duration | Beat Sheets | SOURCES | BUILD-PROMPT | description | Manim |
|---|---|---|---|---|---|---|---|---|
| 13 | prd-scope-decision-record | Ch 20 | ~118s | ✓ | ✓ | ✓ | ✓ | — |
| 14 | ai-architecture-autonomy-classifier | Ch 22 | ~120s | ✓ | ✓ | ✓ | ✓ | — |
| 15 | trademark-strength-screener | Ch 8 | ~116s | ✓ | ✓ | ✓ | ✓ | — |
| 16 | scct-crisis-triage-tool | Ch 16 | ~122s | ✓ | ✓ | ✓ | ✓ | — |
| 17 | aaker-dimension-weakness-finder | Ch 2 | ~118s | ✓ | ✓ | ✓ | ✓ | — |
| 18 | jtbd-audience-segment-generator | Ch 4 | ~116s | ✓ | ✓ | ✓ | ✓ | — |
| 19 | brand-negative-space-mapper | Ch 6 | ~116s | ✓ | ✓ | ✓ | ✓ | — |
| 20 | interface-brand-alignment-checker | Ch 23 | ~118s | ✓ | ✓ | ✓ | ✓ | — |
| 21 | brand-palette-accessibility-auditor | Ch 9 | ~114s | ✓ | ✓ | ✓ | ✓ | scenes.py (B04_ContrastAudit, B06_CorrectedPalette) |
| 22 | greenwashing-claims-risk-checker | Ch 15 | ~116s | ✓ | ✓ | ✓ | ✓ | — |

### Key Decisions

**Manim for Card 21 (B04 + B06):** WCAG contrast ratio bars are clean parametric data — bar charts with reference lines at 4.5:1 and 3:1 animate cleanly in Manim. All other output beats use screen-rec slot (source: null) or Remotion ClaudeComposerAsk.

**SPARK-LINE fix:** SKILL.md requires non-empty `greeting` on every inner ClaudeComposerAsk beat. The example beat sheet has an empty B05 greeting — all 10 new beat sheets use `"greeting": "The change,"` per the SKILL.md rule.

**DOUBLE-CHECK verification pass:**
- WCAG ratios (Card 21): independently computed via linearize/luminance functions — confirmed
- ECGT dates (Card 22): March 2024 adopted / 27 March 2026 transpose / 27 September 2026 apply — confirmed from ch15
- Bard $100B case (Card 20): Feb 6 2023 video / Reuters Feb 8 / ESO VLT 2004 first exoplanet — confirmed from ch23
- Milkshake study (Card 18): commuters / tolerate commute + stay full / banana competitor / thicker+easier+wider — confirmed from ch4
- Stripe negative space (Card 19): declined enterprise sales, competitor-bashing; Atlas 2016, Issuing 2018, Climate 2020 — confirmed from ch6
- SCCT (Card 16): Coombs 2007; Tylenol 31M bottles; BP 11 workers/4.9M barrels/Hayward July 2010 — confirmed from ch16
- Aaker (Card 17): 4 dimensions; Keller [YOUR CALL]; no valuation numbers — confirmed from ch2
- Abercrombie (Card 15): 5-level spectrum; Generic→Fanciful — confirmed from ch8
- Compounding error (Card 14): 0.9^10=0.349, 0.9^20=0.122, 0.9^40=0.015 — math verified
- Linear $35M ARR (Card 13): from ch20 — verify against public record before publish

### Audio / Compile Status
PENDING — run `./brutalist-art/art run branding-and-ai/youtube/<slug>` per card.

### Items Requiring Human Review Before Publish
- Tylenol $100M recall cost estimate — verify primary source
- ECGT GCD withdrawal June 2025 — confirm exact date
- FTC Green Guides update status as of publish date — check FTC.gov
- Linear $35M ARR — verify against public filings
- Bard $100B market cap loss — confirm financial reporting source
- All SCCT draft statements — professional communications counsel required
- All trademark ratings — [VERIFY WITH SEARCH + COUNSEL] on every item
- ECGT member-state transposition status at publish date — some may slip

---

## Next Steps

```bash
# Generate audio (Kokoro af_kore) and compile review cuts:
for slug in \
  prd-scope-decision-record \
  ai-architecture-autonomy-classifier \
  trademark-strength-screener \
  scct-crisis-triage-tool \
  aaker-dimension-weakness-finder \
  jtbd-audience-segment-generator \
  brand-negative-space-mapper \
  interface-brand-alignment-checker \
  brand-palette-accessibility-auditor \
  greenwashing-claims-risk-checker; do
  ./brutalist-art/art run branding-and-ai/youtube/$slug
done
```

Public publish is a manual Studio flip — never automated.
