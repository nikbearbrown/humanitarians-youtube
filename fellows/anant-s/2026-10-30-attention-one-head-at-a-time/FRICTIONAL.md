# Frictional log — Attention, One Head at a Time

## 2026-11-22 — planning to the narration gate, then audio and previews

- **Drive:** https://drive.google.com/drive/folders/15iGSsUDIPzx1JctBB2fqOnfMBC_9GrnE

**What I was working on.** A film on one attention head, planned in the TL;DR format up to the narration gate, then audio, scene code and low-res previews. No 4K render yet.

**What I tried, and what I expected.**

- I expected the toolkit to hold a beat for a set lead or tail silence.
- I expected Kokoro to say the greeting ("Konnichiwa") and "numpy" correctly.
- I expected the film to run about 5.1 min (the estimate from 1,035 words).

**Where it resisted, and what I did next.**

- **There is no hold field.** `compile.py` sizes each beat from its measured audio, and `lead_silence_s` / `tail_silence_s` are not read anywhere under `runtime/`. The main session added `stem-films/tools/pad_silence.py`, which padded B02 (0.8 s lead), BVDT (0.5 s lead) and BOUT (1.0 s tail) into the mp3s.
- **Two words phonemized wrong:** "Konnichiwa" came out as KAH-nish-iwa and "numpy" as /nˈʌmpi/. Both were pinned in the lexicon; the whisper check then heard them correctly.
- `beat_lint` **crashed** reading UTF-8 as cp1252 in a shell without `env.sh`. The gates were re-run from the toolkit root with `env.sh` sourced.
- **Frame QC on the previews** found captions crossing the value-plane frame (B11, B12, B19), an overflowing row and raw "d_k" text in B17, weights showing as "0.6", a unicode "−" that broke LaTeX in B16, and outputs that looked like values in B19. Each was fixed in `scenes.py`.
- Measured audio came to 301.98 s (5:02). All ten Manim previews landed within ±3% of their audio (max +0.85%, B10).

**What Claude contributed, and what I did with it.**

- **Source and fact-check:** Claude wrote `SOURCE.md` and checked it against arXiv:1706.03762 (§3.1, §3.2.1, §3.2.2, §3.5). Five draft lines were corrected, e.g. "a weighted average of all the words" became "of what all the words carry", because the average is over values.
- **Evidence:** Claude wrote `demo/attention_demo.py` (numpy, seed 290537, chosen by a search for legible numbers) and made every on-screen number come from `evidence.json`. It chose d_v = 2 so values and outputs could be drawn as points, and marked that on screen.
- **Script, audio and scenes:** Claude drafted the narration, generated the Kokoro audio, ran the whisper check and alignment, wrote `scenes.py` (B10–B19) and ran gates A, W and B.
- Accepted:
    - **GATE S: one section, S1 "One Head, by Hand".** I approved it with "approve all six" in the main session.
    - **The narration as drafted (GATE P)**, in the same message.
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - The head only sees the four words; chase moves because its weights over the other words change, not its own numbers.
    - The output is a weighted average of value points, so it always lands inside their shape. Equal weights put every word on the same point.
    - Lead and tail silences have to be baked into the audio; the renderer will not add them.
- Not understood / not verified:
    - Whisper heard BVDT "root d k" as "root, decay" and BHTF "Paste this" as "pace this". They were flagged for a human ear; no listen is recorded.
    - CHECKS-REPORT flags an open question: 10 LEARN beats in one section, where a strict reading of the density rule would fold B19 into B18. No decision is recorded; B19 stayed.

## 2026-11-23 — GATE T at 4K, and the first final

- **Drive:** https://drive.google.com/drive/folders/15iGSsUDIPzx1JctBB2fqOnfMBC_9GrnE

**What I was working on.** Getting the scenes through GATE V and the 4K GATE T, then the first final master.

**What I tried, and what I expected.**

- I expected scenes that were clean at preview size to pass at 4K.
- I expected a terracotta box around a row to count as a shape, not as text.

**Where it resisted, and what I did next.**

- **No terracotta on text.** The series' main session set this rule after backprop's export was blocked by GATE T §8.3 (terracotta on cream is 2.74:1). Request rows and labels became ink, with terracotta only on dots, rings and boxes.
- **The local GATE V check failed six beats:** underfill on B12, B16, B17 and low contrast on B13, B14, B15, B19. Pale strokes and tints counted as ink and pulled the contrast toward the page. Structural strokes moved from GHOST to SOFT, the heat-map tint dropped from 0.55·w to 0.45·w, and B12/B16/B17 got content visible by the 50% sample. All 20 samples were then clean (minimum coverage 0.67).
- **The 4K build failed §8.3 on B10, B12, B15, B17:** wide terracotta boxes were read as low-contrast text. They became ink, and each beat's terracotta moment moved to a compact mark. At 4K the four midpoints measured 7.65–10.02:1.
- **Rebuild 1 failed two more checks:** the old B00/B01 heading overhung title-safe by 1 px (fixed in the toolkit by the main session), and a wide ink spotlight ring in B17 read as a text run (§8.6b). `box()` now keeps rings at most 1.4× as wide as tall, so every Manim clip was re-rendered.
- **A process mistake:** while resuming after a usage-limit pause, Claude killed a manim process (PID 1402) that belonged to another session's preview of the overfitting film. That preview needs a re-render.
- The first final was 302.4 s and passed GATE V, GATE T, the strip check (151 samples), the master check and loudness (−24.73 LUFS).

**What Claude contributed, and what I did with it.**

- **Diagnosis:** Claude traced the contrast failures to the check's background estimate (the page binned as 248, 248, 248), which made a 0.25-weight tint count as pale content.
- **Fixes:** all edits were in `scenes.py`; no validator was changed. Claude rendered B10, B12, B15 and B17 at 4K and ran `type_check` on each midpoint.
- **Hand QC:** Claude checked every beat at 15/50/85%. A garbled B12 header at 85% is a morph frame and settles.
- Accepted: none recorded for this day. The terracotta rule came from the series' main session, not from me.
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - The type gate reads any wide coloured shape as possible text, so accent colour belongs on compact marks.
    - A pale stroke can hurt a contrast check more than leaving it out.
- Not understood / not verified:
    - B13 and B16 were not checked at 4K at this stage; only their -ql checks were clean.
    - B15 has one cue 0.11 s late at t = 1.35 (cosmetic).

## 2026-11-24 — converting the film to the ai-explainer format

- **Drive:** https://drive.google.com/drive/folders/15iGSsUDIPzx1JctBB2fqOnfMBC_9GrnE

**What I was working on.** Making this film match the other five: the ai-explainer spine, with no footer.

**What I tried, and what I expected.**

- I asked for this film to match the other five. That meant replacing the TL;DR opening (What, Why, Question, Terms) with the ai-explainer cold open and summary.
- I expected the body, Verdict, Your Turn and outro to stay as they were.
- I expected the new B01 to pass at its first size.

**Where it resisted, and what I did next.**

- **The Terms card went away.** It had defined embedding, dot product and softmax. Each of those is also defined inline in the body (B11, B12, B14), so nothing taught was lost. The four TL;DR beats are in `_superseded/format-tldr/`.
- **GATE V failed B01 on underfill:** 45% at fontSize 130. B01 was re-rendered at fontSize 145, lineSpacing 3.3, which measured 59%. The old clip is in `_superseded/b01_underfill/`.
- The final is 261.0 s (4:21): GATE V 0 blockers / 0 majors, GATE T PASS, bookend PASS, strip check 131/131, master PASS, −24.72 LUFS.

**What Claude contributed, and what I did with it.**

- **New opening:** Claude wrote the B00 `ClaudeComposerAsk` cold open and the B01 `BrutalistHesitantWriter` narration, and ran `stem-films/tools/convert_to_ai_explainer.py`.
- **Render and QC:** Claude re-rendered, fixed the B01 fill, ran every gate, checked all 15 beats by hand, and copied the master to my "Footer removed" folder.
- Accepted:
    - **The new B00 and B01 narration (GATE P),** approved in chat on 2026-11-24.
    - **"Hello" as the greeting,** in place of "Konnichiwa", for all three converted films. My choice.
- Rejected: none recorded.

**What I understand now, and what I still do not.**

- Understood:
    - The body could stay untouched because it already defines its terms where they are used.
    - The fill check measures canvas area, so a two-line card needs larger type to pass.
    - The film is 41.4 s shorter than the TL;DR cut (302.4 s → 261.0 s).
- Not understood / not verified:
    - The Drive copy is still the earlier labelled review cut; it has to be replaced with the clean master.
    - GATE T still gives a §8.10 advisory on BVDT (narration recites the card, 0.84). It does not block the cut.
    - `SCRIPT.md` and `SHOTLIST.md` in the film folder still show the TL;DR B00–B03; the current narration is in `beat_sheet.json`.
    - The film is not published.
