# Frictional log — Softmax and Temperature, Explained

## 2026-11-22 — planning, narration, audio and low-res previews

- **Drive:** https://drive.google.com/drive/folders/1w-Bz0R9QjZE2HX4Egg_fujYbSnVPtRb2

**What I was working on.** Film 2 of 7 in the series: why the same prompt gives a different answer every time. I picked the topic, the ai-explainer format and the default claude-liam branding. Claude Code, using the brutalist.art toolkit, planned the beats, wrote the script and the evidence demo, then built the audio, `scenes.py` and low-res previews.

**What I tried, and what I expected.**

- I asked for the math "with real numbers" and expected real logits from a model.
- I expected the narration gate (GATE P) to be the only stop before audio.
- I expected a sampling check on 10,000 draws to land on the predicted shares.

**Where it resisted, and what I did next.**

- **No real model can run in a pure-numpy demo.** Claude constructed the logits and labelled them on screen (B02, B09), and listed real GPT-2 logits as an open question: it would need a model download plus torch/transformers.
- **The first 10,000-draw check missed by 3.4 σ at T = 2** (mat 33.4% against 35.0%). Other seeds landed within 0.3 points, so it was a seed outlier. Claude switched to the sampler the film shows (inverse CDF, one seeded stream) and recorded that the change came after seeing the result (BUILD-LOG, FACTCHECK #18). The new largest gap is 0.76 points.
- **Audio was blocked.** The session's permission classifier denied `generate_audio_kokoro.py`, because the go-ahead had come from another session, not from me. Claude did not work around it. I wrote "Yes, run audio" directly in that session.
- **"called a logit" came out "called AY logit".** Claude added a `metadata.pronounce` key for "a logit" and regenerated B02; whisper then heard "low jit".
- **B05 overran by 0.54 s.** Manim floors static waits and ceils plays, so frames were gained or lost per call. Claude changed the clock; every clip now lands within one frame of its audio.

**What Claude contributed, and what I did with it.**

- **Script and evidence:** Claude drafted all 13 beats (751 words, about 3.6 min) and wrote `demo/softmax_demo.py`; `make_sheet.py` asserts every spoken number against `evidence.json`. Five DOUBLE-CHECK corrections went into FACTCHECK.
- **Build:** Kokoro audio, whisper check, alignment (13/13, 0 fallbacks), eight Manim scenes, Gates A/W/B, and previews checked at 15/50/85/99%.
- Accepted:
    - **The narration as drafted, all 13 beats.** I approved it in the main session with "approve all six".
    - **Constructed, labelled logits**, and the Sydney/Canberra example in B09.
    - **The title** "Softmax and Temperature, Explained".
- Rejected:
    - **Real GPT-2 logits** (offered as open question 2).
    - **Trimming B07 or B08** to shorten the film.
    - **The alternative title** "Same Prompt, Different Answer".

**What I understand now, and what I still do not.**

- Understood:
    - Softmax with temperature divides the logits first, so it changes the spread but never the order.
    - A check that could have failed is worth more than one that couldn't, and changing its method after a bad result has to be written down.
- Not understood / not verified:
    - How messy a real model's top-5 would look; the film uses constructed logits only.
    - Whisper-base still writes "logit" as "alloget"; the phonemes are /ˈloʊdʒɪt/, but no human listen is recorded.
    - B02's "loop runs again" cue lands 0.15 s late; it was accepted as cosmetic.

## 2026-11-23 — 4K gate failures, fixes and the final master

**What I was working on.** Getting the 4K cut through GATE V and GATE T, then producing the final master.

**What I tried, and what I expected.**

- I expected scenes that passed Gates A, W and B at low resolution to pass GATE V and GATE T at 4K.

**Where it resisted, and what I did next.**

- **GATE T failed** at the midpoints of B03, B05, B08, B09 (§8.3, terracotta read as text) and B02, B06 (§8.6b, closed outline around text). Claude read `type_check.py` and `final_frame_check.py` to see what they count as a text run, then changed the accent pattern: a GHOST outline plus one terracotta dot, INK/SOFT strips with labels below, GHOST boxes in B02.
- **GATE V failed** on B06 (underfill 45%, low contrast 0.17 and 0.20) and on B01. B06 was re-laid at full width (fill at 50% now 61%). B01's hesitant writer went to fontSize 190, lineSpacing 3.0 (fill 63%).
- **Hand QC found the B03 exponent spotlight cutting into the "e".** Both exponent spots now use pad 0.05; the 4K midpoint passes all GATE T checks.
- All 32 frames (15/50/85/99% of B02–B09) were run through both checks at 4K and passed.

**What Claude contributed, and what I did with it.**

- **Diagnosis and fixes:** Claude found the main session's B06 description matched B08, and fixed each scene by its actual content. It moved the old clips to `_superseded/manim-2026-11-23-gateT/` so the 4K re-render started clean.
- **Final and QC:** Claude built the master and ran GATE V, GATE T, the strip check, master check and loudness, plus hand QC at 15/50/85% of every beat. I reviewed the result.
- Accepted:
    - **The B01 and B03 fixes** made in the main session (fontSize 190 / lineSpacing 3.0; spotlight pad 0.05).
    - **The final master**, 237.0 s, sha256 matching `.verified.json` (`ready`). It meets my rule of no "B0x REMOTION" footer or bottom strip in a delivered video: the strip check passed on 119 samples.
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - GATE T treats any INK or MUTE blob 1.5–15× wider than tall as text, so a terracotta bar fails as "accent text" and an outline around a bar fails as overlap.
    - GATE V's contrast is the mean ink colour against the page, so large light fills drag it down.
- Not understood / not verified:
    - GATE T's §8.10 advisory says the BVDT narration recites its card (0.94); it does not block the cut and was not changed.
    - Master check skipped its clock step (`clock_check.py` not found).
    - The film is not published; the Drive copy is still the labelled review cut.
