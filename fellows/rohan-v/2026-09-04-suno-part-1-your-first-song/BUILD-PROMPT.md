# BUILD-PROMPT — suno-part-1

Paste this into Claude Code from `D:\Rohan\Claude\HAI\RohanClaudeHAIbrutalist.art` to build the full cut end to end.

> **Read this first — two traps this reel already fell into.**
> 1. **Never call `compile.py` bare.** Its `--height` defaults to **720**, so it
>    silently writes a 1280×720 master even when every per-beat render is true 4K.
>    Use `./art final`, which passes `--height 2160`.
> 2. **A composition shorter than its beat becomes a still.** `remotion_scenes.py`
>    freeze-holds the last frame to fill the gap between a composition's
>    `durationInFrames` and the beat's measured audio. If Root.tsx says 300 frames
>    and the narration is 21s, ~11s of that beat is a frozen image. Keep
>    `durationInFrames` >= `actual_duration_s * 30`.

```
Build the "Suno, Part One." tutorial reel for Lyrical Literacy.

Reel folder: D:\Rohan\Claude\HAI\lyrical-literacy\youtube\suno-part-1\
Beat sheet:  beat_sheet.json (12 beats, claude-hai-lyrical channel, voice af_bella)

Set PYTHONUTF8=1 before every python step (Windows cp1252 corrupts the beat sheet).

1. GATE L — beat lint (branding kicker, beat mix):
   python3 runtime/qc/beat_lint.py <reel>/beat_sheet.json

2. AUDIO LOCK — three steps, never one. This is the master clock.
   a. python3 runtime/scripts/generate_audio_kokoro.py <reel>
      (writes actual_duration_s back into the beat sheet)
   b. python3 runtime/scripts/align.py <reel>
      THE WORD CLOCK. faster-whisper measures when every word is actually
      spoken -> mp3/words.json. Skipping this is what makes animation drift
      against the voiceover.
   c. python3 runtime/scripts/sync_cues.py <reel>
      Resolves the anchor phrases in <reel>/cues.json against words.json and
      writes exact fractions into beat_sheet.json at shot.remotion.props.cues.
      Scenes read those instead of guessed numbers.
   Re-run (b) and (c) after ANY narration change.

3. Sync composition lengths. sync_cues.py prints the required value per beat.
   In runtime/remotion/src/Root.tsx set each Suno scene's durationInFrames to
   EXACTLY round(actual_duration_s * 30). A few frames off stretches every
   cue fraction and reintroduces drift.

4. Typecheck before rendering (cheap; catches scene errors without a render):
   cd runtime/remotion && npx tsc --noEmit -p tsconfig.json

5. Render every beat (foreground; never hand-roll `npx remotion render`):
   python3 runtime/scripts/remotion_scenes.py <reel> --force

6. Cut the 4K master (NOT compile.py directly):
   bash art final <reel>

7. GATE V — frame-level visual QC. Sampled at 50% and 85% of every beat:
   python3 runtime/qc/final_frame_check.py <reel>
   Then LOOK at _qc/contact_sheet.png yourself. The mp4 probe is a file check,
   not QC. Fix root causes in scene source; re-render until zero BLOCKER.

Scenes used (all registered in Root.tsx + scenes.json):
  B00  ClaudeComposerAsk        BVDT ClaudeVerdictArtifact
  B01  SunoL1Bluf               BHTF ClaudeComposerAsk (recap + Part 2 tease)
  B02  SunoL1HowItWorks         BOUT ClaudeTitleOutro
  B03  SunoL1DiscordLogin
  B04  SunoL1Interface          Shared kit: scenes/sunoKit.tsx
  B05  SunoL1SimpleMode           SceneFrame · splitStage · SunoWindow
  B06  SunoL1PromptFormula        WaveBars · Callout · SUNO tokens
  B07  SunoL1Generate
  B08  SunoL1SongCards

Voice: Kokoro af_bella. Channel: @HumanitariansAI. Never publish.
```

## Scene-authoring rules for this series

Learned from Gate V failures on the first cut. These apply to Parts 2 and 3 too.

- **Use `sunoKit`.** `SceneFrame` owns the vertical rhythm (kicker / title /
  spark) and `splitStage()` owns the app-window + annotation-rail split. Scenes
  that hand-roll absolute coordinates are how the first cut ended up with the
  Suno panel sliding under the section title and the callout rail bleeding to
  x=1865, past the 1824 safe edge.
- **Gate V's canvas-fill test is a BOUNDING BOX test**, not pixel density:
  `bbox_area / SAFE_area >= 0.55`, sampled at 50% and 85% of each beat. The
  composition must already span the safe area by the halfway frame — so land
  structural surfaces early and let *content* resolve later.
- **`INK_DELTA = 28` per channel.** `CLAUDE.CARD` (#FFFFFF, Δ10) and
  `CLAUDE.BORDER` (#E5E2D9, Δ28 — not strictly greater) do **not** register as
  ink against the cream page. A white card with a hairline border is invisible
  to the gate. Give it a terracotta rule or a dark fill.
- **Reveal structure early, dimmed; emphasise later.** Cards that appear one at
  a time leave the rail half-empty at a QC sample. Inactive elements hold at
  ~0.52 opacity — above the ~40% floor the legibility contract sets.
- **Readable text >= 24px.** Mockup chrome may sit at 18–22px as texture.
- **Deterministic only.** No `Math.random`, no `Date` — seed `WaveBars` instead.
- **Never hand-author a timing fraction.** Add an anchor phrase to `cues.json`
  and let `sync_cues.py` measure it. On the first Part-1 cut the guessed
  fractions were out by up to ~6 seconds: a callout highlighted the description
  box at 0.28 when the narration only reaches "Song Description" at 0.559.
  Scenes take an optional `cues` prop and keep authored values as fallbacks.

## Render performance — read before adding any full-frame effect

Renders are at `--scale=2` (3840×2160). Anything that covers the whole frame is
paid for on **every frame of every beat**, so full-frame effects are the single
biggest lever on build time.

Measured on this reel:

| Full-frame treatment | Cost |
|---|---|
| No texture | ~2.6 min/beat |
| Live SVG `feTurbulence` ×2 | **Did not finish one beat in 50 min.** Chrome re-rasterises a filter over the entire 3840×2160 surface every frame. |
| Pre-rendered tile + `mix-blend-mode: multiply` | ~8 min/beat. Blend modes force a full-surface recomposite each frame. |
| Pre-rendered RGBA tile, normal compositing **(current)** | back toward ~3 min/beat. |

**Rules that follow:**
- Never use an SVG filter (`feTurbulence`, `feGaussianBlur`, …) as a full-frame
  layer. Bake it to a bitmap once. `public/paper-tile.png` is generated in the
  frequency domain (random phases over a 1/f envelope, inverse-FFT'd) so it is
  inherently periodic and tiles seamlessly, from a fixed seed for reproducibility.
- Prefer normal alpha compositing to `mix-blend-mode`. **Done:** the tile is now
  RGBA — black ink carried in the ALPHA channel — because compositing black at
  `alpha = 1 - L/255` is *exactly* equivalent to multiplying by a grey tile of
  luminance `L`. Verified rather than assumed: re-rendering the same frame both
  ways gave a max channel difference of **0** across the texture, with variance
  only on the antialiased glyph edges of one `opacity: 0.9` text element
  (0.097% of pixels). Do not reintroduce `mix-blend-mode` on a full-frame layer.
- A beat can also fail *silently*: `remotion_scenes.py` prints `FAIL: <Scene>`
  for that beat but still exits 0, leaving the previous `media/<BID>.mp4` in
  place. **Always read the render log and check `media/` timestamps** — a stale
  file will compile happily into the master. B08 hit a transient
  `createSilentAudio` error this way.

## Register (all three parts)

Internal volunteer training, not promotion. Pro access is stated once,
mechanically. The host's name is spoken exactly once, in the outro, and is
spelled phonetically in the beat sheet for Kokoro. See `CHECKS-REPORT.md` for
the deviations log and `FACTCHECK.md` for every claim made on screen.
