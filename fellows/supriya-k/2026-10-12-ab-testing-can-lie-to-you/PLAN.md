# PLAN — ab-testing-can-lie-to-you (cli-explainer)

**Status: APPROVED 2026-10-18.** Voice: `af_bella` (Bella), persona none, narrator identity
"Supriya" — same setup as correlation-is-not-causation.

## Decisions (approved by Supriya, 2026-10-18)

1. **Case:** the MSN carousel SRM — Fabijan et al., *KDD 2019*, doi:10.1145/3292500.3330722, §1 and
   §5.3. Carousel went from 12 to 16 cards. The test showed a significant drop. The SRM warning
   fired because the bot filter removed the most engaged treatment users. Once that was fixed, the
   result flipped and the feature shipped. Peeking anchor: Johari, Pekelis & Walsh, arXiv
   1512.04922. The paper gives no carousel numbers, so the code beats are a labeled simulation of
   the mechanism.
2. **Code language: Python** (stdlib, fixed seeds) — `py/carousel_v1.py`, `py/carousel_v2.py`,
   `py/peeking.py`, `py/abtest.py`; outputs in `py/*.out`.
3. **Peeking = one beat (B08)**, not a full cycle.
4. **Full-length 9:16.** The 16:9 stays under ~175s. If measured audio exceeds ~170s, re-tighten.
5. **Bitrate:** `compile.py --vbitrate`, then ffprobe both masters. If low, **flag for Supriya**.
   No padding.
6. **Final filenames:** `2026-10-12-ab-testing-can-lie-to-you.mp4` (3840×2160) and
   `2026-10-12-ab-testing-can-lie-to-you-vertical.mp4` (2160×3840).

## Beat arc

| Beat | Role | Renders via |
|---|---|---|
| B00 | INTRO — exact "Hi, I am Supriya and this video is about…" | `ClaudeComposerAsk` |
| B01 | PROBLEM — carousel 12→16, significant drop | Manim |
| B02 | CLI — simulate the mechanism | `ClaudeComposerAsk` |
| B03 | CODE — `carousel_v1.py` | `ClaudeCodeBeat` (`handle`) |
| B04 | OUTPUT — 3.89 vs 3.20, "don't ship" | Manim |
| B05 | CLI — revision: check the split, fix the filter | `ClaudeComposerAsk` |
| B06 | CODE — `carousel_v2.py` + `srm_check` | `ClaudeCodeBeat` (`handle`) |
| B07 | OUTPUT — SRM fires; 3.89 vs 4.65, the flip | Manim |
| B08 | SECOND LIE — peeking: 3.5% → 24.6% vs once 3.8% | Manim |
| B09 | SUMMARY — MSN resolution, ~6%, three checks | Manim |
| B10 | NEXT STEPS — "Your turn." | `ClaudeComposerAsk` |
| B11 | OUTRO — "A/B Tests Can Lie." + full-size Supriya | `ClaudeTitleOutroFilled` |

## Known traps, pre-empted (from correlation-is-not-causation)

Composer `scale` 1.5 · code ≤35-char lines (done) · composer asks ≤ ~110 chars (done) · 9:16 outro
scale 1.3 start · portrait Manim frame 4.5×8 · native 2160×3840 `END.png` · Gate V with `--mp4` on
the clean master · back up/restore `runtime/remotion/_bench/consumers.json` around renders · never
commit `consumers.json` / `package-lock.json` with reel work.

## Gates

1. Plan — **APPROVED** 2026-10-18.
2. Narration script + `FACTCHECK.md` + `PEDAGOGY.md` — **GATE P PASS** (signed by Supriya
   2026-10-18; flags A/B/D no change, C = on-screen source line in B07). `beat_sheet.json` is written once the narration is final.
3. `scenes.py` + test renders — **done 2026-10-18** (`_sanity/`; nothing in the real `media/`/`manim/`
   slots). Manim: all 5 rendered and checked by frame at 480p and as true-4K stills. Fixed: B01
   carousel underfilled, B04/B07 label-vs-tag collisions, B07 source line vs handle, B08 winner label
   hidden by the >30% box, and a Pango bug: small italic Text loses word spacing at 4K ("SRMsarethis")
   → all italic text now built at 3× and scaled down (`itext()`). Remotion at true 4K (sandbox copy,
   `consumers.json` backed up + restored byte-identical): B00, B03, B06, B10, B11 clean; code excerpts
   fill the card; outro title wraps to two lines with full-size handle. B00 output line corrected to
   the exact "3,003 users missing". Portrait Manim (`short/scenes.py`) is built at step 6.
4. Audio → measure. **Done 2026-10-18: 148.94s** (153.4s with the 4.5s endcard) → full-length 9:16.
   Not yet listened to by a person (local whisper is broken) — B00's "A-B" reading still to confirm.
5. 16:9 render → QC frames → ffprobe. **Done 2026-10-18:** `2026-10-12-ab-testing-can-lie-to-you.mp4` —
   3840×2160, 148.94s, 24 fps, **1.17 Mbps video** (40M ABR target undershoots on flat frames) —
   **FLAGGED to Supriya, not padded** (below the ~1.5 Mbps accepted on correlation). Gate B (strict)
   caught two safe-area overflows (B07 right column, B08 title/ticks/tag) and Gate V caught B01's
   carousel crossing the left title-safe edge — all fixed in `scenes.py` and re-rendered. Gate V on
   the clean master: 0 BLOCKER / 0 MAJOR; every beat looked at.
6. 9:16 render → QC frames → ffprobe. **Done 2026-10-18:** `2026-10-12-ab-testing-can-lie-to-you-vertical.mp4` —
   2160×3840, 153.44s (full-length + 4.5s endcard; `shorts.py`: "under the cap → full reformat, no
   beats cut"), 24 fps, **1.39 Mbps video** — **FLAGGED to Supriya, not padded**. Portrait Manim in
   `short/scenes.py` (data/timing imported from `../scenes.py`); Gate B clean on all 5 after fixing
   portrait safe-area grazes. Gate V on the clean master 0 BLOCKER / 0 MAJOR (run.sh's Gate V on the
   `-slate` cut false-flags every portrait frame — known). Changes found by looking/Gate V:
   **B11 outro scale 1.6** (1.3 underfilled at 38% — this title is short; 1.9 crowds the top) — flagged;
   END.png redrawn natively at 2160×3840 with enlarged type (first redraw 52% < 55%); **portrait code
   cards showed "SQL"** (Root.tsx 916 default leak) → `lang: "python"` set explicitly in both sheets,
   B03/B06 re-rendered. B00 output lines shortened ≤30 chars for portrait (same meaning).
   Slate cuts and `mp4/` copies removed; masters are the only mp4s in the reel root.
