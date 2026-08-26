# QC REPORT — Where the Record Stops

Week 19 work video · Humanitarians AI · Tanmay Kulkarni · 2026-08-26

---

## Deliverables

| File | Aspect | Resolution | Duration | Verified |
|---|---|---|---|---|
| `2026-08-25-where-the-record-stops.mp4` | 16:9 | **3840 × 2160** | 287.95s (4:47.9) | `ffprobe` |
| `2026-08-25-where-the-record-stops-short.mp4` | 9:16 | **2160 × 3840** | 101.21s (1:41.2) | `ffprobe` |

Both are **clean masters** — no slate, no review burn-ins — and both are the **paced** cuts.
Audio 24 kHz on both, matching Kokoro's output rate.

## The Short is a trailer, not a shortened film

Per reviewer direction: a Short should be a glimpse that makes someone want the long cut,
delivering value inside ~2:00 — not the same film compressed.

`shorts.py`'s auto-planner drops the **longest** unprotected middle beats until the cut fits
under the 3:00 cap. Left alone it would have produced a ~2:52 shortened film. The drop plan
was therefore driven explicitly:

| | |
|---|---|
| Kept | B01 hook · B03 framework · B07 the blank · B08 fail open · B13 outro |
| Dropped | B02, B04, B05, B06, B09, B10, B11, B12 |
| Result | 5 beats + endcard, **1:41.2** |

The trailer never names DBS in narration, so it makes no claim about them; the non-claim
rides on the endcard instead — *"Not DBS's system — built from what they published."* The
thesis line survives verbatim: *"Where the record stopped, I stopped."*

Every kept beat reuses the parent's audio unchanged. The outro is the only regenerated audio,
per the Shorts Law.

## Resolution chain — every stage at 4K

| Stage | Result |
|---|---|
| Remotion beats, 16:9 | 3840 × 2160 (comps 1920×1080, `--scale=2`) |
| Remotion beats, 9:16 | 2160 × 3840 (comps 1080×1920, `--scale=2`) |
| `compile.py` 16:9 | `--height 2160` |
| `compile.py` 9:16 | `--height 3840` |
| Silent endcard PNG | 2160 × 3840, `--end-height 3840` |

---

## Defects found and fixed

### 1. `ClaudeCodeBeat` silently clipped code in portrait — **FIXED**

Caught by rendering portrait *before* authoring the beat sheet. Five of twelve lines lost
their right-hand end, including the sentence B08 exists to show. Two causes in the shared
component:

- `fontSize: height * 0.022` — portrait height is 1920, so code got a **larger** font in a
  **narrower** column than landscape. Backwards.
- `whiteSpace: 'pre'` with `overflow: 'hidden'` — long lines clipped rather than wrapped, with
  no warning.

Fixed: font scales from `Math.min(width, height)`, lines use `pre-wrap` +
`overflowWrap: anywhere`. Landscape is visually unchanged (0.026% of subpixels differ,
sub-pixel repositioning only). **Authoring rule this created:** portrait fits roughly half the
characters per line — every code line in this film is under ~46 characters.

### 2. A hardcoded display string leaked between films — **FIXED**

B12's badge strip rendered **"WHAT THE LABEL ACTUALLY SAYS"** — the Tunefind-specific header
baked into `SyncSendChecklist` for the *topic* video, meaningless above this film's three
columns. Made `badgeHeader` a prop defaulting to the original, so the topic video is
untouched. A follow-up pass caught the replacement duplicating the footer note.

### 3. An internal bookkeeping note was read aloud — **FIXED**

The Short's auto-rewritten outro said *"The full video also covers **load-bearing —
protected from Short drops**…"* — because `beat_topic()` reads
`graphic.production_viz.label`, where a hero-protection note had been parked. All 13 labels
replaced with real 2–5 word topics, and the trailer outro hand-written rather than
auto-generated.

**Third instance this week of the same root cause** — after the Anthropic credit and the
badge header. Any field a component or script *may* render must be treated as viewer-facing.

### 4. The endcard's silence was 44.1 kHz against Kokoro's 24 kHz — **FIXED at source**

The paced trailer first reported **178.8s** for a 97-second cut — exactly ×1.8375, or
44100/24000. `pacing_pass.py` concatenates with stream copy, so one mismatched segment made
the whole track reinterpret at the wrong rate. `compile.py` had been hiding it by re-encoding.

This defect was already written into PLAYBOOK §6 after the topic video — but fixed there only
in that film's output file, never in `shorts.py` itself. Now fixed at source: the endcard
silence is generated at the reel's own sample rate.

### 5. B12's artifact arrived after the claim it supports — **FIXED**

The narration names the three columns at **4.6s**; the badge strip was landing at **6.0s**.
Moved to 3.4s. This defect only exists once measured audio replaces the estimate — the
pre-audio pass could not have seen it.

### 6. B04 asserted DBS's facts with no citation in frame — **FIXED**

Review 1's production-gate failure, and the one this film could least afford. `BuildLedger`
had no source field at all; a grep found exactly one citation in the entire film. Added an
optional `sourceNote` (empty by default, so B03/B06/B11 are unchanged) and set B04 to
*"DBS newsroom release, 19 August 2026"*. Verified on frame at 85.0s.

### 7. B10's stage names could read as DBS's — **FIXED**

Footnote now reads *"My decomposition, not DBS's. Discovered by running it, not by drawing
it."* One prop, no component change.

---

## Truncation check

Six beats run shorter than their composition and are cut off mid-animation by
`remotion_scenes.py`: **B01 at 42%** of its animation, B02 95%, B03 69%, B04 71%, B06 70%,
B10 62%. Every one was sampled at its final frame and is **fully formed** — reveals complete
in the first 2–3s and the rest is hold.

Worth checking rather than assuming: this is the mechanism that silently deleted the topic
video's payoff frame when a timing prop was expressed as a fraction of the composition
instead of absolute seconds.

## Pacing

`compile.py` has no transition mechanism, so holds are a post-compile pass (PLAYBOOK §5).

| Cut | Default hold | Overrides |
|---|---|---|
| 16:9 | 0.60s × 12 | **1.10s on B07, B08, B09** |
| 9:16 | 0.50s × 5 | 0.90s on B07, B08 |

The overrides exist because those are the three consecutive **code** beats — the viewer is
reading a file, not hearing a sentence. `pacing_pass.py` only supported a uniform `--hold`,
which under-serves dense beats and pads sparse ones; `--hold-for BID=SECS` was added for this
and is reusable.

**Re-run the pacing pass after any recompile** — `compile.py` overwrites the unpaced master.

## Audio

13 beats, Kokoro `am_onyx`. Voice chosen for the peer-conversation register and consistent
with the repo's own male-coded-name default; the series has used both `am_onyx` (3×) and
`af_bella` (4×) previously, so this is within precedent rather than a re-voice.

Onyx runs **~37 wpm faster than Bella at identical nominal speeds** — the conviction peak
initially landed at 238 wpm, faster than the film's own average, which is backwards for a
beat meant to slow down. Per-beat speeds were recalibrated before rendering: B07 202, B08
182, B11 174, B13 161. `silencedetect -40dB:d=0.55` across all 13: clean.

## Frame QC

Sampled at **85–90% of each beat's own duration**, and separately at the **moment of each
assertion** for the eight claim beats (PLAYBOOK §4).

- `qc-sheet-16x9.png` — 13 beats
- `qc-sheet-9x16.png` — 5 beats + endcard

Confirmed by eye in both aspects: the non-claims card, the ledger filling across four beats
with the right groups dimmed, B05's quote and full attribution, all three code beats legible,
B11's straddling row with its *"reasoned, never demonstrated"* note, B12's questions and
columns, the trailer's endcard handle and non-claim line. No clipping, no overlap, nothing
below readable opacity.

## Known deviation — accepted

**`remotion` carries 13/13 beats (100%)**, over MOTION.md's ~40% cap. Same as the topic video.
Accepted and recorded rather than gamed: the histogram keys off `shot.motion`, so adding
motion strings would silence the warning without changing anything. Three of the thirteen
beats are real code on screen, which is arguably a stronger case here than in the topic video.

**Two films in a row now sit at 100%.** Per the topic video's own note, that makes it a house
pattern rather than a per-film choice, and it should be addressed in the next build.

## Ship status

Teaching **12/12** (bar 8). Production gate **PASS** in both aspects, re-run on rendered
frames after the punch list. **Clear-for-public.**

Both cuts watched end to end by a human before this was called done. Not published —
publication is a separate decision and the toolkit has no publishing machinery.
