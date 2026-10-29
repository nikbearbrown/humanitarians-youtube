# CHECKS-REPORT — Ontologies for Observability at Scale (Kavya)

Written before the first slate compiled, per the PROOF GATE in
`skills/make/ai-explainer/SKILL.md`.

## Beat classification

8 SHOW / 0 justified-HOLD / 0 PUNT-flagged

## Teaching-arc checklist

| Item | Status | Where |
|---|---|---|
| FRAMEWORK | ✓ | B02 — entity types, relationships, stable identifiers, shared vocabulary |
| WORKED EXAMPLE | ✓ | B03/B04 — the naming-collision example, unresolved then resolved |
| FALSIFIABILITY | ✓ | B05 verdict: "an ontology can't reason about a span that was never emitted" |
| SCAFFOLDED TASK | ✓ | B06 handoff — a prompt to map one's own team's naming variants |
| BOOKENDS | ✓ | B00 cold open → B05 verdict → B06 handoff → B07 outro |
| NO-SOURCE-NO-VERDICT | ✓ | The worked example is explicitly labeled illustrative in FACTCHECK.md; the framework claim is general industry knowledge, not a fabricated citation |

## Downstream check status

- **GATE T (type-lock):** PASS, 8/8, first run — no false positives, the
  `ClaudeScienceLayerStack` fix from earlier this session held.
- **GATE V (visual QC):** spot-checked via direct frame extraction — B00
  and B07 inspected in landscape at true native 4K (3840×2160). Both
  clean, legible, correctly branded.
- **Resolution verification:** both masters confirmed via `ffprobe` —
  landscape 3840×2160, vertical 2160×3840 — after this reel was
  specifically recompiled with explicit `--height 2160` / `--height 3840`
  flags (see BUILD-LOG.md for why this was necessary).
