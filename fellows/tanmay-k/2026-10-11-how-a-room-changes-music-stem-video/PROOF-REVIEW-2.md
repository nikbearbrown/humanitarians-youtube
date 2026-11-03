# Feedback 2: "How a Room Changes Music: One Cellist, Seven Concert Halls" — Tanmay Kulkarni, Week 26 topic film

**Stage:** rendered stills, both aspects (2026-10-10). 56 frames in `_stills/`, each rendered with the
beat's real props at its moment of assertion (planning clock). Narration fully signed (Gate P, incl.
the B01/B02 re-read). No audio yet beyond the four DEMO beats. Reviewed from the frames themselves,
at full size where it mattered, plus `proof_check.py` (exit 0).

**Verdict:**
- **16:9 (the long-form master): clear to proceed to audio.** Teaching **12/12**, production gate
  **PASS on frames**.
- **9:16: production gate FAIL on 6 card beats.** Not a blocker for the long form. It **is** a
  blocker for any of those beats reaching the Short as they stand.

One line: the film now shows what it claims, in landscape. In portrait, the one shared component
we didn't build (`ClaudeArtifactCardFull`) cuts off its own source lines, which is exactly the
"invisible evidence" this film can't afford.

## Production gate, on frames

| Check | 16:9 | 9:16 |
|---|---|---|
| **Evidence legible at the moment of assertion** | **PASS.** Every claim's artifact is readable in its frame: quotes (B05, B06, B11, B16), figures (1752, 74%, 8.73% next to 74.36%, 2003, 1925, 78 rpm, 303, 20 s → 5 s), the framework (B04, B13) and the waveforms (D01–D04). HallTempo's "Shape only…" note renders at full legibility (B08, B09) | **FAIL, 6 beats.** The card clips its last line(s) inside its own frame: **B05** (source cut after "NPR, 24"), **B11** (source cut mid-word), **B12** (source cut after "(2015),"), **B18** and **B20** ("…not a measurement" loses "measurement"), **B19** (source gone entirely). B06, B07, B10 and B17 fit |
| **Sources on screen, not just voiced** | **PASS.** All 17 external-claim beats show their source in frame; our own material is labelled as ours | **FAIL** on the same 6 beats: a clipped source isn't on screen, and on B19 the "not a measurement" label, which keeps the task honest, is missing |
| **Side-by-side at the moment of comparison** | **PASS.** B10 (his words / the researchers' reading), B11 (8.73% / 74.36%), B05 (Bach / chant), B23 (both passes, waiting vs filling in) | **PASS** where the card doesn't clip; B11's comparison itself is visible, only its source is cut |
| **Shorts UI zones** (top 12%, bottom 25%) | n/a | **FAIL, all 10 card beats.** The card runs to ~94% of the height, deep inside the bottom zone that YouTube's caption, title and buttons cover. Our three new components keep to ~73–75%: RoomVoice, HallTempo and AskAnswer pass |

## Rubric (re-scored on frames)

| Criterion | Score | On the frames |
|---|---|---|
| Explicit framework | **2** | Demonstrated in the cold open, and AskAnswer is legible in B04. **Note:** the cold open grew with the real DEMO audio (D01 6.0 s, D02 9.7 s), so B04's framework graphic now lands at **~0:30**, not ~0:20. The method is *demonstrated* by 0:20 (B03: "The speaker changed"), so the score holds. Recorded as a deliberate trade, not a fix |
| Reusable rubric | **2** | B13's rule line is fully legible in both aspects; B14–B16 visibly reuse the same three stations |
| Worked example | **2** | B08 → B09 reads as one picture changing: the wet half, then the dry half drawing in, labels clear of the line |
| Falsifiability / edge | **2** | B11 (8.73% beside 74.36%), B12 (both null studies named), B17 (second study) |
| Active task | **2** in 16:9 | B18–B20 are readable, with the strong/weak answers on screen. In 9:16 the "not a measurement" label is clipped (see gate) |
| Friction | **2** | B10 holds both explanations on one card, attributed separately |

**12/12** (16:9).

## The problem

**The card component isn't portrait-safe for this much text, and it fails silently.** It clips
inside its own rounded frame instead of shrinking or wrapping, so nothing errors and the frame
looks finished. It's a shared toolkit component (its own header says other reels depend on it),
so it stays untouched; the fix belongs on our side.

## Do X next

1. **[EDIT] Decide how card beats reach 9:16 before the Short is written.** The Short is its own
   script (memory: Shorts must feel complete), so two cheap options:
   - **(a)** the Short uses only RoomVoice, HallTempo and AskAnswer, which all pass in portrait. The
     Short's arc (cathedral → both ends → two rooms) needs no card; **or**
   - **(b)** any card in the Short gets its own short text (≤2 lines, a short source) and is
     checked in a 9:16 still before audio.

   Either way, add a **portrait clip check** to `proof_check.py`: render the 9:16 still, then assert
   the card's last text line ends above 75% of the height. Clipping must fail the build, not wait
   for a person to notice.
2. **[EDIT] `RoomVoice` renders a hardcoded "listening…"** when a beat has no passes yet (B01, B21).
   It's harmless here, but it's a display string that's not a prop (PLAYBOOK §2). Make it a prop
   and set it explicitly in the sheet. Prop-only change, so no new stills needed.
3. **[EDIT] Owed after audio:** re-extract each frame at the Whisper-aligned cue time from the
   compiled master (BEATS.md #18). These stills use the planning clock, and the DEMO beats already
   run longer than estimated.
4. **[RECORD]** Log the framework-at-0:30 trade in `BEATS-DRAFT.md`.

## What works

- **The waveform is the argument.** D01's single smear and D02's four islands with the echo dying
  between them read instantly, in both aspects, and they're drawn from the real audio.
- **HallTempo's turn reads in one glance.** B08 shows the dashed, unknown dry side; B09 fills it in
  terracotta, with "slower too" sitting off the line.
- **The new components respect the Shorts zones**: written dual-aspect from the first line, as the
  playbook asks.
- **Honesty labels survive the render** in 16:9: "Simulated echo… Not a measured room", "Shape
  only…", "Our test", "Our listening heuristic, not a measurement".
