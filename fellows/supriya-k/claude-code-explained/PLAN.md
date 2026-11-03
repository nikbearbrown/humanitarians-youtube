# PLAN — claude-code-explained (cli-explainer)

**Status: APPROVED 2026-10-01.** Voice: `af_bella` (Bella), continuity with the banking reels.

## Decisions (approved by Supriya, 2026-10-01)

1. **Full-length 9:16, no shortened cut.** Narration tightened (420 words, ~170s est.) so the 16:9
   plus the 4.5s endcard fits the 180s Shorts cap. `./art shorts` must report *"under the cap →
   full reformat, no beats cut"*. If measured audio comes in over ~170s, stop and re-tighten — the
   revision cycle is never dropped.
2. **Handle on code beats:** optional `handle` + `lang` props added to the SHARED
   `ClaudeCodeBeat` / `ClaudeCodeBeat916` (defaults `''` / `'python'` → existing reels render
   unchanged). Also fixes TEMPLATE-MISSES #1 (hardcoded `python` chip).
3. **Bitrate:** opt-in `--vbitrate` flag on `compile.py`'s final encode (default off). v2's masters
   probed at 345.8 kbps (3840×2160) and 477.3 kbps (2160×3840) — correct pixels, thin bitrate.
   Target ~35–45 Mbps. Honest caveat: the floor makes the files meet a usable 4K spec; real
   detail still comes from filling the frame.
4. **Location:** `projects/claude-code-explained/` (no parent book).

## The subject, and why these two examples

How Claude Code works as a loop — **plan → gate → execute → verify** — told through two real bugs
from this toolkit's own 9:16 build of `banking-domain-interview-end-to-end-v2`, both recorded in its
`STATUS.md` fix log. Nothing is invented.

- **Cycle 1 — the plan was wrong, verify caught it.** v2's `PLAN.md` said `ClaudeComposerAsk` was
  already portrait-aware. A standalone sanity render (the user's instruction) showed content
  clustered in the top ~55% of the frame. Rewritten as `ClaudeComposerAsk916` → ~86%, 276→341 kbps.
- **Cycle 2 — the check passed, the frame was wrong.** `manim -r 2160,3840` doesn't reset
  `config.frame_width/height`; scenes rendered into the center ~25–28% while Gate B reported clean
  (the audit overrode the frame in its own process). Fixed with two config lines.

## Beat arc (12 beats)

| Beat | Role | Renders via |
|---|---|---|
| B00 | INTRO — exact phrasing "Hi, I am Supriya and this video is about…" | `ClaudeComposerAsk` |
| B01 | PROBLEM — Claude can't watch the video; v1's 139.5 kbps 9:16 | Manim `B01_CannotWatch` |
| B02 | MECHANISM — the loop with the real files at each step | Manim `B02_TheLoop` |
| B03 | CLI — cycle 1 ask | `ClaudeComposerAsk` |
| B04 | CODE — `ClaudeComposerAsk916.tsx` anchors | `ClaudeCodeBeat` (`lang: tsx`, `handle`) |
| B05 | OUTPUT — 55%→86%, 276→341 kbps | Manim `B05_FillBefore_After` |
| B06 | CLI — the revision | `ClaudeComposerAsk` |
| B07 | CODE — `short/scenes.py` config fix | `ClaudeCodeBeat` (`lang: python`, `handle`) |
| B08 | OUTPUT — center quarter → full frame | Manim `B08_WholeFrame` |
| B09 | SUMMARY — four moves, who owns each | Manim `B09_FourMoves` |
| B10 | NEXT STEPS — "Your turn." plan-and-verify prompt | `ClaudeComposerAsk` |
| B11 | OUTRO — "Claude Code, Explained." + full-size Supriya | `ClaudeTitleOutroFilled` |

## Branding (PM requirements 3 & 4)

- B00 narration is the exact phrasing; greeting chip reads "Hi, I am Supriya". Outro: "I am
  Supriya." No "in for X" anywhere.
- "Supriya" visible on **every** beat: composer `folderLabel`, code-beat `handle` chip, a corner
  handle in every Manim scene (16:9 and portrait), full-size outro `handle`, and the 9:16 endcard
  (`shorts.py --handle Supriya` — its default is `@nikbearbrown`).

## Known toolkit traps, pre-empted

| Trap | Source | Plan |
|---|---|---|
| Animation tails truncated when registration > audio | TEMPLATE-MISSES #5 | register/render at measured audio length; keep reveals ≤ p 0.6; check last frames |
| Portrait composer overflow on long asks | MISS #9 | every `command` ≤ ~110 chars |
| Manim portrait coordinate frame | v2 STATUS | `config.frame_width = 4.5; frame_height = 8.0` in `short/scenes.py` from line one |
| ONDA CHECK rewires only already-registered `*916` ids | v2 STATUS | all `916` comps exist before `./art shorts` runs; verify the render log per beat |
| Endcard hardcoded 1080×1920 | v2 STATUS | regenerate `END.png` natively at 2160×3840 |
| SKIN LINT false positives on `916` / `Filled` outro | MISS #8 | expected; noted, not a defect |

## Gates (in order)

1. Plan — **APPROVED** 2026-10-01.
2. Paperwork + `beat_sheet.json` — written; **human signs `PEDAGOGY.md`**.
3. `scenes.py` (5 Manim classes) + `ClaudeCodeBeat`/`916` prop change + `compile.py --vbitrate` —
   human reviews before anything renders; each 916 beat type sanity-rendered standalone first.
4. Audio (`generate_audio_kokoro.py`) → measure; confirm ≤ ~170s.
5. 16:9 render → Gate B → Gate V → look at `_qc` frames → clean master → ffprobe.
6. 9:16 via `./art shorts --handle Supriya` (must be a full reformat) → `short/scenes.py` →
   `compile.py --height 3840` → Gate V + frame look at every beat type → ffprobe.
