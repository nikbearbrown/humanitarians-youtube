# Frictional log — Overfitting, When a Perfect Score Lies

## 2026-11-22 — from topic to approved narration and clean previews

- **Drive:** https://drive.google.com/drive/folders/1SlLqr6rzO6sGKukxhy-S5gk-9tCDSl9a

**What I was working on.** A film on overfitting: why a model with zero training error can be memorizing noise. I directed the work in Claude Code with the brutalist.art toolkit: planning, narration approval, audio and low-res previews of the six Manim scenes. No 4K render this day.

**What I tried, and what I expected.**

- I chose the topic, the ai-explainer format and the default claude-liam branding. The title is "Overfitting, When a Perfect Score Lies"; the greeting is "Namaste, Liam".
- The plan was one film at a time: narration approval (GATE P), then audio (GATE 0), then low-res previews checked frame by frame.
- I expected the previews to land within ±3% of their audio and to pass GATE V's ≥55% canvas fill.

**Where it resisted, and what I did next.**

- **Pronunciation.** espeak read "Namaste" as /nˈæmæst/, dropping the last syllable. Claude pinned it to /nˈʌməstˌeɪ/; the whisper check transcribed it correctly, so no audio was regenerated.
- **Missing evidence.** `evidence.json` had no degree-15 curves for the B06 refits at n = 20, 100 and 1,000, and no per-trial outcomes for the B07 grids. Claude extended the demo before audio rather than refit inside the scene or invent a pattern; a key-by-key diff showed existing values unchanged.
- **Preview frames.** The B03 worked term ran off the right edge; B05 and B06 monospace text ran off-frame or collided; B07 titles overlapped; B02 and B07 openings were underfilled (B02 at about 47%). Claude fixed each and re-gated all six scenes: A 0 / W 0 / B 0.
- **Terracotta on text.** A main-session rule then moved terracotta off text and arrows, because GATE T §8.3 reads them as 2.74:1 on cream. Claude moved each beat's accent onto a shape, added ghost outlines for the empty B07 right grid at 50%, and re-rendered B02, B04, B05 and B07. The first B04 render was killed externally (exit 143) and re-run clean.

**What Claude contributed, and what I did with it.**

- **Script and evidence:** Claude wrote the narration (677 words) and `demo/overfit_demo.py`, ran it (about 7 s), and took every on-screen number from `demo/evidence.json`. `make_sheet.py` asserts every spoken figure against it. Its DOUBLE-CHECK pass made three corrections (FACTCHECK #1, #20, #22).
- **Audio and scenes:** Claude generated the Kokoro `am_onyx` audio (198.5 s), ran the whisper check and `align.py` (11/11 beats), and wrote `scenes.py` with six scenes, `B02_Setup` to `B07_PeekedScore`. Previews ran +0.31% to +1.06% against audio.
- Accepted:
    - **The narration as drafted, all 11 beats** ("approve all six" in the main session, one approval for the six planned films).
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - Degree 15 has 16 coefficients for 16 points, so it threads every one: training error 0, test error 9,882.6. Degree 3 scores 0.0586 and 0.0471.
    - Training error never goes up as the degree rises; test error bottoms out around degrees 3 to 6, just above the 0.04 noise floor, then climbs.
    - More data tames the same model: at 1,000 points degree 15 scores 0.0413 on test.
    - A score used to choose the model comes in optimistic 69.6% of the time; an untouched test set gives 55.2%, near the 53.3% control.
- Not understood / not verified:
    - Whisper flagged B03 "and" (heard "in") and B07 "Say" (heard "So") for a human listen. A listen is not recorded.
    - B07's first ~2 s fill about 57% of the height before "keep the best" lands. That was accepted as above the 55% bar.
    - The locked `ClaudeTitleOutro` may wrap the 38-character title as "Overfitting, When a Perfect / Score Lies."; that was accepted, not changed.

## 2026-11-23 — the B03 GATE T fix and the 4K final

**What I was working on.** Getting B03 through GATE T, then the 4K master and its final checks.

**What I tried, and what I expected.**

- I expected `./art run` and `./art final` to pass, and the master to carry no "B0x REMOTION" footer or bottom strip, a rule I set for every delivered film.

**Where it resisted, and what I did next.**

- **GATE T §8.1 failed on B03:** smallest text run 38 px, under the 41 px floor. Running GATE T's own blob code on the midpoint frame showed it was the hat accent on f̂. Enlarging the formula pushed it past title-safe, and a tighter spotlight box fused with the glyphs and triggered §8.3.
- **The fix:** the prediction is written f(xᵢ) without the hat, the tag "model's guess" names it, and the narration is unchanged. The worked-term line went from 48 to 60; the formula keeps 92 pt and its position. The 4K midpoint measured 56 px.
- **Then §8.3 flagged the wide terracotta spotlight box** at the midpoint. The moving spotlight is now ink, and terracotta is only on the final "MSE = 0" box. The midpoint test passed at 56 px and 10.04:1.
- **Hand QC:** the B03 spotlight box on "MSE" overlapped the "=". It was tightened to pad 0.16 and the settled frame verified clean.

**What Claude contributed, and what I did with it.**

- Claude diagnosed and fixed the B03 failures above, then ran the final: GATE V clean, GATE T PASS, strip check PASS on 99 samples, master check PASS, loudness PASS at −24.69 LUFS.
- Claude hand-checked every beat at 15/50/85% on the final.
- Accepted:
    - **The master** `exports/landscape/claude-liam-overfitting.mp4` (3840×2160, 24 fps, 3:19), matching `.verified.json`, status `ready`.
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - A single accent mark can fail a size gate. Removing the hat fixed the size without changing the narration.
    - A wide terracotta outline reads to GATE T as accent text, so the moving spotlight has to be ink.
- Not understood / not verified:
    - The master check skipped its duration clock check (`clock_check.py` not found).
    - `FACTCHECK.md` and `SOURCES.md` still list the demo hashes from before the extension.
    - The film is not published, and the Drive copy is still the earlier labelled review cut.
