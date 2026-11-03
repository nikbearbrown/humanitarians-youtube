# PROOF review 2: the rendered beats (both formats)

**Film:** *Four Mornings* (Week 26 work video, Mycroft PR #64) · **Date:** 2026-10-10
**Input:** the 20 approved stills (`_stills/`, 10 beats × 16:9 and 9:16), plus frames at the spoken moments
(`_stills/verify/`), all from `beat_sheet.json` built off `SCRIPT.md` draft 2 (Gate P PASS) and `main @ 5097a8f`.
**Clock:** the planning clock (3.3 words/s). Every cue is a narration phrase, so the same cues move onto the
measured clock once the audio exists, and this check is re-run then on the masters.

## Verdict: PASS, 12/12, after three timing [EDIT]s

The teaching held on the frames: the four-part hand-off strip, the same dashboard each morning, and evidence
for every claim. Review 1's intent gate failed on one point. The stills showed the right content at the
right size, but checked at the moment each line is spoken, three things showed up early or late. All three
are fixed and checked on frames rendered either side of the spoken word.

## [EDIT]s applied

| # | Beat | What the frames showed | Fix | Checked at |
|---|---|---|---|---|
| E1 | B05 | The side-by-side (Define Portfolio 50 → 55 · Calculate Metrics 50) appeared only with the evidence, at "So the first step", about six seconds after "Edit the shares in the first…" was spoken | Each compare item now has its own reveal time (`at`, from a cue). Both copies appear at "Edit the shares in the first" | 11.2 s: panel empty · 12.4 s: both copies up · 18.6 s: plus the step-1 and self-test lines |
| E2 | B07 | "pass" appeared already struck through, so "It passed. All green." was never shown as a pass | A separate strike time (`struckAt`). "pass" appears unstruck at "It passed" and is struck at "But the broken version". "Now … caught" appears at "Now the test" | 10.3 s: empty · 11.2 s: "pass" · 12.5 s: struck, with the self-test quote · 23.6 s: the catch beside it |
| E3 | B03–B06 | Each morning's hand-off box was lit (RECORDED / STOPS) from the first frame, before the narration had named the check | Each hand-off has its own light time. The one a beat adds lights on the line that introduces the check: B03 "What changed is the record", B04 "Now the check before it", B05 "So the first step now", B06 "So the dashboard's first step" | ±0.4 s around each cue: unlit before, lit after, in all four beats and both formats (`handoff-timing-16x9.png`, `-9x16.png`) |

**Mechanism:** `MorningDashboard.tsx` (brutalist.art) now takes `at`/`struckAt` on compare items and `at` on hand-offs.
Null keeps the old behaviour, so earlier props render unchanged (`tsc` exit 0). `build_beat_sheet.py` turns any
`…Cue` key into seconds, nested ones included, and fails the build if a cue phrase isn't in the narration.

## Production gate

| Check | Result |
|---|---|
| Every spoken figure and quote is on screen when spoken | PASS (static check 0 fails; E1–E3 timing fixed) |
| Every claim beat names its committed file | PASS. Source line on B01, B03–B08, and the card's source line on B02 |
| "Illustration · every price invented" on every dashboard | PASS, all eight dashboard beats, both formats |
| Side-by-side held | PASS. B05 holds both copies from 12.4 s to the end. B07 holds struck "pass" beside the catch from 23.6 s |
| Legible at the assertion | PASS. 16:9 type was raised about 30% at the stills stage. The 9:16 stack fits inside the Shorts zones |
| No W25 material | PASS. The only trace is the one-cent catch, shown as the self-test D row |

## Pixel checks (refreshed stills plus verification frames)

- **Gate V**, 16:9: 25 frames, 0 BLOCKER / 0 MAJOR. The run's one BLOCKER is `handoff-timing-16x9.png`, a
  contact sheet of crops made for this review, not a frame.
- **Portrait zones**, 9:16: every frame passes except two. One is B02's card, the known shared-card limit, so
  the Short uses `MorningDashboard` only. The other is the 9:16 contact sheet, again not a frame.

## Carried forward

1. Re-run these timing checks on the masters, with cues on the measured (Whisper) clock.
2. B02 stays out of the Short.
3. Audio: Kokoro am_onyx, with the Mycroft override `mˈaɪkɹɔft`.

---

# Audio stage (2026-10-10)

`make_audio.py` (Kokoro am_onyx, stage-1 loudness −16 LUFS / −2 dBTP): 10 beats, 183.4 s (~3:03).
- **Mycroft override** `mˈɪkɹɔft` → `mˈaɪkɹɔft` applied in B02, the only beat that says the name (the
  run fails if a swap finds nothing to replace).
- **Whisper (small.en):** B02 and B04–B07 read back word for word. The other differences are only how Whisper
  writes what it heard: "$65,098" for the spoken amount (B01), "handoffs" for "hand-offs", "behavior" for
  "behaviour", and "For mornings" for "Four mornings" (B10, the same sound, with nothing around it to tell them apart).
- **Gap sweep:** one pause over 0.55 s, B07 at 21.7 s (0.57 s), between "really ran." and "And then it
  catches the break". It's a sentence break on the turn, so it stays.
- **Cue clock:** cues now come from Whisper's start time for each cue's first word (`align_words.py` →
  `mp3/word_times.json`, all 13 cues aligned). The pause-anchored clock ran 0.7 s and 1.2 s late on B07's
  "It passed" and "Now the test", where the long sentences give it no pause to anchor to. It stays as the
  fallback for a cue Whisper can't align.

---

# Masters (2026-10-10)

| | 16:9 `four-mornings-final.mp4` | 9:16 `short/four-mornings-short-final.mp4` |
|---|---|---|
| Size, length | 3840×2160, 3:06 (10 beats, 0.3 s holds) | 2160×3840, 1:53 (7 beats, 0.3 s holds, 2 s after S06) |
| Loudness | −14.8 LUFS, TP −1.6 dBTP | −14.7 LUFS, TP −1.9 dBTP |
| Gate V | 20 frames, 0 BLOCKER / 0 MAJOR | 14 frames, 0 BLOCKER / 0 MAJOR |
| Timing frames (0.7 s after each cue, from the final file) | 22, every reveal on its spoken line | 19, every reveal on its spoken line; portrait zones 19/19 |

**Changes approved by Tanmay after the first masters:**
- **B03 (16:9):** GOOGL tagged "previous close" alongside META. The merged record shows both used it
  (FACTCHECK W20), and the Short now says so. Picture only, no narration change. B03 re-rendered alone,
  with the other nine beats' render stamps kept.
- **Short S01:** "Five stocks, and one total" → "Five stocks. One total". Kokoro had blended it into "five stocks
  in one total" (Whisper heard "in"). S01's audio regenerated alone (`make_audio.py --dir short --only S01`), so
  Whisper now differs only by writing "$65,098". S01 re-timed and re-rendered.

**Short draft 2** (after Tanmay's note on context): the audit of draft 1 and the reasons for each change are at the top
of `short/SCRIPT-SHORT.md`. New facts W20–W22 are in `FACTCHECK.md`. Short Gate P PASS on draft 2.

**Known limit, recorded:** neither pixel gate catches overlapping text (S03/S05 overlaps at the stills stage were
found only by looking). Every frame is looked at, not just gated.
