# Frictional log — Why Neural Networks Need a Bend

## 2026-11-22 — from topic to approved narration and clean previews

- **Drive:** https://drive.google.com/drive/folders/1SlLqr6rzO6sGKukxhy-S5gk-9tCDSl9a

**What I was working on.** A film on why a neural network needs a bend (a ReLU) between its layers. I directed the work in Claude Code with the brutalist.art toolkit: planning, narration approval, audio and low-res previews of the nine Manim scenes. No 4K render this day.

**What I tried, and what I expected.**

- I chose the topic, the ai-explainer format and the default claude-liam branding. The planning session picked the title; the greeting is "Jambo, Liam".
- The plan was one film at a time: narration approval (GATE P), then audio (GATE 0), then low-res previews checked frame by frame.
- I expected the previews to land within ±3% of their audio and to pass GATE V's ≥55% canvas fill.

**Where it resisted, and what I did next.**

- **Length.** The draft was 840 words, about 4.0 min at 3.51 words/s. Claude offered two trims (B10, −68 words; B04, −67 words). I approved the narration as drafted, all 14 beats, B10 kept. Measured audio came out at 251.7 s.
- **Pronunciation.** espeak spelled out ReLU and XOR and got numpy and Jambo wrong. Claude pinned all four in IPA; the whisper check heard them as intended, so no audio was regenerated.
- **Preview frames.** B07 matrices bled right; B02, B07 and B09 underfilled at 50%; B08 band contrast was too low; B06 bar values collided; the t-axis struck through the B10 equations. Claude fixed each, and GATE V on the previews gave 0 BLOCKER, 0 MAJOR.
- **B02 bottom strip.** It landed 0.19 s after "A network alternates". I asked to remove the bottom strip. Claude removed it and boxed "bend" in the ReLU header instead; B02 re-checked at −0.2% against its audio.

**What Claude contributed, and what I did with it.**

- **Script and evidence:** Claude wrote the narration and `demo/nonlinearity_demo.py`, ran it (about 60 s), and took every on-screen number from `demo/evidence.json`. Its DOUBLE-CHECK pass made five corrections (FACTCHECK #2, #3, #23, #28 and the B00 result line).
- **Audio and scenes:** Claude generated the Kokoro `am_onyx` audio, ran the whisper check and `align.py` (14/14 beats), and wrote `scenes.py` with nine scenes, `B02_TwoMoves` to `B10_StraightAgain`. Gates A, W and B were 0 for all nine.
- Accepted:
    - **The narration and title as drafted** ("approve all six" in the main session; "Approve as drafted" in this one).
    - **The pinned pronunciations** for ReLU, XOR, numpy and Jambo.
- Rejected:
    - **The optional trims of B10 and B04.** The narration was approved with all 14 beats, B10 kept.
    - **The B02 bottom strip.** At my request it was removed and replaced by a boxed "bend".

**What I understand now, and what I still do not.**

- Understood:
    - Two straight layers are one layer in disguise: on the seed-0 matrices both paths give (7, 8), and ten layers match one matrix to 8.88×10⁻¹⁵.
    - No line separates XOR; the best of 115,560 lines gets 3 of 4. A two-layer net with no bend stalls at loss 0.25.
    - The bend is necessary, not sufficient: 18 of 100 two-unit runs find XOR, 91 of 100 with eight units.
    - Spotlights are boxes, not underlines: an underlined "−" reads as "=".
- Not understood / not verified:
    - Whisper flagged B02 "flatten negatives" (heard "flat negatives") and B04 "Add a shift" (heard "At a shift") for a human listen. A listen is not recorded.
    - The locked `ClaudeTitleOutro` may wrap the 31-character title; that was accepted, not changed.

## 2026-11-23 — the 4K final

**What I was working on.** The 4K master and its final checks.

**What I tried, and what I expected.**

- I expected `./art run` and `./art final` to pass, and the master to carry no "B0x REMOTION" footer or bottom strip, a rule I set for every delivered film.

**Where it resisted, and what I did next.**

- **The strip check.** The absolute-darkness version falsely flagged the dark-polarity outro (t = 248 s and 250 s). The background-relative version, which checks the label corner and the full bottom band, passed on 126 samples.
- **Hand QC.** The B03 "x" looked garbled at 85%. It is a mid-Write frame and settles correctly, so nothing changed.

**What Claude contributed, and what I did with it.**

- Claude ran the build chain: `./art run` exit 0, GATE V clean on 28 frames, GATE T PASS, `./art final` exit 0. Master check PASS; loudness PASS at −24.67 LUFS.
- Claude hand-checked every beat at 15/50/85% on the final.
- Accepted:
    - **The master** `exports/landscape/claude-liam-nonlinearity.mp4` (3840×2160, 24 fps, 4:12), hash matching `.verified.json`, status `ready`.
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - A strip check must compare against the background, or a dark outro reads as a strip.
    - GATE T passed with one advisory: the verdict narration recites its card (0.94).
- Not understood / not verified:
    - The master check skipped its duration clock check (`clock_check.py` not found).
    - The film is not published, and the Drive copy is still the earlier labelled review cut.
