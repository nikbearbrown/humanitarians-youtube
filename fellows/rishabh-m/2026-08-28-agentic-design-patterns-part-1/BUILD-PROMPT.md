# BUILD-PROMPT — agentic-design-patterns-part-1

Paste-ready Claude Code prompt that rebuilds this reel end to end. Run from
`brutalist.art/`. Never publishes.

> **Machine-specific preamble (this machine only).** Read
> `SETUP-LOG.local.md` and `HOUSE-RULES.local.md` in `brutalist.art/` first.
> `source art-venv/bin/activate` before anything, and **never** run
> `./setup --install` — it fails on the manimpango pin and empties the venv.

---

```
Rebuild the reel at:
  "/Users/rishabh_hm/Documents/RA - Nik Brown/Agentic Design Video/youtube/agentic-design-patterns-part-1"

Read these first, in order:
  1. brutalist.art/HOUSE-RULES.local.md   — Rishabh's greeting + 1s beat gap
  2. brutalist.art/skills/make/ai-explainer/SKILL.md — in full
  3. the reel's CHECKS-REPORT.md, FACTCHECK.md, SOURCES.md

Then run, with art-venv active, from brutalist.art/:

  REEL="/Users/rishabh_hm/Documents/RA - Nik Brown/Agentic Design Video/youtube/agentic-design-patterns-part-1"

  # 1. audio — the master clock. af_sarah, set in metadata.voice_kokoro.
  python3 runtime/scripts/generate_audio_kokoro.py "$REEL"

  # 2. HOUSE-RULES RULE 2 — the 1.0s inter-beat hold. Never skip.
  python3 pad_beats.local.py "$REEL"

  # 3. Remotion beats -> media/<BID>.mp4 at true 4K (--scale=2)
  python3 runtime/scripts/remotion_scenes.py "$REEL" --force

  # 4. compile the review cut, then the clean master
  ./art run "$REEL"
  ./art final "$REEL"

  # 5. VISUAL QC LAW — sample frames and LOOK at them, do not trust the probe
  ffmpeg -i "$REEL"/*-slate.mp4 -vf fps=2 "$REEL"/_qc/frames/%05d.png
  # read the PNGs; audit the 9-point rubric; log to _qc/REPORT.md
  # zero BLOCKER and zero MAJOR before this reel is done

Constraints:
- Voice is af_sarah (author's choice). Do not substitute am_onyx.
- The outro is HaiTitleOutro, NOT ClaudeTitleOutro — the latter hardcodes
  @NikBearBrown (OUTRO-LOCK.md) and must never appear on this channel.
- No mascot on this reel. OUTRO-LOCK is scoped to claude-liam only.
- Never publish. The master stays in the reel folder.
```

---

## Components this reel depends on

Both were authored for it (GATE L punts) and now live in the shared library —
if either is missing, the reel will slate:

| Component | File | Purpose |
|---|---|---|
| `AgenticPatternDiagram` | `runtime/remotion/src/scenes/AgenticPatternDiagram.tsx` | all six pattern topologies + the framework grid (B02–B10) |
| `HaiTitleOutro` | `runtime/remotion/src/scenes/HaiTitleOutro.tsx` | `@HumanitariansAI` title-restate outro (B13) |

Both are registered in `Root.tsx`. After any change run `./art scene-index`.

## Stock components used

`ClaudeComposerAsk` (B00, B12) · `BrutalistHesitantWriter` (B01) ·
`ClaudeVerdictArtifact` (B11).

## Rebuild-from-scratch note

`pad_beats.local.py` keeps the unpadded originals in `mp3/raw/`. If you
regenerate audio, the raw copies are overwritten on the next pad run — which is
correct. To change the gap length, just re-run with `--pad N`; it always
rebuilds from raw rather than compounding.
