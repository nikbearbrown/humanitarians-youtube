# Frictional log — Bayes' Theorem: The Positive That's Usually Wrong

## 2026-11-22 — planning to the narration gate, then audio and previews

- **Drive:** https://drive.google.com/drive/folders/15iGSsUDIPzx1JctBB2fqOnfMBC_9GrnE

**What I was working on.** A film on Bayes' theorem through one medical test, planned in the TL;DR format up to the narration gate, then audio, scene code and low-res previews. No 4K render yet.

**What I tried, and what I expected.**

- The starting framing was a "99%-accurate test" that is usually wrong. I expected that to be a fair description.
- I expected a 1,000-person grid to be enough.
- I expected the film to run about 5.5 min (the 2.6 w/s estimate).
- I expected Kokoro's numbers to be heard clearly.

**Where it resisted, and what I did next.**

- **99% is the sensitivity, not the accuracy.** With 95% specificity the test is right 95.04% of the time overall. The narration now says "catches 99% of cases", and the title moved from the test being usually wrong to **the positive** being usually wrong.
- **1,000 people gives 9.9 and 49.5 people.** The demo asserts whole counts, so the population became 10,000.
- **Whisper heard "sick" after a number as "six":** B15 "Ninety-nine sick." came out as "996", and B13 as "106". In a film about counts that is a real risk. The lines were reworded ("who are sick", "have the disease"), regenerated and re-aligned. B17's "…zero five nine four: one sixth" ran together, so the colon became a full stop.
- **At 480p the 100 sick, drawn as a row, read as a hairline.** They became a 10 × 10 block, and B13's "for this row" became "for this block".
- **The grid failed GATE V's contrast at the skill's DIM colour** (0.277 against 0.30). DIM moved to #7A7E86.
- Measured audio came to 265.98 s (4:26). All ten previews landed within +0.0 to +1.1% of their audio.

**What Claude contributed, and what I did with it.**

- **Source and fact-check:** Claude wrote `SOURCE.md` with 7 references and `FACTCHECK.md`. The Casscells 1978 figures were confirmed through the Manrai 2014 replication; the NEJM full text was not opened (paywalled).
- **Evidence:** Claude wrote `demo/bayes_demo.py` with exact `Fraction` counts and a 100,000-person simulation (P(D|+) = 0.1669 against the exact 1/6).
- **Script, audio and scenes:** Claude drafted the narration, generated the Kokoro audio, ran the whisper check and alignment, wrote `scenes.py` (B10–B19, the grid as 80 row objects rather than 10,000 squares) and ran gates A, W and B.
- Accepted:
    - **GATE S: one section, S1 "Count the Positives".** I approved it with "approve all six" in the main session.
    - **The narration as drafted (GATE P, 860 words)**, in the same message.
    - **The title "Bayes' Theorem: The Positive That's Usually Wrong"**, in the same message. FACTCHECK had left it as an open question.
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - The 99% is the chance of a positive given disease. My question is the chance of disease given a positive. They are different numbers.
    - Counting people makes the gap visible: 99 sick positives against 495 healthy ones.
    - The audio check has to catch words that a listener can mishear as numbers, not only bad pronunciation.
- Not understood / not verified:
    - Whisper heard "Bayes" as "base" or "bass". Kokoro's phonemes are correct, so no pin was added; this is whisper's guess, not a human listen.
    - The four narration edits came after GATE P. They were flagged for my review that day.

## 2026-11-23 — approving the edits, and a blank beat every gate passed

- **Drive:** https://drive.google.com/drive/folders/15iGSsUDIPzx1JctBB2fqOnfMBC_9GrnE

**What I was working on.** Approving the post-GATE-P narration edits and getting the first final master.

**What I tried, and what I expected.**

- I expected a master that passed every gate to show what the narration describes.

**Where it resisted, and what I did next.**

- **Two cues ran 0.11 s late** (B14, B18). Their opening moves were shortened from 0.8 to 0.65 s, and both beats were re-gated.
- **B12 was blank from about 45% to the end.** The first final passed GATE V, GATE T, the strip check (133/133), the master check and loudness (−24.66 LUFS). But in B12 the sick block, the "you" badge, the scan bar and all 495 false-alarm marks were invisible, so "light up" showed nothing.
- **Cause:** ManimCE's `play()` adds the row animations to the top of the draw order, so the cleared rows were painted over everything added earlier. The fix was `set_z_index(1)` on those objects before the sweep. The blank clips are in `_superseded/`, and the full queue was re-run.
- The new final was 266.3 s and passed every gate again. Hand QC showed the B12 marks visible and continuous into B13.

**What Claude contributed, and what I did with it.**

- **Re-verification:** after the usage-limit reset, Claude re-ran gates A, W and B on all 10 scenes and re-rendered B10 and B17 so every preview matched the current `scenes.py`.
- **Hand QC and diagnosis:** Claude checked the 15/50/85% contact sheets by hand, caught the blank B12, found the draw-order cause and made the fix.
- Accepted:
    - **The four post-GATE-P narration edits** (B13 twice, B15, B17). I wrote "Approve the edits" in the main session.
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - The gates check fill, contrast, type, strips and loudness. None of them checks that the right objects are on screen. Only looking at the frames caught B12.
    - In Manim, draw order follows when an object is added to the scene, so a late animation can cover earlier objects.
- Not understood / not verified:
    - The §8.10 card-recital advisories and the TL;DR skin lint were left as advisories; they do not block the cut.

## 2026-11-24 — converting the film to the ai-explainer format

- **Drive:** https://drive.google.com/drive/folders/15iGSsUDIPzx1JctBB2fqOnfMBC_9GrnE

**What I was working on.** Making this film match the other five: the ai-explainer spine, with no footer.

**What I tried, and what I expected.**

- I asked for this film to match the other five. That meant replacing the TL;DR opening (What, Why, Question, Terms) with the ai-explainer cold open and summary.
- I expected the body, including the B12 fix, to carry over unchanged.
- I expected the new B01 to pass at fontSize 145.

**Where it resisted, and what I did next.**

- **The Terms card defined sensitivity and base rate.** Those definitions now sit in B00's on-screen answer lines ("sensitivity: the test catches 99 of every 100 sick people"; "base rate: only 1 in 100 people have the disease"), and B01's narration defines base rate. The four TL;DR beats are in `_superseded/format-tldr/`.
- **B01 measured 49% fill at fontSize 145** before render. It was re-rendered at 160, which measured 59%. The 145 clip is in `_superseded/b01_underfill/`.
- The final is 223.7 s (3:43): GATE V 0/0, GATE T PASS, bookend PASS, strip check 112/112, master PASS, −24.61 LUFS.

**What Claude contributed, and what I did with it.**

- **New opening:** Claude wrote the B00 `ClaudeComposerAsk` cold open and the B01 `BrutalistHesitantWriter` narration, and ran `stem-films/tools/convert_to_ai_explainer.py`.
- **Render and QC:** Claude resized B01, ran every gate, checked all 15 beats by hand, and copied the master to my "Footer removed" folder.
- Accepted:
    - **The new B00 and B01 narration (GATE P), as previewed,** approved in chat on 2026-11-24.
    - **"Hello" as the greeting,** in place of "Salaam", for all three converted films. My choice.
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - The terms a Terms card defined have to land somewhere else when the card goes; here the cold open carries them.
    - The film is 42.6 s shorter than the TL;DR cut (266.3 s → 223.7 s).
- Not understood / not verified:
    - The Drive copy is still the earlier labelled review cut; it has to be replaced with the clean master.
    - GATE T still gives a §8.10 advisory on BVDT (narration recites the card, 0.86). It does not block the cut.
    - `SCRIPT.md` and `SHOTLIST.md` in the film folder still show the TL;DR B00–B03; the current narration is in `beat_sheet.json`.
    - The film is not published.
