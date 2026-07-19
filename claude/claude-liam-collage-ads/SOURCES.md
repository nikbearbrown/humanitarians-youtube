# SOURCES — claude-liam-collage-ads
# "Claude, Collaged." | collage-ads skill teardown

## Verbatim quotes (3 required by VERBATIM QUOTE LAW)

### Quote 1 — B05 (Mechanism · Act 1)
> "The driving question is: 'If I had to regenerate this exact frame from scratch on nano-banana-2, what would I need to specify?'"
- Source: skills/make/collage-ads/SKILL.md — Phase A mindset
- Role: the question that drives over-analysis in Phase A; ensures every attribute is independently swappable for variations; stated once, in B05

### Quote 2 — B06 (Mechanism · Act 2)
> "Labels are burned in at generation, never via arcads_add_text_overlay."
- Source: skills/make/collage-ads/SKILL.md — Notes and rules
- Role: the hard rule about label treatment; burning labels into nano-banana-2 preserves paper-craft texture; stated once, in B06

### Quote 3 — B07 (Mechanism · Act 3)
> "Consistency across scenes is what makes it read as a brand rather than one-offs."
- Source: skills/make/collage-ads/SKILL.md — Phase B4
- Role: rationale for the lock-look-vary-idea scaling law and one-model-per-set rule; stated once, in B07

## Self-demo source
- Phase: Phase A (decode/analyze) — genuinely free, no Arcads MCP calls, no nano-banana-2, no Seedance
- Reference: hypothetical coffee brand ad — cobalt-blue flat field (#1B4FD8), halftone paper coffee cup (white+black, 40 lpi), halftone sun (yellow-orange), burned label "MORNING BREW"
- Output: collage JSON spec with all fields: medium, craft_style, color_field (hex+evenness+grain), 2 elements (cup+sun with halftone/cut/shadow/placement), composition, idea, label (burned in at generation)
- Not faked: JSON spec follows the SKILL.md schema exactly; label treatment follows the "never arcads_add_text_overlay" rule; all fields are independently editable per the Phase A centerpiece design
