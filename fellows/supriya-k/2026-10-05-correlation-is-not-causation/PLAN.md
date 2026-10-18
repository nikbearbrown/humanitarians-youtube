# PLAN — correlation-is-not-causation (cli-explainer)

**Status: APPROVED 2026-10-14.** Voice: `af_bella` (Bella), persona none, narrator identity
"Supriya" — continuity with claude-code-explained and the banking reels.

## Decisions (approved by Supriya, 2026-10-14)

1. **Example:** the kidney-stone Simpson's paradox — Charig et al., *BMJ* 1986 (Table II has both the totals and the size split), framed
   by Julious & Mullee, *BMJ* 1994 "Confounding and Simpson's paradox". Real, published, verified.
   Rejected: Berkeley 1973 admissions (too familiar), HRT / WHI (patient-level data not freely
   available, so the code beat couldn't run on real rows).
2. **Code language: SQL** (SQLite). The table and both queries live in `sql/` and are actually run;
   the CODE beats show them verbatim and the OUTPUT beats animate their real result
   (`sql/*.out`). `lang: sql` on `ClaudeCodeBeat`.
3. **Full-length 9:16, no shortened cut.** The revision cycle IS the punchline, so it stays in the
   9:16. Narration ~390 words, ~152s est.; 16:9 + 4.5s endcard must clear the 180s Shorts cap.
   If measured audio comes in over ~170s, stop and re-tighten — never drop a beat.
4. **Bitrate:** existing opt-in `compile.py --vbitrate` on both final encodes, ffprobe each master.
   Flat Claude-skin frames will likely undershoot (claude-code-explained: 1.0 / 1.25 Mbps). If it
   does, **stop and flag for Supriya's decision** — no artificial CBR padding without approval.
5. **Location:** `projects/correlation-is-not-causation/` (no parent book — same precedent as
   claude-code-explained).
6. **Final filenames:** `2026-10-14-correlation-is-not-causation.mp4` (16:9, 3840×2160) and
   `2026-10-14-correlation-is-not-causation-vertical.mp4` (9:16, 2160×3840).

## The data (verified; `sql/kidney_stones.sql`)

| | Open surgery | Keyhole (PCNL) |
|---|---|---|
| All | 273/350 = 78.0% | 289/350 = **82.6%** |
| Small (<2 cm) | 81/87 = **93.1%** | 234/270 = 86.7% |
| Large (≥2 cm) | 192/263 = **73.0%** | 55/80 = 68.8% |

Success = stones eliminated or < 2 mm at three months (Charig 1986). Confounder: stone size —
263/350 open-surgery patients had large stones; 270/350 keyhole patients had small ones.
**Honest caveat carried in narration (B09):** stratifying is still observational; it removes one
known confounder, not unmeasured ones. Narration says "the hard cases went to surgery", not
"doctors chose to" — the paper reports the mix, not the intent.

## Beat arc (12 beats)

| Beat | Role | Renders via |
|---|---|---|
| B00 | INTRO — exact "Hi, I am Supriya and this video is about…" | `ClaudeComposerAsk` |
| B01 | PROBLEM — 700 patients, two treatments, you pick | Manim `B01_PickOne` |
| B02 | CLI — cycle 1 ask: compare success by treatment | `ClaudeComposerAsk` |
| B03 | CODE — `q1_by_treatment.sql` | `ClaudeCodeBeat` (`lang: sql`, `handle`) |
| B04 | OUTPUT — bars grow to 82.6 vs 78.0, keyhole "wins" | Manim `B04_KeyholeWins` |
| B05 | CLI — the revision: split by stone size | `ClaudeComposerAsk` |
| B06 | CODE — `q2_by_size.sql` | `ClaudeCodeBeat` (`lang: sql`, `handle`) |
| B07 | OUTPUT — bars split; surgery wins both groups | Manim `B07_TheFlip` |
| B08 | MECHANISM — patient counts: who got which stones | Manim `B08_WhoGotWhat` |
| B09 | SUMMARY — three questions + the still-observational caveat | Manim `B09_ThreeQuestions` |
| B10 | NEXT STEPS — "Your turn." confounder-hunt prompt, read aloud | `ClaudeComposerAsk` |
| B11 | OUTRO — "Correlation Is Not Causation." + full-size Supriya | `ClaudeTitleOutroFilled` |

## Branding (PM requirements 3 & 4)

- B00 narration is the exact phrasing; greeting chip "Hi, I am Supriya". Outro: "I am Supriya."
  No "in for X" anywhere.
- "Supriya" visible on **every** beat: composer `folderLabel`, code-beat `handle` chip, a corner
  handle in every Manim scene (16:9 and portrait), full-size outro `handle`, 9:16 endcard via
  `shorts.py --handle Supriya`.

## Known toolkit traps, pre-empted (carried from claude-code-explained)

| Trap | Plan |
|---|---|
| Animation tails truncated when registration > audio (MISS #5) | render at measured audio length; reveals ≤ p 0.6; check last frames |
| Portrait composer overflow on long asks (MISS #9) | every `command` ≤ ~110 chars |
| Manim portrait coordinate frame | `config.frame_width = 4.5; frame_height = 8.0` in `short/scenes.py` from line one |
| ONDA CHECK rewires only already-registered `*916` ids | all `916` comps exist before `./art shorts`; verify render log per beat |
| Endcard hardcoded 1080×1920 | regenerate `END.png` natively at 2160×3840 |
| run.sh Gate V checks the `-slate` cut (labels false-flag portrait) | run `final_frame_check.py --mp4` on the clean master |
| SQL line width in code card (`whiteSpace: pre` clips silently) | queries ≤ ~60 chars/line; `fit` prop if needed; check frames |

## Gates (in order)

1. Plan — **APPROVED** 2026-10-14.
2. Narration script — **APPROVED 2026-10-14** (3 edits + flags A, B applied 2026-10-15; 379 words, ~148s). `beat_sheet.json`, `FACTCHECK.md` (citations verified from scanned pages), `PEDAGOGY.md` — **written**; flags decided → **GATE P PASS** (signed by Supriya 2026-10-15).
3. `scenes.py` (5 Manim classes) — **written 2026-10-15; test renders done** (`_sanity/`, nothing in
   the real `media/`/`manim/` slots). 16:9 Manim: 4 of 5 had layout defects, fixed and re-checked
   by frame — all 5 clean. Remotion at true 4K: 16:9 composer + outro clean; 9:16 composer clean.
   **Approved 2026-10-15:** (a) SQL rewrapped to ≤35-char lines (whitespace only, re-run output
   byte-identical) — applied to `sql/` and B03/B06; (b) 9:16 outro `scale` 1.2 — recorded in
   `beat_sheet.json` `metadata.portrait_overrides`. **GATE 3 PASS.**
   Portrait Manim (`short/scenes.py`) is built at step 6.
4. Audio (`generate_audio_kokoro.py`) → measure; confirm ≤ ~170s. **Done 2026-10-15: 146.25s**
   (150.75s with the 4.5s endcard) → full-length 9:16. Not yet listened to by a person.
5. 16:9 render → Gate B → Gate V → look at `_qc` frames → clean master → ffprobe (flag bitrate).
   **Done 2026-10-15:** `2026-10-14-correlation-is-not-causation.mp4` — 3840×2160, 146.25s,
   **1.58 Mbps** video (40M ABR target undershoots on flat frames; Supriya accepted ~1.5 Mbps, no
   padding). Gates A/W/B clean; Gate V on the master 0 BLOCKER/MAJOR; every beat looked at.
   Shared change (approved): optional `scale` on `ClaudeComposerAsk` (omitted → legacy, verified
   pixel-identical); this reel uses 1.5 on B00/B02/B05/B10.
6. 9:16 via `./art shorts --handle Supriya` (full reformat) → `short/scenes.py` →
   `compile.py --height 3840` → Gate V + frame look at every beat type → ffprobe (flag bitrate).
   **Done 2026-10-15:** `2026-10-14-correlation-is-not-causation-vertical.mp4` — 2160×3840, 150.75s
   (full-length + 4.5s endcard), **1.61 Mbps** video. `shorts.py`: "under the cap → full reformat, no
   beats cut". Portrait Manim in `short/scenes.py` (data/timing imported from `../scenes.py`); all
   Gate B clean. Gate V on the clean master 0 BLOCKER/MAJOR (run.sh's Gate V on the `-slate` cut
   false-flags every portrait frame — known). Outro scale **1.3** (1.2 underfilled 47% < 55%; 1.4
   bleeds). Endcard redrawn natively 2160×3840 and enlarged to pass the fill check.

---

**2026-10-17 — masters renamed to the folder's week date.** The folder became
`2026-10-05-correlation-is-not-causation/` (week 10), and the masters were renamed to match:
`2026-10-05-correlation-is-not-causation.mp4` and `…-vertical.mp4` (content unchanged, same
checksums). The `2026-10-14` names above are the original record. `final_filenames` in
`beat_sheet.json`, `short/beat_sheet.json` and `todo.json` now carry the new names. The
slug-named duplicates, the `mp4/` copies and the three slate cuts were removed.
