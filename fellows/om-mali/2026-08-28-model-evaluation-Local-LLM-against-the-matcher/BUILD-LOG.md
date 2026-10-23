# BUILD-LOG — measuring-a-local-llm-against-the-matcher (week 5)

Built with **brutalist.art** (`ai-explainer`, channel `claude-hai`). Free/local throughout:
Kokoro TTS + Remotion + ffmpeg. **$0.00 spent. No API key used.**

Fourth episode of the Private AI Valuation Agent series (week 1 → 2 → 4 → 5; there is no
week 3 episode). **First episode shipped in both orientations.**

---

## Where the inputs came from

| File | Origin | Status |
|---|---|---|
| `narration_script.md` | `mycroft/data/raw/Private_AI_Valuation_Agent/docs/video_script_week5.md` | **copied** in, unmodified — the Mycroft copy was left alone |
| `figdata_week5.json` | Already in this folder | **the source of truth for every on-screen number** |
| `README.md` | Already here — the figure-to-beat map, the two corrections, the colour note | input, unmodified |
| `pantry/w5-*.png` + `.svg` | Already in `pantry/` | REFERENCE only, never slotted (REBUILD LAW) |

`README.md` states the pantry rule explicitly — do not slot these and do not copy them into
`images/`, because the toolkit writes compile output there. Observed.

---

## Every number is injected, and eight groups are asserted

`build_beat_sheet.py` plots `figdata_week5.json` directly; no figure is typed into a scene or
a beat sheet by hand. The assertions run at injection and fail the build if violated:

```
run.parameter_size == "8.0B"                       # the claim is an 8B model
run.temperature == 0 and run.seed == 7             # deterministic
throughput.calls_measured == 322 and errors == 0
prompt_example.candidates == 11                    # 7 universe + 4 watchlist, NOT 7
micro fp: matcher 1 -> band 196                    # the record count
band_changes: promotions == broke == 14, fixed == 1
confidence.at_full == 315, disagrees_at_95_plus == 12
len(veto_rows) == 4 and exactly one vetoed
```

Two of these exist because the PROSE was wrong until a generated figure disagreed with it.
`README.md` records both: confidence was 1.000 on **315** answers, not 308, and the model was
offered **11** candidates, not 7. Neither error was caught by reading; both were caught by a
figure that generated its own counts. The assertions move that check to build time.

`python build_beat_sheet.py --check` runs the assertions and writes nothing.

---

## Decisions taken during the build

| # | Decision | Why |
|---|---|---|
| 1 | **Five script sections → eight body beats.** | The 1:00 section carried three failure examples, and the script's own shot note asks for "one example per beat" and for the Fidelity code to "sit on screen alone". Split into B04/B05/B06 exactly as asked. The other sections carry one idea each and stay whole. |
| 2 | **The Scaled Agile example was KEPT.** | The script offers it as the first cut if the reel runs long. It is the example where the cost jumps from 1 holding to 32, which is the evidence B03's records argument rests on. The bookends are additive here, so the cut-for-time reason did not apply. |
| 3 | **"Last month's 322 test cases" → "the same 322 labelled names".** | DOUBLE-CHECK LAW: strip what dates the video. Week 4 shipped the same month. Same referent, no date claim. |
| 4 | **An on-screen qualifier was added to 1 → 196.** | Spoken alone, "one wrong record becomes 196" reads as a 196× multiplier on a single error. It is 14 wrong NAMES carrying 196 holdings. The narration is unchanged; the screen carries "a case is a name and a name can carry hundreds of holdings". |
| 5 | **B08's holding names shortened at the exposure clause.** | The real strings run to 138 characters. Rendered in full they cross the right title-safe edge and overprint the notes beneath — the exact BLOCKER week 4 hit at B08. The truncation is disclosed in the on-screen source line, and the trailing-space distinction between rows 3 and 4 survives as a row note rather than being silently collapsed. |
| 6 | **The flattering hardest-cases 100% is excluded entirely.** | The script's note is explicit: that subset excludes the rows where nothing should match, and those are the only rows the model damages. True and misleading at once. It is in `FACTCHECK.md` and nowhere on screen. |
| 7 | **The veto beat runs LAST, not first.** | It is the one positive result. Putting it after every failure, with the sample size at the same visual weight as the 1.0000 and a SWITCHED OFF stamp across it, is what stops the episode becoming a silver-lining cut. |
| 8 | **Greeting rotated to `Hallo, HAI`.** | Week 1 `Ola`, week 2 `Hej`, week 4 `Ciao`. German short form; the lexicon rotates so the series never repeats a language. |
| 9 | **Kicker is `Irreducibly Human`.** | GATE L rule 7 — the fixed `claude-hai` series name. Set at authoring time, so GATE L passed on the first run for the third episode running. |
| 10 | **`MeasuringLocalLlm.tsx` is self-contained.** | Same reasoning as weeks 2 and 4: reel-local files duplicate the chrome helpers so the earlier signed masters stay re-renderable byte-identically. |

---

## Both orientations, from one source

New this week, at the author's request: **16:9 at 3840×2160 and 9:16 at 2160×3840.**

The vertical cut is a **re-layout, not a crop.** Every week-5 component reads its orientation
from `useVideoConfig()` and every value that differs goes through one helper,
`f(landscape, portrait)`. Side-by-side pairs become stacked; the 322-dot grid goes from 26
columns to 18; type is re-sized rather than scaled down. Both orientations render from the
**same component and the same props**, so a number cannot differ between the two masters.

`make_vertical.py` derives `vertical/beat_sheet.json` from the 16:9 sheet: it flips
`aspect_ratio`, suffixes the slug, and rewires every `shot.remotion.pattern` to
`<pattern>916`. It **refuses to run** if any pattern lacks a portrait registration in
`Root.tsx` — a landscape render centre-cut into a portrait frame is not a vertical cut, and
silently producing one is the failure mode worth blocking.

The narration mp3s are **copied, not regenerated**, so the two masters are the same edit to
the frame. `lock_durations.py` measures the mp3s with ffprobe and writes the measured seconds
into both sheets.

The eight body components are registered twice in `Root.tsx` under the toolkit's existing
ONDA-CHECK naming (`<pattern>916`), so `shorts.py` will find them too.

---

## Toolkit defects found and fixed

The week 5 narration is the first in this series to contain a **curly quotation mark**
(U+201D, in B09's verbatim quote of the model's reason). That one character exposed a family
of latent Windows bugs: `0x9D` is **undefined** in cp1252, so instead of round-tripping into
mojibake the way an em dash does, it raised `UnicodeDecodeError` and killed the run outright.

| File | Defect | Fix |
|---|---|---|
| `runtime/scripts/generate_audio_kokoro.py` | Read AND wrote the beat sheet with the ANSI codepage. The write used `ensure_ascii=False`, so on any earlier reel it silently re-encoded mojibake back to the same bytes and looked fine. | explicit `encoding="utf-8"` on 5 sites |
| `runtime/scripts/run.sh` | The inline `HAS_MANIM` probe opened the beat sheet unencoded | `encoding='utf-8'` |
| `align.py`, `brand_variant.py`, `build_cli_d3_reels.py`, `fill_slates.py`, `pantry.py`, `provenance.py`, `shorts.py`, `qc/static_scene_check.py`, `qc/manim_layout_audit.py` | Same defect, same class — 14 further read/write sites, none of them in this reel's path but all of them one non-ASCII character away from the same failure | explicit `encoding="utf-8"` |

One more, found by looking at the portrait frames: **`ClaudeVerdictArtifact916` silently
dropped content.** The card's height is content-driven and nothing clipped it, so a five-clause
recap grew past the bottom of the 1920px frame and the fifth finding — the pre-commitment, the
line the whole episode is about — was simply not on screen. It now estimates the wrapped row
count and shrinks the line type only as far as needed to fit. Content that already fits keeps
scale 1.0 exactly, so the three-line reels that use this component render unchanged.

Also added, minimally: `calculateMetadata={durationFromProps(...)}` on `ClaudeVerdictArtifact916`
and `ClaudeTitleOutro916`, with fallbacks equal to their existing registered lengths (12s and
6s) so any reel that does not pass `durationInSeconds` renders exactly as it did before.

**One toolkit footgun worth knowing, not fixed.** `remotion_scenes.py` loads the beat sheet at
the start of a run and rewrites it at the end. On a 25-minute render, any edit made to the
sheet in the meantime is silently overwritten. It cost one round of rework here (a legend prop
added mid-render was lost) and was recovered by re-running `build_beat_sheet.py` and
`lock_durations.py`. Both scripts are idempotent, which is why the recovery was free.

---

## Visual QC — what LOOKING at the frames caught

GATE V's first pass on the 16:9 cut reported **0 BLOCKER, 0 MAJOR**. Reading the frames found
three defects the gate could not see, one of them a wrong number on screen.

| Beat | Defect | Severity | Fix |
|---|---|---|---|
| B07 | All 15 disagreements rendered as solid terracotta, so the 3 the model was **unsure** about looked identical to the 12 it was sure about — the frame asserted a stronger claim than the data supports | **MAJOR, missed by GATE V** | Confident errors stay solid; unsure ones render hollow. A four-item legend was added so the encoding reads without the narration. |
| B02 | "3.24s mean per call" rendered as **"3s"** for most of the beat — the count-up ran the value through `fmt()`, which rounds | **MAJOR, missed by GATE V** | Only whole-number stats count up now. |
| B03 | "1 wrong cases" | MINOR | Singular when the count is 1. |
| B04 (portrait) | **The strike-through never drew.** The quoted reason wraps to two lines in portrait, and an absolutely-positioned rule inside an inline span only covers the FIRST line box — so "that is not true" never happened on screen | **MAJOR, portrait only, missed by GATE V** | `Struck` re-implemented as a background gradient with `box-decoration-break: clone`, which repeats and grows per line box. Survives any wrap, in either orientation. |
| B01 (portrait) | Five blocks distributed across the 1728px portrait safe box read as thin bands with large empty gaps | MINOR (portrait only) | Portrait type sizes raised — the vertical cut gets bigger type, not more gap. |
| B02, B04, B06 (portrait) | Body type sat around 2% of frame width — legible on a monitor, thin on a phone, which is the whole point of the vertical cut | MINOR (portrait only) | Portrait sizes raised ~15% on the three thinnest scenes; B06's character slots 62 → 72px. |
| B09 (portrait) | **The fifth verdict line was off the bottom of the frame** — the pre-commitment, which is the point of the episode | **BLOCKER, portrait only, missed by GATE V** | `ClaudeVerdictArtifact916` now fits its type to the content instead of letting the card grow past the frame. See the toolkit section above. |

**GATE V's blind spot, third episode running.** The gate checks edge bleed, canvas fill and
contrast. It does not check text-on-text overlap (week 1 B03, week 4 B02) and it cannot check
whether a number on screen is the RIGHT number (week 5 B02). A clean report is not evidence
that the frames are correct; reading them is.

---

## Gates

| Gate | State |
|---|---|
| **FACTCHECK** | 20 rows, all traced. **Rows 3, 9, 13 and 18 flagged** — the 11 candidates, the micro-vs-macro record count, the one rebuttal resting on author knowledge rather than an artifact, and the 12-of-15 confidence finding. |
| **PROOF GATE / CHECKS-REPORT** | PASS — 8 SHOW / 4 justified-HOLD / 0 PUNT. Teaching arc 6/6. Written before the first compile. |
| **GATE P (pedagogy)** | **PASS — signed by the author (Om Mali), 2026-08-28**, after reviewing the slate cuts. Covers the three-way split of the failures section, keeping the Scaled Agile example the script offers to cut, the four wording changes, FACTCHECK rows 3/9/13/18, excluding the flattering hardest-cases 100%, the B10 handoff prompt, and the dual-orientation build. Audio for the pre-signature review cut was generated with `--no-gate`, recorded here rather than passed silently; the gate was re-run WITHOUT the override after signing and passes on its own. |
| **GATE L** (beat-mix lint) | PASS on the first run. |
| **GATE V** (frame-level visual QC) | PASS on BOTH masters, re-run against the 4K files themselves rather than the review cuts — 16:9: 24 frames, 0 BLOCKER, 0 MAJOR. 9:16: 24 frames, 0 BLOCKER, 0 MAJOR. |
| **GATE F** | Not triggered — no Manim beats. |

**One advisory, not a gate.** `compile.py` warns that `illustrate` carries 8 of 12 beats (66%)
against a ~40% cap. That cap is written for reels built from pantry media, where too much
`illustrate` means too many stills being panned. Every body beat here is a native animated
Remotion scene with its own scheme, which is what the ILLUSTRATE LAW asks for. Weeks 2 and 4
carried the same shape.

---

## Build facts

- **12 beats**, all filled by Remotion. Zero slates.
- **Audio**: Kokoro `am_onyx` (the fellow's persistent voice, unchanged since week 1),
  **215.11s narration + 0.40s lead = 215.5s (3:35.5)**. The same mp3s drive both orientations.
- **Eight reel-local scenes**, eight different visual schemes, each laid out natively at both
  1920×1080 and 1080×1920. No two consecutive body beats share a scheme (ILLUSTRATE LAW).
- **Body beats 51–67 words** — all eight inside the 45–70 band.
- **This is a negative result and the cut refuses to soften it.** The verdict is spoken in the
  cold open, the one positive finding runs last with its sample size beside it, and the
  flattering number is left out on purpose.
- **Never published.** The masters stay in this folder. Publishing is a separate, explicitly
  human-authorized step that this toolkit does not perform.

---

## Finalization (2026-08-28)

GATE P signed. Three things before the masters were stamped:

1. **Staleness proved per BEAT, not per file — and not by argument either.** File mtimes
   flagged 10 of the 24 renders as stale, because `MeasuringLocalLlm.tsx` was edited after
   them. Every one of those edits changed only the PORTRAIT argument of
   `f(landscape, portrait)`, so most of the flags were false. Rather than assert that from
   memory, each flagged beat was re-rendered as a single still from the current source and
   diffed against the shipped frame at native 4K.

   The first two attempts at this measurement were wrong and are worth recording: comparing a
   scale-1 still against supersampled-then-downscaled video differs at every glyph edge and
   proves nothing, and even at matched resolution an absolute threshold is a guess against
   h264 ringing. What made it conclusive was adding **controls** — two beats known to be
   current. They scored 0.126% and 0.287% differing pixels; every flagged beat scored
   0.153–0.744%, i.e. inside the control band. The one high reader (B08, the densest frame in
   the reel) was localised: its differing pixels spread across 20 of 36 grid cells wherever
   text sits, with no hot/cold cluster pair, which is compression ringing rather than a moved
   element. **Nothing needed re-rendering.**

2. **GATE P re-run without the override.** `generate_audio_kokoro.py --dry-run` passes the
   PEDAGOGY check on its own now. `--dry-run` deliberately: regenerating the audio would shift
   the measured durations by milliseconds and invalidate every render against them.

3. **`mp4/` refreshed by hand.** `./art final` writes only the master, so the mirrors go stale
   every week. Same step weeks 1, 2 and 4 needed.

GATE V was re-run against the two 4K masters themselves: **24 frames each, 0 BLOCKER,
0 MAJOR.**
