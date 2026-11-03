# BUILD-LOG — financial-services--claude-liam-fx-carry-trade

**2026-09-01** — hai-simple, mode=redo. Source:
`anthropics/financial-services/youtube/claude-liam-fx-carry-trade` (Teardown
register, 7 beats). Kept the source's question, facts (fx-carry-trade skill:
spot rates, forward points, interest rate differentials, volatility surface
analysis, historical price trends; Claude reads `SKILL.md`, runs its Steps
section linearly; same input → same output; outside-scope inputs uncovered),
and beat count. All source body beats (B01–BVDT) were already REMOTION —
none were AI-VIDEO/pantry — so no NO-GENAI/NO-PANTRY replacement was needed;
only narration was re-registered to Plain (verdict/judgment language removed
from B03 and the old BVDT→BCRY beat) and the on-screen "Verdict" pill /
"DESIGN TELL" eyebrow were dropped from `SkillTeardownMechanism`.

**Open/close deltas (per hai-simple SKILL.md):**
- B00: source's `ClaudeComposerAsk` → `BrutalistHesitantWriter`. Naive framing
  "Is Claude calculating?" corrected in place to "Is Claude following a
  skill?", humanitarians palette (`bg #F3EBDD` / `ink #2F2A26` / `accent
  #E4572E`). Measured B00 audio: 11.75s + 0.8s lead silence ≈ 12.55s — clears
  the ≥9s WRITER LAW window; frame-checked the correction lands on screen.
- Outro: **did not** use `ClaudeTitleOutro` (source's BOUT pattern) — its own
  header comment hardcodes `handle = '@NikBearBrown'` and states "Other
  channels (HAI, Medhavy, Musinique) use their own outro components — never
  this one" (OUTRO-LOCK.md). Used `OutroSeries` + `OutroCTA` instead
  (BOUT/BOUTB), per hai-simple's doctrine and `skills/make/hai/SKILL.md`.

**Known gap, logged not fixed:** `OutroSeries`/`OutroCTA` import
`tokens/vox.ts`, whose house default is `teardown` (white/near-black/red) —
not `tokens/humanitarians.ts` — and neither component exposes a `bg`/`ink`/
`accent` override prop. So BOUT/BOUTB render in white/near-black/red, not the
humanitarians cream/teal/crimson the skill's palette table calls for. This is
a shared-component wiring gap (no per-reel fix available), not a build
blocker. Also: no `AUTHOR.MD :: Humanitarians AI` section exists anywhere on
this machine (it lives on Bear's machine per `std_retrofit.py`'s
`BOOKS_BASE`), so `OutroCTA`'s CTA line was authored directly rather than
pulled from that source.

**Bug caught by frame QC (fixed before delivery):** `BHTF`'s
`ClaudeComposerAsk` beat omitted `folderLabel`, which silently fell back to
the Root.tsx Composition-level default `'@NikBearBrown'` — wrong attribution
on a Humanitarians AI reel. Confirmed by pulling a frame at the beat's
midpoint. Fixed by setting `folderLabel: "@HumanitariansAI"` explicitly,
re-rendered BHTF only, recompiled, re-verified the frame.

**Gates:**
- GATE T (type_check.py): one round of fixes — BOUT eyebrow was too long for
  its box ("CLAUDE BASICS · HUMANITARIANS AI" → "CLAUDE BASICS"), and B03's
  `SkillTeardownMechanism.body` exceeded the 12-word pull-quote budget
  (trimmed to the 9-word input list). PASS after fixes.
- Audio: generated via `generate_audio_kokoro.py`, Kokoro `am_onyx`, 8/8
  beats, $0.00.
- Compile: `compile.py` (no `--review`) forced a 4K (3840×2160) master
  directly per the 4K LAW — `financial-services--claude-liam-fx-carry-trade.mp4`,
  88.06s. `GATE AUDIO: PASS mean_volume -24.0 dB` (well above the -40dB
  floor). Non-blocking WARNING: 100% of beats are REMOTION (over the ~40%
  motion-histogram cap) — expected for a redo that keeps the source's
  all-REMOTION body; not a defect to fix here.
- Gate V: pulled frames every 6s across the full 88s master + one targeted
  BHTF re-check frame. All legible, correct safe-inset, no overlap, correct
  handle after the folderLabel fix.
- Verified: `financial-services--claude-liam-fx-carry-trade.mp4` is newer
  than `beat_sheet.json`, is 3840×2160, 88.06s, mean_volume -24.0dB. COMPLETE.

**Delivery:** master is already native 4K from the standard compile (no
separate low-res pass was ever produced), so the 4K deliverable is a direct
copy of the master, not a second render.
