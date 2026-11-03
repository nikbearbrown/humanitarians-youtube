# BUILD-PROMPT — agentic-design-patterns-part-2

Paste-ready Claude Code prompt that rebuilds this reel and its Short end to end.
Run from `brutalist.art/`. Never publishes.

> **Machine-specific preamble.** Read `SETUP-LOG.local.md` and
> `HOUSE-RULES.local.md` in `brutalist.art/` first. `source art-venv/bin/activate`
> before anything, and **never** run `./setup --install` — it fails on the
> manimpango pin and empties the venv.

---

```
Rebuild the reel at:
  "/Users/rishabh_hm/Documents/RA - Nik Brown/Agentic Design Video/youtube/agentic-design-patterns-part-2"

Read first, in order:
  1. brutalist.art/HOUSE-RULES.local.md      — greeting/sign-off, 1s beat gap, gotchas
  2. brutalist.art/skills/make/ai-explainer/SKILL.md — in full
  3. this reel's PEDAGOGY.md, CHECKS-REPORT.md, FACTCHECK.md, SOURCES.md

Then, with art-venv active, from brutalist.art/:

  REEL="/Users/rishabh_hm/Documents/RA - Nik Brown/Agentic Design Video/youtube/agentic-design-patterns-part-2"

  # ---- LONG (16:9) ----
  python3 runtime/scripts/generate_audio_kokoro.py "$REEL"
  python3 pad_beats.local.py "$REEL"                    # HOUSE-RULES RULE 2 — never skip
  python3 runtime/scripts/remotion_scenes.py "$REEL" --force
  ./art run   "$REEL"                                   # gates + review cut + Gate V
  ./art final "$REEL" --out "$REEL"                     # clean 4K master

  # ---- SHORT (9:16) ----
  SHORT="$REEL/short"
  python3 runtime/scripts/generate_audio_kokoro.py "$SHORT"
  python3 pad_beats.local.py "$SHORT"
  python3 runtime/scripts/remotion_scenes.py "$SHORT" --force
  ART_QC=0 python3 runtime/scripts/compile.py "$SHORT" --height 3840 --out "$SHORT"
  python3 runtime/qc/final_frame_check.py "$SHORT" \
          --mp4 "$SHORT/agentic-design-patterns-part-2-short.mp4"

  # ---- VISUAL QC LAW: sample frames and LOOK at them ----
  # zero BLOCKER and zero MAJOR before this reel is done.

Constraints:
- Voice is af_sarah. Do not substitute am_onyx.
- Outro is HaiTitleOutro / HaiTitleOutro916 — NEVER ClaudeTitleOutro, which
  hardcodes @NikBearBrown (OUTRO-LOCK.md). No mascot on this channel.
- metadata.topic must stay "Irreducibly Human" — GATE L blocks the build
  otherwise (runtime/qc/brand_labels.json fixes the claude-hai kicker).
- The Short is PURPOSE-AUTHORED, not a shorts.py derivative. Do not regenerate
  it with ./art shorts.
- Never publish. Masters stay in the reel folder.
```

---

## Why the Short compiles differently

`ART_QC=0` then a separate Gate V call is **not** a way to skip QC — it is the
workaround for a toolkit bug. Gate V samples the `-slate.mp4` and excludes its
burn-in label via `BURN_IN_EXCLUDE = (0.0, 0.94, 0.60, 1.0)`, which covers only
60% of frame width. In portrait the label spans ~98%, so every beat false-flags
as `edge-bleed`. QC the clean cut instead — that is what ships anyway.

## Components

No new components were authored for Part 2. All seven topologies are carried by
`AgenticPatternDiagram`, built for Part 1.

| Component | Used by |
|---|---|
| `ClaudeComposerAsk` / `…916` | B00, B13 · S00 |
| `BrutalistHesitantWriter` | B01 |
| `AgenticPatternDiagram` / `…916` | B02–B11 · S01–S08 |
| `ClaudeVerdictArtifact` | B12 |
| `HaiTitleOutro` / `…916` | B14 · S09 |

All are registered in `runtime/remotion/src/Root.tsx`. After any component
change run `./art scene-index`.

## Known beat-level constraints

- **B01** (`BrutalistHesitantWriter`) is the fragile one. Narration is 39 words
  → 12.0s so Gate V's 50% sample lands after the ~5.3s typing floor; `fontSize`
  is 175 for canvas fill. Shortening that narration will fail `underfill`.
- **S09** portrait outro title size is adaptive (`4760 / len`) — a fixed size
  made canvas fill depend on title length.
