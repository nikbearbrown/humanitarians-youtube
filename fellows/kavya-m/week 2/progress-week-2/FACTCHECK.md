# FACTCHECK — Brutalist Progress — Week 2 (Kavya)

Every claim mapped to its evidence, with an honest status on each.

## What kind of reel this is

A real, independently verifiable recap — a direct sequel to
`kavya-brutalist-week1-progress`. Every claim traces to an actual file/line
fixed this session.

## B00 — Cold open

- **"1 new reel built, both formats, same day"** — real; refers to
  `youtube/claude-liam-semantic-layers-ai-context/`.
- **"1 new bug found — in a file week 1 already touched"** — real, see B03.
- **"0 of the old six bugs came back"** — real; the week-1 fixes were not
  re-broken by this week's work.

## B01 — BLUF

- No new factual claim beyond B00/B02.

## B02 — What happened

- **"Reused the fixed pipeline — zero of the six week-1 bugs came back"** —
  real, confirmed by this week's clean builds not re-triggering any of the
  six week-1 defects.
- **"Built a new reel — Semantic Layers Become AI Context, 8 beats"** —
  real, see that reel's own folder.
- **"Found one new bug — a layout overlap in code week 1 already touched"**
  — real, see B03.
- **"Shipped same day, 16:9 and 9:16, zero blocking defects"** — real.

## B03 — The bug

- **`SkillTeardownPipeline916` layout overlap, caused by week 1's own GATE T
  font-size fix making two text lines taller** — real; traced to
  `colBottom=0.80` / `footer-top=0.825` in that component's source.

## B04 — The fix

- **"Tried: shorten the footer text (not the real cause)"** — real; this was
  attempted first and did not resolve the overlap.
- **"Actual fix: colBottom 0.80 → 0.76, footer 0.825 → 0.87"** — real, the
  layout-math fix that actually resolved it.
- **"Verified: real frame extracted and checked, not just the preview"** —
  real; confirmed by extracting an actual frame from the compiled mp4,
  since the QC contact-sheet thumbnail was found to misrepresent portrait
  aspect ratio.

## B05 — Verdict

- Restates B02/B03/B04's claims; no new facts introduced.

## B06 — Handoff

- No factual claim; a prompt for the viewer to run on their own fix.

## B07 — Outro

- No factual claim; "Built by — Kavya Mehta" credit card.

## Corrections & caveats applied during this build

- This reel reuses the real, already-fixed-at-the-root content from
  `youtube/brutalist/claude-liam-brutalist-week2-progress/`, built earlier
  this session — the bug, its false-lead fix attempt, and its actual fix are
  identical and real; only the on-screen persona, greeting, folder chip,
  terminal host field, and outro were changed to credit Kavya Mehta by name
  and remove claude-liam / Nik Bear Brown branding.
- GATE T flagged B02 (`ClaudeScienceLayerStack`) for the same "8px text run"
  advisory already documented for the equivalent beat in
  `kavya-brutalist-week1-progress` (B03, same component). A frame was
  extracted from the compiled `media/B02.mp4` and visually inspected — all
  four card titles and sub-labels are fully legible. Assessed as the same
  false positive (the narrow colored accent bar on each card being
  misclassified as a text run), not a real legibility defect. See
  BUILD-LOG.md.
- GATE T also flagged an advisory-only §8.10 redundancy finding on B05
  (narration closely recites the on-screen verdict card, similarity 0.89).
  Advisory, no exit effect — the `ClaudeVerdictArtifact` verdict pattern
  intentionally has the narration summarize the same points shown on
  screen; not treated as a defect.
