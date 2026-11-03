# BUILD-PROMPT — suno-part-2

Paste into Claude Code from `D:\Rohan\Claude\HAI\RohanClaudeHAIbrutalist.art`.

> **Read `../SERIES-PIPELINE.md` first.** It carries every trap this series has
> already paid for: the 720p default, the word clock, the silent beat failure,
> the black-frame fade, the paint-order bug, render cost. This file is only the
> Part-2-specific sheet.

```
Build "Suno, Part Two." for Lyrical Literacy.

Reel:       D:\Rohan\Claude\HAI\lyrical-literacy\youtube\suno-part-2\
Beat sheet: beat_sheet.json  (11 beats, claude-hai-lyrical, voice af_bella)
Cues:       cues.json        (anchor phrases -> measured fractions)

export PYTHONUTF8=1 before every python step.

1. GATE L    python3 runtime/qc/beat_lint.py <reel>/beat_sheet.json
2. AUDIO LOCK — three steps, never one:
   a. python3 runtime/scripts/generate_audio_kokoro.py <reel>
   b. python3 runtime/scripts/align.py <reel>
   c. python3 runtime/scripts/sync_cues.py <reel>
3. Root.tsx  set each SunoL2* durationInFrames to the value sync_cues prints
             (= round(actual_duration_s * 30)). Exact, not "at least".
4. cd runtime/remotion && npx tsc --noEmit -p tsconfig.json
5. python3 runtime/scripts/remotion_scenes.py <reel> --force
   --only takes ONE beat id. Read the log; a beat can print FAIL and still exit 0.
   Diff media/ timestamps before compiling.
6. bash art final <reel>
7. python3 runtime/qc/final_frame_check.py <reel>
   Then LOOK at _qc/contact_sheet.png, and sample frames AT the measured cue
   times to confirm motion lands on the words.

Beats -> scenes:
  B00  ClaudeComposerAsk        B06  SunoL2Iterate   (new)
  B01  SunoL2Bluf      (new)    B07  SunoL2Advanced  (new)
  B02  SunoL2Contrast  (new)    BVDT ClaudeVerdictArtifact
  B03  SunoL2Style     (new)    BHTF ClaudeComposerAsk
  B04  SunoL2Mood      (new)    BOUT ClaudeTitleOutro
  B05  SunoL2Topic     (new)

Never publish.
```

## Seven new scenes — the contract

All build on `runtime/remotion/src/scenes/sunoKit.tsx`. No new layout
primitives; that is what the kit is for.

- `PaperGround` as the background — **not** a flat `background: CLAUDE.PAGE`.
- `SceneFrame` owns kicker/title/spark. **Pass
  `kicker="LYRICAL LITERACY · SUNO TUTORIAL PART 2"`** — the kit default still
  says PART 1.
- Lay content inside `CONTENT` (x 96, y 174, w 1728, h 768).
- Schema: `{ sparkLine: z.string().default(...), cues: z.record(z.string(), z.number()).optional() }`
  and resolve with `const at = (k, d) => cues?.[k] ?? d;` so the scene still
  renders sensibly before `sync_cues.py` has run.
- Readable annotation text ≥ 24px. App chrome may sit at 15–22px as texture.
- Deterministic only — no `Math.random`, no `Date`. Seed `WaveBars`.
- One accent per surface: terracotta on cream; Suno's magenta only inside dark
  Suno surfaces.
- Structure must span the safe area by the **50%** frame (Gate V samples 50% and
  85%). Land surfaces early, resolve content later.
- Register the composition in `Root.tsx` and run `bash art scene-index`.

## Cue keys each scene must accept

| Scene | Beat | Cue keys |
|---|---|---|
| `SunoL2Bluf` | B01 | `sentence` · `vague` · `specific` · `map` |
| `SunoL2Contrast` | B02 | `vague` · `vagueOut` · `specific` · `specificOut` · `verdict` |
| `SunoL2Style` | B03 | `frame` · `genre` · `instruments` · `production` · `close` |
| `SunoL2Mood` | B04 | `feeling` · `energy` · `together` · `caution` |
| `SunoL2Topic` | B05 | `subject` · `far` · `near` · `close` |
| `SunoL2Iterate` | B06 | `problem` · `rule` · `counter` · `close` |
| `SunoL2Advanced` | B07 | `advanced` · `split` · `styles` · `lyrics` · `structure` |

## Fidelity notes for `SunoL2Advanced`

Build against `../Suno Screenshots/Advanced Tab 1-4.png`. Panel order:
**Lyrics** (placeholder *"Start writing lyrics…"*, `Help me write lyrics`
button) → **Styles** (comma-separated tags + chips) → **More Options**
(collapsed) → `Song Title (Optional)` → `Save to… My Workspace` → `Create`.

**Do not render More Options expanded** — Exclude styles, Vocal Gender,
Weirdness, Style Influence and Duration are Part 3.

Suno is near-black with low-chroma greys; the one saturated colour is the
magenta version badge. The Create button is a muted dark control, never a
gradient.

## Ear-check before shipping

The build cannot hear itself. A human must listen for:

- `lo-fi` (B03)
- `Rohaan` (BOUT)

And scan any narration edit for heteronyms — Part 1 shipped "live" read as
/laɪv/. See `CHECKS-REPORT.md` for the pass already done.
