# BUILD-PROMPT — agentic-design-patterns-part-3

Paste-ready Claude Code prompt that rebuilds this reel and its Short end to end.
Run from `brutalist.art/`. Never publishes.

> **Machine-specific preamble.** Read `SETUP-LOG.local.md` and
> `HOUSE-RULES.local.md` in `brutalist.art/` first. `source art-venv/bin/activate`
> before anything, and **never** run `./setup --install` — it fails on the
> manimpango pin and empties the venv.

---

```
Rebuild the reel at:
  "/Users/rishabh_hm/Documents/RA - Nik Brown/Agentic Design Video/youtube/agentic-design-patterns-part-3"

Read first, in order:
  1. brutalist.art/HOUSE-RULES.local.md      — greeting/sign-off, 1s beat gap, gotchas
  2. brutalist.art/skills/make/ai-explainer/SKILL.md — in full
  3. this reel's PEDAGOGY.md, CHECKS-REPORT.md, FACTCHECK.md, SOURCES.md

Then, with art-venv active, from brutalist.art/:

  REEL="/Users/rishabh_hm/Documents/RA - Nik Brown/Agentic Design Video/youtube/agentic-design-patterns-part-3"

  # ---- LONG (16:9) ----
  python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
  python3 pad_beats.local.py "$REEL"                    # HOUSE-RULES RULE 2 — never skip
  python3 runtime/scripts/remotion_scenes.py "$REEL" --force
  ./art run   "$REEL"
  ./art final "$REEL" --out "$REEL"

  # ---- SHORT (9:16) ----
  SHORT="$REEL/short"
  python3 runtime/scripts/generate_audio_kokoro.py "$SHORT"
  python3 pad_beats.local.py "$SHORT"
  python3 runtime/scripts/remotion_scenes.py "$SHORT" --force
  ART_QC=0 python3 runtime/scripts/compile.py "$SHORT" --height 3840 --out "$SHORT"
  python3 runtime/qc/final_frame_check.py "$SHORT" \
          --mp4 "$SHORT/agentic-design-patterns-part-3-short.mp4"

  # ---- VISUAL QC LAW: sample frames and LOOK at them ----
  # zero BLOCKER and zero MAJOR before this reel is done.

Constraints:
- Voice is af_sarah. Do not substitute am_onyx.
- Outro is HaiTitleOutro / HaiTitleOutro916 — NEVER ClaudeTitleOutro, which
  hardcodes @NikBearBrown (OUTRO-LOCK.md). No mascot on this channel.
- metadata.topic must stay "Irreducibly Human" — GATE L blocks otherwise.
- The Short is PURPOSE-AUTHORED. Do not regenerate it with ./art shorts.
- Never publish. Masters stay in the reel folder.
```

---

## B01 is the fragile beat — do not resize it casually

It has two constraints that pull against each other, and both were violated on
the first pass:

1. **Audio window.** `BrutalistHesitantWriter` has a fixed typing floor (~5.3s
   for three lines) and Gate V samples at 50% of the beat. Narration is 42 words
   → 16.5s, sampling at 8.2s. A shorter narration fails `underfill`.
2. **Line width.** EB Garamond is **0.385 em per character**, so
   `max chars per line ≈ 4220 / fontSize`. At 175pt that is 24 characters; the
   longest line here is 26, which rendered at 101% of SAFE.w — an `edge-bleed`
   BLOCKER. `fontSize` is **162**, which allows 26.

**Count the longest line in its FINAL state.** `"These seven are features."` is
25 characters but becomes `"These seven are governors."` — 26 — only after the
trigger-word swap. The correction can lengthen the line.

## Components

No new components. All seven topologies *and* B10's blueprint chain are carried
by `AgenticPatternDiagram`, built for Part 1 — the third reel running on it
unmodified.

| Component | Used by |
|---|---|
| `ClaudeComposerAsk` / `…916` | B00, B13 · S00 |
| `BrutalistHesitantWriter` | B01 |
| `AgenticPatternDiagram` / `…916` | B02–B11 · S01–S09 |
| `ClaudeVerdictArtifact` | B12 |
| `HaiTitleOutro` / `…916` | B14 · S10 |

All registered in `runtime/remotion/src/Root.tsx`. After any component change
run `./art scene-index`.

## Why the Short compiles differently

`ART_QC=0` plus a separate Gate V call is **not** skipping QC — it is the
workaround for a toolkit bug. Gate V samples the `-slate.mp4` and excludes its
burn-in label via `BURN_IN_EXCLUDE = (0.0, 0.94, 0.60, 1.0)`, covering only 60%
of frame width. In portrait the label spans ~98%, so every beat false-flags as
`edge-bleed`. QC the clean cut — that is what ships.
