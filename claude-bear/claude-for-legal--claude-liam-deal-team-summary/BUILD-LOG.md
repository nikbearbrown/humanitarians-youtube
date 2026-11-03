# BUILD-LOG — claude-for-legal--claude-liam-deal-team-summary

## 2026-08-29 — hai-simple redo, built end to end

**Mode:** redo, per SUBJECT.json (`source_sheet`:
`anthropics/claude-for-legal/youtube/claude-liam-deal-team-summary/beat_sheet.json`).

**Source defect found before scripting:** the source `beat_sheet.json` has a batch-
templating bug — several narration fields contain a literal, unfilled `>` where the
task-specific fact should be (`"Claude's job: >."`, `"The SKILL.md is the spec — >."`,
`"Paste this into Claude: 'I want to >.'"`). Confirmed this is systemic across the whole
`claude-for-legal` batch (checked a sibling, `claude-liam-nda-review/beat_sheet.json` —
same `>` gaps in the same fields). The `source_skill` path
(`/Users/bear/Documents/CoWork/bear-textbooks/books/anthropics/claude-for-legal/
corporate-legal/skills/deal-team-summary/SKILL.md`) is on Bear's other machine and does
not exist here; `PEDAGOGY.md` in the source dir is a one-line stub with no content; there
is no source `SCRIPT.md`.

**Call made (logged per COMPLETION LAW):** kept every fact the source sheet actually had
(non-placeholder) — a skill is a folder Claude reads before it acts (source B01), it
contains one file, SKILL.md, plain language (source B01), steps run in the order the file
lists them, linear, no branching unless the file says so (source B02), and the
reliability property is repeatable structure from a fixed spec, not better judgment
(source BVDT, minus its `>` gap). The one task-specific fact this reel needed — what
"Claude's job" is for *this* skill — was inferred directly and only from the skill's own
name, `deal-team-summary`: a structured status update (parties, key terms, status, open
issues, next steps) for a deal team, which is the plain industry-standard meaning of that
phrase in corporate/M&A practice. No claim is made about the real SKILL.md's actual
fields, prompts, or output format — the reel stays at the level the name safely supports.
Full reasoning in `SCRIPT.md`'s "Source-fidelity note."

**What changed from source (per hai-simple SKILL.md):**
- B00 replaced: was `ClaudeComposerAsk` (Teardown host line); now `BrutalistHesitantWriter`
  — writer types "Claude writes a deal / team summary by / magic?", corrects "magic" →
  "instructions" on screen (the newcomer's actual wrong guess: that Claude does this by
  built-in knowledge, not by reading a file — directly ties to B01's real anatomy fact).
  Narration 30 words + `lead_silence_s: 0.8`; measured `media/B00.mp4` = 9.47s (≥8s per
  TIMING LAW). Verified on frame-pulls at 0.5s spacing: "magic" appears in terracotta at
  t≈5.5s, held, backspaced, and replaced with "instructions" by t≈6.5s — well before the
  9.47s end. (A first pass at 6s-spaced QC frames missed the ~1s correction window
  entirely and had to be re-checked at finer spacing — logging this because it's an easy
  false negative for future QC passes on this component.)
- Body compressed onto the hai-simple spine (stakes → wrong guess → break it → mechanism
  ×2 → anchor planted → anchor payoff → both directions ×2 → carry-out) as 9 GRAPHIC
  (`FormBCard`) beats, S01–S09, each ≤34 words.
- The two mechanism beats (S04 anatomy, S05 pipeline) are the source's real B01/B02 facts,
  re-registered Teardown → Plain (no register change was actually needed — the source
  narration for these two beats carried no verdict/judgment language to begin with).
- S03 (break it — same deal, twice, no skill, two different answers) and S08/S09 (both
  directions) are new content not literally in the source, honestly derived from the
  source's own established claim (repeatable structure from a fixed spec) rather than
  fabricated — the falsifying case and both failure directions are the logical inverse/
  boundary of that one claim, not new facts about the specific skill.
- The anchor (S06 planted → S07 paid off) is an explicitly labeled illustrative example
  (Aster Corp / Vale Robotics — fictional company names), not a claim about a real deal.
- Carry-out (`WantQuote`): "A skill doesn't make Claude better at judgment. It makes
  Claude follow the same steps, in the same order, every single time." — compresses the
  source's own BVDT claim (minus its `>` gap), not new material.
- Your Turn (`ClaudeComposerAsk`) is a real, runnable Claude prompt built around the same
  concept (ask Claude to state its structure before filling it in, then re-run and compare)
  — doesn't require the viewer to have the actual `deal-team-summary` skill installed.
- Outro swapped `ClaudeTitleOutro` → `OutroSeries` + `OutroCTA` (Humanitarians AI skin per
  `skills/make/hai`), eyebrow "CLAUDE BASICS" (constant series brand per hai-simple
  SKILL.md), closing narration "…Liam, in for Bear."
- Playlist: `claude-for-legal` has no entry in `loop/playlists.json`'s family map. **Correction
  during Phase 4** — initially resolved via `_default` → "Claude Across the Curriculum" and
  shipped that in the first pass of the description; caught before final delivery by
  checking `HAILOOP-LOG.md` precedent, which shows every other `claude-for-legal` sibling
  resolving via the **`hai-simple` skill-key fallback** (`playlists.json` maps
  `"hai-simple": "Claude Basics"` directly — a real entry, not a guess) rather than
  `_default`. Corrected the `.md` description's `Playlist:` line to "Claude Basics" and
  re-ran `deliver.py --push` to re-stage/re-commit with the fix. `metadata.playlist` inside
  `beat_sheet.json` still reads the stale "Claude Across the Curriculum" — left untouched
  per COMPLETION LAW (no post-compile sheet edits; the field doesn't affect the rendered
  cut, only the description generation step, which now carries the correct value
  independently).

**Gate L:** `./art scenes --check` confirmed `BrutalistHesitantWriter`, `FormBCard`,
`WantQuote`, `ClaudeComposerAsk`, `OutroSeries`, `OutroCTA` all RENDERABLE before slating —
no new component needed. Pulled `BrutalistHesitantWriter`'s actual zod schema from source
(`triggerWords`/`replacementWords` are comma-separated strings, not arrays) rather than
guessing from the SKILL.md prose description.

**Build:** `generate_audio_kokoro.py` (14 beats, am_onyx, $0.00) → `remotion_scenes.py`
(14/14 rendered at 3840×2160, ran to completion in the background after exceeding the
120s foreground shell timeout — polled its output file to a real exit code 0 before
proceeding, never treated the harness's auto-backgrounding as a stopping point) →
`compile.py` (4K master forced, 14/14 real, 140.7s).

**GATE T:** one real §8.9 truncation FAIL on first pass (`S02/items[1].label` too long) —
shortened to a 5-word label, re-ran, GATE T → PASS, 0 FAILs. §8.10 redundancy advisories on
5 of 9 FormBCard beats (narration recites the card) are non-blocking and match the
accepted pattern from this series' prior builds (FormBCard is a discuss-and-show pattern
by design). Motion-histogram WARNING (graphic 9/14 = 64%, over the ~40% pantry cap) is
also non-blocking and matches the same accepted precedent.

**Gate V:** frame-pulled every 6s across the full 140.7s master (23 frames) — all 14 beats
legible, correctly inset, no text overlap; targeted B00 pulls at 0.5s spacing confirmed
the correction is visible mid-beat, not just at the end.

**Audio presence:** `ffmpeg -af volumedetect` → mean_volume −23.9 dB, max_volume −2.9 dB
(well above the −40 dB floor). Master mtime (19:33:26) newer than `beat_sheet.json` mtime
(19:30:57).

**Result:** `claude-for-legal--claude-liam-deal-team-summary.mp4` — 140.7s, 3840×2160,
14/14 real beats, GATE T PASS, Gate V PASS, audio PASS. Review cut DONE.

**Phase 4 — delivery:** the review-cut master was already born 4K (3840×2160,
`compile.py` forces 2160p, no `--review` markers), so it was copied to
`claude-for-legal--claude-liam-deal-team-summary-4k.mp4` rather than re-rendered. Wrote
`claude-for-legal--claude-liam-deal-team-summary.md` (YouTube description: hook,
timestamped chapters from measured beat offsets, Your Turn prompt, AI-disclosure line,
code link, `Playlist: Claude Across the Curriculum` resolved via `loop/playlists.json`'s
`_default` fallback — no `claude-for-legal` entry exists in the family map). Ran
`deliver.py --push`: staged `DELIVERY/claude-for-legal--claude-liam-deal-team-summary/`
(4K + description) and committed the text artifacts to
`humanitarians-youtube/claude-bear/claude-for-legal--claude-liam-deal-team-summary/`
(commit `c3173de1`, pushed clean). DELIVERED.
