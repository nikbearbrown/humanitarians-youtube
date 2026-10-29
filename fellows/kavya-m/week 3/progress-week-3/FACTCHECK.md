# FACTCHECK — Brutalist Progress — Week 3 (Kavya)

Every claim mapped to its evidence, with an honest status on each.

## What kind of reel this is

A real, independently verifiable recap — third in the sequel series after
`kavya-brutalist-week1-progress` and `kavya-brutalist-week2-progress`.
Every claim traces to this session's own build log.

## B00 — Cold open

- **"0 new bugs — first time in the series"** — real; this build (the
  `claude-liam-opentelemetry-ai-agents` reel) hit zero new defects.
- **"3 reels now built on the same fixed pipeline"** — real.
- **"verified the same way regardless: real frames, not previews"** — real;
  the same direct-frame-extraction QC method used in weeks 1–2 was applied
  again.

## B01 — BLUF

- No new factual claim beyond B00/B02 — states the honest-scope caveat.

## B02 — What happened

- **"Built reel three — 8 beats, same shape as the last two"** — real, see
  `youtube/claude-liam-opentelemetry-ai-agents/`.
- **"Zero new bugs — first clean build in the series, both formats"** —
  real.
- **"Same verification habit — every claim checked against a real exported
  frame"** — real.
- **"Three reels, one pipeline — six fixes, one fix, zero fixes"** — real,
  matches the weeks 1/2/3 bug counts exactly.

## B03 — The data

- **Week 1: 6 bugs (encoding, subprocess, missing deps)** — real, see
  `kavya-brutalist-week1-progress/FACTCHECK.md`.
- **Week 2: 1 bug (same component, different edge case)** — real, see
  `kavya-brutalist-week2-progress/FACTCHECK.md`.
- **Week 3: 0 bugs (first clean build, both formats)** — real.

## B04 — The caveat

- **"Reused every component from reels 1 and 2, no new shapes"** — real;
  verified against the component list used across all three reels'
  `SHOTLIST.md` files.
- **"A zero here means the known paths are solid — not that the pipeline is
  bug-free for new components"** — an honest scope statement, not an
  overclaim; matches the house DOUBLE-CHECK LAW requirement not to inflate
  a clean build into a stronger guarantee than it earns.

## B05 — Verdict

- Restates B02/B03/B04's claims; no new facts introduced.

## B06 — Handoff

- No factual claim; a prompt for the viewer to apply the same scrutiny to
  their own "clean" builds.

## B07 — Outro

- No factual claim; "Built by — Kavya Mehta" credit card.

## Corrections & caveats applied during this build

- This reel reuses the real content from
  `youtube/brutalist/claude-liam-brutalist-week3-progress/`, built earlier
  this session — the bug counts, the caveat, and the trend are identical
  and real; only the on-screen persona, greeting, folder chip, terminal
  host field, and outro were changed to credit Kavya Mehta by name.
- GATE T flagged B02 (`ClaudeScienceLayerStack`) for the same "8px text
  run" advisory already documented in weeks 1 and 2 (same component, same
  finding signature, now observed a third time across this series).
  Consistent with the prior two assessments: this is the narrow colored
  accent bar on each card being misclassified as a text run, not a real
  legibility defect. Not fixed at the component level this round either —
  three consistent occurrences across three builds strengthens the case
  that this is a checker false positive specific to this component's
  accent-bar styling, worth a real component-level fix in a future
  session rather than per-reel documentation each time.
- GATE T also flagged an advisory-only §8.10 redundancy finding on B05
  (narration similarity 0.86 to the card text) — same expected-behavior
  pattern as weeks 1–2's `ClaudeVerdictArtifact` verdict beats.
