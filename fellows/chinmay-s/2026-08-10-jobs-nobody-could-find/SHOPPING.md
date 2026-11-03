# SHOPPING.md — Gate D2 (duration-locked, tier-tagged)

Written AFTER audio lock (durations below are the measured mp3 lengths, not
estimates). One entry per missing pantry still. Each motion asset asks for
MORE seconds than its beat so conform TRIMS (lossless) rather than STRETCHES.
Until these are filled, the 5 vox beats render as slates in the previz — which
is exactly what Gate D1 expects.

| Beat | Lane | Beat dur | Ask for | Tier | What to source | Motion |
|---|---|---|---|---|---|---|
| B02 | vox | 12.50s | ≥ 15s | 1 (illustrative) | A cold, near-empty database / a single laptop in the dark — "correct code no user ever felt." Generic, no real referent. | kenburns, focus centre |
| B10 | vox | 13.67s | ≥ 16s | 1 (illustrative) | A search bar / "Google for Jobs" style results surface with the site absent from it — invisibility. Generic mock, not a real screenshot. | kenburns |
| B18 | vox | 12.89s | ≥ 15s | 1 (illustrative) | A Search-Console-style coverage dashboard: lines climbing, a few amber warnings beside them. Generic dashboard, no real account data. | kenburns |
| B21 | vox | 13.21s | ≥ 16s | 1 (illustrative) | A tidy documentation / handoff page — "the systems outlive the author." AI-generate; label as `source: ai`. | kenburns |
| B22 | vox | 14.02s | ≥ 16s | 1 (illustrative) | An empty calendar week / a blocked door — the stalled transition week, reported straight. AI-generate; label as `source: ai`. | hold |

## Notes
- All five are **Tier 1** (generic/illustrative, no real referent) → no rights
  escalation; AI-generate or stock. None depict a real named person or place.
- Drop each into `pantry/<BID>.png`, run the pantry intake, set `shot.focus`,
  add the `source: ai` disclosure sidecar for B21/B22, then recompile — only
  the changed slots re-render.
- "Ship with slates" override is fine for this demo: the previz is watchable as
  is and nothing here publishes.
