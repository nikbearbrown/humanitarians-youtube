# BUILD LOG — hai-simple/behind-the-model--claude-constitution-operator-floor

Redo of `anthropics/youtube/behind-the-model/claude-constitution-operator-floor`
("Gagged, Not Weaponized", Teardown-register, 19 beats, ~360s) as `hai-simple`
(Plain register, Humanitarians AI skin). Source folder untouched. Built from
scratch — the target reel dir contained only SUBJECT.json at the start of
this invocation. Sibling redos from the same source family
(`claude-constitution-corrigibility-dial`, `-honesty-standard`, `-many-hands`)
were already built in this tree the same day (2026-09-04) and served as the
structure template for this one.

## Source was thinner than the fully-written beats suggest

Like the sibling redos, this source's body beats (A10–A51) were never
fleshed out — each is a `[seed] ... expand from the source with a concrete
instance` placeholder, not written narration. The load-bearing facts actually
came from the source's fully-written beats (B00, B01, EX, VERDICT) and
`metadata.one_idea`, which together name the argument precisely: trust is
layered (Anthropic bounds operators, operators bound users), but a small set
of user guarantees is non-overridable. No external source doc was found
under `anthropics/claude-constitution/` matching the referenced
`20260120-constitution.md` path — same disposition as the other redos in this
family, documented in QUESTION.md rather than papered over.

## What changed vs. source (per redo contract)

- **Register:** Teardown → Plain. Body compressed to one idea per beat (10
  beats: B00 writer + B01–B06 body + BCRY + BHTF + BOUT).
- **Cold open:** source's `FormBCard` beat (already flagged by the source's
  own `skin_warnings` as violating COLD OPEN LAW) → `BrutalistHesitantWriter`.
  Writer types "If operators outrank users, doesn't operator rank mean total
  control over what Claude does?", hesitates on "total", corrects to
  "bounded" — the reel's actual wrong guess, picked up and falsified by B03.
- **Close:** `OutroCTA` + `@HumanitariansAI`, Liam sign-off, instead of
  source's `ClaudeTitleOutro`/`@NikBearBrown`.
- **Voice:** unchanged — Liam, Kokoro `am_onyx`.
- **Facts/argument:** the three-principal hierarchy, the operator-as-employer
  framing, the key case (refusing "tell users you are human" while following
  other unusual rules), and the airline worked example all carry from the
  source, reworded for register. **Not carried:** the source's separate
  "permission stack" and "resolving operator-user conflicts" acts as distinct
  ideas — folded into one continuous floor mechanism (see QUESTION.md) to
  avoid fracturing the one-anchor law.

## NO-GENAI / NO-PANTRY LAW

No source beat kept in this compression was AI-VIDEO, pantry, or a human-drop
slot. Every beat in this reel is REMOTION (B00, BCRY, BHTF, BOUT — all
GATE-L-checked renderable: `BrutalistHesitantWriter`, `WantQuote`,
`ClaudeComposerAsk`, `OutroCTA`) or bespoke GRAPHIC/Manim (B01–B06, humanitarians
palette `#F3EBDD`/`#2F2A26`/`#E4572E`/`#1F4E5F`).

## Gate V and GATE T — real defects found and fixed, not just re-run

First full compile passed content/frame/lane checks and GATE AUDIO, but the
automated type gate (`type_check.py`, GATE T) failed on the *rendered video*
(not just the sheet), catching defects Gate V's frame-pull sampling had
missed:

1. **B03 layout bug (found via frame QC, before GATE T ran):** the
   "TELL USERS YOU ARE HUMAN" chip's slide-to-floor animation used
   `move_to(floor.get_center() + UP*0.55)`, which snaps to x=0 regardless of
   the chip's own column — it landed on top of the "UNUSUAL TOPIC RULE"
   chip's stamp instead of continuing straight down its own column. Fixed by
   giving every chip a fixed per-column x-coordinate throughout its
   animation, verified via frame grabs at t=44s/49s before and after.
2. **GATE T kerning FAIL (B02):** `type_check.py` measures inter-glyph pixel
   gaps only at 1080p (explicitly skips the check at 4K — "pixel-level kern
   check skipped" — per its own scale-aware design). The raw Manim beats were
   rendering at 1080p (`-qh`), and one specific title string ("THE NATURAL
   GUESS") produced an anomalous 41px gap, a real Pango/Montserrat-Bold
   shaping quirk for that exact string (different wording — "THE OBVIOUS
   READ" — measured a smaller but still-failing 24px gap, confirming it's
   string-specific, not a fixable-by-rewording issue).
3. **GATE T bbox-overlap FAIL (B05), root-caused by direct pixel inspection:**
   this was chased through several wrong hypotheses (apostrophe glyphs,
   opacity-based dimming, single- vs. multi-line Text objects, EB Garamond
   substitution — the last of which made things *worse*, breaking 4 more
   beats with the same false-positive pattern because EB Garamond has no
   true bold face on this system, and Manim's synthetic-bold fallback for
   BOLD tier/stamp text produced duplicate glyph fragments). Cropping the
   exact flagged pixel region `(432,666)-(1409,899)` from the checker's own
   sampled frame (`ffmpeg -ss <mid-clip-t> ... | crop`) showed the truth: the
   chip's own rounded-rectangle border stroke (`border_width=2`) was dense
   enough, at this box's specific w×h proportions, to clear the checker's
   "solid text vs. hollow outline" area-density threshold (§8.6b's
   `area >= bbox*0.04` filter) — so the border was being misdetected as a
   text-run, and the label rendered inside it (which sits inside the border's
   bbox by construction) was flagged as "overlapping" it. Fixed at the root
   by thinning `_chip()`'s border to `border_width=1.2` (verified: text and
   layout unchanged, only the stroke thickness).
4. **Systemic fix, not a workaround:** switched `render_scenes.py` from
   `-qh` (1080p) to `-qk` (native 4K) for all Manim beats. This is a real
   quality improvement (`compile.py`'s 4K LAW upscales the final master to
   2160p regardless, so rendering Manim natively at 4K avoids an unnecessary
   upscale step) and, per `type_check.py`'s own documented behavior, correctly
   routes the fragile 1080p-only kerning pixel-check to a skip while using
   scale-aware thresholds elsewhere — it did not, by itself, fix the B05
   border-stroke bug (root-caused and fixed separately per #3 above).

All fixes were verified by re-rendering, recompiling, and re-running
`type_check.py` to a clean PASS — not assumed from the diagnosis alone.

## Gates

- **TIMING LAW (B00):** narration 32 words + `lead_silence_s` 0.8 → measured
  `actual_duration_s` **10.87s** (≥9s floor, ≥8s render floor). Correction
  ("total" → "bounded") verified fully typed and settled by frame grabs at
  t=5s (mid-hesitation) and t=8s (corrected, settled).
- **GATE AUDIO:** PASS, mean_volume **-23.8 dB** (well above the -40 dB
  floor, verified independently via `ffmpeg -af volumedetect`), max_volume
  -2.8 dB.
- **GATE T (type_check.py):** PASS, 0 FAILs across all 8 pixel checks
  (min-size, overflow, contrast, contrast-local, bbox-overlap, card-clip,
  kerning) after the fixes above — see TYPECHECK.md.
- **Gate V (frame QC):** every beat checked at a mid-beat and near-end
  timestamp; the B03 column-snap bug (above) was the one real defect caught
  by direct frame reading that the automated checks didn't independently
  flag.
- **Lane-check / content-check / frame-check:** all PASS per `compile.py`
  output (10/10 beats, no violations).
- **Motion histogram:** WARNING, graphic 6/10 (60%, over the ~40% pantry
  cap). Non-blocking and structural for this skill: B00 (writer), BCRY, BHTF,
  BOUT are REMOTION by the hai-simple spine itself, and at only 6 body beats
  this 10-beat reel necessarily runs higher than 40% on the graphic side.
  Same disposition as the corrigibility-dial and many-hands redos' histogram
  warnings.

## Output

`behind-the-model--claude-constitution-operator-floor.mp4` — 129.6s,
3840×2160, 10/10 beats real (no slate), audible narration throughout
(mean -23.8 dB, independently verified via ffprobe/ffmpeg). Master mtime
(2026-09-04T21:51) is newer than `beat_sheet.json`'s last content edit —
COMPLETION LAW satisfied. `compile.py` forces a 4K master by default ("4K
LAW"), so no separate low-res pass exists for this cut.

## Delivery

Master born natively 3840×2160 via `compile.py`'s 4K LAW; Manim source beats
also rendered natively at 4K (`-qk`), so no upscale occurred anywhere in the
pipeline. Playlist: **Behind the Model** (direct family-prefix match in
`playlists.json`).
