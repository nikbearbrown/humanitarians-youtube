# PROOF review: Week 25 work video, *Same Logic, Two Languages* (pre-production, 2026-10-04)

**Stage:** script drafted, fact-checked and linted; **before Gate P**. Nothing is generated yet: no audio, no
scenes. This review is placed before the read on purpose (the Week 24 lesson: checks before renders).

**Verdict: 5 fixes, all applied in SCRIPT.md draft 2. Ready for the Gate P read.** The structure, claims and framing
hold. Two fixes are about what Kokoro would actually say, two are about clarity and accuracy, and one is a
uniqueness boundary.

## Teaching rubric

| Criterion | Score | Why |
|---|---:|---|
| Explicit framework | **2** | B02 announces three matches; B05 states the idea: "A match only tells you something if a mismatch could have shown up" |
| Reusable rubric | **2** | One portable question (B05, B12): where could these two differ, and is a test standing exactly there? It works for any rewrite, migration or refactor |
| Worked example | **2** | Three matches, each on a real run: expected flags (B04), parity 16/16 (B05), report vs log (B09) |
| Falsifiability / edge case | **2** | B07: my own changes went unnoticed (verified on a scratch copy, 14/14); B10: everything live is untested |
| Active task | **2** | B12: "Find that one spot, and make sure a single test is standing exactly on it" |
| Friction | **2** | B01's two answers to one question; B05's "then it started to bother me"; B07's "still agreed" |

**12/12 on the script.** Re-scored on the first compile, where the production checks apply.

## Findings

| # | Beat | Finding | Severity | Fix (applied) |
|---|---|---|---|---|
| 1 | B02, B09 | **Kokoro says "Mycroft" as MICK-roft** (`mˈɪkɹɔft`): the repo's name, said wrong twice | MAJOR (ear) | Narration respelled **"My-croft"** → `maɪkɹˈɔft`. Captions and on-screen text keep "Mycroft" (caption step must map it back) |
| 2 | B04, B09 | **Past-tense "read" is voiced as "reed"** (`ɹˈiːd`) in "I read the original JavaScript" and "I read the human report": it sounds like present tense | MAJOR (ear) | B04 "I **went through** the original JavaScript"; B09 "I **put** the human report **side by side with** its machine log". Re-phonemized: clean |
| 3 | B04, B05, B09 | **The structure was never said out loud.** The on-screen labels said "pair one, two, three", but the narration first said "the third pair" in B09, so a listener meets a third of something never introduced | MAJOR (clarity) | B02 ends "It came down to **three matches**." B04 opens "The first match is my own reading against the original." B05 "The second match is the real comparison." B09 "The third match…". "Match" also echoes the thesis line in B05 |
| 4 | B02 | **"This week I contributed to Mycroft"** can be heard as merged. The work is on my fork and the PR isn't open yet (B11 says "waiting for review") | MINOR (accuracy) | "This week I **worked on a contribution** to My-croft" |
| 5 | structure | **"Pairs" overlaps W20 B12** ("write the pairs down", two states that must stay distinct) | MINOR (uniqueness) | Renamed to **matches** throughout (narration, act labels, on-screen). Matches are things that must *agree*, the opposite idea from W20's |

Checked and **not** findings:
- Every claim maps to a ✅ row in FACTCHECK.md: L1–L3 live in Node and Python; C8 reproduced on a scratch copy of `d9cd514`.
- Both quotes are verbatim: README line 9; SNICKERDOODLE P6.
- No critique of the original workflow, no author named. Every gap shown is my own (test data, report step).
- New phrases checked against W15–W24 narration, all 0 hits: "honest about", "closer to home", "felt good", "bother", "on the line", "standing exactly". The phrases the angle avoids ("break", "attack", "coverage", "receipt", "dark", "fails closed") are still absent.
- "Live" in B10 is said `lˈaɪv` (correct).
- Every digit is spoken separately in "zero point six two five" (correct).
- Runtime ~4:50 (919 words at 3.17 words/s).

## Production plan checks (before anything is generated)

| Check | Plan |
|---|---|
| Sources on screen as they're said | B02 README line, B09 P6 line, B04 the `expected-flags.json` basis, B06 the real FXQ flag, B11 the GitHub comparison |
| Honesty labels | B07's changed copy labelled "my copy, changed on purpose, scratch run" whenever on screen |
| Captions | Map "My-croft" → "Mycroft" in the SRT/VTT; Whisper-check the respelling is heard as MY-kroft |
| Timing | audio → **Whisper-align immediately** → every cue on the Whisper clock before the first render |
| Loudness | normalise each master to −14 LUFS / −2 dBTP before assembly (it has slipped twice before) |
| Masters | 16:9 at 3840×2160; the Short at 2160×3840 |
| New scene (TWO COLUMNS) | build the two-column JS ↔ Python component once, then **stills of B01, B07 and B09 in both aspects** before rendering all beats |
| Numbers to re-check at render | B11's "115 added · 3 modified · 0 removed · 0 renamed" against the live GitHub comparison (it changes if the branch gets another commit) |

---

# PROOF review: stills, both aspects (2026-10-04)

**Stage:** script draft 3 (B11's "on my fork, waiting for review" removed at Tanmay's request; B11 re-recorded,
15.08 s, Whisper `medium.en` hears it as written; word clock re-aligned, 13/13). 26 stills, each beat's end state,
16:9 and 9:16, rendered from the real props on the word clock. Every still was looked at, full size where it mattered.

**Verdict: 8 findings, all fixed and re-rendered. The stills are ready for your review.**

| # | Beat | Finding | Severity | Fix |
|---|---|---|---|---|
| 1 | all | **Underfill**: content in the top half, small type, the lower half empty (worst in 9:16) | MAJOR (fill) | Type grows with how little a beat carries; content centred (safe-centre, so it can't spill up) |
| 2 | B03, B10, 9:16 B03–B11 | **Overflow** once type grew: text over the matches strip, the heading and the source line | MAJOR (legibility) | 9:16 boost capped; a phone frame shows the newest 1–3 panel blocks; B03/B10 drop the matches strip (they aren't one of the three matches) |
| 3 | B01 | Code `(0.625).toFixed(2)` **wrapped mid-token** | MAJOR (accuracy of code on screen) | Code is sized to fit its column on one line, never wrapped |
| 4 | B07, B08 | **"SCRATCH RUN · NOT THE SHIPPED CODE" sat under the ORIGINAL column**, so it read as if the original were the scratch copy | MAJOR (honesty label) | The label moved under "MY COPY" |
| 5 | B08 | The narration says each change "fails on the company placed for it", but the **grid showed FXR and FXQ without "≠"** | MAJOR (picture ≠ claim) | FXR turns "≠" at "The threshold, on Romeo"; FXQ at "The rounding, on Quebec"; grid titled "where each change now fails" |
| 6 | B12 | **"↑ put one test exactly here" pointed at "your original"**, not the spot between the versions | MAJOR (clarity, closing image) | A dashed terracotta ring in the gutter, lit at "Find that one spot", with the caption centred under it |
| 7 | B02, B04 | Empty dashed circles read as **unfinished verdicts** (these rows are a rewrite, not a comparison) | MINOR | "→" for a port / a reading |
| 8 | B11 | Terracotta on "0 removed / 0 renamed" broke the accent grammar (terracotta = a difference) | MINOR | Ink |

Also: column titles that wrapped (B04, B05) shortened; code ligatures switched off (code renders as typed).

Checked and **not** findings:
- Every on-screen string matches FACTCHECK.md. Sources are on every frame except the closing question and the title card.
- The scratch-run beats (B07, B08) are labelled.
- No critique of the original anywhere; "waiting for review" and the fork no longer appear in narration or on screen.
- 9:16: the bottom 25% (Shorts UI) and top 12% stay clear.

**Left as is (your call):**
- B13's 16:9 title card is the shared outro scene (as shipped in W24): title top left, space below.
- The source lines cite the branch `Tanmay-Kulk/mycroft · add-contradiction-detection-recipe` as provenance.

**Not checkable on stills (next, on the first compile):** cue timing against the voice, motion and camera, the
per-frame luma scan (no black frames), loudness (−14 LUFS / −2 dBTP), 4K masters.

---

# PROOF on the 16:9 master (2026-10-04): `same-logic-two-languages-final.mp4`

| Check | Result |
|---|---|
| Resolution / length | 3840×2160, 270.9 s (13 beats, 12 holds of 0.3 s) |
| GATE V (compile.py, 26 frames) | first compile: 1 MAJOR, B12 at 50% filled 47% (only the heading up). Fixed: table and a rewrite note open with B12; re-rendered B12. Recompile: **0 BLOCKER · 0 MAJOR** |
| Dark frames (YAVG < 80, every frame) | **0 of 6,496** |
| Loudness | −24.6 → **−14.1 LUFS, −2.2 dBTP**. `normalise.py` now trims the shortfall with a ceiling at −2.6 dBFS and converges (the linear pass alone stopped at −15.0 / −1.9, as the topic video shipped) |
| Claims on screen when said | 41 frames, each 0.7 s after its cue, from the final file: every verdict, grid change and block is up as it's spoken |
| Captions | 92 cues, 0.68–4.87 s; numbers as written (0.625, 0.63…), "Mycroft" not "My-croft"; last cue ends 270.0 s |
| Skin lint | cold open / outro scene types (same notes W24 shipped with) |
| Minor, open | B12: the "↑ one test, standing exactly here" caption shows ~4 s before its ring lights (ring at "Find that one spot") |

---

# PROOF review: the Short's stills (9:16, 2026-10-04)

**Stage:** Short script draft 2 (Gate P PASS), audio locked (137.4 s, Whisper `medium.en`: all 9 beats as written).
Stills from the real props on the word clock: each beat's **end state** and its **opening frame**, so every cut can be
checked as one story (last frame of a beat against the first frame of the next).

**Verdict: 7 findings, all fixed. Ready for the Short render.**

| # | Beat / cut | Finding | Severity | Fix |
|---|---|---|---|---|
| 1 | all | **Underfill**: phone-native Short at the long film's 9:16 type size, lower half empty | MAJOR (fill) | Short type scale 1.3 on the sparse beats (S01, S05, S06, S09) |
| 2 | S02–S04, S07, S08 | 1.3 **overflowed** the dense beats into the source line | MAJOR (legibility) | Per-beat scale 0.95–1.0 on those five |
| 3 | S07 → S08 | **State lost at the cut**: S07 ends on both rows and 14 companies; S08 opened on an empty table and a ghosted grid | MAJOR (continuity) | S08's rows and 14 companies are on screen from frame 0; FXR, FXQ and the ≠ verdicts land at "and each one fails" |
| 4 | S06 → S07 | The two rows faded back in at S07's start | MINOR (continuity) | Carried from frame 0 |
| 5 | S05 | **Empty table for ~6 s** while "that told me almost nothing" is spoken | MAJOR (picture ≠ narration) | The three code pairs are up from frame 0 (the ≠ verdicts land at "like that rounding tie"); the thesis note "A match only means something…" arrives as it's said |
| 6 | S02 | **Empty table for ~10 s** under the Mycroft quote | MAJOR (picture ≠ narration) | The two ported nodes are up from frame 0; "→" lands at "rewrote its core logic" |
| 7 | S09 | "SAMPLE DATA ONLY" sat **under a blank space** reserved for the question table (it arrives 9 s in) | MINOR (layout) | Panel above the table in this beat |

Also: S01's name wrapped mid-phrase as a chip, so it's a text line now; S09's "↑ one test, standing exactly here" now
arrives with its ring (the scene fix made for B12).

Checked and **not** findings:
- Every on-screen string traces to FACTCHECK.md (the Short claims nothing new).
- The scratch-run label sits under "MY COPY" (S06–S08).
- Your name is in S01 and S09.
- Sources cite the recipe, not the branch.
- No overlaps; the top 12% and bottom 25% (Shorts UI) stay clear.

Open, minor: at the S07 → S08 cut the two rows' "=" give way to an empty gutter until "and each one fails" (the
re-run); the rows and companies themselves carry across.

---

# PROOF on the Short master (2026-10-04): `short/same-logic-two-languages-short-final.mp4`

| Check | Result |
|---|---|
| Resolution / length | 2160×3840, 140.1 s (9 beats, 8 holds of 0.3 s) |
| GATE V (compile.py, 18 frames) | **0 BLOCKER · 0 MAJOR** |
| Dark frames (every frame) | **0 of 3,357** |
| Loudness | −24.6 → **−14.2 LUFS, −2.4 dBTP** |
| Claims and cuts on the final file | 44 frames (each claim 0.7 s after its cue, plus both sides of every cut). One defect: **S09 at 14 s**, the name block stacked on the sample-data card, pushed the question table down into the source line, then the table jumped again at 16.8 s. Fixed: the card leaves as the name arrives, and a fixed-height panel keeps the table still. Re-rendered S09; re-checked through the beat at six points |
| Captions | 45 cues, 1.33–4.52 s; "Mycroft", numbers as written. One cue ended on "Quebec," (Kokoro pauses at the comma): moved into "Quebec, with a news average / of exactly 0.625.", timed to the spoken word (108.43 s) |
| Name | S01 and S09 |

---

# FINAL PROOF: both masters, as they ship (2026-10-04)

Reviewed on the final files (`same-logic-two-languages-final.mp4`, `short/same-logic-two-languages-short-final.mp4`)
and their captions, not on stills.

## Teaching rubric, re-scored on the finished films

| Criterion | 16:9 | Short | Why |
|---|---:|---:|---|
| Explicit framework | 2 | 2 | The idea is said and shown as it lands: "A match only tells you something if a mismatch could have shown up" (B05 / S05), with the three matches on a strip (16:9) |
| Reusable rubric | 2 | 2 | One portable question (B12 / S09): where could two versions differ, and is a test standing exactly there? Shown as the ring between "your original" and "your rewrite" |
| Worked example | 2 | 2 | Real runs on screen: 0.625 → 0.63 / 0.62, 16/16, the 14/14 that missed, FXR/FXQ turning ≠, the 13-vs-0 report/log (16:9) |
| Falsifiability / edge | 2 | 2 | My own changes went unnoticed (scratch run, labelled); sample data only, live mode declined |
| Active task | 2 | 2 | "Find that one spot, and make sure a single test is standing exactly on it" / "Put one test exactly there" |
| Friction | 2 | 2 | Two answers to one question; "Then it started to bother me"; "The comparison still agreed" |

**12/12 on both.** The Short carries the context on its own (what Mycroft is, what the detector does, invented
companies, answers written first, the limits), so a viewer who never sees the long film can follow it.

## Production

| Check | 16:9 | Short |
|---|---|---|
| Resolution · length | 3840×2160 · 4:31 | 2160×3840 · 2:20 |
| GATE V | 0 BLOCKER · 0 MAJOR (26 frames) | 0 BLOCKER · 0 MAJOR (18 frames) |
| Dark frames, every frame | 0 / 6,496 | 0 / 3,357 |
| Loudness | −14.1 LUFS · −2.2 dBTP | −14.2 LUFS · −2.4 dBTP |
| Claims on screen when said | 41 frames, all on time | 44 frames incl. every cut, all on time |
| Narration as written (Whisper `medium.en`) | 13/13 | 9/9 |
| Name | B02, B13 | S01, S09 |
| Accuracy / framing | every on-screen string traces to FACTCHECK.md; no critique of the original; no branch or "waiting for review" line; scratch runs labelled | same |

## Finding in this pass, fixed

| # | Where | Finding | Severity | Fix |
|---|---|---|---|---|
| 1 | captions, both | **Caption drift from the voice**: the long film's "So the question I couldn't put down was this." ended at 17.5 s though spoken to 18.2 s, and the next cue opened ~1 s before "If"; 4 cues under 1.2 s (as short as 0.68 s) | MAJOR (accessibility) | New `make_captions_words.py`: cues timed on the word clock the films are built on (it agrees with Whisper word timestamps to ~0.1 s); breaks at clauses and sentence ends, never opening on a sentence's tail; balanced two-line wrap; ≥ 1.2 s; no overlaps. Long 91 cues (1.25–5.00 s), Short 45 cues (1.29–5.63 s); all rules pass |

## Known, accepted

- Caption reading speed is ~20–25 characters per second because it follows Kokoro's measured pace (~3.4 words/s);
  slowing it would mean re-voicing.
- Style lint: cold open / outro scene types (the same notes Week 24 shipped with). B13's 16:9 title card kept as is (your call).
- Short S07 → S08: the two "=" give way to an empty gutter until "and each one fails" (the re-run).

**Verdict: both masters are clear to publish.**
