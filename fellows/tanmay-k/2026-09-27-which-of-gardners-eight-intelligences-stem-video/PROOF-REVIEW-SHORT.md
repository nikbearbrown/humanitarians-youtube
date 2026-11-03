# PROOF review — Week 24 Short, v2 script ("ONE HOUSE, ONE CAMERA"), pre-audio (2026-09-27)

**Verdict: fix before Gate P.** The script and structure do what the brief asked. The Short has one
continuous arc and answers its own hook. But four MAJOR production defects are already visible
on paper, and one of them (S04) needs a narration change, so it has to be fixed before Gate P.
The others are props or layout.

**Reviewed:** `build_short_sheet.py` → `beat_sheet.json` (6 beats, 287 words, ~1:31 at the long's
measured pace). There is no audio or render yet. Cue times are estimated from word position at
3.17 words/s. Kokoro will shift the absolutes, but the proportions below hold, because cues are
word-position fractions of each beat.

## What's done

| Step | State |
|---|---|
| v1 (stitched room beats) | rejected by Tanmay; recorded in `SHORT.md` and memory |
| v2 short-only script with its own arc | written, `build_short_sheet.py` |
| Toolkit: per-room cues, accent follow, timed captions (`EightRooms.tsx`) | added, `tsc` clean |
| **Regression: the long is unaffected** | re-rendered the long's B03 (plan) and B15 (tour) in a scratch reel: **pixel-identical** to the shipped clips at 4 timestamps each |
| End card | regenerated cream / EB Garamond (unused in v2) |
| Gate P mechanical lint | 1 flag (NAME `Gardner`, accepted in the long); a BREATH flag was already fixed |
| Gate P | **not signed**, correctly: no audio exists |

## Trailer gate (the Week 23 Short rubric; interactivity replaced by the brief's "feels complete")

| Criterion | Score | Why |
|---|---:|---|
| Hook | **2** | S01 names Tanmay first, then a specific, checkable sentence ("not yet a serious competitor") and a turn ("He did ask") |
| Accuracy / no overclaim | **2** | Every line traces to FACTCHECK (0.3, 0.5, 1.1, 1.2, 3.2–3.5, 3.11). The "may have been" hedge is kept; "the same paper's history" attributes 1956 correctly |
| Complete on its own | **2** (on paper) | Hook → house → six → two exceptions → answer, and the answer closes the hook. Continuity is designed into every cut (`SHORT.md`) but **not yet verified on frames** |
| Honest incompleteness | **2** | "The full video opens every door" is true, and the Short doesn't claim to have shown the evidence it only names |
| Clear, accurate CTA | **2** | The long's title is on the S06 card; room seven's question really is the long's closing ask (B18) |
| Brand / technical | **2** | Name at open and close, handle, cream, OFL fonts. Shorts UI zones: **0 FAIL across all 394 frames** of a full-length silent render of every beat; every button-column LOOK was checked by eye and is decoration, not text. No black frames. Captions carry across cuts without blinking (see "Brand / technical: resolved") |

**12/12** (Brand/technical raised to 2 on 2026-09-27, below). "Complete on its own" is now also verified on frames at every cut, not just designed.

## Production gate: 4 MAJOR, 3 MINOR

| # | Beat | Defect | Evidence | Severity | Fix |
|---|---|---|---|---|---|
| 1 | S02–S05, S06 | **Evidence captions sit where YouTube's Shorts UI covers them.** The toolkit's own portrait rule (`ClaudeTitleOutro916.tsx`) reserves the top 12% and bottom 25%. The EightRooms portrait layout starts its caption at **72%** of the height (grid ends at 69%), so every quote and source line falls in the bottom band, under the title/channel overlay. S06's card pins the handle 6% from the bottom, also under it | layout maths from `roomRect` at 1080×1920: gridTop 248px, grid bottom 1323px, caption from 1381px; the reserved line is 1440px | **MAJOR**: the Short's sources-on-screen rule would pass on the file and fail on the phone | portrait branch of EightRooms: top pad 12%, reserve the bottom 25%, shrink the grid to fit; keep `roomRect` in step so the tour still lands. S06: portrait padding to the same zones. Landscape is untouched, so the long is unaffected (re-run the regression) |
| 2 | S04 | **The "category error" evidence barely appears inside the room.** The interior caption lands at 15.1s and the walk-out starts at 15.4s: 0.3s of evidence, after 4.3s inside with no caption. The quote is the beat's last words, so the camera leaves as it's spoken | cue table: interiorInAt 10.88, interior caption 15.14, interiorOutAt 15.43 | **MAJOR**: the Short's key claim, unshown at its moment | **narration** (so it's due before Gate P): move the quote up and close on the long's own resolution: "…knowing yourself stays dark. Using that word for a program at all, they write, 'can be seen as a category error.' So it isn't dark because a machine failed. It's dark because, on their reading, the question doesn't apply." Walk in at "stays dark", caption at "can be seen", out at "It's dark because" |
| 3 | S03, S04 | **Captions replaced faster than they can be read.** S04's "one should be more cautious" (12 words) holds **1.3s**. S03's bodily-kinesthetic caption (9 words) holds **1.9s** (needs ~3.4s) | cue table | **MAJOR**: legibility in a format watched once, fast | S04: merge into one caption held across room 7 ("“one should be more cautious” · evidence: diplomacy, salesmanship, gamesmanship, therapeutic interactions"). S03: cue each caption on the room's name ("Space", "The body"), not on its quote, which gives +1–1.5s each and still lands before the claim |
| 4 | S05 | **The correction is shown without the thing it corrects.** At "that essay's sentence?… 1956" only the 1956 record is on screen. The essay's A-side isn't. This is the long's own defect class (PROOF-REVIEW-FINAL #2, fixed there in B07) | caption_steps S05 | **MAJOR**: side-by-side at the moment of comparison | S05 second caption: "Essay: 1983, “not yet a serious competitor to any of them” · Record: 1956 programs “carried out mathematical and logical operations”" (holds ~6s; check the fit after defect 1) |
| 5 | S02→S03, S04→S05 | The source line changes text at two cuts (S02 adds "Rooms: Frames of Mind…"; S05 adds the essay), a visible flicker in an otherwise continuous take | props | MINOR | one source string for S02–S05 covering all three sources |
| 6 | S01 | Composer has no `durationSeconds`, so it renders at the registered 15s and the last ~1.4s is a freeze | Root.tsx `ClaudeComposerAskOFL916` default 15s | MINOR | builder sets `durationSeconds` for the composer too |
| 7 | S06 | Title card registered at 150 frames (5s) with no duration hook; ~3.5s freeze on an 8.5s beat | Root.tsx | MINOR (static card, invisible) | accept, or add the hook the other 916 scenes have |

Checked and **not** defects:
- S01's quote is on screen (~3s) before it's spoken (~6s).
- Every S03 light switches on at its spoken cue.
- The accent hand-offs at the cuts match: S03 ends on Naturalist and S04 opens on it; S04 ends on room 8 and S05 opens on it.
- "It's linked right below" is the house CTA wording (Week 23).
- The right-side Shorts buttons overlap only the right edge of the right-column rooms, whose labels start at 52% of the width. That's cosmetic, and defect 1's margins can widen it anyway.

## Not yet checkable (after audio and render)

- Continuity on the actual frames at each cut, including the 0.6s holds
- The 4K portrait scale: 916 compositions are 1080×1920 and must be rendered or scaled to 2160×3840
- GATE V, loudness (-14 LUFS target, as the long), and the moment-of-assertion OCR on the Short's master

## Order from here

1. Fix 1–4 (+5–6), with 2 as a narration edit → regenerate the sheet → re-run the lint and this cue table
2. **Gate P** on the revised S04 (and the rest, read aloud)
3. Audio → portrait renders → frames of every beat and every cut to Tanmay → 4K compile → PROOF on the master

---

## Fixes applied (2026-09-27, Tanmay: "apply all the fixes")

| # | Fix | Verified |
|---|---|---|
| 1 | **Shorts UI zones.** New `planLayout()` in `EightRooms.tsx`, shared with `EightRoomsTour` (plan, camera target and interior). Portrait reserves the top 12% and bottom 25%, and captions/source stop at 82% of the width (clear of the right-hand action buttons). `ClaudeTitleOutroFull` portrait uses the same zones | pre-audio test renders of S02–S06 at 2160×3840 with guide lines: all heading, grid, caption and source text sits inside the band and left of the button column (`_qc/pre/sheet.png`, `sheet2.png`) |
| 2 | **S04 narration** (Gate P): the quote moves to mid-interior, and the beat closes on the long's own resolution while the camera pulls back ("So it isn't dark because a machine failed. It's dark because, on their reading, the question doesn't apply.") | cue table: the interior caption now holds **4.2s inside** (was 0.3s), with the walk-out at "It's dark because" |
| 3 | **Caption holds.** S04: one merged room-7 caption (holds 9.8s). S03: captions cued on the room's name. Music gets its own phrase ("even new pieces in distinctive styles", FACTCHECK 3.11) so its caption isn't replaced within 0.6s | S03 holds: 3.8 / 5.4 / 2.5 / 4.7s. Two sit slightly under the 3.5 words/s estimate (LLM quote, Musical), but both are spoken as they appear; recheck on measured audio |
| 4 | **S05 side-by-side:** "Essay: in 1983… · Record: 1956…" together at "that essay's sentence" | holds ~11s; fits in 4 lines inside the band (test frame) |
| 5 | **One source line** across S02–S05 | no footer change at any cut |
| 6–7 | **Render length = measured audio** for every scene; `durationSeconds` added to the ComposerAsk and TitleOutroFull schemas, plus a duration hook on `ClaudeTitleOutroFullOFL916` | applies once audio exists |
| + | Found on the test frames: S03's accent stayed on Music while the body was described. It now moves at "The body," | — |

**Regression, re-run after all layout changes:** the long's B03 (plan) and B15 (tour) re-render
**pixel-identical** at 8 timestamps. Landscape layout is untouched. `tsc` clean.

Pre-audio renders are truncated at the registered length (no measured audio yet), so continuity
and the S04 pull-back can only be checked on the post-audio renders. They were deleted so nothing
stale gets compiled.

**Status: ready for Gate P** (the whole script, S04 changed most).

## Brand / technical: the path from 1 to 2 (2026-09-27)

Tanmay asked how to close this row. Fixing the layout wasn't enough to score it. The score needs
the fix measured on the deliverable ([[measure the mechanism before closing a fix]]).

- **New check, `_qc/safezone_check.py`:** it samples the master and FAILs on any ink in the top 12%
  or bottom 25%. Ink in the right-hand button column is flagged LOOK and checked by eye, because
  decorative edges and the ~1s camera move may pass under the buttons but text may not.
- **The check found a miss in my own fix on its first run.** S01 (ClaudeComposerAsk) wasn't
  covered: the topic tag was in the top band and the accent rule in the bottom band (16/17
  frames FAIL). The composer also reached the button column, and the essay quote was set in small
  mono. Fixed in portrait only: the elements are repositioned and output lines are 1.15·UI (was
  0.85·UI). The scene's `largeText` was tried first and rejected, because the source line wrapped
  into the bottom band. Result: **0 FAIL, 0 LOOK**, and the quote is legible at phone size.
- **Regression:** the long's B01 (composer) and B19 (title card) re-render pixel-identical,
  as B03 and B15 did.

**2/2 is awarded when:** `safezone_check.py` on the final Short master = **0 FAIL**, and every LOOK
is classified as non-text by eye. Plus the usual GATE V at 2160×3840.

## Brand / technical: resolved → 2 (2026-09-27, before Gate P)

Tanmay: *"resolve this, and see if we can push it to 2 and then I'll go through the read aloud
file and only then I can pass gate p."* Where things sit on screen doesn't depend on the audio (the
audio only moves *when* they appear), so the check is a **full-length silent render of all six
beats** at the estimated pace, 2160×3840, swept every 0.25s.

| Check | Result |
|---|---|
| `safezone_check.py`, top 12% / bottom 25% | **0 FAIL in 394 frames** (S01 67 · S02 64 · S03 79 · S04 86 · S05 64 · S06 34) |
| Button column (right 16%, 45–90% height) | 265 LOOK. By eye (`_qc/pre/looks.png`), every one is the right edge of the bottom-row Intrapersonal card (45–50% height; its label sits at the card's left) or the room copy during the ~1s walk-in. **No text** |
| Cuts inside the house (last frame vs next first frame) | S02→S03 **0.0%** changed · S03→S04 **0.1%** · S04→S05 **0.0%** (grid and caption bands) |
| Planned scene changes | S01→S02 (composer → house), S05→S06 (house → title card) |
| Regression, the long | B01, B03, B15 and B19 are pixel-identical after every toolkit change |

### Defects this pass found (all fixed)

1. **A black frame at the cut into the title card.** `ClaudeTitleOutroFull` faded its whole fill in from
   opacity 0, so frame 0 rendered solid black. The sweep caught it on S06. Now the page is opaque
   from frame 0 and only the content fades. **The same frame is in the long master at 5:50.38**
   (one frame, ~0.04s; a per-frame luma scan of the whole master finds exactly this one). GATE V and
   the earlier dense sweep missed it. See "The long" below.
2. **The caption blinked at every cut inside the house.** The carried-over caption restarted its
   fade-in at 0s, so the first frame of S03, S04 and S05 had no caption. The pixel numbers didn't
   show it; the cut sheet did (`_qc/pre/cuts.png`). Now a step at ≤0s is fully shown from frame 0,
   and S05 carries S04's caption until "six lights on".
3. **S01 was outside the fix** (topic tag in the top band, accent rule in the bottom band, small mono
   quote). Fixed in portrait only (see above).
4. **Years read wrongly by the voice** (found writing the read-aloud sheet). Kokoro reads digit years
   as "nineteen hundred eighty three", "nineteen hundred fifty six", "two thousand twenty four". The
   Short's narration now writes them in words (the same TTS-spelling treatment as the long's "gee"
   and "M-I"). Captions keep the digits.

### The long: two defects found, not yet fixed (Tanmay's call)

| Defect | Where | Fix |
|---|---|---|
| One black frame at the cut into the outro | 5:50.38, B18→B19 | re-render B19 (the component is already fixed) → recompile → pace → loudnorm. Picture only |
| Years read as "nineteen hundred eighty three" (×4), "mid nineteen hundred ninety z" ("mid-1990s"), "nineteen hundred fifty six", "two thousand seven / nineteen / twenty four" | B01–B05, B07, B17 | spell the years out in words → regenerate those beats' audio → re-cue → recompile. TTS spelling only, like "gee", but it changes the audio, so Tanmay should hear it |

**Still required on the final Short master:** the same sweep at 0 FAIL, GATE V, loudness, and the
moment-of-assertion OCR. That's a confirmation that nothing regressed, not the basis of this score.

---

# PROOF review — the Short's 4K master (2026-09-27)

**Verdict: clear-for-public.** Trailer gate **12/12**. Production gate **PASS**.
Gate P signed 2026-09-27 (*"Gate P PASS"*). Frames of every beat and every cut went to Tanmay
before the compile (`_qc/review/`), and he approved the compile.

**File:** `gardner-eight-rooms-short-final.mp4` · **2160×3840**, 24 fps · **1:38** (98.0s: 94.9s of
narration + 5 holds × 0.6s) · **-14.9 LUFS**, **-1.9 dBFS** true peak, LRA 3.1 · AAC 48 kHz · video
stream identical to the paced cut (MD5), so normalisation touched audio only.

## Production gate

| Check | Result |
|---|---|
| GATE V (`compile.py`, 12 frames) | **0 BLOCKER · 0 MAJOR**. The first compile was refused, see defect 1 |
| Shorts UI zones, whole master every 0.25s (`_qc/safezone_check.py`) | **0 FAIL in 393 frames**. Button-column LOOKs are the room-card edge and the room copy during the walk-in (by eye, no text) |
| Dark frames, every frame (luma < 80) | **0** |
| Claims on screen at the moment of assertion (`_qc/claims_at_assertion.py`, OCR) | **16/16** |
| Cuts inside the house | ≤0.1% of the frame changes; captions carry over with no blink (`_qc/review/cuts.png`) |
| Pacing holds | 5 × 0.6s |
| Fonts / images | OFL only; no third-party images |

## Defect found at compile (fixed)

1. **The portrait walk-in was a letterbox strip.** Room cells in the 2×4 portrait grid are wide and
   flat, so a uniform scale stopped at the frame's width. "Walking into" room 8 grew a thin dark
   band and GATE V flagged S04 at 85% as underfill (15% of the safe area). In portrait the room now
   opens to the full safe band, width and height separately. Landscape is unchanged: the long's
   B07 and B15 re-render pixel-identical at 5 timestamps each.

## Trailer gate: 12/12

| Criterion | Score |
|---|---:|
| Hook (name first, a checkable sentence, "He did ask") | 2 |
| Accuracy / no overclaim (16/16 evidenced; hedges kept) | 2 |
| Complete on its own (one arc; the answer closes the hook; continuity measured at every cut) | 2 |
| Honest incompleteness ("the full video opens every door") | 2 |
| Clear, accurate CTA (the long's title on the card; the room-seven question is the long's own) | 2 |
| Brand / technical (UI zones measured on the master, no dark frames, OFL, handle, cream) | 2 |

## Known and accepted

- Three captions hold slightly under a 3.5 words/s reading estimate: the LLM quote 3.7s, Musical 2.5s,
  "Six lights on" 3.6s. Each appears while the same words are spoken.
- Room 8's interior shows the art alone for ~2.7s before "category error" is spoken, so the quote
  isn't shown before its moment.

Render only: upload, the related-video link to the long, and scheduling are Tanmay's.

---

# PROOF review — the finished Short, viewer pass (2026-09-27)

Tanmay: *"now do a proof review on this completed shorts video!"* The master review above ran
the gates. This pass asks what those gates don't measure: does the picture move **with the words**,
does it read at **phone size**, how does the **sound** flow between beats, and does every line land for
someone who hasn't seen the long?

**Verdict: clear-for-public, with three recommended [EDIT]s** (no narration change, so Gate P
stands). Nothing is inaccurate, unsourced or unsafe. The findings are about how it plays.
Trailer gate stays **12/12** (it doesn't score sync or type size). **Production gate PASS.**

## What was measured

| Check | Method | Result |
|---|---|---|
| Lights switch at their cues | luma at each room's centre, 0.3s before / 0.4s / 0.8s after each S03 cue | all 6 **dark → lit within 0.4s of the cue** |
| **Cues vs the actual speech** | `_qc/cue_drift.py`: sentence starts aligned in order to the audio's pause ends (monotone DP), signed | **mean 0.55s, max 1.01s; 13 of 21 over 0.5s** |
| Gaps between beats | `silencedetect` on the master | 5 gaps of **1.14–1.22s** (voice tail + 0.6s hold + next lead-in) |
| Loudness per beat | ebur128 over each beat's span | -15.2 to -14.4 LUFS, even |
| Type size at phone width (390 pt) | component sizes at 2160 px | caption 15.5 pt · heading 24 pt · composer quote 12.8 pt · source 9.4 pt · **room names 8.1 pt · "light on / dark" 6.1 pt** |
| First voice | silencedetect | 0.07s (no dead lead-in) |

## Findings

| # | Finding | Evidence | Severity | Fix |
|---|---|---|---|---|
| 1 | **The picture drifts from the words by up to a second.** Cue times are placed by word count, but Kokoro pauses at punctuation, so later sentences land off their estimate. The ones you'd notice are the **late** ones: "Music: on" lights **0.72s** after it's said, the body's accent **0.58s**, "And nature: on" **0.66s**, the S02 highlight trails the names by **0.76s**, and room 7's door opens **0.52s** after "Other people". Early ones (the S02 rule caption, 1.0s) read as captions arriving first, which is harmless | `cue_drift.py` table | **MAJOR (polish)**: S03's whole idea is the light on the word | **[EDIT] pause-anchored cues**: anchor each sentence to its real pause (the same alignment), interpolate words inside it, re-render, recompile. Props only. Target: every visual cue within ±0.25s |
| 2 | **Room names are small on a phone.** 8.1 pt names, 6.1 pt state labels. The state is carried by the fill, and the names are spoken in S02 and S03, so nothing is lost, but they're below comfortable reading size | layout maths at 2160 px | MINOR | **[EDIT]** portrait only: names ×1.5 (≈12 pt), state labels ×1.5 (≈9 pt). The cells have the width ("Logical-mathematical" ≈ 750 px of ~900). Landscape untouched |
| 3 | **Five 1.2s silences** in a 98s Short. The picture holds still, so each cut is a small stop in a film meant to feel like one take | silencedetect | MINOR | **[EDIT]** hold 0.3s instead of 0.6s for the Short (gaps ≈ 0.9s, −1.5s runtime). The long keeps 0.6s |
| 4 | **"Using that word for a program at all"** (S04): no word has been named. The listener hears "knowing yourself stays dark. Using that word…", so "that word" has no clear antecedent. The same line is in the long's B15 | read as a first-time viewer | MINOR (clarity) | optional **[NARRATION]**, needs Gate P and new S04 audio: "Even applying that idea to a program, they write, 'can be seen as a category error.'" (FACTCHECK 3.5: invoking it for a program) |
| 5 | The hook proper starts at 3.7s ("An essay I read…"); 0–3.7s is the name, over the question typing in | first voice + S01 text | note, not a defect | a deliberate trade: Week 23's feedback put the name first. The typing question is the visual hook in those seconds |

Checked and fine:
- the S01 quote is on screen before it's spoken
- the accent hand-offs at every cut
- 16/16 claims on screen when spoken
- 0 dark frames and 0 UI-zone fails
- the title card holds under the CTA and sign-off
- loudness is even
- no dead air at the start

## Also true of the long (found here, not yet fixed)

Same cue method, same drift: **mean 0.51s, max 1.17s, 28 of 62 sentence starts over 0.5s**
(`cue_drift.py` on the long's sheet). Its 35/35 claims pass because the evidence arrives with or
before the words. The fix in #1 applies there too.

## Not yet made (publishing kit, Tanmay's to use)

- the Short's upload title and description (with the long's title for the related-video link)
- an `.srt` caption file (it can be generated from the same pause-anchored timings as #1)

## Recommended order

#1 → #2 → #3 (props, layout and pacing only; re-render, recompile, re-run every gate). #4 only if
Tanmay wants the line changed, since it reopens Gate P for S04.

## Fixes 1–3 applied, to the Short and the long (2026-09-27)

Tanmay: "go ahead and apply fixes 1-3 to the short and long".

| Fix | What changed | Verified |
|---|---|---|
| 1. Pause-anchored cues | new `cue_align.py`, used by both builders and both claim checks. Punctuation boundaries are aligned in order to the real pauses (−38 dB, 0.08s); letters are interpolated across **speech only**, ending at the next pause's start. The first version counted the pause itself, which pushed Nature's light +1.07s late; it was caught by the sync check and fixed. Nature's cue moved to the anchored "And nature" | `sync_check.py` (independent: the master's own frames against the master's own audio). **Short: mean +0.50s / max 0.97s → mean +0.28s**, every light switching on the word. The residual ≈0.3s is the light's own rise to half-bright. Music 0.97 → 0.27s, body 0.97 → 0.30s, room 7's door 0.68 → 0.18s. The one +0.72s reading (Nature) is a measurement miss: after loudnorm the 0.09s pause before "And" isn't detected in the master, so the check matched the pause before "On." In the beat audio, Nature starts on its word like the others. **Long: mean +0.44s → +0.41s** on its 3 measurable lights (B11 0.96 → 0.58s) |
| 2. Larger room labels | `planLayout().labelScale`: portrait ×1.5 (names ≈12 pt, state ≈9 pt at phone width), landscape ×1.3. The walk-in copy matches | frames: every name on one line in both aspects, including "Logical-mathematical" and "Bodily-kinesthetic" |
| 3. Shorter holds | pacing hold 0.6 → **0.3s** (both films) | Short gaps 1.14–1.22s → **0.84–0.92s**. Long 19 gaps, mean 0.86s, max 0.97s |

**Short master** (`gardner-eight-rooms-short-final.mp4`): 2160×3840 · **1:37** (96.5s) · -14.8 LUFS /
-1.9 dBFS · GATE V 0/0 · 0 UI-zone FAIL (387 frames) · 0 dark frames · **16/16** claims · video = paced (MD5).

**Long master** (`gardner-eight-intelligences-machine-final.mp4`): 3840×2160 · **5:46** (346.0s) ·
-14.9 LUFS / -1.9 dBFS · GATE V 0/0 · 0 dark frames · **35/35** claims · video = paced (MD5).

Both verdicts unchanged: **clear-for-public**. Narration unchanged, so Gate P stands for both.
Still open: optional [NARRATION] #4 ("Using that word…"), and the publishing kit (titles,
descriptions, `.srt`).
