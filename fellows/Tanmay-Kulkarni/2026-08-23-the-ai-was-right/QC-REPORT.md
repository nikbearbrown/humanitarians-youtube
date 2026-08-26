# QC REPORT — The AI Was Right. That Was the Problem.

Week 19 · Humanitarians AI · Tanmay Kulkarni · 2026-08-23

---

## Deliverables

| File | Aspect | Resolution | Duration | Verified |
|---|---|---|---|---|
| `2026-08-23-the-ai-was-right.mp4` | 16:9 | **3840 × 2160** | 176.78s (2:56.8) | `ffprobe` |
| `2026-08-23-the-ai-was-right-short.mp4` | 9:16 | **2160 × 3840** | 177.88s (2:57.9) | `ffprobe` |

Both are **clean masters** — no slate, no review burn-ins. `compile.py` refuses slates in a
clean master by default and reported `10/10` and `11/11` slots filled with `VIDEO`.

The Short is the 16:9 master's derivative cut: same beats, same audio, **no beats dropped**,
plus a 3.0s silent endcard (trimmed from 4.5s to buy pacing headroom). Two things differ in
runtime: that endcard, and the per-aspect hold — 0.60s on the long cut, 0.35s on the Short
(v2.3 addendum).

## Resolution chain — every stage at 4K

| Stage | Result |
|---|---|
| Remotion beat renders, 16:9 | 3840 × 2160 (comps are 1920×1080, `--scale=2`) |
| Remotion beat renders, 9:16 | 2160 × 3840 (comps are 1080×1920, `--scale=2`) |
| `compile.py` 16:9 | `--height 2160` → 3840 × 2160 |
| `compile.py` 9:16 | `--height 3840` → 2160 × 3840 |
| Silent endcard PNG | **2160 × 3840** — see defect 1 |

`compile.py --height` was passed explicitly at both stages and the output probed, rather
than trusting the default (PLAYBOOK §6: it silently produced 720p once).

---

## Defects found during render and compile

### 1. Endcard was upscaled from 1080×1920 — **FIXED**
`compile.py` warned: *"END: still 1080x1920 under output 2160x3840 — the move will reveal
upscale artifacts."* `shorts.py`'s `endcard_png()` was hardcoded to `W, H = 1080, 1920` with
fixed 64/44px type. Made resolution-aware — every dimension now derives from `h`, defaults
unchanged — and added `--end-height`. Regenerated at 2160×3840; warning cleared.

### 2. Endcard carried the wrong channel handle — **FIXED**
`shorts.py --handle` defaults to `@nikbearbrown`. The Short's endcard — the funnel card,
the last thing a viewer sees — read `@nikbearbrown` instead of `@HumanitariansAI`. Caught by
looking at a sampled frame, not by any lint. Corrected and recompiled.

### 3. Quote attribution overlapped the quote in 9:16 — **FIXED**
`WantQuote` positioned the attribution at a fixed `translateY(height * 0.14)` below centre.
That holds while a quote wraps to ~2 lines. In portrait the column is far narrower, the
Tunefind quote wrapped to **five** lines, and the last line ran straight through the
attribution rule — *the source was illegible at the exact moment of assertion.* A
production-gate failure on the beat whose job is carrying a source.

Fixed structurally: quote and attribution now flow in one centred flex column, so the layout
is line-count independent in any aspect. Both quote beats re-rendered in both aspects.

### 4. `SKIN LINT` — B07 had an empty spark line — **FIXED**
SPARK-LINE LAW wants a short serif cue on inner composer beats. Set to `"One caveat,"`,
which suits the limitations beat. Lint cleared.

---

## Known deviation — accepted, not fixed

**`remotion` carries 10/10 beats (100%), over MOTION.md's ~40% cap.**

Week 18's *Their Numbers, My Arrows* sat at 38% Remotion / 62% Manim, deliberately under the
cap. This film is entirely Remotion.

Accepted for three reasons, and recorded rather than silently passed:

1. The teaching *is* the diagrams. Every beat is a generated structure the argument depends
   on — there is no archival or captured material this subject calls for.
2. Perceived variety is carried by the components, not the language: a stepped layer stack,
   geological strata, a tally list, a composer card, two quote cards and an artifact page.
   No two adjacent beats share a scheme.
3. Converting beats to Manim purely to satisfy the histogram would be gaming the lint. The
   histogram keys off `shot.motion`, so adding motion strings would also have silenced it —
   deliberately not done.

Worth revisiting if the next film in this series is also all-Remotion; two in a row would be
a house pattern rather than a per-film choice.

Also emitted: `SKIN LINT: END: outro is 'un-annotated' — OUTRO LAW wants ClaudeTitleOutro`.
Structural to `shorts.py`, which always appends `END` after the real outro. B10 *is*
`ClaudeTitleOutro`; `END` follows it by the Shorts Law. Not a defect in this film.

---

## Frame QC

Frames were sampled at **90% of each beat's own duration**, not fixed frame numbers
(PLAYBOOK §4) — the payload of several beats lands in the last third, so a fixed early
sample would have read as missing content.

- `qc-sheet-16x9.png` — 10 beats, landscape
- `qc-sheet-9x16.png` — 11 beats incl. endcard, portrait

Both regenerated after the v2.2 changes.

Confirmed by eye in both aspects: all ten `SyncCheckResult` rows plus the tally and the
`n = 10 · one model · one run · not a rate` caveat; the fourth layer resolving in
`SyncClaimLayers` on B02 and B05; both source attributions legible and correct; `Opus 5` on
both composer cards; no clipped labels, no overlap, no text below readable opacity.

## Audio

10 beats, Kokoro `af_bella`, per-beat speed 0.93–1.04 to track the tone arc. Delivered
147–224 wpm. `silencedetect -40dB:d=0.55` across all ten files: **clean**, no gaps.
Measured durations are the clock and are stamped into both beat sheets.

## Ship status

**Teaching 12/12** (bar 8). **Production gate: PASS** — re-run on rendered frames in both
aspects, after the four fixes above.

Not published. `PEDAGOGY.md` Gate P is signed for audio; publication is a separate human
decision and the toolkit has no publishing machinery.

---

## Addendum — v2.2 (2026-08-23, after the end-to-end read)

Two changes, both from reading the narration as continuous prose rather than beat by beat.

**B03 extended with a two-sentence bridge.** Audio regenerated at speed 1.00: 21.61s → 24.36s.
**B09 re-shot on a new component**, `SyncSendChecklist` (+ `916` alias), replacing
`ClaudeVerdictArtifact`. Same duration; the beat now renders the three real placement-site
label states with a source line, because the narration asks the viewer to read a label the
film had never shown.

Both re-rendered in both aspects at 4K and both cuts recompiled. Runtimes moved:

| | before | after |
|---|---|---|
| 16:9 | 168.37s (2:48.4) | **171.12s (2:51.1)** |
| 9:16 | 172.87s (2:52.9) | **175.62s (2:55.6)** |

**Runtime headroom is now the thing to watch.** The Shorts hard cap is 180s and `shorts.py`
plans against 178s (cap minus 2s headroom). At 175.62s there are **2.4s** left. Any further
beat growth will start dropping beats from the vertical cut; trim B04 or B09 first if so.

Also fixed in this pass: `SyncClaimLayers` gained `hiddenAtS` (absolute seconds) after a
fraction-based version silently pushed B05's payoff past the truncation point. Documented in
the component and in `PROOF-REVIEW.md`.


---

## Addendum — v2.3 (2026-08-24): pacing pass

Reviewer note: beats cut into each other too fast to absorb. Per PLAYBOOK §5 the fix is a
**hold** — last frame frozen plus silence, then a clean hard cut — never a crossfade, which
softens the cut without giving the viewer time to read. `compile.py` has no transition
mechanism at all, so this is a post-compile pass: `pacing_pass.py`, reused from Week 17 and
copied into this folder.

| Cut | Hold | Before | After |
|---|---|---|---|
| 16:9 | 0.60s × 9 | 171.12s | **176.78s (2:56.8)** |
| 9:16 | 0.35s × 10 | 175.62s | **177.88s (2:57.9)** |

**The two cuts use different holds on purpose.** 0.60s × 10 on the vertical would have
produced 181.6s and broken YouTube's 180s Shorts cap. Shorts are also a swipe-away format
where six seconds of dead air is expensive. To buy the room, the silent endcard was trimmed
4.5s → 3.0s. Final margin under the cap: **2.1s**.

Verified: boundary holds read as 0.70–0.73s of continuous silence at −91 dB, against
0.40–0.55s for natural in-beat pauses — the pause at a cut is audibly longer than a pause
within a beat. Video and audio stream durations agree within 0.043s on both cuts; 4K
preserved (3840×2160 / 2160×3840).

### Defect found and fixed during this pass — endcard sample rate

The first paced vertical cut reported **326.8s** for a file whose video was 4264 frames at
24 fps (177.8s). Cause: Kokoro writes 24 kHz, but `shorts.py` hardcoded the silent endcard at
`anullsrc=r=44100`. `pacing_pass.py` concatenates with stream copy, so one mismatched segment
made the **whole** audio track be reinterpreted at the wrong rate — exactly
177.84 × (44100 / 24000) = 326.8s.

Two fixes: the endcard was regenerated at 24 kHz, and `shorts.py` now probes the reel's own
first beat and matches its sample rate instead of assuming 44.1 kHz. All eleven files in
`short/mp3/` confirmed at 24000 Hz.

Note this never showed up before because `compile.py` re-encodes audio and silently
normalised the mismatch. It only surfaced once a stream-copy concat was introduced.

### Re-run note

`pacing_pass.py` reads `clips/` and writes a separate `-paced.mp4`. `compile.py` overwrites
the unpaced master and knows nothing about this pass, so **re-run pacing after any
recompile**. The files in this folder are the paced cuts, renamed to the clean deliverable
names.
