# Lyrical Literacy · Suno series — build playbook

> **This document is now the SUNO-SPECIFIC companion.** The tool-agnostic build
> playbook — build order, the word clock, Gate V mechanics, render performance,
> the failure modes that fake success, register rules and evidence discipline —
> was promoted to `D:\Rohan\Claude\HAI\VIDEO-PIPELINE.md` when the Midjourney
> series started, so the two series cannot drift apart. Read that first; this
> file's §8 (verified Suno UI facts) remains Suno-only.

Everything learned building Part 1, in the order you need it. **Read this before
starting any part.** Every rule here exists because breaking it cost a rebuild.

Toolkit: `D:\Rohan\Claude\HAI\RohanClaudeHAIbrutalist.art` (brutalist.art)
Reels:   `D:\Rohan\Claude\HAI\lyrical-literacy\youtube\suno-part-N\`

---

## 0. Non-negotiables

- `export PYTHONUTF8=1` before **every** python step. Windows cp1252 corrupts
  the beat sheet's en-dashes and typographic quotes, and crashes scripts that
  print them.
- **Never call `compile.py` directly.** Its `--height` defaults to **720**, so it
  silently writes a 1280x720 master even when every per-beat render is true 4K.
  Use `bash art final <reel>` — that passes `--height 2160`.
- **Never publish.** The master stays in the reel folder.
- **No screen recordings, ever.** All UI is rebuilt as native Remotion scenes
  (REBUILD LAW). The screenshots in `Suno Screenshots/` are reference only.

---

## 1. The build order

Steps 2a-2c are one unit. Splitting them is what desynced Part 1.

```
1.  beat_sheet.json          author narration + show blocks + cues.json anchors
2a. generate_audio_kokoro.py writes actual_duration_s back into the beat sheet
2b. align.py                 THE WORD CLOCK -> mp3/words.json
2c. sync_cues.py             resolves anchors -> props.cues + prints frame counts
3.  Root.tsx                 durationInFrames = round(actual_duration_s * 30)
4.  npx tsc --noEmit         cheap; catches scene errors without a render
5.  remotion_scenes.py --force
6.  bash art final <reel>    the 4K master
7.  final_frame_check.py     Gate V, then LOOK at the frames yourself
```

Re-run **2b, 2c, 3** after *any* narration change, however small.

---

## 2. Sync — the thing that bit hardest

Scenes animate on fractions of `durationInFrames`. Authored by hand those
fractions are guesses, and guesses drift. Measured drift on the first Part-1 cut:

| beat | cue | guessed | measured | error |
|---|---|---|---|---|
| B05 | "Song Description" | 0.28 | 0.559 | **~6.1s early** |
| B04 | "Home" | 0.06 | 0.268 | ~4.5s early |
| B06 | "Topic" | 0.55 | 0.454 | ~2.2s late |

**Two conditions must both hold:**

1. Cues come from the word clock. `cues.json` maps cue names to anchor phrases;
   `sync_cues.py` resolves them against `words.json` and writes fractions into
   `beat_sheet.json` at `shot.remotion.props.cues`. Scenes take an optional
   `cues` prop with authored fallbacks.
2. `durationInFrames` **equals** `round(actual_duration_s * 30)`. A few frames
   off stretches every fraction. `sync_cues.py` prints the right number per beat.

`cues.json` format — anchors are matched case/punctuation-insensitively:

```json
{ "B05": { "tabs": "three tabs", "desc": "Song Description box",
           "inst": "Instrumental toggle", "create": "Create button" } }
```

Prefer a distinctive 2-4 word phrase. Single common words mis-anchor.

---

## 3. Layout — use the kit, do not hand-roll coordinates

`runtime/remotion/src/scenes/sunoKit.tsx` exists so the Part-1 defects are
unrepresentable:

- `SceneFrame` owns the vertical rhythm (kicker / title / spark) and hands you a
  `CONTENT` rect of **x 96, y 174, w 1728, h 768**. Hand-rolled coordinates are
  how the first cut slid the app window under its own section title.
- `splitStage()` derives an app-window + annotation-rail split whose right edge
  lands on the safe edge **by construction**. The first cut placed a rail at
  `panelRight + 36` with a fixed width and it resolved to x=1865, past 1824.
- `SunoWindow` is the full app chrome; `SunoTrackRow` is a library row;
  `Callout` is the cream annotation card; `WaveBars` is a seeded waveform.
- `PaperGround` (`tokens/paper.tsx`) is the cream page with laid-paper texture.

**Title-safe: x 96-1824, y 54-1026.** Nothing readable crosses it.

---

## 4. Gate V — how it actually measures

Knowing the mechanics saves a render cycle:

- **Canvas fill is a BOUNDING-BOX test**, not pixel density:
  `bbox_area / SAFE_area >= 0.55`, sampled at **50% and 85% of every beat**. So
  the composition must already span the safe area by the halfway frame — land
  structural surfaces early and let *content* resolve later.
- **`INK_DELTA = 28` per channel.** `CLAUDE.CARD` (#FFFFFF, delta 10) and
  `CLAUDE.BORDER` (#E5E2D9, delta **28** — not strictly greater) do **not** count
  as ink on the cream page. A white card with a hairline border is invisible to
  the gate. Give it a terracotta rule or a dark fill.
- **Judge the settled state.** Frames mid-transition legitimately show
  translucent overlays; the rubric excludes them. Re-sample ~1.5-3s after a cue
  before calling something a defect.
- Its `low-contrast` check compares *surfaces*, not text against its own
  background. A big white card on a textured page can trip it while the text is
  WCAG AAA. Measure before believing it.

Reveal structure **early and dimmed**, emphasise later. Cards that pop in one at
a time leave dead space at the 50% sample. Inactive elements hold at ~0.52
opacity — above the ~40% floor the legibility contract sets. But note: 0.52 is
correct on cream and turns to mud over the dark app window; there, keep cards
opaque and de-emphasise with a filter, or dock them in an opaque cream drawer.

Readable annotation text **>= 24px**. App chrome may sit at 15-22px as texture.

---

## 5. Render performance

At `--scale=2` (3840x2160) anything covering the whole frame is paid for on every
frame of every beat.

| full-frame treatment | cost |
|---|---|
| none | ~2.6 min/beat |
| live SVG `feTurbulence` x2 | **never finished one beat in 50 min** |
| pre-rendered tile + `mix-blend-mode` | ~8 min/beat |
| pre-rendered RGBA tile, normal compositing **(current)** | ~5.8 min/beat |

- Never use an SVG filter as a full-frame layer. Bake it to a bitmap once.
- Avoid `mix-blend-mode` on a full-frame layer. Multiplying a tint by a grey tile
  is *exactly* compositing black at `alpha = 1 - L/255`, so bake grain into the
  ALPHA channel instead. Verified pixel-identical (max channel diff 0).
- Budget ~70 min for a 12-beat render. Run it in the background.

---

## 6. Failure modes that fake success

- **A beat can fail silently.** `remotion_scenes.py` prints `FAIL: <Scene>` for
  that beat and **still exits 0**, leaving the previous `media/<BID>.mp4` in
  place. A stale beat compiles happily into the master. **Always** read the
  render log AND diff `media/` timestamps before compiling. Hit once, via a
  transient `createSilentAudio` error.
- **Paint order.** Absolutely-positioned elements paint ABOVE static content, so
  `PaperGround` covered the outro's title and subline — the handle survived only
  because its `opacity: 0.9` created a stacking context. `PaperGround` now carries
  `zIndex: -1`; that is load-bearing.
- **Zod `.default()` on a shared component breaks other reels.** It makes the
  prop *required* in Remotion's `defaultProps` type. Use `.optional()` when
  adding a prop to a house scene, so existing reels compile untouched.
- **A scene-level fade can encode a BLACK FRAME.** `ClaudeTitleOutro` put its
  opening `opacity` on the `AbsoluteFill` *including the background*, so frame 0
  rendered fully transparent and encoded as pure black. Beats are hard-concatenated
  (`compile.py` has no crossfade), so that became a one-frame black flash on the
  cut into the outro. **Never fade a fill that carries the ground — fade the
  content inside it and keep the ground opaque from frame 0.** Detect it by
  sampling the first frames of the beat mp4, not the master: a single black frame
  is easy to step over when sampling the concatenated cut.
- **Heteronyms will be mispronounced and you cannot hear it.** Kokoro read
  "where the actions **live**" as /laɪv/ ("live TV") instead of /lɪv/. Since the
  build cannot listen back, prefer rewording over a phonetic gamble: "where the
  actions **sit**". Other traps to avoid in narration: read, lead, bow, close,
  record, present, use, wind, tear, object, produce, contract.
- **A reference document can itself carry the error.** `SUNO-UI-SPEC.md` §9 put
  two menu entries on one line of a code block; a line-count then read "four
  submenus" when the product has five, and that reached a narration draft. When a
  spec states a COUNT, write the count out explicitly and put one item per line.
- **A fact fix is never one edit.** Correcting the submenu count meant changing
  the narration, the sparkLine, the scene's ring set AND the annotation rail copy.
  Changing only the narration would have left the voice saying "five" over four
  rings. After any factual correction, grep the scene for the old number and the
  old wording — hardcoded copy does not follow the data. This has now bitten
  three times: the Part 1 menu callout, the Part 2 tease, and here.
- **Composition too short = a frozen still.** `remotion_scenes.py` freeze-holds
  the last frame to fill any gap. 300 frames against 21s of narration means ~11s
  of still image. This is why step 3 exists.

---

## 7. Register and content rules (all parts)

- **Internal volunteer training, not promotion.** No "free forever", no "no credit
  card", no selling the organisation's generosity. Pro access is stated **once**,
  mechanically, as a consequence of signing in with Discord.
- **Host:** opens "Hi, I'm Rohaan from Humanitarians AI"; full name spoken
  **exactly once**, in the outro. Phonetic spellings for Kokoro are deliberate —
  `Rohaan` = Row-Haan. Do not "correct" them.
- **Body beats ~45-70 words.** The screen carries evidence; the voice carries
  judgment. Author the `show` block before the narration.
- **End card:** episode title restated, handle beneath, name in small print.
- **Every on-screen claim goes in `FACTCHECK.md`.** No model version numbers or
  figures that will date.

---

## 8. Verified Suno UI facts

Built from the author's screenshots in `youtube/Suno Screenshots/`. Corrections
already paid for once:

- Sidebar: **Home · Explore · Create · Studio · Library · Hooks**, then the
  workspace chip, then Earn Credits · Labs · Notifications · More, then
  "Upgrade to Premier". There is **no Search or Radio nav item**.
- Wordmark is **`SUNO`** — caps, heavy, letterspaced.
- Create tabs are **Simple · Advanced · Sounds**. There is **no "Custom" tab**;
  Advanced is where lyrics and structure live.
- Suno is near-black with low-chroma greys. The one saturated colour is the
  **magenta version badge** (`v5.5`). The Create button is a **muted dark
  control**, not a purple gradient.
- Instrumental is a **pill**, beside a "+ Lyrics" pill — not a toggle switch.
- Create page is **three columns**: sidebar | composer | workspace result list.
- A **bottom player bar** is present on every page.
- Track rows show artwork + duration badge + version badge + actions, and
  **no waveform**. Waveforms are this series' own explanatory device.
- Song cards have **no "Regenerate" button**. The three-dot menu is
  Extend · Remix/Edit · Download · Share · Move to Trash.
