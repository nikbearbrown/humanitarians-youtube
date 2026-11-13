# Feedback: "Color Never Hears the Music" — long film (16:9), rendered beats, review 3

**Rubric:** `PROOF.md` teaching rubric (six criteria, 0–2 each, /12) plus the binary production gate.
**Reviewed:** the 17 rendered 3840×2160 stills (B01–B13, `_stills/`), the mixed beat audio (`mp3/beat-*.mix.wav`), and measured checks from `proof_check_beats.py` (log: `_proof_check.log`). **No video exists yet**, so hold times, motion and fades are scored from the plan, not measured.
**Prior review:** `PROOF-REVIEW.md` (script level, 12/12).
**Verdict (after the fixes below, re-measured 2026-10-25):** teaching **12/12**; production gate **PASS on the stills**. **Public still waits on the video**, where the hold times, fades and loudness are measured. The first pass of this review (before the fixes) was unlisted-until-fixed: the gate failed on source lines crowding the bottom edge of five beats.
One line: this film delivers the two-scale method and a falsifiable task, but five of its source lines sit 6–20 px from the bottom edge of the frame, where a player bar can cover them.

## Rubric (on the rendered frames)

| Criterion | Score | Reason (frame) |
|---|---|---|
| Explicit framework | 2 | The strip is on screen from B01-a. It is small there (about 21% of frame height) and reads as a framework only when B02 outlines it with "two scales: happy to sad, strong to weak" and B04 enlarges it. All of that comes before the worked example (B05). Finding F4 below asks for a larger strip. |
| Reusable rubric | 2 | B05-b shows "1 rate the sound · 2 rate the color · 3 do they agree?"; B10-b shows the four-step card. Both are legible. |
| Worked example | 2 | B05-a and B05-b walk Bach and Brahms through the strip, with the dots, the swatches and the sky changing together. |
| Falsifiability / edge case | 2 | B07 shows "nonwestern scales: untested" with the US↔Mexico row; B10-a/B11 set a prediction the paper's chart can refute (B11 shows slow-minor, fast-minor and fast-major on shared axes, "between"). |
| Active task | 2 | B10-a: the 3×2 grid with the FAST-MINOR cell highlighted, two answer slots, a 6-s countdown ring; B10-b: the four-step card. |
| Friction | 2 | B01 shows two skies in an order that does not match the order played; B10-a shows two opposing arrows. |
| **Total** | **12/12** | |

## Production gate

| Check | Result |
|---|---|
| **Evidence legible at the moment of assertion** | **FAIL (placement), PASS (everything else).** Measured: the lowest ink sits at 2139–2149 px of 2160 (about 6–10 px logical from the bottom edge) on **B03-a, B05-b, B07, B09, B11**, and at 2081 px (about 40 px logical) on most of the rest. The cause is two-line source captions wrapped near the bottom. A player bar or caption overlay can cover them. Contrast is fine: INK 10.98, INK_SOFT 4.73, SPARK_TEXT 4.70 against cream, all ≥ 4.5. Margins on the left, top and right are ≥ 60 px everywhere. |
| Sources on screen, not just voiced | PASS: every beat has a source line, in pixels, except B13, which carries its source in the text column. B10-a's source sits higher on the page than the others (inconsistent, not missing). Figures spoken are asserted on screen by the builder's checks (.97, .99, .96, .89; 97; 18; 37; 2011; 60; 9; etc.). |
| Side-by-side at the moment of comparison | PASS by arrangement: B01-b (two skies), B04 (four rows), B07 (two contexts + the US↔Mexico row), B08 (two strips), B09 (three columns), B11 (three points per axis). **Held ≥ 2–3 s is not measurable on stills**; it is set in the plan and must be measured on the video. |

## The problem

**The source band is too low on five beats** (B03-a, B05-b, B07, B09, B11). The sources are the film's receipts, so they have to be fully inside the safe area, not touching the edge.

## Findings and punch list

1. **[EDIT] Raise the source band** so the last baseline is no lower than y 1000 of 1080 (about 74 px from the bottom edge) on every beat, and make the two-line captions one line wide or shorter. Re-run `proof_check_beats.py`; target: lowest ink ≤ 2080 px on every still. (Fixes the gate.)
2. **[EDIT] B04 label "no direct link needed"** is stronger than the narration, which says the paper doesn't rule a direct link out. Reword it (for example "through feeling") or remove it.
3. **[EDIT] Footer position** is inconsistent (B10-a's source sits higher than the rest). Put every source line on one baseline.
4. **[EDIT] Enlarge the strip** (about 230 px logical in the lower-left) and the 24–28 px captions; the strip is the film's method and is small on every beat. Nothing is clipped; this is about how it reads at YouTube size.
5. **[EDIT] B13** has no source band by design; fine. The redesigned end card (full-colour skies, title, study line) was re-viewed and reads cleanly.
6. **Not yet measured (needs video):** fades (Week 27's lesson: whole-fill fades can render a black frame 0), the 3 s holds, the 6-s countdown, B01's clip A/B timing against the tunes in the audio, audio loudness on the compiled master (stage-1 mixes sit at about −16 to −17.5 LUFS), and audio-to-picture sync.

## Audio observations (measured)

- Narration reads at **3.1–3.9 words per second** within beats (B01 3.91, B08 3.79, B12 3.74, B06 3.72) with 0.4–0.5 s of tail between beats. That is brisker than the 3.3 planning rate. If it feels fast on a listen, the lever is Kokoro's speed (1.0 → about 0.92), applied to both formats so they match.
- The tunes are in the holds of B01 (8 s quick, 8 s slow, 3 s pick) and B12 (4 s, 4 s). Whisper on B04/B07 heard the words as written ("rated", "adds") with normal numeral/spelling differences only.

## What works

- Every frame has one idea, a headline in serif, and a source line; no beat carries more than about six elements.
- The two skies carry the film's argument visually (B01-b → B12), and B12 is the exact swap of B01.
- The numbers on screen match the paper and the FACTCHECK table, and B11 is labelled approximate.

## Do next

1. [EDIT] Findings 1–4, re-render the five flagged stills (and B04, B10-a), re-run `proof_check_beats.py`.
2. Encode the beats as video and measure the items in finding 6.
3. Re-run this review on the video; the gate can then pass.

## Re-check after the fixes (2026-10-25)

Tanmay approved the long-film fixes; they were applied in `build_long_stills.py` and every still was re-rendered. Re-measured with `proof_check_beats.py`:

| Finding | Result |
|---|---|
| 1. Source band too low | **Fixed.** Every caption starts at x 520 and ends on one baseline (y 996 of 1080). Lowest ink is now 2047–2058 px of 2160 on every still (was 2139–2149 on five beats). Long flags: **0**. |
| 2. B04 label | **Fixed.** Now "through feeling". |
| 3. Footer inconsistent | **Fixed.** B10-a's source now sits on the common baseline. B13 has none by design. |
| 4. Strip and captions small | **Fixed.** Strip 300 px logical (was about 230), labels 28 px; every sans caption at least 28 px. Contact sheet and B03-a, B07, B09, B11 viewed at full size: nothing collides or clips. One caption (B03-a's source) wraps after "48 US +"; it reads fine but is not ideal. |
| 5. B13 | Unchanged (clean end card). |
| 6. Needs video | Still open. |

Production gate now: evidence legible PASS (sources inside the safe area, contrast ≥ 4.5), sources on screen PASS, side-by-side PASS by arrangement. **Hold times (≥ 2–3 s) remain unmeasured until the video exists.**
