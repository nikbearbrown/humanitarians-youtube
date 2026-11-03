# VISUAL QC LOG — The Judgment Is the Job.

Frame-level QC per VISUAL QC LAW. Frames sampled from every beat's measured span and
**read as images**, then measured with Gate V's own `analyze_frame`. The mp4 probe was
never treated as QC. `_qc/REPORT.md` is machine-generated and overwritten each
`./art run`; this file is the durable record.

## Headline: 10/10 beats rendered first time, zero failures

Unlike the previous reel in this series, nothing crashed and nothing had to be replaced.
That is a direct consequence of carrying its QC findings forward — see § Lessons applied.

## Per-beat measurement (per-beat renders, frame at 94% of span)

| Beat | Composition | ink x | ink y | coverage | verdict |
|---|---|---|---|---|---|
| B00 | `ClaudeComposerAsk` | 306 – 3532 | 224 – 2009 | 0.86 | CLEAN |
| B01 | `JdgDiverge` | 301 – 3644 | 171 – 2043 | 0.93 | CLEAN |
| B02 | `JdgSplit` | 191 – 3644 | 130 – 2043 | 0.98 | CLEAN |
| B03 | `ClaudeComposerAsk` | 306 – 3532 | 224 – 2009 | 0.86 | CLEAN |
| B04 | `JdgOptions` | 193 – 3644 | 130 – 2043 | 0.98 | CLEAN |
| B05 | `JdgBranch` | 301 – 3644 | 171 – 2043 | 0.93 | CLEAN |
| B06 | `JdgStakes` | 192 – 3644 | 130 – 2043 | 0.98 | CLEAN |
| B07 | `ClaudeVerdictArtifact` | 442 – 3359 | 581 – 1648 | 0.46 | MAJOR underfill |
| B08 | `ClaudeComposerAsk` | 306 – 3532 | 224 – 2009 | 0.86 | CLEAN |
| B09 | `ClaudeTitleOutro` | 1242 – 2595 | 934 – 1208 | 0.06 | MAJOR underfill |

Safe area is x 192–3648, y 108–2052 at this canvas. **Maximum ink on any beat is
x = 3644 against a right edge of 3648 — zero edge-bleed, on every beat.** All five body
beats clear Gate V's 0.55 canvas-fill floor with room (0.93–0.98).

## Lessons applied from the previous reel (why this pass was clean)

1. **The three quantitative deckPatterns scenes were excluded up front.** Last reel,
   `ScaleComparison` crashed the render, `AttritionChain` printed "1 / 100" and "1%
   remain", and `Threshold` printed a numeric axis. All three are structurally incapable
   of respecting a no-numbers constraint, so none was used here.
2. **The safe-area mapping was in place before the first render**, extracted into
   `scenes/claudeStage.tsx` (`SafeStage`). Last reel this was discovered by finding label
   boxes at x≈3792; here B01 measured x_max = 3644 on its very first render.
3. **`BinaryBranch` strings were kept short by design.** Last reel's QC found it overflows
   fixed-width boxes with sentence-length copy, so B05's branch labels, details and
   resolver were written to fit.
4. **`ClaudeTitleOutro` was given `subline: ""` from the start.** Last reel it rendered
   Musinique's default "bot vs bot, season one" because the beat passed a `slug` prop the
   component ignores.
5. **The inner composer beat got a spark line from the start** (`"Every concept."`),
   rather than tripping SKIN LINT's SPARK-LINE LAW check.
6. **Motion languages were labelled accurately** (`diverge / ledger / populate / branch /
   reveal`), so MOTION.md's ~40% per-language cap is not tripped. Last reel labelled five
   distinct motions "illustrate" and hit 50%.

## Risks that were carried into QC and how they resolved

- **`JdgOptions` label wrapping at 28px across a 4×3 grid** — RESOLVED. All twelve labels
  fit on one line; nothing clips or wraps. Coverage 0.98.
- **`JdgStakes` row crowding across four rows at 44px + 28px** — RESOLVED. Rows sit clear
  of one another with the closer line well separated. Coverage 0.98.

## Accepted, not fixed

- **`underfill` on B07 (0.46) and B09 (0.06).** Identical to the previous reel and accepted
  for the same reason: both are *shipped fidelity components* — a Claude artifact page and
  a poster-style title card — whose generous whitespace is the Claude app's own design.
  FILL-THE-CANVAS LAW and the FIDELITY rule ("do not retint it, theme it, or improve it")
  conflict here, and the fidelity rule is the more specific. Every beat this reel authored
  clears the floor.
- **Mono labels in the two reused deckPatterns scenes (B01, B05).** The claude type stack
  reserves mono for terminal/output lines. Fixing it means editing a file shared with other
  reels or forking the patterns. The three purpose-built scenes use
  `CLAUDE_FONT.serif`/`.ui` correctly.
- **Two terracotta elements on B05**, from `BinaryBranch`'s own tone mapping (the `warn`
  branch plus the resolver), softening "one terracotta moment per beat".
- **Model chip in the composer chrome.** `ClaudeComposerAsk` renders a model name
  (currently "Fable 5") in its chrome on B00/B03/B08. Component chrome, never referenced by
  narration; means the bookends date faster than the body. Logged in `FACTCHECK.md`.

## Gate V's blanket `edge-bleed` BLOCKERs remain a toolkit false positive

Established on the previous reel and unchanged: Gate V inspects the `--review` cut and
flags **the review burn-in that `compile.py --review` deliberately draws top-right**.
`final_frame_check.py`'s `BURN_IN_EXCLUDE = (0.0, 0.94, 0.60, 1.0)` masks only the bottom
strip, so the exclusion never applies. On this toolkit Gate V cannot pass any reel.

The measurements in the table above were therefore taken from the **per-beat renders and
the clean master**, not the review cut, and they are the numbers that describe the
delivered file. Suggested upstream fix: run Gate V against the clean cut, or widen
`BURN_IN_EXCLUDE` to cover the top-right label.

## Blocked by the toolkit, not by this reel

- **GATE T never ran** — `type_check.py` is not shipped anywhere in this tree, though the
  skill calls it "ALWAYS RUN". Type sizes checked by eye against the ~24px floor; the
  smallest type on any authored beat is the 22px eyebrow, with body labels at 28–44px.
- **The outro mascot clause cannot be satisfied** — `ClaudeMascotScene`/`ClaudeMascotGrid`
  are absent and `ClaudeTitleOutro` renders no mascot. PIXEL-ART LAW is moot: there are no
  pixel-art rects. Stated in the beat's `show` block rather than faked.
- **`OUTRO-LOCK.md`, `AUDIT-MODE.md`, `DESIGN-PRINCIPLES.md`** are referenced by the skill
  and none ship here; their rules were followed as quoted inside `SKILL.md`.

## Constraint audit (no invented statistics)

A numeral sweep over every on-screen string ran before the first render. One hit: "my last
**5** pieces" in B08's handoff prompt — a quantity in an instruction the viewer pastes
about their own work, not a claim about the world. Kept deliberately and justified in
`FACTCHECK.md`. Everything else on screen is ordinal or worded.

## Audio

Verified independently before compositing: 10/10 files present, mean volume −23.1 to
−24.5 dB against a −40 dB floor, durations matching the beat sheet exactly. Each
composition's `durationInFrames` equals its beat's measured length × 30fps, so every slot
conformed without a retime or freeze-pad.

---

## Delivered master — verification

`claude-liam-the-judgment-is-the-job.mp4` · 3840×2160 · h264 · 24fps · AAC ·
149.41s (2:29) · 7.6 MB · mean −24.1 dB, max −0.6 dB (no clipping).

Gate V's `analyze_frame` run against **the clean master** at ten points across the reel:

| t | x_max / 3648 | coverage | verdict |
|---|---|---|---|
| 6s | 3532 | 0.86 | CLEAN |
| 20s | 3644 | 0.93 | CLEAN |
| 36s | 3644 | 0.98 | CLEAN |
| 52s | 3532 | 0.86 | CLEAN |
| 62s | 3644 | 0.98 | CLEAN |
| 78s | 3644 | 0.93 | CLEAN |
| 96s | 3644 | 0.98 | CLEAN |
| 112s | 3359 | 0.46 | underfill (B07 verdict card — accepted) |
| 132s | 3532 | 0.86 | CLEAN |
| 146s | 2595 | 0.06 | underfill (B09 title outro — accepted) |

**edge-bleed on the delivered master: 0 / 10 frames.** 8/10 CLEAN. The only two flags are
the accepted underfills on shipped fidelity bookends.

Compile was clean: 10/10 slots VIDEO, zero slates, no SKIN LINT warnings, and the motion
histogram (type-on 3 · diverge · ledger · populate · branch · reveal · stagger · fade)
stays under MOTION.md's per-language cap.

Not published. Master remains in the reel folder.

---

# REVISION — narrator Yatra, voice Bella, and a 9:16 derivative

## What changed and why

1. **Narrator: Liam → Yatra.** Still the IN-FOR-BEAR LAW stand-in pattern on Bear's
   channel, just with a different name: B00 says "this is Yatra, in for Bear", the outro
   signs off the same way, the greeting reads "Namaste, Yatra", and the footer chip and
   outro handle remain `@NikBearBrown`. Wagwan is untouched — a stand-in never takes it,
   whatever the slug's charsum says.
   *Caveat recorded:* the skill's channels table has no `claude-yatra` row. This is the
   documented stand-in pattern applied with a new name, not a new channel. Making it
   official would mean adding a table row to the skill.
2. **Voice: Kokoro `am_onyx` → `af_bella` ("Bella").** This is the only female voice the
   toolkit permits: `generate_audio_kokoro.py` hard-enforces
   `ALLOWED_VOICES = {"am_onyx", "af_bella"}` and rejects anything else, even though the
   Kokoro model file itself ships eleven `af_*` voices.
3. **Narration trimmed ~20% on the wordy beats.** Not cosmetic — see below.

## The duration problem Bella caused, and the fix

Bella speaks slower than Onyx. With the original narration the reel came out at
**180.02s**, i.e. **0.02s over the hard 3:00 YouTube Shorts cap**. That matters because
`shorts.py` responds to going over the cap by *cutting beats* from the portrait version —
so the two sizes would no longer have been the same video, and the reel would also have
broken the 1–3 minute brief.

Fixed the doctrine way: **regenerate audio, never hand-tune timing.** Trimmed the eight
wordiest beats (B00–B08) by roughly 20% of their words, holding every body beat inside the
45–70 word budget and preserving all four of the requested subject areas.

| | Onyx (original) | Bella (untrimmed) | Bella (trimmed — delivered) |
|---|---|---|---|
| Total | 149.41s (2:29) | 180.02s (3:00.02) | **160.27s (2:40)** |
| vs Shorts cap | under | **OVER by 0.02s** | under by 19.7s |

New measured per-beat durations, and every composition re-registered to match
(`durationInFrames` = measured seconds × 30):

```
B00 12.65s/380f   B01 19.41s/582f   B02 19.95s/598f   B03  6.78s/203f   B04 17.15s/514f
B05 19.58s/587f   B06 16.34s/490f   B07 21.06s/632f   B08 19.71s/591f   B09  7.64s/229f
```

## The 9:16 cut is a relayout, not a resize

`shorts.py` never centre-crops a generated graphic — a crop chops text mid-word. It looks
for a portrait composition named `<pattern>916` and rewires the short's sheet to it. The
Claude bookends already had portrait variants (`ClaudeComposerAsk916`,
`ClaudeVerdictArtifact916`, `ClaudeTitleOutro916`); the five illustration scenes did not,
so they were authored: `runtime/remotion/src/scenes/JudgmentIsTheJob916.tsx`.

These are **not scaled clones**. The Shorts law's composition logic — "16:9 lays out SIDE
BY SIDE; 9:16 stacks TOP AND BOTTOM" — is applied per scene:

| Beat | Landscape | Portrait re-band |
|---|---|---|
| B01 | two diverging tracks | two **stacked** outcome bands |
| B02 | two side-by-side ledger columns | two **stacked** sections |
| B04 | 4 across × 3 down concept wall | **3 across × 4 down** |
| B05 | branches splayed left/right | branches **stacked** vertically |
| B06 | four rows | four rows, re-spaced for the taller box |

**Shorts UI keep-out.** `layout.ts` warns the Shorts chrome covers roughly the bottom ~25%
and right ~11% of the frame at runtime, so the portrait scenes work inside a tighter box
than SAFE916 (x 54–1026, y 96–1824) would allow: content stays left of x≈960 and above
y≈1440. The `@NikBearBrown` corner bug also moves to the **lower-left** in portrait,
because lower-right is where the Shorts UI sits.

## Still outstanding after this revision

- The reel folder and output filenames still read `claude-liam-…` — the slug predates the
  narrator change. Renaming would change the delivered filenames, so it was left alone
  rather than done silently.
- The sibling reel `claude-liam-the-bottleneck-moved` had its beat sheet and all ten mp3s
  switched to Yatra/Bella before scope narrowed to this reel. Its `.mp4` was never rebuilt,
  so **its delivered master still has Liam and Onyx while its sheet says Yatra and Bella**.
  It is inconsistent and needs either a rebuild or a revert — flagged, not hidden.

---

# REVISION 2 — @Yatra channel, and a self-introducing Beat 2

## 1. Beat 2 now introduces the narrator by name

B01 (the EXECUTIVE-SUMMARY / BLUF beat) opens **"Hi, I'm Yatra, and this video is about
what AI actually did to advertising."** then states the whole idea in one breath. This is
compatible with EXECUTIVE-SUMMARY LAW rather than a departure from it — the law asks Beat 2
for "what is this video about, and why should I care", and a named self-introduction just
makes the frame explicit.

Consequence: **B00 no longer introduces the narrator.** It previously carried
"this is Yatra, in for Bear" in its first breath. Keeping that *and* adding "Hi, I'm Yatra"
one beat later would introduce the same person twice in fifteen seconds, so B00 now opens
straight on the hook and Beat 2 owns the introduction.

*(A reference video was supplied for style. It was not used, because video cannot be
watched — the pattern was implemented from the human's written spec instead. Recorded here
so nobody assumes the reference was matched by observation.)*

## 2. Channel handle: @NikBearBrown → @Yatra

Every on-screen handle changed: the composer folder chip on **B00, B03, B08**, the outro
handle on **B09**, and the LOGO LAW corner bug on every illustration beat in both
orientations (`scenes/claudeStage.tsx` landscape, `scenes/JudgmentIsTheJob916.tsx`
portrait).

**This ends the IN-FOR-BEAR framing, and that is a real doctrine change, not a cosmetic
one.** "In for Bear" only means something on Bear's channel. Once the handle stopped being
`@NikBearBrown`, the phrase became false, so it was removed from B00 and B09; B09 now signs
off "I'm Yatra — thanks for watching."

So this reel is no longer the documented stand-in pattern — it is a **new channel**
(`claude-yatra`), and the skill's channels table defines no such row. Making it official
means adding one, with its own register and audience line. Until then this reel is
correct-but-undocumented at the skill level, which is why it is written down here.

The alternative offered was `@HumanitariansAI`; `@Yatra` was chosen because it matches the
new "Hi, I'm Yatra" self-introduction. Switching is a one-line change in the beat sheet
plus the two LogoBug defaults.

## 3. Timing after the rewrite

| Beat | Was | Now | Reason |
|---|---|---|---|
| B00 | 12.65s | 10.90s | self-intro moved out to B01 |
| B01 | 19.41s | 21.21s | gained the "Hi, I'm Yatra…" frame |
| B09 | 7.64s | 8.02s | new sign-off |
| **Total** | **160.27s** | **160.70s (2:40.7)** | still **19.3s under** the 3:00 Shorts cap |

`JdgDiverge` / `JdgDiverge916` re-registered 582 → **636 frames** to match B01's new
measured length. B00, B09 and B03/B08 are Claude bookends registered at fixed durations,
which `compile.py` conforms to the measured audio.

B07 was NOT re-rendered: its content and duration are unchanged and it carries no handle.
